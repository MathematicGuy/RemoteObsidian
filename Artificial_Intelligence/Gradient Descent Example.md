![[Pasted image 20240930102108.png]]
Starting Point (x=0.05x=0.05):
	The function we want to minimize is f(x)=ex−log⁡(x)f(x)=ex−log(x).
	The gradient of the function is f′(x)=ex−1xf′(x)=ex−x1​.

Step 1:
	At x=0.05x=0.05, the derivative is f′(0.05)=−18.9f′(0.05)=−18.9.
	The update rule is: xnew=xold−α⋅f′(xold)xnew​=xold​−α⋅f′(xold​).
	With a learning rate of α=0.005α=0.005, we get:
	x→0.05−0.005×(−18.9)=0.1447
	x→0.05−0.005×(−18.9)=0.1447
	This means the next point is x=0.1447x=0.1447.

Step 2:
	At x=0.1447x=0.1447, the derivative is f′(0.1447)=−5.7552f′(0.1447)=−5.7552.
	Update xx again:
	x→0.1447−0.005×(−5.7552)=0.1735
	x→0.1447−0.005×(−5.7552)=0.1735
	This process continues, each time moving xx closer to the minimum point.