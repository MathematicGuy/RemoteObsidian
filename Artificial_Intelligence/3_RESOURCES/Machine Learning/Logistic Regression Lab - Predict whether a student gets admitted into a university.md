**X**
![[Pasted image 20241021232850.png]]

**Y**
![[Pasted image 20241021232857.png]]

**m = 100**
![[Pasted image 20241021232916.png]]

**Plot**
![[Pasted image 20241021233042.png]]

![[Pasted image 20241021233417.png]]

**Gradient for logistic regression**
![[Pasted image 20241022001923.png]]
**Partial Derivative**
![[Pasted image 20241022001943.png]]

![[Pasted image 20241022002926.png]]

![[Pasted image 20241022011834.png]]

![[Pasted image 20241022015716.png]]

![[Pasted image 20241022090149.png]]

![[Pasted image 20241022090203.png]]

Note: Re-frame exam into hw take roughly 23 minutes
Question: why GD for Linear regression depend on m while independent GD have flexible iterations ?
+ $ **Conclusion:** Practice feature mapping and how to map fomular then code it.  


--- 

Feature mapping involves creating additional features by generating polynomial combinations of the original features. This is done to allow the model (in this case, a logistic regression classifier) to learn more complex relationships and fit the data better, especially when the decision boundary is nonlinear.

Let's break it down using your example.

### Original Features:
You have two features $x_1$ and $x_2$. These could be, for example, two test scores (as per your description). Without feature mapping, a logistic regression model would try to find a **linear** decision boundary between classes based on these two features.

### What is Feature Mapping?
Feature mapping transforms these original features ($x_1$, $x_2$) into higher-dimensional space by introducing polynomial combinations of these features. This allows the model to create more complex, **nonlinear decision boundaries**.

### Polynomial Feature Mapping:
In this case, you're transforming the original two features $x_1$ and $x_2$ into a set of polynomial terms up to the **sixth power**. The new features include:

1. Original features: $x_1$, $x_2$
2. Squared terms: $x_1^2$, $x_2^2$, $x_1 x_2$
3. Cubic terms: $x_1^3$, $x_2^3$, $x_1^2 x_2$, $x_1 x_2^2$
4. Higher powers: $x_1^k$, $x_2^k$, and mixed terms like $x_1^a x_2^b$ where $a + b \leq 6$.

This results in a feature vector of **27 dimensions** as you combine different powers of $x_1$ and $x_2$. Here’s a simplified example of what the feature vector would look like:

$$\text{map\_feature}(x) = 
\left[\begin{array}{c}
x_1\\
x_2\\
x_1^2\\
x_1 x_2\\
x_2^2\\
x_1^3\\
x_1^2 x_2\\
x_1 x_2^2\\
x_2^3\\
\vdots\\
x_1 x_2^5\\
x_2^6\end{array}\right]$$
for each (n degree) iteration :
start from index 0, append x1 and x2 where
$x_{1}^{(i-j)} * x_{2}^j$ 
Ex:
i = 1, j = 0
i = 2, j = 1
i = 1, j = 0



This higher-dimensional feature space enables the logistic regression model to learn a more complex decision boundary, which would be nonlinear when projected back onto the original 2D feature space.

### Why is this useful?
In logistic regression, without feature mapping, the classifier would create a **linear decision boundary** between the classes, which may not always capture the underlying patterns in the data. By mapping the features into a higher-dimensional space, the logistic regression model can now fit a **nonlinear decision boundary**, allowing it to separate classes that aren't linearly separable.

For instance:
- A **linear decision boundary** in 2D space would be a straight line.
- With feature mapping, the decision boundary could be curved or more complex, potentially following the true underlying structure of the data.

### Example:
If you were trying to classify data points based on their scores on two tests (represented by $x_1$ and $x_2$), mapping these features into polynomial combinations allows the logistic regression model to create more sophisticated decision boundaries that better classify the students based on their scores.

### Code Example for `map_feature` Function:
Here’s what the `map_feature` function might look like:

```python
def map_feature(x1, x2):
    degree = 6
    mapped_features = [np.ones(len(x1))]  # Start with a bias term (x^0)
    
    for i in range(1, degree + 1):
        for j in range(i + 1):
            mapped_features.append((x1 ** (i - j)) * (x2 ** j))
    
    return np.vstack(mapped_features).T
```

This code will transform the two original features $x_1$ and $x_2$ into a 27-dimensional feature space, which can then be used to train the logistic regression classifier.