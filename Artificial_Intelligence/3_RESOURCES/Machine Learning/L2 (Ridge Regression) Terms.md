1) **1st term:** $$\frac{1}{m}\sum^{m}_{i=1}(f_{\vec{w}, b}(\vec{x}^{(i)}) - y^{(i)})$$
- **Represents the training data**: This is the mean squared error (MSE) between the predicted values $f_{\vec{w}, b}(\vec{x}^{(i)})$  and the actual target values $y^{(i)}$ in the training set.
	
- The model tries to minimize this term to fit the training data as closely as possible.


2) **2nd term (Regularization term):** $$\frac{\lambda}{2m}\sum^{n}_{j=1}w_{j}^2$$
- **Represents the regularization penalty**: This is the sum of the squared weights $w_{j}^2$ multiplied by the regularization parameter $\lambda$.
	
- It **discourages the model from assigning very large values to the weights**, thereby **limiting the model's complexity and helping it generalize better to unseen data.** (basically generalize new data by make model see its training data less important, by generalizing I mean fit polynomial function too close to each training data points)
