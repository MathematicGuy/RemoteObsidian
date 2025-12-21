**Reference:**
+ [Deep Learning cơ bản CNN]( (https://nttuan8.com/bai-6-convolutional-neural-network/))
+ Super Good Reference for a straight forward outline: [How CNN work, in depth](https://youtu.be/JB8T_zN7ZC0?si=G7pMoNJv4teu0HQQ)

**Overview of everything + Conclusion of the Blog**
+ What you'll learned and discouver
+ Main Topic
+ Extras Topic
+ Credit and Reference
Note - goes into each topic with Intuition.

1. [[Introduction to Computer Vision - CNN Focus]]
	*Intro to how Image presented in Computer Vision*
	*Introduct to Tensor (1D, 2D and 3D)*
	*Problem with MLP for Image Classification* **(IMPORTANT)**
		MLP run too slow. How about we simplified all features before input it to the MLP -> Add CONV layers. So CNN not replacing MLP but **enhancing its feature extraction ability.**

2. *CNN Overview* - [[CNN from Scratch]] - [how CNN work in depth](https://brandonrohrer.com/how_convolutional_neural_networks_work.html)
	Describe CNN *architecture fully* and *each of its component along with their functionality and purpose*. Bonus: show Different before and After with [Real Example](https://poloclub.github.io/cnn-explainer/).
	*Overall of CNN calculation in 1 paragraph:*
	(Image Pixels + bias) -> (Conv -> ReLU) x 2 -> Pooling) x 2 -> (Flatten + bias) -> Softmax -> Output

3. *CNN Operation in Depth* - [Stanford CNN](https://cs231n.github.io/convolutional-networks/)
	(For each Operation explain. What it do ? Why do we need it)
+ *What is Convolution ?* (Interative Convolution Operation)
+ *Padding* (when padding is necessary ?)
+ *Stride* (stride of 1 == the kernel move 1 pixel per dot product)
	Effect of Stride to Feature Extraction.
	Local feature vs Global feature
+ *Explain ReLU function*
	Purpose: Introduce Non-Linearity (*Explain Non-Linearity and why*) and remove Noise ???
	[source](https://www.quora.com/What-are-the-main-role-of-ReLU-Activation-Function-in-deep-learning): In Image Processing using CNNs, we _use ReLU activation_ to _remove_ an unnecessary _noise_ due to negative _values_ that could persists. For those ...

4. *CNN Backpropagation*

5. Advance CNN (Pooling, Batch Normalize, etc..)

*Final:* Code with OOP
*Extras:*
+ *Deepen Conv Understanding*: What 1 x 1 Convolution actually do.
+ *Why Flatten the last layer of CNN ?* 
	Sau khi thực hiện qua nhiều mức trừu tượng hoá và tích luỹ thông tin bậc cao qua nhiều lớp CNN thì mỗi “điểm” mang nhiều thông tin tích luỹ hơn, đồng thời tính “phụ thuộc không gian” giảm rất nhiều (do đã nén vào các điểm ảnh cuối qua mạng sâu).  
	  
	Chính vì thế Flattern lúc này thì không ảnh hưởng nhiều lắm đến spatial gốc nữa. MLP lúc này là để “classifier” (ra quyết định) chứ không còn là “xử lý thông tin ảnh” nữa.  
	  
	Việc mất mát thuộc tính không gian ở cấp độ này sẽ rất ít vì dữ liệu không gian đã được nén trong các tầng CNN rồi.






----
### MLP Batch Norm
![[Pasted image 20251212154825.png]]
**Where Batch Norm was applied in MLP:**
1. **Linear Layer:** Computes "Raw" signal comming out of the linear layer $z=Wx+b$. This value is unstable, might be very large or small.
2. **Batch Normalization Layer:** Receives $z$ as input and normalizes it.
	 $z$ $\to$ Apply Batch Norm $\to$  $\hat{z_{i}}$ as $\text{Normalized} \space z$" $\to$ Output $y_{i} = \gamma \hat{z_{i}} + \beta$   as the final Normalization value.
3. **Activation Function (ReLU):** Receives the *normalized output from Batch Norm.*

*Batch Norm process include 2 step:*
To normalize all inputs $z$, we would need to calculate the normalization value of each $z$.
![[Pasted image 20251212155124.png]]
*For the Normalization layer to be more flexible*, we *implement 2 learnable parameters $\gamma$ (scaling) and $\beta$ (shifting)* (update the same as like weight as bias). Where *1 Scale* the original Normalization value and *1 shift to Stabalize* the normalization value.
$$y_{i} = \gamma \hat{z_{i}} + \beta$$
(*Output* annotate as $y_{i}$ to *seperate from the original unormalized value*)
The flexibility *help avoid these problem:*
1) **Restoring Parameters:** Simply forcing every layer's input to be a standard normal distribution (Mean=0.5, Std=0.5) might be too restrictive and could limit the network's ability to represent complex patterns. **These parameters allow the network to "undo"** the normalization **if it decides that the raw distribution was actually better for learning.**

2) **Optimial Activation Range:** **Different activation function work best with different input ranges.** For example, if the network needs the inputs to be slightly shifted to the positive side to activate a ReLU more often, it can learn a positive $\beta$. If it needs the data to be more spread out, it can learn a larger $\gamma$.

3) **Recovering:** *In theory dividing $\gamma$ is the opposite of dividing $\sigma_{\beta}$ and adding $\beta$ is opposite of subtracting $\mu_{\beta}$.* Since the network learn both $\gamma$ and $\theta$ during backward propagation, it can recover the original input $z_{i}$ exactly. This guarantees that BatchNorm doesn't lose any information, it just recognize it to make training easier.
+ $ Conclusion: *Batch Normalization help stabalize weight and bias* value and *improve convergence* speed since value are minimize to only 0 and 1 *during Training*.

+ ? So we Batch Normalization optimize parameters during Training, *what about optimization method during Initializtion*. Well, we have "He Initialization".

**He Initialization** design solely for ReLU.
+ Keep variance stable from the start.
+ Better Gradient from the start.
+ Less Negative Weight and Bias from the start.

---

### LeNet
+ $ **Cải tiến:** Lookback Mechanism and Gaussian Connections.
![[Pasted image 20251219205304.png]]
**Cơ chế Lookback:** Học features từ các bảng trước đó.
![[Pasted image 20251219205140.png | 255]]


### AlexNet
+ $ **Cải Tiến:** Overlapping Max POOL, thay Tanh -> ReLU, Drop Out (Drop tham số mỗi lớp về 0 vs xs 0.5%)
![[Pasted image 20251219210919.png]]

![[Pasted image 20251219211652.png]]
![[Pasted image 20251219211711.png]]

![[Pasted image 20251219212000.png]]

### ZFNet -> Foundation of CNN Visualization
+ ? fintuning AlexNet. ![[Pasted image 20251219212014.png]]
+ $ Cải tiến: Max Unpooling.

![[Pasted image 20251219212022.png]]

Dùng Unpooling để dịch ngược lại. ie. *Obtain an approximate inverse by recording the locations of the maxima.*
![[Pasted image 20251219212133.png]]

**DeConvolution technique for Visualization: reverse of Conv**
![[Pasted image 20251219212438.png# left | 455]]
**How DeConv work ?**
![[Pasted image 20251219212737.png]]
Duplicated Conv get sum. Lấy tổng nhưng phần bị trùng.
![[Pasted image 20251219213240.png]]

![[Pasted image 20251219213345.png]]

Low Frequency: góc cạnh - High Frequency - cong
![[Pasted image 20251219213555.png]]

Aliasing - image become Abstract. Alias Example:
(Layer 2: (c) Aliasing artifacts in AlexNet and (d) much cleaner features in ZFNet)
![[Pasted image 20251219214054.png | 444]]

Nhận xét sau khi xác định Điểm Yếu -> Cải tiến Layer 1 + 2.
![[Pasted image 20251219214202.png]]

**Các phương pháp Normalization**
+ Normalize theo Channel.
+ Local Response Normalization ![[Pasted image 20251219214455.png]]
![[Pasted image 20251219214649.png]]

![[Pasted image 20251219214732.png]]

+ ? Bản thân trong 1 class có hiện tượng Shifting cái Features. Cần có cơ chế can thiệp để xem cái scale và shift tương ứng.
+ $
![[Pasted image 20251219214927.png]]

### VGG16Net (VGG 16 lớp)
Nâng số lớp theo Compute của thời đại.

### GoogleLetNet: Inception Net
+ ! VGG thêm số Lớp nhưng không giả quyết đc vde Gradient Vanishing. **VGG add more layers but not Improving.**
Sử dụng kĩ thuật **1x1 Conv.**
**Sử dụng kĩ thuật Trung Gian để giảm số lượng Params xuống.**
![[Pasted image 20251219220229.png]]

Hỗ trợ cái Non-Linearity.
![[Pasted image 20251219220544.png]]

Add 1x1 Conv at the beginning to reduce total Features ( asl well as params)
![[Pasted image 20251219220714.png]]

Cách chọn kiến trúc và số lớp -> thử nghiệm và ra đc V2 Module.
![[Pasted image 20251219220904.png]]

![[Pasted image 20251219221017.png]]
+ ! Still suffer from Exploding and Vanishing Gradient. Unable to Improve Accuracy by Increasing Layer.

### ResNet
+ $ **Skip-Connection.** Allow up to 34 Layers.
Càng nhiều Layer thì Error càng lớn, Layer cuối càng có ít thông tin từ Layer đầu hơn.
![[Pasted image 20251219221215.png]]

![[Pasted image 20251219221428.png# left | 322]]

Ý tưởng là giữ lại đặc trưng gốc từ Layer đầu.
![[Pasted image 20251219221400.png# left | 255]]

Back Prop qua Skip-Connection.
![[Pasted image 20251219221844.png]]

### MobileNet
1.Using Depthwise Separable Convolutions (2D Conv)
	Pointwise Conv (1D Conv)
2.Using two Shrinking Hyperparameters:

**Network in Network and 1x1 Convolution**

**2D Convolution -> Depthwise Parameters**
Giảm số lượng


## ResNet
+ @ reference paper: Deep Residual Learning for Image Recognition
![[Pasted image 20251221202824.png]]

+ ! **Motivation:** Vanishing Gradient.
+ $ ResNet uses **residual connections** to allow deeper layer learn Previous layer features without forgetting it.
	Enable **easier training and improve performance as depth increase.**

**Resnet Bypass layers by adding shortcut paths.**
![[Pasted image 20251221203931.png | 433]]
+ Enable the network to learn residual functions instead of direct mappings.
+ Allow gradients to flow more easily through the network.
+ Make optimization smoother and training more stable.
+ Accelerate convergence during training.
+ Enable the training of deeper models with improved accuracy.
+ ? When apply derivative, only the relevant information get kept. (Verify THIS LATER)

## DenseNet

