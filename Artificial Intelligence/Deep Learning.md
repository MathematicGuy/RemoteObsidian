note and [resource](https://drive.google.com/drive/folders/1dHXTL_7PUNuzcu-ZSwLDGHGQLhvnc0ee?usp=drive_link)

---
# Deep Learning Book
>the book assume all readers come from a computer science background that are familiarity with programming, basic understading of computational performance issues, complexity theory, introductory level calculus and some of the terminology of graph theory.

#### **Part I:** **Introduces basic mathematical tools and machine learning concepts**
>readers familiar with linear algebra, probability, and fundamental machine learning concepts can skip Part I 

tensor: array with more than 2 axis.
distributive: phân phối
associative: liên kết, (adj) tập hợp  

$Ax = b$ where A is a $m \times n$ matrix and $b$ is a known vector $m$ and $x$ is a unknown vector waiting to be solved.

$orthogonal \space matrix$ is a square matrix whose row are mutually orthonormal
$A^{T}A = AA^{T} = I$
![[Pasted image 20241003155344.png]]
+ ? One of the most widely used kinds of matrix decomposition is called eigen-
decomposition, in which we decompose a matrix into a set of eigenvectors and
eigenvalues

Let use A to represent Eigendecomposition of the image above. with v1 orthonormal with v2 and scale by a factor of eigenvector $\lambda$. we written the $eigendecomposition$ of A as:
![[Pasted image 20241003155519.png]]
where V is the matrix concatinate eigenvectors to form a matrix V with one eigenvector per column, $\lambda$ vector is the concatination of $\lambda_{1}$ and $\lambda 2$, 

### [[The Argument of a Complex Number]]
+ note: understand complex number $i$ for this part.

#### **Part II:** **Describes the most established deep learning algorithms that are essentially solved technologies**
> note: readers who just want to implement a working system need not read beyond Part 2.


#### **Part III:** **Describes more speculative ideas that are widely believed to be important for future research in deep learning**


