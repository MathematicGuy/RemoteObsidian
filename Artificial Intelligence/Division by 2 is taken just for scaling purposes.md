In the context of linear regression and gradient descent optimization, the cost function is defined as:
$$E\left(m, b\right) = \frac{1}{2n}\sum_{i=1}^{n} \left(\hat{y}^{(i)} - y^{(i)}\right)^2 =
\frac{1}{2n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)^2,\tag{1}$$

Say we **divided by 2**, the function will be **simplified without effecting the final result as we can just mul by 2 after**. Without 2, ours **partial derivative can be calculated more easily since gradient descent is all about getting closer to a expected value** (the more origin the function are, the easier to calculate)
+ **Partial Derivative with Respect to $m$:**
	$$
	\frac{\partial E}{\partial m} = \frac{1}{2n}. 2\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)x^{(i)}   = \frac{1}{n} \sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)x^{(i)}   
	$$

+ **Partial Derivative with Respect to $b$:**
	$$
	\frac{\partial E}{\partial b} = \frac{1}{2n}. 2\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right) = \frac{1}{n} \sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)
	$$


### Example:

Suppose we have a single training example for simplicity:

- $ x^{(1)} = 2 $
- $y^{(1)} = 5$
- Initial parameters: $m = 0,\space b = 0$
- Learning rate: $alpha = 0.1$


---

### Without Division by 2:

- **Cost function**: 
$$E' = (mx^{(1)} + b - y^{(1)})^2$$
  
- **Partial derivatives**:

$$ \frac{\partial E'}{\partial m} = 2(mx^{(1)} + b - y^{(1)}) x^{(1)} = 2(0 + 0 - 5)(2) = -20$$

$$\frac{\partial E'}{\partial b} = 2(mx^{(1)} + b - y^{(1)}) = 2(0 + 0 - 5) = -10$$

- **Gradient descent updates**:
	$m_{\text{new}} = 0 - 0.1 \times (-20) = 2$
	$b_{\text{new}} = 0 - 0.1 \times (-10) = 1$
  

---

### With Division by 2:

- **Cost function**:   $$E = \frac{1}{2} (mx^{(1)} + b - y^{(1)})^2$$  
- **Partial derivatives**:
  $$\frac{\partial E}{\partial m} = (mx^{(1)} + b - y^{(1)}) x^{(1)} = (0 + 0 - 5)(2) = -10$$
  $$\frac{\partial E}{\partial b} = (mx^{(1)} + b - y^{(1)}) = (0 + 0 - 5) = -5$$

- **Gradient descent updates**:
	$m_{\text{new}} = 0 - 0.1 \times (-10) = 1$
	$b_{\text{new}} = 0 - 0.1 \times (-5) = 0.5$


### Conclusion:

- Without division by 2, the gradient steps are larger due to the extra factor of 2.
- With division by 2, the steps are smaller and may lead to more stable convergence depending on the learning rate.
