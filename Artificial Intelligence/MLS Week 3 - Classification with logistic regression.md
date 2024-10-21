note: logistic regression can be non-linear.
### [[Cost function]] vs Loss function
$$J(\vec{w}, b)$$This is the **cost function.** It **represents the average error over All the Training Examples**. In the context of gradient descent, the goal is to minimize this cost function by adjusting the model parameters $\vec{w}$ and $\vec{b}$.

 $$L \left(f_{\vec{w}, b}(\vec{x^{(i)}, y^{(i)}})\right)$$This is the **loss function.** It **measures how well the model's prediction**  matches the actual target $y^{(i)}$ for a **Single Training Example** $i$.

**Cost function:** $J(\vec{w}, b)$ applies to the entire training set.
**Loss function:** $L(\dots)$ applies to a single training examples

---
# Classification with logistic regression
### Motivation
Classify Spam using linear regression upon a threshold >= 0.5
![[Pasted image 20241017143836.png]]
But if there a outlier tumor size x, it cause much worst function for this classification probelm. 
![[Pasted image 20241017144159.png]]
In the next section we will learn about decision boundary and logistic regression (although it called regression but used for classification problem)
> The example above demonstrates that the linear model is insufficient to model categorical data.

## Logistic Regresison
Look quite the same as Sigmoid function. What different is Sigmoid took both neg and pos value on x-axis while logistic only took positive.
![[Pasted image 20241017151630.png]]

**Logistic Regression Model** 
> In Neural Network, algorithm with the word "model" refer to puting the algorithm's function into a activation function to output a certain result. 

return output between 0 and 1. input line function z 
( put **logistic regression** fomula: $z = \vec{w}.\vec{x} + b$ into sigmoid function $\sigma$ )
![[Pasted image 20241017165923.png]]
How to interpret (diễn giải) the output of logistic regression: 
![[Pasted image 20241017170515.png]]
The function **output the probability of y = 1** (i.e. how many % that y = 1) given x, w and b.** 
![[Pasted image 20241018104314.png]]

## Decision Boundary
![[Pasted image 20241018100807.png]]
>The output g(z) is determine by z which is w,x and b represent on the x-axis. So if $z >= 0$ then $g(z)$ closer to 1 and if $z < 0$ then $g(z)$ closer to 0. Apply a threshold of 0.5 where tumor is maglinant as $\hat{y}=1$ and  $\hat{y}=0$ for tumor that not. With sigmoid function, it clearly $\hat{y}=1$ if $z \geq 0$ and  $z < 0$ then $\hat{y} = 0$.
	note: understand relationship between e and log

At $z=0$ we call that a decision boundary

Let's figure out when wx plus b is **greater than equal to 0 and when wx plus b is less than 0.**
-> z exactly = 0
![[Pasted image 20241018105739.png]]
![[Pasted image 20241018105929.png]]
+ $ Use Function to map out the decision boundary which is when the function = 0. Using the state inside or outside the function as 0 and 1 to classified point in space.

## Cost Function for [[Logistic Regression]]
+ Using **cost function with linear regression** we **got a convex**, which is **very good for gradient descent in minimizing loss.**
+ However, when apply **cost function with logistic regression** we **got a non-convex graph that contain multiple local-minimal.** Thus for Logistic Regression, Square Error Cost function is **not a good choice**
![[Pasted image 20241018155657.png]]

**Denote the loss suround in blue via capital L** as the **function of the prediction of the learning algorithm.** where $y^{(x)}$ is the **true label** and $f_{\vec{w}, b}(\vec{x^{(i)}})$ is the **predicted label**. (we want the predict label close to true label)
![[Pasted image 20241018160107.png]]
+ ? Remember, the **Loss Function measures how well you're doing on one training example**. And is **by summing up the losses on all of the training examples** that you then get, the **Cost Function**.

>F is the output of logistic regresison thus f is always between 0 and 1. As for the loss when y is equal to 1 we see that as
>+  f get closer to 0, loss (y-axis) increase to infinity.
>+ f get closer to 1, loss (y-axis) decrease to 0
![[Pasted image 20241018161323.png]]

