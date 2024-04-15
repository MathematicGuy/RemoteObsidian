note: 


In this Assignment, we explores the **Foundational concepts of linear transformations and neural networks in two distinct parts**
1) ?  Linear Transformation -> Create func to generate matrices for Stretching, Shearing and Rotation Operations.
2) ? Neural Network -> implementing forward propagation in a simple architecture with two inputs and one perceptron
+ $ **Goal:** By dissecting these fundamental components, this assignment aims to provide a clear understanding of the **role of linear algebra in both vector transformations and neural network computations.**

+ 𝑇 : ℝ2→ℝ3. Transforming vector 𝑣∈ℝ2 into the vector 𝑤∈ℝ3
+ 𝑇(𝑣) = 𝑤 and read it as "_T of v equals to w_" or "_vector w is an **image** of vector v with the transformation T_".


### 1.2 - Linear Transformations
+ 𝑇(𝑘𝑣)=𝑘𝑇(𝑣),
- 𝑇(𝑢+𝑣)=𝑇(𝑢)+𝑇(𝑣)
![[Pasted image 20240415102233.png]]

```python
u = np.array([[1], [-2]])
v = np.array([[2], [4]])

k = 7
# Linear transformation
print("T(k*v):\n", T(k*v), "\n k*T(v):\n", k*T(v), "\n\n")
print("T(u+v):\n", T(u+v), "\n\n T(u)+T(v):\n", T(u)+T(v))
```
