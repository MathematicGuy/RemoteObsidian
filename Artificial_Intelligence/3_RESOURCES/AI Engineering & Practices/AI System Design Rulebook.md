---
category: "3_RESOURCES/AI Engineering & Practices/AI System Design Rulebook.md"
summary: "Dưới đây là **outline + header cho Guide Book** theo đúng mục tiêu của bạn: luyện tư duy nhanh để thiết kế 5 hệ thống RAG trong exam context. # Guide Book: Thiết Kế MVP AI System Với RAG Trong Exam..."
keywords: []
confidence: "high"
analyzed_at: "2026-06-01T02:22:41.025780+00:00"
---

Dưới đây là **outline + header cho Guide Book** theo đúng mục tiêu của bạn: luyện tư duy nhanh để thiết kế 5 hệ thống RAG trong exam context.

# Guide Book: Thiết Kế MVP AI System Với RAG Trong Exam Context

## 0. Overview

Guide này giúp Fresher AI Engineer thiết kế nhanh MVP AI System dùng RAG trong bối cảnh bài thi. Mục tiêu không phải học toàn bộ RAG theory, mà là luyện khả năng:
```text
Business Question -> AI Engineering Problem -> RAG Design -> Workflow -> Implementation Plan
```
Trong exam, bạn cần trả lời nhanh, rõ, có cấu trúc, và thể hiện được tradeoff giữa **quality, cost, latency, risk, implementation complexity**.

---

## 1. Understand The 5 Questions And Their Domain

### 1.1 Exam Context
- Tổng thời gian: 120 phút.
- Tổng số câu: 10 câu.
- 5 câu RAG + 5 câu AI Agent.
- Mục tiêu cho 5 câu RAG: khoảng 30-45 phút.
- Thời gian mỗi câu RAG: khoảng 6-9 phút.
- Chiến lược: dùng 1 answer format cố định, sau đó customize theo domain/use case.

### 1.2 Characteristics Of Each RAG Question

| Question | Domain                 | Main Task                                                 | Main Data                                                               | Main Risk                                                           | Likely RAG Type                            |
| -------- | ---------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| Q1       | Giáo dục               | Sinh câu hỏi trắc nghiệm                                  | PDF, table, graph image, formula, đề thi cũ                             | Câu hỏi/distractor kém chất lượng                                   | Multimodal Fusion RAG                      |
| Q2       | Y tế                   | Hỗ trợ tra cứu/chẩn đoán/phác đồ                          | Bệnh án, lab table, image, clinical notes, guideline                    | Sai y khoa, bảo mật, thiếu citation                                 | On-prem Multimodal Graph + Corrective RAG  |
| Q3       | Pháp lý                | Rà soát tuân thủ và phân tích rủi ro hợp đồng             | Hợp đồng dài, bộ luật, quy tắc nội bộ, hợp đồng cũ, bảng điều khoản mẫu | Bỏ sót rủi ro pháp lý, trích luật sai, lộ bí mật kinh doanh         | On-prem Rule-based Graph/Hybrid RAG        |
| Q4       | Tuyển dụng             | Phân tích, xếp hạng và giải thích độ phù hợp của ứng viên | CV PDF, ảnh chụp, text thô, bảng kỹ năng, JD, tiêu chuẩn chuyên môn     | Bỏ sót ứng viên tốt, bias, parse sai CV, giải thích thiếu minh bạch | Multimodal Hybrid RAG + Ranking Pipeline   |
| Q5       | Doanh nghiệp Công nghệ | Tra cứu và tổng hợp tri thức nội bộ                       | Wiki, SOP, Slack threads, hướng dẫn kỹ thuật, metadata quyền truy cập   | Trả lời sai ngữ cảnh, lộ thông tin nhạy cảm, dữ liệu lỗi thời       | Permission-aware Fusion/Conversational RAG |

## 2. Brainstorming Framework When Designing AI System

### 2.1 The 6 Fast Questions
Khi đọc đề, luôn hỏi:
```text
1. User là ai?
2. Output cần tạo là gì?
3. Data input là gì?
4. Constraint lớn nhất là gì?
5. Risk lớn nhất là gì?
6. Standard RAG sẽ fail ở đâu, cần upgrade thành RAG type nào?
```

### 2.2 Translate Business Requirement -> AI Engineering Translation
**Ví dụ:**

| Business Signal             | Translate Into AI Engineering                          |
| --------------------------- | ------------------------------------------------------ |
| “Dữ liệu đa dạng”           | Multimodal parsing + Fusion RAG                        |
| “Không được sai”            | Corrective RAG + verification + citation               |
| “Bảo mật, không rời nội bộ” | On-prem deployment + local vector DB                   |
| “Cần đúng văn phong”        | Historical example retrieval / style retrieval         |
| “Nhiều quan hệ phức tạp”    | Graph RAG                                              |
| “Ngân sách thấp”            | API/small model/cache, avoid fine-tuning/self-host GPU |
| “Chấp nhận chậm vài phút”   | Add reranking, verification, multi-step retrieval      |
| “Chat nhiều lượt”           | Conversational RAG                                     |
| “Nhiều nguồn dữ liệu”       | Fusion RAG                                             |


## 3. Answer Format And Exam Strategy
### 3.1 Revised Answer Format
```markdown
**Solution:**  
[Thiết kế hệ thống ngắn gọn] - giải quyết [vấn đề chính]. Chọn [RAG type] vì [lý do chính].

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| Vấn đề 1 | Giải pháp 1 | Tiêu chí đánh giá | Vì sao giải pháp này có giá trị |
| Vấn đề 2 | Giải pháp 2 | Tiêu chí đánh giá | Vì sao phù hợp business |
| Vấn đề N | Giải pháp N | Tiêu chí đánh giá | Vì sao chọn giải pháp này |

**Abstract Workflow:**  
Step 1 -> Step 2 -> Step 3 -> Step N

**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP |
|---|---|---|
| 1. Step name | Mục tiêu | Cách triển khai |
| 2. Step name | Mục tiêu | Cách triển khai |

**MVP Scope and Tradeoffs:**  
Ưu tiên [must-have]. Tạm hoãn [nice-to-have]. Tradeoff chính là [quality vs cost/latency/complexity/scope].
```

### 3.2 Time Strategy
Cho mỗi câu RAG:
1 phút: gạch keyword
1 phút: chọn RAG type
2 phút: điền Analyze Business Question
2 phút: viết workflow
2 phút: viết implementation steps
1 phút: viết MVP scope/tradeoff

---

# 4. Brainstorming And Answer Practice

## Before 4.1: Warm-up Check
**Trước khi làm Practice Question 1, bạn cần biết (Dùng Tài Liệu của AIO:):**
1. RAG là gì?
2. Basic RAG workflow gồm những component nào?
3. Input và output của từng component là gì?
4. Standard RAG thường fail ở đâu? 
**Search Internet:**
5. Khi nào cần Fusion RAG, Graph RAG, Corrective RAG, Multimodal RAG?

