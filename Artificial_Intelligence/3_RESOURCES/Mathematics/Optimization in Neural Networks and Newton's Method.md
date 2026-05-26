![[Pasted image 20241002102152.png]]
note: $\sqrt{ 2 }$ is the positive solution for $x^2-2=0$.  ($\sqrt{ 2 }$ is the result of $x^2-2$)


![[Pasted image 20241002102158.png]]
+ $ The smallest value converge the faster


![[Pasted image 20241002102203.png]]
+ $ Newton's Method Convergence: the method will refine the guess (i.e. negative value) in the direction of the closest root. If $-\sqrt{ 2 }$  is closer than $\sqrt{ 2 }$  then its will converge to $-\sqrt{ 2 }$. In reverse if the initial point is possitive.


![[Pasted image 20241002102213.png]]
+ $ replace $f(x)$ with Newton's Method fomula.


![[Pasted image 20241002102220.png]]
+ $ For recursion formula: Newton's Method $f(x)$ will take another derivative as $f(x)$ thus making $\frac{f(x_{k})}{f'(x_{k})}$ become $\frac{f'(x_{k})}{f''(x_{k})}$


![[Pasted image 20241002102226.png]]
+ $ For 2nd Derivative Local Minimum when $f''(x) > 0$ 


![[Pasted image 20241002102241.png]]
+ $ Apply Hessian matrix fomula which calc the derivative in respect of x and y of f(x, y) 2 times.


![[Pasted image 20241002102250.png]]
+ $ Parameters are define as variables of the model like: Weights $w$, Biases $b$ (i.e. a constant). There're 3 layers:
	+ Input Layers contain 4 inputs (3 vars, 1 bias). Each input are connected to each nodes, Each Connection create a parameter (e.g. $z_{1}^1$): So 4 inputs and 3 Nodes mean **12 parameters.** 
	+ Hidden Layer have 3 layers, 1st layer have 3 nodes and 1 bias making 4 inputs in total,  2nd layer have 2 nodes and 1 bias that is 3 inpouts in total, 3rd layer have 1 nodes. Each inputs connected to each nodes making **$4.2 + 3*1 =$ 11 parameters**.
	+ The result then return at the output layer.
	-> So 12 +11 = **23 parameters in total.**

![[Pasted image 20241002102257.png]]
+ $ To find $\frac{\Delta L}{\Delta w_{1}}$ we first need to find its derivative. We have: 
	+ $z=w_{1}.x_{1} + w_{2}.x_{2} + b$ 
	+ $\hat{y}=\sigma(z)$ and $L(y, \hat{y})$. This Mean $L$ is depending on $\hat{y}$ and $\hat{y}$ is depending on $w_{1}$ (not $z$ because we want to extract variable inside z)  		
		![[Pasted image 20241002111415.png]]
	+ So apply the chain we, we got:
		![[Pasted image 20241002111835.png]]
	+ $\frac{\Delta\hat{y}}{\Delta w_{1}}$ is just $x_{1}$. And the Derivative of L with respect of $\hat{y}$ is
		![[Pasted image 20241002112136.png]]
	+ Combine the result we get:
		$$-(y-\hat{y})x_{1}$$


![[Pasted image 20241002102307.png]]
+ 2 Derivative having Hessian Matrix All Positive -> Local Minimum.