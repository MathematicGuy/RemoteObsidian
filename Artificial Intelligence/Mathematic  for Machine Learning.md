+ obscure: mơ hồ

![[Pasted image 20240304110152.png]]

![[Pasted image 20240304110252.png]]

### Matrix Presentation
```
[ 4 -3  1 | -10]
[ 2  1  3 |  0 ]
[-1  2 -5 |  17]
```
+ **Coeficients:** The numbers before the variables (x, y, z) are called coefficients. They tell you how much each variable contributes to the result on the right side of the equation.
	
	- For example, in the first equation `4x - 3y + z = -10`, the coefficient of `x` is 4, meaning that for every change of 1 in the value of `x`, the left side of the equation changes by 4.
	
- **Constants:** The numbers on the **right side of the equations (-10, 0, 17) are the constants**. They represent the target values that each equation must equal.
    
- **Variables:** The letters (x, y, z) are the variables (the unknowns) we are trying to solve for. Our goal is to find a combination of values for x, y, and z that satisfy all three equations simultaneously
	
- **Augmented Column:** The vertical line with the constants on the right side creates the Augmented Matrix. It separates the coefficients of the variables from the constants in the equations.


![[Pasted image 20240304110413.png]]
w are the same
y are different
b - weight
Turn this into a vector
![[Pasted image 20240304110520.png]]

a + c - p = 6
a - c + 2p  = 4
4a - 2.c + p = 10

w = a,c,p (consistant across all the statement)
y = 6,4,10
feature x: 2,4

![[Pasted image 20240304114529.png]]
Complete: Non-singular
all rest: singular
![[Pasted image 20240304114630.png]]
3 different type so it non-singular and a complete system
all with more than 1 black -> redundant
black dog and white dog -> contracdictory (still -> singular)
	just 1 dog with 2 type, and 1 bird

![[Pasted image 20240304115702.png]]
Sum of a + b equation remain 10 for every input. hence linear mean stay the same.
![[Pasted image 20240304115817.png]]

When 2 of the linear line across. So at the cross point the answer (a, b) for both of them are the same (unique solution, 1 solution)
![[Pasted image 20240304115850.png]]
situation 2 line are the same. so a and b are the same for every a, b (Infinity solution)
+ increase value of 2nd function by 2 to the 1st function  -> polymeric (trùng) 
![[Pasted image 20240304115943.png]]
they never touch so no solution. 
+ Increase by 2 but different solution. (=24). So parallel
![[Pasted image 20240304120115.png]]

As we learn earlier we have 
![[Pasted image 20240304120329.png]]
+ (Contradictory) -> the same but different on 1 thing. as for the line. banana is 2 more value than apple but have the same function.

Many Planes cross eachother through a POINT -> Non-Singular
![[Pasted image 20240304120838.png]]
But Many Planes cross eachother through a LINE -> Singular (Redundant)
![[Pasted image 20240304120740.png]]
Planes Parallel to eachother -> no solution (Contradictory)
![[Pasted image 20240304121413.png]]
plane collapse to eachother -> infinite solution (redundant)
![[Pasted image 20240304121452.png]]


coefficients : hệ số
![[Pasted image 20240304122018.png]]

An easy way to find if a system is singular or non singular is to turn the constants into zeros and to study that system
![[Pasted image 20240304122222.png]]

![[Pasted image 20240304122412.png]]
Base on the system, we get the Matrix with the same system.
![[Pasted image 20240304122431.png]]


Cannot multiply 1 row to get other row -> linearly independant
or else it is dependent (because other row can infer it )
![[Pasted image 20240304124410.png]]


**Linear dependence and independence**
+ ? If one of the row depend on others rows. (phụ thuộc tuyến )
![[Pasted image 20240304123743.png]]
Highly singular system
![[Pasted image 20240304123811.png]]

Row 2 can be made with row1 + row3 -> row2 is avg
![[Pasted image 20240304123855.png]]

