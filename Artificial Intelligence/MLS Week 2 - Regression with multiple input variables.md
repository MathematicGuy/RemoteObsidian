![[Pasted image 20241014141110.png]]
+  arrow above parameter (e.g. x) notate that it a vector of number array. 
+ Each column represet a feature
+ Each row represent a example of its column. For example $x^{(1)} _{i}$ mean feature 1 (i.e. column 1) feature index at i (i.e. thứ i or i-th) 

Model:
![[Pasted image 20241014141317.png]]
Model with continuous features. 
![[Pasted image 20241014141311.png]]
Example for house price prediction base on features the house have, we can plot the function as (base price as the starting price):
![[Pasted image 20241014141415.png]]

#### Vectorization
> Achieve parallel mutiplication in matrix multiplication for efficiency (which processed using GPU)  

>`np.dot()`: help you to calc the sum of the product between 2 corresponding elements. 
![[Pasted image 20241014142644.png]]
+ ? If 2 matrix use np.dot() each value in matrix 1 row will multiply with each value in matrix 2 column.

> Vectorization allow parallel processing (i.e. the computer subtract/addition/divided/multiply at the same time)
![[Pasted image 20241014143438.png]]
![[Pasted image 20241014143749.png]]

