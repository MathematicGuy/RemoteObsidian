# Intro

**NN**
	Inference - download and use other NN for prediction 
	Training - train NN yourself
**Practical Advice** - how to build system efficiency and effectively.
**Decision Trees**
	powerful algorithms commonly uses.

---

# Neural Network Intuition

## Neurons and the brain
**origin:** algo that try to mimic the brain
	Used in the 1980's and early 1990's.
	Fell out of favor in the late 1990's.
**Resurgence** from around 2005.

**Human Neuron**: take inputs and output signal, the signal get transfer to other neurons as input.
![[Pasted image 20241022143338.png]]

Why NN -> obtain NN performance as data growed.
![[Pasted image 20241022143935.png]]

## Demand Prediction
>Example of Neuron for demand prediction problem. Take input into activation function and output whether a shirt is a top seller.
![[Pasted image 20241022144203.png]]

# Neural Network Model
![[Pasted image 20241022151932.png]]
>output
![[Pasted image 20241022152027.png]]

**Notation**
![[Pasted image 20241022145237.png]]
**Where**
+ ? $[\space l \space]$ : as the $l$-th neuron layer.
	
+ ? $j$ : as the j-th node of $l$-th layer.
	
+ ? $a^{[l -1]}$: activation function of the previous layer.
	
+ ? $a^{[l]}_{j} = g(\vec{w}^{[l]}_{j} . \vec{a}^{[l -1]} + b^{[l]}_{j})$: as node $j$-th of the $l$-th layer is the result of activation function g which take $j$-th weight of the current layer multiply with the previous layers activation value $\vec{a}^{[l-1]}$ addition with bias of the curernt layer.


#### Handwritten Digit Recognition
![[Pasted image 20241022152345.png]]

![[Pasted image 20241022152411.png]]

## TensorFlow implementation
**Goal:** build a coffee roasting classification in tensorflow.
![[Pasted image 20241022152635.png]]
> Point within the triangle are roasted coffee.

note: Dense is a layer in NN
![[Pasted image 20241022152806.png]]

**Example of Carrying out inference in tensorflow** (previous output as input)
![[Pasted image 20241022152901.png]]

### Data in TensorFlow

+ ? Why double squared bracket ?
![[Pasted image 20241022153019.png]]

2 by 3 Matrix. Dimension of matrix is notate in row by column.
![[Pasted image 20241022153051.png]]
> A Matrix is just a 2D array of numbers.
![[Pasted image 20241022153224.png]]

**Activation Vector**
>**a tensor represent a matrix**
![[Pasted image 20241022153342.png]]
+ Pass numpy into tensor flow, it got turned into tensor format.

### Building a Neural Network
![[Pasted image 20241022154205.png]]
predict -> carried out the inference

**Other way to code NN**
![[Pasted image 20241022154250.png]]

## Neural network implemenation in Python
### Forward prop in a single layer
![[Pasted image 20241024092128.png]]

### General implementation of forward propagation
![[Pasted image 20241024093734.png]]

## AI 
**ANI (artificial narrow intelligence)** E.g. smart speker, self-driving car, web search, etc..
**AGI (artificial general intelligent)** Do anything a human can do.

Hope for AGI, well the "one learning algorithm" hypothesis show that human brain cortex can learn and adapt to whatever information given to it, for example **rewrite Somatosensory Cortex (i.e. touch processing) to feed in images, it learn to see.**
![[Pasted image 20241024093346.png]]

**Real Life Example**
![[Pasted image 20241024093514.png]]

## Vectorization
### How neural networks are implemented efficiently
+ ? `np.matmul` allow fast matrix multiplication in parallel.
![[Pasted image 20241024094233.png]]

### Recognize 2 Handwritten Digits
(Binary Classification Task)

**NN Model**
![[Pasted image 20241024101248.png]]
![[Pasted image 20241024101242.png]]

$$Parameters=(\text{input units} \times \text{output units})+\text{output units}$$
Example Calculation 
1. **First Dense Layer:**

- **Input size**: 400 (specified by `Input(shape=(400,))`)
- **Output size**: 25 (the number of units in the first `Dense` layer)

**The number of parameters is:** $(400 \times 25) + 25 = 10,000 + 25 = 10,025$
