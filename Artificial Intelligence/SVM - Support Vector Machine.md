[[SVM HW]]

Face (green) / Non-Face (red)
![[Pasted image 20240625133833.png]]
> Can be written using (for 2D plane)
![[Pasted image 20240625133852.png]]

**A Linear Decision Boundary in 3-D space is a 2-D Plane**
![[Pasted image 20240625133959.png]]

**What is the optimal decision boundary ?**
> we do that using a safe zone or a margin: **width that u can extend until you hit features of both size**.
![[Pasted image 20240625134256.png]]
> Support Vectors: Closest data samples to the boundary
+ When points touching the boundary, its **supporting us to find the safe zone**. Thus we called them Support Vector. When we finding out those point, we can ignore all rest (points).

#Example:
**Given:**
![[Pasted image 20240625134620.png]]

**Find:**
![[Pasted image 20240625134657.png]]

## Finding Decision Boundary (W, b)
![[Pasted image 20240625134808.png]]

![[Pasted image 20240625135113.png]]


 ![[Pasted image 20240625135213.png]]

---

### Definition
+ **Subspace:** space inside another space
+ **Hyperplane:** is a flat subspace that divides a higher dimension into 2 parts. In 3D a hyperplane is a plane, in 2D a hyperplane is line both of them divide a space into 2 half-spaces.
	![[image/images.jpg]]
	
+ **[[Vector]] Components:** Each part of the vector is called a components. 2D vector have 2 components, 3D vector have 3 components. 
	*e.g.* Vector with 2 Components
	![[Pasted image 20250206162024.png]]


## Points to Hyperplane
**A line** *Y = WX + b* represents a linear model equation, where:
- *Y* is the predicted output,
- *X* is the input feature vector,
- *W* is the weight vector (coefficients),
- *b* is the bias term or intercept.
- The equation essentially states that the predicted output (Y) is a linear combination of the input features (X), weighted by the coefficients (W), and added with a bias term (b)


**[[Scalar projection]]**
![[Pasted image 20250206164211.png]]
$$s = ||a||cos\theta=a \cdot \hat{b}$$ where $s$ is the hypotenuse $a_{1}$ 
$$\cos \theta=\frac{a \cdot \hat{b}}{||a||}$$



## Support Vector Machine (SVM) - Basic Intuition 

**Terminology:** Say we have 2 groups of points red and blue, you want to draw a line to seperate them, but you don't just want a line divides the 2 groups, but a line that stays as far away from both groups as possible. 

**SVM aim to divide 2 groups of data/points by a single line** where its distant/margin to 2 data group is maximize, those closest point "touch" the margin are called **support vectors**. That distance called "marginal distant" and the single line called "Hyperplane" in SVM.   

 
(Good for Loss function?)
In a SVM, 2 class/group in the same dimension seperate into 2 side positive and negative.   

**Aim:** maximize marginal plane/distance -> help model generalize better
![[Pasted image 20250206114344.png]]

