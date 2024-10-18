note: logistic regression can be non-linear.
### Cost function vs Loss function
$$J(\vec{w}, b)$$This is the cost function. It represents the average error over all the training examples. In the context of gradient descent, the goal is to minimize this cost function by adjusting the model parameters $\vec{w}$ and $\vec{b}$.

 $$L \left(f_{\vec{w}, b}(\vec{x^{(i)}, y^{(i)}})\right)$$This is the loss function. It measures how well the model's prediction  matches the actual target $y^{(i)}$ for a single training example $i$.

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
return output between 0 and 1. input line function z 
![[Pasted image 20241017165923.png]]
Output Example:
![[Pasted image 20241017170515.png]]

## Decision Boundary
