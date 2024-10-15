# Scaling & Shifting
> transform every data point to smaller or larger value while still maintain the distribution between each data point.
![[Pasted image 20241015154308.png]]
>Choose a specific value over the data -> normalization 


# Normalization
![[Pasted image 20240719091104.png]]

**Example**
![[Screenshot 2024-10-15 152130.png]]





![[Pasted image 20240719091158.png]]
+ ! This is not normal distribution. Bc it a linear transformation

![[Pasted image 20240719091421.png]]

For example you have 2 point as 2 features and compute the distance between 2 features. But 1 feature have much bigger value than other feature. 
![[Pasted image 20241015155021.png]]

Higher value doesn't mean it more important -> by rescaling each features contribute roughtly to the distance.
![[Pasted image 20240719091629.png]]

# Standardization (Z-Score Normalization)
> Conducted to **Transform the data** to **have a mean of zero and standard deviation of 1**. Which mean data average is zero and average deviation from 0 is 1 (i.e. most of the data stay in range -1 to 1) ![[Screenshot 2024-10-15 153125.png]]
> where:
 
**Mean $\mu$:** $$\mu = \frac{1}{n} \sum^{n}_{i=1}x_{i}$$![[Pasted image 20241015160927.png]]

**Standard Deviation $\sigma$:**$$\sigma = \sqrt{ \frac{1}{n} \sum^{n}_{i=1}(x_{i} -\mu)^2}$$
![[Pasted image 20241015161047.png]]


+ ? Standardization is a **Linear Transformation**.
+ ? Implement using Skit-learn![[Pasted image 20241015153005.png]]
Z Board: Let me determine the distribution between 0 and 1 using the Area to the Left which is the sum of $z_{x}$ and $z_{y}$ coordinate. 
Ex: z = 0.507 then I choose $z_{x}=0.07$  and $z_{y}=0.5$
![[Pasted image 20240719092819.png]]

![[Pasted image 20240719092048.png]]
Deviation: độ lệch (tốc độ tăng trưởng của z/ khoảng cách tương đối giữa các điểm) 
Mean: giá trị trung bình của các điểm.
![[Pasted image 20240719092242.png]]

![[Pasted image 20240719092419.png]]
Let Convert the value to find the distribution for X < 49
![[Pasted image 20240719092643.png]]

For X in between in this example: 5.81 < X < 6.3. We just need to substract the smaller area to the bigger area. (Since the bigger area contain the smaller area. thus subtract the smaller will return us the between area)
> To solve this:
> 1) Standardization the Distribution using Z-Scores.
> 2) Subtract 2 standardized area. Done
![[Pasted image 20240719095011.png]]

---
# STANDARDIZATION vs NORMALIZATION
> **Scaling (standard or normalization) is required** when we use **machine learning algorithm used gradient calculation (e.g. ANN, Logistic Regression, etc...)**
+ ? However, scaling is not required for distance-based and tre-based algorithms suck as K-Means Clustering, SVD and K Nearest Neighbor, Decision Trees, Random Forest and XG-Boost.

Specifically for Neural Network (use Gradient Descent), **Normalization is preferred** since we **don't assume any data distribution**. 
**Standardization is preffered** 
	+ when **data follows gaussian distribution**.
	+  over normalization **when there are a lot of outliers**.

