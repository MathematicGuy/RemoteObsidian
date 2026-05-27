---
category: "3_RESOURCES/Artificial Intelligent/Deep Learning/Gradient-Descent-Derivations.md"
summary: "Proves convergence bounds for gradient descent on L-smooth convex functions. Demonstrates maximum decrease bounds by setting learning rate to 1/L."
keywords: ["gradient descent", "convex optimization", "convergence analysis"]
confidence: "high"
analyzed_at: "2026-05-27T16:31:06.209645+00:00"
---
# Gradient Descent Derivations

Mathematical proof and derivations for gradient descent optimization algorithms, focusing on convex optimization limits and learning rate bounds.

## Definition
Let $f: \mathbb{R}^d \to \mathbb{R}$ be a continuously differentiable, L-smooth convex function.
The update step is:
$$x_{k+1} = x_k - \eta \nabla f(x_k)$$

## Convergence Analysis
For an L-smooth function, the gradient step satisfies:
$$f(x_{k+1}) \le f(x_k) - \eta \left(1 - \frac{\eta L}{2}\right) \|\nabla f(x_k)\|^2$$
By setting $\eta = \frac{1}{L}$, we get maximum decrease per step:
$$f(x_{k+1}) \le f(x_k) - \frac{1}{2L} \|\nabla f(x_k)\|^2$$
This guarantees linear convergence for strongly convex functions.
