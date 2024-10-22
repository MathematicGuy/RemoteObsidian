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
(note: normalized data using Least Square Method)
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
Let's try to find linear regression coefficients $m$ and $b$, by minimising the difference between original values $y^{(i)}$ and predicted values $\hat{y}^{(i)}$ with the **loss function** $L\left(w, b\right)  = \frac{1}{2}\left(\hat{y}^{(i)} - y^{(i)}\right)^2$ for each of the training examples. [[Division by 2 is taken just for scaling purposes]] for calculating partial derivatives. 

To compare the resulting vector of the predictions $\hat{Y}$ with the vector $Y$ of original values $y^{(i)}$, you can take an average of the **loss function values** for each of the training examples:
  

$$E\left(m, b\right) = \frac{1}{2n}\sum_{i=1}^{n} \left(\hat{y}^{(i)} - y^{(i)}\right)^2 =

\frac{1}{2n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)^2,\tag{1}$$


where $n$ is a number of data points. This function is called the sum of squares **cost function**. To use gradient descent algorithm, calculate partial derivatives as:
+ $ Goal: Minimize Cost using Cost Function. For cost function with multi-variable, we calc the derivative with respect to every variables. (i.e. $W, b$. where $W=[w_{1}, w_{2}, \space \dots, w_{n}], b=[b_{1}, b_{2},\dots, b_{n}]$) 
+ ? Because **Partial Derivative Derive from Cost Function** it calc the average **partial derivative** w.r.t all given variables for all point.  
  
$$
\begin{align}

\frac{\partial E }{ \partial m } &=

\frac{1}{n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)x^{(i)},\\

\frac{\partial E }{ \partial b } &=

\frac{1}{n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right),

\tag{2}\end{align}$$

and update the parameters iteratively using the expressions
$$\begin{align}

m &= m - \alpha \frac{\partial E }{ \partial m },\\

b &= b - \alpha \frac{\partial E }{ \partial b },

\tag{3}\end{align}$$
where $\alpha$ is the learning rate.


Original arrays `X` and `Y` have different units. To make gradient descent algorithm efficient, you need to bring them to the same units. A common approach to it is called **normalization**: substract the mean value of the array from each of the elements in the array and divide them by [[standard deviation]] (a statistical measure of the amount of dispersion of a set of values) - (đo lường xác suất sự phân tán của 1 tập giá trị).
+ **Large values of x or y** can produce **large gradients**, causing the gradient descent algorithm to take **large steps** in certain directions.
- **Small values of x or y** can produce **small gradients**, resulting in **small steps** in other directions.
- **Unbalance value of x and y** can cause gradient descent algorithm to take **disproportionate steps** (bước đi không cân xứng) in each direction **(i.e. small step in x-axis, large step in y_axis)**  which leads to **inefficienct convergence** or even **divergence**. 
```python
X_norm = (X - np.mean(X))/np.std(X)
Y_norm = (Y - np.mean(Y))/np.std(Y)
```
X_norm and Y_norm value look like this
```python
print("X_norm:",X_norm)
print("Y_norm:",Y_norm)
```
> **X_norm:** [ 0.96985227 -1.19737623 -1.51615499 0.05204968 0.3941822 -1.61540845 -1.04557682 -0.31343659 -1.61657614 0.61604287 .... ]
> **Y_norm:** [ 1.55205313 -0.69604611 -0.90740587 0.86033029 -0.21568303 -1.31091086 -0.42704278 -0.15803946 -1.77205942 -0.65761706 ... ]


### Implement code
##### Define Cost Function
```python
def E(m, b, X, Y):
    return 1/(2*len(Y)) * np.sum((m*X + b - Y)**2)
```

##### Define Partial Derivative of the Cost Function
```python
def dEdm(m, b, X, Y):
    n = len(Y)
    #? 2 options, same result
    # re = 1/n * sum((m*X +b - Y) * X)
    re = 1/n * np.dot(m*X +b - Y, X) 

    return re

def dEdb(m, b, X, Y):
    n = len(Y)
    re = 1/n * np.dot(m*X + b - Y, Y**0)
    return re
```

##### Implement Gradient Descent to find m and b with Partial Derivative of Cost Function
$$
\begin{align}
m &= m - \alpha \frac{\partial E }{ \partial m },\\
b &= b - \alpha \frac{\partial E }{ \partial b },
\end{align}
$$
```python
def gradient_descent(X, Y, m, b, learning_rate=0.002, iteration=30, print_cost=False):
    '''
        X: dataset use to predict
        Y: predicted dataset 
        m: slope 
        b: y-intercept
        
    '''
    for i in range(iteration):
        m_new = m - learning_rate*dEdm(m ,b, X, Y)
        b_new = b - learning_rate*dEdb(m ,b, X, Y)
            
        m = m_new
        b = b_new
        
        if print_cost is True:
            print(f"Cost Function after {i} iteration:", E(m, b, X, Y))
    
    return m ,b
```
##### Choose a initial point for m and b and test
```python
m_initial = 0; b_initial = 0; iteration = 30; learning_rate = 1.2

m_gd, b_gd = gradient_descent(X_norm, Y_norm, m_initial, b_initial, learning_rate, iteration, print_cost=True)
```

### Verification
```python
X_pred = test_tv
# Use the same mean and standard deviation of the original training array X
X_pred_norm = (X_pred - np.mean(X))/np.std(X)
Y_pred_gd_norm = m_gd * X_pred_norm + b_gd
# Use the same mean and standard deviation of the original training array Y
Y_pred_gd = Y_pred_gd_norm * np.std(Y) + np.mean(Y)

print(f"TV marketing expenses:\n{X_pred}")
print(f"Predictions of sales using Scikit_Learn linear regression:\n{Y_pred_sklearn.T}")
print(f"Predictions of sales using Gradient Descent:\n{Y_pred_gd}")
```
>output. yes, they are correct
```python
TV marketing expenses:
[ 50 100 150 200 300 350 400 450]
Predictions of sales using Scikit_Learn linear regression:
[[ 9.40942557 11.78625759 14.16308961 16.53992164 21.29358568 23.6704177
  26.04724972 28.42408174]]
Predictions of sales using Gradient Descent:
[ 9.40942557 11.78625759 14.16308961 16.53992164 21.29358568 23.6704177
 26.04724972 28.42408174]
```

