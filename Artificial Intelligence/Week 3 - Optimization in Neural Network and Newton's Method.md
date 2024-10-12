## Lesson 1 - Optimization in Neural Network
### Regression with a Perceptron
alternate to gradiend descent called Newton's method (very fast and useful)

![[Pasted image 20240926150726.png]]
>**Main Goal:** Find weights and bias that will optimise the predictions -> optimal values for w1, w2 and b such that we minimize the error. 
>i.e. Reduce the error in the predictions (using The Loss Function) 

### Loss Function
>Find Loss by subtract the real value to the predicted value. Since this will cause the Loss both positvie and negative, we square Loss function and divided it by 2. (divide by 2 help cancel out the 2 when Loss function Derivative) 
![[Pasted image 20240926151419.png]]
![[Pasted image 20240926152102.png]]


Using Gradient Descent to find Loss Function, we first need to find the Partial Derivative of $\hat{y}$. Apply the chain rule, there are 3 partial derivative for each constant:
![[Pasted image 20240926152432.png]]
Let simplied this for what need to be calculated:
![[Pasted image 20240926153352.png]]
![[Pasted image 20240926153335.png]]
Let update these Partial Derivative to find w1, w2 and b
![[Pasted image 20240926153510.png]] 

### Classification with Perceptron
#### Motivation: classified output base on input features
![[Pasted image 20240927085659.png]]

We have a word table contain 2 unique word with their repeated time. Since our models take numerical input, we can plot  the point on 2 features axis: Aack and Beep, their repeated times as value.
>Now we need a function represent the line which divide the plot if emotion are happy or sad (0 & 1)
![[Pasted image 20240927090004.png]]

>Our perceptron will have 2 nodes: W_1 and W_2 determine how important any other features are, say the word `aack` is really **correlated with happiness** then **W_1 going to be a larger number**, if `beep` is really **irrelevant (ko liên quan)** then **W2 is going to be a small number**.
+ ? **How can we turn entire number line 0 and 1**, we're going to use what's called the activation function, denoted by the letter **Sigmoid of z**
![[Pasted image 20240927085639.png]]


#### Classification with Perceptron - Sigmoid Function
input - x
output - y
![[Pasted image 20240927092127.png]]

Sigmoid function crunches the entire number line into the interval (0, 1) and is that its derivative is really nice.
+ ? Fomula use in the derivative below is: $e^u$, the chain rule, basic derivatives 
 ![[Pasted image 20240927092320.png]]
 ![[Pasted image 20240927092450.png]]
 ![[Pasted image 20240927092622.png]]


#### Classification with Perceptron - Gradient Descent
in normal regression problem we use least square error to calc the Loss. For **Classification problem**, the **best function is the Log Loss**. 
![[Pasted image 20240927100240.png]]
$L(y, \hat{y})$ 
	![[Pasted image 20240927101436.png]]
+ Larger if $\hat{y}$ is close to 1, Smaller if $\hat{y}$ is close to 0.
+ Larger number if $y$ and $\hat{y}$ is far from each other, and small if $y$ and $\hat{y}$ are close to each other. 

Like before, we find w1, w2 and b such that $\hat{y}$ give the least errors using Gradient Descent. To achieve that, we first find Derivative of the Loss function in respect of $w1,\space w2,\space b$. Then start with initial value: w1, w2, b to activate Gradient Descent. Finally put (w1, w2 and b) or $\hat{y}$ back the Loss Function to verify.     
![[Pasted image 20240927101754.png]]
> Because $\hat{y}$ function is inside $L(\hat{y}, y)$ function, we use the Chain Rule to seperate each derivate for simplification and tackle each of them 1 by 1. 
	![[Pasted image 20240927112155.png]]
	![[Pasted image 20240927112132.png]]
	For $\hat{y}$, we already have the derivative of $\sigma$ calculated as $\sigma' = \sigma(z).(1 - \sigma(z))$, using the chain rule we have: $\sigma'.(w_{1}x_{1} + w_{2}x_{2} + b)$ with respect of w1, w2 and b.
	![[Pasted image 20240927113039.png]]
	Put each derivative back, we have most of the denominator and end up with this very simplified partial derivative in respect of w1, w2, and b 
	![[Pasted image 20240927113434.png]]
	![[Pasted image 20240927113542.png]]
