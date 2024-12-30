---
~
---

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
+ $(A - \mu)^\top (A - \mu)$ : Get the Relation of each point to each others point.  
	![[dot_product_components.png]]
+ $\frac{1}{n-1}$ : Dividing to total point's sum except for the center point (0, 0) that all points centralized around.
+ $ So we can understand that the **Covariance Matrix return a Matrix contain the information about the relationship between each points to each others** (The Mean of every Vectors or the PCA of each )
$$C = \frac{1}{n-1} (A - \mu)^\top (A - \mu)$$

Each vale pair (x, y) have it own PCA, the yellow line is 1 example out of many
![[Pasted image 20240709143558.png]]
![[Pasted image 20240709143752.png]]
The Matrix have 2 eigenvalues -> 2 eigenvectors -> 2 PCA line.


> How to **find the best line**, let's use the same Matrix we use previsously (in Eigenvalue and Eigenvector chapter)
![[Pasted image 20240703215609.png]]
Eigenvector and Eigenvalues come in pair
note: Xem lại nguồn gốc Eigenvectors
+ Covariance: 4 (Covariance always symmetric))
+ X-variance is 9
+ Y-variance is 3
	![[Pasted image 20240703220500.png]]
+ Choose the 1st Eigenvector since it Eigenvalue is much larger. (Thus more points can projected onto it)
	![[Pasted image 20240703220608.png]]
+ In case we have more features, we will need to sort them from low to High
	![[Pasted image 20240709153333.png]]
	![[Pasted image 20240709160403.png]]
	
+ Now we can projected all points onto the PCA line to reduce the dimensionality from 2D to 1D (x, y to z for example)
	![[Pasted image 20240703220700.png]]
	![[Pasted image 20240709160440.png]]

More:
+ https://ranasinghiitkgp.medium.com/principal-component-analysis-pca-with-code-on-mnist-dataset-da7de0d07c22
+ https://colah.github.io/posts/2014-10-Visualizing-MNIST/
+ https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix
+ https://www.kaggle.com/code/jonathankristanto/experimenting-with-pca-on-mnist-dataset

---



Here’s the complete translation of the document into Vietnamese while preserving its original meaning:

---

# Các Khái Niệm Toán Học Quan Trọng Trong PCA

## 1. Span (Không gian bao phủ)

**Định nghĩa:**
Span của một tập vector là tập hợp tất cả các tổ hợp tuyến tính có thể của các vector đó. Nó định nghĩa không gian được bao phủ bởi các vector.

**Trong PCA:**
Span của các thành phần chính (vector riêng) định nghĩa không gian mới với số chiều thấp hơn mà dữ liệu được chiếu tới.

**Ví dụ:**
Nếu các vector riêng là:
$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$
thì span của chúng là toàn bộ mặt phẳng 2D trong không gian ban đầu.

**Tại sao quan trọng?**
Span giúp chúng ta hiểu không gian mà các thành phần chính bao phủ, điều này rất quan trọng trong giảm số chiều.

## 2. Basis (Cơ sở)

**Định nghĩa:**
Cơ sở là một tập hợp tối thiểu các vector tuyến tính độc lập mà bao phủ toàn bộ không gian vector. Số lượng vector trong cơ sở là số chiều của không gian đó.

**Trong PCA:**
Các thành phần chính (vector riêng) tạo thành một cơ sở cho không gian mới với số chiều thấp hơn.

**Ví dụ:**
Nếu các vector riêng là:
$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$
chúng tạo thành cơ sở cho mặt phẳng 2D.

**Tại sao quan trọng?**
Các vector cơ sở cung cấp một hệ tọa độ mới cho không gian, cho phép biểu diễn dữ liệu duy nhất trong không gian đó.

## 3. Determinants (Định thức)

**Định nghĩa:**
Định thức của một ma trận là một giá trị vô hướng, cung cấp thông tin về các đặc tính của ma trận như khả năng nghịch đảo và hệ số co giãn của phép biến đổi tuyến tính mà nó đại diện.

**Trong PCA:**

Định thức của ma trận hiệp phương sai liên quan đến thể tích phân bố dữ liệu.

Định thức bằng 0 cho thấy dữ liệu nằm trong một không gian con có số chiều thấp hơn (ví dụ: một đường thẳng trong không gian 2D).

