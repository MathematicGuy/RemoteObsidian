### Understanding Derivatives in 2D (for $x$ and $y$):

For a function $f(x, y)$ that takes two inputs (like $x$ and $y$) and gives two outputs (like $f_1(x, y)$ and $f_2(x, y)$), we want to understand how small changes in the inputs $x$ and $y$ affect the outputs. This is where **partial derivatives** come into play.

#### 1. **Partial Derivative with Respect to $x$:**

- **Definition**: The partial derivative $\frac{\partial f_1}{\partial x}$ tells you how **the output $f_1(x, y)$ changes** when you make **a small change in the $x$-coordinate, while keeping the $y$-coordinate fixed.**
	
- **Interpretation**: It captures the **rate of change** of the function in the **horizontal direction** (along the $x$-axis). Similarly, $\frac{\partial f_2}{\partial x}$ does the same for the second output $f_2(x, y)$.

#### 2. **Partial Derivative with Respect to $y$:**

- **Definition**: The partial derivative $\frac{\partial f_1}{\partial y}$ tells you how **the output $f_1(x, y)$ changes** when you make **a small change in the $y$-coordinate, while keeping the $x$-coordinate fixed.**
	
- **Interpretation**: It captures the **rate of change** of the function in the **vertical direction** (along the $y$-axis). Similarly, $\frac{\partial f_2}{\partial y}$ does the same for the second output $f_2(x, y)$.

### How These Derivatives Help in Approximating the Function:

When you want to approximate how a function $f(x, y)$ behaves near a point $(a, b)$, you use these **partial derivatives** to construct a **linear approximation** that tells you how the function responds to small changes in $x$ and $y$.

- **In 2D**:
  - **$\frac{\partial f_1}{\partial x}$** and **$\frac{\partial f_1}{\partial y}$** describe how the first output of the function $f_1(x, y)$ changes as $x$ and $y$ vary.
  - **$\frac{\partial f_2}{\partial x}$** and **$\frac{\partial f_2}{\partial y}$** describe how the second output of the function $f_2(x, y)$ changes as $x$ and $y$ vary.

By combining these partial derivatives into a **Jacobian matrix**, you can linearly approximate how **both outputs** change with respect to small changes in the **input variables** $x$ and $y$.

### Example:
Suppose you have a function $f(x, y)$ that maps points in 2D space to another 2D space, with two outputs:

$$
f(x, y) = (f_1(x, y), f_2(x, y))
$$

- To approximate how the function behaves near the point $(a, b)$, we look at the **rate of change** (derivatives) of $f_1$ and $f_2$ with respect to $x$ and $y$.

- The **Jacobian matrix** **collects these rates of change:**

$$
J(a, b) = \begin{pmatrix} 
\frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\
\frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y} 
\end{pmatrix}
$$

- This matrix gives the **best linear approximation** of the function near $(a, b)$. Small changes in $x$ and $y$ can now be **approximated** by multiplying the change vector $\Delta x$ and $\Delta y$ by the Jacobian matrix.


### Why Does This Work?

The **derivatives** capture the **instantaneous rate of change** of the function in both the $x$-direction and the $y$-direction (i.e. rate of change at a given point). Since these derivatives tell us how the function is changing locally, they allow us to construct a **linear model** (the Jacobian matrix) that approximates how the function behaves around a point. 

In higher dimensions, the same idea holds: the **partial derivatives with respect to each input dimension** (e.g., $x$, $y$, $z$, etc.) tell us how the function changes in each direction, and combining these derivatives into a matrix (the Jacobian) gives us the best **linear approximation** of the function near that point.

### Conclusion:

The **derivatives with respect to the $x$ and $y$ coordinates** help **approximate the function because they describe the rate of change** in the **horizontal and vertical directions**. By **using these rates of change, we can construct** a **linear map** (the Jacobian matrix) that **provides a close approximation to the function near a given point** $(a, b)$. This approximation becomes particularly important when dealing with higher dimensions, where visualizing or working directly with the function is more complex.

> (Dựng bản đồ tuyến tính (Ma Trận Jacobian) xấp xỉ với hàm được cho gần điểm (a, b))
> -> Quan trọng để giúp miêu tả các chiều không gian cao hơn hoặc khi làm việc với các hàm phức tạp. 
> -> Ma trận Jacobian là công cụ giúp xấp xỉ tuyến tính các hàm đa biến xung quanh một điểm cụ thể trong không gian, cho chúng ta cái nhìn về cách [[hàm biến đổi cục bộ]] tại điểm đó.


