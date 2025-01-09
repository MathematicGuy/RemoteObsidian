Gradient Descent -> Neural Network -> Multi-Layers Perceptrons -> CNN -> Transformer

note: mô hình mặc định dùng He-Innitialization.

Problem with MLP: perform badly in testing for image classification.
![[Pasted image 20241204201319.png]]
And perform even worst when adding 3 more layers
![[Pasted image 20241204201706.png]]

Trong MLP, bất kể dữ liệu gì cũng sẽ đc flatten xuống 1-D vector. Việc này tạo ra vấn đề:
+ Xóa thông tin không gian của dữ liệu. Không hiệu quả khi có nhiều tham số -> ảnh 2D khó có thể biểu diễn tốt dưới dạng 1D. 
	  ![[Pasted image 20241204202422.png]]
	
+ 1 node đầu lớp sau đc nối vs mọi nodes lớp tr'c -> gây nhiễu và khiến thông tin từ nhiều ảnh trộn lẫn vào nhau.

Field of views (FoV)
	giống như khi mình nhìn 1 bức ảnh to, mình phải nhìn từng khoảng 1 lúc chứ ko nhìn toàn bộ ảnh 1 lúc -> cách thức giống chia để trị trong thuật toán.
	Ex: cho 1 hình 3x3, FoV của mình là 2x2 thì mình sẽ khai thác đc toàn bộ bức ảnh 3x3 sau 4 lần nhìn.  
	Gọi giá trị trích xuất từ 4 lần nhìn qua FoV 2x2 là m1, m2, m3, m4.    ![[Pasted image 20241204203640.png]]

Trong Convolution Layer, thường 3x3 là hiệu quả vì nó đối xứng (ko nhất thiết phải là 9x9, hay Kernel ko vuông như 3x4)
![[Pasted image 20241204210325.png]]
$S_{d}: stride$
$K: \text{kernel size}$
$S_{o}: \text{step size}$
Ex: $S_{0} = \frac{5-3}{1} + 1 = 3$ -> 3x3 Feature Maps

![[Pasted image 20241204212237.png]]
(3, 32, 32) với 4 kernels (3, 5, 5) có feature maps (4, 28, 28) vì 
![[Pasted image 20241204212708.png]]
(Depth = 4 đương nhiên sẽ giữ nguyên)
For Stride = 1.
`(Output - 1 - Input_size) = Kernel_size `

**Code**
![[Pasted image 20241204213543.png]]

note: lỗi chiều sâu data ko khớp với Conv2d. *data* có `in_channels=3` trong khi *layer* có chiều sâu input 1 (i.e. `in_channels=1`)
![[Pasted image 20241204214016.png]]

Tổng số lượng tham số của CNN là 64, 32, 3, 3 nghĩa là lớp Convo cuối cùng output 64 kernels, lớp tr'c nó output 32 kernels, và vân vân.
![[Pasted image 20241204214301.png]]

![[Pasted image 20241204214851.png]]
note: intput (3, 32, 32) -> chỉ cần nhớ là tính (input_size - kernel_size + 1) vì Stride trong TH này là 1
![[Pasted image 20241204215423.png]]

**Overview**
![[Pasted image 20241204215517.png]]

Giải pháp chống mất Spatial Information, chỉ 
![[Pasted image 20241204215615.png]]

Bao nhiêu kernels là đủ ? -> ảnh càng phức tạp thì cần càng nhiều kernels, và chủ yếu là do kinh nghiệm cá nhân.
(Rule: chiều sâu càng ngày càng tăng, chiều cao và rộng càng ngày càng giảm)
![[Pasted image 20241204220258.png]]
note: ban đầu feature maps có size là 5x5 nhưng sau nhiều nghiên cứu thì học dùng 3x3. (bởi một số cân nhắc thực tế và lý thuyết nhằm cân bằng giữa hiệu quả, hiệu suất và độ phức tạp tính toán)
+ A **3x3 kernel** performs **9 multiplications per position**, while a **5x5 kernel** performs **25 multiplications per position**, requiring more computational resources.
+ Both kernels leverage parallelism for efficiency, but **3x3 is faster** because it requires fewer computations per position.

+ ? Khi nào kernel size nhỏ hơn 7x7 thì mới nên flatten.


### Pooling
Trong grid 2x2 pixel,
+ max pooling: lấy giá trị lớn nhất trong 4 giá trị của grid 2x2
+ average pooling: lấy giá trị trung bình của 4 giá trị của grid 2x2
	dùng trong GAN vì nó dùng 4 dữ liệu 1 lúc thay vì 1 ở max pooling.

Tại sao, Khi nào dùng max-pooling? 
>Khi các feature maps đang tổng hợp thông tin trừu tượng sau n layers ổn định rồi, sau đó mình ms giảm số chiều xuống dùng max pooling.  


note: có thể dùng stride bằng 2 thay cho max-pooling

