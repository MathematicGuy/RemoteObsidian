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
	Understand [[Determinant]] = Volumn of the New Vector / Volumn of Old Vector  
	EXPLAIN [[Singular Matrix]]. WHY DET <= 0 IS SINGULAR  
	WHY MATRIX HAVE TO BE SQUARE

+ Eigen value in physic also present ressonant frequecy - tần số vọng lại


## Row Echelon
Row Echelon we aim to reduced the Matrix so that all value below the [[matrix pivot]] are 0:
$$
\left[ \begin{array}{ccc|c} 0 & 2 & 1 & 3 \\ 1 & 1 & 1 & 6 \\ 1 & 2 & 1 & 12 \\ \end{array} \right]

\rightarrow

\left[ \begin{array}{ccc|c} 1 & 2 & 3 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 5 & 4 \\ \end{array} \right]
$$

### Let go from the start to understand how:
$$
\left[ \begin{array}{ccc|c} 0 & 2 & 1 & 3 \\ 1 & 1 & 1 & 6 \\ 1 & 2 & 1 & 12 \\ \end{array} \right]
$$
To turn the Matrix using Row Echelon, we have to follow these rule:
+ All values to the left of the pivot must be all 0
+ All value along the diagnol must be 1
+ 




#### 1st Step: All Pivot must be 1
> in other word values along the Diagnol must be 1. In Row Echelon we multiply matrix rows with its pivot. For example, `Row1 * 1/Row1_Pivot -> Row1`    
+ Ex: $$[2, 2, 4] * 1 / 2 \rightarrow [1, 1, 2]$$ Now the  as 1, we can assign it as the pivot (of the 1st row)

+ To make it easier to code, we call and Value as pivot_candidate:
	Pivot 


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