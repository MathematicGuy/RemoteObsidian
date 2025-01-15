CV docs: https://docs.opencv.org/4.x/d0/d86/tutorial_py_image_arithmetics.html
### HW
+ Read about Color Space, Color Space Conversion
+ How Human Vision relate to Computer Vision

Gray Scale - Ảnh đa cấp xám

---

**HW: Code ALL of THIS**
S: Kết Quả
T: Phép/Hàm Biến Đổi 
r: input value

## Contrast Stretching and Thresholding
![[Pasted image 20250110091831.png]]
>Encourage highly inverse values if one of 2 axis/color move between the threshold value range.   

## Intensity Correction
>Adjust image brightness using function 
![[Pasted image 20250110093527.png]]
### Log Correction
![[Pasted image 20250110092951.png]]
> Help balance out image bright intensity. With log, if the image is too light or too dark, log convert image brightness back to the average value.   

### [Gamma Correction](https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/)
![[Pasted image 20250110093302.png]]

### Contrast Stretching
![[Pasted image 20250110093542.png]]

## [Histogram](https://medium.com/@khanhson0811/unlocking-image-enhancement-a-guide-to-histogram-processing-and-equalization-with-opencv-8db4477e6ba6) Processing (Xử lý dùng biểu đồ tần suất)
source: https://viblo.asia/p/tuan-3-histogram-histogram-equalization-3P0lPnxmKox
![[Pasted image 20250115084130.png]]

(Tần suất dải màu từ sáng 0 tới tối 255)
h(g) -> feature vector
Image Retrieval 

 **Solution:** Có thể truy cứu ảnh sử dụng Histogram vì Histogram của ảnh cùng kích thước (e.g. 8-bits) luon có cùng kích thước vector (i.e. độ dài). 
-> Histogram cho ta biết tần số của từng dải mầu trong từng ảnh
-> nếu 2 ảnh có cùng tần số dải màu thì ta có thể dễ dàng so sánh bằng cách tính khoảng cách 
-> truy cứu đc ảnh giống nhau.
**Phương pháp:**
1) [Tính Histogram](https://processing.org/examples/histogram.html) của từng ảnh
2) Tạo hàm so sánh với 2 input là histogram1 và histogram2, với histogram là 1 vector chứa tần số (frequency) của từng giá trị (pixel value) trên dải màu từ 0 đến 255 trên Histogram.
3) Tính khoảng cách Euclit sử dụng histogram1 và histogram2. That it foul !!!


### Problems with Histogram
Examples:
**Problem 1:** Image's histogram can be the same but image's pixels position can be different like in flip image, black ball on a white canvas or "chess board vs half white canvas".
	-> Histogram cannot detect different because it colors frequency base, thus histogram cannot describe spatial features. 
**Solution:** Divide the image to 4 pieces or n-pieces and compare them independently althought computational cost increase.

**Problem 2:** when resize the same image can describe diff values.
**Solution:** chuẩn hóa sử dụng `tần suất của từng giá trị pixel`  / `tổng số lượng pixel của ảnh.` 

 **Problems 2: Same Image but Different Brightness**
 S = r + c where c is a constant represent diff in brightness and r is the original brightness.
 **Solution:** Can use MLP and take 1 image as input and 1 image as grounth truth image then train the model to match with the weight `c` (i.e. brightness)
