> Newton's Method is used to find the 0 of a function.

Let's take the tangent at this point X0, so let's take the derivative and draw the tangent and see where it hits the horizontal X axis. And at this point we're going to call it X1, notice that X1 is much closer to zero than X0. We draw more time for X2, its very close to 0, do this one more time X3 pretty much found it (very close)
![[Pasted image 20241001101700.png]]

The Slope is f(X0), it base is X0 - X1. The slope is calc by Rise over Run. So $$f'(x_{0}) = \frac{f(x_{0})}{x_{0} - x_{1}}$$ Simplified it we get $x_{1}$
![[Pasted image 20241001102053.png]]
$$x_{k+1} = x_{k} - \frac{f(x_{0})}{f'(x_{0})}$$
and got $x_{k}, x_{k-1}$ as the first 2 points created the slope. Iterate on the step we get Newton's method.    
![[Pasted image 20241001102742.png]]

So how Newton's Method can be use for optimization. 
+ ? Gradient Decent found the minimum of a function, Newton's method only find the 0 of the function not the minimum. Well, to minimize g(x) we have to find zeros of $g'(x)$ so we just need to chose which zeros is the minimum. (cho ptr bằng 0 và chọn nghiệm bé nhất) 
+ $ In other word, if I let F of X be the derivative of G of X, then by finding the zeros of F of X, I am minimizing G prime of X. And the derivative of F prime of X, is simply the derivative of G of X and the derivative of that.

In NM, we first initiate $x_0$ as the starting point and update it. For Optimization, because by finding the derivative of $f(x_{k})$ also minimizing $g(x)'$. We replace F of X with G prime of X.
	![[Pasted image 20241001103540.png]]![[Pasted image 20241001103933.png]]


## Newton's Method Example
Back to e hat x minus log of x example. g'(x) =0.5671 (given answer)
Let see if Newton's Method work. we have G prime of x therefor ours function for f prime becomed $(g'(x))'$ since f(x) is depend on g(x). Starting at $x_{0}=0.05$ we iterate until reached the minimum: 0.5671.  
![[Pasted image 20241001104348.png]]
After 5 iterations we found it. Quite like gradient descent right.
![[Pasted image 20241001105555.png]]

### Second Derivative
> Rate of change of "the rate of change"

note:
+ derivative of a func is a constance mean that func is a line.
+ curvature: độ cong
+ convex: lồi

**Notation**
![[Pasted image 20241001112719.png]]

Understanding Second Derivative with Real Life example
![[Pasted image 20241001112943.png]]
The map show the change in distance x through time t.  
+ ? For each point of time we map the line function. And calculate the derivative with respect of t. 
+ ? Lines in the 1st, 2nd Derivative because all functions result are constants. 

>The first derivitive show the car's Speed
![[Pasted image 20241001114056.png]]

>  The second derivative show the car's Acceleration
![[Pasted image 20241001113239.png]]
```ad-summary
The 2nd Derivative result positive when the car accelerating and result negative when the car deaccelerating. When the car speed is constant (speed unchanged) 2nd Derivative result in 0.
```


**Curvature**
note: 2D mean 2nd Derivative
![[Pasted image 20241001114951.png]]
(hướng lên khi 2D > 0. hướng xuống khi 2D < 0, cần thêm thông tin khi 2D = 0)

![[Pasted image 20241001115148.png]]
+ ? As the image showed, local min when 2D>0 and local max when 2D<0.
Note: Inconclusive mean we don't know it maximum or minimum.

[[1st Derivative vs 2nd Derivative]]
![[Pasted image 20241001115337.png]]
> The 2nd Derivative tell at how the "rate of change" (1st Derivative) is changing.

```ad-summary
- The **first derivative** gives the **rate of change** or **slope** of the function.
- The **second derivative** gives information about the **concavity** or **curvature**.
- For a **quadratic function**, the **second derivative is constant**, which gives rise to a **parabolic shape**.
- Higher-order functions have **changing second derivatives**, resulting in more complex and varied curves, not just parabolas.
```


## The Hessian
+ $ Example above was just 1 variable, for multiple variables, the **second derivative is a Matrix full of second derivatives called the Hessian**.

![[Pasted image 20241001142935.png]]

