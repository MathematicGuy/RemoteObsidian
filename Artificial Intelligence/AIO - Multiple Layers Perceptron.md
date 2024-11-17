TH: Áp dụng cho dữ liệu ảnh
Note: 
1bytes = 8bits
1 ảnh 28x28 = 784 pixel.
File gồm 60000 ảnh được nén dưới dạng 1 array: 60000 * 784 pixles
![[Pasted image 20241113203743.png]]

Mỗi ảnh được thể hiện bằng 4 bytes ~ 32bits
![[Pasted image 20241113204027.png]]

```python
.reshape(-1, 28*28) # -1 để tự xác định số hàng là 60000
```

# Review Code
download dataset from online url
![[Pasted image 20241113205056.png]]

> Read file dataset
![[Pasted image 20241113205217.png]]
+ 'rb': reade bytes
+ uint8 - 0 to 255
+ offset: ?

PIL-image: 1 kiểu dữ liệu ảnh

![[Pasted image 20241113211220.png]]
+ 1 kênh màu, 28 hàng, 28 cột (dữ liệu có dạng này vì pytorch đc thiết kế vs tâm lý cho ảnh 3D, CNN)


![[Pasted image 20241113211826.png]]
batch_size ~ batch size
num_workers: number of run in parallel
shuffle: shuffle each batch

>automatical stop when out of datas
![[Pasted image 20241113212434.png]]


![[Pasted image 20241113213705.png]]
batch size = 10

![[Pasted image 20241113213729.png]]
batch_size: 5
hàng x cột: 28x28

Lưu ý: nếu **normalize cho 1 data thì phải normalize hết mọi data**, test, train, etc...

Lý do hidden layer thực chất chỉ cần 1 activation function nếu có 1 hay n node:
$z_{0} = \theta^T.X_{0}$
$z_{1} = z_{0}.X_{1}$
$z_{1} = \theta^T.X_{0}.X_{1}$
written X as a matrix. $Z$ basically 1 function: $Z = \theta^T.X$


Motivation: softmax regression ko làm tốt cho dữ liệu ảnh


![[Pasted image 20241113224348.png]]
1 sample có 784 tham số, sau khi đi qua linear array 1D trở thành 256, đi qua reLu vẫn là 256, đi qua Linear trở thành 10 tham số.
note: 'bs' là batch size
![[Pasted image 20241113224435.png]]

vanishing gradient: giá trị đạo hàm sau cập nhập quá nhỏ. Vd sau khi đi qua 1 hàm kích hoạt giá trị bị chia 4, thì giá trị sẽ dễ dàng bị siêu bé sau nhiều lần đạo hàm -> vanishing gradient.

Improve model -> Add more layers


# Results
LR = 0.01 (quite high), normalize 0-255 to 0-1
Result: Bad
![[Pasted image 20241114105651.png]]
+ $ Conclude: Normalize data and increase number of nodes in a hidden layers or increase number of hidden layers can improve result.   

---
# Insight into Multi-layer Perceptron
>Đi sâu vào mỗi phần sau, bây h học tổng quát và học cách sử dụng tr'c

**To-do List for Training**
![[Pasted image 20241115200929.png]]

![[Pasted image 20241115201942.png]]
1b 2a 3c

Cho data FashionMNIST:
![[Pasted image 20241115202329.png]]
note: dù kết quả có thể chạy tốt hoặc ko chạy tốt, nhất định mình phải có ý kiến, nhận xét về nó. 

Batch Normalization is the most effective

### How many nodes ?
+ ? Vì sao có nhiều lớp -> để trích xuất dữ liệu/đặc trưng hơn. e.g. để trích xuất dữ liệu từ 1 ảnh 70x70 ko thể dùng NN gồm 1 hidden layer vs 2 nodes đc. 
![[Pasted image 20241115204519.png]]
+ $ Kết luận: dựa vào thử nghiệm và kinh nghiệm. Tăng số lượng layers có thể tăng khả năng của model nhưng có thể dẫn tới overfitting nếu có quá ít data. Khả năng model nên đi cùng với số lượng data, vấn đề dễ, model dễ và ngược lại.

### Activation Functions
note: vì sao sử dụng ReLU.
![[Pasted image 20241115205034.png]]
+ ? Điểm yếu của ReLU là nó sẽ tiến tới 1 giới hạn và gần như ko thể nhỏ hơn đc nữa (vì tăng trưởng quá chậm) ![[Pasted image 20241115210101.png]]
+ **ReLU Intuition:** **Feature có ý nghĩa đc thì giữ nguyên, Feature ko quan trọng thì cho bằng 0**.
	-> giải quyết vấn đề Gradient Vanishing vì nó lấy mọi giá trị có ý nghĩa. 
+ ! Tuy nhiên, trong **TH muốn giữ lại tất cả những dữ liệu thì ReLU ko phải là 1 lựa chọn tốt**. Ví dụ khi train nhiều layers, mình muốn giữ lại 1 số thông tin để train tiếp.

+ ? Tanh cũng gặp vấn đề này ![[Pasted image 20241115210205.png]]

+ ? **LeakyReLU(x)** khi giá trị có vấn đề thì mình đặt nó bằng 0.01 -> chống TH mất đi giá trị
+ ! Tuy nhiêm, tham số cứng như 0.01 là ko tốt. 
![[Pasted image 20241115211429.png]]

+ $ **ELU**: tốt hơn ReLU ở 2 chỗ, chống bằng 0 
+ ? ReLU: thường dùng trong xử lý ảnh
+ ? Swish Funtion ![[Pasted image 20241115212029.png]]
note: swish 1 là đặt giá trị a bằng 1

**GELU đc dùng nhiều nhất gần đây** (có sử dụng trong ChatGPT)
> Hàm đc dựng từ hàm CDF của Gaussian (1 hàm tính tích phân).
![[Pasted image 20241115212620.png]]
+ ? Khả năng học của mô hình lớn.

### MLP Example 
![[Pasted image 20241115213634.png]]
note:
+ ReLU cho giá trị âm về hết 0, chỉ lấy gtri dương.
 + w được khởi tạo ngẫu nhiên

Tính lớp thứ 2
![[Pasted image 20241115213851.png]]
đưa kết quả vào hàm softmax để tính xác suất
![[Pasted image 20241115213939.png]]

Do cùng lớp vs x, nên ta có thể ghép giá trị bias b bằng 1 vào cùng ma trận x.
![[Pasted image 20241115214247.png]]
Do x nhân ma trận với w, mình có thể đặt hàng 1 của w bằng 0 để triệt tiêu bias ở x.
![[Pasted image 20241115214625.png]]

### Example 2 - Dying ReLU
![[Pasted image 20241115220222.png]]
giá trị ở h2 nhỏ hơn 0 và ko thể thay đổi đc nữa -> phí hiệu suất model để tính h2 trong các iterations sau.
+ ? Nếu tham số bằng 0 hết thì theta sẽ ko update đc. Vì chỉ còn b -> mô hình ko học đc. Nếu b=1 thì input sẽ luon=1.

![[Pasted image 20241115222423.png]]
>AI vì vấn đề Gradient Vanishing, giá trị đạo hàm nhỏ xuất hiện khi có nhiều layers.  

1 số Activation Function vs quá nhiều Hidden layers có thể khiến Gradient Vanishing
![[Pasted image 20241115224235.png]]

