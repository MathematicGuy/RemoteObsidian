### 1D Edge Detection using 1st Derivative 
>Edge is a rapid change in image intensity in a small region
![[Pasted image 20250219094518.png]]
+ ? **Derivative** of a **continuous function represents the amount of change in the function**. Edge represent the most change between color intensity.
+ $ Therefor 1st derivative should return the local Extreme indicate Edges in a small region. Simple as that  
![[Pasted image 20250219094740.png]]

### 2D Edge Detection in Continuos domain
+ ? Take account for both x and y axies, we got the gradient. 
-> Gradient (Partial Derivative) represents the direction of the most rapid change in intensity. 
![[Pasted image 20250219095509.png]]

Gradient $\nabla$ as Edge Detector
![[Pasted image 20250219133749.png]]
Now we know how derivative can be calc in continous domain, let see how we might implement to a discrete image.  

To find the diff you need at least 2 pixels where the physical distance between 2 pixels is $\epsilon$ (i.e. epsilon) 
![[Pasted image 20250219134011.png]]
Matrixfy the equation, we see these 4 points can be implemented as Convolution (i.e. convo detect x-axis and y-axis)
![[Pasted image 20250219134135.png]]