>Let put these back to ours Gradient Descent function:
>![[Pasted image 20240927113657.png]]

### Classification Problem Motivation
+ ? **Neural Network**: bunch of perceptron stacked in layers.
+ ? **How to train theses neural networks?** just using gradient descent like before. Except now we have many derivatives.  

Let build a neural network to classify emotion.
![[Pasted image 20240930161130.png]]

**2,2,1 Neural network**   
![[Pasted image 20240930161010.png]]
+ ? Each node have the previous layer weight and bias. (both hidden and output) and let not forget the Log Loss function we calc. 
![[Pasted image 20240930162839.png]]

+ $ **Goals:** Adjust each of the weights and biases to reduce the loss function.
+ ? How do these biases affect the loss? with partial derivative. In other words, this partial derivative tell us exactly what direction to move each one of the weights and biases in order to reduce the log loss function. ![[Pasted image 20240930163826.png]]

Like before, we going to use the chain rule so let look at the derivative of each weight as bias first:
![[Pasted image 20240930163948.png]]

So there a lot of variables in between L and W11. And we're going to keep track all of them by a humongous chain rule. The reason is because the loss function $L(y, \hat{y})$  depend on $\hat{y}$ so we need $\frac{\Delta L}{\Delta\hat{y}}$, and $\hat{y}$ depend on $z$ so we need $\frac{\Delta \hat{y}}{\Delta z}$ and $a$ depend on $z$ so we have $\frac{\Delta z}{\Delta a_{1}}$ and z1 is depend on a1 so we have $\frac{\Delta a_{1}}{\Delta z_{1}}$ and w11 is depend on z1 so we have $\frac{\Delta z_{1}}{\Delta w_{11}}$. This NN is the combination of all these derivative.
![[Pasted image 20240930164241.png]]

Calculating all the derivative have the $\frac{\Delta L}{\Delta\hat{y}}$ Log Loss function of this 2,2,1 Neural Network as below:
![[Pasted image 20240930165805.png]]
Replace Loss function to the Gradient Descent
$$w_{11} \to w_{11} - \alpha.(-x_{1}.w_{1}.a_{1}.(1-a_{1})(y-\hat{y}))$$

+ ? The Chain Rule Process repeat for every weights and biases. i.e. $w_{11}, w_{12}, b, etc..$ (yes, even the bias)
	![[Pasted image 20240930170521.png]]
	![[Pasted image 20240930170540.png]]

**Summary**: If you do these updates for a learning rate $\alpha$, you get better weights and biases. (That is for the first layer) 
![[Pasted image 20240930170622.png]]

**Second Layer**
![[Pasted image 20240930171055.png]]

**w1, w2 and b**
![[Pasted image 20240930171122.png]]
![[Pasted image 20240930171129.png]]

### Gradient Descent and Backpropagation
> Backward Derivative (use Chain Rule)

Node notation (ký hiệu) in each layer.  
![[Pasted image 20241001095227.png]]

Eveything can be calculated using these weights (notate in green). In Backpropagation we calc all the derivative in backward.
	![[Pasted image 20241001095645.png]]
Let Begin with $\frac{\Delta L}{\Delta w^{[3]}}$
	![[Pasted image 20241001095808.png]]

+ ? The derivative at the bottom right is already calculated so remember to store them for reused.
![[Pasted image 20241001100311.png]]
+ ? For the last one, we just have to calc the node itself, bc its previous node are already calcualated (in bottom right)
![[Pasted image 20241001100411.png]]


## Lesson 2: Newton's method
> Newton's Method is used to find the 0 of a function.

Let's take the tangent at this point X0, so let's take the derivative and draw the tangent and see where it hits the horizontal X axis. And at this point we're going to call it X1, notice that X1 is much closer to zero than X0. We draw more time for X2, its very close to 0, do this one more time X3 pretty much found it (very close)
![[Pasted image 20241001101700.png]]

