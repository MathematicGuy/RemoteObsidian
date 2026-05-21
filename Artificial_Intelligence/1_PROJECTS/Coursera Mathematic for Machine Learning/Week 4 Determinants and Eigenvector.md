---
banner: 1000_F_572489735_fRAzXItiIcyTttjJ9MUjsBEgvLTrphaa.jpg
---
# Span in Linear Algebra
> Span is the line that contain the vector
![[Pasted image 20240705162326.png]]

$$R^{2} = 1 − \frac{\sum(yi−y^i)^2}{\sum(yi−yˉ)^2}$$

$\overline{y}$
> The Basis is a Minimal Spanning Set (Basis is only 1 vector ). A line only have 1 Basis. The Basis is any vector align with the line.
![[Pasted image 20240705162432.png]]
> This is not a Basis, because it have 2 vector with same magnitude and direction. (too many vectors)
![[Pasted image 20240705163127.png]]

> Number of elements in the basis is the dimension. As the Basis is the original vector of that Space.
![[Pasted image 20240705162147.png]]

> A group of vectors is said to be **linearly independent if none of the vectors in the group can be obtained as a linear combination of the others.** or in other word
+ $ Ex: **A basis for a 3D vector space must consist of three linearly independent vectors. (n chiều thì n nghiệm**. VD: 3D -> 3 Nghiệm)

+ ? What if you added this other vector instead? In this case the **new vector in red is pointing in the same direction as the green one**. But it's simply **twice as long as the original vector.**
+ $ Since **one vector can be obtained as a linear combination of the others**, this set of vectors is called **linearly dependent**. Notice also that **even though we added a new vector to our set, the span of these vectors did not change, it remained a straight line**.
![[Pasted image 20240705162721.png]]
> If a vector not in the same direction and span. It is Linearly Dependent 

However this case the vectors are **not linearly independant**, this is because **the 4rd vector can be obtain from the Red and Teal vectors**.
+ $ This mean having 3 nor more vectors in the plance, or 4 or more vectors in the 3D space.
![[Pasted image 20240705163744.png]]

#### Let's see how to check for linear dependence 
![[Pasted image 20240705164120.png]]


# Determinants In-depth (định thức hiểu sâu)
## Singularity and rank of linear transformations
The image is Singular. it not covering the whole plane on the right, just a portion of it (**singular: matrix -> a line, a point**)
![[Pasted image 20240420230556.png]]

## Example: what T(0,1)=(2,5) T(1,0)=(3,1) mean ?
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

**Determinant**
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

+ ! The dot product in the upper image is wrong
	((1, 4),
	(-3, 3)) -> 3 + 12 = 15

**Matrix A:** 
	[2 3] 
	[4 1]	
**Matrix B:**
	[5 6] 
	[2 3]
**A * B** =  [2.5 + 3.2, 2.6 + 3.3]
		[4.5 + 1.2, 4.6 + 1.3]
**result** =  [16, 21]
		[22, 27]

## Others way to Calculate Determinant
![[Pasted image 20240708115216.png]]


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

+ ? PCA Visualization: Project data (matrix) onto a eigenvectors (PCA) 
![[Pasted image 20240702202537.png]]
Project (1, 1) we have the vector at the value of 1. However, summing the 2 variable (coordinate 1, 1) you ending up with a vector length of 2. 
+ To get the length we divided it by the square root of 2. Which is the norm of [1, 1]. (căn(1 + 1) = căn 2)

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

# [[Motivating PCA]]
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
#### PCA Goals: find the projection that preserves the maximum possible spread in your data, even as you reduce the dimensionality of your data set


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
+ ? The image show 2 diff way to represent Variance. One in Text and One in Symbol
+ Calc the Variance of X and Y
	![[Pasted image 20240702220131.png]]


Problem: giá trị trên x và y giống nhau nhưng khi nhìn thì rõ ràng các điểm giá trị là khác nhau.
	**Variance helps us quantify how spread out your data is but now consider a situation where variance alone wouldn't be helpful. These two datasets have three observations each. They would have identical y variance and x variance and yet, it's obvious that there's a significant difference in the patterns of these datasets.** 
	![[Pasted image 20240702220401.png]]
	Left: X Inscre, Y Descre
	Right: Y Inscre, X Descre
	![[Pasted image 20240702220523.png]]

