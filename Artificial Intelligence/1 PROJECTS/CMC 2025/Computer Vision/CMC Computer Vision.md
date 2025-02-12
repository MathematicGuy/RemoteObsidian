**CV** docs: https://docs.opencv.org/4.x/d0/d86/tutorial_py_image_arithmetics.html

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
![[Pasted image 20250116195429.png]]

**Inputs:** Ảnh trắng đen 
	Histogram của ảnh Tần suất dải màu từ sáng 0 tới tối 255)

**Idea:** Có thể truy cứu ảnh sử dụng Histogram vì Histogram của ảnh cùng kích thước (e.g. 8-bits) luon có cùng kích thước vector (i.e. độ dài). 
-> Histogram cho ta biết tần số của từng dải mầu trong từng ảnh
-> nếu 2 ảnh có cùng tần số dải màu thì ta có thể dễ dàng so sánh bằng cách tính khoảng cách 
-> Truy cứu đc ảnh giống nhau.
**Phương pháp:**
1) [Tính Histogram](https://processing.org/examples/histogram.html) của từng ảnh
2) Tạo hàm so sánh với 2 input là histogram1 và histogram2, với histogram là 1 vector chứa tần số (frequency) của từng giá trị (pixel value) trên dải màu từ 0 đến 255 trên Histogram.
3) Tính khoảng cách Euclidean sử dụng histogram1 và histogram2. That it foul !!!
3) Tính khoảng cách giữa 2 hình ảnh sử dụng công thức tương quan ([[Correlation Coeficient]]). 
![[Pasted image 20250117070918.png]]

### Problems with Histogram
Examples:
**Problem 1:** Image's histogram can be the same but image's pixels position can be different like in flip image, black ball on a white canvas or "chess board vs half white canvas".
	-> Histogram cannot detect different because it colors frequency base, thus histogram cannot describe spatial features. 
**Solution:** Divide the image to 4 pieces or n-pieces and compare them independently althought computational cost increase.

**Problem 2:** when resize the same image can Describe diff values.
**Solution:** chuẩn hóa sử dụng `tần suất của từng giá trị pixel`  / `tổng số lượng pixel của ảnh.` 

**Problems 3: Same Image but Different Brightness**
 S = r + c where c is a constant represent diff in brightness and r is the original brightness.
**Solution:** Can use MLP and take 1 image as input and 1 image as grounth truth image then train the model to match with the weight `c` (i.e. brightness)

### Histogram Matching
```python
def match_histograms(source, template):
    source_hist, _ = np.histogram(source.flatten(), 256, [0, 256])
    template_hist, _ = np.histogram(template.flatten(), 256, [0, 256])

    source_cdf = source_hist.cumsum()
    template_cdf = template_hist.cumsum()

    source_cdf_normalized = source_cdf / source_cdf.max()
    template_cdf_normalized = template_cdf / template_cdf.max()

    mapping = np.interp(source_cdf_normalized, template_cdf_normalized, np.arange(256))
    
    return mapping[source.flatten()].reshape(source.shape)

matched_image = match_histograms(image, image2)
```

### [Histogram Equalization](https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html) and [CLAHE](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html)
**Histogram Equalization**
![[Pasted image 20250117081811.png]]
	1) Get the highest gray value 5 and its bits (bit size that can represent 5)
	2) Initiate gray levels range = $2^{bits}$. e.g. $2^3=8$
	3)  Start Calculating: 
	+ **PDF:** Probability Distribution (*value_i / the total_value*)
	+ **CDF:** Cumulative Distribution (*cumulative sum*) annotate as $S_{k}$
	+ $S_{k} \times max(\text{gray level})$: Multiply CDF with the highest gray level 
	+ **Histogram equal level:** approximate value upward (i.e. `.ceil()`  in python)
	4) Replace old pixel values with new pixel values.

**CLAHE**
![[Pasted image 20250117070011.png]]
> **Histogram Equalization stretch the histogram to include all ranges** `[0, 255]`. **CLAHE** divide a image into `n 8x8 tiles/grids, then **apply Histogram Equalization into each tile**. 

## Spatial Filtering (Kernel)
[Otsu's Method](https://medium.com/@vignesh.g1609/image-segmentation-using-otsu-threshold-selection-method-856ccdacf22)
[Gaussian Blur](https://en.wikipedia.org/wiki/Gaussian_blur)

## Morphological (hình thái) Operation
The most [basic morphological operations](https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html) are: Erosion and Dilation. They have a wide array of uses, i.e. :
- Removing noise
- Isolation of individual elements and joining disparate elements in an image.
- Finding of intensity bumps or holes in an image

 **Original Image**
	![[Pasted image 20250207091354.png]]

### Dilation (phép giãn)
![[Pasted image 20250207091443.png]]
>Dialation include **convolving an image (A) with some kernel (B)** which can have any shape and size, usually square or circle. Each **convolve pick the maximum value inside the kernel each pixel across the image**. (e.g. 1 out of `[0, 1]`)

### Erosion (phép co)
![[Pasted image 20250207091514.png]]
>Erosion is the same as Dilation except for it picking Minimum value (e.g. 0 out of `[0, 1]`) 

### Openning (Phép mở: co -> giãn)



### Closing (Phép đóng: giãn -> co)


## Contour (research)
[OpenCV Contour](https://docs.opencv.org/3.4/d3/d05/tutorial_py_table_of_contents_contours.html)
**Note:** Describe object border  

## Canny 
**Note:** Like Contour but a set of dotted lines.

