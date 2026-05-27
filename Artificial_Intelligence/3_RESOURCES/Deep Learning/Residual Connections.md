Resnet use for Deep Neural network (>10, 20 layers) to solve Gradient Vanishing problem in deep NN layer -> Allow Deeper NN -> Deeper NN allow higher accuracy and better learning. This is because:
+ Gradien is Information, and due to how activation function and backprop work gradient vanishing as the layers deeper. Using Skipconnection help preserve these information -> Better Learning -> Faster Convergence\
	[quick explain in kaggle](https://www.kaggle.com/discussions/general/543200)
+ ! Don't use ResNet for Shallow Network (e.g. 2-3 layer CNN), skipconnection might add extra complexity. 

Basic Ideas of Residual Connection is to pass information between NN layers throught a intermediate activation function -> This mean keeping the Input/Output dimension the same.

**How to apply Residual Block** - code Identify Block (another name for residual connection)
The most common way to use residual connections is to place them inside blocks that do **not** change the spatial size or the channel depth.
```python
class ResidualBlock(nn.Module):
	def __init__(self):
		
```

Simple logic for how Kernel, Stride, Padding for Conv2d and TransposeConv2d *transform the image size:* 
+ Conv2d: kernel subtract X, padding add 2X and Stride divided by image by X. X is equivilent to 1 pixel.
+ TranposeConv2d is opposite: kernel add 1X, padding subtract 2X while stride multiple by X and output_padding add 1X. 

![[Pasted image 20260422181925.png]]


