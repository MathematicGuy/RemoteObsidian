---
~
---
# Determinants and Eigenvectors 

## Application to PCA
![[Pasted image 20240709121250.png]]

## What to Expect
![[Pasted image 20240709121339.png]]
![[Pasted image 20240709121431.png]]
>Learn how to find the Basis of a Matrix base on the Matrix Singularity

![[Pasted image 20240709121404.png]]
![[Pasted image 20240709121448.png]]
>Learn the relationship of between Span and Determinant

![[Pasted image 20240709121415.png]]
![[Pasted image 20240709121456.png]]
> Finally, Find the Eigenvalues and Eigenvectors of a Matrix. Which allow us to find the basis vector that reduced the matrix dimension. 


![[Pasted image 20240709121841.png]]
>Determinant is the Area of a Matrix. Thus Singular Matrix (1 Dimension Matrix) have Determinant of 0.
+ ? However if the Det is Negative, it doesn't affect the singularity of the matrix
	![[Pasted image 20240709122235.png]]


## Determinant of a Product
![[Pasted image 20240709122300.png]]

Multiplying the original matrix with a matrix with Det = 5 -> Its blow up by 5
![[Pasted image 20240709122342.png]]
**Apply the same method, we have:**
![[Pasted image 20240709123124.png]]
+ ! The dot product in the upper image is wrong. The correct result for det  = 15 is
	((1, 4),
	(-3, 3)) -> 3 + 12 = 15

![[Pasted image 20240709123052.png]]

### Inverse Matrix: 1 / M (literally)
> Determinant of the Matrix
![[Pasted image 20240709123238.png]]
![[Pasted image 20240709123256.png]]
> If det = 0, it wouldn't have an Inverse. Because 1/0 = null

![[Pasted image 20240709123907.png]]

# Base

> Basis Vector is the Base Vector of a Matrix
![[Pasted image 20240709124416.png]]
![[Pasted image 20240709124411.png]]

Bases of a Matrix can be use to navigate to any point in the plane. (eigenvectors)
![[Pasted image 20240709124455.png]]


Span is like the magnitude of a vector (Eigenvalue) pointing to a direction
![[Pasted image 20240709124603.png]]

![[Pasted image 20240709124703.png]]
> This mean there cannot be 2 indentical vectors with the same magnitude pointing toward a direction. (Matrix have the same span -> that span not a basis)

 A group of vectors is said to be **linearly independent if none of the vectors in the group can be obtained as a linear combination of the others.** or in other word
+ ? Ex: **A basis for a 3D vector space must consist of three linearly independent vectors. (n chiều thì n nghiệm**. vd: 3D -> 3 Nghiệm)
![[Pasted image 20240709124754.png]]
+ $ Since **one vector can be obtained as a linear combination of the others (2 blue = 1 red)**, this set of vectors is called **linearly dependent**. Notice also that **even though we added a new vector to our set, the span of these vectors did not change, it remained a straight line**.

