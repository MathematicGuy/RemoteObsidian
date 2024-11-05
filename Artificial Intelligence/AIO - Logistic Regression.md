# Basic Logistic Regression
**Index**
Xem Xét Loss with Validation
Optimal Learning Rate
24GB with Optimal able to run with 10k epoch 

Logistic Regression for Classification Task.
![[Pasted image 20241029201736.png]]
Predict output $[0, 1]$ for continuous input. 

Convert linear func into sigmoid function, and set a threshold for sigmoid func to predict.
![[Pasted image 20241029202731.png]]

**Logistic Regression using Gradient Descent**
Loss-Log (Cross-Entropy Loss)
![[Pasted image 20241029202932.png]]
Note: Log is natural log (i.e. ln) if it doesn't go with base 10 like this: $\log_{10}a$.
Độ đo phù hợp là: Accuracy.
+ ? Theta $\theta$ and Weight $w$ have the same numbers as total features.

## Optimization
khả vi: tính đạo hàm đc tại 1 điểm

## Idea of Logistic Regression
**Condition: iead must come from linear regression**
Tại sao dùng hàm f(x): vì từ x có thể suy ra y (kết quả)
![[Pasted image 20241030202516.png]]


**Linear Regression use to fit data.** This mean the line or multivariable function been coordinate best so it closest to all the data points.

After function f(x) was coordinate (fit) to the best position. **We need a function between to compress f(x) to $[0, 1]$ range. To predict base on Possibility and statistic.**

This function, come from:
Piere Francos muốn mô phỏng **sự thay đổi của 1 quần thể theo thời gian.**
![[Pasted image 20241030202908.png]]
+ ! Cần 1 hàm nào đó đi qua tất cả các điểm này. (Sigmoid?)

**Sigmoid đến từ 1 phương trình vi phân của mô hình [[Logistic Growth (to Sigmoid)]].** 
![[Pasted image 20241031001014.png]]
Vi Phân: (Hiếm khi sử dụng trong Deep Learning)
![[Pasted image 20241030202924.png]]
![[Pasted image 20241030203222.png]]
![[Pasted image 20241030203239.png]]
There we go, that how I meet sigmoid function
![[Pasted image 20241030203426.png]]
phương trình đối xứng $[0, 0.5]$ và $[0.5, 1]$, cho phép fit dữ liệu x trong khoảng từ $\int_{-\infty}^{\infty}$  và y bị ép vào khoảng $[0, 1]$
có thể dịch chuyển b để giúp hàm fit vs data của mình.

**What is Sigmoid function capability?**
say your data be reverse, sigmoid can tweak through n iteration and fit itself again.
+ $ Capability of adapting to new data.
	![[Pasted image 20241030204844.png]]

example of sigmoid function for x input
![[Pasted image 20241030204802.png]]

**What loss function should I use ?**
since the perfect function would go through all data points. The loss function should tell us how far apart the function to all data point. 
sigmoid fit data and have output $[0, 1]$ range. The closer to 1 the better f(x) fit. 
There for, subtract 1 - f(x) should give us the loss. 
![[Pasted image 20241030205718.png]]

(Đoạn này kiểm tra bài thực hành Logitstic thầy cho)
vấn đề bị nhiễu, giải pháp -> chia ra từng sample. batch để huấn luyện. 
![[Pasted image 20241030210950.png]]
Derivative of Sigmoid  
![[Pasted image 20241030211646.png]]
+ ? Em ko nghe rõ phần hàm mất mát ad giải thích ntn lắm. E đang hiểu đc là ad có nói là đầu ra của sidmoid là 0 hoặc 1. Hàm sigmoid càng chính xác sẽ đi qua càng nhiều điểm và sigmoid gần với 1 hơn. Nên bằng cách lấy 1 - y_hat sẽ trả lại giá trị mất mát ạ?
![[Pasted image 20241030214556.png]]
Convex Function: reverse derivative
Logistic ko convex nên ko.

### Rethinking Logistic Regression
hàm loss phải có tính liên tục + khả vi.
![[Pasted image 20241030214456.png]]
y = 0, nên y mũ gần 0 thì loss sẽ nhỏ. và khi y mũ gần 1 loss sẽ tăng.

Theo cảm nhận thì: mô hình tốt, mất mát nhỏ -> $\hat{y} \to 0$. Ánh xạ từ đầu vào X sang Y và ngược lại khi $\hat{y} \to 1$ (note: đoạn này chưa quan tâm đến hàm Loss vội)
![[Pasted image 20241030214817.png]]
![[Pasted image 20241030214943.png]]
đoạn này thầy giải thích convex của đạo hàm 2 lần sẽ ntn cho y=0 và y=1.
![[Pasted image 20241031002025.png]]


Gợi ý 1 số hàm loss (mất mát), hàm nào tốt nhất?
![[Pasted image 20241030215241.png]]
+ $ Số 4 $y = -log(1-x)$

+ ! Y >= 0. Nên mọi hàm < 0 sẽ sai. $\log(y)$ ko thể tính khi y < 0.  
Khi y = 0. thì y mũ gần 0: $\hat{y} \to 0$, loss sẽ nhỏ. Dùng hàm số 4 sẽ hợp nhất
Khi y = 1. thì y mũ gần 1: $\hat{y} \to 1$, loss sẽ nhỏ. Dùng hàm số 6 sẽ hợp nhất
![[Pasted image 20241030215912.png]]
+ Ví dụ trên đi từ cảm nhận, sau đó mới tiến tới lý thuyết. 
Reason why for y=0 and y=1, yhat have log like above. Replace y=0 and y=1 to Binary cross-entropy function, we have these fomular.
![[Pasted image 20241031002658.png]]

