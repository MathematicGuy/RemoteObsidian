+ ! remember to filter NULL
**references:**
+ [invoice information extraction](https://medium.com/analytics-vidhya/invoice-information-extraction-using-ocr-and-deep-learning-b79464f54d69)
+ [id card infor extraction website](https://github.com/liemkg1234/WebOCR_identitycard?tab=readme-ov-file)
+ [image alignment guide](https://viblo.asia/p/pytorch-tutorial-3-alignment-anh-chung-minh-thu-voi-pytorch-huong-dan-de-nhu-an-keo-4dbZNJ8mZYM) 
+ [image detection using tensorflow v2 api](https://viblo.asia/p/chinh-phuc-bai-toan-object-detection-voi-tensorflow-v2-api-trong-5-phut-1VgZvMRrKAw)

![[Pasted image 20241212142019.png]]
Later: 
Improve Model prediction with different lighting (Augment in Roboflow, minimize manual labeling by choosing 4-5 different diff lighting condition then augment them to simulate more lighting condition)
+ Apply NMS later
+ Add Earepisodely Stopping
+ Gather a lot of image for auto labeling using pre-trained model  -> add this dataset with label to the processed main dataset (in my pre-processing lab)
+ Test and Detect Text Clarity
+ Compare current image pre-processing method with canny (How to reduce the vietname circle crest behind the text)
+ Summarize data using Summarization Model.  

Plan: 


Train New YOLO Model with Greyscale pre-processing
Load New Model to my Detection Anomaly and Modify it into ID Card Detection Project

Test: 
Initialize Perspective Transform
Train Text Detection Model (VietOCR)




---

**Run Detection Model**
```python
import cv2
from ultralytics import YOLOv10

# Load the YOLOv10 model
model = YOLOv10(f'{HOME}/weights/yolov10n.pt')

# Open a connection to the webcam (0 for the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform inference on the current frame
    results = model(source=frame, conf=0.25)
    
    # Render the results on the frame
    frame_with_results = results.render()[0]
    
    # Display the frame with detections
    cv2.imshow('YOLOv10 Live Detection', frame_with_results)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

```

**Return Detection Result in dictionary format**
```python
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    """
    Perform object detection on an uploaded image with preprocessing.
    """
    try:
        # Load the uploaded image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_np = np.array(image)[:, :, ::-1]  # Convert PIL image to BGR NumPy array

        # Preprocess the image (including resizing)
        preprocessed_image = preprocess_frame(image_np)
        
        # Perform object detection with YOLO
        results = model(preprocessed_image, conf=0.4)

        # Process results
        detections = []
        for result in results:
            for box in result.boxes:
                bbox = box.xyxy.tolist()[0]  # Bounding box coordinates [x1, y1, x2, y2]
                confidence = box.conf.tolist()[0]  # Confidence score
                class_id = int(box.cls.tolist()[0])  # Class ID
                detections.append({
                    "class_id": config['names'][class_id],
                    "confidence": confidence,
                    "bbox": bbox
                })

        # Annotate the image with bounding boxes
        annotated_image = annotate_image(preprocessed_image, detections)

        # Save the annotated image to a file
        original_filename = file.filename
        save_filename = f"processed_{os.path.splitext(original_filename)[0]}.jpg"
        save_path = os.path.join("validation/output", save_filename)
        cv2.imwrite(save_path, annotated_image)
        
        # Optionally, return the file path or a URL for the saved image
        return JSONResponse(content={"detections": detections, "image_path": save_path})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
```

---

### Vocabularies
FLOPs: Floating Point Operations per Second. 
+ Floating Point mean doing calculation involving fractions or decimal
+ FLOPs count how many of these decimal-based calculations a computer or model can do in a second.

**Examples:**
+ Small FLOPs (Simple Model): If a model uses fewer FLOPs, it might process an image quickly but with less accuracy. Imagine spotting apples in a basket but missing the oranges because you're in a hurry.
	
+ Large FLOPs (Complex Model): If a model uses many FLOPs, it works more thoroughly. This is like carefully inspecting the basket and identifying every single fruit but taking more time.

Compare YOLO11s vs YOLO11n: [[YOLO Models performance comparison]]
Winner: YOLO11n -> Better without lossing much accuracy

---
(Understand disk footprint later)
 `footprint=disk(15)` with a radius of 15 pixels. This footprint is then used by the `rank.equalize` function to perform local histogram equalization on the image.
 + `disk(15):` create a disk-shaped structureing element with radius of 15.
 + `disk`: fuction genarates a 2D array where element within the specified radius (i.e. 15) are set to 1, and elements outside to 0.
+  **Used**: by the `rank.equalize` function to define the neighborhood around each pixel for local histogram equalization.
	![[Pasted image 20241212110144.png]]


# Problems: 

### Skews Parallelogram when Reconstructing using midpoint

**Reasons for Out-of-Bounds Coordinates:**
1. **Inaccurate Input Coordinates:** The most likely reason is that the initially detected corners (botleft, botright, topleft in your example) are not perfectly accurate. Even small errors in the positions of the detected corners can be amplified when calculating the missing corner, especially if the ID card is significantly skewed or distorted.
    
    - **Object Detection Errors:** The underlying object detection model might be:
        
        - **Misidentifying corners:** It might be selecting points that aren't true corners of the ID card.
            
        - **Imprecise localization:** Even if it correctly identifies the corner, the bounding box might not be perfectly tight, leading to slightly offset coordinates.
            
        - **Confused by background clutter or noise:** If the image background is complex, the detector might be confused.
            
2. **Perspective Distortion:** Real-world images of ID cards often suffer from perspective distortion. Your calculate_missed_coord_corner function assumes the ID card is a perfect parallelogram. When perspective is present, the four corners will not form a perfect parallelogram, and using the midpoint-based reconstruction can lead to inaccurate and out-of-bounds results. In your specific case:
    
    - If the top of the ID card is further away from the camera than the bottom, the topright corner will appear closer to the topleft and potentially higher up (smaller y-value). Your calculation, assuming a parallelogram, tries to extend the top edge horizontally, resulting in a negative y-value.
        
3. **Edge Cases and Extreme Skew:** If the ID card is extremely rotated or skewed in the image, the parallelogram assumption breaks down even further. The two provided corners might not accurately define the orientation and size of the card's edges for a reliable parallelogram completion.
    
4. **Numerical Precision:** While less likely in this specific scenario with floats, sometimes minor numerical precision issues can accumulate. However, the magnitude of your offset suggests a more fundamental problem.

### Solutions
1) **Improve Corner Detection:** The most impactful solution is to improve the accuracy of your initial corner detection. This involves:

2) - **Constrain the Output:** After calculating the missing corner, explicitly check if the coordinates fall within the image boundaries (0 to width, 0 to height). If they don't, you can implement strategies like:
    
    - **Clamping:** Set the out-of-bounds coordinate to the nearest boundary value (e.g., if y < 0, set y = 0). This is a simple but potentially inaccurate fix.
        
    - **Flagging and Ignoring:** If a coordinate is out of bounds, you can flag the reconstruction as potentially unreliable and skip further processing for that image or use a fallback method.

3) **Account for Perspective Distortion:** More sophisticated methods can account for perspective:
    
    - **Homography Estimation:** If you have four reasonably accurate corner detections (or can reliably estimate three and have a good prior), you can estimate a homography matrix. This matrix describes the transformation between the distorted quadrilateral in the image and a rectangular template. This is a more accurate approach than assuming a parallelogram.
        
    - **Perspective Correction Techniques:** Apply image transformations to "unwarp" the ID card before or after corner detection. This requires identifying a plane in the image.

4) **Validate Input Corners:** Before calculating the missing corner, perform some basic validation checks on the input corners:
    
    - **Check for reasonable ordering:** For example, topleft's x-coordinate should generally be less than topright's x-coordinate. Similarly, y-coordinates should follow a general pattern.
        
    - **Check for proximity:** The distances between the provided corners should be within a reasonable range based on the expected size of an ID card. Large discrepancies might indicate errors.