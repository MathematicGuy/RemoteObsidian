ancronym: dgl -> được gọi là

**Câu 1. Nêu khái niệm của Trí tuệ nhân tạo và 3 ứng dụng kèm phân tích trên thực tế.**
+ Trí tuệ mô phỏng bộ não con người, có nghĩa là đảm bảo được 1 trong số các chức năng và hoạt động của bộ não con người, và nó là do con người tạo ra.
+ Nó sẽ không là trí tuệ nhân tạo nếu không đạt được 1 trong các điều kiện dưới đây
	+ Học Máy (Machine Learning)
	+ Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP)
	+ Thị giác máy tính (Computer Vision)
	+ Hệ thống chuyên gia (Expert System)
	+ Mạng nơ-ron nhân tạo (Artificial Neural Networks)
	+ Tự động hóa quá trình robot (Robotic Process Automation - RPA)
VD: AlphaGo của Deepmind học chơi cờ đam qua ML, GPT-4o quan sát sự vật và đưa ra miêu tả về nó.


**Câu 2. Học máy là gì? Sự khác nhau giữa học có giám sát và học không giám sát?**
Là 1 phần của trí tuệ nhân tạo cho phép máy học hỏi và cải thiện theo thời gian, dựa trên dữ liệu và kinh nghiêm mà không cần lập trình rõ ràng. (not require hard code to do a specific thing)

**Học có giám sát:** là mô hình học máy sẽ được huấn luyện trên các dữ liệu sẽ được gắn nhãn.
	VD: Dùng hồi quy tuyến tính để phân loại email vào thư rác và thư quan trọng dựa trên những giá trị được gắn nhãn. Gắn nhãn nếu giá trị  < 0.4 thì là thư rác, nếu giá trị >= 0.4 là thư bình thường.

**Học không giám sát:** dữ liệu huấn luyện không có nhãn và mô hình được huấn luyện để tìm ra cấu trúc của dữ liệu như là điểm giống nhau, khác thường, quy luật của dữ liệu đó. 
	VD: Những kĩ thuật sử dụng học không giá sát phổ biến là phân cụm (PCA chẳng hạn) và giảm kích thước áp dụng để xác định sự khác nhau và tương đồng của dữ liệu.  

**Câu 3. Vẽ mô hình học có giám sát và giải thích các khối.**
![[Pasted image 20240514180021.png]]
vd: phân loại động vật

+ **Input Raw Data**: Đây là dữ liệu thô cần phải được gắn nhãn
+ **Labels**:  Nhãn dùng để phân loại các đối tượng trong dữ liệu đầu vào.
+ **Algorithm**: Thuật toán được huấn luyện sử dụng dữ liệu gắn nhãn bằng cách điều chỉnh lặp đi lặp lại các tham số bên trong của nó để giảm thiểu sự khác biệt giữa các dự đoán của nó và các nhãn thực tế.
+ **Traning data set:** Là các tập dữ liệu được xử lý về cùng 1 dạng, chuẩn hóa và gắn nhãn.
+ **Desired Output:** Ví dụ cho kết quả đầu ra mong đợi
+ **Procssing:**  Xử lý các dữ liệu sử dụng thuật toán và đưa ra kết quả. 

**Giải Thích Cách Hoạt Động**:
+ Bao gồm huấn luyện máy bằng dữ liệu gắn nhãn
+ Dữ luệu gắn nhãn là 1 tập ví  với đáp án chính xác hoặc phân 
+ Máy học các mqh giữa đầu vào (ảnh động vật) và đầu ra (nhãn động vật: voi, bò, lạc đà)
+ VÍ dự bạn có 1 tập dữ liệu ảnh. Máy sẽ cần phân tích ảnh để trích xuất hình, màu và kết cấu. Rồi nó sẽ so sánh những đặc điểm của ảnh đó tới những đặc điểm của động vật đã học. Nếu đặc điểm của ảnh mới giống bò nhất thì nó sẽ đoán ảnh đó có con bò.
	(depression - lõm)
	+ Ví dụ hình dáng con vật trong ảnh có 2 màu đen và trắng, đuôi có chỏm lông, bụng phìng ra và đang ăn cỏ trên thảo nguyên.  Hình đó sẽ được gán nhãn là con bò.
Bây h, máy đã học đc kiến thức đó từ dữ liệu trước đó và lần này máy sẽ pải dùng nó 1 cách khôn ngoan. Máy sẽ phân loại con vạt với hình và màu sắc để xác nhận nó là BÒ và cho vào mục Bò. Vì máy học được điều đó từ dữ liệu huấn luyện (ảnh động vật) và sẽ áp dụng kiến thức đó để kiểm tra các dữ liệu mới (ảnh động vật mới) 