In this example, we can form the yellow vector using blue and red vector -> Not Linearly Dependent (because there're >1 yellow vector) 
![[Pasted image 20240709125217.png]]
This also not independant because the red vector can be form using the combination of yellow and blue.
![[Pasted image 20240709125401.png]]

![[Pasted image 20240709125436.png]]
Put $\beta$ and $\alpha$ to the equation we achive $[-5, 3]$, thus the matrix is linear dependence.
+ $ We could also use others method to find the x and y like Gaussian Elimination.

![[Pasted image 20240709130330.png]]
1. **First Scenario (Leftmost)**:
    
    - **Description**: One vector.
    - **Spanning**: This vector spans a line (1-dimensional subspace).
    - **Independence**: It is linearly independent by itself.
    - **Conclusion**: It is a basis for a line.
2. **Second Scenario**:
    
    - **Description**: Two vectors.
    - **Spanning**: These vectors span the plane (2-dimensional space).
    - **Independence**: They are linearly independent (no vector can be written as a combination of the other).
    - **Conclusion**: They form a basis for the plane.
3. **Third Scenario**:
    
    - **Description**: Two vectors pointing in the same direction (collinear).
    - **Spanning**: They only span a line (1-dimensional subspace), not the entire plane.
    - **Independence**: They are linearly dependent (one vector can be written as a scalar multiple of the other).
    - **Conclusion**: They do not form a basis for the plane.
4. **Fourth Scenario (Rightmost)**:
    
    - **Description**: Three vectors.
    - **Spanning**: They can span the plane (if not all are collinear).
    - **Independence**: They are linearly dependent (at least one vector can be written as a linear combination of the others).
    - **Conclusion**: They do not form a basis for the plane because of the dependency.

### Why the Last Two Are Not Linearly Independent:

- **Third Scenario**:
    
    - **Spanning**: The two vectors span only a line, not the entire plane.
    - **Dependence**: Both vectors are collinear, making them linearly dependent. Therefore, they cannot form a basis for a plane (which requires two linearly independent vectors).
- **Fourth Scenario**:
    
    - **Spanning**: Three vectors can span the plane.
    - **Dependence**: The presence of three vectors in a 2D space inherently leads to linear dependence, meaning at least one of the vectors can be expressed as a linear combination of the other two.
    - **Example**: If you have vectors v1,v2,v_1, v_2,v1​,v2​, and v3v_3v3​, and v3v_3v3​ can be written as v3=av1+bv2v_3 = a v_1 + b v_2v3​=av1​+bv2​, then they are linearly dependent.

### Summary:

- **Third Scenario**: The vectors are collinear, hence linearly dependent and do not span the plane.
- **Fourth Scenario**: In a 2-dimensional space, having more than two vectors means they are necessarily linearly dependent, which disqualifies them from forming a basis despite spanning the plane.


# Determinants and Eigenvectors
## Eigenbasis
![[Pasted image 20240709130906.png]]
> Magnitude or a Scalar for Matrices.

## Eigenvalues and Eigenvectors
> It a **Simplified form of Matrix Multiplication.** Instead of 1 result, we seperate it into a vector called eigenvectors and a value called eigenvalue.   
![[Pasted image 20240709131049.png]]
![[Pasted image 20240709131302.png]]

To find the **3rd vectors eigenvalue and "eigenvector** we can use vector combination method. (like pythagorean). We achieve, -3 in x-axis and 2 in y-axis for each vectors.
![[Pasted image 20240709131341.png]]
Fomulate, we get the Eigenvalues and eigenvectors of the 3rd vector.
![[Pasted image 20240709131335.png]]
![[Pasted image 20240709131637.png]]

+ $ **Eigenvalues and Eigenvectors Conludesion**
![[Pasted image 20240709131726.png]]
+ Allow us to Form a new vectors base on the basis (eigenvectors) and scalar (eigenvalue of each eigenvectors)

+ ? A - $\lambda I$ = 0    
![[Pasted image 20240709131928.png]]
+ ? Use Eigenvalue to find Eigenvectors
![[Pasted image 20240709132003.png]]
+ **[[Example of Finding Eigenvectors and Eigenvalues]]**

![[Pasted image 20240709132322.png]]

### On the number of eigenvectors
![[Pasted image 20240709132342.png]]
![[Pasted image 20240709132352.png]]
![[Pasted image 20240709132417.png]]
![[Pasted image 20240709132434.png]]
![[Pasted image 20240709132504.png]]
> We achieve 3 vectors, thus a **Eigenbasis can be form** 

Add 4 to the A[0, 2], we have only 3 vectors -> no eigenbasis 
![[Pasted image 20240709132640.png]]

![[Pasted image 20240709132602.png]]

# Dimensionality reduction and Projection
![[Pasted image 20240709134423.png]]
**Goals:**
+ Reduce dimensions (n of columns) of dataset
+ Preserve as much information as possible
**Suggested method:** delete columns, however it can lead to **Loses of valuable information**

What we do is we use all the information we gather using mathematic fomula and compress mutiple values into 1 or less than than the original total values/features.

>Given eigenvectors matrix M = (x, y) and  eigenvalues = [1, 1] as the values for this example
![[Pasted image 20240709134655.png]]
+ ? Using Pythagorean we, can calculate the magnitude of  eigenvectors (1, 1) as $\sqrt{ 1 + 1}$ . In matrix we call it the norm of 1 (1st norm) 
![[Pasted image 20240709135041.png]]
+ ? Next, we project the the 1st row into eigenvectors (1, 1) by multiplying 2 vectors (1, 1) with the magnitude of (1,1) = $\sqrt{2}$  => $\frac{1+1}{\sqrt{2}}$ 
![[Pasted image 20240709140147.png]]
Do the same for every matrix's row, we got the final coordinates 
![[Pasted image 20240709140311.png]]

Rotate the plane to horizontal for better visulize, we can say the the 1st 2 values are the most important factors. 
![[Pasted image 20240709140721.png]]

+ $ **Conclude Fomula**
![[Pasted image 20240709140829.png]]
+ $A_{P}$ Projected Matrix = The Matrix  * Eigenvectors (eigenvector as the PCA line)  
+ A as the Matrix (row x column)
+ V as the eigenvectors (by n column/features)

V is the n features we want to reserve for matrix A. V with 2 columns = reserve 2 features from Matrix A.  
![[Pasted image 20240709141418.png]]

![[Pasted image 20240709141553.png]]

# [[Motivating PCA]]
Step-by-Step Dimensionality Reduction
**Given Matrix A represent every points in the plane**
![[Pasted image 20240709142849.png]]
1) **Centralize the Data**	![[Pasted image 20240709142912.png]]
	First we have to **calculate the Mean** of features/columns (n row's values mean n column)
		![[Pasted image 20240709143045.png]]
	Then Centralize all point by subtract each point by its $\mu$ (Mean) 
	![[Pasted image 20240709143421.png]]
	![[Pasted image 20240709143443.png]]


Now, we want to reduce the information we have by placing a line called PCA which allow use to preserve n dimension data by projecting all point to the PCA. In other word the eigenvectors that contain the most information. (have the most spreaded points/datas)
![[Pasted image 20240709144920.png]]
-> Most Spreaded data mean the **largest average distributed distance between all points**. So achieve that, we calculate the Covariance matrix
$$
A - \mu = \begin{bmatrix} x_1 - \mu_x & y_1 - \mu_y \\ \vdots & \vdots \\ x_n - \mu_x & y_n - \mu_y \end{bmatrix} \quad C = \frac{1}{n-1} (A - \mu)^\top (A - \mu)
$$
Since this Matrix will return a square matrix (singular matrix) which contain a Eigenvalues and Eigenvectors. 
+ $(A - \mu)$ : Coordinate of a centralized points.
+ $(A - \mu)^\top (A - \mu)$ : Projected each point to each others point.
+ 

+ ? To achieve this, we  

After that, we need to measure the relationship between each point by **projected all points onto the Mean Line of each Means** (each point have it own line, the yellow line is 1 example)
+ ? We  
![[Pasted image 20240709143558.png]]
![[Pasted image 20240709143752.png]]