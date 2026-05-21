**OBJECTIVE**
![[Pasted image 20241120200438.png]]
[Weight Initialization](https://www.geeksforgeeks.org/weight-initialization-techniques-for-deep-neural-networks/)

**Experimental Result**
![[Pasted image 20241120201419.png]]
**ReLU:** Loss giữ nguyên ở 10, ko học đc -> bước nhảy quá lớn. vì ReLU lấy a = 255 hoặc 0 nên giá trị sẽ rất lớn kể cả khi đạo hàm.
(Cần Normalize thêm nếu dùng ReLU)

![[Pasted image 20241120201439.png]]
**Sigmoid**: ổn định hơn vì giá trị luon đc chuẩn hóa qua hàm Sigmoid.
-> ReLU ko phải luon luon mạnh hơn Sigmoid.

## Gradient Vanishing

**Gradient Vanishing Có thể xảy ra khi có quá nhiều layer** dẫn tới các bước đi ko có tác dụng.
note: luyện tập bằng cách tự tính tay lại. s là sigmoid 

Với 5 lớp:
![[Pasted image 20241120202646.png]]
![[Pasted image 20241120202807.png]]
Với 8 lớp:
![[Pasted image 20241120202857.png]]

## Gradient Explosion
>Large weight initialization and large learning rate. Đây là khi đạo hàm lớn mất cân bằng. Ngược lại đối vs Gradient Vanishing.
![[Pasted image 20241120203051.png]]

## Activation Functions
**PReLU Function**: khắc phục vấn đề Dying ReLU.
![[Pasted image 20241120203615.png]]

**Mean**
![[Pasted image 20241120203546.png]]
![[Pasted image 20241120203936.png]]

**Variance**
![[Pasted image 20241120204528.png]]
note: sum of P(X) = 1, that why it get remove
![[Pasted image 20241120204123.png]]

Với tham số X, Y độc lập, Variance là:
![[Pasted image 20241120204743.png]]
**summary**
![[Pasted image 20241120204927.png]]

# Initialization Methods
### Xavier Glorot Initialization
+ ? Cần chuẩn hóa dữ liệu có range [-1, 1] và z-score
+ ? Giả định activation dùng Sigmoid và Tanh (vì hồi Glorot ra chỉ có 2 cth này)

Từng vị trí có giá trị bằng nhau -> uniform
![[Pasted image 20241120205037.png]]
Do xác suất rời rạc nên dùng f(x) thay vì P(X), ta chuyển đổi hàm sang tích phân
![[Pasted image 20241120205301.png]]
Lấy nguyên hàm cho hàm tích phân
![[Pasted image 20241120205417.png]]
Summarize
![[Pasted image 20241120205450.png]]

Gắn hàm E vào lại công thức, ta đc  
![[Pasted image 20241120205526.png]]

Gaussian Distribution (Normal Distribution)
![[Pasted image 20241120205746.png]]

![[Pasted image 20241120205923.png]]
note: Maclaurin là TH đặc biệt của Taylor khi x ~ 0
![[Pasted image 20241120210240.png]]
 
# How to avoid Gradient Vanishing and Explosion

Luồng variance từ lớp này sang lớp khác ko thay đổi thì ko bị gradient vanish/explo

![[Pasted image 20241120214720.png]]
Để đạt đc điều trên, ta normalize hoặc dùng activation function (tanh, sigmoid)

Giả sử (với layer đầu)
![[Pasted image 20241120212759.png]]
Vs b = 0  và giả sử mỗi biến là các tham số độc lập IID
![[Pasted image 20241120213015.png]]

Từ z -> a sẽ lặp lại trong hidden layer, nên z->a có tính chu kỳ và chỉ cần kiểm tra var của z->a có thay đổi hay ko là đc.
![[Pasted image 20241120213512.png]]
(missing a image)
![[Pasted image 20241120213824.png]]


2) Với layer ở giữa
Để Var(a) = 0, dùng activation
	tanh(a) - đối xứng qua 0
	sigmoid - dịch chuyển từ a = 1/2 (+ x/4)
![[Pasted image 20241120214954.png]]

![[Pasted image 20241120215122.png]]
Summary
![[Pasted image 20241120215138.png]]
Để luồng thông tin ổn định
![[Pasted image 20241120215247.png]]

2 và 3 vì model construction cho số lớp 
![[Pasted image 20241120220601.png]]

---

![[Pasted image 20241120221846.png]]

![[Pasted image 20241120222037.png]]

Summary
![[Pasted image 20241120222308.png]]
![[Pasted image 20241120222327.png]]

