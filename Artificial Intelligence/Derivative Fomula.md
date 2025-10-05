# List of Derivative Formulas

## Basic Derivatives

### Constants and Powers

- Derivative of a constant function:

  $$
  \frac{d}{dx} (c) = 0
  $$

- Power rule:

  $$
  \frac{d}{dx} (x^n) = n x^{n-1}
  $$

### Exponential and Logarithmic Functions

- Derivative of the natural exponential function:

  $$
  \frac{d}{dx} (e^x) = e^x
  $$

- Derivative of the natural logarithm:

  $$
  \frac{d}{dx} (\ln x) = \frac{1}{x}
  $$

- Derivative of an exponential function with base $a$:

  $$
  \frac{d}{dx} (a^x) = a^x \ln a
  $$

- Derivative of a logarithm with base $a$:

  $$
  \frac{d}{dx} (\log_a x) = \frac{1}{x \ln a}
  $$

### Trigonometric Functions

- $$
  \frac{d}{dx} (\sin x) = \cos x
  $$

- $$
  \frac{d}{dx} (\cos x) = -\sin x
  $$

- $$
  \frac{d}{dx} (\tan x) = \sec^2 x
  $$

- $$
  \frac{d}{dx} (\cot x) = -\csc^2 x
  $$

- $$
  \frac{d}{dx} (\sec x) = \sec x \tan x
  $$

- $$
  \frac{d}{dx} (\csc x) = -\csc x \cot x
  $$

### Inverse Trigonometric Functions

- $$
  \frac{d}{dx} (\arcsin x) = \frac{1}{\sqrt{1 - x^2}}
  $$

- $$
  \frac{d}{dx} (\arccos x) = -\frac{1}{\sqrt{1 - x^2}}
  $$

- $$
  \frac{d}{dx} (\arctan x) = \frac{1}{1 + x^2}
  $$

- $$
  \frac{d}{dx} (arccot x) = -\frac{1}{1 + x^2}
  $$

- $$
  \frac{d}{dx} (arcsec x) = \frac{1}{|x| \sqrt{x^2 - 1}}
  $$

- $$
  \frac{d}{dx} (arccsc x) = -\frac{1}{|x| \sqrt{x^2 - 1}}
  $$

### Hyperbolic Functions
$$
  \frac{d}{dx} (\sinh x) = \cosh x
$$

$$
  \frac{d}{dx} (\cosh x) = \sinh x
$$

$$
  \frac{d}{dx} (\tanh x) = \text{sech}^2 x$$

- $$
  \frac{d}{dx} (\coth x) = -\text{csch}^2 x
  $$

- $$
  \frac{d}{dx} (\text{sech}\, x) = -\text{sech}\, x\, \tanh x
  $$

- $$
  \frac{d}{dx} (\text{csch}\, x) = -\text{csch}\, x\, \coth x
  $$

### Inverse Hyperbolic Functions

- $$
  \frac{d}{dx} (\sinh^{-1} x) = \frac{1}{\sqrt{x^2 + 1}}
  $$

- $$
  \frac{d}{dx} (\cosh^{-1} x) = \frac{1}{\sqrt{x^2 - 1}}
  $$

- $$
  \frac{d}{dx} (\tanh^{-1} x) = \frac{1}{1 - x^2}
  $$

- $$
  \frac{d}{dx} (\coth^{-1} x) = \frac{1}{1 - x^2}
  $$

- $$
  \frac{d}{dx} (\text{sech}^{-1} x) = \frac{-1}{x \sqrt{1 - x^2}}
  $$

- $$
  \frac{d}{dx} (\text{csch}^{-1} x) = \frac{-1}{|x| \sqrt{1 + x^2}}
  $$

## Rules of Differentiation

### Sum Rule

- $$
  \frac{d}{dx} [f(x) + g(x)] = f'(x) + g'(x)
  $$

### Difference Rule

- $$
  \frac{d}{dx} [f(x) - g(x)] = f'(x) - g'(x)
  $$

### Product Rule

- $$
  \frac{d}{dx} [f(x) \cdot g(x)] = f'(x) g(x) + f(x) g'(x)
  $$
 
### Quotient Rule

- $$
  \frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x) g(x) - f(x) g'(x)}{[g(x)]^2}
  $$

### Chain Rule

- $$
  \frac{d}{dx} [f(g(x))] = f'(g(x)) \cdot g'(x)
  $$

| wx + b - y | -> (wx + b - y) / | wx + b - y |  


## Other Useful Formulas

- Derivative of the absolute value function:

  $$
  \frac{d}{dx} |x| = \frac{x}{|x|}
  $$

  (for $x \ne 0$)

- Derivative of the square root function:

  $$
  \frac{d}{dx} (\sqrt{x}) = \frac{1}{2\sqrt{x}}
  $$

- Derivative of $\ln |x|$:

  $$
  \frac{d}{dx} [\ln |x|] = \frac{1}{x}
  $$

- Derivative of $a x$ (where $a$ is a constant):

  $$
  \frac{d}{dx} (a x) = a
  $$

- Derivative of a constant multiplied by a function:

  $$
  \frac{d}{dx} [a \cdot f(x)] = a \cdot f'(x)
  $$

- Derivative of an implicit function (using implicit differentiation):

  If $F(x, y) = 0$, then:

  $$
  \frac{dy}{dx} = -\frac{\partial F/\partial x}{\partial F/\partial y}
  $$

## Second Derivatives

- Second derivative of a function $f(x)$:

  $$
  \frac{d^2 y}{dx^2} = \frac{d}{dx} \left( \frac{dy}{dx} \right)
  $$

## Higher-Order Derivatives

- $n$-th derivative of $x^n$:

  $$
  \frac{d^n}{dx^n} (x^n) = n!
  $$

  (for integer $n \geq 0$)
