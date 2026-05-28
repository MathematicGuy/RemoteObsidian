### Structure of an Augmented Matrix

Consider a system of linear equations:
$$
\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \\ \end{cases} 
$$
​
Here, $a_i,_j$  are the coefficients of the variables
 $x_1,x_2,…,x_n \;and \; b_i$ are the constants on the right-hand side. The augmented matrix for this system is:
$$
\left[\begin{array}{cccc|c}
a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \\
\end{array}\right]
$$


**Row Operations**
To solve the system of equations, we often use row operations to transform the augmented matrix into a simpler form, typically row echelon form (REF) or reduced row echelon form (RREF). The row operations are:

1) Swap Rows: Swap the positions of two rows.
2) Scale a Row: Multiply all elements of a row by a nonzero scalar.
3) Row Addition: Add or subtract a multiple of one row to/from another row.

## Example System of Linear Equations
Consider the system:
$$
\begin{cases}
x + 2y + 3z = 9 \\
2x + 3y + z = 8 \\
3x + y + 2z = 7 \\
\end{cases}
$$
​
The augmented matrix is:
$$
\left[\begin{array}{ccc|c} 1 & 2 & 3 & 9 \\ 2 & 3 & 1 & 8 \\ 3 & 1 & 2 & 7 \\ \end{array}\right]
$$

We can perform row operations to simplify this matrix. For instance, we might start by subtracting twice the first row from the second row and three times the first row from the third row to eliminate the xx-terms below the first row.
**Applications**
1) Solving Systems of Linear Equations: By transforming the augmented matrix to RREF, we can directly read off the solutions to the system of equations.
2) Finding Inverses of Matrices: The process of row reducing an augmented matrix can be used to find the inverse of a matrix by augmenting it with the identity matrix.
3) Linear Transformations: Augmented matrices can represent transformations and solve related problems.

**Conclusion**
Augmented matrices are a powerful tool in linear algebra, providing a systematic method for solving systems of linear equations. They simplify many operations and help visualize the process of finding solutions through row operations.

