# Advice for applying machine learning
## Evaluate a model
> See how to improve a model
![[Pasted image 20241104144828.png]]

**Split a part to test your model**
![[Pasted image 20241104144948.png]]

**Regularization Revision**
+ ? **Regularization** help **reduce the effect of the current features** by **adding features which help to build accurate curve** but not overfitting. 
	The model then tweaking these features base on their important and find the best fit.
![[Pasted image 20241104150446.png]]


![[Pasted image 20241104145447.png]]
![[Pasted image 20241104145515.png]]
+ ? Your training cost $J_{train}$ can be low while the $J_{test}$ can be high, this is because training accuracy doesn't reflect real world accuracy. 
 
Example for **classification problem using Regularization Logistic Regression**. 
![[Pasted image 20241104145743.png]]

**A commonly used method** is **instead of using the logistic loss** to compute the test error and the training error, we **measure what the fraction of the test set**.
![[Pasted image 20241104151244.png]]
+ ? **Fraction of correctly classified examples :** simply the accuracy of all predictions. 
	Example for **spam or not spam classification**, Instead of looking at the logistic loss, we’d report the test error as the **fraction of correct predictions**, which is **85/100 = 0.85**, or **85% accuracy**.

Train model with many different amount of parameters, and choose the one with lowest loss. So choose $J_{test}(W^{<5>},b^{<5>})$, if it the lowest loss for example:
![[Pasted image 20241104161140.png]]
note: d as degree of polynomial (bậc của đa thức)
### Training/cross validation/test set
Split data into 3 parts. 
+ ? **Cross Validation** use to check or cross check the validity or really the **accuracy of different models.** 
![[Pasted image 20241104161426.png]]
note: some time it called the development set or the dev set.

Pick Model using Cross-Validation. Estimate Generalization error using the test set J.
![[Pasted image 20241105143539.png]]

Validation is when you choose 1 part for testing out of all part.. Cross-validation is when you traverse through the whole dataset, for each part can be chosen, use it as the validate data and other as the training data. 
Ex: 5 block. For each block, choose 1 block for validate (orange), 4 block for training (blue) until there are no block that  haven't been trained. 
![[Pasted image 20241105150428.png]] ![[Pasted image 20241105151031.png]], repeat until all block been trained. 

# Bias and Variance
![[Pasted image 20241105155344.png]]

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

