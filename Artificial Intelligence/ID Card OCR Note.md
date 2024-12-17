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
+ Add Early Stopping
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


