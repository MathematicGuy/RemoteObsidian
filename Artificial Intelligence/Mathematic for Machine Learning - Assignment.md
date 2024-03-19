## Row echelon form

- Rows consisting entirely of zeroes should be positioned at the bottom.
- Each **non-zero row must have its left-most non-zero coefficient** (termed as a **pivot**) located to the right of any row above it. Consequently, **all elements below the pivot within the same column should be 0.**
	The 1st pivot must have all zero below it (in column)

Checkpoint - 1: Understand get_index_first_non_zero_value_from_column(N, column = 2, starting_row = 2) function
![[Pasted image 20240319110217.png]]