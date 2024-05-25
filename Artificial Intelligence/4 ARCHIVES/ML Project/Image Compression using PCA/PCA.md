**PCA Overview**
• Understand the differences between supervised and unsupervised learning
• Have a conceptual understanding of PCA
• Understand the PCA drawbacks
• Understand in details the PCA algorithm
• Details the PCA algorithm
• Understand the difference between Covariance matrix and SVD
• Have a clear idea about the main applications of PCA
• Implement PCA from scratch for Image compression
• Implement PCA from scratch for Data Preprocessing & Visualization
• Use PCA for Regression tasks and compare the performance with and without PCA (Regression tasks - nhiệm vụ hồi quy) 
• Understand the biplot and the screeplot 
• Discuss the importance of Feature scaling for PCA (chia tỷ lệ tính năng cho )
• That's it !!

---
1D
![[Pasted image 20240516022045.png]]
2D, but if we draw a line through all the line we can present it in 1D (the new line represent that dimension)
![[Pasted image 20240516022008.png]]
2D (For this example, we can draw a line and present information, but some information will loss)
![[Pasted image 20240516022020.png]]
+ In the first two examples, we can represent the data fully without losing any information with only ONE DIMENSION
+ In the third example, we can represent the data with one dimension but some information will be lost.

**What is PCA**
![[Pasted image 20240516021818.png]]
+ The fish's shape is described by 2 variables, height and width
+ The two variables are dependent on each other,
+ **We can get the shape Of the fish using only a single component. The Principal component**.
	we call it the principle component because it contain most of the information if not all.


note: the dimension perpendicular to the original line -> orthogonal (2 vector vuông góc)
+ PCA transforms the two original variables into two orthogonal (trực giao) (independent) components that give a complete alternative description.
+ The first component (blue line) will explain most of the variation in the data.
+ The second component (dotted line) will explain the remaining variation.
	component (thành phần)

> PCA Works by finding the direction/ line/component that has the least information loss the largest variance.
+ The goal of PCA is to reduce the dimensionality of the data while keeping the information loss minimum.

**PCA Drawback**
![[Pasted image 20240516023331.png]]
+ PCA assumes that the variabels are linearly correlated. If the correlations is not linear, then PCA will not be as efficient: a
+ PCA performs lossy compression, which means that information is lost when we discard insignificant components: b
+ Scaling of variables can yield different results, Hence, scaling that you use should be documented Scaling should not be adjusted to match prior knowledge Of data.
+ Since each principal components is a linear combination of the original features, visualizations are not easy to interpret or relate to original features

###  PCA Algorithm steps
+ Suppose x1, x1, ..., xM are N-dimensional vectors. So, x is an N * M matrix
	N: numbers of dimension/features
	M: numbers of samples
	![[Pasted image 20240516031652.png]]

note: Mean -> giá trị trung bình của dữ 
**1 - Compute the data mean** (tính giá trị trung bình của x)
Sum all the variables/examples then divided by the numbers of variables (M) we have.
![[Pasted image 20240516031858.png]]


**2 - Substract mean from each rows of X (centering the data)** 
![[Pasted image 20240516031913.png]]
	centering all the points by substract to its dimension means.
	can be x, y, z (Phi(i) = Y(i) - Yˉ)

**3 - Form the matrix A** 

```tikz
\usepackage{tikz} \usepackage{pgfplots} % For plotting graphs
\begin{document}

\begin{tikzpicture}
    \begin{axis}[
        xlabel=$X$,
        ylabel=$Y$,
        xmin=-1.5, xmax=1.5,
        ymin=-1.5, ymax=1.5,
        axis lines=middle,
        grid=both,
        minor tick num=1,
        ]
        \addplot[only marks, mark=*, blue] coordinates {
            (0.8, 0.9) 
            (1.0, 1.1) 
            (0.5, 0.7)
            (-0.2, -0.1) 
            (-0.8, -0.7) 
        };
    \end{axis}
\end{tikzpicture}

\end{document}
```

![[Pasted image 20240516032105.png]]
then [[compute the covariance matrix C]] 
	Ma trận hiệp phương đóng vai trò xoay vector của biến trở thành thành phần chính qua việc nhân với vetor để xoay chiều của nó.
![[Pasted image 20240516032122.png]]

(both are covariance matrix C but present in different form)
$$
\text{cov}(X,Y) = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n - 1} 
$$
- Xi​ and Yi​ are individual data points
- Xˉ and Yˉ are the means of X and Y, respectively
- n is the number of data points
note: A(t) -> A transpose matrix


**4 - Compute the eigen values of C**
![[Pasted image 20240516032600.png]]
- Giải quyết vấn đề xoay đường PC. Nhân đến khi nào mà hướng của vector không đổi khi nhân với ma trận hiệp phương và lúc đó ta sẽ có giá trị slope lớpn nhất, 
N column -> N eigen value
*Example:* (eigenvector and eigenvalues - vectơ riêng và giá trị riêng)
![[Pasted image 20240516034719.png]]
Eigen vector (x) and Eigenvalue (lambda)
![[Pasted image 20240516035949.png]]

5 - Compute the **eigen vectors** of C
![[Pasted image 20240516040458.png]]
+ Since C is symmetric u1, u2,...,uN form a basis
+ Any vector
	 ![[Pasted image 20240516040527.png]]
	phi(i) can be re-construct using the linear combination of the eigenvectors
	![[Pasted image 20240516040725.png]]	
So, basically, **[[Principal Component = Eigenvectors]]**. Watch [this video](https://www.youtube.com/watch?v=fKivxsVlycs) for more reference 
Make the vector to turn toward where the variance the greatest

6 - **Dimensionality Reduction Step:** Keep only the terms corresponding to the K largest eigen values.
![[Pasted image 20240516050819.png]]
Reduction step: keep only the term corresponding to the k largest eigenvalues  
what we going to do is **calc the eigenvalue** from the cov matrix and the cov matrix is coming from subtracting the mean from each row. And we will get these eigenvalues **they will be values and sort them in decending order**. Then we get the corresponding eigenvector

