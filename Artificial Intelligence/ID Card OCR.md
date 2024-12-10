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


**yolov10s:**
![[image/Untitled.png]]

```
0: 640x480 1 CardID, 12.1ms
Speed: 2.8ms preprocess, 12.1ms inference, 22.5ms postprocess per image at shape (1, 3, 640, 480)
```


**yolov10n**
![[image/Untitled 1.png]]![[Pasted image 20241206172334.png]]

