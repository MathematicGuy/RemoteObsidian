Make Artificial Neuro for simulating brain activity
Basic neuron: input - hidden -output layers

Hidden layer and node depend on the designer (with experience)


Mặc dù Mạng Neuron thông thg đã có nhiều ứng dụng, tuy nhiên nếu gặp các bài toán như xử lý ảnh, xử lý văn bản, xử lý dữ liệu lớn sẽ bị hạn chế. Năm 2006, đánh dấu sự ra đời của mạng neuron nhiều lớp (hay còn gọi là mạng neuron sâu) - deep learning (1 số loại phổ biến: CNN, LSTM - long short term memory). 
Cấu trúc của mạng CNN: lớp tích chập, lớp pooling, lớp fully connected


Lớp tích chập đầu tiên sẽ dùng 1 cửa sổ để quét ma trận dữ liệu đầu vào từ trái qua phải từ trên xuống 
Max/Min/Average Pooling - lớn/nhỏ/trung bình 

sau 1 số lần sử dụng luân phiên (Convo + Acti Func (ReLU) + Pooling)(k lần)


Mạng neron học sâu vs thông thường
+ Có thêm 1 số lớp. (Đối vs mạng CNN -> lớp tích chập, lớp pooling)
+ Để tạo ra các bản đồ đặc trưng (feature maps) của dữ liệu. Giúp hệ thống nhìn rõ đối tượng cần xử lý hơn. 

Feature - đặc trưng
Để nhận dạng hìh ảnh phải dựa trên các đặc trưng. Ko phải giá trị
	Các đặc trưng có kết nối vs nhau.
Tại sao lại cần CNN để tạo ra các features?

	+ Hình ảnh vector tại cái lớp phẳng.