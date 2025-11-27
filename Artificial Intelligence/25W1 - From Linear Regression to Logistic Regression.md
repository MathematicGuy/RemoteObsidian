### Linear regression model 
![[Pasted image 20251105203646.png]]
Cost Function overview
![[Pasted image 20251105203803.png]]
$y^{(i)}$ - true target
$\hat{y}^{(i)} - y^{(i)}$ - subtract predict valuey hat to y. 

### Cost function Intuition (understanding the cost function)
If you set *w=1 & b=0*. And calculate the loss of $f_w(x)$ over all *predict datapoint (point map to the blue line*) and *grounth truth datapoint* (*annotate in RED*) we get a Loss Function Value of *0.58.*
![[Pasted image 20251105210015.png]]
Repeat this step for w=0&b=0 and we get Loss Func value of 2.3
![[Pasted image 20251105210238.png]]
**Repeat for this step for all other value** then we get this beautiful parralbol line. 
	+ $ So when you trace what the Cost function $J$ by W for all x. The loss/cost function $J$ look like this. 
+ ? However, *how can we choose the correct value of $w$ that minimize $J$.*
![[Pasted image 20241014112735.png| 244]]
That also how you adjust the weight to minimize the loss function. 
![[Pasted image 20251105210646.png]]


### Visualize the cost function (How $f_{w,b}$ relate to the Cost function $J$ )
Like the previous example, for the given W and all input x, we can calculate the loss function value. In 3D, it the same, for the given $f_{w,b}$ you can see whether the loss value on the loss function graph is minimal (ie. at the center) or not.  
![[Pasted image 20251105220944.png]] 


### Feature Scaling 
+ @ Allow Gradient Descent to converge faster by rescale all features so they all take on a comparable range of values. (Đưa các features về cùng 1 khoảng giá trị 0 và )
 
**Features and Parameters:** with **large value** model often choose **small parameters**, likewise for **small value** model often choose **large parameter** since it make the prediction **more reasonable.** 
![[Pasted image 20241014164249.png]]

For feature with large value, `size in feet`  for example (as $x_{2}$) and bedroom as $x_{1}$. A **little change in $x_{1}$ (say 200) can affect a large change in the cost function/prediction**, while a **large change in x1 (say 5) didn't make a little change at all.** To encounter this problem, we must **rescale/normalize both value into 1 value range.**  
![[Pasted image 20241014165034.png]] 
With Rescaling, the contour plot (parabol from top down view) now even and represent a circle. 
![[Pasted image 20241014164820.png]]

So how do you actually scale the vales? by dividing by it maximum value
![[Pasted image 20241014165801.png | 344]]

![[Pasted image 20251105223957.png]]

#### other way is to use Mean Normalization
1) find the feature average (axis average value) 
2) substract the value with the Mean and dividing to it (max - min) 
![[Pasted image 20241014170400.png]]

#### Z-score Normalization
![[Pasted image 20251105224222.png]]

