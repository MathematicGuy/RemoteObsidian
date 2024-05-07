# Determinants In-depth (định thức hiểu sâu)

## Singularity and rank of linear transformations
The image is Singular. it not covering the whole plane on the right, just a portion of it (**singular: matrix -> a line, a point**)
![[Pasted image 20240420230556.png]]

## example: what T(0,1)=(2,5) T(1,0)=(3,1) mean ?
$$
\begin{bmatrix} 1 & 0\\ 2 & 3 \end{bmatrix} 
\times
\begin{bmatrix} 0\\ 1 \end{bmatrix} 
= \begin{bmatrix} 0\\ 3 \end{bmatrix} 
$$
And
$$
\begin{bmatrix} 1 & 0\\ 2 & 3 \end{bmatrix} 
\times
\begin{bmatrix} 1\\ 0 \end{bmatrix} 
= \begin{bmatrix} 1\\ 2 \end{bmatrix} 
$$
So, (0,1)→(0,3)(0,1)→(0,3) and (1,0)→(1,2)(1,0)→(1,2).

The rank of the matrix mean it Dimension.
![[Pasted image 20240420230926.png]]

Determinant
![[Pasted image 20240420231813.png]]
![[Pasted image 20240420231946.png]]
What if the determinant is negative
![[Pasted image 20240420232451.png]]
Depending on what order we take 2 basis vectors as follows.
![[Pasted image 20240420232158.png]]
 
+ ? Negative value doesn't affect the singuality of the matrix. The only that affect is when the determinant is 0.
![[Pasted image 20240420232314.png]]

**Determinant** of a  product
it like multiplication for matrices. It blow up the area of a matrix.
![[Pasted image 20240421000026.png]]
> To transform the first matrix instantly we multiply by the product of its Det (matrice of det=5 * matrix of det=3)


Matrix A: 
	[2 3] 
	[4 1]	
Matrix B:
	[5 6] 
	[2 3]
A * B =   [2.5 + 3.2, 2.6 + 3.3]
		[4.5 + 1.2, 4.6 + 1.3]
result =  [16, 21]
		[22, 27]

Singular matrix  * any matrix -> singular matrix. Why?
![[Pasted image 20240421001559.png]]
![[Pasted image 20240421001334.png]]
If a matrix is singular. whatever area you have left, it gets blown up by zero.
![[Pasted image 20240421002440.png]]

# Determinant of Inverse
![[Pasted image 20240421002741.png]]
> zero has no Inverse

+ ? Why is the determinant of the identity matrix 1?
![[Pasted image 20240421002905.png]]
$$
det(AA^{-1}) = IdentityMatrix = det(A)det(A^{-1}) = 1
$$

+ ? (Identity matrix always equal 1) 
$$
det(A) = 1 / det(A^{-1})
$$
**Bases in Linear Algebra****
**2point form a vector, 2 vector form a bases

**Span in Linear Algebra** -> created by 2 lines
![[Pasted image 20240506222628.png]]
so they're linearly dependent
![[Pasted image 20240506222705.png]]

Eigenbasis