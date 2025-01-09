

AlexNet: just MLP (train with 2GPU cards)
VGG: MLP with Convolution Layers. 
![[Pasted image 20250109154115.png]]
U-Net: Important
ConvNext - once better than transformer, but transformer more better the more data it learned. 


**How to increase training accuracy ?**
**VGG16**
![[Pasted image 20241206202035.png]]
```python
conv2d(3, 64, 244) # kernel_size/input 3, output 64, image_size 244x244
conv2d(64, 128, 112) # kernel_size/input 64, output 128, image_size 244x244
```
maxpooling x128 ở lớp thứ 3 vì đấy là 1 cách cài đặt khác và max-pooling chỉ chia đôi số lượng pixels của ảnh.

**VGG-16: 16 layers with parameters**
![[Pasted image 20241206202446.png]]
note: channel là số kênh màu của 1 ảnh, mỗi channel đại diện cho 1 loại màu của ảnh. 
Mỗi Conv2d có parameter đầu vào là (input_channel, output_channel, image_size) Ex: Conv2d có kênh đầu vào là 3, kênh đầu ra là 64 và có kernel_size là 3   
![[Pasted image 20241206202800.png]]
Mỗi Sequential tượng trưng cho 1 Block hình trên 
![[Pasted image 20241206202918.png]]
note: Dense là Linear + Activation_Function (fully-connected)


### Testing and Problems
Test Cifar-10 dataset: show Model low capability, how to improve this? 
![[Pasted image 20241206204727.png]]
add more block to improve model ability to see abstraction behind image
![[Pasted image 20241206204932.png]]

Imitate VGG Model, add more layers but still use sigmoid. As you could have guess, we get Gradient Vanishing problems
![[Pasted image 20241206205451.png]]

The same but with ReLU, performance improve dragstically 
![[Pasted image 20241206205236.png]]
Using Glorot uniform initialization and a lot of improvement technique:
![[Pasted image 20241206205314.png]]
![[Pasted image 20241206205323.png]]
However the Network does not learn again. But isn't that model with more layers learn better? 
![[Pasted image 20241206205348.png]]
+ $ While **Sigmoid fit with Cifar-10**. **ReLU** does not fit with Cifar-10 Dataset, but **fit with Kaiming He**. 
note: cần phải hiểu activation function này đi đc cùng vs phương pháp, công cụ nào để ko trở nên vô dụng.

### Solutions
![[Pasted image 20241206205914.png]]
Work well on MNIST but bad in Cifar-10 -> Because of dataset Complexity -> How to reduce the complexity of the Cifar-10 dataset?
![[Pasted image 20241206205923.png]]
Answer: normalization.
![[Pasted image 20241206210115.png]]

### Solution 1: Normalization
**This normalization helps network to be invariant to linear transformation**.  
**Intuition:** máy nhìn ảnh 1 con chó bị mờ nó sẽ nhìn ra 1 con khác, để cho máy hiểu nó vẫn là 1 con chó thì mình áp dụng Normalization. 
$\leftrightarrow$ Đưa giá trị của 2 ảnh về 1 miền giá trị. Hence Linear transformation. 
![[Pasted image 20241206210058.png]]
+ ? **note:** $\mu_{y}$ nghĩa là đầu vào là y. Nên $\mu_{y}= \frac{1}{n}\sum Y=\frac{1}{n}\sum(aX + b)$
+ $ Điều này cho thấy, Y có thể chuyển hóa về ngang hàng vs X. (note lại cái này sau)

Sol 1: Đưa về mean bằng 0, giảm mức độ phức tạp của data xuống 
-> Kết quả là Train tốt hơn -> Tăng khả năng học của mô hình
![[Pasted image 20241206211118.png]]
phương pháp khác, cũng đc nhưng ko tốt bằng 0-mean
![[Pasted image 20241206211235.png]]


### Solution 2: Batch Normalization
![[Pasted image 20241206211359.png]]
Để dễ quản lý, xử lý phần Train, mình normalize x1, x2 để đưa giá trị về cùng 1 thước đo. 
Batch Normalization dựng lên dựa trên mini-batch 
![[Pasted image 20241206212450.png]]
Tại sao cần 2 learning parameters, ...
![[Pasted image 20241206212529.png]]

note: $\hat{U}, \hat{V}$ ~ $\hat{X_{i}}$ (dùng U và V thay cho X mũ, đây chỉ là 1 cách đặt tên)
![[Pasted image 20241206212845.png]]

Mỗi mặt phẳng là 1 lần tính Mean.
![[Pasted image 20241206213642.png]]
Để lấy tổng của i và j, ta thêm ký hiệu tổng k, tượng trưng cho kernel k.
![[Pasted image 20241206214145.png]]

![[Pasted image 20241206214546.png]]
C: total kernel (tương đương vs số mặt phẳng của 1 hình)
	Ex: 2D ~ 2 kernel
	![[Pasted image 20241206214747.png]]
BS: batch size

Scenario: Cannot train
Apply Batch Normalization, 
![[Pasted image 20241206214858.png]]
![[Pasted image 20241206215031.png]]



---

# TA - Exercise
`6@28x28:` 6 feature maps (not kernel size), 28x28 image sizes
![[Pasted image 20241208204844.png]]
![[Pasted image 20241208205308.png]]
C1 have Output = 14, Input = 28, kernel size = 2, Padding  = 0 -> Stride = 2 (và bằng số kernel)

**Coding Pipeline**
![[Pasted image 20241208205836.png]]

**Inference**
![[Pasted image 20241208213058.png]]
dùng để đẩy lên steamlit 
giá trị mặc định 0.13, 0.38 
