It is possible to evaluate the symbolic functions for each element of the array, but you need to make a function `NumPy`-friendly first:
```python
from sympy.utilities.lambdify import lambdify

f_symb_numpy = lambdify(x, f_symb, 'numpy')
```

```python
print("x: \n", x_array)
print("f(x) = x**2: \n", f_symb_numpy(x_array))
""" output
x: 
 [1 2 3]
f(x) = x**2: 
 [1 4 9]
"""
```

```python

```

```python

```

```python

```

```python

```