Bạn nên viết câu trả lời ngắn theo format:
```text
Component: Retrieval
Input: user query + index
Output: relevant chunks
Main failure: retrieve sai/thiếu context
Evaluation: Recall@k, Precision@k, MRR
```

---

## 4.1 Practice Question 1: Giáo Dục - Sinh Câu Hỏi Trắc Nghiệm
Một trường trung học phổ thông đang tìm cách triển khai **hệ thống tự động tạo sinh câu hỏi trắc nghiệm** nhằm giảm tải áp lực cho giáo viên. Thách thức lớn nhất nằm ở tính chất đa dạng của học liệu: giáo trình bao gồm các tệp PDF chứa nhiều bảng số liệu kinh tế (table), biểu đồ (graph Image) và công thức phức tạp (math formula). Nhà trường yêu cầu hệ thống phải hiểu sâu nội dung để tạo ra các phương án nhiễu (distractors) thực sự chất lượng, đánh trúng các lỗi tư duy phổ biến thay vì chỉ đưa ra các câu trả lời sai ngẫu nhiên. Tuy nhiên, ngân sách của trường chỉ ở mức trung bình, ưu tiên chi phí vận hành hàng tháng thấp thay vì đầu tư máy chủ đắt tiền. Đặc biệt, hệ thống phải có khả năng mô phỏng chính xác văn phong, cấu trúc câu hỏi và tiêu chuẩn độ khó dựa trên kho lưu trữ đề thi lịch sử của nhà trường. 
**Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai ?**

### 4.1.B Brainstorming Questions
Không viết answer ngay. Trả lời nhanh các câu này trước:
1. User chính là ai?
2. Output cuối cùng là gì?
3. Dữ liệu nào là nguồn kiến thức chính?
4. Dữ liệu nào dùng để học style?
5. Tại sao Standard RAG chưa đủ?
6. Có những modality nào cần xử lý?
7. Rủi ro lớn nhất của hệ thống là gì?
8. Ngân sách ảnh hưởng đến thiết kế thế nào?
9. Có cần human-in-the-loop không?
10. RAG type phù hợp nhất là gì?

### 4.1.A Answering AI System Question
Dùng câu hỏi sau để tự điền format:

**Solution:**  
- Hệ thống tên gì?
- Dùng RAG type nào?
- Giải quyết vấn đề chính nào?

**Analyze Business Question:**  
- Vấn đề 1: dữ liệu multimodal cần xử lý thế nào?
- Vấn đề 2: distractors chất lượng cần kỹ thuật gì?
- Vấn đề 3: mô phỏng đề thi cũ bằng cách nào?
- Vấn đề 4: làm sao giữ chi phí thấp?
- Vấn đề 5: kiểm soát chất lượng ra sao?

**Abstract Workflow:**  
- Các step từ upload học liệu đến giáo viên duyệt là gì?

**Implementation:**  
- Parser nào dùng cho PDF/text/table/image/formula?
- Index thế nào?
- Retrieve từ những nguồn nào?
- Prompt output schema gồm gì?
- Quality checker kiểm gì?

**MVP Scope and Tradeoffs:**  
- MVP nên giới hạn ở môn/chương nào?
- Tạm hoãn gì?
- Tradeoff chính là gì?


----

## 4.2 Practice Question 2: Y Tế - Hỗ Trợ Chẩn Đoán Và Tra Cứu Phác Đồ
Bệnh viện chúng tôi muốn xây dựng một công cụ hỗ trợ bác sĩ ra quyết định lâm sàng dựa trên kho bệnh án khổng lồ hiện có. Hệ thống phải đảm bảo an toàn tuyệt đối, thông tin đưa ra bắt buộc phải có trích dẫn từ các hướng dẫn y khoa chính thống và không được phép sai lệch vì liên quan trực tiếp đến tính mạng bệnh nhân. Do các quy định khắt khe về bảo mật y tế, toàn bộ dữ liệu bệnh nhân không được phép rời khỏi hạ tầng nội bộ của bệnh viện để xử lý ở bên ngoài. Với ngân sách đầu tư ban đầu khiêm tốn, chúng tôi yêu cầu AI phải hiểu được các mối liên hệ phức tạp giữa các chỉ số xét nghiệm dạng bảng biểu (table), kết quả chẩn đoán hình ảnh (image) và các ghi chú lâm sàng của bác sĩ. Bệnh viện chấp nhận việc hệ thống mất vài phút để phân tích, miễn là kết quả cuối cùng đạt độ xác thực và tin cậy cao nhất.
**Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai ?**


### 4.2.B Brainstorming Questions
1. User chính là ai?
2. Hệ thống có được tự chẩn đoán thay bác sĩ không?
3. Output cuối cùng nên là gì?
4. Rủi ro lớn nhất là gì?
5. Vì sao bắt buộc citation?
6. Vì sao dữ liệu không được rời hạ tầng nội bộ?
7. Data gồm những loại nào?
8. Có cần Graph RAG không? Vì sao?
9. Có cần Corrective RAG không? Vì sao?
10. Latency vài phút giúp ta thêm được module nào?

### 4.2.A Answering AI System Question

**Solution:**  
- Hệ thống nên là clinical decision support hay autonomous diagnosis?
- Dùng RAG type nào?
- Vì sao phải on-prem?

**Analyze Business Question:**  
- Vấn đề 1: an toàn tuyệt đối thì cần verification gì?
- Vấn đề 2: citation guideline chính thống thì retrieval/index ra sao?
- Vấn đề 3: bảo mật dữ liệu bệnh nhân thì deployment thế nào?
- Vấn đề 4: lab table/image/clinical notes thì parsing thế nào?
- Vấn đề 5: quan hệ y khoa phức tạp thì dùng Graph RAG ra sao?

**Abstract Workflow:**  
- Từ ingest guideline/bệnh án đến doctor review gồm những bước nào?

**Implementation:**  
- Local vector DB?
- Local/open-source model?
- Access control?
- Audit log?
- Guideline citation?
- Abstention khi thiếu bằng chứng?

**MVP Scope and Tradeoffs:**  
- MVP nên giới hạn ở 1 chuyên khoa hay toàn viện?
- Tradeoff chính là accuracy/privacy vs cost/complexity đúng không?


## 4.3 Practice Question 3: Pháp Lý - Rà Soát Tuân Thủ Và Phân Tích Rủi Ro Hợp Đồng
Phòng pháp chế của một tập đoàn đa quốc gia muốn triển khai hệ thống tự động rà soát các dự thảo hợp đồng dựa trên bộ quy tắc ứng xử nội bộ và luật pháp hiện hành. Các văn bản này thường dài hàng chục trang với ngôn ngữ pháp lý lắt léo và các điều khoản liên kết chéo phức tạp cần được đối soát kỹ lưỡng để tránh các rủi ro mà con người dễ bỏ sót. Mọi quá trình xử lý dữ liệu phải diễn ra hoàn toàn nội bộ (on-premise) để đảm bảo bí mật kinh doanh tuyệt đối. Hệ thống cần đưa ra kết quả nhanh chóng để kịp thời hỗ trợ các luật sư ngay tại bàn đàm phán trực tiếp với đối tác. Tài nguyên hiện có bao gồm kho dữ liệu khổng lồ về các bộ luật, lịch sử các hợp đồng đã ký và các bảng quy định (table) điều khoản mẫu của tập đoàn.

**Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai?**

### 4.3.B Brainstorming Questions

1. User chính là ai: luật sư, phòng pháp chế, hay đội đàm phán?
2. Output cuối cùng cần là gì: checklist rủi ro, điều khoản vi phạm, citation luật, hay đề xuất sửa đổi?
3. Dữ liệu đầu vào gồm những gì?
4. Vì sao hợp đồng dài hàng chục trang là vấn đề lớn với Standard RAG?
5. Điều khoản liên kết chéo gây ra failure mode nào?
6. Vì sao cần xử lý hoàn toàn on-premise?
7. Vì sao hệ thống cần phản hồi nhanh tại bàn đàm phán?
8. Kho luật pháp, hợp đồng cũ và bảng điều khoản mẫu nên được index riêng hay chung?
9. Có cần Graph RAG không? Nếu có, graph biểu diễn quan hệ gì?
10. Có cần Rule-based RAG không? Nếu có, rule đến từ đâu?
11. Có cần Hybrid Search không? Vì sao keyword pháp lý và số điều khoản quan trọng?
12. Có cần citation bắt buộc không?
13. Rủi ro lớn nhất của hệ thống là gì: hallucination, bỏ sót điều khoản, trích luật sai, hay lộ bí mật hợp đồng?
14. MVP nên giới hạn ở loại hợp đồng nào trước?
15. Tradeoff chính là gì: tốc độ tại bàn đàm phán vs độ sâu rà soát pháp lý?

### 4.3.A Answering AI System Question

**Solution:**  
- Hệ thống nên là contract review assistant hay tự động phê duyệt hợp đồng?
- Dùng RAG type nào: On-prem Rule-based + Graph + Hybrid RAG?
- Vấn đề chính cần giải quyết là gì: rà soát điều khoản, tuân thủ luật, đối chiếu rule nội bộ, phát hiện rủi ro?

**Analyze Business Question:**  
- Vấn đề 1: hợp đồng dài, ngôn ngữ pháp lý phức tạp -> cần retrieval/chunking kiểu nào?
- Vấn đề 2: điều khoản liên kết chéo -> cần Graph RAG hoặc structure-aware retrieval ra sao?
- Vấn đề 3: bộ quy tắc nội bộ và luật hiện hành -> cần Rule-based RAG/citation như thế nào?
- Vấn đề 4: dữ liệu bí mật, phải on-premise -> deployment và data security ra sao?
- Vấn đề 5: cần phản hồi nhanh tại bàn đàm phán -> làm sao cân bằng latency và accuracy?
- Vấn đề 6: có hợp đồng đã ký và bảng điều khoản mẫu -> dùng làm benchmark/risk pattern/style reference thế nào?

**Evaluation Criteria:**  
- Clause detection accuracy.
- Risk classification accuracy.
- Citation correctness.
- Missing-risk rate.
- False positive rate.
- Latency per contract/query.
- Access control correctness.
- Lawyer acceptance rate.

**Abstract Workflow:**  
- Từ upload hợp đồng đến báo cáo rủi ro gồm các bước nào?
- Có bước parse clause không?
- Có bước detect cross-reference không?
- Có bước retrieve luật/rule nội bộ không?
- Có bước generate risk report không?

**Implementation:**  
- Parser nào dùng cho hợp đồng PDF/DOCX?
- Chunk theo page hay theo clause?
- Metadata nên gồm gì: contract type, clause type, jurisdiction, effective date, risk level?
- Index luật, hợp đồng cũ, rule nội bộ và bảng điều khoản mẫu thế nào?
- Graph lưu quan hệ nào: clause -> referenced clause, clause -> law, clause -> internal policy?
- Output schema gồm gì: issue, clause, risk level, violated rule, citation, suggested revision?

**MVP Scope and Tradeoffs:**  
- MVP nên giới hạn ở NDA, MSA, hợp đồng mua bán hay hợp đồng lao động?
- Tạm hoãn gì: full legal reasoning, multi-jurisdiction support, auto-redlining?
- Tradeoff chính là gì: tốc độ phản hồi vs độ đầy đủ phân tích rủi ro?

---

## 4.4 Practice Question 4: Tuyển Dụng - Phân Tích Và Xếp Hạng Hồ Sơ Ứng Viên
Tập đoàn chúng tôi đang đối mặt với việc xử lý hàng ngàn hồ sơ ứng viên mỗi đợt tuyển dụng. Các hồ sơ này rất lộn xộn, từ tệp PDF, ảnh chụp cho đến văn bản thô, chứa nhiều định dạng bảng biểu kỹ năng và lịch sử làm việc khác nhau. Chúng tôi cần một giải pháp tự động bóc tách và xếp hạng ứng viên dựa trên mô tả công việc (JD) một cách khách quan nhất, loại bỏ cảm tính cá nhân và phải giải thích được lý do cụ thể tại sao ứng viên đó lại phù hợp. Do số lượng hồ sơ cực lớn, hệ thống cần ưu tiên khả năng xử lý hàng loạt với độ chính xác cao để không bỏ sót những tài năng tiềm năng. Tài nguyên hiện có bao gồm kho CV tích lũy qua nhiều năm và danh sách các tiêu chuẩn chuyên môn khắt khe được cập nhật liên tục.
**Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai?**

### 4.4.B Brainstorming Questions

1. User chính là ai: HR, recruiter, hiring manager?
2. Output cuối cùng là gì: ranking, shortlist, explanation, skill gap, hay interview recommendation?
3. Dữ liệu đầu vào gồm những loại nào?
4. Vì sao CV lộn xộn từ PDF/ảnh/text là vấn đề parsing?
5. JD đóng vai trò gì trong retrieval/ranking?
6. Tiêu chuẩn chuyên môn cập nhật liên tục nên được lưu và retrieve thế nào?
7. Kho CV tích lũy nhiều năm dùng để làm gì: benchmark, talent rediscovery, ranking baseline?
8. Rủi ro lớn nhất là gì: bỏ sót ứng viên tốt, ranking bias, parse sai CV, explainability kém?
9. Có cần RAG không, hay chỉ classification/ranking? RAG giúp ở đâu?
10. Có cần Hybrid Search không? Vì skill keyword, tool name, certification rất quan trọng?
11. Có cần fairness/bias guardrail không?
12. Có cần human-in-the-loop không?
13. Do số lượng CV lớn, batch processing nên thiết kế thế nào?
14. Có nên dùng multimodal parsing không?
15. Tradeoff chính là gì: recall ứng viên tiềm năng vs precision shortlist?

### 4.4.A Answering AI System Question

