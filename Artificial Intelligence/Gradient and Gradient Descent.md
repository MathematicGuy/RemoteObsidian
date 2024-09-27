[Article Explain](https://viblo.asia/p/optimizer-hieu-sau-ve-cac-thuat-toan-toi-uu-gdsgdadam-Qbq5QQ9E5D8) 
# Lesson 1: Gradient

### Intro: Tangent Plane
Tangent Plane: mặt phẳng tiếp tuyến
	contain the tanget lines of more than 2 tangent lines.
	![[Pasted image 20240805104205.png]]

### Partial Derivative - Part 1 (Đạo hàm riêng)
+ ? **A partial derivative is derivative taken with respect to 1 variable while keeping all other variables constant.** It is used when u are dealing with functions with multiple variable.
> In simpler terms, partial derivative mean to calculate the derivative of each variable, it measures how a function changes as 1 of its variables changes, while others remain fixed.  
	![[Pasted image 20240805102659.png]]
	![[Pasted image 20240805102942.png]]
+ $ Treat the not derivative one as a Constant. Ex: Derivative of x, see y as a constant. 
	$f_{x} = 2x$ and $f_{y} = 2y$

```ad-check

```

### Partial Derivative - Part 2
$f(x, y) = 2x^2y^3$
$=> f(x,y) = 6xy^3$
	![[Pasted image 20240805103507.png]]

### Gradient
	![[Pasted image 20240805105716.png]]


### Gradients and maxima/minima (Start Here)
+ $ Normaly to find the minimum of a 2D, we find the derivative of the graph and set it to 0. The same apply to 3D
+ ? **Minimum is when slope = 0 <-> Both Slopes of x and y is 0 while z stay fixed**
	![[Pasted image 20240805105858.png]]
To Calculate the the function minimum, we **calc the Derivative of 2 variables and set it equal to 0.**
	![[Pasted image 20240805110029.png]]

### Optimization with gradients: An example (in 3D)
+ $ $Motive: Find the **Coldest place in the Sauna Room** -> The coldest place in the room is when every other direction you walk are hoter.
	![[Pasted image 20240805110428.png]]
	To get to that Coldest position we calc the Partial Dervative, we see that it symmetric to the floor.
	![[Pasted image 20240805110505.png]]
	**Example:**
	1) **Calculate the Partial Derivative of f(x,y) which is the derivative of X and Y respectively**![[Pasted image 20240805111430.png]]
	2) **Set the Partial Derivative = to 0:** $$\frac{\delta f}{\delta x}, \frac{\delta f}{\delta y} = 0$$![[Pasted image 20240805111648.png]]
	We notice there are some point outside of the Sauna, so just remove those invalid values. 
	+ $ Insert x, y back to the function, we see that x=4 and y=4 it the Minimum of the function. ![[Pasted image 20240805111837.png]]

### Optimization using Gradients - Analytical Method (Important)
> Back to power line example, the cost is the area of the square starting from the points to the line.
	![[Pasted image 20240805154215.png]]

+ Before calc the total cost, we need to calc the cost from 1 point like a to b first, with x = 1, we have y=m+b. So the cost from a to b is $(m+b - 2)^2$ for blue. for orange is $(2m + b - 5)^2$, for green is $(3x + b - 3)^2$.
	![[Pasted image 20240920164817.png]] 
+ $ Therefor the total cost is the sum of these 3 numbers, thus we got the **cost function**
![[Pasted image 20240920165550.png]]


+ ? find the partial derivative of E with respect to m (only dervi m; b constant)
+ ? find the partial derivative of E with respect to b (only dervi b; m constant)![[Pasted image 20240805155408.png]]
Now we set both equal to 0. 


**Goal: Minimize sum of squares cost.**
multiply by 2.
subtract to the first equation -> get m
plug the answer back to the 2nd equation -> get b 
![[Pasted image 20240805160346.png]]
**This actually call Linear Regression: Optimal Solution**
>Which use to solve a problem where you have a bunch of points and
   you try to find the closest line to them
![[Pasted image 20240805160427.png]]
+ ? Is there a easier way to do this => Gradient Descent 
[[Partial Derivative and Gradient HW]]

## Optimization using Gradient Descent in 1 Variable
### Hard to Optimize Functions
![[Pasted image 20240809053708.png]]
+ ? Is there any other way ???

Gradient Descent allow you to find the minimum point by allow the function to jump big step when the Slope is Large, and small step when the Slope is small.
![[Pasted image 20240809054927.png]]
![[Pasted image 20240809054947.png]]

