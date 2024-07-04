note: 
Dimension -> variable from x, y, z.(e.g. with x, y form a 2D matrix we calc the Means of x and y)
![[Pasted image 20240704130726.png]]
Given a dataset
+ ? 1st we caculate the Mean of Each Dimension in the given data
![[Pasted image 20240704131927.png]]

+ ? 2nd we calculate the variance of Each Dimension
	we know with **Variance** of x we can **center the data** of around the Mean of X. (center of data is a dot, since we only have x)
	
+ $ Moving on with **COVARIANCE** (co mean together/mutual) 
	![[Pasted image 20240704131118.png]]
	With x and y, we can center data around a line since x and y form a line which we can call the Mean Line.
	![[Pasted image 20240703114939.png]]
+ $ To **Calculating the Center Line (PCA) of n many variable** and dimension we can **Rewrite the COVARIANCE into COVARIANCE MATRIX**  
+ ? A as the Matrix contain value of x and y 
+ ? $\mu$ as the Mean of x and y
+ ? note: we have to tranpose 1 of the (A - $\mu$) to perform dot product between matrixes.
	![[Pasted image 20240704132423.png]]
	In simple form, we can see Covariance Matrix as:
	![[Pasted image 20240704133055.png]]
**Covariance Matrix with dimensional value (x, y, z, etc...)**
+ **x** as the **1st variable along the diagnol**
+ **y** as the **2nd variable along the diagnol** 
+ **Covariance** as the **opposite diagnol**
+ ? notice that Var(x) come from Var(x, x)

**Example of how to calc the Covariance Matrix:**
![[Pasted image 20240704133733.png]]


+ ? 3rd Step is to **calc the Eigenvalue and Eigenvectors of the Covariance Matrix**
	**Visual Example:**
	![[Pasted image 20240704134853.png]]

+ ? 4th is to Sort Eigenvalue and Eigenvector by it size. (Help we to access the most important features (v and $\mu$) easier) 
![[Pasted image 20240704134810.png]]

+ ? 5th **Take n features base on your need** (The Dimension you willing to compress to e.g. orginal dimension is 5, you compress it to 2) and **put it into a Matrix** (**let call it a Features Matrix**)
![[Pasted image 20240704134803.png]]

+ ? 6th: Project the original Data onto the New Features Matrix you just found to Reduce it Dimension. Now you 
	![[Pasted image 20240704135021.png]]
+ X as the Data (Might be a Matrix)
+ $\mu$ Mean of the Data (Might be a Mean Matrix)
+ $V$ : Your Eigenvalues and Eigenvectors you just calculate.

