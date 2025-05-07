**Note:** [[SVD Singular Value Decomposition in Dimensionality Reduction]]

---

![[Pasted image 20250507153740.png]]

![[Pasted image 20250507153807.png]]

**Note:** A Matrix is orthogonal if its transpose is equal to its inverse ($A^T = A^{-1}$)
![[Pasted image 20250507155244.png]]

**Transpose of a Square Matrix**
![[transpose2.jpg]]


$AV = U\Sigma$ = $U \Sigma V^T$, Find U & V -> Multiply both side by its transpose. 
Where:
+ $A$ is the **original matrix being decomposed.**
+ $\Sigma$ is the **diagnol matrix.** (Matrix with numnbers along the diagnol  -> inverse of $\Sigma$ is just itsef)
+ $U$ is an **orthogonal (vuông góc) matrix** whose columns are the **left singular vectors of A.** 
+ $V$ is an **orthogonal matrix** whose columns are the r**ight singular vectors of A.** 
+ Note: $I$ is the identity matrix where its diagnol full of 1.

![[Pasted image 20250507162931.png]]
+ $V$ is given eignedecomposition of $A^T A$
+ $V$ is an orthogonal matrix, because $A^T A$ is symmetric
 
 
![[Pasted image 20250507163155.png]]

+ $ **SVD** answer the question which direction the Vector stretched the most. 
![[Pasted image 20250507163232.png]]

![[Pasted image 20250507163332.png]]

![[Pasted image 20250507163347.png]]

![[Pasted image 20250507163411.png]]

![[Pasted image 20250507163451.png]]

Inverse Matrix cannot inverse matrix that are squash from a higher dimension. 