**When to Rescaling ?**
![[Pasted image 20241014171619.png# left | 433]]
+ $ Checking gradient descent for convergence
 + ? **Converged** mean the algorithm has reached a point **where every update is very small** indicating that the **loss function has reached the optimal or nearly optimal value** and **further iteration would not significantly reduce loss.**  
 You can use $\epsilon$ (epsilon) for automatic convergence test:
 Let $\epsilon=10^{-3}$ then 
	 If $J(\vec{w}, b) \leq \epsilon$ in 1 iteration, declare convergence ( i.e. parameters $\vec{w}, b$ to get close to global minimum )  

+ $ Choosing the learning rate
![[Pasted image 20241015093817.png]]
+ ? **Learning rate too big the convergen become unstable**. What we want is a **learning rate allowed big step but not too big at the start and take smaller and smaller step** when the curvature is more flat (i.e. parabol curve become flatter at the center point). (This also indicate bugs might be in your code) 
+ ! Choosing a **too small learning rate lead the function unconvergerable.** Since each step become  smaller and smaller, it would take forever which is not optimal.
+ ? so How to Choose the Right Learning Rate. 

### Feature Engineering
Normal way to choose features
![[Pasted image 20241015221722.png]]
**Feature Engineering:** create new features by using **intuition** to design **new features**, by transforming or combining original features.
![[Pasted image 20241015222100.png]]

### Polynomial Regression (đa thức hồi quy)
> Fit curve, non-linear function into your data.
+ 
**Note:** Linear represent a straight line, if sth called linear, meaning it is **Proportionality:** If x increase then y increase $y=2x$. increase or decrease at a constant rate and **Additivity** like 1+1=2.

Example of Polynomial Regression with non-linear features: feature may be $x, x^{2}, x^{3}$. Since the feature value is exponential, feature scaling would be very important. Especially in Gradient Descent
![[Pasted image 20241016140747.png]]

**Choice of Features**
>So how can we chose the right type of features. Which to include or not include. In Course 2, you can learn it.
![[Pasted image 20241016140833.png]]


### Regularization (From Polynomial to L1 and L2)
+ ? Polynomial Regression (đa thức hồi quy)
	+ **Polynomial:** đa thức nhiều biến x. Example: ax1 + bx2 + cx3 = y(x1, x2, x3) ![[Không có tiêu d_.jpg | 444 ]] 
*Simple Linear Equation:* $y = b_0 + b_1 x_1$
*Multiple Linear Equation:* $y = b_0 + b_1 x_1 + b_2 x_2 + \dots + b_n x_n$
*Polynomial Linear Regression:* $y = b_0 + b_1 x_1 + b_2 x_1^2 + \dots + b_n x_1^n$

**Note:** Linear represent a line, if sth called linear, it is a line. 
**Proportionality:** If x increase then y increase $y=2x$. increase or decrease at a constant rate and **Additivity** like 1+1=2.

Example of Polynomial Regression with non-linear features: feature may be $x, x^{2}, x^{3}$. Since the feature value is exponential, feature scaling would be very important. Especially in Gradient Descent
![[Pasted image 20241016140747.png]]
**Choice of Features**
>So how can we chose the right type of features. Which to include or not include. In Course 2, you can learn it.
![[Pasted image 20241016140833.png]]

### Logistic Growth Model and its relation to ln()
N - pop size
r - growth rate = (birth - death) / N -> return pos or neg pop's rate of growth.
### [Logistic Regression with Maximum Likelihood](https://youtu.be/TM1lijyQnaI?si=--OOiSPPTybNRGzw)

----

## Lecture Analysis
### From Linear Regression to Logistic Regression
+ @ **Main Problem:** explain how to choose the right Loss function, start from Linear Regression to Logistic Regression. **How to design a Learning Algorithm ?**
Linear Regression Revision (intuition + calculation + ideas)
$\hat{y} = H(x) = \sum_{i=0}^j \theta_i X_i$


+ ? [What is "First Order" in First Order Trend](https://www.reddit.com/r/AskEngineers/comments/1kdz6on/first_order_effect_for_the_eng_word_geeks_what/): 
	+ **"To first order"** is **colloquial for** the notion that you're **discussing the biggest effects and ignoring others.**
	+ Mathematically, **"first order (1D)" suggests the first term of a taylor expansion, ignoring higher order (ie 2D, 3D, 4D, etc...)**. In perturbation theoreis first order is the base theory, maybe with only a linear term for correction. There are other specific definitions, but it's not a single well defined concept.

Give new problem -> The need for Logistic Regression...
+ Goal: Fit the data best. Find the func that describe (predict) the data pattern. Author solve this problem by using a already proven fomula. 
+ Try with Linear Regression -> not fit bc of straight line. 
+ Try with Logistic Regression -> see better result. 
 ![[Pasted image 20251109212724.png]]**NOTE:** Sigmoid Function. (Thêm phần giải thích sâu và CM công thức trong section Tại Sao). 
**Step of Logistic Regression**
1) Initialize Parameters
2) Calculating y -> Calculate Sigmoid z
3) Calculate Loss base on $\hat{y}$ and $y$ 
4) Calculate Parameters Gradient 
5) Update Parameters Gradient (w and b)
![[Pasted image 20251109222411.png]]
Tính đạo hàm theo x rồi tính đạo hàm theo y. Hoặc ngược lại, kq như nhau thoi. 

Logistic Growth Fomula review (giải phương trình vi phân) -> Sigmoid -> Dùng Sigmoid vì nó đưa dải giá trị về 0 và 1. Dễ phân loại khi có Threshold.  
(Giải thích vì sao Sigmoid hoạt động, 1) là đáp ứng nhu cầu 2) giải thích dưới mặt toán học)
![[Pasted image 20251109212913.png]]
Sau khi biết cách làm -> Cần cập nhật trọng số -> Tính đạo hàm 
![[Pasted image 20251109212948.png]]
Đạo hàm MSE 
![[Pasted image 20251109213622.png]]
Thầy giảng thiếu phần nhược điểm của MSE ??
![[Pasted image 20251110000357.png]]
Khi tính đạo hàm ta thấy MSE ko phù hợp để làm hàm mất mát vì ... nó là non-convex. 
+ ? 1 Hàm Loss non-convex sẽ:
		+ sẽ là 1 hàm không lồi. Nghĩa là nó có nhiều local-minimal (giải thích thêm phần này sử dụng Coursera) khiến thuật toán sử dụng Gradient Descent bị mắc kẹt ko tiến đến đc Global minimal. 
	+ Đạo hàm rất nhỏ vì công thức sử dụng Nhân, nên càng cập nhật nhiều sẽ càng chậm -> hiện tượng này gọi là Vanishing Gradient, đạo hàm ít tới mức có thể coi như là không cập nhật gì. 
	+ Hàm mất mát không có ý nghĩa thống kê vì nó đc thiết kế cho bài toán Regression với mục tiêu dự đoán các giá trị biến động liên tục. Trong khi Logistic Regression là 1 bài toán phân loại dự đoán xác suất thuộc về 1 lớp nhất định. (Regression có nhiều giá trị, Classification có 1 số giá trị nhưng vẫn có thể đếm đc), sử dụng Cross-Entropy, 1 hàm thuần xác suất để phân loại nhị phân sẽ có ý nghĩa thống ke tốt hơn. 
+ ? Giải thích tính Convex của 1 hàm bằng cách chứng minh liệu 1 hàm có convex hay không. i.e. đạo hàm bậc nhất và đạo hàm bậc 2. Nếu đạo hàm bậc 2 > thì Convex, =0 sẽ ... < 1 sẽ ... Note: tính convex theo số lượng tham số $w_{0}, w_{1}, etc..$

2u - 4 = 2(3x + 2) - 4 = 6x
dg(f)/df * df(x)/dx = (2f-4) * 3 
= (2*(3x + 2) - 4) * 3 = (6x + 4 - 4) * 3 = 6x * 3
 
**Finally Evaluation function Overview: LR using MSE -> BCE.**
+ @ Tập trung vào **giải thích Cách Tiếp Cận chứ không chỉ giải thích đơn thuần.** -> Hiểu sâu hơn và tự chủ đc nhiều hơn. Giúp ng đọc hiểu vì sao lại chọn Hàm Loss này mà ko chọn hàm loss khác.
MSE (tính chất và giải thích)
- Với X, Y tại vị trí này thì Hàm F bằng bao nhiêu. 
- Convex -> Luon luon lớn hơn hoặc bằng 0. Biết hàm L là Convex nhưng chưa biết nó làm gì. 
+ Điều kiện: giúp đánh giá model tốt với 
	1) Hàm Loss càng nhỏ model càng tốt. e.g. y(x) = 0.01 hoặc khi y tiến tới 1 chỉ định model tốt và Loss trả về giá trị nhỏ. 
	2) Hàm Loss càng lớn model càng tệ  e.g. y(x) = 0.9
