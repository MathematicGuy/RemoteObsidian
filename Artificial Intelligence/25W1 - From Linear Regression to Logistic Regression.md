### Linear regression model 
![[Pasted image 20251105203646.png]]
Cost Function overview
![[Pasted image 20251105203803.png]]
$y^{(i)}$ - true target
$\hat{y}^{(i)} - y^{(i)}$ - subtract predict valuey hat to y. 

### Cost funciton Intuition (understanding the cost function)
If you set *w=1 & b=0*. And calculate the loss of $f_w(x)$ over all *predict datapoint (point map to the blue line*) and *grounth truth datapoint* (*RED*) we get a Loss Function Value of *0.58.*
![[Pasted image 20251105210015.png]]
Repeat this step for w=0&b=0 and we get Loss Func value of 2.3
![[Pasted image 20251105210238.png]]
**Repeat for this step for all other value** then we get this beautiful parralbol line. 
+ $ So when you trace what the Cost function $J$ by W for all x. The loss/cost function $J$ look like this. 
+ ? However, *how can we choose the correct value of $w$ that minimize $J$.*
![[Pasted image 20241014112735.png| 244]]
That also how you adjust the weight to minimize the loss function. 
![[Pasted image 20251105210646.png]]

### Visualize the cost function (How $f_{w,b}$ relate to the Cost function $J$ )
Like the previous example, for the given W and all input x, we can calculate the loss function value. In 3D, it the same, for the given $f_{w,b}$ you can see whether the loss value on the loss function graph is minimal (ie. at the center) or not.  
![[Pasted image 20251105220944.png]] 


### Feature Scaling 
+ @ Allow Gradient Descent to converge faster by rescale all features so they all take on a comparable range of values. (Đưa các features về cùng 1 khoảng giá trị 0 và )
 
**Features and Parameters:** with **large value** model often choose **small parameters**, likewise for **small value** model often choose **large parameter** since it make the prediction **more reasonable.** 
![[Pasted image 20241014164249.png]]

For feature with large value, `size in feet`  for example (as $x_{2}$) and bedroom as $x_{1}$. A **little change in $x_{1}$ (say 200) can affect a large change in the cost function/prediction**, while a **large change in x1 (say 5) didn't make a little change at all.** To encounter this problem, we must **rescale/normalize both value into 1 value range.**  
![[Pasted image 20241014165034.png]] 
With Rescaling, the contour plot (parabol from top down view) now even and represent a circle. 
![[Pasted image 20241014164820.png]]

So how do you actually scale the vales? by dividing by it maximum value
![[Pasted image 20241014165801.png | 344]]

![[Pasted image 20251105223957.png]]

#### other way is to use Mean Normalization
1) find the feature average (axis average value) 
2) substract the value with the Mean and dividing to it (max - min) 
![[Pasted image 20241014170400.png]]

#### Z-score Normalization
![[Pasted image 20251105224222.png]]

**When to Rescaling ?**
![[Pasted image 20241014171619.png# left | 433]]
+ $ Checking gradient descent for convergence
 + ? **Converged** mean the algorithm has reached a point **where every update is very small** indicating that the **loss function has reached the optimal or nearly optimal value** and **further iteration would not significantly reduce loss.**  
 You can use $\epsilon$ (epsilon) for automatic convergence test:
 Let $\epsilon=10^{-3}$ then 
	 If $J(\vec{w}, b) \leq \epsilon$ in 1 iteration, declare convergence ( i.e. parameters $\vec{w}, b$ to get close to global minimum )  

+ $ Choosing the learning rate
![[Pasted image 20241015093817.png]]
+ ? **Learning rate too big the convergen become unstable**. What we want is a **learning rate allowed big step but not too big at the start and take smaller and smaller step** when the curvature is more flat (i.e. parabol curve become flatter at the center point). (This also indicate bugs might be in your code) 
+ ! Choosing a **too small learning rate lead the function unconvergerable.** Since each step become  smaller and smaller, it would take forever which is not optimal.
+ ? so How to Choose the Right Learning Rate. 

### Feature Engineering
Normal way to choose features
![[Pasted image 20241015221722.png]]
**Feature Engineering:** create new features by using **intuition** to design **new features**, by transforming or combining original features.
![[Pasted image 20241015222100.png]]

### Polynomial Regression (đa thức hồi quy)
> Fit curve, non-linear function into your data.
+ 
**Note:** Linear represent a straight line, if sth called linear, meaning it is **Proportionality:** If x increase then y increase $y=2x$. increase or decrease at a constant rate and **Additivity** like 1+1=2.

Example of Polynomial Regression with non-linear features: feature may be $x, x^{2}, x^{3}$. Since the feature value is exponential, feature scaling would be very important. Especially in Gradient Descent
![[Pasted image 20241016140747.png]]

**Choice of Features**
>So how can we chose the right type of features. Which to include or not include. In Course 2, you can learn it.
![[Pasted image 20241016140833.png]]


### Regularization (From Polynomial to L1 and L2)
+ ? Polynomial Regression (đa thức hồi quy)
	+ **Polynomial:** đa thức nhiều biến x. Example: ax1 + bx2 + cx3 = y(x1, x2, x3) ![[Không có tiêu d_.jpg | 444 ]] 
*Simple Linear Equation:* $y = b_0 + b_1 x_1$
*Multiple Linear Equation:* $y = b_0 + b_1 x_1 + b_2 x_2 + \dots + b_n x_n$
*Polynomial Linear Regression:* $y = b_0 + b_1 x_1 + b_2 x_1^2 + \dots + b_n x_1^n$

**Note:** Linear represent a line, if sth called linear, it is a line. 
**Proportionality:** If x increase then y increase $y=2x$. increase or decrease at a constant rate and **Additivity** like 1+1=2.

Example of Polynomial Regression with non-linear features: feature may be $x, x^{2}, x^{3}$. Since the feature value is exponential, feature scaling would be very important. Especially in Gradient Descent
![[Pasted image 20241016140747.png]]
**Choice of Features**
>So how can we chose the right type of features. Which to include or not include. In Course 2, you can learn it.
![[Pasted image 20241016140833.png]]

### Logistic Growth Model and its relation to ln()
N - pop size
r - growth rate = (birth - death) / N -> return pos or neg pop's rate of growth.
  
 