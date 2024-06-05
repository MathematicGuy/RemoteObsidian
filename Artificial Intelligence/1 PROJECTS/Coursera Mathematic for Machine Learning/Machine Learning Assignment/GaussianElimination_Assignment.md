# Programming Assignment - Gaussian Elimination


Welcome to the programming assignment on Gaussian Elimination! In this assignment, you will implement the Gaussian elimination method, a foundational algorithm for solving systems of linear equations.

Linear algebra is fundamental to machine learning, serving as the basis for numerous algorithms. Gaussian elimination, while not the most advanced method used today, is a classical and essential technique for solving systems of linear equations. It provides valuable insights into the core principles of linear algebra and lays the groundwork for more advanced numerical methods.

## Why should you care?

- **Foundational Skills**: Strengthen your understanding of key linear algebra concepts.
- **Programming Practice**: Enhance your coding skills by implementing a classical mathematical algorithm.**
- **Historical Significance**: Gaussian elimination, though not the most cutting-edge method today, is historically significant and provides a solid starting point for understanding the evolution of linear algebra techniques.

# Outline
- [ 1 - Introduction ](#1)
  - [ 1.1 How to complete this assignment](#1.1)
  - [ 1.2 Gaussian Elimination Algorithm](#1.2)
- [ 2 - Necessary imports](#2)
- [ 3 - Auxiliary functions](#3)
  - [ 3.1 - Function swap rows](#3.1)
  - [ 3.2 - Finding the first non-zero value in a column starting from a specific value](#3.2)
  - [ 3.3 - Find the first non zero element for any row](#3.3)
  - [ 3.4 Moving one row to the bottom](#3.4)
  - [ 3.5 - Constructing the Augmented Matrix](#3.5)
- [ 4 - Row echelon form](#4)
  - [ 4.1 - Row Echelon Form](#4.1)
  - [ 4.2 - A worked example ](#4.2)
    - [ Exercise 1](#ex01)
- [ 5 - Back substitution](#5)
  - [ Exercise 2](#ex02)
- [ 6 - The Gaussian Elimination](#6)
  - [ 6.1 - Bringing it all together](#6.1)
    - [ Exercise 3](#ex03)
- [ 7 - Test with any system of equations!](#7)



### 1.1 How to complete this assignment

This is the first assignment in the Math for Machine Learning and Data Science specialization! Let's quickly go over how it works.

This assignment has $3$ graded functions. Each graded function will have some parts replaced as `None`. These parts you have to replace with the proper value. For instance, in the first graded function there is this line of code:

```Python
pivot_candidate = M[None, None]
```

This means that you must replace the correct values for the row (first None) and column (second None). Do not worry, the functions have comments on every line of code so you won't get lost! 

After each graded function, there is a code to test your solution. It will test your function with some basic and quick tests to assure you are in the right path! **Note that these tests perform only basic tests, so you may pass in the unit tests but fail when submitting your code.** This is because when grading we perform more complex tests. However, in any case you will be provided with feedbacks so it will help you debugging your code.

<a name="1.2"></a>
### 1.2 Gaussian Elimination Algorithm

Gaussian elimination offers a systematic approach to solving systems of linear equations by transforming an augmented matrix into row-echelon form, thereby enabling the determination of variables. The algorithm comprises several essential steps:

**NOTE**: 

- For simplicity, the algorithm you will develop here will only work on **non-singular** systems of equations, i.e., equations that have a unique solution.
- Remember you can check if a matrix is singular or not by computing its determinant.

### Step 1: [[Augmented Matrix]] (tạo ma trận tăng cường)
Consider a system of linear equations:

$$
\begin{align*}
2x_1 + 3x_2 + 5x_3&= 12 \\
-3x_1 - 2x_2 + 4x_3 &= -2 \\
x_1 + x_2 - 2x_3  &= 8 \\
\end{align*}
$$

Create the augmented matrix \([A | B]\), where \(A\) represents the coefficient matrix and \(B\) denotes the column vector of constants:

$$
A = \begin{bmatrix}
\phantom{-}2 & \phantom{-}3 & \phantom{-}5  \\
-3 & -2 & \phantom-4 \\
\phantom{-}1 & \phantom{-}1 & -2  \\
\end{bmatrix}
$$

$$
B = \begin{bmatrix}
\phantom-12 \\ -2 \\ \phantom-8 
\end{bmatrix}
$$

Thus, \([A | B]\) is represented as:

$$
\begin{bmatrix}
\phantom{-}2 & \phantom{-}3 & \phantom{-}5 & | & \phantom{-}12 \\
-3 & -2 & \phantom-4 & | & -2 \\
\phantom{-}1 & \phantom{-}1 & -2 & | & \phantom{-}8 \\
\end{bmatrix}
$$

Note: For this assignment, matrix \(A\) is **always square**, accommodating scenarios with \(n\) equations and \(n\) variables.

### Step 2: Transform Matrix into Row Echelon Form
Initiate row operations to convert the augmented matrix into row-echelon form. The objective is to introduce zeros below the leading diagonal.

- **Row Switching:** Rearrange rows to position the leftmost non-zero entry at the top.
- **Row Scaling:** Multiply a row by a non-zero scalar.
- **Row Replacement:** Substitute a row with the sum of itself and a multiple of another row.

### Step 3: Back Substitution

After attaining the row-echelon form, solve for variables starting from the last row and progressing upwards.

Remember, the aim is to simplify the system for easy determination of solutions!

### Step 4: Compile the Gaussian Elimination Algorithm

Combine each function related to the aforementioned steps into a single comprehensive function.

<a name="2"></a>
## 2 - Necessary imports

Next codeblock will import the necessary libraries to run this assignment. Please do not add nor remove any value there.


```python
import numpy as np
```


```python
import w2_unittest
```

<a name="3"></a>
## 3 - Auxiliary functions

This section introduces three auxiliary functions crucial for facilitating your assignment. These functions have already been coded, eliminating the need for your concern regarding their implementation. However, it's essential to examine them carefully to grasp their appropriate usage.

**Note: In Python, indices commence at $0$ rather than $1$. Therefore, a matrix with $n$ rows is indexed as $0, 1, 2, \ldots, n-1$.**


<a name="3.1"></a>
### 3.1 - Function swap rows
This function has as input a [numpy array](https://numpy.org/doc/stable/reference/generated/numpy.array.html) and two indexes to swap the rows corresponding to those indexes. It **does not change the original matrix**, but returns a new one.


```python
def swap_rows(M, row_index_1, row_index_2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.
    """

    # Copy matrix M so the changes do not affect the original matrix. 
    M_copy = M.copy()
    # Swap indexes
    M_copy[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M_copy
```
Detail example swap_row work:
```python
'''
example augmented_matrix:
[[ 2.  3.  5. 12.]
 [-3. -2.  4. -2.]
 [ 1.  1. -2.  8.]]
'''
 
# This mean get row 1 to row 2 of M_copy Matrix 
print(M_copy[[row_index1, row_index2]]) 
''' output1
[[-3. -2.  4. -2.]
 [ 2.  3.  5. 12.]]
'''

# This mean get row 2 to row 1 of M_copy Matrix 
print(M_copy[[row_index2, row_index1]]) 
''' output2
[[ 2.  3.  5. 12.]
 [-3. -2.  4. -2.]]
'''
# after that swap row with M_copy Matrix so the original matrix M not get modified
M_copy[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
```


Let's practice with some examples. Consider the following matrix $M$.
```python
M = np.array([
[1, 3, 6],
[0, -5, 2],
[-4, 5, 8]
])
print(M)
```

    [[ 1  3  6]
     [ 0 -5  2]
     [-4  5  8]]


Swapping row $0$ with row $2$:


```python
M_swapped = swap_rows(M, 0, 2)
print(M_swapped)
```

    [[-4  5  8]
     [ 0 -5  2]
     [ 1  3  6]]


<a name="3.2"></a>
### 3.2 - Finding the first non-zero value in a column starting from a specific value

This function becomes essential when encountering a $0$ value during row operations. It determines whether a non-zero value exists below the encountered zero, allowing for potential row swaps. Consider the following scenario within a square matrix (non-augmented):

Let's say, during a specific step of the row-echelon form process, you've successfully reduced the first 2 rows, but you encounter a zero pivot (highlighted in red) in the third row. The task is to search, **solely in entries below the pivot**, for a potential row swap.

$$
\begin{bmatrix}
6 & 4 & 8 & 1 \\
0 & 8 & 6 & 4 \\
\color{darkred}0 & \color{darkred}0 & \color{red}0 & \color{darkred}3 \\
0 & 0 & 5 & 9 
\end{bmatrix}
$$

Performing a row swap between indexes 2 and 3 (remember, indexing starts at 0), the matrix transforms into:

$$
\begin{bmatrix}
6 & 4 & 8 & 1 \\
0 & 8 & 6 & 4 \\
0 & 0 & 5 & 9  \\
0 & 0 & 0 & 3 
\end{bmatrix}
$$

Resulting in the matrix achieving the row-echelon form.


```python
def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
	    int: The index of the first non-zero value in the specified column, starting from the given row.
		Returns -1 if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:,column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array. 
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol = 1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return -1.
    return -1
```

Let's practice with this function. Consider the following matrix.


```python
N = np.array([
[0, 5, -3 ,6 ,8],
[0, 6, 3, 8, 1],
[0, 0, 0, 0, 0],
[0, 0, 0 ,0 ,7],
[0, 2, 1, 0, 4]
]
)
print(N)
```

    [[ 0  5 -3  6  8]
     [ 0  6  3  8  1]
     [ 0  0  0  0  0]
     [ 0  0  0  0  7]
     [ 0  2  1  0  4]]


If you search for a value below the first column starting at the first row, the function should return -1:


```python
print(get_index_first_non_zero_value_from_column(N, column = 0, starting_row = 0))
```

    -1


Searching for the first non zero value in the last column starting from row with index 2, it should return 3 (index corresponding to the value 7).


```python
print(get_index_first_non_zero_value_from_column(N, column = -1, starting_row = 2))
```

    3


<a name="3.3"></a>
### 3.3 - Find the first non zero element for any row

This function aids in locating the pivot within a designated row of a matrix. It identifies the index of the first non-zero element in the desired row. If no non-zero value is present, it returns -1.


```python
def get_index_first_non_zero_value_from_row(M, row, augmented = False):
    """
    Find the index of the first non-zero value in the specified row of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - row (int): The index of the row to search.
    - augmented (bool): Pass this True if you are dealing with an augmented matrix, 
                        so it will ignore the constant values (the last column in the augmented matrix).

    Returns:
    int: The index of the first non-zero value in the specified row.
                Returns -1 if no non-zero value is found.
    """

    # Create a copy to avoid modifying the original matrix
    M = M.copy()


    # If it is an augmented matrix, then ignore the constant values
    if augmented == True:
        # Isolating the coefficient matrix (removing the constant terms)
        M = M[:,:-1]
        
    # Get the desired row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns -1.
        if not np.isclose(val, 0, atol = 1e-5):
            return i
    return -1
```

Let's practice with the same matrix as before:


```python
print(N)
```

    [[ 0  5 -3  6  8]
     [ 0  6  3  8  1]
     [ 0  0  0  0  0]
     [ 0  0  0  0  7]
     [ 0  2  1  0  4]]


If not passing the argument `augmented`, then it is assumed the matrix is not augmented. 

Looking for the first non-zero index in row $2$ must return -1 whereas in row $3$, the value returned must be $4$ (the index for the value $7$ in that row). 


```python
print(f'Output for row 2: {get_index_first_non_zero_value_from_row(N, 2)}')
print(f'Output for row 3: {get_index_first_non_zero_value_from_row(N, 3)}')
```

    Output for row 2: -1
    Output for row 3: 4


Now, let's pass the argument `augmented = True`. This will make the algorithm consider $N$ an augmented matrix, therefore the last column will be removed from consideration. Now, the output for row 3 (starting from 0) should be different, excluding the last column, the output should be `-1` as well, since in the coefficient matrix (the matrix without the last column) there is no non-zero element:


```python
print(f'Output for row 3: {get_index_first_non_zero_value_from_row(N, 3, augmented = True)}')
```

    Output for row 3: -1


<a name="3.5"></a>
### 3.4 - Constructing the Augmented Matrix

This function constructs the augmented matrix by combining a square matrix of size $n \times n$, representing $n$ equations with $n$ variables each, with an $n \times 1$ matrix that denotes its constant values. The function concatenates both matrices to form the augmented matrix and returns the result.


```python
def augmented_matrix(A, B):
    """
    Create an augmented matrix by horizontally stacking two matrices A and B.

    Parameters:
    - A (numpy.array): First matrix.
    - B (numpy.array): Second matrix.

    Returns:
    - numpy.array: Augmented matrix obtained by horizontally stacking A and B.
    """
    augmented_M = np.hstack((A,B))
    return augmented_M
```


```python
A = np.array([[1,2,3], [3,4,5], [4,5,6]])
B = np.array([[1], [5], [7]])

print(augmented_matrix(A,B))
```

    [[1 2 3 1]
     [3 4 5 5]
     [4 5 6 7]]


<a name="4"></a>
## 4 - Row echelon form

<a name="4.1"></a>

<a name="4.1"></a>
### 4.1 - Row Echelon Form

As discussed in the lectures, a matrix in row echelon form adheres to the following conditions:

- Rows consisting entirely of zeroes should be positioned at the bottom.
- Each non-zero row must have its left-most non-zero coefficient (termed as a **pivot**) located to the right of any row above it. Consequently, all elements below the pivot within the same column should be 0.


**NOTE:**

- The algorithm you will build will consider only non-singular system of equations, this implies that the coefficient matrix must have determinant different from $0$. Also, it implies one very important property: **the matrix's row echelon form will have all its pivots in the main diagonal**. This is an important property because it will significantly simplify the computation.


This form ensures a structured arrangement facilitating subsequent steps in the Gaussian elimination process.


Example of matrix **in row echelon form**

$$M =
\begin{bmatrix}
7 & 2 & 3 \\
0 & 9 & 4 \\
0 & 0 & 3 \\
\end{bmatrix}
$$

Examples of matrices that **are not in row echelon form**

$$
A = \begin{bmatrix}
1 & 2 & 2 \\
0 & 5 & 3 \\
1 & 0 & 8 \\
\end{bmatrix}
$$

$$B = 
\begin{bmatrix}
1 & 2 & 3 \\
0 & 0 & 4 \\
0 & 0 & 7 \\
\end{bmatrix}
$$

Matrix $A$ fails to satisfy the criteria for row echelon form as there exists a non-zero element below the first pivot (located in row 0). Similarly, matrix $B$ does not meet the requirements as the second pivot (in row 1 with a value of 4) has a non-zero element below it.

<a name="4.2"></a>
### 4.2 - A worked example 

In this section, you'll revisit an example from the lecture to facilitate the implementation of an algorithm. If you feel confident in proceeding with the algorithm, you may skip this section.

Consider matrix $M$ given by:

$$
M = 
\begin{bmatrix} 
* & * & * & \\
0 & \text{pivot} & * \\
0 & \text{value} & * 
\end{bmatrix}
$$

Here, the asterisk ( * ) denotes any number. To nullify the last row (row $2$), two steps are required:

- Scale $R_1$ by the inverse of the pivot:

$$
\text{Row 1} \rightarrow \frac{1}{\text{pivot}} \cdot \text{Row } 
$$

Resulting in the updated matrix with the pivot for row $1$ set to $1$:

$$
M = 
\begin{bmatrix} 
* & * & * & \\
0 & 1 & * \\
0 & \text{value} & * 
\end{bmatrix}
$$

Next, to eliminate the value below the pivot in row $1$, apply the following formula:

$$
\text{Row 2} \rightarrow \text{Row 2} - \text{value}\cdot \text{Row 1}
$$

This transformation yields the modified matrix:

$$
M = 
\begin{bmatrix} 
* & * & * & \\
0 & 1 & * \\
0 & 0 & * 
\end{bmatrix}
$$

**Note that the square matrix $A$ needs to be in row-echelon form. However, every row operation conducted must also affect the augmented (constant) part. This ensures that you are effectively preserving the solutions for the entire system!** 

Let's review the example covered in the lecture. 

$$
\begin{align*}
2x_2 + x_3 &= 3 \\
x_1 + x_2 +x_3 &= 6 \\
x_1 + 2x_2 + 1x_3 &= 12
\end{align*}
$$

Consequently, the square matrix $A$ is formulated as:

$$
A = 
\begin{bmatrix} 
0 & 2 & 1 & \\
1 & 1 & 1 & \\
1 & 2 & 1 & 
\end{bmatrix}
$$

The column vector (a matrix of size $n \times 1$) is represented by:

$$
B = 
\begin{bmatrix} 
3\\
6\\
12
\end{bmatrix}
$$

Combining matrices $A$ and $B$ yields the augmented matrix $M$:

$$
M = 
\begin{bmatrix} 
0 & 2 & 1 & | & 3 \\
1 & 1 & 1 & | & 6 \\
1 & 2 & 1 & | & 12 
\end{bmatrix}
$$

**Step 1:**

Commencing with row $0$: The initial candidate for the pivot is always the value in the main diagonal of the matrix. Denoting row $0$ as $R_0$:

$$R_0= \begin{bmatrix} 0 & 2 & 1 & | & 3 \end{bmatrix}$$

The value in the main diagonal is the element $M[0,0]$ (the first element of the first column). The first row can be accessed by performing $M[0]$, i.e., $M[0] = R_0$.

The first row operation involves **scaling by the pivot's inverse**. Since the value in the main diagonal is $0$, necessitating a non-zero value for scaling by its inverse, you must switch rows in this case. Note that $R_1$ has a value different from $0$ in the required index. Consequently, switching rows $0$ and $1$:

$$R_0 \rightarrow R_1$$
$$R_1 \rightarrow R_0$$

Resulting in the updated augmented matrix:

$$
M = 
\begin{bmatrix} 
1 & 1 & 1 & | & 6 \\
0 & 2 & 1 & | & 3 \\
1 & 2 & 1 & | & 12 
\end{bmatrix}
$$

Now, the pivot is already $1$, eliminating the need for row scaling. Following the formula:

$$ R_1 \rightarrow  R_1 - 0 \cdot R_0 = R_1$$

Therefore, the second row remains unchanged. Moving to the third row ($R_2$), the value in the augmented matrix below the pivot from $R_0$ is $M[2,0]$, which is $1$.

$$R_2 = R_2 - 1 \cdot R_0 = \begin{bmatrix} 0 & 1 & 0 & | & 6  \end{bmatrix}$$

Resulting in the modified augmented matrix:

$$
M = 
\begin{bmatrix} 
1 & 1 & 1 & | & 6 \\
0 & 2 & 1 & | & 3 \\
0 & 1 & 0 & | & 6
\end{bmatrix}
$$

Progressing to the second row ($R_1$), the value in the main diagonal is $2$, different from zero. Scaling it by $\frac{1}{2}$:

$$R_1 = \frac{1}{2}R_1$$

Resulting in the augmented matrix:

$$
M = 
\begin{bmatrix} 
1 & 1 & 1 & | & 6 \\
0 & 1 & \frac{1}{2} & | & \frac{3}{2} \\
0 & 1 & 0 & | & 6
\end{bmatrix}
$$

Now, there's only one row below it for row replacement. The value just below the pivot is located at $M[2,1]$, which is $1$. Thus:

$$R_2 = R_2 - 1 \cdot R_1 = \begin{bmatrix} \phantom{-}0 & \phantom{-}0 & -\frac{1}{2} & | & \phantom{-}\frac{9}{2} \end{bmatrix} $$

Resulting in the augmented matrix:


$$
M = 
\begin{bmatrix} 
\phantom{-}1 & \phantom{-}1 & \phantom{-}1 & | & \phantom{-}6 \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}\frac{1}{2} & | & \phantom{-}\frac{3}{2} \\
\phantom{-}0 & \phantom{-}0 & -\frac{1}{2} & | & \phantom{-}\frac{9}{2} 
\end{bmatrix}
$$

Finally, normalizing the last row as

$$R_2 = -2 \cdot R_2$$

The resulting matrix is
$$
M = 
\begin{bmatrix} 
\phantom{-}1 & \phantom{-}1 & \phantom{-}1 & | & \phantom{-}6 \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}\frac{1}{2} & | & \phantom{-}\frac{3}{2} \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -9 
\end{bmatrix}
$$

Thus, the matrix is now in row echelon form with unitary pivots.
Now you are ready to go! You will implement such algorithm in the following exercise.

<a name="ex01"></a>
### Exercise 1

This exercise involves implementing the elimination method to convert a matrix into row-echelon form. As discussed in lectures, the primary approach involves inspecting the values along the diagonal. If they equate to $0$, an attempt to swap rows should be made to obtain a non-zero value.

```python
# GRADED FUNCTION: row_echelon_form

def row_echelon_form(A, B):
    """
    Utilizes elementary row operations to transform a given set of matrices, 
    which represent the coefficients and constant terms of a linear system, into row echelon form.

    Parameters:
    - A (numpy.array): The input square matrix of coefficients.
    - B (numpy.array): The input column matrix of constant terms

    Returns:
    numpy.array: A new augmented matrix in row echelon form with pivots as 1.
    """
    
    # Before any computation, check if matrix A (coefficient matrix) has non-zero determinant. 
    # It will be used the numpy sub library np.linalg to compute it.

    det_A = np.linalg.det(A)

    # Returns "Singular system" if determinant is zero
    if np.isclose(det_A, 0) == True:
        return 'Singular system'

    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()


    # Convert matrices to float to prevent integer division
    A = A.astype('float64')
    B = B.astype('float64')

    # Number of rows in the coefficient matrix
    num_rows = len(A) 

    ### START CODE HERE ###

    # Transform matrices A and B into the augmented matrix M
    M = augmented_matrix(A,B)
    print("am:", M)
    # Iterate over the rows.
    for row in range(num_rows):

        # The first pivot candidate is always in the main diagonal, let's get it. 
        # Remember that the diagonal elements in a matrix has the same index for row and column. 
        # You may access a matrix value by typing M[row, column]. In this case, column = None
        pivot_candidate = M[row, row]

        # If pivot_candidate is zero, it cannot be a pivot for this row. 
        # So the first step you need to take is to look at the rows below it to check if there is a non-zero element in the same column.
        # The usage of np.isclose is a good practice when comparing two floats.
        if np.isclose(pivot_candidate, 0) == True: 
            # Get the index of the first non-zero value below the pivot_candidate. 
            first_non_zero_value_below_pivot_candidate = get_index_first_non_zero_value_from_column(M, row, row) 

            # Swap rows
            M = swap_rows(M, row, first_non_zero_value_below_pivot_candidate) 

            # Get the pivot, which is in the main diagonal now 
            pivot = M[row,row] 
        
        # If pivot_candidate is already non-zero, then it is the pivot for this row
        else:
            pivot = pivot_candidate 
            
        # Now you are ready to apply the row reduction in every row below the current
        print(M)

        # Divide the current row by the pivot, so the new pivot will be 1. You may use the formula current_row -> 1/pivot * current_row
        # Where current_row can be accessed using M[row].
        M[row] = 1/pivot * M[row]
        print("pivot", pivot)
        # Perform row reduction for rows below the current row
        for j in range(row + 1, num_rows): 
            # Get the value in the row that is below the pivot value. 
            # Remember that, since you are dealing only with non-singular matrices, the pivot is in the main diagonal.
            # Therefore, the values in row j that are below the pivot, must have column index the same index as the column index for the pivot.
            value_below_pivot = M[j, row]
            print("value_below_pivot", M[j, row])
            # Perform row reduction using the formula:
            # row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row
            M[j] = M[j] - value_below_pivot*M[row]
            
    ### END CODE HERE ###

    return M
            
```


```python
A = np.array([[1,2,3],[0,1,0], [0,0,5]])
B = np.array([[1], [2], [4]])

row_echelon_form(A,B)
```

    am: [[1. 2. 3. 1.]
     [0. 1. 0. 2.]
     [0. 0. 5. 4.]]
    [[1. 2. 3. 1.]
     [0. 1. 0. 2.]
     [0. 0. 5. 4.]]
    pivot 1.0
    value_below_pivot 0.0
    value_below_pivot 0.0
    [[1. 2. 3. 1.]
     [0. 1. 0. 2.]
     [0. 0. 5. 4.]]
    pivot 1.0
    value_below_pivot 0.0
    [[1. 2. 3. 1.]
     [0. 1. 0. 2.]
     [0. 0. 5. 4.]]
    pivot 5.0





    array([[1. , 2. , 3. , 1. ],
           [0. , 1. , 0. , 2. ],
           [0. , 0. , 1. , 0.8]])




```python
w2_unittest.test_row_echelon_form(row_echelon_form)
```

    am: [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    pivot 1.0
    value_below_pivot 0.0
    value_below_pivot 0.0
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    pivot 1.0
    value_below_pivot 0.0
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    pivot 1.0
    am: [[1. 2. 3. 4.]
     [5. 0. 2. 3.]
     [1. 4. 5. 6.]]
    [[1. 2. 3. 4.]
     [5. 0. 2. 3.]
     [1. 4. 5. 6.]]
    pivot 1.0
    value_below_pivot 5.0
    value_below_pivot 1.0
    [[  1.   2.   3.   4.]
     [  0. -10. -13. -17.]
     [  0.   2.   2.   2.]]
    pivot -10.0
    value_below_pivot 2.0
    [[ 1.   2.   3.   4. ]
     [-0.   1.   1.3  1.7]
     [ 0.   0.  -0.6 -1.4]]
    pivot -0.6000000000000001
    [92m All tests passed


<a name="5"></a>
## 5 - Back substitution

The final step of the algorithm involves back substitution, a crucial process in obtaining solutions for the linear system. As discussed in the lectures, this method initiates from the bottom and moves upwards. Utilizing elementary row operations, it aims to convert every element above the pivot into zeros, ending with a matrix in **reduced row echelon form**. The formula employed is:


$$\text{Row above} \rightarrow \text{Row above} - \text{value} \cdot \text{Row pivot}$$

In this equation, $\text{value}$ denotes the value above the pivot, which initially equals 1. To illustrate this process, let's consider the matrix discussed previously:

$$
M = 
\begin{bmatrix} 
\phantom{-}1 & -1 & \phantom{-}\frac{1}{2} & | & \phantom{-}\frac{1}{2} \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}1 & | & -1 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -1 
\end{bmatrix}
$$

Starting from bottom to top:

- $R_2$:

- -  $R_1 = R_1 - 1 \cdot R_2 = \begin{bmatrix} 0 & 1 & 0 & | & 0 \end{bmatrix}$
- - $R_0 = R_0 - \frac{1}{2} \cdot R_1 = \begin{bmatrix} 1 & -\frac{1}{2} & 0 & | & 1 \end{bmatrix}$

The resulting matrix is then

$$
M = 
\begin{bmatrix} 
\phantom{-}1 & -\frac{1}{2} & \phantom{-}0 & | & \phantom{-}1  \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}0 & | & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -1 
\end{bmatrix}
$$

Moving to $R_1$:

- $R_1$:

- - $R_0 = R_0 - \left(-\frac{1}{2} R_1 \right) = \begin{bmatrix} 1 & 0 & 0 & | & 1 \end{bmatrix}$

And the final matrix is

$$
M = 
\begin{bmatrix} 
\phantom{-}1 & \phantom{-}0 & \phantom{-}0 & | & \phantom{-}1  \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}0 & | & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -1
\end{bmatrix}
$$

Note that after back substitution, the solution is just the values in the augmented column! In this case,

$$x_0 = 1 \\ x_1 =0\\ x_2 = -1$$

<a name="ex02"></a>
### Exercise 2

In this exercise you will implement a function to perform back substitution in an **augmented matrix with unique solution and in row echelon form with unitary pivots**


```python
# GRADED FUNCTION: back_substitution

def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.

    Parameters:
    - M (numpy.array): The augmented matrix in row echelon form with unitary pivots (n x n+1).

    Returns:
    numpy.array: The solution vector of the linear system.
    """
    
    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()
#     M[0] = [1, -1, 1/2, 1/2]
#     M[1] = [0, 1, 1, -1]
#     M[2] = [0, 0, 1, -1]
    
    print(M)
    
    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = M.shape[0]
        
    ### START CODE HERE ####
    
    # Iterate from bottom to top
    for row in reversed(range(num_rows)): # start with 3
        print("row: ", row)
        substitution_row = M[row]
        print("substitution_row: ", substitution_row)
        
        # Get the index of the first non-zero element in the substitution row. Remember to pass the correct value to the argument augmented.
        index = get_index_first_non_zero_value_from_row(M, row, augmented = False)
        print("index: ", index)
        
        # Iterate over the rows above the substitution_row
        for j in reversed(range(row)): 
            # Get the row to be reduced. The indexing here is similar as above, with the row variable replaced by the j variable.
            row_to_reduce = M[j]
            print("row_to_reduce: ", row_to_reduce)
            # Get the value of the element at the found index in the row to reduce
            value = row_to_reduce[index]
            print("value to reduced: ", value)
            
            # Perform the back substitution step using the formula row_to_reduce -> row_to_reduce - value * substitution_row
            row_to_reduce = row_to_reduce - value * substitution_row
            
            # Replace the updated row in the matrix, be careful with indexing!
            M[j,:] = row_to_reduce
            print("M[j,:]: ", M[j,:])
            print("new matrix:\n", M)
    ### END CODE HERE ####

     # Extract the solution from the last column`
    solution = M[:,-1]
    print("substitution_row: ", solution)
    return solution
```


```python
# A = A.copy()
# B = B.copy()

# # Convert matrices to float to prevent integer division
# A = A.astype('float64')
# B = B.astype('float64')

# M = augmented_matrix(A,B)
# back_substitution(M)
```


```python
w2_unittest.test_back_substitution(back_substitution)
```

    [[1 0 0 5]
     [0 1 0 6]
     [0 0 1 7]]
    row:  2
    substitution_row:  [0 0 1 7]
    index:  2
    row_to_reduce:  [0 1 0 6]
    value to reduced:  0
    M[j,:]:  [0 1 0 6]
    new matrix:
     [[1 0 0 5]
     [0 1 0 6]
     [0 0 1 7]]
    row_to_reduce:  [1 0 0 5]
    value to reduced:  0
    M[j,:]:  [1 0 0 5]
    new matrix:
     [[1 0 0 5]
     [0 1 0 6]
     [0 0 1 7]]
    row:  1
    substitution_row:  [0 1 0 6]
    index:  1
    row_to_reduce:  [1 0 0 5]
    value to reduced:  0
    M[j,:]:  [1 0 0 5]
    new matrix:
     [[1 0 0 5]
     [0 1 0 6]
     [0 0 1 7]]
    row:  0
    substitution_row:  [1 0 0 5]
    index:  0
    substitution_row:  [5 6 7]
    [[ 1.          2.          3.          4.        ]
     [-0.          1.          1.3         1.7       ]
     [-0.         -0.          1.          2.33333333]]
    row:  2
    substitution_row:  [-0.         -0.          1.          2.33333333]
    index:  2
    row_to_reduce:  [-0.   1.   1.3  1.7]
    value to reduced:  1.3
    M[j,:]:  [ 0.          1.          0.         -1.33333333]
    new matrix:
     [[ 1.          2.          3.          4.        ]
     [ 0.          1.          0.         -1.33333333]
     [-0.         -0.          1.          2.33333333]]
    row_to_reduce:  [1. 2. 3. 4.]
    value to reduced:  3.0
    M[j,:]:  [ 1.          2.          0.         -2.99999999]
    new matrix:
     [[ 1.          2.          0.         -2.99999999]
     [ 0.          1.          0.         -1.33333333]
     [-0.         -0.          1.          2.33333333]]
    row:  1
    substitution_row:  [ 0.          1.          0.         -1.33333333]
    index:  1
    row_to_reduce:  [ 1.          2.          0.         -2.99999999]
    value to reduced:  2.0
    M[j,:]:  [ 1.          0.          0.         -0.33333333]
    new matrix:
     [[ 1.          0.          0.         -0.33333333]
     [ 0.          1.          0.         -1.33333333]
     [-0.         -0.          1.          2.33333333]]
    row:  0
    substitution_row:  [ 1.          0.          0.         -0.33333333]
    index:  0
    substitution_row:  [-0.33333333 -1.33333333  2.33333333]
    [[ 1.          5.          6.          9.        ]
     [-0.          1.          1.          1.64285714]
     [ 0.          0.          1.          0.        ]]
    row:  2
    substitution_row:  [0. 0. 1. 0.]
    index:  2
    row_to_reduce:  [-0.          1.          1.          1.64285714]
    value to reduced:  1.0
    M[j,:]:  [-0.          1.          0.          1.64285714]
    new matrix:
     [[ 1.          5.          6.          9.        ]
     [-0.          1.          0.          1.64285714]
     [ 0.          0.          1.          0.        ]]
    row_to_reduce:  [1. 5. 6. 9.]
    value to reduced:  6.0
    M[j,:]:  [1. 5. 0. 9.]
    new matrix:
     [[ 1.          5.          0.          9.        ]
     [-0.          1.          0.          1.64285714]
     [ 0.          0.          1.          0.        ]]
    row:  1
    substitution_row:  [-0.          1.          0.          1.64285714]
    index:  1
    row_to_reduce:  [1. 5. 0. 9.]
    value to reduced:  5.0
    M[j,:]:  [1.        0.        0.        0.7857143]
    new matrix:
     [[ 1.          0.          0.          0.7857143 ]
     [-0.          1.          0.          1.64285714]
     [ 0.          0.          1.          0.        ]]
    row:  0
    substitution_row:  [1.        0.        0.        0.7857143]
    index:  0
    substitution_row:  [0.7857143  1.64285714 0.        ]
    [[1. 8. 6. 9.]
     [0. 1. 8. 6.]
     [0. 0. 1. 1.]]
    row:  2
    substitution_row:  [0. 0. 1. 1.]
    index:  2
    row_to_reduce:  [0. 1. 8. 6.]
    value to reduced:  8.0
    M[j,:]:  [ 0.  1.  0. -2.]
    new matrix:
     [[ 1.  8.  6.  9.]
     [ 0.  1.  0. -2.]
     [ 0.  0.  1.  1.]]
    row_to_reduce:  [1. 8. 6. 9.]
    value to reduced:  6.0
    M[j,:]:  [1. 8. 0. 3.]
    new matrix:
     [[ 1.  8.  0.  3.]
     [ 0.  1.  0. -2.]
     [ 0.  0.  1.  1.]]
    row:  1
    substitution_row:  [ 0.  1.  0. -2.]
    index:  1
    row_to_reduce:  [1. 8. 0. 3.]
    value to reduced:  8.0
    M[j,:]:  [ 1.  0.  0. 19.]
    new matrix:
     [[ 1.  0.  0. 19.]
     [ 0.  1.  0. -2.]
     [ 0.  0.  1.  1.]]
    row:  0
    substitution_row:  [ 1.  0.  0. 19.]
    index:  0
    substitution_row:  [19. -2.  1.]
    [92m All tests passed


<a name="6"></a>
## 6 - The Gaussian Elimination

<a name="6.1"></a>
### 6.1 - Bringing it all together

Your task now is to integrate all the steps achieved thus far. Start with a square matrix $A$ of size $ n \times n$ and a column matrix $B$ of size $n \times 1$ and transform the augmented matrix $[A | B]$ into reduced row echelon form. Subsequently, verify the existence of solutions. If solutions are present, proceed to perform back substitution to obtain the values. In scenarios where there are no solutions or an infinite number of solutions, handle and indicate these outcomes accordingly.

<a name="ex03"></a>
### Exercise 3

In this exercise you will combine every function you just wrote to finish the Gaussian Elimination algorithm.


```python
# GRADED FUNCTION: gaussian_elimination

def gaussian_elimination(A, B):
    """
    Solve a linear system represented by an augmented matrix using the Gaussian elimination method.

    Parameters:
    - A (numpy.array): Square matrix of size n x n representing the coefficients of the linear system
    - B (numpy.array): Column matrix of size 1 x n representing the constant terms.

    Returns:
    numpy.array or str: The solution vector if a unique solution exists, or a string indicating the type of solution.
    """

    ### START CODE HERE ###

    # Get the matrix in row echelon form
    row_echelon_M = row_echelon_form(A, B)

    # If the system is non-singular, then perform back substitution to get the result. 
    # Since the function row_echelon_form returns a string if there is no solution, let's check for that.
    # The function isinstance checks if the first argument has the type as the second argument, returning True if it does and False otherwise.
    if not isinstance(row_echelon_M, str): 
        solution = back_substitution(row_echelon_M)

    ### END SOLUTION HERE ###

	return solution
```


```python
w2_unittest.test_gaussian_elimination(gaussian_elimination)
```

    am: [[-9. -1. -5.  1.]
     [-9. -9. -8.  4.]
     [ 0. -3. -8.  8.]]
    [[-9. -1. -5.  1.]
     [-9. -9. -8.  4.]
     [ 0. -3. -8.  8.]]
    pivot -9.0
    value_below_pivot -9.0
    value_below_pivot 0.0
    [[ 1.          0.11111111  0.55555556 -0.11111111]
     [ 0.         -8.         -3.          3.        ]
     [ 0.         -3.         -8.          8.        ]]
    pivot -8.0
    value_below_pivot -3.0
    [[ 1.          0.11111111  0.55555556 -0.11111111]
     [-0.          1.          0.375      -0.375     ]
     [ 0.          0.         -6.875       6.875     ]]
    pivot -6.875
    [[ 1.          0.11111111  0.55555556 -0.11111111]
     [-0.          1.          0.375      -0.375     ]
     [-0.         -0.          1.         -1.        ]]
    row:  2
    substitution_row:  [-0. -0.  1. -1.]
    index:  2
    row_to_reduce:  [-0.     1.     0.375 -0.375]
    value to reduced:  0.375
    M[j,:]:  [0. 1. 0. 0.]
    new matrix:
     [[ 1.          0.11111111  0.55555556 -0.11111111]
     [ 0.          1.          0.          0.        ]
     [-0.         -0.          1.         -1.        ]]
    row_to_reduce:  [ 1.          0.11111111  0.55555556 -0.11111111]
    value to reduced:  0.5555555555555556
    M[j,:]:  [1.         0.11111111 0.         0.44444444]
    new matrix:
     [[ 1.          0.11111111  0.          0.44444444]
     [ 0.          1.          0.          0.        ]
     [-0.         -0.          1.         -1.        ]]
    row:  1
    substitution_row:  [0. 1. 0. 0.]
    index:  1
    row_to_reduce:  [1.         0.11111111 0.         0.44444444]
    value to reduced:  0.1111111111111111
    M[j,:]:  [1.         0.         0.         0.44444444]
    new matrix:
     [[ 1.          0.          0.          0.44444444]
     [ 0.          1.          0.          0.        ]
     [-0.         -0.          1.         -1.        ]]
    row:  0
    substitution_row:  [1.         0.         0.         0.44444444]
    index:  0
    substitution_row:  [ 0.44444444  0.         -1.        ]
    am: [[ 1.  7. -5. -8. -8.]
     [ 0. -5. -1.  9.  4.]
     [ 6. -6.  0.  5.  9.]
     [ 7. -6.  8.  9.  5.]]
    [[ 1.  7. -5. -8. -8.]
     [ 0. -5. -1.  9.  4.]
     [ 6. -6.  0.  5.  9.]
     [ 7. -6.  8.  9.  5.]]
    pivot 1.0
    value_below_pivot 0.0
    value_below_pivot 6.0
    value_below_pivot 7.0
    [[  1.   7.  -5.  -8.  -8.]
     [  0.  -5.  -1.   9.   4.]
     [  0. -48.  30.  53.  57.]
     [  0. -55.  43.  65.  61.]]
    pivot -5.0
    value_below_pivot -48.0
    value_below_pivot -55.0
    [[  1.    7.   -5.   -8.   -8. ]
     [ -0.    1.    0.2  -1.8  -0.8]
     [  0.    0.   39.6 -33.4  18.6]
     [  0.    0.   54.  -34.   17. ]]
    pivot 39.6
    value_below_pivot 54.0
    [[ 1.          7.         -5.         -8.         -8.        ]
     [-0.          1.          0.2        -1.8        -0.8       ]
     [ 0.          0.          1.         -0.84343434  0.46969697]
     [ 0.          0.          0.         11.54545455 -8.36363636]]
    pivot 11.545454545454554
    [[ 1.          7.         -5.         -8.         -8.        ]
     [-0.          1.          0.2        -1.8        -0.8       ]
     [ 0.          0.          1.         -0.84343434  0.46969697]
     [ 0.          0.          0.          1.         -0.72440945]]
    row:  3
    substitution_row:  [ 0.          0.          0.          1.         -0.72440945]
    index:  3
    row_to_reduce:  [ 0.          0.          1.         -0.84343434  0.46969697]
    value to reduced:  -0.8434343434343435
    M[j,:]:  [ 0.          0.          1.          0.         -0.14129484]
    new matrix:
     [[ 1.          7.         -5.         -8.         -8.        ]
     [-0.          1.          0.2        -1.8        -0.8       ]
     [ 0.          0.          1.          0.         -0.14129484]
     [ 0.          0.          0.          1.         -0.72440945]]
    row_to_reduce:  [-0.   1.   0.2 -1.8 -0.8]
    value to reduced:  -1.8
    M[j,:]:  [ 0.          1.          0.2         0.         -2.10393701]
    new matrix:
     [[ 1.          7.         -5.         -8.         -8.        ]
     [ 0.          1.          0.2         0.         -2.10393701]
     [ 0.          0.          1.          0.         -0.14129484]
     [ 0.          0.          0.          1.         -0.72440945]]
    row_to_reduce:  [ 1.  7. -5. -8. -8.]
    value to reduced:  -8.0
    M[j,:]:  [  1.           7.          -5.           0.         -13.79527559]
    new matrix:
     [[  1.           7.          -5.           0.         -13.79527559]
     [  0.           1.           0.2          0.          -2.10393701]
     [  0.           0.           1.           0.          -0.14129484]
     [  0.           0.           0.           1.          -0.72440945]]
    row:  2
    substitution_row:  [ 0.          0.          1.          0.         -0.14129484]
    index:  2
    row_to_reduce:  [ 0.          1.          0.2         0.         -2.10393701]
    value to reduced:  0.2
    M[j,:]:  [ 0.          1.          0.          0.         -2.07567804]
    new matrix:
     [[  1.           7.          -5.           0.         -13.79527559]
     [  0.           1.           0.           0.          -2.07567804]
     [  0.           0.           1.           0.          -0.14129484]
     [  0.           0.           0.           1.          -0.72440945]]
    row_to_reduce:  [  1.           7.          -5.           0.         -13.79527559]
    value to reduced:  -5.0
    M[j,:]:  [  1.           7.           0.           0.         -14.50174978]
    new matrix:
     [[  1.           7.           0.           0.         -14.50174978]
     [  0.           1.           0.           0.          -2.07567804]
     [  0.           0.           1.           0.          -0.14129484]
     [  0.           0.           0.           1.          -0.72440945]]
    row:  1
    substitution_row:  [ 0.          1.          0.          0.         -2.07567804]
    index:  1
    row_to_reduce:  [  1.           7.           0.           0.         -14.50174978]
    value to reduced:  7.0
    M[j,:]:  [1.        0.        0.        0.        0.0279965]
    new matrix:
     [[ 1.          0.          0.          0.          0.0279965 ]
     [ 0.          1.          0.          0.         -2.07567804]
     [ 0.          0.          1.          0.         -0.14129484]
     [ 0.          0.          0.          1.         -0.72440945]]
    row:  0
    substitution_row:  [1.        0.        0.        0.        0.0279965]
    index:  0
    substitution_row:  [ 0.0279965  -2.07567804 -0.14129484 -0.72440945]
    am: [[ -9.  -9.  -2.   3. -10.   3.]
     [  6.   5.   6.   2.   7.  -4.]
     [ -6.  -2.   5.   5.   7.   1.]
     [ -4.  -5.  -6.  -9.   4.  -2.]
     [  3.  -6.  -2.  -8.  -8.  -3.]]
    [[ -9.  -9.  -2.   3. -10.   3.]
     [  6.   5.   6.   2.   7.  -4.]
     [ -6.  -2.   5.   5.   7.   1.]
     [ -4.  -5.  -6.  -9.   4.  -2.]
     [  3.  -6.  -2.  -8.  -8.  -3.]]
    pivot -9.0
    value_below_pivot 6.0
    value_below_pivot -6.0
    value_below_pivot -4.0
    value_below_pivot 3.0
    [[  1.           1.           0.22222222  -0.33333333   1.11111111
       -0.33333333]
     [  0.          -1.           4.66666667   4.           0.33333333
       -2.        ]
     [  0.           4.           6.33333333   3.          13.66666667
       -1.        ]
     [  0.          -1.          -5.11111111 -10.33333333   8.44444444
       -3.33333333]
     [  0.          -9.          -2.66666667  -7.         -11.33333333
       -2.        ]]
    pivot -1.0
    value_below_pivot 4.0
    value_below_pivot -1.0
    value_below_pivot -9.0
    [[  1.           1.           0.22222222  -0.33333333   1.11111111
       -0.33333333]
     [ -0.           1.          -4.66666667  -4.          -0.33333333
        2.        ]
     [  0.           0.          25.          19.          15.
       -9.        ]
     [  0.           0.          -9.77777778 -14.33333333   8.11111111
       -1.33333333]
     [  0.           0.         -44.66666667 -43.         -14.33333333
       16.        ]]
    pivot 25.0
    value_below_pivot -9.777777777777779
    value_below_pivot -44.666666666666664
    [[ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
     [-0.          1.         -4.66666667 -4.         -0.33333333  2.        ]
     [ 0.          0.          1.          0.76        0.6        -0.36      ]
     [ 0.          0.          0.         -6.90222222 13.97777778 -4.85333333]
     [ 0.          0.          0.         -9.05333333 12.46666667 -0.08      ]]
    pivot -6.902222222222222
    value_below_pivot -9.053333333333335
    [[ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
     [-0.          1.         -4.66666667 -4.         -0.33333333  2.        ]
     [ 0.          0.          1.          0.76        0.6        -0.36      ]
     [-0.         -0.         -0.          1.         -2.02511269  0.70315518]
     [ 0.          0.          0.          0.         -5.86735351  6.28589826]]
    pivot -5.867353509336773
    [[ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
     [-0.          1.         -4.66666667 -4.         -0.33333333  2.        ]
     [ 0.          0.          1.          0.76        0.6        -0.36      ]
     [-0.         -0.         -0.          1.         -2.02511269  0.70315518]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row:  4
    substitution_row:  [-0.        -0.        -0.        -0.         1.        -1.0713345]
    index:  4
    row_to_reduce:  [-0.         -0.         -0.          1.         -2.02511269  0.70315518]
    value to reduced:  -2.0251126851255634
    M[j,:]:  [-0.         -0.         -0.          1.          0.         -1.46641791]
    new matrix:
     [[ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
     [-0.          1.         -4.66666667 -4.         -0.33333333  2.        ]
     [ 0.          0.          1.          0.76        0.6        -0.36      ]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row_to_reduce:  [ 0.    0.    1.    0.76  0.6  -0.36]
    value to reduced:  0.6
    M[j,:]:  [0.        0.        1.        0.76      0.        0.2828007]
    new matrix:
     [[ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
     [-0.          1.         -4.66666667 -4.         -0.33333333  2.        ]
     [ 0.          0.          1.          0.76        0.          0.2828007 ]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row_to_reduce:  [-0.          1.         -4.66666667 -4.         -0.33333333  2.        ]
    value to reduced:  -0.33333333333333304
    M[j,:]:  [-0.          1.         -4.66666667 -4.          0.          1.6428885 ]
    new matrix:
     [[ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
     [-0.          1.         -4.66666667 -4.          0.          1.6428885 ]
     [ 0.          0.          1.          0.76        0.          0.2828007 ]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row_to_reduce:  [ 1.          1.          0.22222222 -0.33333333  1.11111111 -0.33333333]
    value to reduced:  1.1111111111111112
    M[j,:]:  [ 1.          1.          0.22222222 -0.33333333  0.          0.85703834]
    new matrix:
     [[ 1.          1.          0.22222222 -0.33333333  0.          0.85703834]
     [-0.          1.         -4.66666667 -4.          0.          1.6428885 ]
     [ 0.          0.          1.          0.76        0.          0.2828007 ]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row:  3
    substitution_row:  [-0.         -0.         -0.          1.          0.         -1.46641791]
    index:  3
    row_to_reduce:  [0.        0.        1.        0.76      0.        0.2828007]
    value to reduced:  0.76
    M[j,:]:  [0.         0.         1.         0.         0.         1.39727831]
    new matrix:
     [[ 1.          1.          0.22222222 -0.33333333  0.          0.85703834]
     [-0.          1.         -4.66666667 -4.          0.          1.6428885 ]
     [ 0.          0.          1.          0.          0.          1.39727831]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row_to_reduce:  [-0.          1.         -4.66666667 -4.          0.          1.6428885 ]
    value to reduced:  -4.0
    M[j,:]:  [-0.          1.         -4.66666667  0.          0.         -4.22278314]
    new matrix:
     [[ 1.          1.          0.22222222 -0.33333333  0.          0.85703834]
     [-0.          1.         -4.66666667  0.          0.         -4.22278314]
     [ 0.          0.          1.          0.          0.          1.39727831]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row_to_reduce:  [ 1.          1.          0.22222222 -0.33333333  0.          0.85703834]
    value to reduced:  -0.3333333333333333
    M[j,:]:  [1.         1.         0.22222222 0.         0.         0.36823237]
    new matrix:
     [[ 1.          1.          0.22222222  0.          0.          0.36823237]
     [-0.          1.         -4.66666667  0.          0.         -4.22278314]
     [ 0.          0.          1.          0.          0.          1.39727831]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row:  2
    substitution_row:  [0.         0.         1.         0.         0.         1.39727831]
    index:  2
    row_to_reduce:  [-0.          1.         -4.66666667  0.          0.         -4.22278314]
    value to reduced:  -4.666666666666667
    M[j,:]:  [0.         1.         0.         0.         0.         2.29784899]
    new matrix:
     [[ 1.          1.          0.22222222  0.          0.          0.36823237]
     [ 0.          1.          0.          0.          0.          2.29784899]
     [ 0.          0.          1.          0.          0.          1.39727831]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row_to_reduce:  [1.         1.         0.22222222 0.         0.         0.36823237]
    value to reduced:  0.2222222222222222
    M[j,:]:  [1.         1.         0.         0.         0.         0.05772608]
    new matrix:
     [[ 1.          1.          0.          0.          0.          0.05772608]
     [ 0.          1.          0.          0.          0.          2.29784899]
     [ 0.          0.          1.          0.          0.          1.39727831]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row:  1
    substitution_row:  [0.         1.         0.         0.         0.         2.29784899]
    index:  1
    row_to_reduce:  [1.         1.         0.         0.         0.         0.05772608]
    value to reduced:  1.0
    M[j,:]:  [ 1.          0.          0.          0.          0.         -2.24012291]
    new matrix:
     [[ 1.          0.          0.          0.          0.         -2.24012291]
     [ 0.          1.          0.          0.          0.          2.29784899]
     [ 0.          0.          1.          0.          0.          1.39727831]
     [-0.         -0.         -0.          1.          0.         -1.46641791]
     [-0.         -0.         -0.         -0.          1.         -1.0713345 ]]
    row:  0
    substitution_row:  [ 1.          0.          0.          0.          0.         -2.24012291]
    index:  0
    substitution_row:  [-2.24012291  2.29784899  1.39727831 -1.46641791 -1.0713345 ]
    am: [[ -8.  -9. -10.  -9.   7.  -4.   1.]
     [  2.   8.   8.   3.  -8.  -2.  -6.]
     [ -4.   0.   3.   0.   2.   9.  -4.]
     [  2.  -6.  -8.  -2.  -8.   9.  -1.]
     [ -2.  -1.  -3.   3.   4.  -3.  -1.]
     [-10.   1.  -5.  -6.   3.  -4.   9.]]
    [[ -8.  -9. -10.  -9.   7.  -4.   1.]
     [  2.   8.   8.   3.  -8.  -2.  -6.]
     [ -4.   0.   3.   0.   2.   9.  -4.]
     [  2.  -6.  -8.  -2.  -8.   9.  -1.]
     [ -2.  -1.  -3.   3.   4.  -3.  -1.]
     [-10.   1.  -5.  -6.   3.  -4.   9.]]
    pivot -8.0
    value_below_pivot 2.0
    value_below_pivot -4.0
    value_below_pivot 2.0
    value_below_pivot -2.0
    value_below_pivot -10.0
    [[  1.      1.125   1.25    1.125  -0.875   0.5    -0.125]
     [  0.      5.75    5.5     0.75   -6.25   -3.     -5.75 ]
     [  0.      4.5     8.      4.5    -1.5    11.     -4.5  ]
     [  0.     -8.25  -10.5    -4.25   -6.25    8.     -0.75 ]
     [  0.      1.25   -0.5     5.25    2.25   -2.     -1.25 ]
     [  0.     12.25    7.5     5.25   -5.75    1.      7.75 ]]
    pivot 5.75
    value_below_pivot 4.5
    value_below_pivot -8.25
    value_below_pivot 1.25
    value_below_pivot 12.25
    [[  1.           1.125        1.25         1.125       -0.875
        0.5         -0.125     ]
     [  0.           1.           0.95652174   0.13043478  -1.08695652
       -0.52173913  -1.        ]
     [  0.           0.           3.69565217   3.91304348   3.39130435
       13.34782609   0.        ]
     [  0.           0.          -2.60869565  -3.17391304 -15.2173913
        3.69565217  -9.        ]
     [  0.           0.          -1.69565217   5.08695652   3.60869565
       -1.34782609   0.        ]
     [  0.           0.          -4.2173913    3.65217391   7.56521739
        7.39130435  20.        ]]
    pivot 3.695652173913043
    value_below_pivot -2.608695652173913
    value_below_pivot -1.6956521739130435
    value_below_pivot -4.217391304347826
    [[  1.           1.125        1.25         1.125       -0.875
        0.5         -0.125     ]
     [  0.           1.           0.95652174   0.13043478  -1.08695652
       -0.52173913  -1.        ]
     [  0.           0.           1.           1.05882353   0.91764706
        3.61176471   0.        ]
     [  0.           0.           0.          -0.41176471 -12.82352941
       13.11764706  -9.        ]
     [  0.           0.           0.           6.88235294   5.16470588
        4.77647059   0.        ]
     [  0.           0.           0.           8.11764706  11.43529412
       22.62352941  20.        ]]
    pivot -0.41176470588235237
    value_below_pivot 6.882352941176471
    value_below_pivot 8.11764705882353
    [[ 1.00000000e+00  1.12500000e+00  1.25000000e+00  1.12500000e+00
      -8.75000000e-01  5.00000000e-01 -1.25000000e-01]
     [ 0.00000000e+00  1.00000000e+00  9.56521739e-01  1.30434783e-01
      -1.08695652e+00 -5.21739130e-01 -1.00000000e+00]
     [ 0.00000000e+00  0.00000000e+00  1.00000000e+00  1.05882353e+00
       9.17647059e-01  3.61176471e+00  0.00000000e+00]
     [-0.00000000e+00 -0.00000000e+00 -0.00000000e+00  1.00000000e+00
       3.11428571e+01 -3.18571429e+01  2.18571429e+01]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
      -2.09171429e+02  2.24028571e+02 -1.50428571e+02]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
      -2.41371429e+02  2.81228571e+02 -1.57428571e+02]]
    pivot -209.17142857142892
    value_below_pivot -241.371428571429
    [[  1.           1.125        1.25         1.125       -0.875
        0.5         -0.125     ]
     [  0.           1.           0.95652174   0.13043478  -1.08695652
       -0.52173913  -1.        ]
     [  0.           0.           1.           1.05882353   0.91764706
        3.61176471   0.        ]
     [ -0.          -0.          -0.           1.          31.14285714
      -31.85714286  21.85714286]
     [ -0.          -0.          -0.          -0.           1.
       -1.07102855   0.71916405]
     [  0.           0.           0.           0.           0.
       22.71288075  16.15708237]]
    pivot 22.712880753995364
    [[  1.           1.125        1.25         1.125       -0.875
        0.5         -0.125     ]
     [  0.           1.           0.95652174   0.13043478  -1.08695652
       -0.52173913  -1.        ]
     [  0.           0.           1.           1.05882353   0.91764706
        3.61176471   0.        ]
     [ -0.          -0.          -0.           1.          31.14285714
      -31.85714286  21.85714286]
     [ -0.          -0.          -0.          -0.           1.
       -1.07102855   0.71916405]
     [  0.           0.           0.           0.           0.
        1.           0.71136209]]
    row:  5
    substitution_row:  [0.         0.         0.         0.         0.         1.
     0.71136209]
    index:  5
    row_to_reduce:  [-0.         -0.         -0.         -0.          1.         -1.07102855
      0.71916405]
    value to reduced:  -1.0710285480125665
    M[j,:]:  [0.         0.         0.         0.         1.         0.
     1.48105316]
    new matrix:
     [[  1.           1.125        1.25         1.125       -0.875
        0.5         -0.125     ]
     [  0.           1.           0.95652174   0.13043478  -1.08695652
       -0.52173913  -1.        ]
     [  0.           0.           1.           1.05882353   0.91764706
        3.61176471   0.        ]
     [ -0.          -0.          -0.           1.          31.14285714
      -31.85714286  21.85714286]
     [  0.           0.           0.           0.           1.
        0.           1.48105316]
     [  0.           0.           0.           0.           0.
        1.           0.71136209]]
    row_to_reduce:  [ -0.          -0.          -0.           1.          31.14285714
     -31.85714286  21.85714286]
    value to reduced:  -31.857142857142907
    M[j,:]:  [ 0.          0.          0.          1.         31.14285714  0.
     44.51910664]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.5
      -0.125     ]
     [ 0.          1.          0.95652174  0.13043478 -1.08695652 -0.52173913
      -1.        ]
     [ 0.          0.          1.          1.05882353  0.91764706  3.61176471
       0.        ]
     [ 0.          0.          0.          1.         31.14285714  0.
      44.51910664]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [0.         0.         1.         1.05882353 0.91764706 3.61176471
     0.        ]
    value to reduced:  3.6117647058823534
    M[j,:]:  [ 0.          0.          1.          1.05882353  0.91764706  0.
     -2.5692725 ]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.5
      -0.125     ]
     [ 0.          1.          0.95652174  0.13043478 -1.08695652 -0.52173913
      -1.        ]
     [ 0.          0.          1.          1.05882353  0.91764706  0.
      -2.5692725 ]
     [ 0.          0.          0.          1.         31.14285714  0.
      44.51910664]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [ 0.          1.          0.95652174  0.13043478 -1.08695652 -0.52173913
     -1.        ]
    value to reduced:  -0.5217391304347826
    M[j,:]:  [ 0.          1.          0.95652174  0.13043478 -1.08695652  0.
     -0.62885456]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.5
      -0.125     ]
     [ 0.          1.          0.95652174  0.13043478 -1.08695652  0.
      -0.62885456]
     [ 0.          0.          1.          1.05882353  0.91764706  0.
      -2.5692725 ]
     [ 0.          0.          0.          1.         31.14285714  0.
      44.51910664]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [ 1.     1.125  1.25   1.125 -0.875  0.5   -0.125]
    value to reduced:  0.5
    M[j,:]:  [ 1.          1.125       1.25        1.125      -0.875       0.
     -0.48068105]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.
      -0.48068105]
     [ 0.          1.          0.95652174  0.13043478 -1.08695652  0.
      -0.62885456]
     [ 0.          0.          1.          1.05882353  0.91764706  0.
      -2.5692725 ]
     [ 0.          0.          0.          1.         31.14285714  0.
      44.51910664]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row:  4
    substitution_row:  [0.         0.         0.         0.         1.         0.
     1.48105316]
    index:  4
    row_to_reduce:  [ 0.          0.          0.          1.         31.14285714  0.
     44.51910664]
    value to reduced:  31.14285714285719
    M[j,:]:  [ 0.          0.          0.          1.          0.          0.
     -1.60512025]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.
      -0.48068105]
     [ 0.          1.          0.95652174  0.13043478 -1.08695652  0.
      -0.62885456]
     [ 0.          0.          1.          1.05882353  0.91764706  0.
      -2.5692725 ]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [ 0.          0.          1.          1.05882353  0.91764706  0.
     -2.5692725 ]
    value to reduced:  0.9176470588235295
    M[j,:]:  [ 0.          0.          1.          1.05882353  0.          0.
     -3.92835657]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.
      -0.48068105]
     [ 0.          1.          0.95652174  0.13043478 -1.08695652  0.
      -0.62885456]
     [ 0.          0.          1.          1.05882353  0.          0.
      -3.92835657]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [ 0.          1.          0.95652174  0.13043478 -1.08695652  0.
     -0.62885456]
    value to reduced:  -1.0869565217391304
    M[j,:]:  [0.         1.         0.95652174 0.13043478 0.         0.
     0.98098583]
    new matrix:
     [[ 1.          1.125       1.25        1.125      -0.875       0.
      -0.48068105]
     [ 0.          1.          0.95652174  0.13043478  0.          0.
       0.98098583]
     [ 0.          0.          1.          1.05882353  0.          0.
      -3.92835657]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [ 1.          1.125       1.25        1.125      -0.875       0.
     -0.48068105]
    value to reduced:  -0.875
    M[j,:]:  [1.         1.125      1.25       1.125      0.         0.
     0.81524047]
    new matrix:
     [[ 1.          1.125       1.25        1.125       0.          0.
       0.81524047]
     [ 0.          1.          0.95652174  0.13043478  0.          0.
       0.98098583]
     [ 0.          0.          1.          1.05882353  0.          0.
      -3.92835657]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row:  3
    substitution_row:  [ 0.          0.          0.          1.          0.          0.
     -1.60512025]
    index:  3
    row_to_reduce:  [ 0.          0.          1.          1.05882353  0.          0.
     -3.92835657]
    value to reduced:  1.058823529411765
    M[j,:]:  [ 0.          0.          1.          0.          0.          0.
     -2.22881748]
    new matrix:
     [[ 1.          1.125       1.25        1.125       0.          0.
       0.81524047]
     [ 0.          1.          0.95652174  0.13043478  0.          0.
       0.98098583]
     [ 0.          0.          1.          0.          0.          0.
      -2.22881748]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [0.         1.         0.95652174 0.13043478 0.         0.
     0.98098583]
    value to reduced:  0.13043478260869565
    M[j,:]:  [0.         1.         0.95652174 0.         0.         0.
     1.19034934]
    new matrix:
     [[ 1.          1.125       1.25        1.125       0.          0.
       0.81524047]
     [ 0.          1.          0.95652174  0.          0.          0.
       1.19034934]
     [ 0.          0.          1.          0.          0.          0.
      -2.22881748]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [1.         1.125      1.25       1.125      0.         0.
     0.81524047]
    value to reduced:  1.125
    M[j,:]:  [1.         1.125      1.25       0.         0.         0.
     2.62100075]
    new matrix:
     [[ 1.          1.125       1.25        0.          0.          0.
       2.62100075]
     [ 0.          1.          0.95652174  0.          0.          0.
       1.19034934]
     [ 0.          0.          1.          0.          0.          0.
      -2.22881748]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row:  2
    substitution_row:  [ 0.          0.          1.          0.          0.          0.
     -2.22881748]
    index:  2
    row_to_reduce:  [0.         1.         0.95652174 0.         0.         0.
     1.19034934]
    value to reduced:  0.9565217391304348
    M[j,:]:  [0.         1.         0.         0.         0.         0.
     3.32226171]
    new matrix:
     [[ 1.          1.125       1.25        0.          0.          0.
       2.62100075]
     [ 0.          1.          0.          0.          0.          0.
       3.32226171]
     [ 0.          0.          1.          0.          0.          0.
      -2.22881748]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row_to_reduce:  [1.         1.125      1.25       0.         0.         0.
     2.62100075]
    value to reduced:  1.25
    M[j,:]:  [1.        1.125     0.        0.        0.        0.        5.4070226]
    new matrix:
     [[ 1.          1.125       0.          0.          0.          0.
       5.4070226 ]
     [ 0.          1.          0.          0.          0.          0.
       3.32226171]
     [ 0.          0.          1.          0.          0.          0.
      -2.22881748]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row:  1
    substitution_row:  [0.         1.         0.         0.         0.         0.
     3.32226171]
    index:  1
    row_to_reduce:  [1.        1.125     0.        0.        0.        0.        5.4070226]
    value to reduced:  1.125
    M[j,:]:  [1.         0.         0.         0.         0.         0.
     1.66947817]
    new matrix:
     [[ 1.          0.          0.          0.          0.          0.
       1.66947817]
     [ 0.          1.          0.          0.          0.          0.
       3.32226171]
     [ 0.          0.          1.          0.          0.          0.
      -2.22881748]
     [ 0.          0.          0.          1.          0.          0.
      -1.60512025]
     [ 0.          0.          0.          0.          1.          0.
       1.48105316]
     [ 0.          0.          0.          0.          0.          1.
       0.71136209]]
    row:  0
    substitution_row:  [1.         0.         0.         0.         0.         0.
     1.66947817]
    index:  0
    substitution_row:  [ 1.66947817  3.32226171 -2.22881748 -1.60512025  1.48105316  0.71136209]
    am: [[-10.   8.  -8.  -6.   4.   2.  -2.   0.]
     [  3.   1.   6.   2.  -3.  -5. -10.  -5.]
     [  4.   9.  -9.   1.   2.  -9.  -7.   2.]
     [ -2.  -9.   1.   9.   6.  -2.  -2.  -6.]
     [ -3.  -5. -10.   9.   4.   1. -10.   5.]
     [  6.   8.   7.  -3.   6.  -6.   8.   4.]
     [  4.  -8.   5.  -4.   1.   3.   6.  -2.]]
    [[-10.   8.  -8.  -6.   4.   2.  -2.   0.]
     [  3.   1.   6.   2.  -3.  -5. -10.  -5.]
     [  4.   9.  -9.   1.   2.  -9.  -7.   2.]
     [ -2.  -9.   1.   9.   6.  -2.  -2.  -6.]
     [ -3.  -5. -10.   9.   4.   1. -10.   5.]
     [  6.   8.   7.  -3.   6.  -6.   8.   4.]
     [  4.  -8.   5.  -4.   1.   3.   6.  -2.]]
    pivot -10.0
    value_below_pivot 3.0
    value_below_pivot 4.0
    value_below_pivot -2.0
    value_below_pivot -3.0
    value_below_pivot 6.0
    value_below_pivot 4.0
    [[  1.   -0.8   0.8   0.6  -0.4  -0.2   0.2  -0. ]
     [  0.    3.4   3.6   0.2  -1.8  -4.4 -10.6  -5. ]
     [  0.   12.2 -12.2  -1.4   3.6  -8.2  -7.8   2. ]
     [  0.  -10.6   2.6  10.2   5.2  -2.4  -1.6  -6. ]
     [  0.   -7.4  -7.6  10.8   2.8   0.4  -9.4   5. ]
     [  0.   12.8   2.2  -6.6   8.4  -4.8   6.8   4. ]
     [  0.   -4.8   1.8  -6.4   2.6   3.8   5.2  -2. ]]
    pivot 3.4000000000000004
    value_below_pivot 12.2
    value_below_pivot -10.6
    value_below_pivot -7.4
    value_below_pivot 12.8
    value_below_pivot -4.8
    [[  1.          -0.8          0.8          0.6         -0.4
       -0.2          0.2         -0.        ]
     [  0.           1.           1.05882353   0.05882353  -0.52941176
       -1.29411765  -3.11764706  -1.47058824]
     [  0.           0.         -25.11764706  -2.11764706  10.05882353
        7.58823529  30.23529412  19.94117647]
     [  0.           0.          13.82352941  10.82352941  -0.41176471
      -16.11764706 -34.64705882 -21.58823529]
     [  0.           0.           0.23529412  11.23529412  -1.11764706
       -9.17647059 -32.47058824  -5.88235294]
     [  0.           0.         -11.35294118  -7.35294118  15.17647059
       11.76470588  46.70588235  22.82352941]
     [  0.           0.           6.88235294  -6.11764706   0.05882353
       -2.41176471  -9.76470588  -9.05882353]]
    pivot -25.117647058823525
    value_below_pivot 13.823529411764703
    value_below_pivot 0.235294117647058
    value_below_pivot -11.352941176470587
    value_below_pivot 6.882352941176469
    [[  1.          -0.8          0.8          0.6         -0.4
       -0.2          0.2         -0.        ]
     [  0.           1.           1.05882353   0.05882353  -0.52941176
       -1.29411765  -3.11764706  -1.47058824]
     [ -0.          -0.           1.           0.08430913  -0.40046838
       -0.30210773  -1.20374707  -0.79391101]
     [  0.           0.           0.           9.65807963   5.12412178
      -11.94145199 -18.00702576 -10.61358314]
     [  0.           0.           0.          11.21545667  -1.0234192
       -9.10538642 -32.18735363  -5.69555035]
     [  0.           0.           0.          -6.39578454  10.62997658
        8.33489461  33.03981265  13.81030445]
     [  0.           0.           0.          -6.69789227   2.81498829
       -0.33255269  -1.48009368  -3.59484778]]
    pivot 9.65807962529274
    value_below_pivot 11.215456674473069
    value_below_pivot -6.395784543325527
    value_below_pivot -6.697892271662764
    [[  1.          -0.8          0.8          0.6         -0.4
       -0.2          0.2         -0.        ]
     [  0.           1.           1.05882353   0.05882353  -0.52941176
       -1.29411765  -3.11764706  -1.47058824]
     [ -0.          -0.           1.           0.08430913  -0.40046838
       -0.30210773  -1.20374707  -0.79391101]
     [  0.           0.           0.           1.           0.53055286
       -1.23642095  -1.86445199  -1.09893307]
     [  0.           0.           0.           0.          -6.97381183
        4.76163919 -11.27667313   6.62948594]
     [  0.           0.           0.           0.          14.02327837
        0.42701261  21.11517944   6.78176528]
     [  0.           0.           0.           0.           6.3685742
       -8.61396702 -13.96799224 -10.95538312]]
    pivot -6.9738118331716805
    value_below_pivot 14.023278370514065
    value_below_pivot 6.368574199806014
    [[  1.          -0.8          0.8          0.6         -0.4
       -0.2          0.2         -0.        ]
     [  0.           1.           1.05882353   0.05882353  -0.52941176
       -1.29411765  -3.11764706  -1.47058824]
     [ -0.          -0.           1.           0.08430913  -0.40046838
       -0.30210773  -1.20374707  -0.79391101]
     [  0.           0.           0.           1.           0.53055286
       -1.23642095  -1.86445199  -1.09893307]
     [ -0.          -0.          -0.          -0.           1.
       -0.6827886    1.61700278  -0.95062587]
     [  0.           0.           0.           0.           0.
       10.00194715  -1.5605007   20.11265647]
     [  0.           0.           0.           0.           0.
       -4.26557719 -24.26599444  -4.90125174]]
    pivot 10.0019471488178
    value_below_pivot -4.26557719054242
    [[  1.          -0.8          0.8          0.6         -0.4
       -0.2          0.2         -0.        ]
     [  0.           1.           1.05882353   0.05882353  -0.52941176
       -1.29411765  -3.11764706  -1.47058824]
     [ -0.          -0.           1.           0.08430913  -0.40046838
       -0.30210773  -1.20374707  -0.79391101]
     [  0.           0.           0.           1.           0.53055286
       -1.23642095  -1.86445199  -1.09893307]
     [ -0.          -0.          -0.          -0.           1.
       -0.6827886    1.61700278  -0.95062587]
     [  0.           0.           0.           0.           0.
        1.          -0.15601969   2.0108741 ]
     [  0.           0.           0.           0.           0.
        0.         -24.93150847   3.67628695]]
    pivot -24.931508468448406
    [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.2        -0.        ]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      -3.11764706 -1.47058824]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
      -1.20374707 -0.79391101]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
      -1.86445199 -1.09893307]
     [-0.         -0.         -0.         -0.          1.         -0.6827886
       1.61700278 -0.95062587]
     [ 0.          0.          0.          0.          0.          1.
      -0.15601969  2.0108741 ]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  6
    substitution_row:  [-0.         -0.         -0.         -0.         -0.         -0.
      1.         -0.14745546]
    index:  6
    row_to_reduce:  [ 0.          0.          0.          0.          0.          1.
     -0.15601969  2.0108741 ]
    value to reduced:  -0.15601969018549675
    M[j,:]:  [0.         0.         0.         0.         0.         1.
     0.         1.98786815]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.2        -0.        ]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      -3.11764706 -1.47058824]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
      -1.20374707 -0.79391101]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
      -1.86445199 -1.09893307]
     [-0.         -0.         -0.         -0.          1.         -0.6827886
       1.61700278 -0.95062587]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [-0.         -0.         -0.         -0.          1.         -0.6827886
      1.61700278 -0.95062587]
    value to reduced:  1.6170027816411663
    M[j,:]:  [ 0.          0.          0.          0.          1.         -0.6827886
      0.         -0.71218999]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.2        -0.        ]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      -3.11764706 -1.47058824]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
      -1.20374707 -0.79391101]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
      -1.86445199 -1.09893307]
     [ 0.          0.          0.          0.          1.         -0.6827886
       0.         -0.71218999]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 0.          0.          0.          1.          0.53055286 -1.23642095
     -1.86445199 -1.09893307]
    value to reduced:  -1.864451988360815
    M[j,:]:  [ 0.          0.          0.          1.          0.53055286 -1.23642095
      0.         -1.37385669]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.2        -0.        ]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      -3.11764706 -1.47058824]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
      -1.20374707 -0.79391101]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
       0.         -1.37385669]
     [ 0.          0.          0.          0.          1.         -0.6827886
       0.         -0.71218999]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
     -1.20374707 -0.79391101]
    value to reduced:  -1.2037470725995314
    M[j,:]:  [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
      0.         -0.97141008]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.2        -0.        ]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      -3.11764706 -1.47058824]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
       0.         -0.97141008]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
       0.         -1.37385669]
     [ 0.          0.          0.          0.          1.         -0.6827886
       0.         -0.71218999]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
     -3.11764706 -1.47058824]
    value to reduced:  -3.117647058823529
    M[j,:]:  [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      0.         -1.9303023 ]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.2        -0.        ]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
       0.         -1.9303023 ]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
       0.         -0.97141008]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
       0.         -1.37385669]
     [ 0.          0.          0.          0.          1.         -0.6827886
       0.         -0.71218999]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 1.  -0.8  0.8  0.6 -0.4 -0.2  0.2 -0. ]
    value to reduced:  0.2
    M[j,:]:  [ 1.         -0.8         0.8         0.6        -0.4        -0.2
      0.          0.02949109]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.          0.02949109]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
       0.         -1.9303023 ]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
       0.         -0.97141008]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
       0.         -1.37385669]
     [ 0.          0.          0.          0.          1.         -0.6827886
       0.         -0.71218999]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  5
    substitution_row:  [0.         0.         0.         0.         0.         1.
     0.         1.98786815]
    index:  5
    row_to_reduce:  [ 0.          0.          0.          0.          1.         -0.6827886
      0.         -0.71218999]
    value to reduced:  -0.68278859527121
    M[j,:]:  [0.         0.         0.         0.         1.         0.
     0.         0.64510371]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.          0.02949109]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
       0.         -1.9303023 ]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
       0.         -0.97141008]
     [ 0.          0.          0.          1.          0.53055286 -1.23642095
       0.         -1.37385669]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 0.          0.          0.          1.          0.53055286 -1.23642095
      0.         -1.37385669]
    value to reduced:  -1.2364209505334627
    M[j,:]:  [0.         0.         0.         1.         0.53055286 0.
     0.         1.08398513]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.          0.02949109]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
       0.         -1.9303023 ]
     [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
       0.         -0.97141008]
     [ 0.          0.          0.          1.          0.53055286  0.
       0.          1.08398513]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [-0.         -0.          1.          0.08430913 -0.40046838 -0.30210773
      0.         -0.97141008]
    value to reduced:  -0.30210772833723654
    M[j,:]:  [ 0.          0.          1.          0.08430913 -0.40046838  0.
      0.         -0.37085975]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.          0.02949109]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
       0.         -1.9303023 ]
     [ 0.          0.          1.          0.08430913 -0.40046838  0.
       0.         -0.37085975]
     [ 0.          0.          0.          1.          0.53055286  0.
       0.          1.08398513]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 0.          1.          1.05882353  0.05882353 -0.52941176 -1.29411765
      0.         -1.9303023 ]
    value to reduced:  -1.2941176470588234
    M[j,:]:  [ 0.          1.          1.05882353  0.05882353 -0.52941176  0.
      0.          0.64223294]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4        -0.2
       0.          0.02949109]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176  0.
       0.          0.64223294]
     [ 0.          0.          1.          0.08430913 -0.40046838  0.
       0.         -0.37085975]
     [ 0.          0.          0.          1.          0.53055286  0.
       0.          1.08398513]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 1.         -0.8         0.8         0.6        -0.4        -0.2
      0.          0.02949109]
    value to reduced:  -0.2
    M[j,:]:  [ 1.         -0.8         0.8         0.6        -0.4         0.
      0.          0.42706472]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4         0.
       0.          0.42706472]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176  0.
       0.          0.64223294]
     [ 0.          0.          1.          0.08430913 -0.40046838  0.
       0.         -0.37085975]
     [ 0.          0.          0.          1.          0.53055286  0.
       0.          1.08398513]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  4
    substitution_row:  [0.         0.         0.         0.         1.         0.
     0.         0.64510371]
    index:  4
    row_to_reduce:  [0.         0.         0.         1.         0.53055286 0.
     0.         1.08398513]
    value to reduced:  0.5305528612997091
    M[j,:]:  [0.         0.         0.         1.         0.         0.
     0.         0.74172351]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4         0.
       0.          0.42706472]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176  0.
       0.          0.64223294]
     [ 0.          0.          1.          0.08430913 -0.40046838  0.
       0.         -0.37085975]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 0.          0.          1.          0.08430913 -0.40046838  0.
      0.         -0.37085975]
    value to reduced:  -0.40046838407494145
    M[j,:]:  [ 0.          0.          1.          0.08430913  0.          0.
      0.         -0.11251611]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4         0.
       0.          0.42706472]
     [ 0.          1.          1.05882353  0.05882353 -0.52941176  0.
       0.          0.64223294]
     [ 0.          0.          1.          0.08430913  0.          0.
       0.         -0.11251611]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 0.          1.          1.05882353  0.05882353 -0.52941176  0.
      0.          0.64223294]
    value to reduced:  -0.5294117647058822
    M[j,:]:  [0.         1.         1.05882353 0.05882353 0.         0.
     0.         0.98375844]
    new matrix:
     [[ 1.         -0.8         0.8         0.6        -0.4         0.
       0.          0.42706472]
     [ 0.          1.          1.05882353  0.05882353  0.          0.
       0.          0.98375844]
     [ 0.          0.          1.          0.08430913  0.          0.
       0.         -0.11251611]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 1.         -0.8         0.8         0.6        -0.4         0.
      0.          0.42706472]
    value to reduced:  -0.4
    M[j,:]:  [ 1.        -0.8        0.8        0.6        0.         0.
      0.         0.6851062]
    new matrix:
     [[ 1.         -0.8         0.8         0.6         0.          0.
       0.          0.6851062 ]
     [ 0.          1.          1.05882353  0.05882353  0.          0.
       0.          0.98375844]
     [ 0.          0.          1.          0.08430913  0.          0.
       0.         -0.11251611]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  3
    substitution_row:  [0.         0.         0.         1.         0.         0.
     0.         0.74172351]
    index:  3
    row_to_reduce:  [ 0.          0.          1.          0.08430913  0.          0.
      0.         -0.11251611]
    value to reduced:  0.08430913348946134
    M[j,:]:  [ 0.          0.          1.          0.          0.          0.
      0.         -0.17505018]
    new matrix:
     [[ 1.         -0.8         0.8         0.6         0.          0.
       0.          0.6851062 ]
     [ 0.          1.          1.05882353  0.05882353  0.          0.
       0.          0.98375844]
     [ 0.          0.          1.          0.          0.          0.
       0.         -0.17505018]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [0.         1.         1.05882353 0.05882353 0.         0.
     0.         0.98375844]
    value to reduced:  0.05882352941176462
    M[j,:]:  [0.         1.         1.05882353 0.         0.         0.
     0.         0.94012764]
    new matrix:
     [[ 1.         -0.8         0.8         0.6         0.          0.
       0.          0.6851062 ]
     [ 0.          1.          1.05882353  0.          0.          0.
       0.          0.94012764]
     [ 0.          0.          1.          0.          0.          0.
       0.         -0.17505018]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 1.        -0.8        0.8        0.6        0.         0.
      0.         0.6851062]
    value to reduced:  0.6000000000000001
    M[j,:]:  [ 1.        -0.8        0.8        0.         0.         0.
      0.         0.2400721]
    new matrix:
     [[ 1.         -0.8         0.8         0.          0.          0.
       0.          0.2400721 ]
     [ 0.          1.          1.05882353  0.          0.          0.
       0.          0.94012764]
     [ 0.          0.          1.          0.          0.          0.
       0.         -0.17505018]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  2
    substitution_row:  [ 0.          0.          1.          0.          0.          0.
      0.         -0.17505018]
    index:  2
    row_to_reduce:  [0.         1.         1.05882353 0.         0.         0.
     0.         0.94012764]
    value to reduced:  1.0588235294117645
    M[j,:]:  [0.         1.         0.         0.         0.         0.
     0.         1.12547489]
    new matrix:
     [[ 1.         -0.8         0.8         0.          0.          0.
       0.          0.2400721 ]
     [ 0.          1.          0.          0.          0.          0.
       0.          1.12547489]
     [ 0.          0.          1.          0.          0.          0.
       0.         -0.17505018]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row_to_reduce:  [ 1.        -0.8        0.8        0.         0.         0.
      0.         0.2400721]
    value to reduced:  0.8
    M[j,:]:  [ 1.         -0.8         0.          0.          0.          0.
      0.          0.38011224]
    new matrix:
     [[ 1.         -0.8         0.          0.          0.          0.
       0.          0.38011224]
     [ 0.          1.          0.          0.          0.          0.
       0.          1.12547489]
     [ 0.          0.          1.          0.          0.          0.
       0.         -0.17505018]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  1
    substitution_row:  [0.         1.         0.         0.         0.         0.
     0.         1.12547489]
    index:  1
    row_to_reduce:  [ 1.         -0.8         0.          0.          0.          0.
      0.          0.38011224]
    value to reduced:  -0.8
    M[j,:]:  [1.         0.         0.         0.         0.         0.
     0.         1.28049215]
    new matrix:
     [[ 1.          0.          0.          0.          0.          0.
       0.          1.28049215]
     [ 0.          1.          0.          0.          0.          0.
       0.          1.12547489]
     [ 0.          0.          1.          0.          0.          0.
       0.         -0.17505018]
     [ 0.          0.          0.          1.          0.          0.
       0.          0.74172351]
     [ 0.          0.          0.          0.          1.          0.
       0.          0.64510371]
     [ 0.          0.          0.          0.          0.          1.
       0.          1.98786815]
     [-0.         -0.         -0.         -0.         -0.         -0.
       1.         -0.14745546]]
    row:  0
    substitution_row:  [1.         0.         0.         0.         0.         0.
     0.         1.28049215]
    index:  0
    substitution_row:  [ 1.28049215  1.12547489 -0.17505018  0.74172351  0.64510371  1.98786815
     -0.14745546]
    [92m All tests passed


<a name="7"></a>
## 7 - Test with any system of equations!

The code below will allow you to write any equation in the format it is given below (any unknown lower case variables are accepted, in any order) and transform it in its respective augmented matrix so you can solve it using the functions you just wrote in this assignment!

You just need to change the equations variable, always keeping * to indicate product between unknowns and variables and one equation in each line!


```python
from utils import string_to_augmented_matrix
```


```python
equations = """
3*x + 6*y + 6*w + 8*z = 1
5*x + 3*y + 6*w = -10
4*y - 5*w + 8*z = 8
4*w + 8*z = 9
"""

variables, A, B = string_to_augmented_matrix(equations)

sols = gaussian_elimination(A, B)

if not isinstance(sols, str):
    for variable, solution in zip(variables.split(' '),sols):
        print(f"{variable} = {solution:.4f}")
else:
    print(sols)
```

    am: [[  3.   6.   6.   8.   1.]
     [  5.   3.   6.   0. -10.]
     [  0.   4.  -5.   8.   8.]
     [  0.   0.   4.   8.   9.]]
    [[  3.   6.   6.   8.   1.]
     [  5.   3.   6.   0. -10.]
     [  0.   4.  -5.   8.   8.]
     [  0.   0.   4.   8.   9.]]
    pivot 3.0
    value_below_pivot 5.0
    value_below_pivot 0.0
    value_below_pivot 0.0
    [[  1.           2.           2.           2.66666667   0.33333333]
     [  0.          -7.          -4.         -13.33333333 -11.66666667]
     [  0.           4.          -5.           8.           8.        ]
     [  0.           0.           4.           8.           9.        ]]
    pivot -7.0
    value_below_pivot 4.0
    value_below_pivot 0.0
    [[ 1.          2.          2.          2.66666667  0.33333333]
     [-0.          1.          0.57142857  1.9047619   1.66666667]
     [ 0.          0.         -7.28571429  0.38095238  1.33333333]
     [ 0.          0.          4.          8.          9.        ]]
    pivot -7.285714285714286
    value_below_pivot 4.0
    [[ 1.          2.          2.          2.66666667  0.33333333]
     [-0.          1.          0.57142857  1.9047619   1.66666667]
     [-0.         -0.          1.         -0.05228758 -0.18300654]
     [ 0.          0.          0.          8.20915033  9.73202614]]
    pivot 8.209150326797387
    [[ 1.          2.          2.          2.66666667  0.33333333]
     [-0.          1.          0.57142857  1.9047619   1.66666667]
     [-0.         -0.          1.         -0.05228758 -0.18300654]
     [ 0.          0.          0.          1.          1.18550955]]
    row:  3
    substitution_row:  [0.         0.         0.         1.         1.18550955]
    index:  3
    row_to_reduce:  [-0.         -0.          1.         -0.05228758 -0.18300654]
    value to reduced:  -0.05228758169934659
    M[j,:]:  [ 0.          0.          1.          0.         -0.12101911]
    new matrix:
     [[ 1.          2.          2.          2.66666667  0.33333333]
     [-0.          1.          0.57142857  1.9047619   1.66666667]
     [ 0.          0.          1.          0.         -0.12101911]
     [ 0.          0.          0.          1.          1.18550955]]
    row_to_reduce:  [-0.          1.          0.57142857  1.9047619   1.66666667]
    value to reduced:  1.9047619047619044
    M[j,:]:  [-0.          1.          0.57142857  0.         -0.59144677]
    new matrix:
     [[ 1.          2.          2.          2.66666667  0.33333333]
     [-0.          1.          0.57142857  0.         -0.59144677]
     [ 0.          0.          1.          0.         -0.12101911]
     [ 0.          0.          0.          1.          1.18550955]]
    row_to_reduce:  [1.         2.         2.         2.66666667 0.33333333]
    value to reduced:  2.6666666666666665
    M[j,:]:  [ 1.          2.          2.          0.         -2.82802548]
    new matrix:
     [[ 1.          2.          2.          0.         -2.82802548]
     [-0.          1.          0.57142857  0.         -0.59144677]
     [ 0.          0.          1.          0.         -0.12101911]
     [ 0.          0.          0.          1.          1.18550955]]
    row:  2
    substitution_row:  [ 0.          0.          1.          0.         -0.12101911]
    index:  2
    row_to_reduce:  [-0.          1.          0.57142857  0.         -0.59144677]
    value to reduced:  0.5714285714285714
    M[j,:]:  [-0.          1.          0.          0.         -0.52229299]
    new matrix:
     [[ 1.          2.          2.          0.         -2.82802548]
     [-0.          1.          0.          0.         -0.52229299]
     [ 0.          0.          1.          0.         -0.12101911]
     [ 0.          0.          0.          1.          1.18550955]]
    row_to_reduce:  [ 1.          2.          2.          0.         -2.82802548]
    value to reduced:  2.0
    M[j,:]:  [ 1.          2.          0.          0.         -2.58598726]
    new matrix:
     [[ 1.          2.          0.          0.         -2.58598726]
     [-0.          1.          0.          0.         -0.52229299]
     [ 0.          0.          1.          0.         -0.12101911]
     [ 0.          0.          0.          1.          1.18550955]]
    row:  1
    substitution_row:  [-0.          1.          0.          0.         -0.52229299]
    index:  1
    row_to_reduce:  [ 1.          2.          0.          0.         -2.58598726]
    value to reduced:  2.0
    M[j,:]:  [ 1.          0.          0.          0.         -1.54140127]
    new matrix:
     [[ 1.          0.          0.          0.         -1.54140127]
     [-0.          1.          0.          0.         -0.52229299]
     [ 0.          0.          1.          0.         -0.12101911]
     [ 0.          0.          0.          1.          1.18550955]]
    row:  0
    substitution_row:  [ 1.          0.          0.          0.         -1.54140127]
    index:  0
    substitution_row:  [-1.54140127 -0.52229299 -0.12101911  1.18550955]
    x = -1.5414
    y = -0.5223
    w = -0.1210
    z = 1.1855


Congratulations! You have finished the first assignment of this course! You built from scratch a linear system solver!