### Covariance (Hiệp Phương Sai)
+ ! The Distance between 2 point. If we calc the distance of the same point, it truly just the Variance of that Point.
>They look the same as the Covariance of X and Y, but now depended on both of X and Y.
![[Pasted image 20240702220612.png]]
+ n - 1: mean every point except the center (0, 0) point. Because we are alignning all others points to it. 

![[Pasted image 20240702220705.png]]

> Reason for Neg and Pos Cov(X, Y) => -X * Y -> - Cov(X, Y) and the Same for Y]
![[Pasted image 20240702221416.png]]

# Covariance Matrix  (Ma Trận Hiệp Phương Sai)
![[Pasted image 20240703114445.png]]
![[Pasted image 20240703114551.png]]
**Remember how similar the covariance and variance formulas were**, it turns out that **the covariance of a variable with itself is actually just the variance** so you could rewrite your covariance matrix like this: (**Covariance** is just **Variance** with a **Co-Variance**. **Co** mean both x and y) 
![[Pasted image 20240703114857.png]]
>This truly is just a matrix of covariances between variables.  
>Cov(x, x) mean distance between 2 point x and x itself.  
![[Pasted image 20240703114939.png]]

### Rewrite the Covariance in Matrix form
Using A and $\mu$. 
+ A: represent a array of x and y
+ $\mu$: represent a array of $\mu_{x}$ and  $\mu_{y}$ (Mean_x and Mean_y)
+ ? Notice that we have to Tranpose the First $(A - \mu)^T$ so we can apply Matrix Multiplication (or dot product)
 ![[Pasted image 20240703115536.png]]
**Write it all down, we end up with**
![[Pasted image 20240703120006.png]]
+ ? Practice to calc the 1st row:
	![[Pasted image 20240703120040.png]]


#### Compact the Equation, we achieve:
**1st Multiplication:** $Cov(x, x)$ or $Var(x)$
 $$ 
\frac{1}{n-1}\prod(x_{1} - \mu_{x})(x_{1} - \mu_{x}) \Leftrightarrow \frac{1}{n-1}\prod(x_{1} - \mu_{x})^2 
$$

**2nd Multiplication**: $Cov(x, y)$ 
$$
\frac{1}{n-1}\prod(x_{1} - \mu_{x})(y_{1} - \mu_{y}) 
$$

**3rd Multiplication** $Cov(y, x)$ 
$$
\frac{1}{n-1}\prod(y_{1} - \mu_{y})(x_{1} - \mu_{x}) 
$$

**4th Multiplication** $Cov(y, y)$ or $Var(y)$ 
$$
\frac{1}{n-1}\prod(y_{1} - \mu_{y})(y_{1} - \mu_{y}) 
$$
#### Combine 4 equations above:
$$
\frac{1}{n-1}
\begin{bmatrix} 
Var(x) & Cov(x, y) \\
Cov(y, x) & Var(y)
\end{bmatrix} 

\Leftrightarrow

\frac{1}{n-1}
\begin{bmatrix} 
Cov(x, x) & Cov(x, y) \\
Cov(y, x) & Cov(y, y)
\end{bmatrix} 
$$
+  $\Leftrightarrow$  mean "the same as"

## To Conclude the Matrix Fomula is
$$
A - \mu = \begin{bmatrix} x_1 - \mu_x & y_1 - \mu_y \\ \vdots & \vdots \\ x_n - \mu_x & y_n - \mu_y \end{bmatrix} \quad C = \frac{1}{n-1} (A - \mu)^\top (A - \mu)
$$
![[Pasted image 20240703122547.png]]
+ $ Conclude: Any Covariance Matrix you calc will be Symmetric

![[Pasted image 20240703200007.png]]
+ ! Note: Use Numpy to check if your code are correct

### PCA - Overview
![[Pasted image 20240703212612.png]]
> How to find the best line, let's use the same Matrix we use previsously (in Eigenvalue and Eigenvector chapter)