**Ví dụ:**
Với ma trận hiệp phương sai:
$$
C = \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}
$$
Định thức là:
$$
\text{Det}(C) = 4 \times 4 - 4 \times 4 = 0
$$
Điều này chỉ ra rằng dữ liệu nằm trên một đường thẳng.

**Tại sao quan trọng?**
Định thức giúp chúng ta hiểu hình học của phân bố dữ liệu, điều này quan trọng trong việc xác định các đặc trưng dư thừa.

## 4. Linear Independence (Độc lập tuyến tính)

**Định nghĩa:**
Một tập hợp các vector là độc lập tuyến tính nếu không vector nào trong tập hợp đó có thể được biểu diễn như một tổ hợp tuyến tính của các vector khác.

**Trong PCA:**
Các thành phần chính (vector riêng) là độc lập tuyến tính do tính chất của chúng.

**Ví dụ:**
Nếu các vector riêng là:
$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$
chúng là độc lập tuyến tính vì không vector nào là bội số của vector còn lại.

**Tại sao quan trọng?**
Độc lập tuyến tính đảm bảo rằng các thành phần chính không dư thừa và mô tả các hướng phương sai riêng biệt.

## 5. Variance (Phương sai)

**Định nghĩa:**
Phương sai đo lường mức độ phân tán của các điểm dữ liệu quanh giá trị trung bình. Nó thể hiện sự biến thiên trong dữ liệu.

**Công thức:**
$$
\text{Var}(X) = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2
$$
Với:

- ${x_i}$: Các điểm dữ liệu.
- $\bar{x}$: Giá trị trung bình.
- $n$: Số lượng điểm dữ liệu.

**Ví dụ:**
Dữ liệu: `[1, 3, 5]`.
Trung bình: $\bar{x} = 3$.
Phương sai:
$$
\text{Var}(X) = \frac{(1-3)^2 + (3-3)^2 + (5-3)^2}{2} = \frac{4 + 0 + 4}{2} = 4
$$

**Tại sao quan trọng?**
Phương sai giúp hiểu mức độ biến thiên của dữ liệu, điều cần thiết để nhận diện các mẫu và mối quan hệ.

## 6. Covariance (Hiệp phương sai)

**Định nghĩa:**
Hiệp phương sai đo lường mức độ thay đổi cùng nhau của hai biến và chỉ ra hướng của mối quan hệ tuyến tính giữa chúng.

**Công thức:**
$$
\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$
Với:

- $x_i, y_i$: Các điểm dữ liệu của biến $X$ và $Y$.
- $\bar{x}, \bar{y}$: Giá trị trung bình của $X$ và $Y$.

**Ví dụ:**
$X = [1, 3, 5]$, $Y = [2, 4, 6]$.
Trung bình: $\bar{x} = 3, \bar{y} = 4$.
Hiệp phương sai:
$$
\text{Cov}(X, Y) = \frac{(1-3)(2-4) + (3-3)(4-4) + (5-3)(6-4)}{2} = 4
$$

**Tại sao quan trọng?**
Hiệp phương sai giúp hiểu mối quan hệ giữa hai biến, rất cần thiết trong PCA.

## 7. Covariance Matrix (Ma trận hiệp phương sai)

**Định nghĩa:**
Ma trận hiệp phương sai là ma trận vuông chứa phương sai và hiệp phương sai giữa tất cả các cặp đặc trưng trong tập dữ liệu.

**Công thức:**
$$
C = \frac{1}{n-1} (X - \mu)^T (X - \mu)
$$
Với:

- $X$: Ma trận dữ liệu đã được chuẩn hóa.
- $\mu$: Vector trung bình.

**Ví dụ:**
Với $X = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$, ma trận hiệp phương sai là:
$$
C = \begin{bmatrix}
\text{Var}(X) & \text{Cov}(X, Y) \\
\text{Cov}(Y, X) & \text{Var}(Y)
\end{bmatrix} = \begin{bmatrix}
4 & 4 \\
4 & 4
\end{bmatrix}
$$

**Tại sao quan trọng?**
Ma trận hiệp phương sai được sử dụng trong PCA để xác định hướng của phương sai tối đa trong dữ liệu.