**Solution:**  
- Hệ thống nên là AI screening assistant hay auto-reject system?
- Dùng RAG type nào: Multimodal Hybrid RAG + Ranking/Scoring Pipeline?
- Vấn đề chính cần giải quyết là gì: parse CV, match JD, xếp hạng khách quan, giải thích lý do?

**Analyze Business Question:**  
- Vấn đề 1: CV nhiều định dạng lộn xộn -> cần document parsing/OCR thế nào?
- Vấn đề 2: cần match với JD -> dùng skill extraction + retrieval/ranking ra sao?
- Vấn đề 3: tiêu chuẩn chuyên môn cập nhật liên tục -> index criteria/rubric thế nào?
- Vấn đề 4: không bỏ sót talent -> ưu tiên recall hay precision ở bước đầu?
- Vấn đề 5: cần khách quan và explainable -> output cần evidence/explanation gì?
- Vấn đề 6: xử lý hàng loạt -> batch pipeline, caching, queue ra sao?

**Evaluation Criteria:**  
- CV parsing accuracy.
- Skill extraction accuracy.
- Recall@k for qualified candidates.
- Ranking quality: NDCG@k / Precision@k.
- Explanation quality.
- Bias/fairness metrics.
- Processing throughput.
- Human recruiter acceptance rate.

**Abstract Workflow:**  
- Từ upload CV/JD đến shortlist gồm những bước nào?
- Có bước extract structured profile không?
- Có bước normalize skills không?
- Có bước retrieve criteria/JD không?
- Có bước score/rank không?
- Có bước recruiter review không?

**Implementation:**  
- OCR/parser nào dùng cho PDF/ảnh/text?
- Extract field nào: education, years experience, skills, projects, certifications, job history?
- Skill taxonomy dùng thế nào?
- JD được parse thành requirement bắt buộc và optional ra sao?
- Ranking score gồm những thành phần nào?
- Output schema gồm gì: candidate score, matched skills, missing skills, evidence from CV, risk/concern, explanation?

**MVP Scope and Tradeoffs:**  
- MVP nên giới hạn ở 1-2 vị trí tuyển dụng trước không?
- Tạm hoãn gì: full ATS integration, automated rejection, deep fairness auditing?
- Tradeoff chính là gì: không bỏ sót ứng viên tốt vs shortlist quá rộng?

---

## 4.5 Practice Question 5: Doanh Nghiệp Công Nghệ - Tra Cứu Tri Thức Nội Bộ
Chúng tôi muốn xây dựng một cổng thông tin tập trung để nhân viên có thể nhanh chóng tra cứu các quy trình vận hành (SOP) từ kho Wiki và các hướng dẫn kỹ thuật trên Slack. Hiện tại, thông tin bị phân mảnh khiến nhân viên mất nhiều thời gian để tìm được câu trả lời chính xác cho công việc hàng ngày. Hệ thống cần khả năng tổng hợp thông tin từ các đoạn hội thoại hoặc văn bản dài để đưa ra câu trả lời ngắn gọn, đúng ngữ cảnh. Yêu cầu quan trọng là phải đảm bảo quyền truy cập: nhân viên chỉ được thấy những tài liệu phù hợp với phòng ban của mình, không được tiếp cận các thông tin nhạy cảm của cấp quản lý. Chúng tôi ưu tiên một giải pháp ổn định, chi phí vận hành thấp và dữ liệu chỉ cần cập nhật định kỳ mỗi ngày thay vì phải cập nhật tức thời.
**Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai?**

### 4.5.B Brainstorming Questions
1. User chính là ai: nhân viên mới, engineer, support, manager?
2. Output cuối cùng là gì: câu trả lời ngắn gọn, citation, link đến SOP/wiki/slack?
3. Dữ liệu nguồn gồm những gì?
4. Vì sao thông tin phân mảnh là vấn đề retrieval?
5. Slack conversation khác Wiki/SOP ở điểm nào?
6. Có cần Conversational RAG không nếu nhân viên hỏi follow-up?
7. Có cần Fusion RAG không vì dữ liệu đến từ Wiki + Slack?
8. Yêu cầu quyền truy cập ảnh hưởng đến retrieval như thế nào?
9. Cần permission filtering ở trước retrieval hay sau retrieval?
10. Dữ liệu chỉ cập nhật mỗi ngày, vậy indexing pipeline nên chạy thế nào?
11. Chi phí thấp và ổn định thì nên chọn kiến trúc gì?
12. Có cần real-time ingestion không?
13. Rủi ro lớn nhất là gì: trả lời sai SOP, lộ thông tin nhạy cảm, context lỗi thời?
14. Có cần citation/source link không?
15. Tradeoff chính là gì: độ mới dữ liệu vs chi phí vận hành?

### 4.5.A Answering AI System Question

**Solution:**  
- Hệ thống nên là internal knowledge assistant hay search portal?
- Dùng RAG type nào: Permission-aware Fusion/Conversational RAG?
- Vấn đề chính cần giải quyết là gì: tổng hợp tri thức phân mảnh, trả lời ngắn gọn, đảm bảo access control?

**Analyze Business Question:**  
- Vấn đề 1: tri thức nằm ở Wiki và Slack -> cần Fusion RAG/index nhiều nguồn ra sao?
- Vấn đề 2: văn bản dài và hội thoại rời rạc -> cần summarization/chunking thế nào?
- Vấn đề 3: nhân viên chỉ được thấy tài liệu theo phòng ban -> permission-aware retrieval ra sao?
- Vấn đề 4: cần câu trả lời ngắn đúng ngữ cảnh -> prompt/context compression thế nào?
- Vấn đề 5: ưu tiên ổn định và chi phí thấp -> batch daily indexing/caching ra sao?
- Vấn đề 6: không cần cập nhật tức thời -> tradeoff freshness vs cost thế nào?

**Evaluation Criteria:**  
- Answer correctness.
- Groundedness/citation accuracy.
- Retrieval Precision@k / Recall@k.
- Access control violation rate.
- Answer latency.
- Cost/query.
- User satisfaction.
- Deflection rate / time saved.

**Abstract Workflow:**  
- Từ sync Wiki/Slack đến trả lời nhân viên gồm những bước nào?
- Có daily ingestion không?
- Có permission metadata không?
- Có hybrid retrieval không?
- Có citation/source link không?

**Implementation:**  
- Connector lấy dữ liệu từ Wiki/Slack thế nào?
- Làm sạch Slack thread ra sao?
- Chunk Wiki và Slack khác nhau thế nào?
- Metadata cần gì: department, role, channel, document owner, updated_at, sensitivity level?
- Index vào vector DB + BM25 thế nào?
- Permission filter dùng user profile/department/role ra sao?
- Output schema gồm gì: short answer, sources, confidence, escalation khi thiếu thông tin?

**MVP Scope and Tradeoffs:**  
- MVP nên giới hạn ở vài team hoặc vài wiki space/channel trước không?
- Tạm hoãn gì: real-time sync, full enterprise SSO integration, advanced personalization?
- Tradeoff chính là gì: freshness của dữ liệu vs chi phí vận hành và độ ổn định?




# 5. Brainstorming And Answer Examples