**Các lại học giám sát**
+ **Hồi Quy:** 1 vấn đề hồi quy là khi giá trị đầu ra là giá trị thật như là "củ khoai", "cân nặng". 
+ **Phân Loại:** 1 vấn đề phân loại là khi 1 giá trị đầu vào là 1 mục, ví dụ là "con bò", "con voi" hay "không bị bệnh", "bị "

Học có giám sát xử lý với hoặc học các dữ liệu gán nhãn. Điều này ám chỉ (cho thấy) vài dữ liệu đã được gắn nhãn đúng tr'c đó. (vd là người gắn nhãn rồi mới cho máy xử lý dữ liệu theo nhãn đã gắn) 

**Câu 4. Phân cụm là gì? Ý nghĩa của bài toán phân cụm dữ liệu?**
Phân Cụm là kỹ thuật máy không giám sát được sử dụng để nhóm các điểm dữ liệu tương tự lại với nhau trong tập dữ liệu. 
+ Mục tiêu của phân cụm là xác định các mẫu hoặc cấu trúc cơ bản trong dữ liệu mà không có bất kỳ nhãn nào được xác định tr'c. 
+ Vấn đề phân cụm dữ liệu liên quan đến việc tìm các nhóm hoặc cấu trúc vốn có trong các điểm dữ liệu sao cho các điểm dữ liệu trong một cụm tương ứng và khác biệt với các điểm dữ liệu trong các cụm khác.

**Câu 5. Mạng nơ ron là gì? Cho ví dụ về cấu trúc của mạng Nơ ron và giải 
thích? Các tham số trong mạng nơ ron gồm những gì?**
	references: https://nttuan8.com/bai-3-neural-network/

Mạng Neuron là mô hình học máy mô phỏng mạng lưới thần kinh của con người. Các tế bào não của con người, còn đc gọi là nơ-ro, tạo thành một mạng lưới phức tạp, có tính liên kết cao và gửi các tín hiệu điện đến nhau để giúp con người xử lý thông tin. Tương tự, 1 mạng nơ-ron nhân tạo được tạo ra từ các tế bào neuron nhân tạo, cùng nhau phối hợp để giải quyết 1 vấn đề. 
-  Mạng Neuron cơ bản thường bao gồm 3 lớp:
	- **1 lớp đầu vào**
		Dữ liệu gốc đi vào mạg nơ ron qua các nút đầu vào xử lý dữ liệu, phân tích hoặc phân loại và sau đó chuyển dữ liệu sang lớp tiếp theo.
	- **1 hoặc nhiều lớp ẩn** 
		Dữ liệu đi vào lớp ẩn đến từ lớp đầu vào hoặc các lớp ẩn khác. Mỗi lớp ẩn phân tích dữ liệu đầu ra từ lớp trước, xử lý dữ liệu đó sâu hơn và rồi chuyển dữ liệu sang lớp tiếp theo.
	- **1 lớp đầu ra**
		Lớp đầu ra cho ra kết quả cuối cùng của tất cả dũ liệu được xử lý bởi mạng nơ ron nhân tạo. Lớp này có thể có 1 hoặc nhiều nút. Vd: giả sử chúng ta gặp phải 1 vấn đề phân loại nhị phân (có/không), lớp đầu ra sẽ có 1 nút đầu ra, nút này sẽ cho ra kết quả 1 hoặc 0. Tuy nhiên, nếu chúng ra gặp phải vấn đề phân loại nhiều lớp, lớp đầu ra có thể bao gồm nhiều hơn 1 nút đầu ra.  

Tham số của mạng neuron cơ bản:
$$
a = \sigma(Wa+ b)
$$


- **a**: Đây là đầu ra (activation) của lớp nơ ron hiện tại.
	  
- **W**: Đây là ma trận trọng số (weights) giữa các nơ ron của lớp trước và lớp hiện tại.
	- **Vai Trò**: Trọng số xác định mức độ ảnh hưởng của đầu vào từ các nơ ron lớp trước đến đầu ra của nơ ron lớp hiện tại.
	- **Dạng**: Trọng số thường được tổ chức dưới dạng ma trận. Kích thước của ma trận này phụ thuộc vào số lượng nơ ron trong lớp hiện tại và lớp trước đó.
	- **Ví Dụ**: Nếu lớp trước có 3 nơ ron và lớp hiện tại có 2 nơ ron, ma trận trọng số W sẽ có kích thước 2×32×3.
	  
