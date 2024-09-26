```ad-success
In this Note we will exploring how to **Applying Linear Regression and Gradient Descent** to **Predict Sales by TV Marketing Expenses**
```


### Understand the Data
**Dataset:** data/tvmarketing.csv
```js
TV,Sales
230.1,22.1
44.5,10.4
17.2,9.3
...
```

Before solving problems let understand what our dataset look like by reading head values
```python
path = "data/tvmarketing.csv"
s = pd.read_csv(path)d
adv.head
```
![[Pasted image 20240916211912.png]]
and ploting it
```python
adv.plot(x='TV', y='Sales', kind='scatter', c='black')
```
![[Pasted image 20240916211945.png]]

### Plotting Linear Regression Line
Before starting, we need to find the polynomial that fit to the graph/data points. "Tìm đa thực cho đồ thị"/"các điểm trên". 
>We could use `np.polyfit` from numpy to finds the coefficients (hệ số) of a [[polynomial]] (đa thức mũ 2) using [[Least Squares Method]] (basically **find m and b of a polynomial)** **of x: tv marketing and y: sales.**
```python
import numpy as np
import matplotlib.pyplot as plt

# Perform a linear fit
m_numpy, b_numpy = np.polyfit(tv, sales, 1)

# Generate the fitted line
fitted_line = m_numpy * X + b_numpy

# Plot the data points and the fitted line
plt.scatter(X, Y, color='red', label='Data Points')
plt.plot(X, fitted_line, label=f'Fit: y = {m_numpy:.2f}x + {b_numpy:.2f}', color='blue')
plt.legend()
plt.show()
```
![[Pasted image 20240925142010.png]]
+ $ To improve further understanding, here a version of **LeastSquare** function from scratch which represent these fomula:
$$m=\frac{n\sum xy - \sum x\sum y}{n\sum x^{2}- \left( \sum x\right)^{2}}; \space b = \frac{\sum y - m\sum x}{n}$$
```python
def LeastSquares(x, y):
    n = len(x)
    xy_sum = sum(x*y)
    x_sum = sum(x)
    y_sum = sum(y)
    x_sqrt_sum = sum(x**2)
    
    m = (n*xy_sum - x_sum*y_sum)/(n*x_sqrt_sum - x_sum**2)
    b = (y_sum-m*x_sum)/(n)
    return m, b
```
+ ? For x and y, its represent tv and sales. Ours goal is to predict sales by tv marketing express. So let **tv marketing express** as **x** and find **y as sales**.
```python
# input tv as x and sales as y
m, b = LeastSquares(tv, sales)
# get m and b for find x and y
print(f"Linear regression. Slope: {m}. Intercept: {b}")
```
> Linear regression. Slope: 0.04753664043301965. Intercept: 7.032593549127711
```python
data.plot(x='TV', y='Sales', kind='scatter')
# we have tv as x
plt.plot(tv, m*tv+b, color='red', label=f'Regression Line: y = {m:.2f}x + {b:.2f}')
plt.legend()
```
>as we see, it the same like above when using np.polyfit(X, Y, 1)
![[Pasted image 20240925142621.png]]
#### Liner Regression using `Scikit-Learn`
>Beside the code above, there Scikit-learn library can help us to find the linear regression line.
```python
lr_sklearn = LinearRegression()
```
Before fitting x, y into lr_sklearn. remember to convert them to numpy data type.
```python
tv = np.array(tv)
sales = np.array(sales)
lr_sklearn.fit(X_sklearn, Y_sklearn)
```
After that, call sklearn function to find m and b
```python
m_sklearn = lr_sklearn.coef_
b_sklearn = lr_sklearn.intercept_

#? Yay, the result are the same as above
print(f"Linear regression using Scikit-Learn. Slope: {m_sklearn}. Intercept: {b_sklearn}")
```
Let test `lr_sklearn` on tv dataset. however before we start:
+  **scikit-learn, expect the input data to be in a 2-dimensional array format** where **rows represent samples and columns represent features**.
	So we use `np.newaxis` to **increase the dimension of the existing array by 1 more dimension**, thus **1D** array will become **2D** array, **2D** array will become **3D** array and so on.
	(**Row Vector:** 1 row, 4 column; **Column Vector:** 4 row, 1 column)
	![[Pasted image 20240925152517.png]]
```python
def pred_sklearn(X, lr_sklearn):
	# convert 1D into 2D array
    X_2D = X[:, np.newaxis] # with X as value for each row insert a axis
    Y = lr_sklearn.predict(X_2D)
    
    return Y
```

```python
test_tv = np.array([50, 100, 150, 200, 300, 350, 400, 450])
Y_pred_sklearn = pred_sklearn(test_tv, lr_sklearn)

print(f"TV marketing expenses:\n{test_tv}")
print(f"Predictions of sales using Scikit_Learn linear regression:\n{Y_pred_sklearn.T}")
```
**output:** - yay, the result are the same as above
```python
X_2D:
 [[50]
 [100]
 [150]
 [200]
 [300]
 [350]
 [400]
 [450]]
TV marketing expenses:
[ 50 100 150 200 300 350 400 450]
Predictions of sales using Scikit_Learn linear regression:
[[ 9.40942557 11.78625759 14.16308961 16.53992164 21.29358568 23.6704177
  26.04724972 28.42408174]]
```

## 3 - Linear Regression using Gradient descent
+ Explain why division by 2 -> Visualize the process -> name for that process? normalization?