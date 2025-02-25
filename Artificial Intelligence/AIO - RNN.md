## Text Classification
+ Tokenize: Chia các từ ra từng unique character
+ Processing: xóa bỏ những ký tự ko cần thiết/quan trọng
+ Embedding: Chuyển từng unique char thành số (số vector)
	Tạo từ điển riêng cho từng câu khác nhau. "key : value" cho "chữ : số"	![[Pasted image 20241218201726.png]]
Nhưng nếu vs 1 từ nhiều nghĩa thì thể hiện như thế nào?
different word are enormous, how to represent 'text' effectively. -> acronym. 

Normalize độ dài của chữ. dùng padding là số 0 để chèn vào ô trống. Vd: thấy có 4 từ, nhưng đi có 2 từ nên phải thêm 2 số 0 vào để cân bằng list. 
+ ! Không có tính tương tác từ trái sang phải. 

### Step 1: Tokenization
![[Pasted image 20250224150201.png]]
>Token each word as a unique token. However each word can represent many meaning. 
+ ? How to make 1 word to represent 2 meaning  using number ? 
	$8 \to (x_{1}, x_{2})$ where both $x_{1}, x_{2}$ value changes through the training process.
+ $ After training process, similar meaning words come closer together in multi-dimensional space.
![[Pasted image 20250224150532.png]]

Mỗi từ biểu diễn bằng 1 số bằng cách nào ? 
+ $ -> Sử dụng dictionary trong python hay nói đúng hơn là tham chiếu từng token với 1 số.  (Embedding)
+ ? Với những từ không có trong từ điển đặt bằng `'<UNK>'` đại diện cho unknow word với id sau khi embedding là 0.
![[Pasted image 20241218204738.png]] 

Sau đó mỗi embedding id được chuyển sang dữ liệu tensor. Việc này chuyển đổi không gian biểu diễn (của từ) từ không gian 1D sang không quan đặc trưng. 
+ ? Lý do cho việc này là gì các mô hình học sâu làm việc với dữ liệu liên tục (continuous numerical data). Việc chuyển dữ liệu đầu vào sang không gian đặc trưng nghĩa là biểu diễn từng token như 1 vector (i.e. tensor) trong không gian liên tục.
+ $ Việc này giúp các từ thể hiện được đặc trưng không gian của nó tốt hơn và giúp mình nắm bắt đc mối quan hệ trong không gian của mỗi từ  (e.g. sử dụng khoảng cách euclit), ngoài ra mô hình sử dụng tensor cũng áp dụng tính toán ma trận để tìm ra các đặc tính, học các ràng buộc và hiểu ngữ cảnh của toàn bài.
![[Pasted image 20250224151810.png]]
Sử dụng MLP để xử lý, từng feature tensor đại diện cho 1 đầu vào thì đối với lượng dữ liệu lớn, mô hình sẽ không thể xử lý được 1 cách hiệu quả. 
e.g. 1000 từ -> vector 1000 đặc trưng 
![[Pasted image 20250224151400.png]]
Mô hình MLP tính toán như bình thường sử dụng linear regression với tensor là X nhân với W là weight cộng với bias b. 
Bằng cách này, mỗi tensor đều chia sẻ cùng 1 weight W và nối liền thành 1 vector đặc trưng. 
+ ? Mỗi Tensor được nối liền với 1 bộ Tham số chung. (Shared Weight) -> Việc này giúp thể hiện mqh giữa mỗi tensor khi model học -> tránh TH quá tải weight khi số lượng từ (tensor) quá lớn.
(**Liên hệ với CNN:** W hoạt động cũng giống như 1 kernel, áp dụng cho cả 5 input để cùng trích xuất đặc trưng của từng từ và học mqh giữa các từ)
![[Pasted image 20250224153410.png]]
Tuy nhiên vấn đề về tính tương đồng vẫn chưa được xử lý.

**Mục tiêu:** 
+ **Làm hàm** $h_{1}(z_{1})$ **non-linear bởi vì nếu linear thì mô hình sẽ chỉ học đc dữ liệu đơn giản** và ko học được dữ liệu phức tạp hơn. -> Dùng tanh() để biểu diễn dữ liệu dưới dạng non-linear.
+ **Làm $h_{2}$ phụ thuộc vào** $h_{1} \to h_{2} = f_{2}(z_{2}, h_{1})$  
+ ? Note: *nhìn nhận việc sử dụng h1 để tính h2 như là dịch chuyển không gian của h1 sang h2 để tính h2.* (vì cùng không gian mới tính đc) - **important**
![[Pasted image 20250224155133.png]]
Vậy nên để tính sự ràng buộc giữa $h_{n}$ và $h_{n-1}$ mình cần 1 bước để chuyển đổi không gian từ $h_{1}$ sang $h_{2}$ sử dụng Linear transformation **(thay đổi không gian trong đại số tuyến tính)**: 
$$W_{hh}h_{1}+b_{hh}$$
rồi mới tính toán $h_{1}$ và $h_{2}:$
$$h2=tanh(z_{2} + W_{hh}h_{1}+b_{hh})$$
trong đó $z_{2}=(W_{xh}X_{2}+b_{xh})$ 
![[Pasted image 20250224161420.png]]
Như trong MLP, h1 đến h5 đều có cùng 1 tính chất nên đều dùng cùng 1 bộ tham số (i.e. 4 tham số trong W).
![[Pasted image 20241218220039.png]]
Sau khi có được góc nhìn tổng quan, mình xem lại cách tính được biểu diễn ntn.
1) **Tensor của từng word được flatten về vector 1 chiều.**
	![[Pasted image 20250224163416.png]]
2) ? **note: chiều dài (số cột) của W luôn tương ứng vs chiều rộng (số hàng) của X**. Và giá trị khởi đầu bằng 0 vì chỉ cộng vs bias.
	![[Pasted image 20250224163516.png]]
### Text Deep Models
![[Pasted image 20250224221139.png]]![[Pasted image 20250224221557.png]]
**Tính parameters**
In: 6 
Out: 8
Số Lớp: 2 
Phép tính có thêm bias sẽ +1 tham số. Ở đầu tiên 6 cộng thêm 1 là 7, vậy tổng tham số của phép tính đầu là 7 * 8 = 56.  

Đầu ra là 8, phép tính để chuyển đổi không gian $h_{1}$ sang $h_{2}$ là 8 cộng thêm bias là 9, nên tổng tham số thứ 2 là: 8 * 9 = 72

Phép tính thứ 3 tương tự như phép tính đầu là 7 * 8 = 56.
=> Tổng tham số $72 + 56 \times 2 = 184$
![[Pasted image 20250224223741.png]]
N tổng sample, L là số layers, H_out là đầu ra cuối cùng và cũng là đầu ra của $h$. 
![[Pasted image 20250224225251.png]]
Stack of RNNs
![[Pasted image 20250224225457.png]]
note: nhìn h1 truyền lên như là đầu vào X1, X2 thôi.

Ví dụ tính tham số 2:
Vocab_size = 8, emb_dim =4 -> Embedding có tổng tham số là 8 * 4 = 32.

![[Pasted image 20250224230442.png]]