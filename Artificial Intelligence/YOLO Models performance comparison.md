## Bounding Box
**yolov10s:**
![[image/Untitled.png]]

```
0: 640x480 1 CardID, 12.1ms
Speed: 2.8ms preprocess, 12.1ms inference, 22.5ms postprocess per image at shape (1, 3, 640, 480)
```

**yolov10n**
![[image/Untitled 1.png]]

## 4 Corners Detection

**Train**
yolov11n
![[Pasted image 20241210115051.png]]

yolov11s
![[Pasted image 20241210115326.png]]


**Validation**
yolov11n
![[image/Untitled 2.png]]
![[Pasted image 20241210120823.png]]
![[Pasted image 20241210120845.png]]
![[Pasted image 20241210121015.png]]


yolov11s
![[Pasted image 20241210121658.png]]
![[Pasted image 20241210120748.png]]![[Pasted image 20241210120800.png]]
![[Pasted image 20241210121054.png]]

# Normalization and Augumentation
>Improve dataset integity, Augumentate clean data, Normalize using Rank-Based Equalization and denoise with Gaussian Blur

**Adaptive Equalization for Normalization** 
**108 epochs - mAP: 0.86** 
![[Pasted image 20241217141223.png]]

**Rank-Based Equalization for Normalization** 
**95 epochs - mAP: 0.863** -> not overfitting, generalize better
![[Pasted image 20241217141142.png]]
