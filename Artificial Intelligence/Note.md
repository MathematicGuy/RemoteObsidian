
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
**Exercise 1:** If they equate to 0, an attempt to swap rows should be made to obtain a non-zero value.

