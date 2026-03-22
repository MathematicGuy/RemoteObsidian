## [[Continous Learning Research Plan Board]]

## [[Continual Learning Survey]]
**Continous Learning -** Learn new information continously without forgetting old information.
**Memory Hiarchy:** Cache or Intermediate Memory (RAG) -> Long Term -> Pernament (Continous Learning).
### [[Continous Learning and Catastrophic Forgetting]]
### [[Mathematical of Continual Learning]]

### [[When Continual Learning is useful]]
[[Continous Learning vs RAG in solving Catastrophic Forgeting]] 
+ ? Why they are not substitutes.
+ $ **Want the model remember new infors directly (ie. update its params)**. *RAG* is just a tool for retrieving new infors, *retrieving too much then we started to have A PROBLEM called hallucination.* Yes, **RAG can be use as a 2nd Brain but there're limitation**.
### [[Class Incremental Learning Survey]]

### [[Continual Learning Code]]


## Idealization

### [[Orthogonal Projection Loss (2021)]]
### [[Tree LoRA]]

### [[Nested Learning - The Illusion of Deep Learning Architecture]]
**Nested Learning -** new ML paradigm (eg. Google HOPE architecture) by structuring models as **nested optimization problems with different update speeds**, *mimicking brain memory* to prevent catestrophic forgetting and build **"living memory" for AI** (*good at Needle in a Haystack* problem). 
	Inspired from the brain's layered memory consolidation (*fast for short-term*, *slow for long-term*)
![[Pasted image 20251223091039.png]]
	**All NN are associative memory system** that compress their own context flow. 
	**Gradient Descent with momemtum** is indeed a **low-level optimization process**, where the memory is optimized by simple gradient descent algorithm. 

### Continual Relation Extraction
#### [[Few-Shot, No Problem - Descriptive Continual Relation Extraction]]
### [[Adaptive Prompting for Continual Relation Extraction - A Within-Task Variance Perspective]]


### A Comprehensive Survey of Continual Learning Theory Method Application

| Method Categories (Rank by Popularity) | Paper Count | Source |
| -------------------------------------- | ----------- | ------ |
| Replay                                 | 74          | 1      |
| Regularization                         | 28          | 1      |
| Representation                         | 31          | 1      |
| Optimization                           | 28          | 1      |
| Architecture                           | 36          | 1      |


----
**Note:** 
+ **Continual Learning Library:** Avalance vs LibContinual, when to use which.
+ Research Direction Survey proposal  
+ Team work proposal
+ Top Researcher on Continual Learning and Future Research direction for LLM
+  [Kullback-Leibler (KL) divergence](https://www.geeksforgeeks.org/machine-learning/kullback-leibler-divergence/) can be used to test Distribution shift, 
+ Why LoRA is so efficient for CL

### [[Introduction and Motivation for Continual Learning]]

**Why Continual Learning in Facial Recognition Model ?**
You need a model to Embed new face so you could search that face on the Database ->  

1 Papers cần có ít nhất 3 cải tiến.
e.g. Distillation + LoRA is 1 improve, Evaluation process is 1 improvement -> 2 improvement
Consideration - Recruiting team member for research 1-2 peoples. (Hỏi cô Trang xem có bạn hay nhóm nào mình có thể Join cùng hay không ?)

**Research Question:** Phát triển 1 LLM có khả năng nhớ thông tin mới mà không cần Retrainning và không quên kiến thức cũ (vì weights thay đổi khi cập nhật và finetune). 
	Note:
	+ Có thể kết hợp Continual Learning LLM với RAG. 
	+ LLM thông thường khi finetune sẽ quên đi 1 phần kiến thức gốc, Continual LLM sẽ nhớ cả 2. 
	+ Ít bị ảnh hưởng bới Bias và Concept Drift, Domain Drift. 

**Research Purpose:** 
+ *Label-free supervision model* -  giúp hệ thống nhận diện khuôn mặt mới mà không cần huấn luyện lại từ đầu. 

**The Necessity of / Why Continual Learning ?** 
+ *Privacy Concern* -> Retrieved data go straight into trainning without saving to the database. 
+ *Improve LLM Context Windows* -> because RAG help but not prevent Context Windows Overflow. 
+ *Concept Drift* -> Dữ liệu mới thay đổi Phân Phối dữ liệu (Data Distribution) của LLM dẫn tới Accuracy giảm. Continual Learning LLM giảm thiểu tối đa ảnh hưởng của Concept Drift.  
	-> Giảm thiểu ảnh hưởng của Bias, Distribution trong Dữ Liệu hơn. e.g. Nhận diện khuôn mặt của 1 người trong nhiều điều kiện ánh sáng tốt hơn (Domain Adaptation).

**Research Questions**
+ Mô hình không được lưu trữ dữ liệu để học lại, yêu cầu học đến đâu Train đến đó. 
+ Làm sao để thiết kế 1 mô hình chỉ học những thông tin cần thiết. 
+ Cách tiếp cận cho bài toán Catastrophic Forgetting - "Học kiến thức mới mà không quên kiến thức cũ" 
	-> Chỉ học những kiến thức quan trọng, ie. key information có Entropy cao mà không học nhầm phải Noise (ý tưởng của Anchor, mô hình Titan của Google) 
	-> Replay giúp mô hình ôn lại kiến thức cũ
	-> LoRA ...
	-> Architecture ...
	-> Regularization ...
	-> Orthogonal ...
	-> Nested Learning


Want to know more about - **"Real life Application for Continual Learning"**

**Key Characteristic in Continual Learning Model**
+ Model in Continual Learning save knowledge into their Weight (internal memory) while RAG save knowledge into its database. 
+ Continual Learning not just about 1 model, it could be expand into a system that can learn/fine-tune continuously. ![[Pasted image 20260312180513.png]]

**Nhược điểm của Continual Learning:**
+ Prone to Weight Injection and Prompt Injection (Need Continual Unlearning for this)
-> Need method to improve Model (weights) Resilient.
+ Ability to Unlearn unnecessary data.

---

### Framework for CLFace
**Lifelong Face Recognition trong hệ thống nhận dạng sinh trắc học:** liên tục học các đợt danh tính mới mà không được phép lưu trữ exemplars vì vấn đề Quyền Riêng Tư.

**Vấn đề giới hạn bộ nhớ (Memory Constraints):** mở rộng liên tục lớp phân lại (FC layer) cho hàng ngàn danh tính mới mỗi ngày sẽ làm cạn kiệt bộ nhớ và tài nguyên tính toán, do đó yêu cầu một kiến trúc không có lớp phân loại (classification-free architecture).

**Concept Drift:** thích ứng tăng cường với những thay đổi về thuộc tính khuôn mặt của các danh tính đã biết (concept drift) theo thời gian, đảm bảo độ chính xác và độ tin cậy liên tục