+ Thử chọn các giá trị y = 0 để xem Loss tăng giảm ntn.  
+ ? **Thử Nghiệm 1:** Với **x=1 và y=-log(x)** ta thấy x càng lớn thì y càng nhỏ và ngược lại -> Đạt đk 1 + 2, phù hợp cho đánh giá cho x -> 1.    
+ ? **Thử Nghiệm 2:** Song song với đó với **x=1 và y=-log(1-x)** kết quả ngược hoàn toàn, nhưng vẫn đạt đk 1+2 khi x càng tiến gần 0 thì y càng lớn và càng gần 1 (xa 0) thì y càng cao
+ $ Từ 2 thử nghiệm trên mình kết luận được TN1 giúp tính Loss khi cần x tiến đến 1. và TN2 khi cần Loss tiến đến 0.
+ @ Từ từ đã, 1 và 0 có thể đại diện cho 2 lớp, sẽ thế nào nếu mình kết hợp hàm loss cho cả TH1 và TH2.   
![[Pasted image 20251109214802.png]]
Để mô tả, mình có thể viết dưới dạng if 1 else 0, nhưng trong viết báo khoa học, mình cần mô tả công thức dưới dạng 1 phương trình -> ta có đc công thức Binary Cross-Entropy. Ta-Da.
![[Pasted image 20251109215611.png]]
![[Pasted image 20251109215746.png | 444]]

![[Pasted image 20251109220050.png]]
![[Pasted image 20251109220101.png]]
$\hat{y}$ have range from 0 to 1 -> perfect for classification. Tính hàm Loss với y=0 và y=1 rồi tối giản công thức. Xác suất thuộc range(0, 1). Công thức $f(y, \theta, x)$ thầy nói là gộp (Nhân) lại thì đc cthuc này. Vì nếu đặt x là 0 hay 1 thì nó vẫn trả về đúng công thức if else như mong đợi. 
![[Pasted image 20251109220311.png]]
Do là nhân nên sẽ tiến đến 0 hoặc 1 -> expoding gradient hoặc vanishing gradient -> Sử dụng log để biến thành tổng -> Hàm này nói để maximize giá trị -> Mình muốn lấy Minimize thì thêm dấu trừ ở trước là xong. 
![[Pasted image 20251109221329.png]]
Phần tiếp theo -> CM Convex. 

**Ý tưởng của Logistic Regression**
So sánh MSE và BCE 
Sau cùng Traditional -> Vectorize và so sánh. 
![[Pasted image 20251109222829.png]]

1) Overview lý do cần LoRes vì nó fit đúng data. 
2) Giải thích các bước của LoRes và đạo hàm hàm Loss
3) Giải thích trực giác của cách chọn hàm Loss MSE -> BCE. Vì sao ko dùng MSE -> 1 hàm loss lý tưởng sẽ ntn.  
4) Giải thích hàm loss BCE theo 2 hướng
	1) Trực quan hóa từ vấn đề, tiếp cận bài toán từ nhu cầu tìm 2 hàm loss mới để thay thế MSE (vì nó non-convex) - giải thích convex ở đây...convexity là gì. 
	2) Sử dụng XSTK, đi từ cthuc Benoulli cho bài toán phân loại nhị phân.  
5) So sánh MSE và BCE 
	1) bằng cách tính Convexity 
	2) Loss phạt các dự đoán sai khác nhau ![[Pasted image 20251110010008.png | 333]] 
6) 1 Cách tiếp cận khác là sử dụng Entropy
7) [LoRes code](https://youtu.be/HovUiBPojwo?si=97UDcm7Hu37-cd5S)

### Sigmoid and Tanh function
![[Pasted image 20251110020507.png]]
+ ? Can Tanh replace Sigmoid function ? 
As observe, we can see that sigmoid and tanh have some connect but we just haven't proven yet. 
![[Không có tiêu d_ 1.jpg# left ]]
1 - Image 1 & 2 look like Tanh / 2 = Sigmoid on the y-axis.
2 - Image 3 seem like tanh is just Sigmoid2 - 1 S3 = S2 - 1.
3- For image 3, look like we have to prove using math to find the relationship. 
![[Pasted image 20251110022228.png]]
1) Decomposition Tanh function and we get $$\frac{e^{2x} -1}{e^{2x}+1}$$![[Pasted image 20251110024142.png]]
2) Simplified the tanh(x) function by substract 2
$$\frac{e^{2x} + 1 - 2}{e^{2x}+1} = 1 - \frac{2}{e^{2x} +1}$$
![[Pasted image 20251110024205.png]]
+ ? At the end, we see that the function is quite similar to sigmoid, or should I say it sigmoid within tanh(x) function. 
To Conclude, we got a tanh(x) that use sigmoid as the loss function. Everything else stay the same. 
![[Pasted image 20251110024401.png]]
