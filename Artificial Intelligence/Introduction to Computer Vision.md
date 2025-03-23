	### RGB Color
> Red, Green, Blue each 256 color degree (i.e. 256 different way to represent each color respectively)
![[Pasted image 20241008165504.png]]

![[Pasted image 20241008165634.png]]
> Image present in pixels, 800x600 Dimensions mean 800 rows and 600 columns of pixel value in size. Using i and j for row and column indexes, the image can be present in Matrix format:
> ![[Pasted image 20241008165940.png]] 
> Each $w_{ij}$ as a color pixel value: (e.g single color pixel: (0, 0, 256), pixel with 2 colors combine (0, 233, 256))
> ![[Pasted image 20241008170049.png]]
> For the sake of storage and processing 3 parameters (r,g,b) we have each pixel as a seperated matrix:
> ![[Pasted image 20241008170432.png]]
> Each $w_{ij}$ seperate as $(r_{ij}, g_{ij}, b_{ij})$ in general:
> ![[Pasted image 20241008170522.png]]
```ad-summary
To optimize storage and process, we divide each pixel values to 3 matrix: (r, g, b) which represent red, green and blue. 
```

### Tensor
1D: a vector (a)
2D: a matrix (a * b)
Larger than 2D: a tensor (a * b * h) (with h as the image's depth)
	(e.g. 3D tensor, 4D tensor, 5D tensor)
	![[Pasted image 20241008171009.png]]
Thus, an image is a 3D tensor since each pixel value present by 3 matrix r, g and b collapse on top of each other. So 3D tensor for 800x600 image is 800x600x3 
	(with 3 as the depth of the image)
	![[Pasted image 20241008172056.png]]


The same logic for Grey scale image (i.e. black and white image). It still have 800x600 pixels but only need 2 color ranging `[0, 255]` (i.e. back and white) instead of (r, g, b). 
	![[Pasted image 20241008172519.png]]
	Therefor, we only need 1 matrix because each only need 1 variable. 
	(0 is black and 255 is white, the closer value to 255 the whiter it is)
	![[Pasted image 20241009084232.png]]

### Convolution Operant (Operation)
![[Pasted image 20241009085231.png]]
	X as the 6x6 matrix.
	Grid as the 3x3 matrix grid choosed from X.
	W as the k by k matrix (k is a odd number like 1,3,5,7,9, etc)  
	With each element fit the 3x3 matrix grid X perform: 
	$Y= X\otimes W$:  Sum of X multiply with W element-wise, equal Y.$$y11​=sum(A\otimes W)=x11​∗w11​+x12​∗w12​+x13​∗w13​+x21​∗w21​+x22​∗w22​+x23​∗w23​+x31​∗w31​+x32​∗w32​+x33​∗w33​=4$$
	X outer layer cannot fit through the 3x3 grid to perform maultiplication, so we just remove it.
	![[Pasted image 20241009090137.png]]
	and calculate the rest
	![[Pasted image 20241009090250.png]]

### Padding
As the example above show that we loss the outer layers of X, inorder to keep its. We simply add an additional layer called Padding to X. Now 3x3 grid can fit perfectly to X thus reserve the whole matrix.
	![[Pasted image 20241009090857.png]]
+ Padding = 1 mean add k layers of 0 to X matrix.

### Stride
> How much the convolution filter (i.e. kernel) shifts across the input image. Instead of sliding the filter one pixel at a time.
> For Stride=k (k>1).  convolution operantor can only apply to:
$$x_{i*k, \space j*k}$$
![[Pasted image 20241009091253.png]]
> This simply start from $x_{11}$ then each turn step from left to right and down if reach the border. repeat until the end of the matrix.
	[Visualization](https://github.com/vdumoulin/conv_arithmetic)
> Fomula for Convolution Operation of Matrix X with kernel (filter) k * k, stride s, padding p is:
> ($height * width$)
> $$\left( \frac{m−k+2p}{s}+1 \right)∗\left( \frac{n−k+2p}{s}+1 \right)$$
- **m−k:** This accounts for the **size reduction caused by the kernel size.** Since the kernel covers some portion of the input, each step of convolution reduces the effective size.  
	
- **+ 2p:** **This adds back the padding**, which compensates for the size reduction by extending the input size. Since 1 padding conpensates 1 layers which also is 2 size.
	
- **/s:** This divides the result by the stride. Larger strides reduce the output size since the filter "jumps" over more input pixels, processing fewer positions. (Think dividing like you have 6 pizza piece, you can only eat 2 pieces at once thus you can only eat $6/2=3$ times) - this represent how many times the grid can move with stride.
	
- **+1:** This adjusts for the fact that we still get one valid position even after accounting for the above operations.
+ ? By applying stride ours convolution called strided convolution.

### Purpose of Convolution
> To Manipulated base image using a Kernel as filter to change and see a certain aspect of the image.
![[Pasted image 20241009093042.png]]

### Edge Detection
![[Pasted image 20241008144323.png]]
+ ? **filter**: n by n matrix contain used to extract features from images by **sliding** over the image. (e.g. 3x3, 5x5, 7x7 matrices)
+ ? **input matrix:** n by n matrix  representing the image in pixels value
+ ? **stride**: number of steps the filter move at a time. (e.g. A stride of 1 means that the filter moves one step at a time, both horizontally and vertically.)
+ $ The Sliding work like this in the 6x6 image, **chose a 3x3 grid** start from the top left and **multiply the 3x3 grids with the filter element-wise** then sum all that values together to update the 3x3 grid center value (i.e. -5). The sliding move from left to right for each 3x3 grid in the matrix (that not been slide)
	
+ ? Argument prove how 6x6 filter into 4x4 matrix:
	+ ? Call the outer layers as the matrix's margin which include the top margin (1 row), bottom margin (last row), left margin (left column) 
	+ $ (1) : A 6x6 Matrix removing its top & left margins, we got a 5 by 5 matrix. Then removing bottom & righ margins, we got a 4x4 matrix. (yes)
		-> **remove its margin**, remove 2 layers.
	+ $ (2): The 3x3 grid filter it margin while keeping only the center value. In Knowing that 3x3 grid need at least 3 rows (i.e. top/bottom) and 3 columns (i.e. left/right) bc it cannot compute a valid if go out of bound, so sliding a 3x3 grid through the 6x6 matrix will exclude 6x6 margin.
		-> In other word, **remove its margin**.
	(1) + (2): sliding 3x3 grid through 6x6 while only keeping the 3x3 grid center value will leave us with a 4x4 matrix. 
	![[Pasted image 20241008164220.png]]


### Convolution Neural Network
#### Neural Network Problem
A color image 64x64 present in 1 tensor as 64x64x3. So the input to the NN would be 64x64x3=12288. Meaning network have to process 12288 nodes. If the 1st hidden layer is 1000, the paramater numbers would be outstraged. We need a better solution !!!
+ $ Apply convlution operator in Neural Network to process large scale image while keeping its core features.

#### First Convolution layer
+ ! CNN Color Channel doesn't mean CNN Dimension. e.g. r,g,b and bg image both use 2D CNN. 3D CNN refer to when we processing 3 frame at a time of a video to extract the spatial temporal information (thông tin không gian thời gian). Basically, CNN capture information in the represent and future/past at once by process 3 frame at a time. 

> Goals: Minimize Data size while maintaing its core features.
> As for 3D 64 x 64 x 3 images (H x W x D) 
![[Pasted image 20241009100137.png]]
>Convolution act the same but its the sum of 3 matrix $Y = Yr + Yb + Yg$
![[Pasted image 20241009100122.png]]

Padding and stride rule are the same. (the same dimension, calculation method)
![[Pasted image 20241009102425.png]]
note: 
+ $F*F*D$ : kernel shape and Dimension (3x3x3, 3 3x3 matrices) output of a convolution layer will pass through activation function before become the input of the next convolution layers.
	
+ Each Kernel's value $\otimes$ each available input value + 1 (1 as bias) thus the total parameters of a convolution layers are: $F*F*D + 1$. And convolutio layer apply k kernel so the total parameter of a layer is $K*F*F*D + 1$

#### Pooling Layers
> Use to compress image while still maintain its core features. 
> It work like this: slide a FxF grid through X matrix and apply max pooling or average pooling:
	+ max pooling: choosed the maximum value of the FxF grid 
	+ average pooling: get the average value of the FxF grid.
	![[Pasted image 20241009105509.png]]
>
> Pooling layer often used size=(2,2), stride=2, padding=0. to remove half of the input while maintaining depth.  
	![[Pasted image 20241009105416.png]]
+ ? In some model, people use convolutional layer with **stride > 1** to decrease data size instead of pooling layer.

### Fully Connected Layer
> After the images passing through convolutional layers and pooling layers, the model have learned a lot about the image's features then the tensor of the last output in the last layer size $W*H*D$ will be flattern into 1 single vector with the same size $W*H*D$.
>![[Pasted image 20241009110927.png]]
>After that we used fully connected layers (with activation like relu, softmax, etc...) to output the final result.

### Visualise Convolutional Neural Network
> Input image -> Convolutional layer (Conv) + Pooling layer (Pool) -> Fully connected layer (FC) -> Output.
![[Pasted image 20241009111146.png]]

covolution: tích chập
