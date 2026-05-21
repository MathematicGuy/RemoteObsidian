## Tower of Hanoi
[[Recursion]]
![[Pasted image 20240302095842.png]]

![[Pasted image 20240302101632.png]]
**from_rod**
![[Pasted image 20240302101929.png]]
**to_rod**
![[Pasted image 20240302102037.png]]
**aux_rod**
![[Pasted image 20240302101941.png]]


![[Pasted image 20240302100011.png]]
![[Pasted image 20240302101448.png]]
towerOfHanoi(4, A, C, B) mean move the 4th plate to C. and all the remaining to B
+ ? Notice the **left function are the current position**. The **right function are the move we make**.  
+ If there only 1 plate then move it to C.

towerOfHanoi(3, B, C, A) mean switch all the plate from B and C. (all the plate from C goes to C and all the plate from C goes to B) 
![[Pasted image 20240302103729.png]]


![[Pasted image 20240302101430.png]]
Iterative Rule
+ A to B, or reverse
+ B to C, or reverse
+ C to B, or reverse
Repeat until solved

Recursive Answer Thuật toán
if (n = 1)
{
	chuyển 1 đĩa từ A tới C
}
else
{
	chuyen(n-1, A, C, B),
	chuyen(1, A, B, C),
	chuyen(n-1, B, A, C),
}

 
## 8 Queens
Line Queens near the rear to limited its Power.

![[Pasted image 20240228153725.png]]
