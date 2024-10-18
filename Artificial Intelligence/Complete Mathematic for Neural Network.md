#### Prerequites
Basic Linear Algebra
Multivariable Calculus
+ Differential
+ [[Jacobian Matrix]] / Gradients
Basic ML knowledge

---

NN's as functions
Just a bug calculus problem
all about minimizing the cost function

Chain Rule: what if there no intermediate function
![[Pasted image 20241017154312.png]]

# Part II: Forward Propagation
## 2.1 The Neuron Function

**Example with a single neuron**.
note: Inputs are dot product
![[Pasted image 20241017154540.png]]
$w_{i} x_{i}$ (w usually matrix, x usually vector) after dot product are scalar (i.e. also called inner product). b is scalar ![[Pasted image 20241017154704.png]]

**ReLU** (Rectifier Linear Unit) 
+ ? solves the "vanishing gradient problem" which makes it better than sigmoid.

#### 2.2 Weight and Bias Indexing
Explain how w and b are index with i
### 2.3 Layer of NN 
![[Pasted image 20241017155517.png]]
$w^{i}_{jk}$ where 
+ $i$ is the current layer.
+ $j$ is total node in layer $i$
+ k is node in layer before $i$: $i - 1$.
(explain how the notation work with example)
# PART III - Derivatives of Neural Networks and Gradient Descent
![[Pasted image 20241017160057.png]]
## 3.1 Motivation & Cost Function
Explain from a single node -> leading explain to matrix multiplication.
-> explain matrix (notation for row & column) -> example for a weight coordinate.
![[Pasted image 20241017160231.png]]
Example of matrix multiplication in single layer NN
![[Pasted image 20241017160424.png]]
multiplication result
![[Pasted image 20241017160609.png]]
then the activtion function for each result (sigmoid or ReLU is fine)
![[Pasted image 20241017160527.png]]
**Explain Feeding Forward**


## 3.2 Differentiating a Neuron's Operations
**Jacobians and NN's**
-> simple model
-> MSE
-> calc derivatives
-> calc gradient descent

### 3.2.1 Derivative of a Binary Elementwise Function
-> Binary element-wise Operations
-> Hadamard product
-> Sum

Explain Jacobian -> Example -> Using Jacobian Matrix to Describe the broad ideas
![[Pasted image 20241017161728.png]]

### 3.2.2 Derivative of a Hadamard Product



### 3.2.3 Derivative of a Scalar Expansion



### 3.2.4 Derivative of a Sum



## 3.3 Derivative of a Neuron's Activation



## 3.4 Derivative of the Cost for a Simple Network (w.r.t weights)


## 3.5 Understanding the Derivative of the Cost (w.r.t weights)


## 3.6 Differentiating w.r.t the Bias


## 3.7 Gradient Descent Intuition


## 3.8 Gradient Descent Algorithm and SGD


## 3.9 Finding Derivatives of an Entire Layer (and why it doesn't work well)

