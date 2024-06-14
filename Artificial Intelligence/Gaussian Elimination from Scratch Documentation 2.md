# Thing to understand first



### 1) [Augumented Matrix](https://tutorial.math.lamar.edu/classes/alg/augmentedmatrix.aspx): 
> An **augmented matrix** for a system of equations is a matrix of numbers in which **each row represents the constants from one equation** 
 + ? *X have 7 as contant in Row 1*


### *Coefficients and Constant of a Matrix*
 >Having the **coefficients on the left** and the **constant on the right** of the equal sign and **each column represents all the coefficients for a single variable** 
+ ? As you can see *X is the coefficients of column 1, likewise Y for column 2, Z for column 3*
Let’s take a look at an example. Here is the system of equations that we looked at in the previous section.
$$
% System of linear equations
\begin{align*}
x - 2y + 3z &= 7 \\
2x + y + z &= 4 \\
-3x + 2y - 2z &= -10
\end{align*}

\rightarrow 
% Augmented matrix
\left[ \begin{array}{ccc|c}
1 & -2 & 3 & 7 \\
2 & 1 & 1 & 4 \\
-3 & 2 & -2 & -10 \\
\end{array} \right]
$$
 

### Pivot
> Values in the Matrix's Diagnol line 


# Prequisites   
### The Matrix must not be Singular
+ ? If the Determinant of the Matrix <= 0 it is Singular
	Matrix must be Square to calc Determinant

+ ? TODO
	Understand DETERMINANT = Volumn of the New Vector / Volumn of Old Vector  
	EXPLAIN SINGULAR. WHY DET <= 0 IS SINGULAR  
	WHY MATRIX HAVE TO BE SQUARE

## The First Pivot must be 1
>  The First Value along the Diagnol must be 1.
+ Here how to do it:
	New_Value  = Value * 1 / Value 
+ Ex: $$1 = 5 * (1 / 5)$$ Now having the New_Value as 1, we can assign it as pivot
+ Or in Row Echelon 
## Row Echelon
Row Echelon we aim to reduced the Matrix so that all value below the [[matrix pivot]] are 0:
$$
\left[ \begin{array}{ccc|c}
1 & -2 & 3 & 7 \\
0 & 1 & 1 & 4 \\
0 & 0 & 1 & -10 \\
\end{array} \right]
$$
Here how:


## Back Substitution
Back Substitution aim to reduced the Matrix so that all value above the [[matrix pivot]] are 0

$$
\left[ \begin{array}{ccc|c}
1 & 0 & 0 & 65 \\
0 & 1 & 0 & 14 \\
0 & 0 & 1 & -10 \\
\end{array} \right]
$$
Here how: