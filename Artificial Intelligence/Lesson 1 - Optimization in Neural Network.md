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
![[Pasted image 20240927085639.png]]+

### Sigmoid Function
input - x
output - y
![[Pasted image 20240927092127.png]]

Sigmoid function crunches the entire number line into the interval (0, 1) and is that its derivative is really nice.
 ![[Pasted image 20240927092320.png]]
 ![[Pasted image 20240927092450.png]]



![[Pasted image 20240927092622.png]]
