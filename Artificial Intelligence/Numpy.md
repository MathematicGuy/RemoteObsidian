
What if you wanted to create an array with five evenly spaced values in the interval from 0 to 100?
```python
lin_spaced_arr = np.linspace(0, 100, 5)
print(lin_spaced_arr)
```
[  0.  25.  50.  75. 100.]



## Create Matrix through List

```python
import numpy as np
from utils import plot_lines

# 1-D array 
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(
	one_dim_arr, # the array to be reshaped
	(2,3) # dimensions of the new array
)
# Print the new 2-D array with two rows and three columns
print(multi_dim_arr)
```


## 1.4 - More on NumPy arrays[](https://ltncnkhnkdth.labs.coursera.org/notebooks/C1_W1_Lab_1_introduction_to_numpy_arrays.ipynb#1.4---More-on-NumPy-arrays)

One of the advantages of using NumPy is that you can easily create arrays with built-in functions such as:

- `np.ones()` - Returns a new array setting values to one.
- `np.zeros()` - Returns a new array setting values to zero.
- `np.empty()` - Returns a new uninitialized array.
- `np.random.rand()` - Returns a new array with values chosen at random.


## 2.1 - Finding size, shape and dimension.[](https://ltncnkhnkdth.labs.coursera.org/notebooks/C1_W1_Lab_1_introduction_to_numpy_arrays.ipynb#2.1---Finding-size,-shape-and-dimension.)

In future assignments, you will need to know how to find the size, dimension and shape of an array. These are all atrributes of a `ndarray` and can be accessed as follows:

- `ndarray.ndim` - Stores the number dimensions of the array.
- `ndarray.shape` - Stores the shape of the array. Each number in the tuple denotes the lengths of each corresponding dimension.
- `ndarray.size` - Stores the number of elements in the array.