## 1. Hệ thống hỗ trợ biên soạn học liệu

### Quick Brainstorm

| Brainstorm Item | Phân tích nhanh |
|---|---|
| User | Giáo viên, tổ bộ môn, người biên soạn đề. |
| Output | Câu hỏi trắc nghiệm, 4 đáp án, đáp án đúng, lời giải, distractor rationale, độ khó. |
| Data | PDF giáo trình, bảng số liệu kinh tế, biểu đồ ảnh, công thức, đề thi lịch sử. |
| Main Risk | Câu hỏi sai kiến thức, distractors ngẫu nhiên/kém chất lượng, không giống văn phong đề cũ. |
| Constraint | Ngân sách trung bình, ưu tiên chi phí vận hành thấp. |
| RAG Type | **Multimodal Fusion RAG + Style Retrieval**. |

### Answer Example

**Solution:**  
**Multimodal Fusion RAG for MCQ Generation** - hệ thống tạo câu hỏi trắc nghiệm từ PDF giáo trình, bảng, biểu đồ, công thức và đề thi lịch sử. Chọn thiết kế này vì học liệu đa phương thức, cần sinh distractors chất lượng và mô phỏng văn phong/độ khó của đề thi cũ với chi phí vận hành vừa phải.

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| Học liệu đa dạng gồm PDF, bảng, biểu đồ, công thức | Dùng multimodal parsing: PDF parser cho text, table extractor cho bảng, OCR/vision model cho biểu đồ, math OCR/API cho công thức; chuẩn hóa thành text có cấu trúc. | Text extraction quality, table extraction accuracy, chart understanding quality, formula extraction quality. | Giúp tận dụng tài liệu hiện có của trường thay vì giáo viên phải nhập lại thủ công, đồng thời tránh mất thông tin quan trọng trong bảng/biểu đồ/công thức. |
| Cần sinh distractors chất lượng | Dùng misconception-aware generation: trước khi sinh phương án nhiễu, LLM phân tích khái niệm trọng tâm, lỗi tư duy phổ biến, lỗi đọc bảng/biểu đồ, lỗi tính toán. | Distractor quality score, teacher acceptance rate, % distractors cần chỉnh sửa. | Giá trị chính không chỉ là tạo câu hỏi nhanh, mà là giảm tải phần khó nhất cho giáo viên: tạo phương án nhiễu có ý nghĩa sư phạm. |
| Cần mô phỏng văn phong, cấu trúc và độ khó của đề thi cũ | Index đề thi lịch sử riêng; retrieve 3-5 câu mẫu cùng chủ đề/độ khó để làm style examples khi sinh câu mới. | Style similarity, difficulty alignment, teacher rating. | Giúp câu hỏi mới nhất quán với chuẩn ra đề của trường, giảm thời gian giáo viên chỉnh sửa lại. |
| Ngân sách trung bình, cần chi phí vận hành thấp | Không fine-tune model lớn hoặc self-host GPU. Dùng LLM API cho generation, model nhỏ cho classification/checking, cache parsing và embedding. | Cost/question, monthly API cost, token usage/request. | Tránh đầu tư hạ tầng đắt tiền, phù hợp MVP và có thể mở rộng theo nhu cầu thật. |
| Cần đảm bảo chất lượng trước khi dùng | Thêm quality checker + teacher review: kiểm tra bám context, chỉ có một đáp án đúng, distractors hợp lý, không copy đề cũ. | Pass rate, hallucination rate, duplicate rate, teacher accept/edit/reject rate. | Giáo viên vẫn kiểm soát đầu ra cuối cùng, giảm rủi ro câu hỏi sai hoặc kém chất lượng. |

**Abstract Workflow:**  
Upload học liệu -> Parse PDF theo text/table/graph/formula -> Chuẩn hóa nội dung -> Chunk + metadata -> Index giáo trình + đề thi cũ -> Nhận yêu cầu tạo câu hỏi -> Retrieve/Fusion context -> Sinh MCQ + distractors -> Quality check -> Giáo viên duyệt -> Lưu feedback

**Explain each step and how to implement it in short**

| Step                            | Mục tiêu                                                | Cách triển khai MVP                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Upload học liệu              | Thu thập giáo trình và đề thi lịch sử.                  | Web app cho upload PDF/DOCX/image. Lưu file vào local/cloud storage. Metadata: môn, lớp, chương, bài, năm học, loại tài liệu.                         |
| 2. Parse PDF                    | Tách nội dung từ tài liệu phức tạp.                     | Dùng `PyMuPDF`/`Unstructured` cho text, `Camelot`/`Tabula` cho bảng, OCR/vision model cho biểu đồ, Math OCR/API cho công thức nếu ngân sách cho phép. |
| 3. Chuẩn hóa multimodal content | Biến bảng, biểu đồ, công thức thành dạng LLM hiểu được. | Table -> Markdown/CSV + mô tả xu hướng; graph -> caption về trục, đơn vị, xu hướng; formula -> LaTeX + giải thích biến số.                            |
| 4. Chunk + metadata             | Tạo đơn vị kiến thức dễ retrieve.                       | Chunk theo chương/bài/mục. Gắn metadata: `subject`, `grade`, `chapter`, `topic`, `content_type`, `page`, `source`.                                    |
| 5. Index giáo trình và đề cũ    | Cho phép retrieve kiến thức và style.                   | Index giáo trình trong vector DB + BM25. Index đề thi cũ riêng theo stem, options, answer, topic, difficulty, style pattern.                          |
| 6. Nhận yêu cầu tạo câu hỏi     | Cho giáo viên kiểm soát đầu ra.                         | Form gồm môn, chương, chủ đề, số câu, độ khó, loại nội dung cần dùng: text/table/graph/formula, có/không lời giải.                                    |
| 7. Retrieve/Fusion context      | Lấy đúng kiến thức và mẫu style.                        | Retrieve từ giáo trình để lấy kiến thức đúng; retrieve từ đề cũ để lấy văn phong/độ khó; ưu tiên chunk theo `content_type`.                           |
| 8. Generate MCQ                 | Sinh câu hỏi và distractors.                            | Prompt LLM sinh schema: câu hỏi, 4 đáp án, đáp án đúng, lời giải, distractor rationale, misconception, nguồn tham chiếu.                              |
| 9. Quality check                | Giảm lỗi kiến thức và distractor yếu.                   | Rule checker + LLM-as-judge kiểm tra: 1 đáp án đúng, bám context, distractors hợp lý, không copy đề cũ, đúng độ khó.                                  |
| 10. Teacher review              | Đảm bảo chất lượng sư phạm.                             | UI cho giáo viên accept/edit/reject, chỉnh distractor, lời giải, độ khó.                                                                              |
| 11. Feedback loop               | Cải thiện hệ thống sau MVP.                             | Lưu chỉnh sửa của giáo viên để cải thiện prompt, retrieval, metadata và rubric đánh giá.                                                              |

