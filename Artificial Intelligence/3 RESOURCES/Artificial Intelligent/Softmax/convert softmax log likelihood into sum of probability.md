To understand where the softmax regression loss function originates from mathematically, let's dive into its foundation, which is rooted in probability theory and maximum likelihood estimation. 

Here's how we build up to the softmax regression loss function step-by-step:

### 1. The Goal: Predicting the Probability of Each Class

For multiclass classification, we aim to model the probability that a given input $x$ belongs to one of $k$ classes. Let’s denote this probability for class $i$ as $P(y = i | x)$, which means “the probability that the class label $y$ is $i$, given the input $x$.”

To calculate these probabilities, we use a model that assigns a **score** $z_i$ to each class $i$ based on the input $x$, where:

$$
z_i = w_i \cdot x + b_i
$$

where:
- $w_i$ and $b_i$ are the weights and bias for class $i$.
- $z_i$ is the "logit" or raw score for class $i$.

### 2. Converting Scores to Probabilities: The Softmax Function

These raw scores $z_i$ are not probabilities yet—they can be any real numbers, positive or negative. To interpret these scores as probabilities, we need a transformation that:
1. Maps each score to a range between 0 and 1.
2. Ensures that the probabilities for all classes sum to 1.

The **softmax function** is designed for this purpose. Given the set of scores $\{ z_1, z_2, \ldots, z_k \}$, the softmax function for class $i$ is defined as:

$$
P(y = i | x) = \frac{e^{z_i}}{\sum_{j=1}^k e^{z_j}}
$$

This formula takes the exponential of each score (ensuring it’s positive) and divides by the sum of exponentials of all scores, which normalizes them to sum to 1. Now, $P(y = i | x)$ is the probability assigned by the model to class $i$ for input $x$.

### 3. Maximum Likelihood Estimation (MLE)

To train the model, we need a way to measure how well it predicts the correct classes. This is where **maximum likelihood estimation** (MLE) comes in. MLE is a method that finds the parameters of a model that maximize the probability of the observed data.

For each training example $(x, y)$:
- $x$ is the input.
- $y$ is the true label, where $y$ can take on one of $k$ possible values (e.g., $y = 1, 2, \dots, k$).

If our model’s prediction for the probability of class $y$ given $x$ is $P(y | x)$, then the likelihood $\mathcal{L}$ of the model given the data point $(x, y)$ is simply:

$$
\mathcal{L} = P(y | x)
$$

For a set of $N$ training samples, the total likelihood $\mathcal{L}_{\text{total}}$ is the product of the individual probabilities:

$$
\mathcal{L}_{\text{total}} = \prod_{n=1}^{N} P(y^{(n)} | x^{(n)})
$$

To simplify computations, we often take the **logarithm of the likelihood**, converting it to a sum rather than a product. This is called the **log-likelihood**:

$$
\log \mathcal{L}_{\text{total}} = \sum_{n=1}^{N} \log P(y^{(n)} | x^{(n)})
$$

Our goal is to maximize this log-likelihood with respect to the model parameters $w_i$ and $b_i$.

### 4. Deriving the Cross-Entropy Loss

Now let’s translate this maximum log-likelihood objective into the softmax regression loss function.

For each training example $(x, y)$:
1. The probability assigned to the true class $y$ is $P(y | x) = \frac{e^{z_y}}{\sum_{j=1}^k e^{z_j}}$.
2. So the log-likelihood for a single example is:

   $$
   \log P(y | x) = \log \left( \frac{e^{z_y}}{\sum_{j=1}^k e^{z_j}} \right) = z_y - \log \left( \sum_{j=1}^k e^{z_j} \right)
   $$

3. To maximize this, we can equivalently minimize the **negative log-likelihood** (since maximizing a function is the same as minimizing its negative). This negative log-likelihood for a single example is:

   $$
   -\log P(y | x) = -z_y + \log \left( \sum_{j=1}^k e^{z_j} \right)
   $$

4. Extending this to the entire dataset, the total loss function (also known as the **categorical cross-entropy loss**) is the average negative log-likelihood over all $N$ examples:

   $$
   L = -\frac{1}{N} \sum_{n=1}^{N} \left( z_{y^{(n)}}^{(n)} - \log \left( \sum_{j=1}^k e^{z_j^{(n)}} \right) \right)
   $$

This is the **softmax regression loss function**. For each sample:
- $z_{y^{(n)}}^{(n)}$ is the score of the correct class.
- $\log \left( \sum_{j=1}^k e^{z_j^{(n)}} \right)$ represents the log of the total "evidence" (sum of exponentials of all class scores).

### Why This Loss Function Works
This loss function is designed to penalize the model based on how far it deviates from predicting the correct class:
- If the model assigns a high probability to the true class (high $z_y$ relative to other scores), the loss is low.
- If the model assigns low probability to the true class (low $z_y$ relative to others), the loss is high.

This mathematical formulation encourages the model to increase the score of the true class while keeping the scores of other classes lower, effectively pushing the probability of the correct class closer to 1.

### Summary

1. **Softmax function**: Converts raw class scores into probabilities that sum to 1.
2. **Negative log-likelihood**: By minimizing the negative log-likelihood, we find parameters that maximize the probability of the correct class for each input.
3. **Categorical cross-entropy loss**: This is the average negative log-likelihood, which serves as the loss function for softmax regression.

This loss function arises naturally from trying to maximize the probability of the observed data under the softmax model. It’s an elegant result of applying maximum likelihood estimation to a multinomial probability distribution.