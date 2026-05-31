
Out of the box, linear regression provides a means of building models of the form:
$$f_{\mathbf{w},b} = w_0x_0 + w_1x_1+ ... + w_{n-1}x_{n-1} + b \tag{1}$$ 
What if your features/data are non-linear or are combinations of features ? For example,  Housing prices do not tend to be linear with living area but penalize very small or very large houses resulting in the curves shown in the graphic above. Answer is Feature Scaling which is the ability to modify parameter $w, b$ in $(1)$ to 'fit' the equation to the training data.

## Polynomial Features
As for non-linear data $y = 1 + x^2$ obsivously would not fit. 
```python
# create target data
x = np.arange(0, 20, 1)
y = 1 + x**2
X = x.reshape(-1, 1)

model_w,model_b = run_gradient_descent_feng(X,y,iterations=1000, alpha = 1e-2)

plt.scatter(x, y, marker='x', c='r', label="Actual Value"); plt.title("no feature engineering")
plt.plot(x,X@model_w + model_b, label="Predicted Value");  plt.xlabel("X"); plt.ylabel("y"); plt.legend(); plt.show()
```
![[Pasted image 20241016143914.png]]

What we need is a weight multiply $x^2$ or a **polynomial feature**. 
```python
# create target data
x = np.arange(0, 20, 1)
y = 1 + x**2

# Engineer features 
X = x**2    #<-- added engineered featur

X = X.reshape(-1, 1)  #X should be a 2-D Matrix (n, 1) - n rows and 1 col
model_w,model_b = run_gradient_descent_feng(X, y, iterations=10000, alpha = 1e-5)

plt.scatter(x, y, marker='x', c='r', label="Actual Value"); plt.title("Added x**2 feature")
plt.plot(x, np.dot(X,model_w) + model_b, label="Predicted Value"); plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.show()
```
![[Pasted image 20241016145712.png]]

### Selecting Feature
> One could add variety of potential features to try and find the most useful
```python
# create target data
x = np.arange(0, 20, 1)
y = x**2

# engineer features .
X = np.c_[x, x**2, x**3]   #<-- added engineered feature

model_w,model_b = run_gradient_descent_feng(X, y, iterations=10000, alpha=1e-7)

plt.scatter(x, y, marker='x', c='r', label="Actual Value"); plt.title("x, x**2, x**3 features")
plt.plot(x, X@model_w + model_b, label="Predicted Value"); plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.show()
```
![[Pasted image 20241016145833.png]]
> As we can see value $\mathbf{w}$ = `[0.08 0.54 0.03]` and b is `0.0106`. This implies the model after fitting/training is: $$0.08𝑥+0.54𝑥2+0.03𝑥3+0.0106$$

Gradient descent has emphasized the data that is the best fit to the 𝑥2 data by increasing the 𝑤1 term relative to the others. If you were to run for a very long time, it would continue to reduce the impact of the other terms.
+ $ Gradient descent is picking the 'correct' features for us by emphasizing its associated parameter
This mean:
+ **Less Weight** value **implies less important/correct feature**. In extreme case, weight ~ 0 is not useful in fitting the model to the data.
+ Above, after fitting, the **weight associated with the $x^2$ feature is much larger** than the weights for $x$ or $x^3$ as it is the **most useful in fitting the data.**

### Scaling features
> If the data set has features with significantly different scales, one should apply feature scaling to speed gradient descent. Let apply Z-Score to our example:
```python
# create target data
x = np.arange(0,20,1)
X = np.c_[x, x**2, x**3]
print(f"Peak to Peak range by column in Raw X:{np.ptp(X,axis=0)}")

# add mean_normalization 
X = zscore_normalize_features(X)     
print(f"Peak to Peak range by column in Normalized X:{np.ptp(X,axis=0)}")
```
![[Pasted image 20241016150642.png]]
```python
x = np.arange(0,20,1)
y = x**2

X = np.c_[x, x**2, x**3]
X = zscore_normalize_features(X) 

model_w, model_b = run_gradient_descent_feng(X, y, iterations=100000, alpha=1e-1)

plt.scatter(x, y, marker='x', c='r', label="Actual Value"); plt.title("Normalized x x**2, x**3 feature")
plt.plot(x,X@model_w + model_b, label="Predicted Value"); plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.show()
```
![[Pasted image 20241016150658.png]]
> Feature scaling allows this to **converge much faster**. 
> Note again the values of 𝐰. The $𝑤_1$ term, which is the $x^2$ term is the most emphasized. Gradient descent has all but eliminated the $x^3$ term.


### Complex Functions
With Feature Engineering, complex function can be modeled 
```python
x = np.arange(0,20,1)
y = np.cos(x/2)

X = np.c_[x, x**2, x**3,x**4, x**5, x**6, x**7, x**8, x**9, x**10, x**11, x**12, x**13]
X = zscore_normalize_features(X) 

model_w,model_b = run_gradient_descent_feng(X, y, iterations=1000000, alpha = 1e-1)

plt.scatter(x, y, marker='x', c='r', label="Actual Value"); plt.title("Normalized x x**2, x**3 feature")
plt.plot(x,X@model_w + model_b, label="Predicted Value"); plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.show()
```
![[Pasted image 20241016150821.png]]

