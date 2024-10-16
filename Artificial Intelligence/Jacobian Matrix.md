> **Jacobian is a Matrix of Partial Derivative**. **Jacobian is the determinant** of the Jacobian Matrix and the **matrix contain all partial derivative of a vector function**.


Ma Trận Đạo Hàm Riêng
n - row; m - column
"$.$" scaler multiplication
$\times$: vector multiplication

**Purpose:** Calculating Det
![[Pasted image 20241016091423.png]]
**Ví Dụ** (note: $R^{3}\to R^3$ describe the function takes **input from 3D space and gives an output in 3D space.**)
![[Pasted image 20241016091552.png]]

---
# [[What is Jacobian - The right way of thinking derivatives and integrals]]

#### Chapter 1: Linear Maps
Synonymous: have the same idea/meaning (đồng nghĩa)
Derivative ~ Slope
Tangent: touching a curve or surface at 1 point (tiếp tuyến)
What about a function with 2 Inputs and 2 Outputs. we would need a 4D graph??
![[Pasted image 20241016093038.png]]
Good intuition of derivative? -> That is more Generalise
Additional note: 
Integrals: Area (tích phân) - can be though of as the area under the curve (good intuition, or is it?) -> not the best intuition moving on...
What should we actually thing about it? let rethink derivatives and integrals.

Let first look at **Linear Maps in 2D** to get the hang of it.  
Linear: reserve value, stay balance and unchanged.
![[Pasted image 20241016093512.png]]
Red Dot: Original (fixed)
Track the linear map using 2 blue points. **When we know where 2 blue points are, we know where very point goes.**  To represent the location of these 2 point, we need to refer back to the original coordinates.
![[Pasted image 20241016093547.png]]

For example: 
+ The **point (1,0)** on the **horizontal axis gets mapped to the point (1.33, -0.73) in this case; and (0,1) on the vertical axis gets mapped to the point (1.17, 0.75) in this case**
	![[Pasted image 20241016093946.png]]
+ $ **These 4 numbers completely determine the linear map**. (i.e. coordinate of 2 blue points) So we usually represent them in an array like this:
	![[Pasted image 20241016094432.png]]
	Which **(1.33, -0.73) represent where (1, 0) goes** and **(1.17, 0.75) represent where (0, 1) goes.** This array of numbers called a matrix, capturing the essen of linear map.
	
another thing about linear maps is what its does to 2D region, **even though region (i.e. linear maps space) will be distored, the AREAS of any region actually scale by the same factor.**  (using eigenbasis)
	![[Pasted image 20241016095001.png]]
	This **scaling factor called a determinant (scaling factor for areas** by lengths)
		![[Pasted image 20241016095054.png]]
	In 2D linear map represent a matrix, but in 1D we only need to know where 1 goes, so we reduced the matrix to just 1 number which is the scaling factor. 
	![[Pasted image 20241016095416.png]]


#### Chapter 2: Derivatives in 1D
![[Pasted image 20241016095506.png]]
Discrepancy: Sự khác biệt
Neighboring point: các điểm liền kề
Interpretation: in other meaning (phiên dịch)
Reinterpreting Derivatives as Scaling Factors: Mô tả Đạo hàm như hệ số tỷ lệ.

> Choose a random point for the input, it get mapped to f as f(x). So what we actually **want to know is the behaviour of f on the NEIGHBOURING points.** 
+ Let’s zoom into the neighbourhood of the point a, and observe what f does to it.  
![[Pasted image 20241016100138.png]]
>The point a mapped to f(a) rather than staying put, so we have been centering our perspective on a -> This mean we can sort of treat this as an linear map. 


In this case the linear map is represent by the matrix 3, since $a$ is scaling by a factor of 3 (when a mapped to f(x) as f(a))
![[Pasted image 20241016100257.png]]
This is the **Jacobian Matrix at the point $a$ for this 1 dimensional function $f$** and the number 3 in the matrix is the derivative of function $f'(a)$.  (i.e. The scaling factor near the point a) 
(So because can be see as linear maps and have a scaling factor -> it jacobian matrix ?)
note: $f'(a)$ read as "f prime of a"

further supported concept:
[[Linear Approximation]]

