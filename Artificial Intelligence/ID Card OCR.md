+ ! Let ChatBot do the work, focus on what need to be learned.
**Presentation**
1) How it work
2) How to Install and Run
3) Demo Video

[[Computer Vision Roadmap]]
[Triển Khai lên Mobile dùng Flutter](https://viblo.asia/p/thu-lam-app-flutter-cho-nhan-dien-chung-minh-thu-3Q75w1n2ZWb)
Model: **YOLOv8 Nano**
[Real time Shape Detection](https://youtu.be/Fchzk1lDt7Q?si=iIpyeBfKFzQSqims)
Deploy Model using Gradio (Interface for ML App, just like Steamlit for Python App)

note: 
+ Xác định vấn đề cần tự giải quyết và thứ có thể lấy được (vấn đề đc giải quyết)
+ Hiểu mục tiêu cuối cùng của dự án là gì? sau khi quét CCCD
+ tfrecord

![[Pasted image 20241211160351.png]]
![[Pasted image 20241211160415.png]]

+ ! remember to filter NULL
Later: 
Improve Model prediction with different lighting (Augment in Roboflow, minimize manual labeling by choosing 4-5 different diff lighting condition then augment them to simulate more lighting condition)
+ Apply NMS later
+ Add Early Stopping
+ Gather a lot of image for auto labeling using pre-trained model  -> add this dataset with label to the processed main dataset (in my pre-processing lab)

Plan: 


Train New YOLO Model with Greyscale pre-processing
Load New Model to my Detection Anomaly and Modify it into ID Card Detection Project

Test: 
Initialize Perspective Transform
Train Text Detection Model (VietOCR)




---

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

### Bounding Box Detection

![[Pasted image 20241210092038.png]]

# Pre-Processing
### Normalization
Grey Scale, Re-size

### Apply Constract 
Adaptive Equalization

This method enhances edges more effectively by focusing on local contrast, which is crucial for edge detection tasks. It also avoids the excessive noise amplification associated with global histogram equalization.

#### Improve Pre-Processing Speed
### Auto-Annotation using Pre-trained Model


**Apply Parallel Processing**
- **How**: Use multi-threading or parallel processing libraries to process multiple images simultaneously.
- **Implementation**: Utilize `concurrent.futures` for multithreading.


```
curl -L "https://app.roboflow.com/ds/t206iD2fLY?key=LoBpDYe7aP" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
```
# 4 Corners Detection




---
# Bài toán nhận diện chứng minh thư
B1: Biến đổi ảnh đc chụp từ bất kì tư thế nào về 1 hệ tọa độ để xử lý dễ dàng nhất.
**Geometric Transformations of Images** trong xử lý ảnh mà cụ thể đó là **Perspective Transformation** sử dụng 4 góc tọa độ.
![[Pasted image 20241210092617.png]]

# Detect 4 Góc Tọa Độ
Chọn Model:
+ Yolov10s vì nó nhẹ mà tốt. model size ~ SSD Lite (compare SSD with YOLO)

Chọn Dataset
Khai báo 4 class tương ứng vs 4 góc tọa độ
Huấn luyện model
Validate model

### Non Max Suppression
> Áp dụng NMS để chọn lọc những bbounding box tốt nhất. 
![[Pasted image 20241210101915.png]]
  Ví dụ đầu ra
```python
final_boxes 
>>>
array([[ 16, 647,  83, 711],
       [894, 636, 956, 701],
       [ 11,  87,  79, 149],
       [892,  80, 953, 139]])
       
final_labels
>>>
['bottom_left', 'bottom_right', 'top_left', 'top_right']
```

### Perspective Transform (quan trọng)
Lấy điểm trung tâm, dựa vào 4 tọa độ góc.
```python
def get_center_point(box):
    xmin, ymin, xmax, ymax = box
    return (xmin + xmax) // 2, (ymin + ymax) // 2
```

Chuyển đổi sang dạng dict với `{map label}:{label_boxes}` để thuận tiện cho bước tiếp theo 
```python
final_points = list(map(get_center_point, final_boxes))
```
>output
```python
label_boxes = dict(zip(final_labels, final_points))

>>> 
{'bottom_left': (49, 679),
 'bottom_right': (925, 668),
 'top_left': (45, 118),
 'top_right': (922, 109)}
```

**Transform sang tọa độ đích**
```python
# Khai báo hàm Transform
def perspective_transoform(image, source_points):
    dest_points = np.float32([[0,0], [500,0], [500,300], [0,300]])
    M = cv2.getPerspectiveTransform(source_points, dest_points)
    dst = cv2.warpPerspective(image, M, (500, 300))
    
    return dst
```
>Gọi Hàm với tọa độ 
```
```