Explain from the top down, we got the rate of change of $f_{x x}$ (this is just $f'(f'(x))$ 
	the same for the rest, $f_{xy}$, $f_{yy}$, $f_{yx}$  (i.e. rate of change of the derivative in respect of ...)
	![[Pasted image 20241001143458.png]]
	
	![[Pasted image 20241001143445.png]]
+ orthogonal: trực giao. 
	![[Pasted image 20241001143512.png]]
+ change in the change: derivative of the derivative i.e. rate of change of "the rate of change".

note: $f_{x x}$ just mean derivative 2 times. 
![[Pasted image 20241001143534.png]]

took the derivative in respect of x and y.
![[Pasted image 20241001143630.png]]
another example:
![[Pasted image 20241001143745.png]]
**Notation**
> **Hessian matrix is a matrix that keep track of all the 2nd Derivatives of a function.**
> -> This helps us optimize functions with multiple variables. This also called multivariable Newton's method.
![[Pasted image 20241001144237.png]]
+ ? Bonus Fact: **By analyzing the Hessian matrix**, we **can determine whether a point is a minimum, maximum, or a saddle point**
![[Pasted image 20241001144722.png]]

### Hessians and concavity
Example:
+ At (0, 0) both eigenvalue are positive: the function is concave up and the 0.0 is minimum.
	![[Pasted image 20241001144955.png]]
	
+ Concabe Down maximum at (0,0) because eigen value is < 0.
	![[Pasted image 20241001145156.png]]
	
+ Saddle Point (look like a saddle, **a place between maximum and minimum as you can see**): Situation when both eigenvalue is < 0 and > 0. This cannot be determinant, we call it saddle point.
	![[Pasted image 20241001145326.png]]

**In Summary:**
+ If all variable are < 0: the function is concave down and maximum at point (x, y)
+ If all variable are  > 0: the function is concave up and minimum at point (x, y)
+ If any variable = 0 or < 0 and > 0 at the same time -> saddle point thus cannot be determinant.
	![[Pasted image 20241001145524.png]]

### Newton's Method for 2 variables.
> Learn how to apply Newton's method to optimize functions of many variables. And as you guessed it, the Hessian appears here.

+ 1 var: the func and it re-write version.
+ 2 vars or n vars: hessian matrix version (newton's method in matrix version)
![[Pasted image 20241001145924.png]]
+ ? **Notation:** 
	+ $\nabla f$: the gradient (as the 1st derivative with respect of x and y)
	+ $H^{-1}$:  The hassien matrix (as the 2nd derivative with respect of x and y)
+ ! remember, you cannot multiply 2 by 1 vector to the left of the matrix. (i.e. Multiply $\nabla f$ with $H^{-1}$). The oder is crucial !!!
	![[Pasted image 20241001150146.png]]
+ the 2 vars fomula is quite comflex so now we not prove it yet. Accept it as it is for now.

Example:
![[Pasted image 20241001150400.png]]

![[Pasted image 20241001150513.png]]
![[Pasted image 20241001150540.png]]
now let Iterate again, and repeat it until we reach the minimum point (very close to the actual 0).
![[Pasted image 20241001150558.png]]
![[Pasted image 20241001150646.png]]
> This is incredibly fast for finding the minimum point of higher dimension function.


### Gradient Descent vs Newton's Method in calc Multiple Variables

**Gradient Descent:** have learning rate as an extra parameter and converge slower than Newton's Method.  (derivative 1 time at a row). Might not even converge it the dimension is too large.

**Newton's Method:** Converge fast but each variable need dervative 3 times made it computationally expensive that is $n + 2n$ (i.e. 3 variables need derivative 9 times: it self (3 times), its derivative derivative with respect of x and y (each derivative derivate 2 times: 3.2=6 times total))
	![[Pasted image 20241001162406.png]]
+ $ This is the reality of numerical optimization - convergency and actual result depend on the initial parameters. Also, there is no "perfect" algorithm - every method will have advantages and disadvantages.
	
+ reciprocal: nghịch đảo
	**The reciprocal of a non-zero real number** $a$ **is** $\frac{1}{a}$

![[Pasted image 20241001170233.png]]

![[Pasted image 20241001170219.png]]