The Slope is f(X0), it base is X0 - X1. The slope is calc by Rise over Run. So $$f'(x_{0}) = \frac{f(x_{0})}{x_{0} - x_{1}}$$ Simplified it we get $x_{1}$
![[Pasted image 20241001102053.png]]
$$x_{k+1} = x_{k} - \frac{f(x_{0})}{f'(x_{0})}$$
and got $x_{k}, x_{k-1}$ as the first 2 points created the slope. Iterate on the step we get Newton's method.    
![[Pasted image 20241001102742.png]]

So how Newton's Method can be use for optimization. 
+ ? Gradient Decent found the minimum of a function, Newton's method only find the 0 of the function not the minimum (e.g. f(x) = 0). Well, to minimize g(x) we have to find zeros of $g'(x)$ so we just need to chose which zeros is the minimum. (cho ptr bằng 0 và chọn nghiệm bé nhất) 
+ $ In other word, if I let F of X be the derivative of G of X, then by finding the zeros of F of X, I am minimizing G prime of X. And the derivative of F prime of X, is simply the derivative of G of X and the derivative of that.

In NM, we first initiate $x_0$ as the starting point and update it. For Optimization, because by finding the derivative of $f(x_{k})$ also minimizing $g(x)'$. We replace F of X with G prime of X.
	![[Pasted image 20241001103540.png]]![[Pasted image 20241001103933.png]]


## Newton's Method Example
Back to e hat x minus log of x example. g'(x) =0.5671 (given answer)
Let see if Newton's Method work. we have G prime of x therefor ours function for f prime becomed $(g'(x))'$ since f(x) is depend on g(x). Starting at $x_{0}=0.05$ we iterate until reached the minimum: 0.5671.  
![[Pasted image 20241001104348.png]]
After 5 iterations we found it. Quite like Gradient Descent right:
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
Note: Inconclusive (ko có kết luận) mean we don't know it maximum or minimum.

[[1st Derivative vs 2nd Derivative]]
![[Pasted image 20241001115337.png]]
> The 2nd Derivative tell at how the "rate of change" (1st Derivative) is changing.

```ad-summary
- The **first derivative** gives the **rate of change** or **slope** of the function.
- The **second derivative** gives information about the **concavity** or **curvature**.
- For a **quadratic function**, the **second derivative is constant**, which gives rise to a **parabolic shape**.
- Higher-order functions have **changing second derivatives**, resulting in more complex and varied curves, not just parabolas.
```


## The Hessian (Matrix)
+ $ Example above was just 1 variable, for multiple variables, the **second derivative is a Matrix full of second derivatives called the Hessian**.

![[Pasted image 20241001142935.png]]

Explain from the top down, we got the rate of change of $f_{x x}$ (this is just $f'(f'(x))$ 
	the same for the rest, $f_{xy}$, $f_{yy}$, $f_{yx}$  (i.e. rate of change of the derivative in respect of ...)
+ ? **w.r.t** mean with respect to 
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

![[Pasted image 20241001170233.png]]![[Pasted image 20241001170219.png]]

## Optimization in Neural Network and Newton's Method 
## 1 - Classification Problem
![[Pasted image 20241002153710.png]]
+ ? Each layer distinguish by the integer called superscript (i.e. number above) in the square brackets $^{[1]}$ denotes the layer number. 
+ ? nx as the number of input for input layer, nh as the number of nodes in hidden layer, ny as the number of nodes in output layer. 

Simplified the first 2 parameters:
The training examples $x^{(i)}=\begin{bmatrix}x_1^{(i)} \\ x_2^{(i)}\end{bmatrix}$ from the input layer of size $n_x = 2$ are first fed into the hidden layer of size $n_h = 2$ along with b (i.e. scaler):
![[Pasted image 20241002154045.png]]
rewritten in matrix form.
+ ? z hat 1 i represent each vector in layer 1. 
+ ? W hat 1 represent the weight of each node in layer 1. W hat 1 1 mean weights from layer 1 node 1 which contain: $w_{1,1}$ and $w_{2,1}$ the same for w hat 1 2. 
+ ? b hat 1 mean b in the 1st layer, b hat 1 1 mean b of the first node and b hat 1 2 mean b of the 2nd node (both in the 1st layer)

+ $ These **expressions for one training example** $x^{(i)}$ can be rewritten in a matrix form :
$$z^{[1](i)} = W^{[1]} x^{(i)} + b^{[1]},\tag{2}$$
![[Pasted image 20241002153757.png]]