Can only Multiply or Add Row together. Not add value to them.
![[Pasted image 20240304125044.png]]

lin_spaced_arr = np.linspace(0, 100, 5)
print(lin_spaced_arr)
**Determinant (định thức)** - từ 1 cth => đc nhiều coth 
![[Pasted image 20240304125155.png]]

Singular - 0 (singular are 0) - Because it just itself, and by minus it = 0
Non-Singular - 1. 2 different rows value minus eachother cannot be 0. 
![[Pasted image 20240304125328.png]]
Therefore we can pointed out
![[Pasted image 20240304125538.png]]


![[Pasted image 20240304125744.png]]

**Định Thức**
**1. Định nghĩa:**

- Định thức là một hàm số áp dụng cho ma trận vuông (ma trận có số hàng bằng số cột), trả về một giá trị số duy nhất.
- Ký hiệu: `det(A)` hoặc `|A|`, với A là ma trận

**2. Bản chất của định thức:**

- Định thức **thể hiện một số đặc tính quan trọng** của ma trận:
    - **Khả năng đảo ngược:** Ma trận có định thức khác 0 (khác 0) là ma trận khả nghịch, nghĩa là có thể tìm được ma trận nghịch đảo của nó.
    - **Hệ phương trình tuyến tính:** Định thức được sử dụng để giải hệ phương trình tuyến tính.
    - **Hướng:** Định thức ma trận 2x2 có thể được sử dụng để xác định hướng của hai vectơ.


![[Pasted image 20240304130118.png]]
Subtract the other way around
![[Pasted image 20240304130213.png]]

![[Pasted image 20240304130321.png]]

Assignment (Solved)
= 0 -> Singular. Otherwise non-singular
![[Pasted image 20240304130713.png]]
+ **Singular Matrix (det(A) = 0)** have Dependent Row (Determinant = 0)
+ **Non-Singular Matrix (det(A) ≠ 0).** have Linearly Independent rows. (Determinant = 6)

example answer for the 1st one. 
![[Pasted image 20240304130756.png]]

![[Pasted image 20240305014744.png]]
This is dependant because the 1st rows is just the 3rd row - the 2nd row then * 2  
> 3rd - 2nd = (2a, 2b, 2c) then divided by 2 we have a, b, c which is the first row.
 

Divide coefficient of a in both equation. the 1st divided to t, the 2nd divided to 4
![[Pasted image 20240305001911.png]]

![[Pasted image 20240305002539.png]]
Can freely choose X to find a and b
![[Pasted image 20240305002555.png]]

![[Pasted image 20240305002803.png]]



![[Pasted image 20240305002849.png]]
System is Dependant -> Singular 
(Các hàng tự suy ra được nhau -> infinite solution)

### Elimination method
*Gaussian Elimination*
(at the 3rd system. THat not a - b + 2c that a + b + 2c. It just a visual blunder)
+ Isolate a mean there are only 1 line with a in the system. The same with Isolate b by remove the other b from the 3rd row.
![[Pasted image 20240305003027.png]]

![[Pasted image 20240305004343.png]]

![[Pasted image 20240305004447.png]]
And that how we get the Point 3 plane crossed.
![[Pasted image 20240305005002.png]]

Matrix row-reduction (ma trận bậc thang rút gọn)
+ ? The Intermediate System are the System after Gaussian Elimination Process.
![[Pasted image 20240305005506.png]]
> Row echelon form - hình thức cấp bậc hàng

![[Pasted image 20240305005652.png]]


For 0. The Row Echelon form is itself
![[Pasted image 20240305005714.png]]

+ Can have all 1 or 0 at the diagnol. 
+ Below the diagnol everything are 0. above 0 are 0
![[Pasted image 20240305005822.png]]


Row operations that preserve singularity
+ By switching the rows you're subtracting are now subtract the other row.
![[Pasted image 20240305012840.png]]

![[Pasted image 20240305013038.png]]


![[Pasted image 20240305013129.png]]

## Chapter Summary

