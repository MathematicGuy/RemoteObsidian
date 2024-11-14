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
