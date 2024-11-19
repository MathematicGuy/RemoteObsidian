**Motivation:** **prediction errors** can be decomposed into 2 main components: **error from bias and error from variance**. The tradeoff between a model's ability to **minimize bias and variance is foundation to training machine learning models.** 

### Bias and Variance Fomula
$$Bias(\hat{Y})= \mathbb{E}[\hat{Y}] - Y$$$$Variance = \mathbb{E}[(\hat{Y} - \mathbb{E}[\hat{Y}])^2]$$
where $\mathbb{E}[\hat{Y}]$ is the expected predicted value, and $Y$ is the true value.


### Bias vs Variance Tradeoff 
**Total Error Fomula:** The decomposition formula combines Bias and Variance
$$\text{MSE} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}$$
(note: [[Irreducible Error]])

**Summary**
![[Pasted image 20241117160551.png]]
+ Green: predicted value, Black: true value.
+ **Bias** indicate **the average distance of the predicted values to the true value** 
	**High Bias:** *predicted values* far from the *true value*. -> Model is underfit (i.e. pays very little attention to the training data and oversimplified)
	**Low Bias:** *predicted values* close to the *true value* -> Model have the ability to capture the true underlying patterns or relationship (of each datapoints) present in the data. 
	
+ **Variance** indicate **the distance between the predicted values**. 
	**High Variance:** *predicted values* are scatter from eachother
	**Low Variance:** *predicted values* are close to eachother.  

```ad-success
**High Bias, Low Variance:** highly concentrate predicted values that are close to the true value. 

**Low Bias, High Variance:** scatter predicted values that are far from the true value

**Low Bias, Low Variance:** predicted values close to to true value and close from eachother. 

**High Bias, High Variance:** predicted values far from the true value and far from eachother.
```


```ad-abstract
**Bias:** Bias refers to the error due to **overly simplistic model & assumption**. This **make model easier to comprehend and learn but might not capture the underlying complexities of the data**.  It is the error due to the model’s **inability to represent the true relationship between input and output** accurately. When a model has poor performance both on the training and testing data means high bias because of the simple model, indicating **underfitting**.   

**Variance:** Is the error due to **model sensitivity to changes in data**, making it **prediction inconsistent**. High variance occurs when a model **learn the training data's noise and random fluctuations rather than the underlying pattern**. As a result, the model **performs well on the training data but poorly on the testing data (i.e. unseen data), indicate overfitting**.
```
![[Pasted image 20241118090525.png]]

### Ideally, we need Low Variance and Low Bias. 
![[Pasted image 20241118093049.png]]
- **Bias is Error resulted from Training set.**
- **High Bias == High Training error.**
- **Low Bias == Low Training error**
- **Variance is error resulted from Test set.**

![[Pasted image 20241118093102.png]]

---

## Reasons and Technique to reduce Underfitting and Overfitting

**Underfitting:** when you build **model that are too simple**, so it kinda dumb. Model underfit the most when it has **High bias and Low Variance**

**Reasons for Underfitting**
1. The model is too simple, So it may be not capable to represent the complexities in the data.
2. The input features which is used to train the model is not the adequate representations of underlying factors influencing the target variable.
3. The size of the training dataset used is not enough.
4. Excessive regularization are used to prevent the overfitting, which constraint the model to capture the data well.
5. Features are not scaled.
 
**Techniques to Reduce Underfitting**
1. Increase model complexity.
2. Increase the number of features, performing [feature engineering](https://www.geeksforgeeks.org/what-is-feature-engineering/).
3. Remove noise from the data.
4. Increase the number of [epochs](https://www.geeksforgeeks.org/epoch-in-machine-learning/) or increase the duration of training to get better results.


**Overfitting/Overlycomplex:** fit the current data so good that it starts learning from noise and inaccurate data too (e.g. like a overly obey child learning in a cult) The model doesn not categorize the data correctly, because of too many noise and details. 

**Reasons for Overfitting:**
1.  High variance and low bias.
2. The model is too complex.
3. The size of the training data.

**Techniques to Reduce Overfitting**
1. Improving the quality of training data reduces overfitting by focusing on meaningful patterns, mitigate the risk of fitting the noise or irrelevant features.
2. Increase the training data can improve the model’s ability to generalize to unseen data and reduce the likelihood of overfitting.
3. Reduce model complexity.
4. [Early stopping](https://www.geeksforgeeks.org/regularization-by-early-stopping/) during the training phase (have an eye over the loss over the training period as soon as loss begins to increase stop training).
5. [Ridge Regularization](https://www.geeksforgeeks.org/lasso-vs-ridge-vs-elastic-net-ml/) and [Lasso Regularization](https://www.geeksforgeeks.org/implementation-of-lasso-regression-from-scratch-using-python/).
6. Use [dropout](https://www.geeksforgeeks.org/dropout-in-neural-networks/) for [neural networks](https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/) to tackle overfitting.

![[Pasted image 20241118092644.png]]

---
### Machine Learning Model Performance

**Purpose:**
Machine learning model performance is a **measure of how well a model predicts the target variable based on the provided features**. It's typically **assessed using metrics like accuracy, precision, recall, F1-score, mean squared error, etc.**, depending on the type of problem (classification, regression, etc.). A **good performing model** is one that **generalizes well to unseen data, providing accurate predictions**


**Bias and Variance: (one more time let us study this)**

- **Bias**: Bias refers to the difference between the predicted values by the model and the true values. A model with high bias oversimplifies the data, often missing important patterns or relationships.
- **Variance**: Variance is the variability of model predictions for a given data point. A model with high variance models the noise in the data rather than the actual underlying patterns.

**Bias, Variance, Underfitting & Overfitting: (Important to know)**

- **Underfitting**: **High bias, low variance.** The model is too simple to capture the complexity of the data, resulting in poor performance on both the training and unseen data. **An underfit model is too simple to accurately capture the relationships between its features X and label Y.**

- **Overfitting**: **Low bias, high variance**. The model is overly complex, capturing noise and irrelevant patterns from the training data, leading to excellent performance on training data but poor performance on unseen data. **Overfitting refers to the case when a model is so specific to the data on which it was trained that it is no longer applicable to different datasets.**

- **High Bias and Low Variance:** Consistent but inaccurate due to oversimplification.

- **High Variance and Low Bias:** Accurate but inconsistent, capturing noise and overfitting to the training data.

**Ways to Address Bias and Variance:**

- **Regularization**: Adding a regularization term to the model's cost function penalizes complexity, discouraging overfitting. This can be L1 (Lasso) or L2 (Ridge) regularization.

- **Cross-validation**: Use techniques like k-fold cross-validation to assess model performance. It helps to ensure that the model's performance is consistent across different subsets of the data.

- **Feature Engineering**: Properly select and engineer features to help the model better capture the underlying patterns in the data.

- **Ensemble Methods**: Combine multiple models (e.g., Random Forest, Gradient Boosting) to reduce variance and improve predictive performance.

- **Data Augmentation**: Increase the diversity of the training data by generating more samples, helping the model generalize better.

---

source and reference: 
+ [Machine Learning Models: Variance & Bias Impact](https://www.linkedin.com/pulse/machine-learning-models-variance-bias-impact-subbu-mahadevan/)
+ [Bias an Variance Tradeoff](https://www.geeksforgeeks.org/bias-vs-variance-in-machine-learning/)
