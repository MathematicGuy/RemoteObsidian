### Eigenbases (the original vector)
> An **eigenbasis** is a basis for a vector space that consists entirely of eigenvectors of a linear operator (or matrix).
>The **vector after transformation** (notate in orange)
![[Pasted image 20240619134603.png]]
> **Change of Basis**
+ Using [[Matrix Multiplication]] we have (2, 0) for (1, 0) and (1, 3) for (0,1)

> Let's say that you want to find the image of the point 3, 2. You can multiply it by the matrix and get 8, 6
![[Pasted image 20240619140935.png]]

### What is Eigenvalue and Eigenvectors ?
- **Eigenvalues** ($\lambda$): Scalars that, when multiplied by a given eigenvector, yield the same result as applying a given linear transformation (or matrix) to that eigenvector. (vector tỷ lệ. ma trận trở nên to hay bé dựa vào việc nhân vs eigenvalues) (**magnitude**)
	
- **Eigenvectors** ($\mathbf{v}$): Non-zero vectors that change at most by a scalar factor when a linear transformation is applied to them. (Vector điều hướng) (**direction**)
	![[Pasted image 20240619142851.png]]
	After mutiply the 
	+ first matrix with the eigenvector, we get (2.1 + 1.0) and (0.1 + 3.0) == (2, 0) or 2 * (1, 0)
		$\lambda = 2$
		$\mathbf{v} = (1, 0)$
	+ with second matrix, we get: (2.1 + 1.1) and (0.1 + 3.1) == (3, 3) or 3 * (1, 1)
		$\lambda = 3$
		$\mathbf{v} = (1, 1)$
	+ for the third, we get (2.-1 + 1.2) and (0.-1 + 3.2) == (0, 6). We don't have $\lambda$ because the vector don't transform in the same direction.
	
+ From 2 Example above know that Matrix A * Eigenvectors (v1) = Eigenvalue (of A) * Eigenvector (v1)
	![[Pasted image 20240619143810.png]]
+ **This work show that we can optimize Matrix Multiplication using eigenvalue and eigenvectors.** (eigenvalue and eigenvectors goes in pair)  
	![[Pasted image 20240619144135.png]]
+ $ With that in mind, let apply eigenbasis to find the eigenvalues and eigenvectors of others vector that don't have their own eigenbasis.  
	(dùng vector gốc có rồi để chuyển các vector ko có vector gốc về dạng Eigenvectors * Eigenvalue. Từ đó, ta có thể tối ưu tốc độ tính toán của 1 ma trận)

+ ? Since the vectors 1, 0 and 1, 1 form a basis, so we can use it to calc the eigenvalues and eigenvectors of others matrix in the same plant. (eigenbasis đơn giản là dùng 1 số vector làm cột mốc để tính các vector khác) -? but how?
+ In ours case we can **transform 2 eigenvectors (the 1st and 2nd)** with eigenvalue of -3 on the x-axis and 2 on the y-axis **to get the eigenvectors of the 3rd matrix**. 
	![[Pasted image 20240619144408.png]]
	Now re-arrange it slightly
	![[Pasted image 20240619144531.png]]
	We can easily get the eigenvalue and eigen vector as -6, (1, 0) + 6, (1, 0) for the 3rd matrix 
	![[Pasted image 20240619145302.png]]
	+ ! However, it more complicated than that. Learn it later
		![[Pasted image 20240619151558.png]]

```ad-summary
+ **AV = Av** for each eigenvector / eigenvalue

+ **Eigenvectors**: direction of stretch

+ **Eigenvalues**: how much stretch

+ **Eigenbasis**: the set of a matrix's eigenvectors, can be arranged as a matrix with one eigenvector in each column

+ Save work and offer optimization for matrix transformation
```

## How to calculate Eigenvalue and Eigenvectors
![[Pasted image 20240619171845.png]]

$$
A = \begin{pmatrix} 9 & 4 \\ 4 & 3 \end{pmatrix} 
$$
### Step-by-Step Solution

#### 1. **Recall the Eigenvalues**
>From the given information, the eigenvalues are $(\lambda_1 = 11)$ and $(\lambda_2 = 1)$

#### 2. **Find Eigenvectors**
>For each eigenvalue \(\lambda\), solve the equation:
>$(A - \lambda I)v = 0$

##### Eigenvector for ($\lambda_1 = 11$):

1. Form $A - 11I$:
$A - 11I = \begin{pmatrix} 9 & 4 \\ 4 & 3 \end{pmatrix} - 11 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 9-11 & 4 \\ 4 & 3-11 \end{pmatrix} = \begin{pmatrix} -2 & 4 \\ 4 & -8 \end{pmatrix}$

2. Solve $$(A - 11I) \mathbf{v} = 0$$
$$\begin{pmatrix} -2 & 4 \\ 4 & -8 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

This system of linear equations can be reduced to:
$$ 
\begin{aligned}
-2v_1 + 4v_2 = 0 \\
4v_1 - 8v_2 = 0 
\end{aligned}
$$

Both equations are equivalent, so we can take:
$$
\begin{aligned}
-2v_1 + 4v_{2} = 0 \\
v_2 = \frac{v_1}{2}
\end{aligned}
$$


Therefore, one eigenvector for $\lambda_1 = 11$ is:
$$
\mathbf{v}_1 = \begin{pmatrix} 1 \\ \frac{1}{2} \end{pmatrix} 
$$


Or more conveniently, any scalar multiple of this vector, such as:
$$
\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix} 
$$

##### Eigenvector for $(\lambda_2 = 1)$:

1. Form $(A - I)$:
$$
A - I = \begin{pmatrix} 9 & 4 \\ 4 & 3 \end{pmatrix} - 1 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 9-1 & 4 \\ 4 & 3-1 \end{pmatrix} = \begin{pmatrix} 8 & 4 \\ 4 & 2 \end{pmatrix} 
$$

2. Solve $(A - I) \mathbf{v} = 0$:
$$
\begin{pmatrix} 8 & 4 \\ 4 & 2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} 
$$

This system of linear equations can be reduced to:
$$ 
\begin{aligned}
8v_1 + 4v_2 = 0 \\
4v_1 + 2v_2 = 0 
\end{aligned}
$$


Both equations are equivalent, so we can take:
$$
\begin{aligned}
8v_1 + 4v_2 = 0 \\
v_2 = -2v_1 
\end{aligned}
$$


Therefore, one eigenvector for $(\lambda_2 = 1)$ is:
$$\mathbf{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$$

### Summary

- Eigenvalue $(\lambda_1 = 11)$ has the corresponding eigenvector $\mathbf{v}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
- Eigenvalue $(\lambda_2 = 1)$ has the corresponding eigenvector $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$.

These eigenvectors form the eigenbasis for the matrix $A$.

## How to Find Eigenvectors if Matrix have Repeated Eigenvalue
We have 3 eigenvalues: 4, 2, 2
With the 2 we have:
![[Pasted image 20240702194053.png]]
-> Infinitely solution
> Try and we have
	![[Pasted image 20240702194247.png]]

Do the same for the last eigenvalues 4, we have
![[Pasted image 20240702194401.png]]
### Let change 1 value in the matrix (in the 3rd row)
![[Pasted image 20240702194512.png]]

![[Pasted image 20240702194552.png]]
We see that x3 = 4x2, therefor the eigenvector is (v1, v2, v3) = (0, k, 4k)
![[Pasted image 20240702195111.png]]
+ When 2 lambda equal to eachother that mean they can be identical and resulting in 1 eigenvector. More specific, numbers of eigenvectors is depend on that 1 eigenvalue.

