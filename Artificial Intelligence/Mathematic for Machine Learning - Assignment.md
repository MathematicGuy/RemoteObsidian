## Programming Assignment - Gaussian Elimination

```Python
pivot_candidate = M[None, None]
```
> This means that you must replace the correct values for the row (first None) and column (second None).
![[Pasted image 20240408194554.png]]
- In this Assignment, Matrix(A) is **always square** 
### Step 2: Transform Matrix into Row Echelon Form[](https://khxvgneyfzdo.labs.coursera.org/notebooks/C1W2_Assignment_2024_03_28_01_48_45.ipynb#Step-2:-Transform-Matrix-into-Row-Echelon-Form)

Initiate row operations to convert the augmented matrix into row-echelon form. The objective is to introduce zeros below the leading diagonal.

- **Row Switching:** Rearrange rows to position the leftmost non-zero entry at the top.
- **Row Scaling:** Multiply a row by a non-zero scalar.
- **Row Replacement:** Substitute a row with the sum of itself and a multiple of another row.

### Step 3: Back Substitution[](https://khxvgneyfzdo.labs.coursera.org/notebooks/C1W2_Assignment_2024_03_28_01_48_45.ipynb#Step-3:-Back-Substitution)

After attaining the row-echelon form, solve for variables starting from the last row and progressing upwards.

Remember, the aim is to simplify the system for easy determination of solutions!

### Step 4: Compile the Gaussian Elimination Algorithm[](https://khxvgneyfzdo.labs.coursera.org/notebooks/C1W2_Assignment_2024_03_28_01_48_45.ipynb#Step-4:-Compile-the-Gaussian-Elimination-Algorithm)

Combine each function related to the aforementioned steps into a single comprehensive function.



