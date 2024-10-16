note: logistic regression can be non-linear.



### Cost function vs Loss function
$$J(\vec{w}, b)$$This is the cost function. It represents the average error over all the training examples. In the context of gradient descent, the goal is to minimize this cost function by adjusting the model parameters $\vec{w}$ and $\vec{b}$.

 $$L \left(f_{\vec{w}, b}(\vec{x^{(i)}, y^{(i)}})\right)$$This is the loss function. It measures how well the model's prediction  matches the actual target $y^{(i)}$ for a single training example $i$.

**Cost function:** $J(\vec{w}, b)$ applies to the entire training set.
**Loss function:** $L(\dots)$ applies to a single training examples
