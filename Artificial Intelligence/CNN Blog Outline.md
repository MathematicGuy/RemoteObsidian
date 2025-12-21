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
	For each Operation explain. What it do ? Why do we need it ?
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
Note: 
+ Why use addition but not other function for merging feature ?

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

