## [[Continual Learning Survey]]
**Continous Learning -** Learn new information continously without forgetting old information.
**Memory Hiarchy:** Cache or Intermediate Memory (RAG) -> Long Term -> Pernament (Continous Learning).
### [[Continual Learning and Catastrophic Forgetting]]
### [[Mathematical of Continual Learning]]

### [[When Continual Learning is useful]]
[[Continous Learning vs RAG in solving Catastrophic Forgeting]] 
+ ? Why they are not substitutes.
+ $ **Want the model remember new infors directly (ie. update its params)**. *RAG* is just a tool for retrieving new infors, *retrieving too much then we started to have A PROBLEM called hallucination.* Yes, **RAG can be use as a 2nd Brain but there're limitation**.
### [[3 Types of Incremental Learning Survey]]

### [[Continual Learning Code]]


## Idealization
### [[Orthogonal Projection Loss (2021)]]
### [[Tree LoRA]]

### [[Nested Learning - The Illusion of Deep Learning Architecture]]
**Nested Learning -** new ML paradigm (eg. Google HOPE architecture) by structuring models as **nested optimization problems with different update speeds**, *mimicking brain memory* to prevent catestrophic forgetting and build **"living memory" for AI** (*good at Needle in a Haystack* problem). 
	Inspired from the brain's layered memory consolidation (*fast for short-term*, *slow for long-term*)
### [[Continual Learning a Big Topic Survey]]


## Continual Relation Extraction 
### [[Narrow and Interest Topic - Continual Relation Extraction]]
#### [[Few-Shot, No Problem - Descriptive Continual Relation Extraction]]
#### [[Adaptive Prompting for Continual Relation Extraction - A Within-Task Variance Perspective]]
### [[Latent Representation]]


next: https://www.facebook.com/groups/1094847652564195
*Dựa trên các research gaps đã tìm ra* ở tuần trước, nhóm cần:
- *Đề xuất giải pháp/mô hình cụ thể* cho nhánh nghiên cứu của mình.
- *Xây dựng cấu trúc chi tiết* cho phương pháp thực hiện.
- *Hoàn thiện bản Proposal cuối cùng* và thiết kế Slide thuyết trình.

