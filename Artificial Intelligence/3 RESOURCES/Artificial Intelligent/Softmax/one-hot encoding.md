The **softmax log-likelihood** formulation leverages **one-hot encoding** primarily to **simplify the computation of the loss function**, especially when **dealing with matrix or vector operations**. Here's why and how this works in practice:

### 1. Purpose of One-Hot Encoding in Softmax Log-Likelihood

In the softmax log-likelihood, one-hot encoding allows us to:
1. **Select the correct class probability** in a way that's efficient for matrix and vector operations.
2. **Eliminate unnecessary probabilities** for classes that are not the true class, reducing computational overhead and simplifying the math.
3. **Easily implement the loss function using linear algebra operations**, making it much more efficient when implemented in software (especially with large datasets and multiple classes).

### 2. How It Works with Matrix/Vector Multiplication

Let’s say we have:
- $N$ samples in our dataset.
- $C$ possible classes (e.g., for a 4-class problem, $C = 4$).

For each sample $x^{(i)}$, the model outputs a vector of probabilities for each class, calculated using the softmax function:
$$
\hat{y}^{(i)} = [P(y = 1 | x^{(i)}), P(y = 2 | x^{(i)}), \dots, P(y = C | x^{(i)})]
$$

The true label for each sample $y^{(i)}$ is encoded as a one-hot vector:
$$
y^{(i)} = [y_1^{(i)}, y_2^{(i)}, \dots, y_C^{(i)}]
$$
where $y_j^{(i)} = 1$ if $j$ is the true class, and $y_j^{(i)} = 0$ otherwise.

### 3. Using One-Hot Encoding in the Log-Likelihood Calculation

The softmax log-likelihood for each sample is the log of the probability assigned to the correct class. With one-hot encoding, we can express this directly in a compact, vectorized form.

The likelihood (or probability) for the true class is:
$$
P(y^{(i)} | x^{(i)}) = \prod_{j=1}^{C} (\hat{y}_j^{(i)})^{y_j^{(i)}}
$$
 In another term, the expression above can be rewrite as:
![[Pasted image 20241106074603.png]]

This simplifies to just the probability assigned to the true class, as discussed before:
$$
P(y^{(i)} | x^{(i)}) = \hat{y}_{y^{(i)}}
$$

The **log-likelihood** for this sample becomes:
$$
\log P(y^{(i)} | x^{(i)}) = \sum_{j=1}^{C} y_j^{(i)} \log \hat{y}_j^{(i)}
$$

### 4. Softmax Cross-Entropy Loss in Matrix Form

For an entire dataset of $N$ samples, the total **cross-entropy loss** (negative log-likelihood) across all samples is:

$$
L = -\frac{1}{N} \sum_{i=1}^{N} \sum_{j=1}^{C} y_j^{(i)} \log \hat{y}_j^{(i)}
$$

Thanks to one-hot encoding, only the probability of the correct class is considered for each sample. This summation can be efficiently implemented in matrix form as:

$$
L = -\frac{1}{N} \text{trace}(Y^\top \log(\hat{Y}))
$$

where:
- $Y$ is the $N \times C$ matrix of one-hot encoded true labels for all samples.
- $\hat{Y}$ is the $N \times C$ matrix of predicted probabilities for all classes for each sample.
- $\log(\hat{Y})$ applies the logarithm element-wise to each entry in $\hat{Y}$.

### Summary

One-hot encoding in the softmax log-likelihood:
- **Selects the correct class probability efficiently** through matrix multiplication.
- Allows us to **express the loss in a compact, vectorized form** that is highly efficient for computation.
- **Simplifies the computation** to focus only on the correct class probability, leaving the others out.

This encoding makes it computationally practical to implement softmax log-likelihood (or cross-entropy loss) efficiently, especially for large datasets with many classes.