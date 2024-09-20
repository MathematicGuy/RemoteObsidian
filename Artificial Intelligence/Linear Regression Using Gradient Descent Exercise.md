```ad-success
In this Note we will exploring how to **Applying Linear Regression and Gradient Descent** to **Predict Sales by TV Marketing Expenses**
```

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

Before starting, we need to find the polynomial that fit to the graph/data points. "Tìm đa thực cho đồ thị"/"các điểm trên". We could use `np.polyfit` from numpy to finds the coefficients (hệ số) of a [[polynomial]] (đa thức mũ 2) using [[Least Squares Method]] (basically **find m and b of a polynomial)**.
```python
import numpy as np
import matplotlib.pyplot as plt

# Example data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 2, 3.5, 3.8, 5.1])

# Perform a linear fit
m_numpy, b_numpy = np.polyfit(X, Y, 1)

# Generate the fitted line
fitted_line = m_numpy * X + b_numpy

# Plot the data points and the fitted line
plt.scatter(X, Y, color='red', label='Data Points')
plt.plot(X, fitted_line, label=f'Fit: y = {m_numpy:.2f}x + {b_numpy:.2f}', color='blue')
plt.legend()
plt.show()
```

