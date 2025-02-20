### Topic
**(1) What is an Edge**
**(2) Edge Detection Using Gradients**
**(3) Edge Detection Using Laplacian**
**(4) Canny Edge Detector**
**(5) Corner Detection**
[vid](https://www.youtube.com/watch?v=Z-65nqxUdl4&t=9388s)
### What is an Edge
+ ? **Cause of Edges:** **Rapid/Sudden changes in image intensity are caused by varios physical phenomena**.
![[Pasted image 20250219162602.png]]

### Type of Edges
![[Pasted image 20250219162749.png]]
### Edge Detector
Edge Detector produces:
+ Edge Position
+ Edge Magnitude (Strength)
+ Edge Orientation (Direction/Angle)

Performance Requirements:
+ High Detection Rate (Low False Positive and False Negative)
+ Good Localization -> Detect edge excactly where it take place.>
+ Low Noise Sensitivity. 

## Edge Deteciton Using Gradients
### 1D Edge Detection using 1st Derivative 
>Edge is a rapid change in image intensity in a small region
![[Pasted image 20250219094518.png]]
+ ? **Derivative** of a **continuous function represents the amount of change in the function**. So derivative should be extreme at edge position.
+ $ Derivative of `f(x)` reach maxima when light intensity increase rapidly, and minima when light intensity decrease rapidly. We just want to detect edges, so the absolute of `f(x)'` would be fit for ours case.
-> Absolute `f(x)'` tell use where the edges are and their magnitude.
![[Pasted image 20250219094740.png]]


### 2D Edge Detection in Continuos domain
![[Pasted image 20250219163805.png]]
+ ? **Partial Derivatives** of a 2D continuous function represents the amount of change along each dimension. 
+ $ Taking account for both x and y derivative, we got the gradient. 
-> Gradient (Partial Derivative) represents the direction of the most rapid change in intensity. 
![[Pasted image 20250219095509.png]]

Gradient $\nabla$ as Edge Detector
![[Pasted image 20250219133749.png]]
Now we know how derivative can be calc in continous domain, let see how we might implement to a discrete image.  
 
+ ? We know that derivative are implemented using finite differences when it comes to discrete images. 
To find the diff you need at least 2 pixels where the physical distance between 2 pixels is $\epsilon$ (i.e. epsilon) 
![[Pasted image 20250219134011.png]]
Matrixfy the equation, we see these 4 points can be implemented as Convolution (i.e. convo detect x-axis and y-axis)
![[Pasted image 20250219134135.png]]

![[Pasted image 20250219154743.png]]
**Small Operators (kernel):** Good localization, Noise sentive, Poor Detection.
**Large Operators (kernel):** Poor Localization, Less Noise Sensitive, Good Detection. Because the edge is more likely to be influent by sth else.

#### Edge Thresholding
![[Pasted image 20250219155038.png]]
**Hysteresis Based** is just Stadard thresholding but its see **value in between the 2 thresholds as edges if they're neighboring pixels**.

## Laplacian: using $2^{nd}$Derivative to detect edges
+ **zero-crossing:** refers to the point on a graph **where the derivative of a function crosses the x-axis.** (literally) Meaning the derivative of f(x) when crossing x is zero. This indicate the location where the function changes in direction (i.e. increase to decrease and vice versa).

![[Pasted image 20250219165015.png]]

![[Pasted image 20250219165443.png]]

![[Pasted image 20250219165458.png]]
+ ? 2 $\epsilon$ because after calculating, **the equation divided to $\epsilon$ again.**
 + $ The original conv mask can't detect 45 degree angle bc of the 0 across the diagnol. So the Laplacian operator was modified to be more accurate. 
![[Pasted image 20250219200942.png]]

### Effects of Noise
>It disrupt edges detection completely
![[Pasted image 20250219201056.png]]
+ $ We **need to suprress the noise** before apply any operator. For instance, using **Gaussian Smoothing**.
	The peak of $\nabla( n_{\sigma} * f)$ is indeed match the edge.  
	![[Pasted image 20250219201232.png]]
+ ? We know that Gaussian Smoothing is Linear. Therefore we can find the 1st derivative of the Gaussian, then apply the derivative to the noise signal and got the location of the edge. ![[Pasted image 20250219201924.png]]
+ $ From **the method above**, it **proof** that we can **detect edge by finding the derivative of the gaussian without smoothing the image first**. Apply Laplacian 2nd derivative and we got 

**Laplacian of Gaussian** ($\nabla^2n_{\sigma}$ or $\nabla^2G$)**.
![[Pasted image 20250219202524.png]]

![[Pasted image 20250219202653.png]]

![[Pasted image 20250219202835.png]]