We use sigmoid as ours activation function $\sigma\left(x\right) = \frac{1}{1 + e^{-x}}$: Rewritten in matrix form we get: 
$$a^{[1](i)} = \sigma\left(z^{[1](i)}\right) = 
\begin{bmatrix}\sigma\left(z_1^{[1](i)}\right) \\ \sigma\left(z_2^{[1](i)}\right)\end{bmatrix}.\tag{3}$$
Then the hidden layer output gets fed into the output layer of size $n_y = 1$. This was covered in the previous lab, the only difference are: $a^{[1](i)}$ is taken instead of $x^{(i)}$ (i.e. x from input layer) and layer notation $^{[2]}$ appears to identify all parameters and outputs:
$$z^{[2](i)} = w_1^{[2]} a_1^{[1](i)} + w_2^{[2]} a_2^{[1](i)} + b^{[2]}= W^{[2]} a^{[1](i)} + b^{[2]},\tag{4}$$
rewrite all the expression, group them for convenience.
![[Pasted image 20241002162221.png]]
Finally, the predictions for some example $x^{(i)}$ (i.e. input $x^{(i)}$) can be made taking the output $a^{[2](i)}$ and calculating $\hat{y}$ as: $\hat{y} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5, \\ 0 & \mbox{otherwise }. \end{cases}$


### 2.2 - Neural Network Model with Two Layers for Multiple Training examples
+ $ **Goals:** perform training of the model, find such set of parameters $𝑊^{[1]}$, $𝑏^{[1]}$ (i.e. layer 1), $𝑊^{[2]}$, $𝑏^{[2]}$ (i.e. layer 2), that will minimize the cost function.
+ ? **True Label:** Correct output $y^{(i)}$ of the function. (either 0 and 1)
+ ? **Test Label:**  Label use to test and compare with true label.
+ note: $\hat{y}$ now replace as $a^{[2](i)}$
	Like in the previous example of a single perceptron neural network, the cost function can be written as:
$$\mathcal{L}\left(W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\right) = \frac{1}{m}\sum_{i=1}^{m} L\left(W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\right)$$$$=  \frac{1}{m}\sum_{i=1}^{m}  \large\left(\small - y^{(i)}\log\left(a^{[2](i)}\right) - (1-y^{(i)})\log\left(1- a^{[2](i)}\right)  \large  \right), \small\tag{8}$$where $y^{(i)} \in \{0,1\}$ are the original labels and $a^{[2](i)}$ are the continuous output values of the forward propagation step (elements of array $A^{[2]}$).
+ $ **Loss Function Purpose**: Measures the discrepency (khác biệt, tương phản) between predicted probability and the true label. 

To minimize loss we updating the parameters using gradient descent:
$$\begin{align}
W^{[1]} &= W^{[1]} - \alpha \frac{\partial \mathcal{L} }{ \partial W^{[1]} },\\
b^{[1]} &= b^{[1]} - \alpha \frac{\partial \mathcal{L} }{ \partial b^{[1]} },\\
W^{[2]} &= W^{[2]} - \alpha \frac{\partial \mathcal{L} }{ \partial W^{[2]} },\\
b^{[2]} &= b^{[2]} - \alpha \frac{\partial \mathcal{L} }{ \partial b^{[2]} },\\
\tag{9}
\end{align}
$$where $\alpha$ is the learning rate.

To perform training of the model you need to calculate now $\frac{\partial \mathcal{L} }{ \partial W^{[1]}}$, $\frac{\partial \mathcal{L} }{ \partial b^{[1]}}$, $\frac{\partial \mathcal{L} }{ \partial W^{[2]}}$, $\frac{\partial \mathcal{L} }{ \partial b^{[2]}}$ (i.e. Derivative of Weight and bias from 1st and 2nd layer annotation in $^{[1], \space [2]}$)  

