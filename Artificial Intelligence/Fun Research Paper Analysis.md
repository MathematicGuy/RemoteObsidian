If you have a super powerful memory , your model can remember and understand the property of your loss function landscape and find a effective solution to that.

associative memory - the ability to map and recall one thing based on another (like recalling a name when you see a face).

We show that the **training process itself,** specifically the [backpropagation](https://en.wikipedia.org/wiki/Backpropagation) process, can be **modeled as an associative memory**

---
## Deepfake Survey
### Hướng nghiên cứu tóm tắt: 
**Vision encoder “thông thường” học gì?**

Vision encoder dùng cho phân loại/nhận diện/VQA kiểu phổ biến chủ yếu học ngữ nghĩa:
Đây là ai / cái gì (khuôn mặt, xe, biển báo…)
Đang làm gì / ở đâu (hành động, bối cảnh)
Những đặc trưng giúp “hiểu nội dung” và ổn định trước nhiễu (nén nhẹ, mờ nhẹ, đổi sáng…)

Vì mục tiêu là hiểu nội dung, nó thường bỏ qua (hoặc làm yếu đi) các chi tiết rất nhỏ như **hạt nhiễu, dấu vết nén, “vân” nội suy… vì các thứ đó hay bị xem là nhiễu không quan trọng.**

**Vision encoder “forensic” học gì?**
Encoder forensic thì ngược lại: nó học để nhận ra độ tự nhiên của ảnh (ảnh có được tạo ra/đi qua xử lý gì bất thường không), nên nó ưu tiên các tín hiệu kiểu:

**Kết cấu bề mặt:** da thật thường có vi cấu trúc không đều; *ảnh giả hay bị “mịn đều”, hoặc có vân lặp/nhựa.*

**Tính liên tục không gian:** ảnh *thật có chuyển tiếp tự nhiên giữa vùng-vùng;* ảnh giả hay có chỗ “khớp” không trơn (viền tóc, rìa mặt, vùng miệng…).

**Dấu vết xử lý ảnh:** **nội suy** khi *phóng/thu, làm mịn, ghép vùng, nén lại nhiều lần*… để lại *dấu vết rất nhỏ nhưng có quy luật.* 

**Nói gọn:**
Encoder thường trả lời “ảnh nói về cái gì”, còn **encoder forensic trả lời “ảnh được tạo ra như thế nào, có tự nhiên không”.**

**-->** **Làm sao con vision encoder LLM có thể encoder forensic.** 
**-->** **Giả thuyết:** ngta bảo cái ảnh fake/vùng fake nó có miền tần số cao hơn ảnh thật. Kiểu vẫn mask như cũ, nhưng với frequency chứ k chỉ mỗi ảnh pixel. Dùng phương pháp này để con vision encoder nhìn forensic hơn là chỉ là object
**--> Thì contribution là** sau cái đó là zero shot training dùng cho nhiều ảnh fake detection khác mà k cần train lại và **phát hiện fake từ bản chất hình ảnh** chứ không phải chỉ vật trong ảnh
![[Pasted image 20251217022829.png]]
**Các nguyên nhân chính gây ra "tần số cao bất thường" này:**
Lỗi của mô hình AI (Artifacts): Các mô hình tạo ảnh (như GANs đời cũ) thường tạo ra các "lưới ô bàn cờ" (checkerboard artifacts) siêu nhỏ do cách chúng phóng to ảnh. Những lưới này là các cạnh sắc nét lặp đi lặp lại -> Tín hiệu tần số cao nhân tạo.

Đường ghép không hoàn hảo: Khi ghép một khuôn mặt fake vào một cơ thể thật (deepfake), đường ranh giới dù được làm mờ nhưng ở cấp độ pixel, nó vẫn tạo ra một sự thay đổi đột ngột về đặc tính ảnh so với vùng xung quanh -> Tín hiệu tần số cao tại đường viền.

Sự không nhất quán về nhiễu (Noise inconsistency): Ảnh chụp bằng camera thật luôn có một lớp hạt nhiễu tự nhiên (sensor noise) đồng nhất. Vùng ảnh fake được AI tạo ra thường quá "phẳng" và trơn láng, sau đó người ta cố thêm nhiễu giả vào cho giống thật, nhưng lớp nhiễu giả này không khớp với nhiễu thật của phần còn lại -> Tạo ra sự chênh lệch tần số cao.



**Difficulty Survey**




---

**Mediapipe + Feature Engineer + LSTM approach for Action Recognition Problem** 