- **b**: Đây là vector độ dời (bias) của lớp hiện tại.
	- **Vai Trò**: Độ dời là một tham số bổ sung cho phép mô hình dịch chuyển hàm kích hoạt để phù hợp hơn với dữ liệu. Nó giúp mạng nơ ron học được các hàm phức tạp hơn.
	  
	- **Dạng**: Độ dời thường là một vector có kích thước bằng số lượng nơ ron trong lớp hiện tại.
	
	- **Ví Dụ**: Nếu lớp hiện tại có 2 nơ ron, vector độ dời bb sẽ có kích thước 22.
	  
+ **Sigmoid**:  Đây là hàm kích hoạt (activation function), được áp dụng cho tổ hợp tuyến tính của các đầu vào và trọng số.
	- **Vai Trò**: Hàm kích hoạt áp dụng một phép biến đổi phi tuyến tính lên tổ hợp tuyến tính của các đầu vào, trọng số và độ dời. Điều này giúp mạng nơ ron học được các mối quan hệ phi tuyến tính trong dữ liệu.
	
	- **Ví Dụ**: Các hàm kích hoạt phổ biến bao gồm
		hàm sigmoid
		$$
		(σ(x)=11+e−xσ(x)=1+e−x1​) 
		$$
		hàm tanh
		$$ 
		tanh⁡(tanh(x))
		$$               hàm ReLU 
		$$
		ReLU(max⁡(0,x))
		$$

Cấu trúc mạng neuron tích chập:
	Những lớp ẩn trong trong mạng neuron tích chập thực hiện các chức toán học cự thể, như tóm tắt hoặc sàng lọc được gọi là tích chập. Chúng được ứng dụng trong việc xử lý ảnh vì chúng trích xuất ra các đặc điểm liên quan từ hình ảnh, điều này có lợi cho việc nhận dạng và phân loại ảnh. Biểu mẫu mới dễ xử lý hơn mà không làm mất đi các đặc điểm quan trọg để đưa ra dự đoán chính xác. Mỗi lớp ẩn trích xuất và xử lý các đặc điểm hình ảnh khác nhau, như các cạnh, màu sắc và độ sâu.  


**Câu 6. Học trong mạng nơ ron là gì? Giải thích thuật toán back 
propagation?**
Học trong mạng Neuron bao gồm việc điều chỉnh trọng số và độ lệch của kết nối giữa các neuron để giảm thiểu sự khác biệt giữa các kết quả đầu ra được dự đoán mà kết quả đầu ra thực tế trong quá trình đào tạo. Quá trình này thường đạt được thông qua 1 thuật toán gọi là Lan Truyền Ngược (Back Propagation)
	Thuật toán hoạt động bằng cách tính toán lỗi hoặc tổn thất giữa đầu ra dự đoán và đầu ra thực tế, sau đó truyền ngược lỗi này qua mạng để cập nhập trọng số và độ lệch.
**Các bước của thuật toán Back Propagation**
1) **Forward Pass (chuyển tiếp):** trong quá trình chuyển tiếp, dữ liệu đầu vào được đưa vào mạng và đầu ra được tính toán.
2) **Loss Calculation (tính toán tổn thất):** tổn thất hoặc lỗi đc tính bằng cách so sánh đầu ra dự đoán với đầu ra thực tế
3) **Back Propagation (truyền ngược):** Lỗi sau đó được truyề ngược theo từng lớp, tính toán độ dốc của lỗi liên quan đến trọng số và độ lệch.
4) **Weight Update (cập nhật trọng số)**: Trọng số và độ lệch được cập nhật bằng thuật toán tối ứu hóa để giảm thiểu lõi.
5) **Lặp lại:** Lặp các bước 1-4 nhiều lần cho đến khi mạng hội tụ về 1 giải pháp thỏa đáng. 


**Câu 7. Mạng CNN là gì? Khác gì với mạng nơ ron truyền thống?**














**Câu 8. Trình bày các lớp và vai trò của nó trọng mạng CNN.**



**Câu 9. Cửa số (filter) được sử dụng như thế nào trong lớp tích chập?**



**Câu 10. Giải thích việc tính toán cho lớp tích chập trong mạng CNN.**



**Câu 11. Liệt kê các thư viên chính sử dụng trong các bài toán mạng học sâu trên Google Colab.**



**Câu 12. Thực hành trên Google Colab cho bài toán phân loại ảnh. Bổ sung thêm lớp mới, thay đổi hàm kích hoạt, huấn luyện với các bộ dữ liệu khác nhau và trình bày vào bảng kết quả.** Link
https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/classification.ipynb