Let's start from the end of the neural network. You can rewrite here the corresponding expressions for $\frac{\partial \mathcal{L} }{ \partial W }$ and $\frac{\partial \mathcal{L} }{ \partial b }$ from the single perceptron neural network:
$$\begin{align}
\frac{\partial \mathcal{L} }{ \partial W } &= 
\frac{1}{m}\left(A-Y\right)X^T,\\
\frac{\partial \mathcal{L} }{ \partial b } &= 
\frac{1}{m}\left(A-Y\right)\mathbf{1},\\
\end{align}$$
where $\mathbf{1}$ is just a ($m \times 1$) vector of ones. Your one perceptron is in the second layer now, so $W$ will be exchanged with $W^{[2]}$, $b$ with $b^{[2]}$, $A$ with $A^{[2]}$, $X$ with $A^{[1]}$:
$$\begin{align}
\frac{\partial \mathcal{L} }{ \partial W^{[2]} } &= 
\frac{1}{m}\left(A^{[2]}-Y\right)\left(A^{[1]}\right)^T,\\
\frac{\partial \mathcal{L} }{ \partial b^{[2]} } &= 
\frac{1}{m}\left(A^{[2]}-Y\right)\mathbf{1}.\\
\tag{10}
\end{align}$$

Let's now find $$\frac{\partial \mathcal{L} }{ \partial W^{[1]}} = 
\begin{bmatrix}
\frac{\partial \mathcal{L} }{ \partial w_{1,1}^{[1]}} & \frac{\partial \mathcal{L} }{ \partial w_{2,1}^{[1]}} \\
\frac{\partial \mathcal{L} }{ \partial w_{1,2}^{[1]}} & \frac{\partial \mathcal{L} }{ \partial w_{2,2}^{[1]}} \end{bmatrix}$$It was shown in the videos that $$\frac{\partial \mathcal{L} }{ \partial w_{1,1}^{[1]}}=\frac{1}{m}\sum_{i=1}^{m} \left( 
\left(a^{[2](i)} - y^{(i)}\right) 
w_1^{[2]} 
\left(a_1^{[1](i)}\left(1-a_1^{[1](i)}\right)\right)
x_1^{(i)}\right)\tag{11}$$
If you do this accurately for each of the elements $\frac{\partial \mathcal{L} }{ \partial W^{[1]}}$, you will get the following matrix:

$$\frac{\partial \mathcal{L} }{ \partial W^{[1]}} = \begin{bmatrix}
\frac{\partial \mathcal{L} }{ \partial w_{1,1}^{[1]}} & \frac{\partial \mathcal{L} }{ \partial w_{2,1}^{[1]}} \\
\frac{\partial \mathcal{L} }{ \partial w_{1,2}^{[1]}} & \frac{\partial \mathcal{L} }{ \partial w_{2,2}^{[1]}} \end{bmatrix}$$
$$= \frac{1}{m}\begin{bmatrix}
\sum_{i=1}^{m} \left( \left(a^{[2](i)} - y^{(i)}\right) w_1^{[2]} \left(a_1^{[1](i)}\left(1-a_1^{[1](i)}\right)\right)
x_1^{(i)}\right) & 
\sum_{i=1}^{m} \left( \left(a^{[2](i)} - y^{(i)}\right) w_1^{[2]} \left(a_1^{[1](i)}\left(1-a_1^{[1](i)}\right)\right)
x_2^{(i)}\right)  \\
\sum_{i=1}^{m} \left( \left(a^{[2](i)} - y^{(i)}\right) w_2^{[2]} \left(a_2^{[1](i)}\left(1-a_2^{[1](i)}\right)\right)
x_1^{(i)}\right) & 
\sum_{i=1}^{m} \left( \left(a^{[2](i)} - y^{(i)}\right) w_2^{[2]} \left(a_2^{[1](i)}\left(1-a_2^{[1](i)}\right)\right)
x_2^{(i)}\right)\end{bmatrix}\tag{12}$$
+ $  We called this the Loss Function of each parameters (i.e. weight ans biases). Basically, normally what we do is calculate the loss of a weight and biases of each node by the derivative of it and $\mathcal{L}$ using the chain rule: $\frac{\partial\mathcal{L}}{\partial W_{11}}$. This does just that but in a greater scale which calc the weight and bias of 2 input with 2 nodes (in hidden layer). 
	reference:![[Pasted image 20241003101310.png]]


note: understand how they compress chain rule into a loss function
```python
np.log([1, np.e, np.e**2, 0])
```