![[Pasted image 20240703215609.png]]
Eigenvector and Eigenvalues come in pair
note: Xem lại nguồn gốc Eigenvectors
+ Covariance: 4 (Covariance always symmetric))
+ X-variance is 9
+ Y-variance is 3
	![[Pasted image 20240703220500.png]]
+ Choose the 1st Eigenvector since it Eigenvalue is much larger. (Thus more points can projected onto it)
	![[Pasted image 20240703220608.png]]
+ Now we have projected all points onto the line. We have reduce the dimensionality from 2D to 1D (x, y to z for example)
	![[Pasted image 20240703220700.png]]


  ### Step-by-Step to calc PCA
  From the data we can get the Covariance Matrix. 
  Next, we have to sort the Eigenvalue/vectors from the Biggest to Smallest ![[Pasted image 20240703220919.png]]
  + Say **you want to** reduce the dataset to 2 variable, lets take 2 Biggest variable and discard the rest:
	  ![[Pasted image 20240703221030.png]]

To project your data we'll need a eigenvector (present a features), create a new matrix where each column is one of the two eigen vectors scaled by its own norm.
	![[Pasted image 20240703221218.png]]
+ Finally, project your data onto these 2 vectors, giving you your final dataset which has only 2 features.

## PCA - Why it Works
Eigenvalues and Eigenvector form a Eigenbasis
![[Pasted image 20240703232838.png]]
C - Covariance Matrix: think of it as the change of basis, how would it transform space ?
e.g. the vector in Teal and orange Stretch itself from the origin (0, 0) longer in the opposite direction. 
+ Let's start by adding this point and seeing its transformation, and keep going all around the circle.

### PCA - Mathematical Formulation
**Goals:**
- [x] Understand Deeper about PCA
- [x] Re-write **step-by-step instruction to calc PCA**
- [x] Verification what I know by asking ChatGPT to **list out all the mathematical fomula** I need for Application 
- [x] Revision PCA by watching Startquest
- [x] Watch all Coursera Course and Ace the Exam
+ ! **Don't dig to deep into a topic**. Understand and note the essen of it. I have plenty of thing needed to do (use my time efficiently)
+ ? During the learning process, if I struck on sth find some help, don't waste my time onto what I have too little information about. 
+ ? Use **numpy library to verify my function result**

**Explanation Step**
+ ? Why we need it ? 
+ @ What does it do ?f
+ $ What we get from it?

To desmonstrate, given **5 variables**s with the **goal is reduce to 2 variables**
![[Pasted image 20240704120728.png]]
2) Center the data 
	Trừ vị trí mọi điểm cho vị trí của Mean (vị trí/giá trị trung bình của các điểm)
+ ? Thus, every points will be aligned to the Mean Line

![[Pasted image 20240704121042.png]]
+ ? Relationship between everypoint to the Mean?

![[Pasted image 20240704121416.png]]
+ ? 4) Sort the most Important valuables up top (hence PCA) 
+ ? 5) Discard the rest and keep n variable (in this example we keep 2 variables). Create a Projection Matrix from n most important variables we keep.
+ @ 6) **Project the data onto the vectors you choose** by multiplying the center data by your projection matrix

### Tóm tắt bằng ví dụ trực quan:

Hãy tưởng tượng bạn chụp ảnh một vật thể 3D (như quả bóng) và chuyển nó sang một bức ảnh 2D. Bức ảnh 2D giữ lại phần lớn thông tin về quả bóng, nhưng với ít dữ liệu hơn. PCA hoạt động tương tự bằng cách tìm các "góc nhìn" quan trọng nhất để biểu diễn dữ liệu trong không gian nhỏ hơn.


## Discrete Dynamical Systems
![[Pasted image 20240704165905.png]]
Say you want the predictions the following day, and so on repeat n day for n day ahead.
![[Pasted image 20240704165949.png]]
That what you though right, however the prediction stay put at the 10 days and being the same at the 11 days.
![[Pasted image 20240704170104.png]]![[Pasted image 20240704170216.png]]
Essentially the dot product is 1
![[Pasted image 20240704170252.png]]
> This is the transition matrix
> ![[Pasted image 20240704170339.png]]


       