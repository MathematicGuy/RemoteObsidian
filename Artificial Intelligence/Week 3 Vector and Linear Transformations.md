![[Pasted image 20240410150837.png]]
+ ? This equation help make predictions of my target y for any new set of x values
![[Pasted image 20240410150810.png]]

![[Pasted image 20240410150250.png]]
Linear Equation compute the result in each layer. Finally resulting the final result


Revision Note 
![[Pasted image 20240311084327.png]]
+ 5. Each row of M * each value in v vector.
	Ex: 4x1 + 5x2 + 9x5 and so on...
	


+ ? A Vector
![[Pasted image 20240311091701.png]]

The difference between the vectors 1,3 and 4,1 is also taken component-wise to be 3-2. That is, this vector over here, which doesn't look like anything special, except if you were to translate it, it matches precisely with the vector obtained by joining the points 1,3 and 4,1.
	![[Pasted image 20240311084821.png]]


![[Pasted image 20240311084924.png]]

**Application for ML: calc he distance to vector (for shortest parth algorithm)**
![[Pasted image 20240311085005.png]]

### Multiplying a vector by a scalar
Scaling vector a scalar of 3
![[Pasted image 20240311085118.png]]
reverse direction if negative
![[Pasted image 20240311085141.png]]
Using Lamda as a Scaler
![[Pasted image 20240311085239.png]]


### The dot product
![[Pasted image 20240311085420.png]]
or we can express like this
![[Pasted image 20240311085434.png]]
dot product == Vector multiply with itself
![[Pasted image 20240311085533.png]]
Vector Transpose **(Turn ow to Column)**
![[Pasted image 20240311085600.png]]

![[Pasted image 20240311085630.png]]



#### Distance Between Vector
	![[Pasted image 20240313132925.png]]
#### Magnitude of 2 Vectors


### Geometric Dot Product (Tích Vô )
![[Pasted image 20240311085747.png]]

![[Pasted image 20240311085851.png]]

![[Pasted image 20240311090022.png]]


All the dot product inverse of u is < 0. And same direction as u is > 0
![[Pasted image 20240311090122.png]]
[Vietnamese document](https://minhhn.com/lap-trinh/dot-product-tich-vo-huong-tinh-goc-giua-hai-vector/)
![[Pasted image 20240311090531.png]]

### Equation as dot product
![[Pasted image 20240311091902.png]]

+ ? **Key Points:**
	- **Scalars**: The dot product outputs a single scalar value, not a new vector.
	- **Dimensionality:** The two vectors in a dot product calculation must have the same dimensions.

Cross Multiplication
> The product of 2 matrix can be use to get the 
![[Pasted image 20240313084303.png]]
	You only look at where the two fundamental vectors 1, 0, and 0, 1 go, and those are your columns of the matrix.
(Reverse 0 1 to 1 0)
![[Pasted image 20240311140229.png]]

![[Pasted image 20240311134917.png]]


![[Pasted image 20240313090859.png]]

![[Pasted image 20240313090926.png]]


 Is there a way to Transform the 1st to the 3rd
	![[Pasted image 20240313091036.png]]


![[Pasted image 20240313092050.png]]

Work exactly like the above. 
For each product of Row(m) * Each Product of Column(n) then Add it up together.
Ex: 3.1 + 1.1 + 4.-2 = 2
![[Pasted image 20240313092859.png]]


#### Identity Matrix (ma trận đơn)
> The identity matrix is the matrix that when multiplied by any other matrix it gives the same matrix
	![[Pasted image 20240313093349.png]]


#### Inverse 
![[Pasted image 20240313093519.png]]
 
![[Pasted image 20240313093541.png]]


![[Pasted image 20240313093628.png]]

![[Pasted image 20240313094044.png]]
Can calculate det -> No Inverse exist 
	![[Pasted image 20240313100304.png]]
	![[Pasted image 20240313100317.png]]

Remember Singular Matrix is a matrix with the rank of 1 therefor it just 1 line & cannot be an inverse matrix (Matrix require at least 2 lines to formed)  

### Neural networks and matrices
**Spam Filter**
	use classifier
+ **Identifying Important Words:** In order to build a spam filter, we **need to identify certain words that are commonly associated with spam emails, such as "lottery" and "win"**. 
	
+ **Calculating Sentence Scores:** Once we have the scores for each word, we can calculate the score of a sentence by adding up the scores of the words it contains. 
![[Pasted image 20240313102716.png]]

+ Linear algebra helps us assign scores to these important words. We can assign a score to each word based on its relevance to spam. 
	
+ Setting a Threshold: Linear algebra also helps us set a threshold value. This threshold determines the minimum score required for an email to be classified as spam
![[Pasted image 20240313102813.png]]


+ ? Classification: Finally, linear algebra allows us to classify emails based on their scores. If the score of an email is above the threshold, it is classified as spam. Otherwise, it is classified as non-spam
![[Pasted image 20240313102931.png]]

![[Pasted image 20240313103042.png]]

![[Pasted image 20240313103054.png]]

Check if the Equation is Neg - or Pos + using Threshold
![[Pasted image 20240313103219.png]]


![[Pasted image 20240313130652.png]]

![[Pasted image 20240313131005.png]]


