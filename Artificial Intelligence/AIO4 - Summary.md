Hồi quy là gì?

1) Giải thích tổng quan
hàm loss (vì sao hàm loss ntn, khác gì so vs linear)-> note thêm về convex. giải thích vì sao cần convex ? 

Giải thích vì sao dùng cth (sigmoid) ? so sánh linear vs logistic regress -> giải thích fit là gì? Tại sao logistic tốt cho bài toán này  

Demo bằng việc: Áp dụng bài toán (demo cả code và cách làm)

Giải Thích:
+ normalize/standardize -> lý do lại scale -> vì sao chọn cth này 
+ Việc thêm 1 vào X (nhắc tới vectorization và tối ưu việc tính toán) 
+ vì sao khởi tạo random 
+ lưu kết quả để visualize

note: machine translate NaN to 0. look for these unreasonable values.
Ex: Glucose value of fat people = 0
2 choices -> replace with mean/median value or remove

addition validate technique: f1, resident recall, 

### Softmax Regression

### Using linear activation functions in the hidden layers of a multilayer neural network is equivalent to using a single layer. True/False? 

---

DA before ML --> No

---
### Vì sao cần duy trì dữ liệu phi tuyến tính trong quá trình học sâu ?

1. **Xử Lý Mối Quan Hệ Phức Tạp**
+ $ Vì nó giúp mô hình học đc các mqh phức tạp. Cứ tưởng tượng mô hình tuyến tính là 1 đg thẳng có độ phức tạp thấp. Mô hình phi tuyến tính là dữ liệu bao gồm nhiều điểm ko đối xứng nhưng vẫn có các mối quan hệ vs nhau, chẳng hạn như đg cong, mặt phẳng đa thức, etc...
+ ? Ví dụ để phân loại ngữ nghĩa trong ko gian nhiều chiều, ta ko thể phân biệt nhiều từ bằng mô hình tuyến tính, vì mô hình chỉ là 1 đg thẳng. 

+ $ Trong mạng nơ-ron, hàm kích hoạt phi tuyến tính (như ReLU, sigmoid, hoặc tanh) cho phép mỗi lớp thực hiện các phép biến đổi phi tuyến, giúp mô hình học các đặc trưng đa dạng -> tổng quát hóa tốt hơn. 
+ ? **Tổng quát hóa** nghĩa là máy nắm bắt đc **quy luật, mẫu hoặc mối quan hệ cốt lõi**, ngược lại vs **mô hình tuyến tính dự đoán đơn thuần theo 1 quy luật**, vs con người nó là **ghi nhớ đơn thuần.**
+ $ **Tổng quát hóa:** Tập trung vào việc nắm bắt **bản chất** hoặc quy luật ẩn bên dưới dữ liệu, để áp dụng chúng cho những tình huống chưa gặp.
- ? Ví dụ: Dựa trên một vài hình mèo, mô hình học được cách phân biệt mèo với chó thay vì chỉ nhớ các hình cụ thể.

