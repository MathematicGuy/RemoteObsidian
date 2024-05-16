
**1 - Compute the data mean** (tính giá trị trung bình của x)
Sum all the variables/examples then divided by the numbers of variables (M) we have.
![[Pasted image 20240516031858.png]]


**2 - Substract mean from each rows of X (centering the data)** 
![[Pasted image 20240516031913.png]]
	centering all the points by substract to its dimension means.
	can be x, y, z (Phi(i) = Y(i) - Yˉ)


**3 - Form the matrix A**
$$
\text{cov}(X,Y) = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n - 1} 
$$
Where:
- Xi​ and Yi​ are individual data points
- Xˉ and Yˉ are the means of X and Y, respectively
- n is the number of data points
note: A(t) -> A transpose matrix


**Hands-On Example**
Let's consider the following dataset with five data points for X and Y:

| X   | Y   |
| --- | --- |
| 2   | 4   |
| 3   | 5   |
| 1   | 3   |
| 4   | 6   |
| 0   | 2   |

1. Calculate means (tổng các điểm chia tổng số lượng điểm -> giá trị trung bình)
	- Xˉ = (2+3+1+4+0)/5=2
    - Yˉ = (4+5+3+6+2)/5=4
2. **Subtract means from each data point:** (centering the data)
Dịch chuyển các điểm về gốc bằng cách trừ mỗi điểm cho giá trị trung bình của của Chiều đó. (trong đây có chiều X và Y)
lưu ý: vì điểm trung bình trừ cho điểm trung bình đó sẽ bằng 0. Nói cách khác trừ mọi điểm cho điểm trung bình ta sẽ còn (n-1) điểm 
	vì điểm trung bình tự triệt tiêu chính nó hay dịch chuyển chính nó về vị trí gốc. Vì gốc vs điểm trung bình = nhau nên tổng số điểm sẽ bị trừ 1. 

| X - Xˉ | Y - Yˉ |
| ------ | ------ |
| 0      | 0      |
| 1      | 1      |
| -1     | -1     |
| 2      | 2      |
| -2     | -2     |
3. **Multiply corresponding differences and sum:** (nhân các điểm vào với nhau)
	(0 * 0) + (1 * 1) + (-1 * -1) + (2 * 2) + (-2 * -2) = 10

4. **Divide by (n-1):** (chia cho tổng số biến, -1 vì ko tính gốc.)
	Example of variable: (2-1) = 2 vì có 2 biến
	![[Pasted image 20240516042022.png]]
	10 / (5-1) = 2.5 = cov(X, Y) = C
Therefore, the covariance between X and Y is 2.5. This positive value aligns with the upward trend observed in the scatterplot.

