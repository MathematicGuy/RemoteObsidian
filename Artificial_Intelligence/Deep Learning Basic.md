[Bài 1: Linear Regression và Gradient descent](https://nttuan8.com/bai-1-linear-regression-va-gradient-descent/#Python_code)
[Bài 2: Logistic regression](https://nttuan8.com/bai-2-logistic-regression/)
[Bài 3: Neural network](https://nttuan8.com/bai-3-neural-network/)
[Bài 4: Backpropagation](https://nttuan8.com/bai-4-backpropagation/)
[Bài 5: Giới thiệu về xử lý ảnh](https://nttuan8.com/bai-5-gioi-thieu-ve-xu-ly-anh/)
[Bài 6: Convolutional neural network](https://nttuan8.com/bai-6-convolutional-neural-network/)
[Bài 7: Giới thiệu keras và bài toán phân loại ảnh.](https://nttuan8.com/bai-7-gioi-thieu-keras-va-bai-toan-phan-loai-anh/)

---
# What does this do ?
### Linear Regression
> Help find parameter (e.g. $w_{0}, w_{1}$) that minimize loss (i.e. distance) between current value and the expected value. 


### Gradient Descent
> Help find parameter (e.g. $w_{0}, w_{1}$) easier to minize the loss function by calc the derivative by update the function partial derivative.

### Logistic Regression
> Apply sigmoid for classification. (e.g. classified spam email with y = sigmoid(x). if y > spam elif y < 0.5 not spam) 


### Neural Network
b - bias ?
derivative: describe the rate of change
derivative of derivative: describe the rate of change of "the rate of change" (e.g. car speed and acceleration)

bỏ bias: $w1∗x+w2∗y=0w1​∗x+w2​∗y=0$, sẽ luôn đi qua gốc tọa độ và nó không tổng quát hóa phương trình đường thẳng nên có thể không tìm được phương trình mong muốn.

note: tham số đầu vào = tham số đầu ra (từ đó tham số đầu ra có thể truyền vào 1 hàm khác)

#### Annotation
**translate** 
> with node i-th in layer $l$  bias $b^{(l)}_{i}$ perform 2 steps:
![[Pasted image 20241010114526.png]]
	$l$ as the current layer (start from 0) 
		e.g. $l_{0}$  mean the first/input layer, $l_{1}$ mean the first hidden layer
		$l_{1}=2$ mean first hidden layer have 2 nodes (not include bias of course)
		![[Pasted image 20241010115124.png]]
	$l-1$ as the previsous layer
	$z^{(l)}_{i}$ mean the sum of all previous layers nodes multiply with their correspond weight then add bias b.
	  
	![[Pasted image 20241010114725.png]]

### Feedforward
rewrite $z_{1}$ in general form.
![[Pasted image 20241010115427.png]]
$z^{(1)}$ (matrix z layer 1) mean Multiply all Weight from the previous layer with each Activation Function of the current layer then add bias of its corresponding layer. 
![[Pasted image 20241010120704.png]]
$A$ is just Matrix A with activation function. Thus the while neural netwrk chain can be rewrite as:
![[Pasted image 20241010121035.png]]



### Backpropagation



### Convolution Neural Network



