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


### np.mean()
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
In this example, the mean of each row is calculated:

- First row mean: (1 + 2 + 3) / 3 = 2
- Second row mean: (4 + 5 + 6) / 3 = 5
- Third row mean: (7 + 8 + 9) / 3 = 8

### Visual Summary
- `axis=0`: Mean of columns
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \xrightarrow{\text{axis=0}} [4.0, 5.0, 6.0]$$
- `axis=1`: Mean of columns
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \xrightarrow{\text{axis=0}} [2.0, 5.0, 8.0]$$

---

### Code Documentation

np.polyfit()