## 8. Eigenvectors and Eigenvalues (Vector riêng và giá trị riêng)

**Định nghĩa:**

- **Vector riêng:** Vector không thay đổi hướng khi áp dụng một phép biến đổi tuyến tính (chỉ bị co giãn).

- **Giá trị riêng:** Giá trị vô hướng biểu thị hệ số co giãn của vector riêng.

**Công thức:**
$$
C \mathbf{v} = \lambda \mathbf{v}
$$
Với:

- $C$: Ma trận hiệp phương sai.
- $\mathbf{v}$: Vector riêng.
- $\lambda$: Giá trị riêng.

**Ví dụ:**
Với $C = \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}$, giá trị riêng là $\lambda_1 = 8, \lambda_2 = 0$, và vector riêng là:
$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$

**Tại sao quan trọng?**
Vector riêng định nghĩa các thành phần chính (hướng phương sai lớn nhất), và giá trị riêng cho biết mức độ quan trọng của chúng.

## 9. Principal Component Analysis (PCA - Phân tích thành phần chính)

**Mục tiêu:**
Giảm số chiều của tập dữ liệu trong khi vẫn giữ được càng nhiều phương sai càng tốt.

**Các bước:**

1.  Chuẩn hóa dữ liệu: Trừ đi trung bình từ mỗi đặc trưng.
2.  Tính ma trận hiệp phương sai: Đo lường mối quan hệ giữa các đặc trưng.
3.  Tìm vector riêng và giá trị riêng: Xác định các thành phần chính.
4.  Sắp xếp vector riêng: Dựa theo giá trị riêng giảm dần.
5.  Chọn $k$ thành phần chính: Lựa chọn các thành phần quan trọng nhất.
6.  Chiếu dữ liệu: Biến đổi dữ liệu sang không gian mới với số chiều thấp hơn.

**Ví dụ:**
Với tập dữ liệu $X = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$:

- Dữ liệu chuẩn hóa:
$$
X_{\text{centered}} = \begin{bmatrix} -2 & -2 \\ 0 & 0 \\ 2 & 2 \end{bmatrix}
$$
- Ma trận hiệp phương sai:
$$
C = \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}
$$
- Vector riêng:
$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$
- Dữ liệu đã chuyển đổi:
$$
Z = \begin{bmatrix} -4 \\ 0 \\ 4 \end{bmatrix}
$$

**Tại sao quan trọng?**
PCA được sử dụng để nén dữ liệu, giảm nhiễu, và trích xuất đặc trưng trong học máy.

## 10. Projection (Phép chiếu)

**Định nghĩa:**
Phép chiếu ánh xạ các điểm dữ liệu lên không gian có số chiều thấp hơn được định nghĩa bởi các thành phần chính.

**Công thức:**
$$
Z = X_{\text{centered}} W
$$
Với:

- $Z$: Dữ liệu đã biến đổi.
- $W$: Ma trận chiếu (gồm $k$ vector riêng hàng đầu).

**Ví dụ:**
Với $X_{\text{centered}} = \begin{bmatrix} -2 & -2 \\ 0 & 0 \\ 2 & 2 \end{bmatrix}$ và $W = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$:
$$
Z = \begin{bmatrix} -4 \\ 0 \\ 4 \end{bmatrix}
$$

**Tại sao quan trọng?**
Phép chiếu giảm số chiều trong khi vẫn giữ lại thông tin quan trọng nhất.

## 11. Explained Variance (Phương sai giải thích)

**Định nghĩa:**
Phương sai giải thích đo lường lượng phương sai được giữ lại bởi mỗi thành phần chính.

**Công thức:**
$$
\text{Explained Variance Ratio} = \frac{\lambda_i}{\sum_{j=1}^p \lambda_j}
$$
Với:

- $\lambda_i$: Giá trị riêng của thành phần chính thứ $i$.
- $p$: Tổng số thành phần.

**Ví dụ:**
Với $\lambda_1 = 8$ và $\lambda_2 = 0$:
$$
\text{Explained Variance Ratio} = \frac{8}{8+0} = 1
$$

**Tại sao quan trọng?**
Phương sai giải thích giúp quyết định số lượng thành phần chính cần giữ lại.