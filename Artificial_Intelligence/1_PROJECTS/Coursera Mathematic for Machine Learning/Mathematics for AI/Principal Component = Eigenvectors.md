**The Connection: Why PCs = Eigenvectors**

1. **Covariance Matrix:** In PCA, you start with a covariance matrix of your data. This matrix summarizes how each variable (feature) in your dataset varies with every other variable. The diagonal elements represent variances, while the off-diagonal elements are covariances.
    
2. **Maximizing Variance:** The goal of PCA is to find the directions (PCs) that maximize variance. The variance of the data projected onto a vector is given by:   
$$
	\text{Var(projection)} = \mathbf{v}^T \mathbf{\Sigma} \mathbf{v}
$$
- v is the vector onto which you project the data
- Σ is the covariance matrix

3. Eigenvector Equation:
	The eigenvector equation is the fundamental equation that connects a square matrix (like the covariance matrix Σ) with its eigenvectors and eigenvalues:
	$$
	\mathbf{\Sigma} \mathbf{v} = \lambda \mathbf{v}
	$$
Example: A vector 'v' is shown being transformed by the matrix Σ. The resulting vector (Σv) is in the same direction as v, but scaled by a factor λ (the eigenvalue).]


covariance matrix (ma trận hiệp phương sai) - change together or in opposite direction
![[Pasted image 20240516043945.png]]
Mul by the cov matrix -> turn the vector toward the direction of the greatest variable.
> Rotate vetor/Transform the vetor -> Multiply the Covariance Matrix with the vector

So multiply until when...when multiply to a value that don't turn the vector direction like e2. Because it already on that point
![[Pasted image 20240516044210.png]]

determinant - định 