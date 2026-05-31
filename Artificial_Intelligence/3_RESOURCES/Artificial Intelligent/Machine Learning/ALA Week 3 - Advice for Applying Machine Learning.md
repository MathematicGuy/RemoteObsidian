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

# Bias and Variance
## Diagnosing Bias and Variance
![[Pasted image 20241105155344.png]]
Instead of look Diagnoise by adding more datapoints. A more systematic way to diagnose or to find out if your algorithm has high bias or high variance will be to
>Look at the performance of your algorithm on the training set and on the cross validation set.


**Diagnosing bias and variance**
J_train is the cost of training.
J_cv is the cost of many validationa and training. Thus we come to these conclusion:
![[Pasted image 20241105155746.png]]
+ ? High bias and high variance is like part can be overfit but other part is underfit. 
 ![[Pasted image 20241105155808.png]]

## Regularization and bias/variance
**CV:** Cross Validation

**Linear Regression with regularization**
> The larger $\lambda$ is, the more the algorithm is trying to keep W squared small.
![[Pasted image 20241105170838.png]]

### Regularization and bias/variance
![[Pasted image 20241118141039.png]]
#### Revision
**Motivation:** We need to find a way to avoid underfit and overfit. Underfit can be avoid by adding more features, but by adding our model are vurnerable to overfit. L2 regularization (Lasso Regression) help us to minimize effects of adding features by using $\lambda$. 

**Regularization tradeoff**: As we learn when addressing overfitting
+ For large $\lambda$, $w_{j}$ will be close to 0 making model unable to learn thus underfit. 
+ For small $\lambda$, model focus on minimizing MSE term and not regularization term thus the model remain overfitting.

**How to choose the right $\lambda$ ?**
+ $ Trying a large range of $\lambda$ to pick the right one. The best one is the one  result in the lowest cost $J$. ![[Pasted image 20241105171714.png]]


![[Pasted image 20241118145549.png]]

## Establishing a baseline level of performance
**Baseline**: act like a standpoint/benchmark use to compare/exam model performance. All baseline method to create to serve 1 purposes is to provides some kind of standards for model performance (in calc model loss/cost). 
-> In short, **rather than asking is my training error large, ask is my training error large relative to what `[baseline]` can do on the task?**  
![[Pasted image 20241118154109.png]]
With human level performance as the base line, from example 1 it is clear that training error is 0.2% alway from expected error (i.e. true value) indicate Low Bias while the cv-error is 4.0% alway from training error indicate high variance. (conclusion reverse for example 2 observation)
![[Pasted image 20241119104848.png]]

## Learning Curves
>When you have a larger training set is harder for quadratic function to fit all the training examples perfectly.
![[Pasted image 20241119110617.png]]

#### High Bias learning curves
+ ? When you're fitting the simple linear function, add more data doesn't changes your model much more -> Average training error flattens out after a while.
![[Pasted image 20241119110837.png]]
+ $ So **if your learning algorithms suffers from High Bias, feeding more data doesn't help (by itself) much** (i.e. human level performance). You need to do other thing to help your training algorithm.
![[Pasted image 20241119112113.png]]

#### High Variance learning curves
High Variance result in "too good to be true" loss but do worst on testing data (dat why $J_{train}$ is under the baseline and test data $J_{cv}$ is above the baseline)
+ $ **Adding more trainning data will subdue high variance** bc it overload the training algorithm and increase losses/error.
![[Pasted image 20241119113121.png]]
+ ! notice that more trainning data -> more expensive

### What to do next ? 
![[Pasted image 20241119113510.png]]
> [[L2 (Ridge Regression) Terms]]

#### Observation
+ $ **Large Prediction Errors $\to$ High Bias:**
+ **Try adding polynomial features** 
	_Increases the model's complexity, allowing it to capture more intricate patterns in the data._
+ **Try getting additional features** 
	_Adding relevant features provide the model with more information to reduce bias._
+ **Decrease** $\lambda$, 
	*High bias mean the LA is overly simplistic and not paying enough attention to the training set. Decrease $\lambda$ reduces the penalty on the 2nd terms weights and switch LA attention to the 1st term (i.e. training set) and less to 2nd term (i.e. regularization term), focus on the training mean reduce bias)*


+ $ **If High Variance:**
+ **Get more training example** 
	_help model to generalize more data, reducing overfitting and variance_
+ **Try getting additional features**
	_help model to generalize more features, though care is needed to avoid noisy or redundant features that might worsen overfitting._  
+ **Try smaller sets of features** 
	_sometime adding more features gives your algorithm too much flexibility to fit very complicated models (**Reduce numbers of less important features** is good tactics to **fix high variance**)_
+ **Increase** $\lambda$ 
	*High Variance mean the LA fit the trainning so well that it fail to generalize (i.e. understand unseen data ). Increase $\lambda$ help LA pay more attention to the 2nd term and focus on understanding underlying patterns of more features which help to reduce variance)* 

