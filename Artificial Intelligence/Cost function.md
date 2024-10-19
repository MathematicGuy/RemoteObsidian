

### **1. Primitive Explanation of Cost Function**

#### **What is a Cost Function?**

**Cost Function** provided a quantitative measure of how well the model's predictions align with the actual data, using a term called predicted value to guide model prediction.

A mathematical function that measures the difference (the "cost" (all ex) or "lost" (single ex)) between the predicted outputs of a model and the actual outputs from the data (i.e. distance between 2 points)

#### **Purpose of a Cost Function**

- **Quantifies Error**: It provides a single scalar value representing the model's error over the entire dataset.
	bc cost function calc the average error over the whole dataset.
- **Guides Optimization**: Minimizing the cost function adjusts the model parameters in a way that reduces error.
	using cost function to guide model for which features are important and which are not by adjusting model's parameters.
- **Feedback Mechanism**: It acts as feedback for algorithms like gradient descent to know in which direction and how much to adjust the parameters. 
	cost funciton tell us how well the model perform thus it act like a feedback mechanism. 


#### **General Form**

For a dataset with $N$ samples, the cost function $J(\theta)$ can be expressed as:

$$ J(\theta) = \frac{1}{N} \sum_{i=1}^{N} \text{Cost Function for Sample } i $$

where $\theta$ represents the parameters of the model.

---

### **2. Cost Function for Logistic Regression**

Now that we've established what a cost function is, let's delve into the specific cost function used in logistic regression.

#### **Why Not Use Mean Squared Error (MSE)?**

In linear regression, the Mean Squared Error (MSE) is commonly used:

$$ \text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 $$

However, using MSE for logistic regression is not appropriate because:

- **Non-Linearity**: Logistic regression uses the sigmoid function, which is non-linear.
- **Non-Convexity**: MSE would result in a non-convex cost function for logistic regression, making optimization difficult due to multiple local minima.
- **Inefficient Learning**: MSE doesn't penalize errors in classification effectively for logistic regression.

#### **Introducing the Logistic Regression Cost Function**

The cost function for logistic regression is derived from the **likelihood function** and is designed to handle binary classification problems effectively.

##### **Sigmoid Function Recap**

First, recall that logistic regression uses the sigmoid function to map any real-valued number into a value between 0 and 1:

$$ \hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}} $$

where $z = \theta^T x$ (dot product of parameters and features).

##### **[[Logarithm and Log-Likelihood Function]]**

The **likelihood function** represents the probability of the observed data given the parameters $\theta$:

$$ L(\theta) = \prod_{i=1}^{N} P(y_i | x_i; \theta) $$
(The possibility of $y_{i}$ given  $x_{i};\theta$)

For logistic regression, the likelihood for each sample is:

$$ P(y_i | x_i; \theta) = \hat{y}_i^{y_i} (1 - \hat{y}_i)^{1 - y_i} $$

To simplify optimization, we take the **logarithm** of the likelihood function to obtain the **log-likelihood function**:

$$ \ell(\theta) = \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$

##### **Cost Function Definition**

The cost function is then defined as the **negative log-likelihood** (we take the negative because we typically minimize cost functions, and maximizing the log-likelihood is equivalent to minimizing the negative log-likelihood):

$$ J(\theta) = - \ell(\theta) = - \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$

This is often divided by $N$ to get the average cost:

$$ J(\theta) = - \frac{1}{N} \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$

#### **Interpretation of the Cost Function**

- **Convexity**: This cost function is convex for logistic regression, ensuring a single global minimum, which makes optimization via gradient descent reliable.
- **Penalization**: It penalizes misclassifications more effectively than MSE.
- **Probabilistic Meaning**: It has a clear probabilistic interpretation, aligning with the principles of maximum likelihood estimation.

#### **Understanding Each Component**

- **$ y_i \log(\hat{y}_i) $**: If the actual label $y_i$ is 1, this term becomes $\log(\hat{y}_i)$, heavily penalizing the cost if $\hat{y}_i$ (the predicted probability) is low.
- **$ (1 - y_i) \log(1 - \hat{y}_i) $**: If the actual label $y_i$ is 0, this term becomes $\log(1 - \hat{y}_i)$, heavily penalizing the cost if $\hat{y}_i$ is high (i.e., the model incorrectly predicts a high probability for class 1).

#### **Graphical Representation**

- **Cost vs. Prediction**: Plotting the cost function against $\hat{y}_i$ for $y_i = 1$ and $y_i = 0$ shows that the cost increases sharply as the prediction deviates from the actual label.
- **Asymmetry**: The cost function is asymmetrical around the prediction errors, which is appropriate for classification tasks.

---

### **Summary**

- **Primitive Cost Function**: A measure of the difference between predicted and actual values, guiding the optimization of model parameters.
- **Logistic Regression Cost Function**: Specifically designed to handle binary outcomes, derived from the negative log-likelihood, and ensures convexity for reliable optimization.

---

### **Key Takeaways**

- **Optimization Goal**: In logistic regression, we aim to find parameters $\theta$ that minimize the cost function $J(\theta)$.
- **Gradient Descent**: We use algorithms like gradient descent to iteratively adjust $\theta$ in the direction that reduces $J(\theta)$.
- **Model Improvement**: Minimizing the cost function leads to a model that predicts probabilities closer to the actual labels, improving classification accuracy.

---

### **Final Thoughts**

Understanding the cost function in logistic regression is crucial because it directly influences how the model learns from data. The cost function provides the necessary feedback to adjust the model parameters in a way that improves its predictive performance on classification tasks.

---

This version now properly uses `$` for inline math formatting.