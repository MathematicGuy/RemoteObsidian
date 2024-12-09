# CNN Introduction
+ @ Tóm tắt cơ bản: MLP giúp phân loại nếu số features đầu vào ko quá nhiều. Đối vs dữ liệu ảnh có hàng triệu features, đầu tiên ta dùng **CNN để trích xuất hàng trăm features quan trọng nhất từ hàng triệu features** đó. Rồi mới **đưa vào MLP để phân loại hình ảnh**.    

Trong xử lý ảnh, mỗi ảnh có hàng ngàn pixels, mỗi pixles đc xem như 1 feature. Nếu ảnh có kích thước 1000x1000 thì sẽ có 1.000.000 features. Trong MLP có feed-forward NN vs mỗi layers, mỗi pixel trog 1 layer lại kết nối full-connected vs 1.000.000 pixels ở lớp tr'c. tức sẽ có $10^{6} \times 10^{6} = 10^{12}$  tham số mỗi layer. 
+ ? Bởi vì có quá nhiều tham số, mô hình sẽ dễ bị overfitted (học quá kĩ 1 lg dữ liệu đc cho) và cần lượng lớn data cho training và prediction.

+ $ CNN giúp model giải quyết hiệu quả việc xử lý dữ liệu ảnh bằng cách trích xuất những đặc điểm quan trọng nhất của hình ảnh và dùng nó để phân loại. Có 2 đặc tính của image hình thành nên cách hđ của CNN: 
![[Pasted image 20241208142005.png]]
+ **feature localization:** mỗi pixel hoặc feature có liên quan vs các pixel quanh nó
+ **feature independence of location:** mỗi features đều mang gtrị độc lập. 
-> **CNN xử lý vấn đề có quá nhiều tham số** vs **Shared parameters** (feature independence of location) của **Locally connected network** (feature loclization), đc gọi là Convolution Net.

cụm pixels: n by n pixles block 
+ $ **Locally Connected Layer:**  In the first hidden layer of a CNN, each node (or neuron) connects only to a small portion of the input image, rather than the entire image. This small portion is often referred to as the **receptive field** (*region of the image*). By limiting connections to these local regions, the model significantly reduces the number of parameters compared to a fully connected layer, making it more efficient

+ $ **Shared parameters:** In images, certain key features (e.g., edges, corners, or patterns) often appear repeatedly across different regions or feature maps. To efficiently capture these features, we use the same set of parameters (weights) across the entire image.
+ ? For example, in the inner curve of the digit "7," this pattern might appear in multiple locations across different feature maps. By sharing parameters, the CNN can detect these features regardless of their position, ensuring efficient and consistent feature extraction across the input.

Key Note: 
+ **Kernel:** a N by N grid slide though the images from left to right in order to extract a specific features (like a filter).
	In deeper layers of CNN, more complex kernels are incorporated to detect shapes, objects and complex structures which is done by leverage the previously generated feature maps and their detected simple features to build more complex ones. ![[Pasted image 20241208143921.png]]
	
+ **Convolutional + ReLU:** Convolution applied kernel across the image to create feature maps (i.e. each map contain a specific features) identifying patterns like edges or textures. then applies ReLU a non-linear transformation, setting all negative values to zero, which helps retain meaningful features while ignoring irrelevant parts.
	(Covolution layers identify image's features (each are unique) & ReLU highlight image's meaningful features)![[Pasted image 20241208142940.png]]
	
+ **Pooling:** Pooling reduces the size of feature maps by **selecting the most important value** (e.g., max or average) **from regions of the image**, preserving key features while minimizing computational complexity.
	+ **Max:** take the largest value out of 4 values ​​inside 2x2 grid
	+ **Average:** take the average value of 4 values inside ​​of 2x2 grid
	![[Pasted image 20241208143453.png]]
	
+ Fully Connected Layers (Classifier): Similiar to Feed-Forward network except rather than raw input pixels these are now high-level abstracted featrues from our input.  
	![[Pasted image 20241208150732.png]]
+ **Summary:** CONV and POOL help skim image's features into high-level features, Fully Connected Layers then using those high-level features to classifies images.
	
	+ CNNs clasified images by systematically extracting features maps using convolutional layers (Convs) and reducing these maps to their most meaningful features using poolings layers (Pools). Through this process, the model begins learning basic patterns like edges and gradually identifies more complex shapes (i.e. pixels that hold more information)  
		
	+ These features are then processed and aggregated (i.e. flattening, tổng hợp) through Fully Connected layers to classify what the image represents.
	(*This is similar to how human eyes might scan skimming throught the image, identifying key features that make the image unique*) ![[Pasted image 20241208150732.png]]
	
**CNN Structures** 
	![[Pasted image 20241208163921.png]]
	![[Pasted image 20241208164033.png]]
	





Unmentions Topic (note later):
![[Pasted image 20241208150944.png]]



# How to Train CNN
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
