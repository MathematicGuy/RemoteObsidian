# 1. The Primitive Form of the Logarithm Function
## What is a Logarithm?
A logarithm is a mathematical function that answers the question: **"To what [[exponent]] must we raise to a specific [[base]] to obtain a given number"**

+ **Definition:** For positive real numbers a, b and c where $b \neq 1$ 
$$If \space b^{c} = a, \space then \space \log_{b}(a) = c$$
This read as the **"logarithm base b power c is a"** 

### **Properties of Logarithms**

Understanding the properties of logarithms is crucial because they simplify complex mathematical expressions, especially when dealing with multiplication and exponentiation.

1. **Product Rule**:
   $$
   \log_b(MN) = \log_b(M) + \log_b(N)
   $$
   *The log of a product is the sum of the logs.*

2. **Quotient Rule**:
   $$
   \log_b\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)
   $$
   *The log of a quotient is the difference of the logs.*

3. **Power Rule**:
   $$
   \log_b(M^k) = k \cdot \log_b(M)
   $$
   *The log of a number raised to a power is the power times the log of the number.*

4. **Change of Base Formula**:
   $$
   \log_b(a) = \frac{\log_c(a)}{\log_c(b)}
   $$
   *Allows conversion of logarithms from one base to another.*

**Conversion using Logarithm Example** 
$\log_b(MN) = \log_b(M) + \log_b(N)$
$\log_b(M^k) = k \cdot \log_b(M)$

$p^{8}(1-p)^2$ 
$\log(p^{8}(1-p)^{2)}$ (Since $2^{3}=8$ )
**Apply Product Rule**:
$\log(p^8) + \log((1-p)^2)$
**Apply Power Rule**
$8\log(p) + 2\log(1-p)$

### [[Natural Logarithm]]
> $e^x$ **represent continuous growth and change**
> Số mũ tự nhiên $e = \left( 1 + \frac{1}{n} \right)^{n}, \space n \to \infty$   (Tốc độ tăng trưởng tối đa của lãi suất sau vô tận ngày)
> ![[Pasted image 20241018120257.png]]

- **Base \( e \)**: The natural logarithm uses the irrational constant \( e \approx 2.71828 \) as its base.
- **Notation**: The natural logarithm of \( x \) is written as \( \ln(x) \).
- **Definition**:
  $$
  \ln(x) = \log_e(x)
  $$
+ ? Example:
	+ $\ln(4)=x \iff e^x=4 \implies x \approx 1.386$
	+ $\ln(4) = \log_{e}(4)$ 
The natural logarithm is widely used in calculus and exponential growth models due to its unique mathematical properties.

## $\log_{10}(x)$ vs $\ln(x)$
> Have the same properties. Just use in different occasion.
#### $\log_{10}(x)$
> $\log()$ is often **used in contexts where quantities are measured on a scale** that spans several orders of magnitude. Some examples include:
![[Pasted image 20241018150959.png]]
+ ? Often use with Decimal or Powers of 10 since log() refers to base 10.
+ $ Used in fields like engineering, sound measurement (decibels), chemistry (pH), and geology (Richter scale).

### $\ln(x)$
>The natural logarithm $\ln()$ is frequently used when dealing with **continuous growth** or **decay processes**. These process are often modeled with the base $e$ because of **its natural connection to rates of change**, such as the following contexts:
![[Pasted image 20241018150950.png]]
+ ? $\ln()$ is more common in pure mathematics particularly in calculus and integration, since it can be use to represent continous value and because $e$ has **unique properties related to differentiation and integration.**
	For example, the derivative of $e^x$ is $e^x$, and the derivative of $\ln(x)$ is $\frac{1}{x}$, making $\ln$ very **useful for continous scenarios.**

 **Logistic and Exponential Regression Models**
 > models such as logistic regression in machine learning, which models binray outcomes: 
 > $$\ln\left( \frac{p}{1-p}\right) = \beta_{0} + \beta_{1}x_{1} + \beta_{1}x_{1} + \dots + \beta_{n}x_{n}$$
 > The natural logarithm is also used in **maximum likelihood estimation** (MLE), which involves maximizing the log-likelihood function.
	
