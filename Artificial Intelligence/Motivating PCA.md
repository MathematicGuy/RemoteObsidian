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
+ $ To **Calculating the center line of n many variable** and dimension we can **Rewrite the COVARIANCE into COVARIANCE MATRIX** 
	![[Pasted image 20240704132423.png]]
	

**Covariance Matrix with dimensional value (x, y, z, etc...)**
+ **x** as the **1st variable along the diagnol**
+ **y** as the **2nd variable along the diagnol** 
+ **Covariance** as the **opposite diagnol**
