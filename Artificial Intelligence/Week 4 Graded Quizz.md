![[Pasted image 20240704171725.png]]
+ If MM has size nn, then it has nn distinct eigenvalues - True
	Bc it have n answer, which is n eigenvalues

+ Singular -> Have only 1 answer. (chỉ có 1 nghiệm) which mean it have onlz 1 axis (x, y). Matrix require at least 2 axis so it cannot have identity matrix. 

![[Pasted image 20240704172933.png]]
In our case, we're working with the standard basis of ℝ³:
- **e₁** = [1, 0, 0]
- **e₂** = [0, 1, 0]
- **e₃** = [0, 0, 1]

**Matrix Representation**
The matrix representation of a linear transformation _T_ relative to a chosen basis (in this case, the standard basis) is constructed as follows:
	
1. **Apply T to each basis vector:** We have:
    
    - T(**e₁**) = [1, 3, -4]
    - T(**e₂**) = [2, -1, -3]
    - T(**e₃**) = [4, 5, -11]
2. **Form the matrix:** The results of applying _T_ to the basis vectors become the columns of the matrix:
    
```
[ 1  2 -1 ] 
[ 3  1  3 ]
[ 4  5 -11]
```

![[Pasted image 20240704213449.png]]