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

The first row operation involves **scaling by the pivot's inverse**. Since the value in the main diagonal is $0$, necessitating (đòi hỏi) a non-zero value for scaling by its inverse, you must switch rows in this case. Note that $R_1$ has a value different from $0$ in the required index. Consequently, switching rows $0$ and $1$:

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

Finally, normalizing the last row as (-2 come from the fomula: 1 /  n with n as -1/2 <=> 1 / (-1/2) == -2)

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