Phép toán trên vector và Ma Trận
Cosine Similarity
Background Substraction



**NumPy Arrays** + **Numpy and 2D/3D Data Representation** -> [[Numpy]]
Brightness Changes -> uint8 data type
`np.ndenumerate(arr)`
Note Real life Use-Case using Numpy. 

### Linear Algebra and Applications
Explain Hadamard product
From Textbook - Dot product
Vector Operations
Notations
Background Subtraction
Cosine Similarity
Distance between two vectors
**Use Case:** Traffic Sign Matching
K-Nearest Neighbors


### Exercise: Linear Algebra and Numpy
Vector and Matrix representation
![[Pasted image 20250707205834.png]]
$R^{\space n}$ as vector. $R^{\space n \times m}$ as matrix.
m x n : row x column

**Hadamard Dot product and Division**: Basically performed calculation respectively for each element  on both matrix/vector. (Multiply is the same as division, just diff calculation)
![[Pasted image 20250707210508.png# left | 300 ]] ![[Pasted image 20250707210451.png# right | 400]]


**Multiplying a matrix/vector by a matrix**
+ ? Số CỘT bên Phải bằng số phần tử bên của bên Trái. 
	Vì Nhân ma trận là nhân từng phần tử tương ứng trong mỗi hàng của A nhân vs từng phần tử tương ứng trong mỗi cột ở $\vec{{x}}$.

**Background subtraction (tách nền)**
Trừ nền vs ảnh lấy giá trị tuyệt đối vì khi trừ giá trị có thể bị âm. Đối những giá trị âm, mình có thể clip rồi thay thế bằng 1 giá trị khác. Sau đó áp dụng hàm để thay nền mới.