**Research Plan 4: Brainstorming Idea and Implementation.**
![[Pasted image 20260421174720.png | 666]]
- [Link slide:](https://l.facebook.com/l.php?u=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1vv_SQgavmyqVkoqnybkdagr-0vufi1dC%2Fview%3Fusp%3Dsharing%26fbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR53vZNz4d41d5B1bISc7jN1v8-66eSwpe-1tkxREdYl4cV_EUCy8k47No0fgw_aem_g1o-dIByu1dZijvyqDg6eQ&h=AT7smzCXlo6rfS7fs9bV9-HmoOD7uyi3WvgFuG5GxtbuhjYl6QzRNtIHxdmTa-yeqItmOmJ1_cVlW2BRCnK5p360ASg9QVREF-uUcWh3IWOYEmWfbSGTcrU-o2xoMUPjEX2r&__tn__=-UK-R&c[0]=AT4FCgVbYZSp_-76AG_1Q3d2m7N3w65i_Kspi-HNrhVJVDfhiDwhaYw_DFqQeHchWEQ7EhO4oS4xsRBantUpONV7qclm8BrMQr6WELFsEtljXJ98O8JT9R7qR6tywmLG1qwT2RxbnIZT4tIyTkVkfiR1x-N1BR9Z1tQfDXEWjrTRqY6o0d7jEkyLROne7crMqoEBiw_RbqNvsZeKghIu8y6AgZHNRnq_dEo)[https://drive.google.com/.../1vv.../view...](https://drive.google.com/file/d/1vv_SQgavmyqVkoqnybkdagr-0vufi1dC/view?usp=sharing&fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7Lw5GqSON6gGOVEQX7kZOYmrsI4WUiJxKqLzJq_1yS5eD6yX1AE8psshlvsQ_aem_se0VgT60JHymJbJPejwTxQ)  
- [Link record:](https://l.facebook.com/l.php?u=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1M4VlDwwe1qsBHMBs802jQ86uIELeMEgY%2Fview%3Fusp%3Dsharing%26fbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6SsJixMDoADImPkf2Ko9rHnmjz6DEqaX0q8nI7WELfsx_4Ds6Jz_87vBeV-w_aem_BREFZs5PPQBsLSMxET8AXg&h=AT5FDLuhHJt5EpBIQ7qGjHp-SCjjcurcyJSjxa0Cj3TkYiKQsSRH3fvCw_B2YZTPyRC4Or5YH09dGTw1cEPSX2rql2Ga9YWkWjOVAALg90dWwZtkK6sm8Lq-GmotoDhoYS7j&__tn__=-UK-R&c[0]=AT4FCgVbYZSp_-76AG_1Q3d2m7N3w65i_Kspi-HNrhVJVDfhiDwhaYw_DFqQeHchWEQ7EhO4oS4xsRBantUpONV7qclm8BrMQr6WELFsEtljXJ98O8JT9R7qR6tywmLG1qwT2RxbnIZT4tIyTkVkfiR1x-N1BR9Z1tQfDXEWjrTRqY6o0d7jEkyLROne7crMqoEBiw_RbqNvsZeKghIu8y6AgZHNRnq_dEo)[https://drive.google.com/.../1M4VlDwwe1qsBHMBs802.../view...](https://drive.google.com/file/d/1M4VlDwwe1qsBHMBs802jQ86uIELeMEgY/view?usp=sharing&fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5IUrYIqiY9k-6_etPYPs4JUgm1ZDJ9zgSJ4uja5JmMCllYiUKouNg3mTm-Hg_aem_jJcaIgrMYkrnOdiLoAF9fQ)

**Research Plan 5: How to write the Proposed Method section.**
- [Link slide:](https://l.facebook.com/l.php?u=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1Q0vvRy2LLUyejwhmLuV4XVx4qU3h1_n6%2Fview%3Fusp%3Dsharing%26fbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5JFjPYM3gq-4y_Jzl0yfhFaoezN-gi14cmznbE2KSL53zie4n7OECWtOxelg_aem_wQFvWMMkl0sbaFvylTTJbw&h=AT6cpR_o6SnMxvcn8bPAh5x3S3i3o-diGtHiVKdjEfeHkCNd4z8wR95IOX3mFOTHS1qizjpeBmE65JhWgPXWIvc01ZkgErtVvCjjJHTBKvTBvIpkRgIj33GjJ7Vw-Y6Li9V0&__tn__=-UK-R&c[0]=AT4FCgVbYZSp_-76AG_1Q3d2m7N3w65i_Kspi-HNrhVJVDfhiDwhaYw_DFqQeHchWEQ7EhO4oS4xsRBantUpONV7qclm8BrMQr6WELFsEtljXJ98O8JT9R7qR6tywmLG1qwT2RxbnIZT4tIyTkVkfiR1x-N1BR9Z1tQfDXEWjrTRqY6o0d7jEkyLROne7crMqoEBiw_RbqNvsZeKghIu8y6AgZHNRnq_dEo)[https://drive.google.com/.../1Q0vvRy2LLUyejwhmLuV.../view...](https://drive.google.com/file/d/1Q0vvRy2LLUyejwhmLuV4XVx4qU3h1_n6/view?usp=sharing&fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR535IIDCFNR0UTM17-pMEO1LykjYMVi_IZD80G8rLy0qpZiUeYdbOtkKe-zlQ_aem_w8AUueXTBrZYpunY8drHbg)  
- [Link record:](https://l.facebook.com/l.php?u=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1KdZ3LYA7i-qO3OkTLF82-pPodzQQZ42f%2Fview%3Fusp%3Dsharing%26fbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5IUrYIqiY9k-6_etPYPs4JUgm1ZDJ9zgSJ4uja5JmMCllYiUKouNg3mTm-Hg_aem_jJcaIgrMYkrnOdiLoAF9fQ&h=AT6bK-8Pv4rTvSoVJMI5XD8BYuIqO_67_sVOQ2ORp_FNz8vioaHXgXrzDHyJ-jeB9UrUReZAquWkWttJNdt-KfmxSzSpVsYvU08lfPBwhmJZHyJ8yhh9n2GS5cK1dL2HyfNM&__tn__=-UK-R&c[0]=AT4FCgVbYZSp_-76AG_1Q3d2m7N3w65i_Kspi-HNrhVJVDfhiDwhaYw_DFqQeHchWEQ7EhO4oS4xsRBantUpONV7qclm8BrMQr6WELFsEtljXJ98O8JT9R7qR6tywmLG1qwT2RxbnIZT4tIyTkVkfiR1x-N1BR9Z1tQfDXEWjrTRqY6o0d7jEkyLROne7crMqoEBiw_RbqNvsZeKghIu8y6AgZHNRnq_dEo)[https://drive.google.com/.../1KdZ3LYA7i.../view...](https://drive.google.com/file/d/1KdZ3LYA7i-qO3OkTLF82-pPodzQQZ42f/view?usp=sharing&fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExVXlMSGVsVkM5WlN3bG5pY3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR535IIDCFNR0UTM17-pMEO1LykjYMVi_IZD80G8rLy0qpZiUeYdbOtkKe-zlQ_aem_w8AUueXTBrZYpunY8drHbg)

| Method Categories (Rank by Popularity) | Paper Count | Source |
| -------------------------------------- | ----------- | ------ |
| Replay                                 | **74**      | 1      |
| Regularization                         | 28          | 1      |
| Representation                         | **31**      | 1      |
| Optimization                           | 28          | 1      |
| Architecture                           | **36**      | 1      |
|                                        |             |        |

----
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

**Concept Drift:** thích ứng tăng cường với những thay đổi về thuộc tính khuôn mặt của các danh tính đã biết (concept drift) theo thời gian, đảm bảo độ chính xác và độ tin cậy liên tục\\\