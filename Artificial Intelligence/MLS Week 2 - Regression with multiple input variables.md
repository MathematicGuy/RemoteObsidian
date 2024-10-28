# Multiple Linear Regression

![[Pasted image 20241014141110.png]]
+  arrow above parameter (e.g. x) notate that it a vector of number array. 
+ Each column represet a feature
+ Each row represent a example of its column. For example $x^{(1)} _{i}$ mean feature 1 (i.e. column 1) feature index at i (i.e. thứ i or i-th) 

Model:
![[Pasted image 20241014141317.png]]
Model with continuous features. 
![[Pasted image 20241014141311.png]]
Example for house price prediction base on features the house have, we can plot the function as (base price as the starting price):
![[Pasted image 20241014141415.png]]

#### Vectorization
> Achieve parallel mutiplication in matrix multiplication for efficiency (which processed using GPU)  

>`np.dot()`: help you to calc the sum of the product between 2 corresponding elements. 
![[Pasted image 20241014142644.png]]
+ ? If 2 matrix use np.dot() each value in matrix 1 row will multiply with each value in matrix 2 column.

> Vectorization allow parallel processing (i.e. the computer subtract/addition/divided/multiply at the same time)
![[Pasted image 20241014143438.png]]
>At first we have Gradient Descent repeat for every feature represent in $w_{j}$ ($j$ as feature indexes and if there're 3 features then repeat gradient descent for $w_{1}, w_{2}, w_{3}$ respectively) and $b$.  For simplicity, we shorten $w_{j}$ to $\vec{w}$. 
![[Pasted image 20241014143749.png]]

### Gradient Descent for multiple linear regression
>The same for cost function input array, we could shorten it to $\vec{w}$
![[Pasted image 20241014154254.png]]
>For Gradient Descent, since $x^{(i)} _{1}$ is the example number 1 for i features thus for multiple feature we $x_{1}$ convert to $x_{n}$
![[Pasted image 20241014155347.png]]

**An alternative to gradient descent**
![[Pasted image 20241014155831.png]]

**Notation**
![[Pasted image 20241014162327.png]]

# Feature Scaling 
> Allow Gradient Descent to converge faster
 
**Features and Parameters:** with **large value** model often choose **small parameters**, likewise for **small value** model often choose **large parameter** since it make the prediction **more reasonable.** 
![[Pasted image 20241014164249.png]]

For feature with large value, `size in feet`  for example (as $x_{2}$) and bedroom as $x_{1}$. A **little change in $x_{1}$ (say 200) can affect a large change in the cost function/prediction**, while a **large change in x1 (say 5) didn't make a little change at all.** To encounter this problem, we must **rescale/normalize both value into 1 value range.**  
![[Pasted image 20241014165034.png]] c
With Rescaling, the contour plot (parabol from top down view) now even and represent a circle. 
![[Pasted image 20241014164820.png]]

#### So how do you actually scale the vales? by dividing by it maximum value
![[Pasted image 20241014165801.png]]

#### other way is to use Mean Normalization
1) find the feature average (axis average value) 
2) substract the value with the Mean and dividing to it (max - min) 
![[Pasted image 20241014170400.png]]

#### Z-score Normalization
(understand standard deviation $\sigma$)
![[Pasted image 20241014170929.png]]

![[Pasted image 20241014171619.png]]
(Too small/Too Big -> recale to the average norm of all features)
### Checking gradient descent for convergence
 + ? **Converged** mean the algorithm has reached a point **where every update is very small** indicating that the **loss function has reached the optimal or nearly optimal value** and **further iteration would not significantly reduce loss.**  
 You can use $\epsilon$ (epsilon) for automatic convergence test:
 Let $\epsilon=10^{-3}$ then 
	 If $J(\vec{w}, b) \leq \epsilon$ in 1 iteration, declare convergence (i.e. found parameters $\vec{w}, b$ to get close to global minimum)  

#### Choosing the learning rate
![[Pasted image 20241015093817.png]]
+ ? **Learning rate too big the convergen become unstable**. What we want is a learning rate allowed big step but not too big at the start and take smaller and smaller step when the curvature is more flat (i.e. parabol curve become flatter at the center point). (This also indicate bugs might be in your code) 
+ ? Choosing a **too small learning rate lead the function unconvergerable.** Since each step become  smaller and smaller, it would take forever which is not optimal.
+ $ We want to choose **the right learning rate**. Let learn how to do that !!!
## Feature Engineering

Normal way to choose features
![[Pasted image 20241015221722.png]]

Create new features by using **intuition** to design **new features**, by transforming or combining original features.
![[Pasted image 20241015222100.png]]

#### Polynomial Regression (đa thức hồi quy)
> Fit curve, non-linear function into your data.
+ ? note: explain Polynomial and Regression later 
 
**Note:** Linear represent a straight line, if sth called linear, meaning it is **Proportionality:** If x increase then y increase $y=2x$. increase or decrease at a constant rate and **Additivity** like 1+1=2.


Example of Polynomial Regression with non-linear features: feature may be $x, x^{2}, x^{3}$. Since the feature value is exponential, feature scaling would be very important. Especially in Gradient Descent
![[Pasted image 20241016140747.png]]

**Choice of Features**
>So how can we chose the right type of features. Which to include or not include. In Course 2, you can learn it.
![[Pasted image 20241016140833.png]]

[[Feature Engineering and Polynomial Regression]]
[[Practice Lab Linear Regression - predict best aplace to open restaurant]]