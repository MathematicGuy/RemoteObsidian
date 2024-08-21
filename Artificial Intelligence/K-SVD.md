**Problem**: Noise Problem
**Purpose**: K-SVD is a dictionary learning algorithm for **creating a dictionary for sparse representations**, via a singular value decomposition approach.

![[Pasted image 20240820164504.png]]
1. Learning Dict: Ma trận A
	A Matrix can be voice, image, etc...
	
2. D is the dictionary matrix. The columns of D are the dictionary atoms, which are the building blocks that will be used to represent the data samples in Y. The goal is to learn this dictionary such that it can sparsely represent the data.
	
3. X is the what we want to find. Find X from A through D.
	A matrix (encode in a dictionary matrix)
		Vector K and N mean number of cols > rows.
		h - cols
	x (a sparse vector) - red (1) in x vector mean multiply the red row with k cols in A dictionary matrix. 
		vector with more 0 than 1, hence Sparse vector
	Ex: 3 row, 2 col
+ X là biểu diễn thưa của h thông qua A. Đại diện cho các yếu tốt quan trọng nhất trong tín hiệu đầu vào.

Chuẩn 0/1: số ptử khác 0/1 (/ -> hoặc)
$min_x||min(x)||_0$

**tìm x có số ptu khác 0 ít nhất thông qua A.** 
Tìm A - bằng H_i thông qua X_i 
step 1: find x
step 2: lock A, update A base on x find in step 1.
Cách cập nhât từ điển A có the thông qua H hoặc X.

$\epsilon$ : predefine or calculatable

NP-Hard - cố gắng tìm đc nghiệm có số lỗi $\epsilon$ nhỏ nhất
Idea: col of the dictis selected iter 1 by 1.

OMP -> good for sparse prob (cho biểu diễn thưa)
IRML -> good for dense prob (cho biểu diễn đầy - nhiều 1)
Optimal -> nghiệm có thành phần khác 0 ít nhất.

---

Y - DX ~ 0 the accurate DX is. in other word closer to Y.
	The lower the epsilon (noise) -> optimal
	+ Epsilon represent Noise -> if || Y - DX || lower than epsilon mean almost no noise. 
+ ? Noise Gauss model ???

Nhân với nghiệm tối ưu -> Khử đc nhiễu (nghiệm là gì?)


y_0 = no noise
y = A*x

**OMP**
```python
from sklearn.linear_model import OrthogonalMatchingPursuit
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate a sparse signal
signal_length = 100
sparse_signal = np.zeros(signal_length)
sparse_signal[[10, 30, 50, 70]] = [3, -2, 4.5, 1.2] # Non-zero coefficients

# Step 2: Generate a measurement matrix (dictionary)
measurement_matrix = np.random.randn(50, signal_length)

# Step 3: Create the observed signal with noise
noise_level = 0.5
observed_signal = np.dot(measurement_matrix, sparse_signal) + noise_level * np.random.randn(50)

# Step 4: Apply OMP for signal recovery
# Chuẩn 0, các tín hiệu của X khác 0 < 4. (X khác 0, X < 4)
omp = OrthogonalMatchingPursuit(n_nonzero_coefs=4)
omp.fit(measurement_matrix, observed_signal) # lọc noise
recovered_signal = omp.coef_

# Step 5: Plot the results
plt.figure(figsize=(12, 3))

# Original Sparse Signal
plt.subplot(1, 3, 1)
plt.stem(sparse_signal, basefmt='r', label='Original Sparse Signal')
plt.title('Original Sparse Signal')
plt.legend()

# Observed Signal
plt.subplot(1, 3, 2)
plt.stem(observed_signal, basefmt='b', label='Observed Signal with Noise')
plt.title('Observed Signal with Noise')
plt.legend()

# Recovered Sparse Signal
plt.subplot(1, 3, 3)
plt.stem(recovered_signal, basefmt='g', label='Recovered Sparse Signal')
plt.title('Recovered Sparse Signal using OMP')
plt.legend()

plt.tight_layout()
plt.savefig('omp.png')
plt.show()

```