```python
def layer_sizes(X, Y):
    """
    Arguments:
    X -- input dataset of shape (input size, number of examples)
    Y -- labels of shape (output size, number of examples)
    
    Returns:
    n_x -- the size of the input layer
    n_h -- the size of the hidden layer
    n_y -- the size of the output layer
    """


def initialize_parameters(n_x, n_h, n_y):
    """
    Argument:
    n_x -- size of the input layer
    n_h -- size of the hidden layer
    n_y -- size of the output layer
    
    Returns:
    params -- python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """


def forward_propagation(X, parameters):
    """
    Argument:
    X -- input data of size (n_x, m)
    parameters -- python dictionary containing your parameters (output of initialization function)
    
    Returns:
    A2 -- the sigmoid output of the second activation
    cache -- python dictionary containing Z1, A1, Z2, A2 
    (that simplifies the calculations in the back propagation step)
    """


def compute_cost(A2, Y):
    """
    Computes the cost function as a log loss
    
    Arguments:
    A2 -- The output of the neural network of shape (1, number of examples)
    Y -- "true" labels vector of shape (1, number of examples)
    
    Returns:
    cost -- log loss
    
    """


def backward_propagation(parameters, cache, X, Y):
    """
    Implements the backward propagation, calculating gradients
    
    Arguments:
    parameters -- python dictionary containing our parameters 
    cache -- python dictionary containing Z1, A1, Z2, A2
    X -- input data of shape (n_x, number of examples)
    Y -- "true" labels vector of shape (n_y, number of examples)
    
    Returns:
    grads -- python dictionary containing gradients with respect to different parameters
    """


def update_parameters(parameters, grads, learning_rate=1.2):
    """
    Updates parameters using the gradient descent update rule
    
    Arguments:
    parameters -- python dictionary containing parameters 
    grads -- python dictionary containing gradients
    learning_rate -- learning rate for gradient descent
    
    Returns:
    parameters -- python dictionary containing updated parameters 
    """


```

---
### Mạng neuro 2 lớp cho đầu vào 1 giá trị (vd: $x_{1}=2, x_{2}=3$)
![[Pasted image 20241011103012.png]]
có ![[Pasted image 20241011103505.png]] ($x^{i}$ là vector chứa các giá trị đầu vào) là lớp đầu vào có kích thước ![[Pasted image 20241011103639.png]] được đẩy vào lớp ẩn kích thước ![[Pasted image 20241011103631.png]]
. Chúng đc đẩy vào lớp Perceptron $z_{1}$ với ![[Pasted image 20241011103813.png]] và $z_{2}$![[Pasted image 20241011103854.png]]. ký hiệu số với ngoặc vuông trên các ký hiệu đại diện cho số lớp hiện tại (vd: 1 nghĩa là lớp 1)
Nhân các tham số với nhau và cộng thên bias ta có:p 
![[Pasted image 20241011104023.png]]
với
![[Pasted image 20241011104045.png]]
z là tham số đầu vào có kích thước $n_{h} *1$ của hàm kích hoạt a
W là ma trận của weight còn b là vector của bias.

Tiếp theo, hàm kích hoạt trong lớp ẩn của tham số $a$  cần được áp dụng cho mọi phần tử vector z.
![[Pasted image 20241011104724.png]]
Hàm kích hoạt sigmoid: $\sigma\left(x\right) = \frac{1}{1 + e^{-x}}$. có đạo hàm là $\frac{d\sigma}{dx} = \sigma\left(x\right)\left(1-\sigma\left(x\right)\right)$. Vì Hàm kích hoạt nhận vector z làm tham số nên a biểu diễn dưới dạng:
![[Pasted image 20241011104411.png]]

Rồi đầu ra của lớp ẩn được đưa vào "lớp đầu ra" có kích thước $n_{y}=1$.    
![[Pasted image 20241011104709.png]]
Do z nhận 2 tham số $w_{1}, w_{2}$ nên ta có phương trình của $z_{2}$ là:
![[Pasted image 20241011105020.png]]
note: W lớn tượng trưng cho mọi w của lớp ẩn, và a tượng trưng cho mọi a của lớp ẩn.
+ Sau khi đi qua hàm sigmoid, z trở thanh vector vô hướng (1x1). Vậy là z và b đều là vecter vô hướng (1x1) khi truyền tới lớp đầu ra.
+ Chỉ còn W đại diện cho tham số $w1, w2$ được biểu diễn dưới dạng vector:
![[Pasted image 20241011105456.png]]