#### Chapter 3: Derivatives in 2D 
Pick a point a, b and zoom in far enough. After centering the perspective on the point a. 
![[Pasted image 20241016111254.png]]
we can approximate the linear map to the 2D function, It look like the linear map. Although this is not exact, but we can take the closest linear map approximation. This is the image of the exact linear map, with respect to the original coordinate system.  
![[Pasted image 20241016111325.png]]
>**Jacobian matrix is the matrix representing best linear map approximation of $f$ near a fixed point $(a, b)$ (i.e. (a, b) like the eigenbasis, base coordination show where every points goes)**
> (a, b là tọa độ gốc cho phép mình biểu diễn vị trí của mọi điểm khác ở đâu)

2nd input is fixed
![[Pasted image 20241016111639.png]]
projecting back to the horizontal line. 
![[Pasted image 20241016111723.png]]

![[Pasted image 20241016111755.png]]

![[Pasted image 20241016111840.png]]

![[Pasted image 20241016112001.png]]

![[Pasted image 20241016112017.png]]

![[Pasted image 20241016112028.png]]
```ad-summary
**Jacobian Matrix** represent the ((best linear maps approximation of f  near the (a, b).**

**Determinant** represent **scaling factor**

**Jacobian Determinant** represent **how much areas scale near (a, b)**

Jacobian matrix is use to create a matrix that approximate higher dimensions like 2D, 3D, etc.. base on the centering point (a, b) by using the derivative the derivative with respect of x and y coordinate for each function.
```
+ further explain: [[how the derivatives of the function with respect to the x and y coordinates help approximates]]
	w.r.t x: hàm f thay đổi ntn độc lập trên x (y cố định) 
	w.r.t y: ---------------------------------   y (x cố định)
	-> cho biết hàm thay đổi ntn khi có sự thay đổi nhỏ trên x hoặc y hoặc cả x và y. 

#### Chapter 4: What is integration ? 
How to find the mass of this rot?
![[Pasted image 20241016115805.png]]
> So how do we find the mass of this rod? Well, we can chop the rod into smaller pieces, then find the masses individually, then add them all up.
> ![[Pasted image 20241016115929.png]]
> This is not perfect, but **as the length of the little rod decreases, and there are more and more of them, we come closer to the true mass** (a and b represent the two endpoints of the big rod)
	![[Pasted image 20241016120039.png]]

(giả thuyết: chia ra vô tận các hình vuông siêu nhỏ)
D: region
![[Pasted image 20241016120212.png]]

![[Pasted image 20241016120316.png]]

![[Pasted image 20241016120508.png]]

#### Chapter 5: Changing variables in integration (1D)

value at a specific point $g(u)$. value max/min represent as $g(b)$/$g(a)$
thus function at a specific point: $f(g(u))$ (the same for f with max/min)
![[Pasted image 20241016120828.png]]
>If I have a **random point u** here, we want this to **correspond to the point g(u) on the original rod.** ($u = g(u)$) Thus the density at u would be $f(g(u))$ but that doesn't mean the 2 rot have the same length

note: (Derivative or rate of change accurately can be seen as the scaling factor of a vector)

But we can always chop the rot into smaller pieces, let focus on the point containing $u$. The scale factor induced by g near the point u is precisely $g’(u)$, so if we add this scaling factor we can make the 2 rot (i.e. blue and red) have the same length.  
![[Pasted image 20241016120937.png]]

#### Chapter 6: Changing variables in integration (2D)
**Main Purpose:** Original Matrix represent the mass and using determinant to represent areas of differents Matrieces. 
![[Pasted image 20241016134330.png]]
What if J is negative, so this should be the correct fomula: 
![[Pasted image 20241016134441.png]]
If the derivative (scaling factor) is negative it would flip the integral.  
![[Pasted image 20241016134543.png]]
 with how we define a two-dimensional integral. Orientation is not built into its definition, and we always say that the integral is defined on a region, never specifying its orientation. (orientation in 1D, not in 2D)
![[Pasted image 20241016134654.png]]

![[Pasted image 20241016134857.png]]

#### Chapter 7: Cartesian to polar 
![[Pasted image 20241016134923.png]]

![[Pasted image 20241016135013.png]]

Finding Jacobian
![[Pasted image 20241016135044.png]]

further explain: https://youtu.be/hhFzJvaY__U?si=cp2wa4NpgY1qF5sz

