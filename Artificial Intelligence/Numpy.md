List - slow and Numpy fast 
Why -> numpy is Fixed type 
+ ? This is because computer see number as binary but numpy and list see number in 2 diff ways
	![[Pasted image 20240531151040.png]]
	List store the number as 4 kind of data. Therefor more memory need to be processed thus slower run time.
	![[Pasted image 20240531151157.png]]
+ $ Numpy Advantage over list
	Faster to read less bytes of memory
	No type checking when iterating through objects

+ $ Numpy use Contiguous Memory (data can be search on by one and not have to search base on each memory block)
	while List stored Memory scatter around (list use a array of pointers to point out values) -> more search time -> less performance
	![[Pasted image 20240531151758.png]]
+ ? How List different from Numpy
	![[Pasted image 20240531152019.png]]
	Numpy also core component of Pandas

# Basic Numpy Command 
+ $ Remember numpy shape always: **Row x Column** written in integer.

## Vector & Matrix Creation
+ ? In Code number start from 0 thus if the number starting from n is now $n-1$. (e.g. $1,2,3$ is now $0,1,2$)
**Vector**: 
![[Pasted image 20241014151207.png]]
**Matrix**
![[Pasted image 20241014151030.png]]


Example:
+ ? Create a **zeros vector with 4 elements**
```python
a = np.zeros(4);                
```
+ ? Create a **zeros matrix with 4 rows and 2 columns** 
```python
a = np.zeros((4, 2));
```
+ $ to initialize matrix, add blanket (a, b) where a is number of row and b the number of column.

**Create vector of zeros**
```python
a = np.zeros(4);                
print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
```

#### Create random array: numpy values vector
```python
a = np.random.random_sample(4); 
print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
```

**"rand()" uniform distribution between 0 and 1**
```python
ran = np.random.rand(20)
print(ran)
```

**"randint" is used to generate random integers between upper and lower bounds**
```python
x = np.random.randint(1, 50) # random number in range(min, max)
x
```

**"you can create a matrix of random number as well"**
```python
x = np.random.rand(3, 3)
x
```

**Arrange number from 0 to n by (start_index, stop_index, step_between_index)**
```python
a = np.arange(n); # n represent a integer  
```
> output
```python
array([0, 2, 4, 6, 8])
```

## Operation on Vectors
**Indexing**: refer to getting a elements position from an array (e.g. get value at position 3)
```python
a = np.arange(10)
print(a)
print(a[2]) # get element in position 3
```

**Slicing:** means getting a subset of an array based on their indices. (e.g. get values from index 2 to index 5)
```python
# vector slicing operations
a = np.arange(10)
print(f"a         = {a}")

# access 5 consecutive elements (start:stop:step)
c = a[2:7:1];     print("a[2:7:1] = ", c)

# access 3 elements separated by two 
c = a[2:7:2];     print("a[2:7:2] = ", c)

# access all elements index 3 and above
c = a[3:];        print("a[3:]    = ", c)

# access all elements below index 3
c = a[:3];        print("a[:3]    = ", c)

# access all elements
c = a[:];         print("a[:]     = ", c)
```

**Single vetor operations**
```python
a = np.array([1,2,3,4])
print(f"a             : {a}")
# negate elements of a (i.e. add subtract sign to value)
b = -a 
print(f"b = -a        : {b}")

# sum all elements of a, returns a scalar
b = np.sum(a) 
print(f"b = np.sum(a) : {b}")

b = np.mean(a)
print(f"b = np.mean(a): {b}")

b = a**2
print(f"b = a**2      : {b}")
```

**Vector element-wise operations**
+ $ Element-wise only work with the same size vectors
+ ? The same for subtract/divide/multiply
```python
a = np.array([ 1, 2, 3, 4])
b = np.array([-1,-2, 3, 4])
print(f"Binary operators work element wise: {a + b}")
```

**Vector Dot Product**
![[Pasted image 20241014150825.png]]
```python
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
print(f"my_dot(a, b) = {my_dot(a, b)}")
```

## Matrices Detail
+ ? Each row in the matrix must be symetrical. (if 1 row have 4 values, every rows must have 4 values) 
```python
a = np.array([[5], [4], [3]]);   print(f" a shape = {a.shape}, np.array: a = {a}")
print(f" a shape = {a.shape}, np.array: a = {a}")
```

