The given function \( L(\theta) \) is the **log-likelihood** (or cross-entropy loss) for logistic regression, where \( \sigma(\cdot) \) is the **sigmoid function**, and you're looking for the derivative with respect to the parameter vector \( \theta \). Let's break it down step-by-step to find \( \frac{\partial L(\theta)}{\partial \theta} \).

### Given Function:
The function is:

\[
L(\theta) = \sum_{i=1}^{n} \left[ y_i \log(\sigma(\theta^T \bar{x}_i)) + (1 - y_i) \log(1 - \sigma(\theta^T \bar{x}_i)) \right]
\]

Where:
- \( \theta \) is the vector of model parameters.
- \( \bar{x}_i \) is the feature vector for the \( i \)-th sample.
- \( y_i \) is the actual label for the \( i \)-th sample (binary: 0 or 1).
- \( \sigma(\cdot) \) is the **sigmoid function** defined as:
  \[
  \sigma(z) = \frac{1}{1 + e^{-z}}
  \]

### 1. **Sigmoid Derivative**:
We will need the derivative of the sigmoid function \( \sigma(z) \) with respect to \( z = \theta^T \bar{x}_i \). The derivative of \( \sigma(z) \) is:

\[
\frac{d}{dz} \sigma(z) = \sigma(z)(1 - \sigma(z))
\]

This will be useful in the chain rule later.

### 2. **Derivative of the Loss Function**:

Let’s now compute the derivative of \( L(\theta) \) with respect to \( \theta \).

#### Step 1: Chain Rule for Each Term

The derivative of each term in the sum can be broken into two cases, one for each part of the expression.

For the first term \( y_i \log(\sigma(\theta^T \bar{x}_i)) \):
\[
\frac{\partial}{\partial \theta} \left[ y_i \log(\sigma(\theta^T \bar{x}_i)) \right] = y_i \cdot \frac{1}{\sigma(\theta^T \bar{x}_i)} \cdot \frac{\partial \sigma(\theta^T \bar{x}_i)}{\partial \theta}
\]

Using the chain rule and the fact that \( \frac{\partial \sigma(\theta^T \bar{x}_i)}{\partial \theta} = \sigma(\theta^T \bar{x}_i)(1 - \sigma(\theta^T \bar{x}_i)) \cdot \bar{x}_i \), we get:

\[
\frac{\partial}{\partial \theta} \left[ y_i \log(\sigma(\theta^T \bar{x}_i)) \right] = y_i \cdot (1 - \sigma(\theta^T \bar{x}_i)) \cdot \bar{x}_i
\]

For the second term \( (1 - y_i) \log(1 - \sigma(\theta^T \bar{x}_i)) \):
\[
\frac{\partial}{\partial \theta} \left[ (1 - y_i) \log(1 - \sigma(\theta^T \bar{x}_i)) \right] = -(1 - y_i) \cdot \frac{1}{1 - \sigma(\theta^T \bar{x}_i)} \cdot \frac{\partial (1 - \sigma(\theta^T \bar{x}_i))}{\partial \theta}
\]

Again, applying the chain rule and simplifying, we get:

\[
\frac{\partial}{\partial \theta} \left[ (1 - y_i) \log(1 - \sigma(\theta^T \bar{x}_i)) \right] = -(1 - y_i) \cdot \sigma(\theta^T \bar{x}_i) \cdot \bar{x}_i
\]

#### Step 2: Combining the Two Terms

Now, combining both derivatives for each term in the summation:

\[
\frac{\partial L(\theta)}{\partial \theta} = \sum_{i=1}^{n} \left[ y_i \cdot (1 - \sigma(\theta^T \bar{x}_i)) \cdot \bar{x}_i - (1 - y_i) \cdot \sigma(\theta^T \bar{x}_i) \cdot \bar{x}_i \right]
\]

#### Step 3: Simplification

Notice that both terms involve \( \bar{x}_i \). Factor it out:

\[
\frac{\partial L(\theta)}{\partial \theta} = \sum_{i=1}^{n} \left[ (y_i - \sigma(\theta^T \bar{x}_i)) \cdot \bar{x}_i \right]
\]

### Final Gradient:

The gradient of the log-likelihood function (or cross-entropy loss) with respect to \( \theta \) is:

\[
\frac{\partial L(\theta)}{\partial \theta} = \sum_{i=1}^{n} (y_i - \sigma(\theta^T \bar{x}_i)) \cdot \bar{x}_i
\]

### Interpretation:

- \( y_i - \sigma(\theta^T \bar{x}_i) \) is the **error** for each data point \( i \). This is the difference between the actual label \( y_i \) and the predicted probability \( \sigma(\theta^T \bar{x}_i) \).
- The gradient sums up the weighted errors for each data point, where the weight is the feature vector \( \bar{x}_i \).

This is the gradient used in gradient descent optimization to minimize the loss function in logistic regression.