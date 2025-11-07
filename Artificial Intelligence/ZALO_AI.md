[[How to Review a Paper]]
[[RAG Ultimate]]
[[Prompt Engineering]]
[[fine-tuning]]
[NVIDIA City Challange](https://github.com/NVIDIAAICITYCHALLENGE/2024AICITY_Code_From_Top_Teams/tree/main?tab=readme-ov-file)

----

Zoom lên có thể mất thông tin -> upscale image (but increase run time) 
Data Imbalance -> Focal Loss
Thống kê - Small Object
Biểu đồ thống kê chiều cao, rộng và diện tích (ratio của hìnhD) cho Object
Chia Patch (scale ảnh rồi chia 1 ảnh thành 4 ảnh để xử lý lần lượt)
Data Augmentation bằng cách lấy background tương tự dữ liệu rồi gán object vào -> Thật đối với bot là đc, không phải đối vs người. 

Thống kê + Tổng hợp thông tin -> Perplexity. 
Không nên dùng từ YOLOv9 trở xuống vì nó có NSM (chậm):
+ 2 For, tính toán sử dụng GPU -> inference chậm.
+ Nên tìm những mô hình mà họ nén phần NMS vào lớp Attention. 
Nên dùng kĩ thuật Essemble. 
![[Pasted image 20251102210005.png# left]]

---

5 x 1.5B -> Essemble. 
Syncthetics Data -> Gọi VLM API xịn để generate. 

**Các Questin trong Dataset.**
**50 - 60%:** Fine-tune Baseline.
**60-70%:** Augmentation + Essemble.
**80-90%:** Engineering Skill. 
**10%:** ko giải đc
Note: test grouth để Cheat. :)) Xem sai câu nào nhờ test. 

Note: 
Cứ setup 1 pipeline hoàn thiện tr'c. (Thành làm nốt RAG)
Chị Linh tiếp tục theo hướng Fine-Tune. 

Chị Hà + Phương -> Nghiên cứu ý tưởng các paper khác. 
Còn lại nghiên cứu hướng các bài đã có và thử nghiệm trước. 
Prompt là ra dc ảnh ???

Note: **Để vào conference họ quan tâm đến Idea. :)) ko nhất thiết pải tốt nhất**

**Ôn: Agent Design pattern** - RAG là 1 trong số đó. Reasoning Pattern. 

Các hệ thống đi theo con đường Data Science. rất nhiều.
 ML đóng vai trò là 1 Design Pattern và để học cách xử lý dữ liệu.

Keyword: `Prompt to report`, `Prompt to Data Analysis`.
Tập trung vào vấn đề Lặp Lại Nhiều -> đẩy Agent, AI vào. 
agno - agent flow like langgraph. 
Sự khác biệt giữa OpenModel và LocalModel. 
ReACT ko chạy các setup `<think></think>` -> phải code lại -> nhưng nếu sai thì cả hệ thống đi hết. 

Học A2A (Agent2Agent)
Tập trung vào Nghiên cứu, setup có thể dùng Tools. 



