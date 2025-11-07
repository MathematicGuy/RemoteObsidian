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

----
## Revision Boiiiiiiiiiiiiiiiiii

Objectives of regressio

Population Regression Equation

Sample Regression Line

SSR / SSE / SST

R-Squared ($R^2$)


**L1 vs L2 Regulatization**
![[Pasted image 20251026172628.png]]
**L1:** Discard unimportant weight to exactly zero. 
**L2:** Reduce them close to zero but not exactly. Retain weak feature contribution.  
![[Pasted image 20251026173006.png]]

Note: 
+ Its spared because 1 of the solution is equal to 0. 
+ OLS (Ordinary Least Square) - bình phương tối thiểu. Khoảng cách tối thiểu tới đường thẳng tiếp tuyến.  
+ Linear Regression hence Linear Relationship between X and y. e.g. ice cream sales and season like Summer. 

![[Capture1.png | 555]]


![[Pasted image 20251026182709.png| 555]]


Term written in text book, the same but diff name: 
![[Pasted image 20251026183815.png| 555]]

Why there are 2 calculation: SSR and SSE ? -> Insight here. *WHAT I WANT TO UNDERSTAND.* 
![[Pasted image 20251026183857.png | 555]]

**Degrees of Freedom (DF) / Adj $R^2$**
**Goal:** understand degree of freedom is similar to asking *How much error can we potentially show in this model ?* 

+ ? What is the minimum datapoint you need to run a regression ? 
**Given 2 dp (data point)** -> if you fit a line there **can't be a error at all. Because that the only solution hence ZERO degree of freedom.** (freedom/cases for error to happened) 
![[Pasted image 20251026184235.png# left | 133]]
Now if we have 3 dp (dof - degree of freedome)
-> 2D: there are 1 dof  bc in 2D space bc the model will left 1 dp unfit. 
-> 3D: there are 0 dof in 3D space bc the model able to fit all 3 dp. 
![[Pasted image 20251026185142.png]]
**Given that the model are best fit the data, how much error (misfit datapoint) can exist ?** <-> Model losing oppotunities to show errors. 
![[Pasted image 20251026184733.png# left | 444]]


### What are Multiple Linear Regression
1. **Linear Relationship**
+ A straight line is draw through the data to repreent all dp as good as possible. 
+ Relationship that are dependence to eachother. LR include 1 dependent variable and 1 independent variable. 
	
2. **Independence of Errors** 
	Error of 1 dp doesn't affect another -> can test this with Durbin-Watson Test.  
	
3. **Homoscedasticity**  (Tính đồng nhất phương sai)
	Variance of the model on x & y axis should be constant ![[Pasted image 20251026190120.png# left | 444]]
	Example of NOT homoscedasticity with unequal variance for small and large error![[Pasted image 20251026190255.png# left| 344]]
4. **Normally Distributed Errors**
	test with qq-plot or analytical test ![[Pasted image 20251026190432.png | 333]]
5. **Multicollinearity in Regression** 
![[Pasted image 20251026190508.png# left | 444]] 
If there are 2 highly correlated variables then the Effect of individual variables cannot be clearly seperated.
![[Pasted image 20251026190659.png# left| 444]]
	For example since "Size of house" tend to have more "Number of room", also both of features Indicated if the "Price of house" -> there a overlapped in information, this called **Multicollinearity (Đa cộng tuyến là khi có 2 biến độc lập có ảnh hưởng tuyến tính tương ứng  với Biến phụ thuộc ra).**
![[Pasted image 20251026190824.png# left | 444]]

+ $ But isn't mutilinearity is good ? 
	+ Well YES,*mutilinearity is a good indicator if you use the Regression model for Prediction.* 
+ ? If you're **assesst the influence of each independent variables on the dependent variable**, there should be *no multicolinearity*. 

**How to detect Multilinearity ?**  -> Simply by turning that independent variable $x$ into a Dependent Variable like $\hat{y}$, if that variables can be predict using other variable, it Multilinearity. 
![[Pasted image 20251026192118.png# left | 444]]
For mesurement, we use **$R^2$ (Coefficient of determination)** bc its explain **How well the independent variable explain the variability of the dependent variable**.  
-> High $R^2$ mean the dependent variable is highly correlated. 
![[Pasted image 20251026192625.png | 444]]
![[Pasted image 20251026192653.png | 444]]

  There are 2 way to reduce Multicolinearity. 
1.  **Remove one of the Correlated Variables**
	Choose the variable that is less significant and remove it.
2. **Combine Variables** (ie. taking average)
	Create a single variable by combining the correlated variables

![[Pasted image 20251026193332.png | 544]]
Note: *p value < 0.05 mean the variable truly have infludence to the dependent variable (i.e. Blood Pressure in the example above)* and not due to chance (luckly or by consequence)

(7 câu) 1-> 7: dataset LR AIO25M05LR01 -> LR07
(5 câu) 8 ->13: Tính Loss, MSE
(8 câu) 14 -> 22: Tính Đạo hàm và Các hàm Loss 
(27 câu) 24 -> 31 Genetic Algorithm