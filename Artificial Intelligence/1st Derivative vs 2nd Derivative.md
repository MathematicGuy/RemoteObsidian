### 1st Derivative and 2nd Derivative
```ad-summary
**firsts derivative:** represent the slope of a function at a given point.

**second derivative:** represent the rate of change of the gradient. 
	+ **positive** mean **the gradient is increasing**, suggest the **function is curving upward.**
	+ **negative** mean the **gradient is decreasing**, suggest the **function is curving downward.**

**By considering curvative infor provided by the 2nd derivative, the algo can adjust step size during update:**
+ Gradient increasing, the algorithm adjust step size during updates to avoid over shoot the minimum.
+ Gradient decrease, large step can be taken to accelerate convergence.
```


#### 1st Derivative: Rate of Change

The **first derivative** of a function describes the **rate of change** or the **slope** of the function at any given point. It tells us how the function's value changes as the input changes. For a function f(x)f(x)f(x):

- The **first derivative** is denoted by f′(x)f'(x)f′(x) or dfdx\frac{df}{dx}dxdf​.
- It provides the **instantaneous rate of change** of the function with respect to the variable xxx.
- If f′(x)>0f'(x) > 0f′(x)>0, the function is **increasing** at that point.
- If f′(x)<0f'(x) < 0f′(x)<0, the function is **decreasing** at that point.
- If f′(x)=0f'(x) = 0f′(x)=0, the function has a **critical point**, which could be a local maximum, a local minimum, or a saddle point.

For example, if we have f(x)=x2f(x) = x^2f(x)=x2, the first derivative is:

f′(x)=2xf'(x) = 2xf′(x)=2x

This means that the rate of change of f(x)f(x)f(x) depends on xxx; it increases as xxx moves away from 0.

#### 2nd Derivative: Concavity and Curvature

The **second derivative** of a function is the **derivative of the first derivative**. It tells us how the **rate of change** itself is changing, which relates to the **concavity** and **curvature** of the function.

- The **second derivative** is denoted by f′′(x)f''(x)f′′(x) or d2fdx2\frac{d^2f}{dx^2}dx2d2f​.
- It provides information about the **curvature** of the function.
    - If f′′(x)>0f''(x) > 0f′′(x)>0, the function is **concave up** at that point, meaning it curves upwards like a "cup" (a local minimum may exist).
    - If f′′(x)<0f''(x) < 0f′′(x)<0, the function is **concave down** at that point, meaning it curves downwards like a "cap" (a local maximum may exist).
    - If f′′(x)=0f''(x) = 0f′′(x)=0, the point could be an **inflection point**, where the concavity changes.

For the same example f(x)=x2f(x) = x^2f(x)=x2:

f′′(x)=2f''(x) = 2f′′(x)=2

This tells us that the function is always **concave up**, meaning it has a parabolic shape that opens upward.

### Why the 2nd Derivative Describes a Parabola

The **second derivative** only perfectly describes a **parabola** when dealing with a **quadratic function**. To understand why, let's look at the nature of quadratic functions and higher-order derivatives.

#### Quadratic Function and Parabola

A **quadratic function** is of the form:

f(x)=ax2+bx+cf(x) = ax^2 + bx + cf(x)=ax2+bx+c

Its **first derivative** is:

f′(x)=2ax+bf'(x) = 2ax + bf′(x)=2ax+b

Its **second derivative** is:

f′′(x)=2af''(x) = 2af′′(x)=2a

The second derivative of a quadratic function is **constant** (2a2a2a), meaning the rate of change of the slope is always the same. This constant rate of change in slope is what gives the quadratic function its **parabolic shape**.

- If a>0a > 0a>0, the parabola opens **upward** (concave up).
- If a<0a < 0a<0, the parabola opens **downward** (concave down).
- The second derivative being constant implies that the curvature does not change — hence, it always curves consistently, which is the defining property of a parabola.

#### Higher-Order Polynomials

For **higher-order polynomials** (e.g., cubic, quartic), the second derivative is not constant. It changes as the input changes, which means the curvature of the graph changes throughout, leading to more complex shapes that are not simple parabolas.

- For instance, a **cubic function** like f(x)=x3f(x) = x^3f(x)=x3 has a second derivative of f′′(x)=6xf''(x) = 6xf′′(x)=6x, which changes depending on xxx. This varying second derivative gives the graph of a cubic function an **inflection point** where the concavity changes.

### Summary

- The **first derivative** gives the **rate of change** or **slope** of the function.
- The **second derivative** gives information about the **concavity** or **curvature**.
- For a **quadratic function**, the **second derivative is constant**, which gives rise to a **parabolic shape**.
- Higher-order functions have **changing second derivatives**, resulting in more complex and varied curves, not just parabolas.


	