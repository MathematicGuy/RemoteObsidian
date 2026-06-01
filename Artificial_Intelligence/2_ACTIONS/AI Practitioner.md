---
category: "2_ACTIONS/AI Practitioner.md"
summary: "### Day02-AI-Product-Labs
01/ top 3 Problem Cards, draft workflow trước/sau. 02/ Nhóm 3-4 người làm một bản nhật ký, kiểm chứng/research, Problem Statement, Rule / Workflow / Agent, quyết định cuối..."
keywords: []
confidence: "high"
analyzed_at: "2026-06-01T02:22:41.023571+00:00"
---
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

----
![[Pasted image 20260529210054.png]]

----
### Hand-Selected Most Potential Projects
-> *AI Trợ Lý Phát Hiện Sớm Khó Khăn Học Tập Của Học Sinh* - (Personal AI Assistant for Early Diagnosed Student Learning Struggles) - Mindset: dev the MVP then scale up to Adaptive AI (AI Gia Sư Cá Nhân Hóa Theo Năng Lực Từng Sinh Viên) to Suggest and Create relavent contents to help student catch up with progress.    


|                                    Name                                     |                  Domain                  | Technical Skills |                                                                                                                                                                                                                                                                                                   Problem Description                                                                                                                                                                                                                                                                                                    |                    Tech Stack (định hướng)                     |                                                                                                            MVP Requirements                                                                                                            |
| :-------------------------------------------------------------------------: | :--------------------------------------: | :--------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    **AI20K-066: AI Trợ Lý Phát Hiện Sớm Khó Khăn Học Tập Của Học Sinh**     |   K-12 Education — Early Intervention    |     ML + LLM     |                            Học sinh gặp khó khăn học tập (chậm tiến bộ, lỗ hổng kiến thức) thường được phát hiện muộn khi đã tụt lại xa, khó bắt kịp. Bài toán: AI phát hiện sớm khó khăn học tập: phân tích kết quả và quá trình học tập để nhận diện học sinh có dấu hiệu gặp khó hoặc lỗ hổng kiến thức cụ thể, giải thích vấn đề và gợi ý hướng hỗ trợ cho giáo viên, đề xuất tài liệu/bài tập bổ trợ phù hợp, theo dõi hiệu quả can thiệp. Có guardrail bảo mật dữ liệu trẻ em và dùng để hỗ trợ chứ không gán nhãn. Giúp giáo viên can thiệp kịp thời để không học sinh nào bị bỏ lại.                             |   ML (learning analytics), OpenAI/Claude, FastAPI, dashboard   | Yêu cầu tối thiểu: sản phẩm web/app hoàn chỉnh — deployed online (có URL truy cập), đăng nhập & phân quyền cơ bản, giao diện UI/UX hoàn chỉnh, quản lý user. Không chấp nhận: demo notebook, script CLI, prototype chỉ chạy localhost. |
| AI20K-039: AI Trích Xuất & Tổng Hợp Dữ Liệu Có Cấu Trúc Từ Bài Báo Khoa Học |        Research — Data Extraction        |    NLP + LLM     | Tổng hợp hệ thống (systematic review, meta-analysis) đòi hỏi trích xuất dữ liệu có cấu trúc (kết quả, tham số, phương pháp) từ hàng trăm bài báo — làm thủ công cực kỳ tốn công và dễ sai sót. Bài toán: AI trích xuất dữ liệu nghiên cứu: từ tập bài báo, trích xuất các trường dữ liệu theo mẫu do nhà nghiên cứu định nghĩa (cỡ mẫu, phương pháp, kết quả định lượng...), chuẩn hóa vào bảng có cấu trúc, đánh dấu nguồn để kiểm chứng, phát hiện dữ liệu thiếu/mâu thuẫn. Có guardrail yêu cầu con người kiểm chứng dữ liệu trích xuất. Tăng tốc tổng hợp hệ thống và meta-analysis với độ chính xác kiểm soát được. | OpenAI/Claude, NLP (extraction), PDF parsing, FastAPI, web app | Yêu cầu tối thiểu: sản phẩm web/app hoàn chỉnh — deployed online (có URL truy cập), đăng nhập & phân quyền cơ bản, giao diện UI/UX hoàn chỉnh, quản lý user. Không chấp nhận: demo notebook, script CLI, prototype chỉ chạy localhost. |
|        AI20K-001: AI Gia Sư Cá Nhân Hóa Theo Năng Lực Từng Sinh Viên        | Higher Education — Personalized Tutoring |    LLM + RAG     |                            Giảng viên đại học không thể kèm cặp từng sinh viên trong lớp đông, nên sinh viên yếu bị bỏ lại còn sinh viên giỏi không được thử thách đủ, dẫn đến chênh lệch kết quả học tập. Bài toán: AI gia sư cá nhân hóa: dựa trên tài liệu môn học chính thức, giải đáp thắc mắc theo trình độ từng sinh viên, hướng dẫn từng bước (Socratic, không cho đáp án ngay) để rèn tư duy, tạo bài tập luyện tập theo điểm yếu, theo dõi tiến bộ. Có guardrail chống gian lận (không làm hộ bài kiểm tra). Hỗ trợ học tập cá nhân hóa ở quy mô lớn, thu hẹp khoảng cách năng lực.                            |    OpenAI/Claude, RAG (tài liệu môn học), FastAPI, web app     | Yêu cầu tối thiểu: sản phẩm web/app hoàn chỉnh — deployed online (có URL truy cập), đăng nhập & phân quyền cơ bản, giao diện UI/UX hoàn chỉnh, quản lý user. Không chấp nhận: demo notebook, script CLI, prototype chỉ chạy localhost. |
-> Thay đổi góc nhìn: hệ thống cá nhân hóa phải bắt đầu từ vấn đề cá nhân -> Vì AI không thể dự đoán 1 vấn đề cá nhân được. Vấn đề phải thực tế, đã xảy ra rồi mới bắt đầu dự đoán. 

