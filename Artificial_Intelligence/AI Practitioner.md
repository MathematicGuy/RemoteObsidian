### Day02-AI-Product-Labs
01/ top 3 Problem Cards, draft workflow trước/sau.
02/ Nhóm 3-4 người làm một bản nhật ký, kiểm chứng/research, Problem Statement, Rule / Workflow / Agent, quyết định cuối, workflow trước/sau -> copy bản nhóm vô repo cá nhân của mình. 
03/ eflection cá nhân về AI, vai trò trong nhóm, và bài học sau lab.

?????
```
Nếu có file phụ như ảnh workflow, Mermaid, survey screenshot, research notes, đặt cùng prefix với phần liên quan:

01-individual-problem-scan-workflow-card-1.png
02-group-problem-statement-workflow.pdf
02-group-problem-statement-research-notes.md
```

What keep the users: UI/UX, Handles Errors (reliability).
[[Business_Analyst4AI_Product_Rule_Book]]

**References**
+ 02-deliverable-example.md -> *what a good report look like*
----
Note: Đi từ Bài Toán -> Metrics. 

Chatbot báo cáo từ trong cty.
	**CỤ THỂ** - cần gì, báo cáo ntn, báo cáo từng ban. Báo 
	**What you see ?** Dashboard báo cáo có gì (*Xác định chỉ mục cần báo cáo*: Nếu chỉ có thể xem 5 thông tin thì sếp ưu tiên xem thông tin gì nhất) 
	**Lịch báo cáo:** Hằng Chiều (thời gian lúc nào, hàng ngày, hàng giờ hay có tin mới báo cáo luon)
	Quan trọng là ai chịu **Responsibility:** ai chịu trách nghiệm (GuardRail/AI_Judge, You), Chatbot uy tín hay không ? *(GuardRail)* 


Identify the Right Problem (Scope down) -> Right Solution (Scope Down)
**Problem First, not AI First** *- First Principle Thinking* 
	*Original Question:* *Bot check Gmail xin nghỉ cho sếp* 
	OpenCraw thu mail xin nghỉ từ các app mail (Email, Slack, Zalo) 
	Intent Classifier Chatbot (SLM) -> Xác định độ tự tin cho tin nhắn. 
	-> Hiểu ý nhân viên và viết thư cảm thông cho phép xin nghỉ. 
	-> Check điều kiện xin nghỉ có hợp lý hay *không*
	->  Tóm tắt thông tin xin nghỉ.
	.
	Với nhân viên
	+ Quan trọng với dự án hiện tại: Đề xuất mẫu phản hồi, Con người tự Duyệt.
	+ Không trong dự án hiện tại: Tự động
	.
	*Điểm đau:* phải check email xin nghỉ khi thế giới có sự kiện lớn (như world cup) và tóm tắt thông tin để ra quyết định -> Tiết kiệm thời gian cho phép.
	Sản phẩm rẻ, không tốn nhiều kinh phí. Chỉ mất tiền khi dùng. 
+ ! AI có cần thiết không. 

**Question to ask your Stakeholder**
![[Pasted image 20260529105645.png]]
What Not POC - really integrated in customer workflow ?

---
Anti-Gravity (Thiết kế đơn giản nhưng nhiều feature) - Feature Ẩn trong hệ thống. Kích hoạt nhờ Prompt. e.g. như sub-agent. 
ChatGPT Deep Research - cho phép người dùng tinh chỉnh từ miles stone trong kế hoạch.  

3 Giải pháp để giải quyết bài toán trong Sản Phẩm. Rulebase, LLM.

**Vấn đề:** Quá tải tin nhắn -> Hệ thống tự Re-Ranking độ quan trọng của tin nhắn trên Discord. 
Độ quan trọng = Người Nhắn (Gia đình, Làm cùg dự án) + Nội dung Tin Nhắn (có người Mất, Nd mình Quan Tâm nhiều).

**Rule-Base:**
Chia làm 2 Khung Chat:
1) Những User mình luon tự đọc tin nhắn
2) User ít quen biết, người lạ hoặc không quá quan trọng. 

**AI Agent**
+ ! **Compound Errors effect:** the more steps the AI Agent take, it only need 1 errors to occur for the compound effect to accumulate.e.. 1 steps 95% acc, 10 steps 60% acc and 1 step acc will be only 0.6%. 
+ $ Like human, AI need tools to perform well on given tasks like use Calculator to calc for higher speed and accuracy rather than tell the model to calc 199,999 divided by 292 raw. Be resourceful.

----
![[Pasted image 20260529210054.png]]

![[Pasted image 20260529210651.png]]

![[Pasted image 20260529210741.png]]

![[Pasted image 20260529210750.png]]

![[Pasted image 20260529210846.png]]

![[Pasted image 20260529210859.png]]

![[Pasted image 20260529210913.png]]

![[Pasted image 20260529210927.png]]

![[Pasted image 20260529211027.png]]

![[Pasted image 20260529211040.png]]

![[Pasted image 20260529211052.png]]

![[Pasted image 20260529211130.png]]

![[Pasted image 20260529211140.png]]

![[Pasted image 20260529211155.png]]

![[Pasted image 20260529211209.png]]

![[Pasted image 20260529211523.png]]