Sau khi tính z, hàm sigmoid được sử dụng cho lớp ẩn và truyền tới hàm Loss.
![[Pasted image 20241011105553.png]]

Các công thức của mạng neuron phía trên có thể viết lại ngắn gọn như sau:
$$
\begin{align}
z^{[1](i)} &= W^{[1]} x^{(i)} + b^{[1]},\\
a^{[1](i)} &= \sigma\left(z^{[1](i)}\right),\\
z^{[2](i)} &= W^{[2]} a^{[1](i)} + b^{[2]},\\
a^{[2](i)} &= \sigma\left(z^{[2](i)}\right).\\
\tag{6} \\
\end{align}
$$
với $i$ đại diện cho các biến đầu vào (thứ tự của các biến đầu vào). vd: $z^{[1](i)}$ nghĩa là mọi z lớp 1.

sau đó  $x^{(i)}$ có thể được tạo ra bằng cách lấy đầu ra $a^{[2](i)}$ và tính $\hat{y}$ như sau: $\hat{y} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5, \\ 0 & \mbox{otherwise }. \end{cases}$.


## Mạng Neuron 2 Lớp cho đầu vào nhiều giá trị (vd: $x_{1}=[1,2,3]$) 
![[Pasted image 20241011103012.png]]
note: Đầu vào là x, x được truyền vào lớp ẩn để tính z, z truyền tới hàm kích hoạt để tính a. Và output ra a tới lớp tiếp theo. (Lớp Ẩn: Đầu vào x, Đầu ra a) ([[What is X]])

Gọi số lần huấn luyện là m (để biểu diễn phương trình tốt hơn), m có thể được sắp xếp trong ma trận X có kích thước (2 × m) (gồm m cột) (Vì 2 biến X được huấn luyện m lần).
+ ? vd X khi số đầu vào $n_{x}=3$ có $m=4$. Khi đó mỗi biến là 1 biểu diễn vector $x_{ij}$ có $i$ là thứ tự của vector, và $j$ là thứ tự các giá trị của vector $i$.  
	![[Pasted image 20241011112646.png]]

Với ma trận X, ta đơn giản thay X lớn cho x nhỏ. Thể hiện rằng X là 1 ma trận chứa nhiều vector $x_{i}$
![[Pasted image 20241011110846.png]]

Để đánh giá mạng neuron mình khai báo hàm Log Loss (cho bài toán phân loại)
![[Pasted image 20241011121201.png]]
> "Vì hàm mất mát $\mathcal{L}$ phụ thuộc vào $\hat{y}$ (kết quả dự đoán), mà $\hat{y}$ được tính thông qua các trọng số và độ lệch (i.e. $W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}$) của mô hình, nên hàm Log Loss thực chất phụ thuộc vào các tham số ở lớp đầu vào và lớp ẩn."
>.
>"Để đánh giá mất mát của mô hình trên toàn bộ tập dữ liệu $X$, ta tính tổng giá trị mất mát cho mỗi ví dụ (i.e. vector của X) và sau đó lấy trung bình bằng cách chia cho $m$ (tổng số ví dụ). Điều này giúp đánh giá tổng quát hơn về hiệu năng của mô hình".
>note: 
![[Pasted image 20241011103325.png]]
>trong đó $y^{(i)}$ là giá trị thực (true value/original label) và $a^{[2](i)}$ là giá trị đầu ra của bước forward propagation (các phần tử của $A^{[2]}$).

Để tối giảm mất mát, mình dùng gradient descent để cập nhật các tham số w, b của các lớp tr'c đó (tr'c lớp đầu ra):
$$
\begin{align}
W^{[1]} &= W^{[1]} - \alpha \frac{\partial \mathcal{L} }{ \partial W^{[1]} },\\
b^{[1]} &= b^{[1]} - \alpha \frac{\partial \mathcal{L} }{ \partial b^{[1]} },\\
W^{[2]} &= W^{[2]} - \alpha \frac{\partial \mathcal{L} }{ \partial W^{[2]} },\\
b^{[2]} &= b^{[2]} - \alpha \frac{\partial \mathcal{L} }{ \partial b^{[2]} },\\
\tag{9}
\end{align}
$$
trong đó $\alpha$ là tốc độ học.

Để thực hiện huấn luyện, 