**Logistic Regression Summary**
![[Pasted image 20241031002805.png]]

Information Theory để hiểu log hơn. Log-Loss Entropy đến từ Information Theory.

Đạo hàm bậc 2 của Binary Cross-Entropy nếu >= 0 hay ko? nếu có thì f(x) sẽ convex -> loss tối ưu về giá trị nhỏ nhất. 
![[Pasted image 20241030222339.png]]
![[Pasted image 20241030223026.png]]
+ Lý do vì sao cần tính convex -> để kiểm tra loss >= 0

--- 
### Cross Entropy Proof and Explaination
![[Pasted image 20241030224223.png]]
Nếu lấy ra bi xanh thì sẽ ngạc nhiên hơn.
How to measure suprise: $\frac{1}{P(E)}$ (The lower a event happened, the larger the suprise, make sense)

**Note: Cái gì muốn quy 0 thành 1, hay 1 thành 0 thì dùng $\log$.** Ex: log(1) ~ 0 (a càng gần 1 thì log(a) càng gần 0)
 + ? $\log(Suprise(E))=\log\left( \frac{1}{P(E)} \right) = -log(p(E))$ -> **đo mức độ ngạc nhiên của 1 sự kiện trong 1 hệ thống.**
![[Pasted image 20241030224607.png]]

Giả dụ tính độ bất ngờ của 2 Event: E1 và E2 bằng cách tính tổng chia 2. Ta thay 1/2 bằng trọng số $\lambda$ (vì sao???) ta đc:
![[Pasted image 20241030224811.png]]
bây h nó trở thành **Expected Value**. Tính trung bình có trọng số.
![[Pasted image 20241030224858.png]]
Suprise = E(log(p)) = $\sum p_{i}\log_{i} (p)$ 
Entropy **(đo mức độ hỗn loạn of the system itself**) -> nên chọn chính sự kiện trong cái hệ thống đó là p làm trọng số.

Khi tính entropy thì tính trung bình của cả hệ thống chứ ko lấy chỉ 1 cái event.
(50% thành phần này, 50% thành phần khác -> có thể có độ nhiễu rất là cao)

(đoạn này ko nghe rõ, mai note lại)
giá trị $\hat{y}$ là xác suất của x khi y=1 (ko nhắc tới y=0)
(Đoạn dưới đây liên hệ sigmoid với cross-entropy)
![[Pasted image 20241030225730.png]]
![[Pasted image 20241030230104.png]]

![[Pasted image 20241030230351.png]]

y0 đo suprise của giá trị thứ 1st. y1 đo suprise cho giá trị thứ 2.
![[Pasted image 20241030230442.png]]
gọi là cross-entropy vì 1 giá trị đc lấy thêm từ hệ thống bên ngoài.
>giá trị đó đc lấy cái xs từ 1 cái hệ thống khác đưa vào
+ ? còn binary là do nhị phân

**1 số câu hỏi hay**
+ vì sao eigenvalues >= 0 thì hàm sẽ convex vậy ạ
+ Vì sao determinant >= 0 lại...

---
### Prove Convexity of (Binary) Cross-Entropy


# Advance Logistic Regression 
## Vectorization 
+ ? Logistic Regresison for Multivariable

All the Steps stay the same:
![[Pasted image 20241101204516.png]]
**Matrix multiplication**
1) $z = w.x + b$. remember $X.\theta \neq \theta.X$ since $X.\theta = \phi$ (ko tính đc)
![[Pasted image 20241101204359.png]]

$$\hat{y} = \sigma(z) = \frac{1}{1+e^{-z}} = \frac{1}{1+e^{-\theta.X}}$$

Hessian matrix example for single input (y = wx + b)
![[Pasted image 20241101204830.png]]

**Update Parameter $\theta$ :**
With $\theta$ as $\bar{w}, \bar{b}$ **where** 
	$\bar{w} = {w_{1}, w_{2}, w_{3},\dots,w_{n}}$  
	$\bar{b} = {b_{1}, b_{2}, b_{3},\dots,b_{n}}$
basically we want to use $\theta$ to represent all weight $w$ and bias $b$.
We know their partial derivative is $\nabla L = X(\hat{y}- y)$. So to update all weight and bias we simply update $\theta$ :
$$\theta = \theta - X(\hat{y} - y)$$
now we get:
![[Pasted image 20241101205027.png]]

### Linear Regression for m-samples

Loss function for m-samples is the same as how $z=X.\theta$ and $\hat{y}$ vectorize:
![[Pasted image 20241101214012.png]]

**Compute Loss**
![[Pasted image 20241101214247.png]]
re-write them in vector form.
![[Pasted image 20241101214240.png]]
then we have:
![[Pasted image 20241101214424.png]]

note: replace 1 with $x_{1}^{(1)}, x_{2}^{(2)}$ 
![[Pasted image 20241101214512.png]]
combine the into 1 vector
![[Pasted image 20241101214713.png]]

+ $ Conclusion: Vectorization is a practice to convert variable into vector where the vector represent multiple variable. This allow us to present fomular as  vectors and calc parallel all variable at once when implement using numpy.

### Sigmoid and Tank Functions
tanh(x) (is this tan h(x) ???)
![[Pasted image 20241101221755.png]]
**relationship between sigmoid(x) and tanh(x)**
![[Pasted image 20241101221704.png]]

**Convert Sigmoid into Tanh(x)**
![[Pasted image 20241101222040.png]]