+ ? Like mention above, matrix have 2 indexes describe `[row, column]`. Access either return an element or a row, column.
```python
#vector indexing operations on matrices
a = np.arange(6).reshape(-1, 2)   #reshape is a convenient way to create matrices
print(f"a.shape: {a.shape}, \na= {a}")

#access an element
print(f"\na[2,0].shape:   {a[2, 0].shape}, a[2,0] = {a[2, 0]}")

#access a row
print(f"a[2].shape:   {a[2].shape}, a[2]   = {a[2]}, type(a[2])   = {type(a[2])}")
```

**Reshape:** just like 1-D array (i.e. vector) 
+ ? **Matrix need to have symetrical row/column** so to make thing easier, **-1 return the number of rows that can be symetric** along with the column. (e.g. 2 in our example)
```python
a = np.arange(6).reshape(3, 2) # the same as b
b = np.arange(6).reshape(-1, 2)   #reshape is a convenient way to create matrices
print(f"b.shape: {b.shape}, \nb= {b}")   
```
> output
```python
b.shape: (3, 2), 
b= [[0 1]
 [2 3]
 [4 5]]
```

**Slicing**: slicing indecies using 3 value ($start:stop:step$) 
```python
#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 3 elements each seperate by 2 (start:stop:step)
print("a[0, 2:7:2] = ", a[0, 2:7:2], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 5 consecutive elements (start:stop:step) in two rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# access all elements in one row (very common usage)
print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")
```
>output
```python
a = 
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]]
a[0, 2:7:1] =  [2 3 4 5 6] ,  a[0, 2:7:1].shape = (5,) a 1-D array
a[0, 2:7:2] =  [2 4 6] ,  a[0, 2:7:1].shape = (5,) a 1-D array
a[:, 2:7:1] = 
 [[ 2  3  4  5  6]
 [12 13 14 15 16]] ,  a[:, 2:7:1].shape = (2, 5) a 2-D array
a[:,:] = 
 [[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]] ,  a[:,:].shape = (2, 10)
a[1,:] =  [10 11 12 13 14 15 16 17 18 19] ,  a[1,:].shape = (10,) a 1-D array
a[1]   =  [10 11 12 13 14 15 16 17 18 19] ,  a[1].shape   = (10,) a 1-D array

```


**np.mean()**
1. **np.mean(a, axis=0)**:
- Computes the mean along the columns.
- This means it calculates the average of each column, resulting in an array where each element is the mean of the corresponding column.
**Example**:
```python
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

mean_columns = np.mean(a, axis=0)
print(mean_columns)  # Output: [4. 5. 6.]
```
- In this example, the mean of each column is calculated:
    
    - First column mean: (1 + 4 + 7) / 3 = 4
    - Second column mean: (2 + 5 + 8) / 3 = 5
    - Third column mean: (3 + 6 + 9) / 3 = 6

2. **np.mean(a, axis=1)**:
- Computes the mean along the rows.
- This means it calculates the average of each row, resulting in an array where each element is the mean of the corresponding row.
 
 **Example**:
```python
mean_rows = np.mean(a, axis=1)
print(mean_rows)  # Output: [2. 5. 8.]
```
     

#### Method to Expand matrix or array

[reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
> Disadvantage: you have to point out the shape of the image to reshape it
```python
import numpy as np

# Assume you have a 2D image array of shape (height, width)
image = np.random.rand(28, 28)  # Example: a 28x28 grayscale image

# Reshape it to (height, width, 1)
image_reshaped = image.reshape(28, 28, 1)

print(image_reshaped.shape)  # Output: (28, 28, 1)
```

[expand_dims](https://numpy.org/doc/2.0/reference/generated/numpy.expand_dims.html)
> Easy to expand dimension of a image without directly pointing out its shape. 
```python
import numpy as np

# Assume you have a 2D image array of shape (height, width)
image = np.random.rand(28, 28)  # Example: a 28x28 grayscale image

# Add an extra dimension at the right-most side
image_reshaped = np.expand_dims(image, axis=-1)

print(image_reshaped.shape)  # Output: (28, 28, 1)
```

### Normalization Method



**Z-Score**
