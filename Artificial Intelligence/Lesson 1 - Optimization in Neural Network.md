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
Loss function: $\frac{1}{m}\left(Y- \hat{Y}\right)^2$.
+ ? $\left(Y- \hat{Y}\right)^2$ represent Loss and $\frac{1}{m}$ calculate the average loss.  
+ $ So for other Loss function, we just need to replace equation inside the bracket $( )$    

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

>Our perceptron will have 2 nodes: `W_1` and `W_2` determine how important any other features are, say the word `aack` is really **correlated with happiness** then **W_1 going to be a larger number**, if `beep` is really **irrelevant (ko liên quan)** then **W2 is going to be a small number**.
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
+ ? How do these biases affect the loss? with partial derivative. In other words, this partial derivative tell us exactly what direction to move each one of the weights and biases in order to reduce the log loss function.                                                                                                                                               ![[Pasted image 20240930163826.png]]



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