![[Pasted image 20240809054718.png]]
![[Pasted image 20240809054047.png]]
> $\alpha$ must be small enough to find the minimum point. 
```ad-summary
x is the Initial Starting Point inside the f(x) range
f'(x) is the Derivative Line Slope of the function
For every Iteration: we will decrease from x to find the minimum point
	$x_{k}= x_{k-1} - a.f'(x_k -1)$  
```


## Optimization using Gradient Descent in one variable - Part 3

+ ? What is a good learning rate
	Unfortunately, there is no rule to give the best learning rate $\alpha$

![[Pasted image 20240809055753.png]]
+ ? If we run Gradient Descent for 1 Slope, it may only be the local minima. To solve this, take multiple starting point for gradient descent.

#### 1. Function with One Global Minimum
![[Pasted image 20240809062209.png]]
First, define function $f\left(x\right)=e^x - \log(x)$ and its derivative $\frac{df}{dx}\left(x\right)=e^x - \frac{1}{x}$: Now let apply Gradient Descent to find the minimum point.
```python
def gradient_descent(dfdx, x, learning_rate = 0.1, num_iterations = 100):
    for iteration in range(num_iterations):
        x = x - learning_rate * dfdx(x)
    return x
```
**Testing Gradient Descent on diff learning rate and X Initial Point**
+ ? Firstly, there're thing to consider. $e^x$ larger when | x | > 1 and 1/x larger when | x | < 1 as you can see in the plot below. So the function will start at a stepper slope when x getting closer to 0, I wonder if the point will go down the slope like a car.
![[Pasted image 20240809065156.png]]
**Let see how x affect finding the global minimum point:**
>Use 'Converged' when the Gradient Descent fin the minimum point succesfully.
+ $ num_iterations = 25; learning_rate = 0.1; x_initial = 1.6
+ ? Perfect. Got minimum point sucessfully at iteration 21![[Pasted image 20240809072021.png]]

+ $ num_iterations = 25; learning_rate = 0.3; x_initial = 1.6
+ ? Each step are bigger. but still Converge. The model Swing like a Pendulum ![[Pasted image 20240809071937.png]]

+ $ num_iterations = 25; learning_rate = 0.5; x_initial = 1.6
+ ? Converged Fail. Each step are too Big to find the Minimum Point. v![[Pasted image 20240809071855.png]]

+ $ num_iterations = 75; learning_rate = 0.04; x_initial = 1.6
+ ? Each Step are too more to reach Convergen![[Pasted image 20240809071819.png]]

+ $ num_iterations = 75; learning_rate = 0.04; x_initial = 1.6
+ ? With more Iteration, the model converge slowly and successfully. But computationally expensive![[Pasted image 20240809071716.png]]

