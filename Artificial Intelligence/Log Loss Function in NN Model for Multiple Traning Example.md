
Logarithmic Loss, commonly known as Log Loss or Cross-Entropy Loss, i**s a crucial metric** in machine learning, particularly **in classification problems:**

It **quantifies the performance of a classification model** by **measuring the difference between probabilities and actual outcomes.**

The fomula of Log Loss:
$$\mathcal{L}\left(W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\right)  \frac{1}{m}\sum_{i=1}^{m} L\left(W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\right)$$$$= \frac{1}{m}\sum_{i=1}^{m}  \large\left(\small - y^{(i)}\log\left(a^{[2](i)}\right) - (1-y^{(i)})\log\left(1- a^{[2](i)}\right)  \large  \right), \small\tag{8}$$
Where:
+ m is the number of observation (variable)
+ $y^{(i)}$ is the actual binary outcome (0 or 1) for the i-th observation.
- $a^{[2][i]}$ is the predicted probability that the i-th observation belongs to class 2.
- The cost function $\mathcal{L}$ depends on the model parameters $W^{[1]}, b^{[1]}$, $W^{[2]}, b^{[2]}$ because $a^{[2](i)}$ is computed using these parameters.

### **2. Intuition Behind the Loss Function**

The loss function is designed to assign a **small loss** when the predicted probability aligns with the true label and a **large loss** when it doesn't. Here's the intuition:

- **When $y^{(i)} = 1$**:
    
    - We want $a^{[2](i)}$ to be close to 1.
    - The loss is $L = -\log\left(a^{[2](i)}\right)$.
        - If $a^{[2](i)}$ is close to 1, $\log\left(a^{[2](i)}\right)$ is close to 0, so the loss is small.
        - If $a^{[2](i)}$ is close to 0, $\log\left(a^{[2](i)}\right)$ is a large negative number, so the loss is large.
- **When $y^{(i)} = 0$**:
    
    - We want $a^{[2](i)}$ to be close to 0.
    - The loss is $L = -\log\left(1 - a^{[2](i)}\right)$.
        - If $a^{[2](i)}$ is close to 0, $1 - a^{[2](i)}$ is close to 1, so the loss is small.
        - If $a^{[2](i)}$ is close to 1, $1 - a^{[2](i)}$ is close to 0, so the loss is large.

To better understand how the loss changes with different predicted probabilities, let's consider plots of the loss functions.

#### **Loss When $y = 1$: $L = -\log(a)$**

- **X-axis**: Predicted probability $a$ (from 0 to 1)
- **Y-axis**: Loss $L$
- As $a$ approaches 1, the loss $L$ approaches 0.
- As $a$ approaches 0, the loss $L$ approaches infinity.

#### **Loss When $y = 0$: $L = -\log(1 - a)$**

- **X-axis**: Predicted probability $a$ (from 0 to 1)
- **Y-axis**: Loss $L$
- As $a$ approaches 0, the loss $L$ approaches 0.
- As $a$ approaches 1, the loss $L$ approaches infinity.