**MVP Scope and Tradeoffs:**  
MVP nên giới hạn ở 1-2 môn hoặc vài chương có đủ text, bảng, biểu đồ và công thức. Tạm hoãn fine-tuning model riêng, self-host GPU và xử lý hoàn hảo mọi loại PDF. Tradeoff chính là **chất lượng xử lý multimodal vs chi phí/độ phức tạp triển khai**.


## 2. Trợ lý hỗ trợ chẩn đoán và tra cứu phác đồ

### Quick Brainstorm

| Brainstorm Item | Phân tích nhanh                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------- |
| User            | Bác sĩ, hội chẩn lâm sàng, nhân viên y tế có thẩm quyền.                                          |
| Output          | Gợi ý hỗ trợ quyết định lâm sàng, phác đồ liên quan, cảnh báo rủi ro, citation guideline.         |
| Data            | Bệnh án, lab table, medical image/report, clinical notes, guideline chính thống.                  |
| Main Risk       | Sai y khoa, hallucination, thiếu citation, rò rỉ dữ liệu bệnh nhân.                               |
| Constraint      | Dữ liệu không rời hạ tầng bệnh viện, ngân sách đầu tư khiêm tốn, latency vài phút chấp nhận được. |
| RAG Type        | **On-prem Multimodal Graph + Corrective RAG**.                                                    |

### Answer Example

**Solution:**  
**On-prem Multimodal Graph + Corrective RAG for Clinical Decision Support** - hệ thống hỗ trợ bác sĩ tra cứu phác đồ và phân tích bệnh án nội bộ với citation bắt buộc, verification nhiều lớp và triển khai hoàn toàn trong hạ tầng bệnh viện. Chọn thiết kế này vì y tế là domain rủi ro cao, dữ liệu bệnh nhân phải bảo mật tuyệt đối và kết quả phải có căn cứ từ guideline chính thống.

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| Thông tin y tế không được phép sai lệch | Dùng Corrective RAG: retrieve evidence, rerank, verify bằng guideline, cho phép abstain nếu thiếu bằng chứng. | Groundedness, unsafe recommendation rate, hallucination rate. | Giảm rủi ro đưa ra khuyến nghị sai ảnh hưởng đến tính mạng bệnh nhân. |
| Bắt buộc có trích dẫn từ guideline chính thống | Xây kho guideline được kiểm duyệt, citation-required generation, mọi claim quan trọng phải map về nguồn. | Citation accuracy, source validity, claim-evidence alignment. | Bác sĩ có thể kiểm chứng nhanh và bệnh viện có căn cứ audit khi cần. |
| Dữ liệu bệnh nhân không được rời hạ tầng nội bộ | Triển khai on-premise: local vector DB, local/open-source LLM, access control, audit log. | Data leakage rate, access control correctness, audit completeness. | Đáp ứng quy định bảo mật y tế và bảo vệ thông tin bệnh nhân. |
| Dữ liệu đa phương thức: lab table, image, clinical notes | Parse lab table thành structured values, xử lý clinical notes bằng NLP, ưu tiên dùng radiology report hoặc model vision nội bộ cho image. | Lab extraction accuracy, note extraction quality, image/report understanding quality. | Giúp bác sĩ tổng hợp nhiều nguồn bệnh án thay vì kiểm tra thủ công từng phần. |
| Cần hiểu quan hệ phức tạp giữa xét nghiệm, hình ảnh, triệu chứng và phác đồ | Dùng Graph RAG/clinical knowledge graph để liên kết patient finding -> disease -> guideline -> treatment -> contraindication. | Relationship extraction accuracy, diagnosis-support relevance. | Hỗ trợ phân tích lâm sàng sâu hơn retrieval text đơn thuần. |
| Chấp nhận latency vài phút để đạt độ tin cậy cao | Thêm reranking, multi-step retrieval, second-pass verification, safety checker. | End-to-end latency, verification pass rate, doctor acceptance rate. | Phù hợp nghiệp vụ y tế: tốc độ không quan trọng bằng độ xác thực và an toàn. |

**Abstract Workflow:**  
Ingest guideline + bệnh án -> De-identification/access control -> Parse lab/image/notes -> Build vector index + clinical graph -> Doctor query -> Retrieve patient context + guideline -> Graph reasoning -> Rerank/verify evidence -> Generate answer with citations -> Safety check/abstention -> Doctor review -> Audit log

**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP |
|---|---|---|
| 1. Ingest dữ liệu | Thu thập guideline và bệnh án nội bộ. | Nạp guideline chính thống, bệnh án, lab results, clinical notes, radiology reports vào hạ tầng nội bộ. |
| 2. Security & access control | Bảo vệ dữ liệu bệnh nhân. | Áp dụng RBAC, audit log, encryption, de-identification khi dùng cho evaluation/training nội bộ. |
| 3. Parse multimodal clinical data | Chuẩn hóa dữ liệu y tế. | Lab table -> structured values; clinical notes -> problems/medications/symptoms; image -> ưu tiên radiology report, hoặc vision model nội bộ nếu cần. |
| 4. Build indexes | Tìm kiếm evidence đáng tin cậy. | Tạo vector index + BM25 cho guideline, notes, reports; gắn metadata: source, date, specialty, patient ID, access level. |
| 5. Build clinical graph | Biểu diễn quan hệ y khoa. | Graph gồm finding, lab abnormality, symptom, diagnosis, guideline, treatment, contraindication. |
| 6. Doctor query | Nhận yêu cầu từ bác sĩ. | Bác sĩ nhập câu hỏi hoặc chọn patient case; hệ thống lấy patient context theo quyền truy cập. |
| 7. Retrieve + graph reasoning | Lấy evidence và quan hệ liên quan. | Retrieve guideline/patient context, sau đó dùng graph để tìm quan hệ giữa triệu chứng, xét nghiệm, chẩn đoán, phác đồ. |
| 8. Verify evidence | Kiểm tra trước khi trả lời. | Reranker + LLM verifier kiểm tra claim có được support bởi guideline không; nếu thiếu evidence thì abstain. |
| 9. Generate response | Trả lời có citation. | Output gồm: summary, possible considerations, relevant guideline, citation, confidence, warning, không thay thế quyết định bác sĩ. |
| 10. Doctor review + audit | Giữ bác sĩ là người quyết định cuối. | Bác sĩ xem, chấp nhận/bỏ qua, mọi truy vấn và nguồn dùng được log để audit. |

**MVP Scope and Tradeoffs:**  
MVP nên giới hạn ở 1 chuyên khoa hoặc 1 nhóm bệnh phổ biến, ví dụ tim mạch/đái tháo đường/cấp cứu nội khoa. Tạm hoãn xử lý trực tiếp mọi loại ảnh y tế phức tạp; ưu tiên radiology report trước. Tradeoff chính là **độ tin cậy/bảo mật vs chi phí triển khai và độ phức tạp hệ thống**.

## 3. Hệ thống rà soát tuân thủ và phân tích rủi ro hợp đồng

### Quick Brainstorm