### Vin AI Practitioner - Timeline
![[Pasted image 20260530115153.png | 999]]
![[Pasted image 20260530115207.png | 999]]
![[Pasted image 20260530152634.png | 999]]
![[Pasted image 20260530115221.png | 999]]

----

### AI Application Usecase
**Google Photos** - team though AI for Photo filter is better but actually NO bc rule-based is already enough. 
-> Non-AI Baseline (not everything need to use AI)

**Stripe AI** - weekly summery bot -> reduce 60% report writing time, 70% adoptation after 3 months. 
-> AI is Boost, Not Replace 

**Github Copilot** - AI suggestion UX, use ghost pattern (inline suggestion) and user accept/reject each suggestion.
-> AI suggest, human decide

**-> Human First, Not AI First Design** 

reference:
+ [building LLM for production](https://huyenchip.com/2023/04/11/llm-engineering.html#prompting_vs_finetuning_vs_alternatives)

## Building AI Product
+ ! Luôn đảm bảo mình đang giải quyết VẤN ĐỀ THẬT - CÓ QUAN TRỌNG KO - NGƯỜI ĐAU có QUAN TRỌNG không ? 
	Và PAIN POINT có EVALUATION METRIC như thế nào ? 

### 1. Customer Journey Map
![[Pasted image 20260531195343.png]]
	**Zone A:** The lens provides constraints for the map by assigning **(1)** a persona (“who”) and **(2)** the scenario to be examined (“what”).
	**Zone B:** The heart of the map is the visualized experience, usually aligned across **(3)** chunkable phases of the journey. The **(4)** actions, **(5)** thoughts, and **(6)** emotional experience of the user has throughout the journey can be supplemented with quotes or videos from research.
	**Zone C:** The output should vary based on the business goal the map supports, but it could describe the insights and pain points discovered, and the **(7)** opportunities to focus on going forward, as well as **(8)** internal ownership.

giải pháp hiện có là gì, problem statement của nó là gì. 

+ @ Vấn đề không phải triệt chứng
![[Pasted image 20260531203542.png | 555]]

Từ 1 Problem -> **Problem Statement CỤ THỂ (WHAT)** -> **AI tạo GIÁ TRỊ ở đâu (WHERE)**  
![[Pasted image 20260531203441.png | 555]]

Phân tích VẤN ĐỀ gốc, không phải triệu chứng "lười" bên ngoài. 
![[Pasted image 20260531204733.png | 555]]

+ @ Trong 4 tuần, thì bạn sẽ bỏ những FEATURES nào, LẤY top 3 FEATURE nào. 

Trong Custom Journey RoadMap -> AI nên đặt ở đâu. 
![[Pasted image 20260531210059.png | 555]]


![[Pasted image 20260531212033.png | 888]]

![[Pasted image 20260531212156.png | 888]]

Đừng hỏi tôi sẽ build những Feature AI nào -> *Hãy hỏi trong 14 ngày tiếp theo, tôi sẽ giải quyết được những nỗi đau nào.* 
