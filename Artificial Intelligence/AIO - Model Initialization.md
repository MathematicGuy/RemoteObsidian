**OBJECTIVE**
![[Pasted image 20241120200438.png]]

**Experimental Result**
![[Pasted image 20241120201419.png]]
**ReLU:** Loss giữ nguyên ở 10, ko học đc -> bước nhảy quá lớn. vì ReLU lấy a = 255 hoặc 0 nên giá trị sẽ rất lớn kể cả khi đạo hàm.
(Cần Normalize thêm nếu dùng ReLU)

![[Pasted image 20241120201439.png]]
**Sigmoid**: ổn định hơn vì giá trị luon đc chuẩn hóa qua hàm Sigmoid.
-> ReLU ko phair luon luon mạnh hơn Sigmoid.

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
**PReLU Function**
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

Từng vị trí có giá trị bằng nhau -> uniform
![[Pasted image 20241120205037.png]]
Do xác suất rời rạc nên dùng f(x) thay vì P(X)
![[Pasted image 20241120205301.png]]
Lấy nguyên hàm cho hàm tích phân
![[Pasted image 20241120205417.png]]
Summarize
![[Pasted image 20241120205450.png]]