+ $ num_iterations = 25; learning_rate = 0.1; x_initial = 0.05
+ ? For | x | < 0. The function start at a stepper point in the left and take a big first step with (| f'(0.03) | = 32 and gradient descent of x is 3.23) and yes it does go down the slope like a car.![[Pasted image 20240809070953.png]]

+ $ num_iterations = 25; learning_rate = 0.1; x_initial = 0.03
+ ? The first Step is now even bigger, but still manage to Converged.![[Pasted image 20240809071628.png]]
+ $ num_iterations = 25; learning_rate = 0.1; x_initial = 0.02
+ ? The 1st Step is too big, the model is far from home and fail to converge. ![[Pasted image 20240809071450.png]]
+ ? However, If I increase the Number of Iteration and Decrease the Learning Rate I still manage to Converged: **num_iterations = 400; learning_rate = 0.01**. 


+ ? note: x_initial is the starting point, Model mean Gradient Descent model. 
```ad-summary
+ Should start from the least Stepe Slope. Finding the optimal values for Gradient Descent are much easier.  
+ Starting at a Stepper Sloppe can cause the Model become unstable and harder to find the right value to reach the Minimum Point. 
+ The Stepper the Slope. The smaller the Learning Rate. The slower your model can learn.
+ Learning Rate and Iteration need to be just right for the Model to Converged. Think it like a Car Speed and Gas, you can't goes far if your Gas is low and you can't park if you run 100 km/h.
+ X like Your life Starting point. The Stepper it get, the harder life swing and goes. 
```

### Function with Multiple Minima
![[Pasted image 20240809073216.png]]
Testing with 2 diff starting point.
```python
print("Gradient descent results")
print("Global minimum: x_min =", gradient_descent(dfdx_example_2, x=1.3, learning_rate=0.005, num_iterations=35)) 
print("Local minimum: x_min =", gradient_descent(dfdx_example_2, x=0.25, learning_rate=0.005, num_iterations=35)) 
```

+ $ $num_iterations = 35; learning_rate = 0.005; x_initial = 1.3
+ ? Great Starting Point, Converged ![[Pasted image 20240809073142.png]]

+ $ num_iterations = 35; learning_rate = 0.005; x_initial = 0.25
+ ?  Converged. Find Local Minima ![[Pasted image 20240809073351.png]]

+ $ num_iterations = 35; learning_rate = 0.01; x_initial = 1.3
+ ? Learning Rate too high, Can't find be Converged. ![[Pasted image 20240809073459.png]]

## Optimization using Gradient Descent in 2 variables 
Ideas for Gradient Descent
![[Pasted image 20240915140711.png]]
+ ? What is Delta f: $\nabla f$ (delta mean derivative of sth)
	$\nabla f$ as the new (x, y) direction we want to go to. 
	So given curernt as ($x_0 ,y_0$) we can move by a portion of the direction we want to go ($\nabla f$) by multiply the learning rate $\alpha$  
	![[Pasted image 20240915141033.png]]
	$(x_1, y_1)$ equal to
	![[Pasted image 20240915144306.png]]

### Method 2: Gradient Descent 
+ ? Note: Gradicent Descent -> have to use partial Derivative for each Variable Ex: x, y, z, etc..
$(x_{0}, y_{0}) = (0.5, 0.6)$
![[Pasted image 20240915141116.png]]
Learing Rate = 0.05, So we keep substract the current position (x, y) by $$-0.05 \nabla f(0.5, 0.6)$$ until we reach the minimum point.
![[Pasted image 20240915141351.png]]

```ad-summary
**Gradient Descent**
Choose a starting point -> choose a direction to move -> choose a learning rate -> apply gradient descent fomula until reaching minimum point.
![[Pasted image 20240915141542.png]]
```

+ ! Disadvantage: have to **run many time in many direction to find the global minimum**.
![[Pasted image 20240915141742.png]]

## Gradient and Gradient Descent
![[Pasted image 20240915142340.png]]
> Find the optimal m so that distant between the line and every points is minimal. (smallest distant between all powerlines). The result calculated earlier was approx 4.167, now find m using gradient descent.
![[Pasted image 20240915142431.png]]

+ $ Goal: Minimize sum of squares cost
+ ? remember Delta mean Derivative 
1) Let get x and y function of $\nabla E(m, b)$ by calculating partial derivative of m and b. $\frac{\nabla f}{\nabla m}, \frac{\nabla f}{\nabla b}$ 
	
	![[Pasted image 20240915143356.png]]
2) Choose a "starting position" / "initial starting point" by replacing m and b (your choice)
	![[Pasted image 20240915143446.png]]
3) Start with $(m_0, b_0)$, Iterate until you find the minimum.
	![[Pasted image 20240915150031.png]]
	![[Pasted image 20240915150036.png]]
	(detail note for m1 and b1 after the first iteration)
	![[Pasted image 20240915150234.png]]


### Optimization using Gradient Descent - Least squares with multiple observations
>Plot the square area of each point reaching the line
>![[Pasted image 20240915220817.png]]
![[Pasted image 20240915220712.png]]
> **As you using gradient descent** you can **change m and b** so that the line will match with the **minimal distant from each points.** or to minimize the loss (value when subtracting real value with expected value)

From the idea above (minimal distant), we could combine Gradient Descent into Linear Regression problem to predict the closest value in the future: 
+ ? TV sales for example:
	![[Pasted image 20240915221111.png]]

![[Pasted image 20240915222243.png]]
> We got the line with x as x1 and y as mx1 + b. We then find the Loss by subtracting the current value (x1, mx1 + b) to the point we want to get to (x1, y1) which result in $(mx_1 + b - y_1)$ (x is eliminate obviously). For every other point, we do the same thing, and through each iteration we get a better line (y1, y2, y3, y4, etc..)


> note: $L(m, b)$ as the linear regression line.
+ ? when we take the derivative, 2 in the exponent cancels with this one. 
> To summarize, we calculate the average for all the loss of all the points. to get Linear Regression of all the points. Then apply Gradient Descent starting from $m_0, b_0$ To move the current line to the new position.  
![[Pasted image 20240915222604.png]]
  Repeat this process N time until reaching the minimum point.
![[Pasted image 20240915222635.png]]



