+ ! Let ChatBot do the work, focus on what need to be learned.
**Presentation**
1) How it work
2) How to Install and Run
3) Demo Video

[[Computer Vision Roadmap]]
[Triển Khai lên Mobile dùng Flutter](https://viblo.asia/p/thu-lam-app-flutter-cho-nhan-dien-chung-minh-thu-3Q75w1n2ZWb)
Model: **YOLOv8 Nano**
Deploy Model using Gradio (Interface for ML App, just like Steamlit for Python App)

[[Internship Report Requirements]]
[[ID Card OCR Note]] 

```python
# Install
$ pip install roboflow

# Authenticate
$ roboflow authenticate

# Import
$ roboflow import -w plotting-zurpc -p text-area-detection /path/to/data
```

# Pre-Processing
### Normalization
Grey Scale, Re-size

### Apply Constract 
Adaptive Equalization

This method enhances edges more effectively by focusing on local contrast, which is crucial for edge detection tasks. It also avoids the excessive noise amplification associated with global histogram equalization.

**Improve Pre-Processing Speed**

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



```python
pred_boxes1 = torch.tensor([
	[2, 0.720081090927124, 33.40931, 242.45248, 70.53368, 282.84384],   # Box 2 (topleft)
	[3, 0.6698232889175415, 439.35947, 230.78842, 477.95145, 283.24826], # Box 3 (topright)
	[1, 0.5960968136787415, 443.94025, 484.69257, 489.34003, 536.5535],  # Box 1 (bottomright)
	[0, 0.44452500343322754, 21.572742, 492.26105, 61.92349, 544.39557], # Box 0 (bottomleft)
	[0, 0.29470255970954895, 427.79895, 0.0, 468.2058, 33.488106]
])


pred_boxes2 = torch.tensor(
	[
		[2, 0.720081090927124, 33.40930938720703, 242.45248413085938, 70.53368377685547, 282.8438415527344],
		[3, 0.6698232889175415, 439.3594665527344, 230.78842163085938, 477.9514465332031, 283.2482604980469],
		[1, 0.5960968136787415, 443.94024658203125, 484.69256591796875, 489.34002685546875, 536.5535278320312],
		[0, 0.44452500343322754, 21.572742462158203, 492.26104736328125, 61.92348861694336, 544.3955688476562],
		[0, 0.29470255970954895, 427.7989501953125, 0.0, 468.205810546875, 33.48810577392578]
	]
)
```


```python
# 1st


# 2nd
Image loaded successfully!
label_boxes: {'botleft': (41.0, 518.0), 'botright': (466.0, 510.0), 'topleft': (51.0, 262.0), 'topright': (458.0, 257.0)}
source_points:
 [[ 51. 262.]
 [458. 257.]
 [466. 510.]
 [ 41. 518.]]
```