>On this slide, let's look at the second part of the loss function corresponding to when y is equal to 0.
![[Pasted image 20241018163452.png]]

![[Pasted image 20241018163704.png]]

### Simplified loss function
**y equal only 0 or 1**
![[Pasted image 20241021141609.png]] 

### Gradient Descent Implementation
**Training logistic regression**
![[Pasted image 20241021144235.png]]

![[Pasted image 20241021144432.png]]

Use GD as a tool to update paramaters for Logistic Regression.
![[Pasted image 20241021144455.png]]

## Regularization to Reduce Overfitting
#### The Problem of Overfitting
>Regression Example
![[Pasted image 20241021145738.png]]
+ ? Overfit: might have too many features 
+ $ You can fix this by train model on the more relevant features rather than un-useful features, it may generalize better to new examples.
+ $ Add more data points to the dataset help model to generalize better to new examples. 
![[Pasted image 20241021150214.png]]

#### Addressing overfitting
When overfitting occur, find more data (i.e.  more training example):
 ![[Pasted image 20241021151627.png]]

##### Feature Selection: Choose features that are useful and remove those aren't.
![[Pasted image 20241021151754.png]]

#### Regularization (reduce overfitting)
+ $ Regularization reduce the effect of the selected features while reserve all features, this can help to build accurate curve but not overfitting.
+ ? Use this to Regularize un-useful features.
Setting a feature to 0 or close to 0 to eliminate feature.
![[Pasted image 20241021152154.png]]

### Cost function with regularization
![[Pasted image 20241021153601.png]]
**For example:** replace $w_{3}, w_{4}$ with 0.001.
penalize (pronoun as pi-nerlized)
+ ? Simpler model less likely to overfit.

So we have 100 parameters W1 through W100, because we **don't know whick of these parameters are going to be the important ones. Let's penalize all of them** by adding $\lambda$ multiplyng with $W$ : 
![[Pasted image 20241021155704.png]]
+ ? $\lambda$: **regularization factor**, treat it like learning rate $\alpha$. (divided by 2 to scale equally to the cost function)
+ ? $b$ also **used for regularization for special cases**. but make a very low diff in practice. normally just use $\lambda$.
![[Pasted image 20241021155934.png]]

**Summarize**
> Want to **minimize the "original cost: mean square error + regularization term"**
![[Pasted image 20241021160834.png]] 
  This new cost function trades off 2 goals that you might have. 
  + If you set $\lambda=0$ , you end up with this overly wiggly and complex curve. ***Overfit*** ($\lambda$  too small)
	  ![[Pasted image 20241021161648.png]]
+ If $\lambda=10^{10}$, $w$ in regularization term would be very large and the only way to minimize this is $\lambda \approx 0$. **So if $\lambda$ is very very large, the learning algorithm will adjust** $W_{1}, W_{2}, W_{3}$ and $W_{4}$ to be **extremely close to 0**. So F(x) is basically equal to $b$ thus **representing a straight line.** ***Underfit*** ($\lambda$ too large)
	![[Pasted image 20241021161936.png]]
	![[Pasted image 20241021162026.png]]
+ Choose just right $\lambda$

## Regularized linear regression
+ ? Learn to make GD work with Regularized linear regression.
![[Pasted image 20241021162536.png]]
>We don't change $b$ because the regulization term force us to change $w_{j}$ not $b$.
>($w_j$ represent new added features)

![[Pasted image 20241021163015.png]]
**Example** how $w_{j}$ shrink a little by 1 iteration.
![[Pasted image 20241021163218.png]]

**Partial derivative w.r.t $w_{j}$ for calc the Gradient Descent:**
![[Pasted image 20241021163422.png]]

### Regularized logistic regression
>Modify cost function -> Add $\lambda$ function
![[Pasted image 20241021211350.png]]

>How to minimize the cost function ? Just like linear regresion, except for F(x) function, its logistic regression. 
![[Pasted image 20241021224305.png]]

[[Logistic Regression Lab - Predict whether a student gets admitted into a university]]