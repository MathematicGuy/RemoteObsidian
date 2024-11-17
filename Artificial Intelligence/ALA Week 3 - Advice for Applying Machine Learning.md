# Advice for applying machine learning
## Evaluate a model
> See how to improve a model
![[Pasted image 20241104144828.png]]

**Split a part to test your model** instead of all for training
![[Pasted image 20241104144948.png]]
m_train and m_test are just like everyother input variable, thus the function stay the same, just change the input:
![[Pasted image 20241115141717.png]]
![[Pasted image 20241115141739.png]]
![[Pasted image 20241115141824.png]]

**Train/test procedure for linear regression (with squared error cost)**
+ ? with J test high, we knew the model done well on training set but worst on test set. 
![[Pasted image 20241115141916.png]]

**How to apply train/test Procedure ?**
**Loss Function:** Normal Loss Function + Regularization Term $\frac{\lambda}{2m_{train}}\sum^{n}_{j=1}w_{j}^2$
**Compute test error & train error:** The same  
![[Pasted image 20241115142236.png]]


 
**Regularization Revision**
+ ? **Regularization** help **reduce the effect of the current features** by **adding features which help to build accurate curve** but not overfitting. 
	The model then tweaking these features base on their important and find the best fit.
![[Pasted image 20241104150446.png]]


![[Pasted image 20241104145447.png]]
![[Pasted image 20241104145515.png]]
+ ? Your training cost $J_{train}$ can be low while the $J_{test}$ can be high, this is because training accuracy doesn't reflect real world accuracy. 
 
Example for **classification problem using Regularization Logistic Regression**. 
![[Pasted image 20241104145743.png]]

**A commonly used method** is **instead of using the logistic loss** to compute the test error and the training error, we **measure what the fraction of the test set**. (i.e. calc Loss of test and train respectively)
![[Pasted image 20241104151244.png]]
+ ? **Fraction of correctly classified examples :** simply the accuracy of all predictions. 
	Example for **spam or not spam classification**, Instead of looking at the logistic loss, we’d report the test error as the **fraction of correct predictions**, which is **85/100 = 0.85**, or **85% accuracy**.

### Model selection and training/cross validation/test sets
![[Pasted image 20241115143117.png]]
+ ? Data that is not in the training set is a better indicator for model performance base.

**Model Selection through trials and errors**
**Train model** with **different amount of parameters,** and **choose the one with lowest loss**. 
![[Pasted image 20241104161140.png]]
+ ? To check how well the model performed, report test set error.
+ $ So choose $J_{test}(W^{<5>},b^{<5>})$ since it the lowest loss:
note:
+ **generalization error:** mean the average error on new examples that were not in the training set. 
+ **optimistic estimate** mean it likely to be lower than the actual **generalization error**.
+ **d** mean **"degree"** of polynomial (bậc của đa thức)
![[Pasted image 20241115143930.png]]

**Here's how you modify the training and testing procedure in order to carry out model selection.**
	model selection mean choosing among diff models you might contemplate using for your ML application.

### Training/cross validation (k-fold validation)/test set
Split data into 3 parts: trainning set 60%, cross-validation 20%, test set 20%
+ ? **Cross Validation** use to check or cross check the validity or really the **accuracy of different models.** 
![[Pasted image 20241104161426.png]]
note: some time it called the development set / dev set.

Fomular for calc Loss remain the same, just diffs inputs.
![[Pasted image 20241115145039.png]]

**Model (with diff parameters) Selection with Cross-Validation** and **Estimate error with test set** (rather than just validate using test set alone)
![[Pasted image 20241115145555.png]]
+ ? This also work for choosing **different Neural network architecture**
![[Pasted image 20241105143539.png]]
How this work:
+ Get w, b of each mode.
+ Calc Cost of each model using Cross Validation dataset. 
+ Pick the model with lowest Cross-Validatation error.
+ Only when you picked the best model, evaluate it on the test set. **Because your Model Haven't Been Validate on the Test Set, it Give Out a Fair Estimation of How Well Your Model Generalize on New Datas**. 

+ ? Other Methods:
**Validation** is refer to **splitting yor dataset into training and validation subsets**.
**Cross-validation** or **k-fold cross-validation**:
+ **For every part, choose 1 part to validate data and 4 part to the training data. Repeat until all part have been validate.** 
**Ex:** 5-fold cross-validation. 
**Step 1:** Divided the data into 5 parts
**Step 2:** For each iteration (5 iterations):
	choose 4 parts for training and 1 part for validation:
![[Pasted image 20241105150428.png]] ![[Pasted image 20241105151031.png]]
**Step 3**: Aggregate the results from all 5 iterations to compute a final performance metric.

---
**Code for mapped polynomial degree:**
![[Pasted image 20241115161605.png]]
```python
# Step 1: Initial the polynomial 
n = 2 # 2nd degree polynomial
poly = PolynomialFeatures(degree=n, include_bias=False)

# Step 2: Map data to the new polynomial
# Compute the number of features and transform the training set
X_train_mapped = poly.fit_transform(x_train)
```


# Diagnosing Bias and Variance
![[Pasted image 20241105155344.png]]
High Bias - large errors

**Diagnosing bias and variance**
J_train is the cost of training.
J_cv is the cost of many validationa and training. Thus we come to these conclusion:
![[Pasted image 20241105155746.png]]
+ ? High bias and high variance is like part can be overfit but other part is underfit. 
 ![[Pasted image 20241105155808.png]]

### Regularization and bias/variance
**CV:** **C**ross **V**alidation

**Linear Regression with regularization**
> The larger $\lambda$ is, the more the algorithm is trying to keep W squared small.
![[Pasted image 20241105170838.png]]

**how can you choosing the right $\lambda$ ?**
+ $ Trying a large range of $\lambda$ to pick the right one. The best one is the one  result in the lowest cost $J$. ![[Pasted image 20241105171714.png]]

![[Pasted image 20241105172527.png]]

