w
To Begin I will divided this into 2 part:
+ **The Algorithm as a Whole** and **Algorithm as Code**

# The Algorithm as a Whole

Guassian Elimination include **Row Echelon Form** and **Back-Substitution** 
1) Simplified Matrix to Row Echelon Form
	Original Matrix: $$
	M = 
	\begin{bmatrix} 
	1 & 1 & 1 & | & 6 \\
	0 & 2 & 1 & | & 3 \\
	1 & 2 & 1 & | & 12 
	\end{bmatrix}
	$$
	Row Echelon Form can be Created by Following these Conditions 
	- Rows consisting entirely of zeroes should be positioned at the bottom.
	- Each **non-zeros row must have its left-most coefficient (also know as Pivot) locate to the right of any row above it.**
		Consequently, all number below Matrix's Diagnol should be 0$$
M = 
\begin{bmatrix} 
\phantom{-}1 & \phantom{-}1 & \phantom{-}1 & | & \phantom{-}6 \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}\frac{1}{2} & | & \phantom{-}\frac{3}{2} \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -9 
\end{bmatrix}
$$ 
	+ [[A worked example of Row Echelon]]
	
2) If Matrix is **not in Singular form** then **applied Back-Substitution**
	This method like row-echelon form but in reverse. This method start from the bottom and move upwards to convert every element above the pivot into zeros. 
	The fomula employed is: $$\text{Row above} \rightarrow \text{Row above} - \text{value} \cdot \text{Row pivot}$$
	Ending the matrix with Reduced Row Echelon Form Matrix: $$
M = 
\begin{bmatrix} 
\phantom{-}1 & \phantom{-}0 & \phantom{-}0 & | & \phantom{-}1  \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}0 & | & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -1
\end{bmatrix}
$$ 
+ [[A work example of Back-Substitution]] 
+ ? To see 2 example all at one. Open 2 file and Drag them side-by-side for the full experience.


+ $ **Open work of example side by side** with **the algorithm for Visual understanding**.
**Echelon Form Algorithm**
1) Check if the Matrix A (coefficient matrix) has non-zero determinent (not singular) -> calculatable
2) Combine Matrix A & B to make a augmented_matrix
3) For each Row in the augmented_matrix
	+ Select value in the diagnol as the candidate Pivot
	+  If the Pivot is zero then
		get the index of the first non-zero value below the pivot
		Swap the current row with founded row index  
		Re-define the Pivot. (Because the diagnol value has been changed when rows swapped)  
	+  Else Pivot = candidate_pivot
	+  pivot_row = Divide the current Row to its pivot (Ex: R1 = 1/pivot * R1)
	+ Perform row reduction **for each rows below the current row**
		+ get the value below the pivot
		+ **row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row**
			+ note: yes, value_below_pivot is in the same column as the pivot.
	Return Row Echelon Form

**Back Substitution Algorithm**
1) Take Row Echelon Form Matrix as parameter
2) Iterate from bottom to top (for each row of the matrix in reverse)
	+ for each row of the matrix **in reverse** (row order: 3,2,1)
		**substitution_row** = row (start with 3)
		**index** = first non-zero value from the substitution_row 
		for each row above the substitution_row (Ex: range = 3, rows = 2,1,0)
			**row_to_reduce** = row 
			get the **value** above **index**
			perform back substitution with the fomula:
				**row_to_reduce -> row_to_reduce - value * substitution_row**
			Update the real row above the pivot with row_to_reduce
	Return the solution (the last matrix column)
+ ? At the last iteration. When row = 0 -> row_to_reduce = 0 as well.

# Algorithm as Code

Before getting started in Row Echelon Form and Back Substitution, let understand the 4 basic functions:

+ **Augumented_matrix(A, B) -> Staking Matrix A and B together**
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
+ **get_index_first_non_zero_value_from_column(M, row, row)**
	get index of the first non zero value of the column
+ **get_index_first_non_zero_value_from_row(M, row, augmented = False)**
	get index of the first non zero value of the row
+ **M = swap_rows(M, row, first_non_zero_value_below_pivot_candidate)** 
	Swap 2 row using row's index

+ ! This function combine the Square Matrix (NxN matrix) with a Column Matrix (result constance) to create a full matrix.
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


+ ! Get row pivot by indexes (pivot is numbers align with the diagnol)
```Python
pivot_candidate = M[None, None] # row, column index
```

+ ! Non-zero from Column
```python
def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
    int or False: The index of the first non-zero value in the specified column, starting from the given row.
	Returns False if no non-zero value is found.
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
    # If no non-zero value is found below it, return None.
    return False
```
Scan each single Column of the matrix from top down.
[[ 0  5 -3  6  8]
 [ 0  6  3  8  1]
 [ 0  0  0  0  0]
 [ 0  0  0  0  7]
 [ 0  2  1  0  4]]
```python
print(get_index_first_non_zero_value_from_column(N, column = -1, starting_row = 2))
```
> Scan column -1 mean col 1 in reverse. Which is col 4. 
> Start from row 2. 
> -> Scan column 4 starting from row 2. From top to bottom and we found 7 at index 3 is non-zero. So return 3.


+ ! swap 2 row by row's index (or switch 2 Rows using its column indexs)
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
    M = M.copy()
    # Swap indexes
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M
```

+ ! Non-zero from Row
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
    int or False: The index of the first non-zero value in the specified row.
	Returns False if no non-zero value is found.
    """

    # Create a copy to avoid modifying the original matrix
    M = M.copy()


    # If it is an augmented matrix, then ignore the constant values
    if augmented == True:
        # Isolating the coefficient matrix (removing the constant terms)
        # Slice the Matrix except the last column on the right hand side(bc         it present the result constance )
        M = M[:,:-1]
        
    # Get the desired row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns None.
        # check if val is close to 0 within atol tolerent
        if not np.isclose(val, 0, atol = 1e-5):
            return i
    return False
```

- `np.isclose` checks if `val` is approximately zero (within a tolerance of 1e-5). If `val` is not close to zero, the index `i` is immediately returned.
Example
```python
matrix = np.array([
    [0, 0, 3, 5],
    [1, 2, 0, 0],
    [0, 0, 0, 0] 
])

# Find the first non-zero index in row 0
result = get_index_first_non_zero_value_from_row(matrix, 0)  
print(result)  # Output: 2

# Find the first non-zero index in row 2 (which doesn't exist)
result = get_index_first_non_zero_value_from_row(matrix, 2)  
print(result)  # Output: False 
```




**Row Echelon Form**
```python
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


**Back Substitution**
```python
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



# Gaussian Elimination (bringing it all together)
+ Matrix -> Row Echelon Form
+ If not singular -> Back Substitution
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