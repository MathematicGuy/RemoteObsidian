$$
M = 
\begin{bmatrix} 
\phantom{-}1 & -1 & \phantom{-}\frac{1}{2} & | & \phantom{-}\frac{1}{2} \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}1 & | & -1 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -1 
\end{bmatrix}
$$

Starting from bottom to top:

- $R_2$ :

- $R_1 = R_1 - 1 \cdot R_2 = \begin{bmatrix} 0 & 1 & 0 & | & 0 \end{bmatrix}$
- $R_0 = R_0 - \frac{1}{2} \cdot R_1 = \begin{bmatrix} 1 & -\frac{1}{2} & 0 & | & 1 \end{bmatrix}$

The resulting matrix is then

$$
M = 
\begin{bmatrix} 
\phantom{-}1 & -\frac{1}{2} & \phantom{-}0 & | & \phantom{-}1  \\
\phantom{-}0 & \phantom{-}1 & \phantom{-}0 & | & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}1 & | & -1 
\end{bmatrix}
$$

Moving to $R_1$ :

- $R_1$ :

- $R_0 = R_0 - \left(-\frac{1}{2} R_1 \right) = \begin{bmatrix} 1 & 0 & 0 & | & 1 \end{bmatrix}$

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

