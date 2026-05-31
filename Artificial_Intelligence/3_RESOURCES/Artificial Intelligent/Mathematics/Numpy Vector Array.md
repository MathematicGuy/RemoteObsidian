
### Numpy Axes
#### Array Axes
![[Pasted image 20240925175247.png]]

#### How to think about array axes
ANY VALUE IN AN ARRAY CAN BE IDENTIFIED BY ITS POSITION ALONG THE AXES
> **Axis and indexes in python always start at 0**. So 7 will be at
> + position 1 axis 0: y-1
> + position 2 axis 1: x-2
![[Pasted image 20240925175555.png]]

#### 1D vs 2D array 
>The first axis start with 0. So 1D will be at axis 0
![[Pasted image 20240925180102.png]]
>And 2D will have both axis 0 long the y-axis and 1 along the x-axis
![[Pasted image 20240925180135.png]]

---

```ad-abstract
Vector array is a Matrix represent under array of vectors. For instant

$M = \begin{pmatrix} 1,2,3 \ \\ 4,5,6 \end{pmatrix}$

will be represent as M = `[[1,2,3], [4,5,6]]` with the outside square blanket alert it a numpy array, and inner blanket represent each vector or row of the matrix. `Ex: row-0, col-0 valus is 1`
```
+ ? Many vector combined create a Matrix. 

## 1D Vector
```python
import numpy as np
arr_1d = np.array([1, 2, 3])
print(arr_1d.shape)  # Output: (3,)
```

## 2D Vector
```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.shape)  # Output: (2, 3)
```

## 3D Vector 
```python
# A 3D array containing two 2D arrays
arr_3d = np.array([ [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])

print(arr_3d)
print(arr_3d.shape)  # Output: (2, 2, 3)
```


---

### Increase Dimension of an Array using `np.newaxis`
> This tool is helpful for reshaping arrays for broadcasting, matrix operations, and handling data in higher dimensions.
```ad-note
#### **Revision**
Each value in a matrix (or array) is represented by coordinates **x** and **y**, depending on its dimensionality. In NumPy, the dimensions of an array are referred to as **axes**, with indexing starting from **axis 0**. Here’s how each axis corresponds to different dimensions:

- **Axis-0** represents the vertical axis, which corresponds to the **y-dimension** (rows).
- **Axis-1** represents the horizontal axis, which corresponds to the **x-dimension** (columns).
- **Axis-2** represents the depth of the array, corresponding to the **z-dimension** (used in 3D arrays).
- We’ll ignore higher dimensions for now, but the same pattern continues for higher-dimensional arrays.

#### **Axes Levels in NumPy Arrays**

- **Axis-0** is the outermost structure, representing the entire array or the first level of the array.
    
- **Axis-n** (the deepest axis) represents the innermost elements, which are individual values or vectors at that level.
    
    The deeper the axis, the more detailed and specific the representation becomes. For example, in a 3D array, **axis-2** represents the depth (z-dimension), while **axis-1** and **axis-0** represent rows and columns, respectively. 
```
**Key Insight**: Higher-dimensional arrays are created by stacking lower-dimensional arrays.

#### Examples:

**1D Array**: A 1D array is a single sequence of numbers, with no notion of rows or columns.
```python
[1, 2, 3]
```
	
**2D Array**: A 2D array contains multiple **1D arrays** stacked together, forming rows and columns.
```python
[[1, 2, 3], 
 [4, 5, 6]]
```
+ Here, **axis-0** is the row (vertical/y-axis) and **axis-1** is the column (horizontal/x-axis).
	
 **3D Array**: A 3D array contains multiple **2D arrays**, stacked along a third dimension (depth).
```python
[
 [[1, 2], 
   [3, 4]], 
  
  [[5, 6], 
  [7, 8]]
]
```
- **Axis-0**: The outermost bracket, representing 2 stacked 2D arrays.
- **Axis-1**: Represents rows inside each 2D array.
- **Axis-2**: Represents the columns or values inside each row.
	
 **4D Array**: A 4D array contains multiple **3D arrays** stacked together.
```python
[
	[ 
		[ [1, 2] #1D, [3, 4] ], #2D 
	    [ [5, 6], [7, 8] ]
	], #3D
  
	[
	   [ [9, 10], [11, 12] ], 
	   [ [13, 14], [15, 16] ]
	]
] #4D
```
- **Axis-0**: The outermost bracket, representing 2 sets of 3D arrays.
- **Axis-1**: Represents each 3D array.
- **Axis-2**: Represents rows within each 3D array.
- **Axis-3**: Represents individual values or columns.


####  With a 1D Array
```python
import numpy as np

arr_1d = np.array([1, 2, 3])
print(arr_1d.shape)  # Output: (3,)
```
Applying `np.newaxis`:
+ **Convert to 2D row vector:**
```python
arr_row = arr_1d[np.newaxis, :] # arr_1d[row, col]
print(arr_row.shape)  # Output: (1, 3)
print(arr_row)        # [[1 2 3]]
```
> the code translate to for each row inserting an axis: `[]`  
+ **Convert to a 2D row vector**:
```python
arr_row = arr_1d[:, np.newaxis] #arr_1d[row, col]
print(arr_row.shape)  # Output: (1, 3)
print(arr_row)        # [[1 2 3]]
```
> for each column inserting an axis: `[]`

####  With a 2D Array
> A 2D array has 2 axes (rows and columns):
```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.shape)  # Output: (2, 3)
```
Applying `np.newaxis`:
+ **Expand along the first axis-0 (turn into a 3D array)**:
```python
arr_3d_first = arr_2d[np.newaxis, :, :]
print(arr_3d_first.shape)  # Output: (1, 2, 3)
print(arr_3d_first)        # [[[1 2 3], [4 5 6]]]
```
>

+ **Expand along the second axis-1**:
```python
arr_3d_second = arr_2d[:, np.newaxis, :]
print(arr_3d_second.shape)  # Output: (2, 1, 3)
print(arr_3d_second)        # [[[1 2 3]], [[4 5 6]]]
```

+ **Expand along the third axis-2**:
```python
arr_3d_second = arr_2d[:, :, np.newaxis]
print(arr_3d_second.shape)  # Output: (2, 3, 1)
print(arr_3d_third) # [[[1], [2], [3]], [[4], [5], [6]]]
```

#### With a 3D Array
A 3D array has three axes (depth, rows, coulmns)
```python
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d.shape)  # Output: (2, 2, 2)
```
Applying `np.newaxis`:
**Expand along the first axis**:
```python
arr_4d_first = arr_3d[np.newaxis, :, :, :]
print(arr_4d_first.shape)  # Output: (1, 2, 2, 2)
```

**Expand along the second axis**:
```python
arr_4d_second = arr_3d[:, np.newaxis, :, :]
print(arr_4d_second.shape)  # Output: (2, 1, 2, 2)
```

**Expand along the third axis**:
```python
arr_4d_third = arr_3d[:, :, np.newaxis, :]
print(arr_4d_third.shape)  # Output: (2, 2, 1, 2)
```

**Expand along the fourth axis**:
```python
arr_4d_fourth = arr_3d[:, :, :, np.newaxis]
print(arr_4d_fourth.shape)  # Output: (2, 2, 2, 1)
```