[doc](https://nttuan8.com/bai-6-convolutional-neural-network/)
### What is Convolution ?
+ ? An Image contain 784 pixels, **is there a way to condense the images down to the important features that distinguish a shoes a shoes** or a bag a bag.
	Yes, it involve passing a filter over the image in order to change the underlying image.
+ $ Convolution work like this, for every pixel, look at the value of its neighbors (i.e. adjacent pixel), then update the pixel value by multiplying the filters with the corresponding 3 by 3 grids which contain the pixel.    
![[Pasted image 20241007154310.png]]
+ ? Filters can change the base image, useful for detecting features (e.g. brighten image filter to see dark tone image clearer)
![[Pasted image 20241007154404.png]]

### What is Pooling ?
> pooling is a way of compressing image.
+ ? i.e. **for every 2 by 2 grids, choose the biggest value**. This trick **preserve the features that were highlighted by the convolution** while simutanuously quartering the size of the image.
	![[Pasted image 20241007154716.png]]

### Implementing convolutional layers
![[Pasted image 20241007160328.png]]
+ $ The goal of the Convolution layers is to filters out the features that determine the output. In short, simplified it.

**Element-Wise**
	![[Pasted image 20241007170226.png]]