| Brainstorm Item | Phân tích nhanh                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------- |
| User            | Luật sư, phòng pháp chế, đội đàm phán hợp đồng.                                                    |
| Output          | Báo cáo rủi ro: điều khoản có vấn đề, mức độ rủi ro, rule/law bị ảnh hưởng, citation, đề xuất sửa. |
| Data            | Hợp đồng dài, bộ luật, quy tắc nội bộ, hợp đồng cũ, bảng điều khoản mẫu.                           |
| Main Risk       | Bỏ sót rủi ro pháp lý, trích luật sai, lộ bí mật hợp đồng.                                         |
| Constraint      | On-premise, cần phản hồi nhanh tại bàn đàm phán.                                                   |
| RAG Type        | **On-prem Rule-based Graph/Hybrid RAG**.                                                           |

### Answer Example

**Solution:**  
**On-prem Rule-based Graph/Hybrid RAG for Contract Risk Review** - hệ thống rà soát hợp đồng nội bộ, phát hiện điều khoản rủi ro, đối chiếu luật và quy tắc công ty. Chọn thiết kế này vì hợp đồng dài, có cross-reference phức tạp, dữ liệu tuyệt mật và cần phản hồi nhanh cho luật sư.

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| Hợp đồng dài, ngôn ngữ pháp lý phức tạp | Parse hợp đồng theo clause/section, chunk theo điều khoản thay vì cắt token cố định. | Clause parsing accuracy, risk detection accuracy. | Giúp luật sư không phải đọc thủ công toàn bộ hợp đồng dài, giảm rủi ro bỏ sót điều khoản quan trọng. |
| Điều khoản liên kết chéo phức tạp | Dùng Graph RAG để biểu diễn quan hệ clause -> referenced clause -> law/rule. | Cross-reference detection accuracy, missing-risk rate. | Giúp phát hiện rủi ro phát sinh từ nhiều điều khoản liên quan, điều con người dễ bỏ sót. |
| Cần đối chiếu luật và quy tắc nội bộ | Dùng Rule-based RAG + hybrid search để retrieve luật, policy, bảng điều khoản mẫu. | Citation correctness, rule matching accuracy. | Đảm bảo kết quả không chỉ là nhận xét chung chung mà có căn cứ luật/rule rõ ràng. |
| Dữ liệu hợp đồng tuyệt mật | Triển khai on-premise, local vector DB, local LLM hoặc model nội bộ. | Data leakage rate, access control correctness. | Bảo vệ bí mật kinh doanh và đáp ứng yêu cầu bảo mật của tập đoàn. |
| Cần phản hồi nhanh tại bàn đàm phán | Pre-index luật/rule/hợp đồng mẫu; chỉ parse và phân tích hợp đồng mới khi cần. | Latency/query, time-to-risk-report. | Hỗ trợ luật sư ra quyết định nhanh trong quá trình đàm phán. |

**Abstract Workflow:**  
Upload hợp đồng -> Parse clause/section -> Extract metadata/cross-reference -> Index luật/rule/hợp đồng mẫu -> Hybrid retrieval -> Graph reasoning -> Risk analysis -> Generate report -> Lawyer review -> Audit log

**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP |
|---|---|---|
| 1. Upload hợp đồng | Nhận draft hợp đồng cần rà soát. | Cho upload PDF/DOCX, lưu nội bộ, gắn metadata: loại hợp đồng, quốc gia, phòng ban, đối tác. |
| 2. Parse clause | Tách hợp đồng thành điều khoản. | Dùng document parser để tách heading, section, clause, sub-clause; giữ số điều khoản gốc. |
| 3. Extract cross-reference | Nhận diện điều khoản liên kết chéo. | Dùng rule regex + LLM extraction để phát hiện “theo Điều X”, “subject to Clause Y”. |
| 4. Index tri thức pháp lý | Tìm luật/rule/mẫu liên quan. | Tạo hybrid index cho bộ luật, policy nội bộ, bảng điều khoản mẫu, hợp đồng cũ. |
| 5. Graph retrieval | Theo dõi quan hệ pháp lý phức tạp. | Tạo graph: clause -> referenced clause -> internal rule -> law -> risk category. |
| 6. Risk analysis | Phân loại rủi ro. | LLM so sánh clause với rule/law/mẫu chuẩn, gán risk level: low/medium/high. |
| 7. Generate report | Xuất báo cáo dễ dùng cho luật sư. | Output gồm: clause, issue, risk level, citation, lý do, đề xuất sửa. |
| 8. Lawyer review | Kiểm soát kết quả cuối. | Luật sư accept/edit/reject và lưu feedback để cải thiện rule/prompt. |

**MVP Scope and Tradeoffs:**  
MVP nên giới hạn ở 1-2 loại hợp đồng phổ biến như NDA hoặc hợp đồng mua bán. Tạm hoãn multi-jurisdiction đầy đủ và auto-redlining phức tạp. Tradeoff chính là **tốc độ phản hồi vs độ sâu phân tích pháp lý**.

## 4. Hệ thống phân tích và xếp hạng hồ sơ ứng viên

### Quick Brainstorm

| Brainstorm Item | Phân tích nhanh |
|---|---|
| User | HR, recruiter, hiring manager. |
| Output | Ranking ứng viên, điểm phù hợp, lý do match/mismatch, evidence từ CV. |
| Data | CV PDF, ảnh chụp, text thô, bảng kỹ năng, JD, tiêu chuẩn chuyên môn. |
| Main Risk | Bỏ sót ứng viên tốt, bias, parse sai CV, giải thích không rõ. |
| Constraint | Xử lý hàng ngàn hồ sơ, cần batch throughput cao. |
| RAG Type | **Multimodal Hybrid RAG + Ranking Pipeline**. |

### Answer Example

**Solution:**  
**Multimodal Hybrid RAG + Ranking Pipeline for Candidate Screening** - hệ thống bóc tách CV, so khớp với JD và tiêu chuẩn chuyên môn, sau đó xếp hạng ứng viên kèm lý do giải thích. Chọn thiết kế này vì CV có nhiều định dạng lộn xộn, số lượng lớn và cần ranking khách quan, có bằng chứng.

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| CV có nhiều định dạng: PDF, ảnh, text, bảng kỹ năng | Dùng document parser + OCR + table extraction để chuẩn hóa CV thành structured profile. | CV parsing accuracy, field extraction accuracy. | Giảm công sức đọc CV thủ công và tránh mất thông tin quan trọng từ file lộn xộn. |
| Cần xếp hạng theo JD | Parse JD thành must-have, nice-to-have, skill, experience, certification; so khớp với profile ứng viên. | Ranking quality, Precision@k, Recall@k. | Giúp recruiter ưu tiên đúng ứng viên phù hợp thay vì lọc cảm tính. |
| Không bỏ sót tài năng tiềm năng | Dùng hybrid retrieval và ranking nhiều tầng: keyword skill + semantic match + rule scoring. | Qualified candidate Recall@k, false negative rate. | Ưu tiên recall ở vòng đầu để không loại nhầm ứng viên tốt. |
| Cần giải thích khách quan | Output evidence từ CV: kỹ năng nào match, kinh nghiệm nào liên quan, thiếu gì. | Explanation quality, recruiter acceptance rate. | Tăng niềm tin của HR/hiring manager và giảm tranh cãi khi shortlist. |
| Tiêu chuẩn chuyên môn cập nhật liên tục | Index tiêu chuẩn chuyên môn riêng, cập nhật theo từng role/level. | Criteria update freshness, criteria matching accuracy. | Đảm bảo ranking luôn bám chuẩn tuyển dụng mới nhất. |