### Singular and Non-singular in Matrixes

**Singular Matrix**

- **Definition:** **A square matrix** (meaning it has the same number of rows and columns) is considered singular if its determinant (a specific value calculated from its elements) is equal to zero (det(A) = 0).
- **Properties:** (0 is still zero no matter what)
    - **Non-invertible:** A singular matrix does not have an inverse. The inverse of a matrix allows you to "undo" its multiplication with another matrix. Because of a determinant of zero, the inverse operation cannot be defined for singular matrices.
    - **Dependent Rows/Columns:** A singular matrix often indicates that its rows or columns are linearly dependent. This means one row (or column) can be expressed as a linear combination of the other rows (or columns).


**Non-Singular Matrix**

- **Definition:** A square matrix is non-singular if its determinant is not equal to zero (det(A) ≠ 0).
	
- **Properties:**
	- **Invertible:** A non-singular matrix has an inverse. This allows you to solve systems of linear equations using techniques like Gaussian elimination or Cramer's rule.
	
    - **Independent Rows/Columns:** The rows and columns of a non-singular matrix are typically linearly independent. This means no row (or column) can be created from a linear combination of the others.
	
- **Geometric Interpretation (if applicable):** In 2D, a non-singular matrix represents a transformation that scales or rotates a shape without collapsing it. In 3D, it represents a transformation that scales, rotates, or reflects a shape without collapsing it into a lower dimension.

```ad-conclusion
**How They Affect Systems of Linear Equations**

- **Singular Matrix:** If the coefficient matrix in a system of linear equations is singular, then:
    - There might be no solution (inconsistent system).
    - There might be infinitely many solutions (dependent system).
- **Non-Singular Matrix:** If the coefficient matrix is non-singular, then there exists a unique solution to the system of linear equations.
```
### Solution and Determinant of a Matrix

> Given Matrix A
```
4x - 3y + z  = -10
2x + y  + 3z = 0
-x + 2y - 5z = 17
```

**Solution of a Matrix**

- **Meaning:** A solution to a system of linear equations represented by a matrix is a set of values for the **variables that satisfy all the equations simultaneously.**
	
- **Existence:** A system of equations may have:
    - **A unique solution** (a single set of values for the variables)
    - **Infinitely many solutions** (2 lines coincide/at the same position)
    - **No solution** (parallel)
- **Finding Solutions:** Methods like Gaussian elimination, Cramer's rule, and matrix inversion are used to find the solution(s) to a system of equations.
	
+  Solution of Matrix A : `[1, 4, -2]`  


**Determinant of a Matrix**

- **Meaning:** The determinant of a square matrix is a single scalar value calculated from the elements of the matrix. It has several geometric and algebraic interpretations.
	
- **Geometric Significance:**
    - The magnitude of the determinant indicates the scaling factor by which the matrix transforms areas (2D) or volumes (3D).
    - A zero determinant means the matrix collapses space into a lower dimension.
	
- **Algebraic Significance:**
    - **Matrix Invertibility:** A matrix is invertible (has an inverse) only if its determinant is non-zero.
    - **Linear Independence:** A system of equations has a unique solution if and only if the determinant of its coefficient matrix is non-zero.
	
+ Determinant of matrix A: -60.00

**Key Differences**

| Feature     | Solution                                                              | Determinant                                                         |
| ----------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| What is it? | A set of values for the variables that satisfy the equations          | A single scalar value calculated from matrix elements               |
| Represents  | The point(s) where lines/planes/hyperplanes intersect (if they exist) | Geometric scaling factor, matrix invertibility, linear independence |
| How to find | Gaussian elimination, Cramer's Rule, matrix inversion                 | Specific formulas based on matrix dimensions                        |
**In Summary**

- The solution of a matrix tells you _if_ and _where_ the equations represented by the matrix intersect.
	![[Pasted image 20240304120838.png]]
- The determinant of a matrix tells you about the properties of the transformation the matrix represents and if a unique solution even exists.


