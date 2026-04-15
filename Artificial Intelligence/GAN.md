[[KL Divergence]]
[[Math Behind Generative Adversarial Networks]] - [fomula proof](https://en.wikipedia.org/wiki/Generative_adversarial_network)
[Medium - GAN Detail Explain from Paper and Code](https://medium.com/ai-society/gans-from-scratch-1-a-deep-introduction-with-code-in-pytorch-and-tensorflow-cb03cdcdba0f) 
Understanding Latent Space in Machine Learning 
[Reference GAN Code](https://ubc-mds.github.io/DSCI_572_sup-learn-2/lectures/08_advanced-deep-learning.html)
[Wasserstein Loss Detail](https://machinelearningmastery.com/how-to-implement-wasserstein-loss-for-generative-adversarial-networks/)

GAN HW + GAN Code Interchangbly
	FreeTime Visualize All GAN Generation Image

## Why GAN ? 
![[Pasted image 20260413150343.png | 555]]
+ ! Training data is limited for the model to understand and replicate the Original image. 
-> with limited data, we could at least *leverage data mean and std.* 
+ $ So when we talking about GAN, we talking about matching data distribution. To achieve that we use GAN architecture and its MiniMax Objective function. 


*Discriminator Objective Function Explain*
![[Pasted image 20260413154026.png]]
$$L_{D}(z,x)=-y\log(D(x))-(1-y)\log(1-D(G(z)))$$
+ $x$ as real image, $z$ as the noise, $G(z)$ as the generated image using noise.
+ Binary classification network mean the labels is either 0 or 1. So only 1 loss term existed when classified. 
+ *1st term - Real Loss:* $\log(D(x))$ có $D(x)$ càng *tăng* thì $log(D(x))$ càng *nhỏ* -> *Better Real Image  classification the Lower the Loss.*  
+ *2nd term - Generated Loss:* $(1-y)\log(1-D(G(z)))$ with $D(G(z))$ consider as Generated Accuracy -> *higher generation acc mean lower Generated Loss*. 
Note: divided by 2 to take the average of the Loss.


### Re-Explain GAN
**In short,** GAN include 2 model, the Generator and the Discriminator. Each have its own role, imagine the generator is the thief want to prints fake money that look the same as real money, and the Discriminator is the police trying to expose the thief. They *compete against each other in a zero-sum game* (ie. if 1 win, the other lose).

*Training (zero-sum game and Equilibrium)* - GAN training sturctured as a Minimax game where the gain of 1 model is the loss of the other -> simply, there're 2 loss term in the loss func, if the Discriminator loss Decrease then the Generator loss Increase.

1 common question is which model get trained first and later ? or both at the same time ? 
	Alternating training

Training ended when the Discriminator can't distinguished Generated/Fake image from Real Image.
-> what is the Equilibrium for this. 50% (the same as random guesses or flipping a coin)

GAN is a Binary Classification problem. So no label required -> Unsupervised learning.

**Key Architecture Components**
*Latent Space input -* input noise like Gaussian Noise to Generation model. The Generated image then get Evaluate by the Discrimination model and classified as Real/Fake. Finally update Generator gradient by backpropagation from the Discriminator output back to the Generator.    

*Generator Network -* often uses trainposed conv layers (or "deconvolution layer") to upsample low-dimensional noise into a high-resolution image.

*Discriminator Network -* often use a CNN to output prob (0 to 1) indicating Real or Fake. 


**Key Challenges** 
1. First of we need to talk about *Training Balance*, because traning is constantly switching between the 2 network -> *training could be unstable and difficult* -> leading to oscillation or the failure to converge. 

2. *If the Generator CHEAT* (ie. found a shortcut to trick the discriminator) by producing a **very limited variety** of outputs rather than mapping the entire variety of the data distribution, this would cause *Model Collapse (GAN fail to learn)* - the Generator Cheat bc its zero-sum game.
	
	Type of model collapse: 
	1. *Lack of Diversity -* instead of generating all digit in MNIST (1-9) and capturing the full complex distribution of data, it *only generating number 1 while ignoring every other digits* bc 1 have the highest accuracy (*mô hình sợ sai*)
	2. *Repetitive outputs -*  like "lack of diversity", only Generate 1 or 2 samples.
	3. *A "Helvetica Scenario"-* like the above, regardless of the noise input, the generator consistantly  generate 1 types of character bc it always fools the discriminator. 
	
![[Pasted image 20260413161521.png | 555]]

2. *Vanishing Gradients -* Generator quire feedback to update its gradient like MLP, but if the *discriminator becomes too strong* too quickly, *this mean generated image look so fake, the discriminator confidence is always $D(x) = 1$ $\leftrightarrow$  $log(1) = 0$* (ie. loss always 0) making backprop useless causing learning to stop. 

## Decompose GAN Architecture 
This is what G and D see during Training. 
![[Pasted image 20260414114436.png]]
GAN as a Whole. 
![[Pasted image 20260414114508.png]]



## Practice GAN
Xét một Generator với kiến trúc như hình dưới đây. Giả sử đầu vào của Generator là noise vector `z` có kích thước 100 × 1 × 1, vector này qua bước project and reshape, `z` được biến đổi thành feature map ban đầu kích thước 4 × 4 × 256. Feature map này tiếp tục đi qua 3 lớp `ConvTranspose2d` để tăng kích thước không gian như sơ đồ dưới đây.
![[Pasted image 20260413164559.png]]
Featue Map (`H x W x C`) sau khi đi qua Generator.