**Probability Distributions**:
>In statistics, many probability distributions, such as the **normal distribution** or the **Poisson distribution**, involve the natural logarithm due to the exponential nature of their formulations.

### Example of Conversion Between $\log()$ and $\ln()$
Using the **change of base formula**, you can convert between different logarithmic bases:
$$\log_b(x) = \frac{\ln(x)}{\ln(b)}$$
For example, converting $\log (x)$ to $\ln(x)$:
$$\log(x) = \frac{ln(x)}{\ln(10)}$$
This formula can be useful when you need to switch between $\log()$ and $\ln()$ in a given context.

```ad-summary
+ Use $\log()$ when working with base 10 scales (e.g., in fields like engineering, chemistry, or geophysics).
+ **Used $\ln()$ in modeling natural processes like population growth, decay, or continuous compounding**.
```


# Likelihood Function

**Probability:** Assume how likely sth to happend (i.e. prob without tested)
+ $ Suppose you have an **unbiased** coin. If you flip the coin, the probability of getting head and a tail is equal, which is 0.5. 
+ ? **When calculating the probability of coin getting heads, you assume that P(head) = 0.5**

**Likelihood:** Calc the probability sth actually happened (i.e. prob after tested)
+ $ However, when calculating the likelihood, you are **trying to find if the model parameter (p = 0.5) is correctly specified or not.**
+ ? The **fact that a coin only lands on heads 14 times out of 50 makes you highly suspicious that the true probability of a coin landing on heads on a given toss is p = 0.5.**

Here is the updated version with the `$` formatting applied:

---
### **Likelihood vs. Probability**

- **Probability**: Refers to the likelihood of future events given known parameters.
  - Example: $P(X = x | \theta)$ — "Given $\theta$, what is the probability of observing $x$?"
- **Likelihood**: Considers the data as fixed and assesses how plausible different parameter values are.
  - Example: $L(\theta | x)$ — "Given observed data $x$, how likely is parameter $\theta$?"

### **Example of a Likelihood Function**

**Coin Toss Experiment**:

- **Scenario**: Toss a coin $n$ times; let $k$ be the number of heads observed.
- **Goal**: Estimate the probability $p$ of getting heads.
- **Likelihood Function**:
  $$
  L(p | \text{data}) = P(\text{data} | p) = \binom{n}{k} p^k (1 - p)^{n - k}
  $$
$\left(\text{Likelihood of an Event} = \text{Event Success Possibility} * \text{Event Fail Possiblility} \right)$

  - $\binom{n}{k}$ is the binomial coefficient (number of ways to choose $k$ successes in $n$ trials).
  - $p^k$ is the probability of getting heads $k$ times. 
  - $(1 - p)^{n - k}$ is the probability of getting tails $n - k$ times.

This function tells us how likely different values of $p$ are, given our observed data.

---

## **3. Leading Up to the Log-Likelihood Function**
### **Why Use the Log-Likelihood?**

The likelihood function often involves products of probabilities, which can be cumbersome for computation and differentiation, especially with large datasets. **Taking the logarithm of the likelihood function simplifies these operations due to the properties of logarithms.**

### **Definition of the Log-Likelihood Function**

- **Log-Likelihood Function**:
  $$
  \ell(\theta) = \ln L(\theta | x)
  $$
- **Purpose**: Transforms the product of probabilities into a sum, making mathematical operations more manageable.

### **Advantages of Using the Log-Likelihood**

1. **Simplification of Products to Sums**:
   - Multiplicative terms become additive, which is easier for calculus operations like differentiation.
   - Example:
     $$
     \ln\left(\prod_{i=1}^{n} p_i\right) = \sum_{i=1}^{n} \ln(p_i)
     $$

+ ? Use **Logarithm** to **transform products into sums** help differentiation easier. This help finding the likelihood of $p_i$.