**Abstract Workflow:**  
Upload CV/JD -> Parse CV -> Extract structured profile -> Normalize skills -> Index CV/JD/criteria -> Match & score -> Rank candidates -> Generate explanation -> Recruiter review -> Feedback loop

**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP |
|---|---|---|
| 1. Upload CV/JD | Nhận dữ liệu tuyển dụng. | Upload CV PDF/image/text và JD. Lưu metadata: role, level, location, hiring team. |
| 2. Parse CV | Bóc tách CV lộn xộn. | Dùng PDF parser + OCR cho ảnh chụp; table parser cho bảng kỹ năng/lịch sử làm việc. |
| 3. Extract profile | Chuẩn hóa ứng viên thành dữ liệu có cấu trúc. | Extract education, skills, years of experience, projects, certifications, job history. |
| 4. Normalize skills | Gom các kỹ năng tương đương. | Dùng skill taxonomy để map “JS” -> “JavaScript”, “ML” -> “Machine Learning”. |
| 5. Parse JD/criteria | Hiểu yêu cầu tuyển dụng. | Tách JD thành must-have, nice-to-have, domain knowledge, seniority, certification. |
| 6. Match & rank | Xếp hạng ứng viên. | Kết hợp rule score + semantic similarity + keyword match; ưu tiên recall ở vòng shortlist đầu. |
| 7. Explain result | Giải thích vì sao phù hợp. | Output: score, matched skills, missing skills, evidence từ CV, concern/risk. |
| 8. Recruiter review | Giữ con người trong quyết định tuyển dụng. | HR accept/edit/reject shortlist, lưu feedback để điều chỉnh scoring. |

**MVP Scope and Tradeoffs:**  
MVP nên giới hạn ở 1-2 vị trí tuyển dụng có nhiều CV, ví dụ Data Analyst hoặc Backend Engineer. Không nên tự động reject ứng viên trong MVP. Tradeoff chính là **recall ứng viên tốt vs precision của shortlist**.

---

## 5. Hệ thống tra cứu tri thức nội bộ

### Quick Brainstorm

| Brainstorm Item | Phân tích nhanh |
|---|---|
| User | Nhân viên công ty, engineer, support, nhân viên mới. |
| Output | Câu trả lời ngắn gọn, đúng ngữ cảnh, có citation/link nguồn. |
| Data | Wiki, SOP, Slack threads, hướng dẫn kỹ thuật. |
| Main Risk | Lộ thông tin nhạy cảm, trả lời sai SOP, dữ liệu lỗi thời. |
| Constraint | Chi phí thấp, ổn định, cập nhật mỗi ngày là đủ. |
| RAG Type | **Permission-aware Fusion/Conversational RAG**. |

### Answer Example

**Solution:**  
**Permission-aware Fusion RAG for Internal Knowledge Search** - cổng tra cứu tri thức nội bộ từ Wiki, SOP và Slack, trả lời ngắn gọn kèm nguồn và kiểm soát quyền truy cập. Chọn thiết kế này vì thông tin bị phân mảnh nhiều nguồn và yêu cầu quan trọng nhất là không lộ dữ liệu nhạy cảm.

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| Thông tin phân mảnh ở Wiki và Slack | Dùng Fusion RAG để ingest và index nhiều nguồn dữ liệu. | Retrieval Recall@k, source coverage. | Giúp nhân viên không mất thời gian tìm thủ công qua nhiều hệ thống. |
| Slack dài, rời rạc, nhiều noise | Làm sạch thread, tóm tắt hội thoại, chunk theo topic/thread. | Context relevance, answer correctness. | Biến tri thức ngầm trong Slack thành nguồn tri thức có thể tra cứu. |
| Cần câu trả lời ngắn gọn, đúng ngữ cảnh | Dùng retrieval + context compression + prompt trả lời ngắn kèm citation. | Groundedness, citation accuracy, user satisfaction. | Nhân viên nhận câu trả lời dùng được ngay thay vì đọc nhiều tài liệu dài. |
| Phải kiểm soát quyền truy cập | Permission-aware retrieval: filter theo department, role, sensitivity level trước khi đưa context vào LLM. | Access control violation rate. | Tránh rò rỉ thông tin quản lý hoặc tài liệu nhạy cảm. |
| Ưu tiên ổn định, chi phí thấp, cập nhật hằng ngày | Dùng daily batch indexing, caching, model nhỏ/rẻ cho query thông thường. | Cost/query, latency, daily sync success rate. | Đáp ứng nhu cầu thực tế mà không cần hệ thống real-time đắt tiền. |

**Abstract Workflow:**  
Daily sync Wiki/Slack -> Clean & summarize Slack -> Chunk + metadata/permission -> Index vector + keyword -> User query -> Permission filter -> Retrieve/Fusion context -> Generate concise answer + sources -> Feedback/logging

**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP |
|---|---|---|
| 1. Daily sync data | Lấy dữ liệu nội bộ định kỳ. | Kết nối Wiki/SOP/Slack, chạy batch mỗi ngày, lưu raw data và updated timestamp. |
| 2. Clean Slack data | Giảm noise từ hội thoại. | Gom thread, bỏ emoji/noise, tóm tắt thread dài thành topic + decision + action items. |
| 3. Chunk documents | Tạo đơn vị retrieval tốt. | Wiki/SOP chunk theo heading; Slack chunk theo thread/topic. |
| 4. Add permission metadata | Bảo vệ quyền truy cập. | Gắn metadata: department, role, channel, owner, sensitivity level, allowed groups. |
| 5. Index data | Tìm kiếm nhanh và chính xác. | Dùng vector DB + BM25/full-text để hỗ trợ cả semantic search và keyword search. |
| 6. Permission-aware retrieval | Chỉ retrieve dữ liệu user được phép xem. | Trước retrieval hoặc trong retrieval filter theo user role/department/group. |
| 7. Generate answer | Trả lời ngắn gọn có nguồn. | LLM sinh câu trả lời ngắn, kèm link Wiki/Slack source, nêu không chắc nếu thiếu bằng chứng. |
| 8. Feedback/logging | Cải thiện chất lượng. | Cho user rate answer, báo sai nguồn, log query không trả lời được để bổ sung tri thức. |

**MVP Scope and Tradeoffs:**  
MVP nên giới hạn ở vài Wiki space và Slack channel quan trọng, ví dụ engineering SOP và support runbook. Tạm hoãn real-time sync và personalization phức tạp. Tradeoff chính là **freshness của dữ liệu vs chi phí vận hành và độ ổn định**.