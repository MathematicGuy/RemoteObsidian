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

ND Chính:
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



**Câu 5. Mạng nơ ron là gì? Cho ví dụ về cấu trúc của mạng Nơ ron và giải 
thích? Các tham số trong mạng nơ ron gồm những gì?**



**Câu 6. Học trong mạng nơ ron là gì? Giải thích thuật toán back 
propagation?**



**Câu 7. Mạng CNN là gì? Khác gì với mạng nơ ron truyền thống?**



**Câu 8. Trình bày các lớp và vai trò của nó trọng mạng CNN.**



**Câu 9. Cửa số (filter) được sử dụng như thế nào trong lớp tích chập?**



**Câu 10. Giải thích việc tính toán cho lớp tích chập trong mạng CNN.**



**Câu 11. Liệt kê các thư viên chính sử dụng trong các bài toán mạng học sâu trên Google Colab.**



**Câu 12. Thực hành trên Google Colab cho bài toán phân loại ảnh. Bổ sung thêm lớp mới, thay đổi hàm kích hoạt, huấn luyện với các bộ dữ liệu khác nhau và trình bày vào bảng kết quả.** Link
https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/classification.ipynb