2. **Numerical Stability**:
   - Logarithms can prevent underflow issues when dealing with very small probabilities (common in large datasets).

3. **Facilitates Optimization**:
   - Maximizing the log-likelihood is equivalent to maximizing the likelihood, as the natural log function is monotonically increasing.
	
   - Derivatives of the log-likelihood function are easier to compute, which is essential for finding parameter estimates.

### **Example: Log-Likelihood in the Coin Toss**

Using the earlier coin toss example:

- **Likelihood Function**:
  $$
  L(p) = \binom{n}{k} p^k (1 - p)^{n - k}
  $$
- **Log-Likelihood Function**:
  $$
  \ell(p) = \ln L(p) = \ln \binom{n}{k} + k \ln p + (n - k) \ln (1 - p)
  $$
  - $\ln \binom{n}{k}$ is constant with respect to $p$ and can be ignored during optimization.
  - The log-likelihood simplifies the process of finding the $p$ that maximizes $L(p)$.

### **Connection to Maximum Likelihood Estimation (MLE)**

- **Goal of MLE**: Find the parameter $\theta$ that maximizes the likelihood function $L(\theta | x)$.
- **Using Log-Likelihood**:
  - Since $\ell(\theta)$ is easier to work with, MLE often involves maximizing $\ell(\theta)$ instead.
  - The parameter $\theta$ that maximizes $\ell(\theta)$ also maximizes $L(\theta | x)$.

---

## **4. Applying Log-Likelihood to Logistic Regression**

### **Logistic Regression Overview**

- **Purpose**: Model the probability that a binary outcome variable $y_i$ equals 1, given predictor variables $x_i$.
- **Sigmoid Function**:
  $$
  \hat{y}_i = \sigma(z_i) = \frac{1}{1 + e^{-z_i}}
  $$
  - $z_i = \theta^T x_i$ is the linear combination of input features and parameters.

### **Likelihood Function in Logistic Regression**

- **For Independent Observations**:
  $$
  L(\theta) = \prod_{i=1}^{n} P(y_i | x_i; \theta)
  $$
- **Individual Probability**:
  $$
  P(y_i | x_i; \theta) = \hat{y}_i^{y_i} (1 - \hat{y}_i)^{1 - y_i}
  $$
  - When $y_i = 1$, the probability is $\hat{y}_i$.
  - When $y_i = 0$, the probability is $1 - \hat{y}_i$.

### **Log-Likelihood Function in Logistic Regression**

- **Log-Likelihood Function**:
  $$
  \ell(\theta) = \sum_{i=1}^{n} \left[ y_i \ln \hat{y}_i + (1 - y_i) \ln (1 - \hat{y}_i) \right]
  $$
- **Objective**: Maximize $\ell(\theta)$ with respect to $\theta$ to find the best-fitting model parameters.

### **Interpreting the Log-Likelihood Function**

- **Convex Optimization**: The log-likelihood function in logistic regression is concave (negative of a convex function), which means it has a single global maximum.
	
- **Gradient Ascent**: Optimization algorithms can efficiently find the maximum log-likelihood parameters.
	
- **Connection to Cost Function**: In practice, we often minimize the **negative log-likelihood**, which serves as the cost function in logistic regression:  

$$
  J(\theta) = -\ell(\theta)
$$
---
## **Summary**

- **Logarithm Function**: Simplifies multiplication into addition, essential for handling products of probabilities.
- **Likelihood Function**: Measures the plausibility of parameters given observed data, fundamental in statistical inference.
- **Log-Likelihood Function**: The natural logarithm of the likelihood function; simplifies optimization and improves numerical stability.
- **Application in Logistic Regression**: The log-likelihood function is central to estimating the parameters that best fit the data by maximizing the likelihood of observing the given outcomes.

---

**Understanding the primitive forms of the logarithm and likelihood functions provides a solid foundation for comprehending the log-likelihood function. This knowledge is crucial in statistical modeling and machine learning algorithms, such as logistic regression, where maximizing the log-likelihood function leads to the most probable model parameters given the observed data.**
