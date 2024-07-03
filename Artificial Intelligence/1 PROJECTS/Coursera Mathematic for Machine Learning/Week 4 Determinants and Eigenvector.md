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

**Determinant** of a product
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

## Dimensionality Reduction and projection
> Purpose of Dimension Reduction
![[Pasted image 20240702201935.png]]

Easy approach - just delete cols but loses valuable information
**The idea behind dimensionality reduction is to move your data points into a vector space with fewer dimensions.**
![[Pasted image 20240702202537.png]]
Project (1, 1) we have the vector at the value of 1. However, summing the 2 variable (coordinate 1, 1) you ending up with a vector length of 2. 
+ To get the length we divided it by the square root of 2. Which is the norm of 1. (căn(1 + 1) = căn 2)

![[Pasted image 20240702202314.png]]
![[Pasted image 20240702203330.png]]
**Summary:**
+ Align the vector by the Coordinates. 
+ Scale it down to the original lenth bz dividing it to the norm of 1 (căn bậc 2 ) - The norm is taken from the first coordinate. Which come from the original line. If the line rotate down 45/2 degree (45 -> 22.5 degree) , we would have the norm as căn (0.5 + 1) = căn(1.5)


![[Pasted image 20240702203417.png]]
We can projecting on multiple vectors at one
![[Pasted image 20240702203715.png]]
In the End, the projection can be present as
![[Pasted image 20240702203728.png]]

# Motivating PCA
> At first, we have a cluster of datas
![[Pasted image 20240702211705.png]]

### Step 1: Re-align all the points center around (0,0) point
![[Pasted image 20240702211849.png]]
### Step 2: Try to project all the point on to x, y, x = -y axis
![[Pasted image 20240702211939.png]]
projected point look like this
![[Pasted image 20240702212022.png]]
Do the same for 2x = y axis
![[Pasted image 20240702212107.png]]
For the last line (red), we line the line up where all points projected to it spread out the most.
![[Pasted image 20240702212137.png]]
### Step 3: Re-arrange the line base on how spreaded they are 
![[Pasted image 20240702212432.png]]
### PCA Goals: find the projection that preserves the maximum possible spread in your data, even as you reduce the dimensionality of your data set. 

# Variance and Covariance
## Mean: average value out of total values
![[Pasted image 20240702215451.png]]


### Variance: large spread, large variance
![[Pasted image 20240702215609.png]]
![[Pasted image 20240702215703.png]]
1st Col: coordinates or value of x
2nd Col: Each value of x substract to the mean
3rd Col: Square of 2nd Col value.
![[Pasted image 20240702215955.png]]
> In short, Variance is the average distance from the mean.
>The image show 2 diff way to represent Variance: 1 with texts and 1 with symbols.
+ Calc the Variance of X and Y
	![[Pasted image 20240702220131.png]]


Problem: giá trị trên x và y giống nhau nhưng khi nhìn thì rõ ràng các điểm giá trị là khác nhau.
	**Variance helps us quantify how spread out your data is but now consider a situation where variance alone wouldn't be helpful. These two datasets have three observations each. They would have identical y variance and x variance and yet, it's obvious that there's a significant difference in the patterns of these datasets.**
	![[Pasted image 20240702220401.png]]
	Left: X Inscre, Y Descre
	Right: Y Inscre, X Descre
	![[Pasted image 20240702220523.png]]

### Covariance
> let see how covariance are calculated. They look the same as the Covariance of X and Y, but now depended on both of X and Y.
![[Pasted image 20240702220612.png]]

![[Pasted image 20240702220705.png]]

![[Pasted image 20240702221238.png]]
> Reason for Neg and Pos Cov(X, Y) => -X * Y -> - Cov(X, Y) and the Same for Y

![[Pasted image 20240702221416.png]]
