![[Pasted image 20240709125217.png]]
-> Independent if a vector cannot be form by other vectors.

A group of vectors is said to be **linearly independent if none of the vectors in the group can be obtained as a linear combination of the others.** or in other word
Example:
$v_{1}=(1, 0), v_{2}=(0, 1)$ as independent $v_{1}$ cannot transform into $v_{2}$ (and reverse), in other word $v_{1}$ is not a multiple/scaler for $v_{2}$ (and reverse).
$u_{1}=(1, 2), u_{2}=(2, 4)$ as dependent because $u_{1}$ is depend on $u_{2}$ -> $u_{2} = 2u_{1}$

**Another Linearly Independent Vectors Examples:**
Basis Vectors in $\mathbb{R}^2:(1, 0), (0, 1)$
Standard Basis in $\mathbb{R}^{3}:{(1, 0, 0), (0, 1, 0), (0, 0, 1)}$ - Each vector introduces a new dimension. 
Non-parallel Vectors $\{(1, 2), (3, 1)\}$ - no scaler $c$ exists such that $(1, 2) = c(3, 1)$


**Linearly Dependent Vectors Examples:**
Scalar Multiples: $\{(1, 2), (2, 4)\}$ - Vector 2 is $2\times$ Vector 1.
Set with Zero Vector: $\{(5, 0), (0, 0), (2, 6)\}$ - The zero vector makes the set dependent.
Redundant Vectors: $\{(1, 0, 0), (0, 1, 0), (1, 1, 0)\}$ - The third vector is the sum of the first two $(v_1 + v_2 - v_3 = 0)$
More Vectors than Dimensions: The vectors $(1, 2), (3, 4), (5, 6)$ in $\mathbb{R}^2$ are dependent because there are 3 vectors but only 2 entries each.

