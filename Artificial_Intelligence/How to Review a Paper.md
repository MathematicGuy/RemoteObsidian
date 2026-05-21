
---
Dùng Extention ExCITATION để lọc research paper (né Frontier, NVDI vì nó phức tạp). 
![[Pasted image 20251101232235.png# left ]]
Mấy bài nhiều citation thì vô đọc. vì ít citation nghĩa là tính áp dụng thấp. 

Newbie làm research thường mang tâm lý hiểu muốn hết sau hết module. Nếu dành nhiều thgian đọc đúng bài đó thì sẽ bị stuck vô bài đó. -> **Nên nắm concept chung (cho method thoi)**, có thể **hiểu Method cua Model như 1 blackbox.** **Vì AIO sẽ dạy hết mấy cái đó nên có thể học sau.** 
-> Hiện tại **tập trung vào hiểu vấn đề.** 

**Tư duy hệ thống:** đọc model nền tảng rồi xem nó có MNIST, CNET thì mik ko cần quan tâm nó phát triển ntn. Tập trung hiểu **INPUT/OUTPUT, nó dùng Dataset gì.** 
-> Tập trung vào **Đọc Rộng** chứ **chưa cần Hiểu Sâu**.
-> **Mô hình cải thiện phần nào của con Base trên dataset nào.** (đọc model Base rồi đọc lên)
Học lên cao học sẽ dạy sau e.g. PhD, Master. 

Tramsfromer - LSTM with Attention, RNN -> 
Mấy bài vướng **original paper** - thấy mấy **hướng đi của nó fancy** quá nên đi từ đó, tuy nhiên chỉ thấy hay nhưng không hiểu nền móng của paper đó sẽ ko thực sự hiểu đc vấn đề mà nó giải quyết -> Bị Stuck vì mất nền tảng, do chưa hiểu vấn đề gốc gác mà nó giải quyết. 

Tập liệt kê và đặt câu hỏi (model hiện tại) có các biến thể gì ? -> **Base trên cái gì (dựa trên cái gì)**
**e.g. Linear Regressin -> Logistic Regression -> Neural network -> CNN (mỗi model sau đều giải quyết 1 hoặc nhiều vấn đề của model tr'c)** -> RNN, LSTM ....

-> Lý do nên **học các model gốc vì nó cho mình thấy vấn đề gốc gác** và mang **lại lợi ích lâu dài vì** có thể dùng nó để phát triển lên. e.g. cần hỉểu ResNet hay CNN là gì thế. (**STUCK**)

Nếu paper đc Q1 mà ít citation -> ít giá trị vì chưa giải quyết đc nhiều vde hiện tại. 

Có 2 kiểu paper:
- Summarize  
- Đưa ra phương pháp mới (original paper)  

Trong paper phần qtrog nhất là đoạn cuối Introduction: 
-> Hiểu đc cái Motivation và hiểu đc vấn đề chính mà tác giả giải quyết.

Trừ khi nộp vào hội nghị lướn như NeuRips thì ms cần tập trung sâu vào toán.
- Khi làm Engineering để ra Paper thì mới cần đọc toán để phản biện. Incremental Method (build on top method của người ta)
- Engineering Cty hay Research Application -> hiểu Input/Output vs Experiement Result thoi. -> Tìm bài Game Changer thoi.

Đ**ể World Class** cần phải tự nghĩ, giải quyết vấn đề từ gốc và phản biện. Chứ không kéo code hay xào code của ng khác. -> **Phải đào sâu gốc rễ vấn đề.** 
AI Research discuss tại sao người ta làm như vậy. 

Thực nghiệm -> đọc experiment result. 

**Tìm bài gần vs mục tiêu ->** Nhìn vào Dataset của paper đó xem có cùng bộ dataset với mình hay không. Giống vs dataset mình cần hay không. 
Thuật toán fancy nhưng ko có code -> SKIP luon. 
Người ta hỏi metric đánh giá chứ ko hẳn tập trung hỏi thuật toán. 

