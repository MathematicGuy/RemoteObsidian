**What to Revision ?**
Bias - Tại sao lại bỏ tham số b với 1 số dataset nhất định ? 
Use 1 sample to update 1 and multiple parameter 
![[Pasted image 20251005174704.png# left ]]
Có thể thay đổi được nhưng scale sẽ khác và đạo hàm chậm, tốc độ hội tụ chậm hơn và pải điều chỉnh learning rate bé hơn. 

![[Pasted image 20251005180611.png# left | 444]]
Bước tính Loss ít quan trọng nhất vì bước Cập Nhật trọng số ở Bước 1. Bước 2 chỉ tính Loss để kiểm tra chất lượng mô hình. 
Note: Huấn luyện mô hình 2 lần khác nhau độc lập cùng 1 tham số thì **kết quả sẽ khác nhau** vì **cùng cấu hình** nghĩa là **cùng** 
+ **kiến trúc mô hình** (số layers, neuron và hàm kích hoạt, etc..) 
+ **hyperparameter** (learning rate, batch size, số epoch) 

What I want to learn tonight: 
+ Taylor's Expansion (re-implement taylor expansion)
+ Ôn lại đạo hàm của Linear Regression. 
+ Rewrite and explain (surface level) Linear Regression 
+ Linear Regression Coding Homwork. 
+ Min-Max Scaling, Z-Score Scaling (quick re-explain) with visualization. 
### Taylor's Expansion
**Goals:** calc approximation better. 
But Taylor have a lot of approximation level, which are the best for me ? That the problem we going to solve. 
-> The higher degree of the approx the better approx result become. 


**Taylor expansion of function around a point A** is given by the fomula:
	_f(x) = f(a) + f'(a)(x-a)/1! + f''(a)(x-a)²/2! + f'''(a)(x-a)³/3! + ..._
- _f(x)_ is the original function.
- _a_ is the point around which the expansion is centered.
- _f'(a), f''(a), f'''(a)_, etc., are the first, second, third, etc., derivatives of _f_ evaluated at _a_.
- _n!_ is the factorial of _n_
	
The Taylor series for a function $f(x)$ about a point $a$ is given by: $$
    f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n
$$The expanded form of the series is: $$
    f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^{3 + \cdots}$$
Note: chỉ có x nên đạo hàm theo x.  
Power series: hàm có nhiều biến số. i.e. thêm $c_{n}x^{n}$ trong đó c là 1 hàm số với 1 tham số. 
Taylor Series cấp 1 -> $f(x) = f(a)$
Taylor Series cấp 2 -> $f(x) = f(a) + f'(a)(x-a)$ 
Taylor Series cấp 3 -> $f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2$
Taylor Series cấp n ->  $f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^{3 + \cdots}$


Với $y = e^x$  (khai triển trên $e^x$)  
approx $e^{0.2}$ by 1. In calculus we have the idea of linear approximation.   
 
(GIẢ SỬ) Let say $e^x$ = $c_{0} + c_{1}x$, if $x=0$  $\implies e^{0}= c_{0}$ because $c_{1}*0 = 0$
If we take the derivative we get. 
![[Pasted image 20251005211336.png# left | 260]]
![[Pasted image 20251005211530.png# left | 300]]
1st derivative -> slope
2nd derivative -> concavity

$c_{2}$ must be 1/2 so $c_{2}.2 = 1 = e^0$ 
![[Pasted image 20251005211844.png# left | 444]]
$\implies e^{x}=1+x+\frac{1}{2}x^2$  
Khai triển kiểu gì để hàm $f(x)$ luôn bằng $e^x$.

Vì mỗi lần đạo hàm là theo x, nên mọi hằng số $c$ lần lượt sẽ bị triệt tiêu sau mỗi lần đạo hàm. 
![[Pasted image 20251005212429.png]]
	Sau khi đạo hàm đến lần thứ n-th, thay x = 0. $n(n-1)$ is just repeat the pattern as n go on and on. So for $e^x$ to equal to $n(n-1)$, $f(x)$ need to divide itself to $n(x-1)$.
![[Pasted image 20251005212615.png]]
in other word for $f^{n}(x) = n!.c_{n}$ equal to $e^x$ for $x=0$, we need to divide by $n!$ itself. i.e $n.(n-1)(n-2)\dots(n-(n+1))$. **That Taylor's Series !**

**A Maclaurin Series** is 1 where you doing a power series around $x=0$, compute what their coeficient are. $x=0$ mean $x$ is not important,  we can actually shift this so everywhere there's a zero we can put an A, so it's $x-A$. 
![[Pasted image 20251005214022.png# left | 444]]
 h.o.t - higher order term (abbreviation instead of writing the whole function
	
Taylor Series, Taylor Series with imaginary number $i$ -> Euler's Fomular. 
$$e^{ix}=\cos(x) + i.\sin(x)$$
![[Pasted image 20251005220917.png]]

