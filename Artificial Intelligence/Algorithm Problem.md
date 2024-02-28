## Tower of Hanoi

Điều kiện đặt  Vòng vào cột -> Trống hoặc lớn hơn. Ưu tiên vòng bé tr'c
3, A, B, C
2, A, B, C (C)
1, A, B, C (C, B)
Đặt vòng bé lên vòng to 

xét cái bé nhất
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
