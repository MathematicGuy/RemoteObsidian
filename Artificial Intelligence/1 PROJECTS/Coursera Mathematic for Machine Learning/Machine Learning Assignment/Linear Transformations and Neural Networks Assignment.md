revision note: 
practice numpy
+ how to create a 4x4 matrix
+ code a matrix muls and transformation



---

# Visual Overview
Purpose for learning this: **Understand Math for Debugging**
![[Pasted image 20240416060714.png]]

Matrix Multiplycation 
![[Pasted image 20240416060912.png]]

 The change of x -> change of the output![[Pasted image 20240416061048.png]]
**Linear Transformation**
row x column

matrix x matrix
![[Pasted image 20240416061723.png]]

Each time the state rotate we'll need to mul to a Matrix (called Transformer)
![[Pasted image 20240416061949.png]]
Each matrix transform (rotate) the point to a different location and therefor
**Transformation Multiplycation can get the Point Final Coordinates at any given time** so we don't have to re-multiply all the previous step. This mean I can use the Transformer at the last step to transform a point to that position.
![[Pasted image 20240416061923.png]]

+ ! Order matter. Bc row x column, the second one only have 1 column -. the 1st diff from the 2nd matrice.
![[Pasted image 20240416062351.png]]
+ $ To work it out,  we need to **turn row in to corresponding column** using **Matrix Transpose**
	![[Pasted image 20240416062524.png]]
+ ! The example above **transform Matrix Row into Column** **Changing the rows in a matrix into corresponding columns** is called **Transposing** a matrix (the same for Col to Row)
	![[Pasted image 20240416062714.png]]
	Transpose mean turn Matrix Row to Column

Transpose Matrix will be signal with a T above the variable head.
![[Pasted image 20240416063034.png]]

![[Pasted image 20240416063728.png]]

![[Pasted image 20240416083854.png]]

	

In this Assignment, we explores the **Foundational concepts of linear transformations and neural networks in two distinct parts**
1) ?  Linear Transformation -> Create func to generate matrices for Stretching, Shearing and Rotation Operations.
2) ? Neural Network -> implementing forward propagation in a simple architecture with two inputs and one perceptron
+ $ **Goal:** By dissecting these fundamental components, this assignment aims to provide a clear understandingw of the **role of linear algebra in both vector transformations and neural network computations.**

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


# Notes 

Third Assignment include 2 distrinct part
+ **Foundational concepts of linear transformations** 
	Delve into linear transformations by creating functions to generate matrices for stretching, shearing, and rotation operations.
+ **Neural network**
	Specifically implementing forward propagation in a simple architecture with two inputs and one perceptron.

1) Transformations
	ℝ2→ℝ3 (R present Dimension)
	 Transform vector from R2 to R3.


![[Pasted image 20240627165808.png]]