---
category: "3_RESOURCES/Computer Vision/Example AI System Answers.md"
summary: "Dựa trên câu hỏi thiết kế 1 hệ thống AI để trả lời câu hỏi dưới đây theo format sau:
### Question
Hệ thống hỗ trợ biên soạn học liệu (Giáo dục)
Một trường trung học phổ thông đang tìm cách triển kh..."
keywords: []
confidence: "high"
analyzed_at: "2026-06-01T02:22:41.069997+00:00"
---
Dựa trên câu hỏi thiết kế 1 hệ thống AI để trả lời câu hỏi dưới đây theo format sau:
### Question
Hệ thống hỗ trợ biên soạn học liệu (Giáo dục)
Một trường trung học phổ thông đang tìm cách triển khai hệ thống tự động tạo sinh câu hỏi trắc nghiệm nhằm giảm tải áp lực cho giáo viên. Thách thức lớn nhất nằm ở tính chất đa dạng của học liệu: giáo trình bao gồm các tệp PDF chứa nhiều bảng số liệu kinh tế (table), biểu đồ (graph Image) và công thức phức tạp (math formula). Nhà trường yêu cầu hệ thống phải hiểu sâu nội dung để tạo ra các phương án nhiễu (distractors) thực sự chất lượng, đánh trúng các lỗi tư duy phổ biến thay vì chỉ đưa ra các câu trả lời sai ngẫu nhiên. Tuy nhiên, ngân sách của trường chỉ ở mức trung bình, ưu tiên chi phí vận hành hàng tháng thấp thay vì đầu tư máy chủ đắt tiền. Đặc biệt, hệ thống phải có khả năng mô phỏng chính xác văn phong, cấu trúc câu hỏi và tiêu chuẩn độ khó dựa trên kho lưu trữ đề thi lịch sử của nhà trường. Trong thời hạn 3 tháng, hãy thiết kế 1 MVP (Minimal Viable Product).

Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai ?

### AI System Answer Format Example:
```md
**Solution:**  
[Thiết kế hệ thống ngắn gọn] - giải quyết [vấn đề chính]. Chọn [RAG type] vì [lý do chính: dữ liệu/phạm vi/rủi ro/chi phí].

**Analyze Business Question:**

| Business Problem | Solution / Approach | Evaluation Criteria | Business POV |
|---|---|---|---|
| Vấn đề 1 | Giải pháp 1 | Tiêu chí đánh giá 1 | Vì sao giải pháp này có giá trị cho doanh nghiệp |
| Vấn đề 2 | Giải pháp 2 | Tiêu chí đánh giá 2 | Vì sao giải pháp này phù hợp business |
| Vấn đề N | Giải pháp N | Tiêu chí đánh giá N | Vì sao chọn giải pháp này |

**Abstract Workflow:**  
Step 1 -> Step 2 -> Step 3 -> Step N

**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP |
|---|---|---|
| 1. [Step name] | [Step này giải quyết vấn đề gì] | [Cách triển khai ngắn gọn] |
| 2. [Step name] | [Mục tiêu] | [Cách triển khai MVP] |
| 3. [Step name] | [Mục tiêu] | [Cách triển khai MVP] |

**MVP Scope and Tradeoffs:**  
Trong MVP, ưu tiên [must-have]. Tạm hoãn [nice-to-have]. Tradeoff chính là [quality vs cost / latency / complexity / scope].
```
### Example Answers
**MVP AI System Title:**  Multimodal Fusion RAG MVP for MCQ Generation - hệ thống tạo câu hỏi trắc nghiệm từ PDF giáo trình, bảng, biểu đồ, công thức và đề thi lịch sử. Chọn **Fusion RAG** vì hệ thống cần kết hợp nhiều nguồn tri thức: nội dung học liệu, dữ liệu bảng/biểu đồ/công thức và kho đề thi cũ để mô phỏng văn phong, cấu trúc câu hỏi, độ khó.

**Explain Approaches in 1 paragraph:**  
Cách tiếp cận MVP là xây dựng một hệ thống RAG đa phương thức ở mức vừa đủ dùng trong 3 tháng: ingest PDF giáo trình và đề thi cũ, tách nội dung thành text/table/image/formula, chuyển các phần khó như bảng, biểu đồ và công thức thành mô tả text có cấu trúc, chunk và index dữ liệu, truy xuất nội dung liên quan theo yêu cầu tạo câu hỏi, lấy thêm ví dụ từ đề thi lịch sử để bắt chước văn phong và độ khó, sau đó dùng LLM sinh câu hỏi trắc nghiệm gồm câu hỏi, 4 đáp án, đáp án đúng, giải thích, và lý do vì sao từng distractor là một lỗi tư duy phổ biến. MVP không cố tự train model lớn mà dùng LLM API + retrieval + prompt/rubric kiểm định để giảm chi phí vận hành và triển khai nhanh.

**Explain why you choose this approach in Business POV:**  
Thiết kế này phù hợp với ràng buộc lớn nhất của trường: triển khai MVP trong 3 tháng, ngân sách trung bình, chi phí vận hành thấp, nhưng vẫn cần tạo câu hỏi có chất lượng sư phạm. Nếu xây hệ thống quá phức tạp như fine-tune model lớn, self-GPU, hoặc training model multimodal riêng thì dễ vượt ngân sách và trễ tiến độ. Fusion RAG giúp tận dụng tài liệu sẵn có thay vì huấn luyện model riêng; đề thi lịch sử giúp mô phỏng văn phong và chuẩn độ khó của trường; human-in-the-loop giúp giáo viên kiểm soát chất lượng trước khi sử dụng chính thức. Cách này cân bằng tốt giữa tốc độ triển khai, chi phí, độ chính xác và khả năng mở rộng sau MVP.

**Basic criteria and evaluation metrics:**

| Tiêu chí đánh giá         | Ý nghĩa                                                                 | Metric gợi ý                                                                       |
| ------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Độ đúng nội dung          | Câu hỏi và đáp án có bám sát học liệu không.                            | Factual correctness score, groundedness score, % câu không có lỗi kiến thức.       |
| Chất lượng distractors    | Phương án nhiễu có hợp lý và đánh trúng lỗi tư duy phổ biến không.      | Distractor quality score, teacher acceptance rate, % distractors bị giáo viên sửa. |
| Độ phù hợp văn phong      | Câu hỏi có giống cấu trúc, giọng văn, chuẩn đề thi cũ của trường không. | Style similarity score, teacher rating 1-5.                                        |
| Độ phù hợp độ khó         | Câu hỏi có đúng mức dễ/trung bình/khó theo yêu cầu không.               | Difficulty alignment score, teacher rating, student pilot accuracy rate.           |
| Chất lượng truy xuất      | Context lấy ra có đúng chương/bài/chủ đề không.                         | Recall@k, Precision@k, MRR, context relevance score.                               |
| Khả năng xử lý multimodal | Hệ thống có hiểu được bảng, biểu đồ, công thức không.                   | Table extraction accuracy, chart QA accuracy, formula extraction accuracy.         |
| Tốc độ sử dụng            | Giáo viên có tạo được câu hỏi nhanh hơn không.                          | Time-to-generate, average review time per question.                                |
| Chi phí vận hành          | Có phù hợp ngân sách hàng tháng không.                                  | Cost per generated question, monthly API cost, token usage per request.            |
| Tỷ lệ sử dụng thực tế     | Giáo viên có chấp nhận dùng kết quả không.                              | Acceptance rate, edit rate, reject rate.                                           |

**Abstract Workflow:**  
Upload tài liệu -> Parse PDF theo text/table/image/formula -> Chuẩn hóa thành text có cấu trúc -> Chunk + gắn metadata -> Index vào vector DB + keyword search -> Index đề thi lịch sử -> Nhận yêu cầu tạo câu hỏi -> Retrieve giáo trình + đề thi lịch sử -> Sinh MCQ + distractors -> Tự kiểm định chất lượng -> Giáo viên duyệt -> Lưu feedback


**Explain each step and how to implement it in short**

| Step | Mục tiêu | Cách triển khai MVP | Evaluation metric |
|---|---|---|---|
| 1. Upload tài liệu | Cho trường đưa giáo trình và đề thi cũ vào hệ thống. | Làm web app đơn giản cho upload PDF/DOCX/XLSX/image. Lưu file vào cloud storage hoặc local server. Metadata bắt buộc: môn, lớp, chương, bài, năm học, loại tài liệu. | Upload success rate, % tài liệu có metadata đầy đủ. |
| 2. Parse PDF | Tách nội dung phức tạp khỏi PDF. | Dùng `PyMuPDF` hoặc `Unstructured` để lấy text. Dùng `Camelot/Tabula` cho bảng. Dùng OCR như PaddleOCR/Tesseract cho ảnh. Với công thức, MVP có thể dùng OCR/math parser API nếu ngân sách cho phép. | Text extraction accuracy, table extraction accuracy, OCR accuracy, formula extraction accuracy. |
| 3. Chuẩn hóa nội dung | Biến bảng, biểu đồ, công thức thành dạng LLM hiểu được. | Table -> Markdown table + mô tả xu hướng. Graph image -> caption: trục X/Y, đơn vị, xu hướng, điểm nổi bật. Formula -> LaTeX hoặc text mô tả công thức. | Structured conversion accuracy, % bảng/biểu đồ/công thức dùng được trong generation. |
| 4. Chunk + metadata | Tạo các mảnh kiến thức dễ truy xuất. | Chunk theo chương/bài/mục thay vì cắt token mù. Mỗi chunk có metadata: `subject`, `grade`, `chapter`, `topic`, `content_type`, `source_file`, `page`, `difficulty_hint`. | Chunk relevance score, metadata completeness rate, retrieval precision by topic. |
| 5. Index dữ liệu | Cho phép tìm lại nội dung liên quan nhanh. | Dùng vector DB chi phí thấp như Chroma/Qdrant Cloud/Supabase pgvector. Kết hợp BM25 hoặc full-text search cho từ khóa, số liệu, công thức, thuật ngữ kinh tế. | Recall@k, Precision@k, MRR, query latency. |
| 6. Index đề thi lịch sử | Học phong cách câu hỏi của trường. | Tách đề thi cũ thành từng câu hỏi. Lưu cấu trúc: stem, options, correct answer, difficulty, topic, wording style. Retrieve 3-5 câu mẫu cùng chủ đề/độ khó để làm style examples. | Style retrieval relevance, difficulty label accuracy, % câu mẫu đúng chủ đề. |
| 7. Nhận yêu cầu tạo câu hỏi | Giáo viên chỉ định đầu ra mong muốn. | Form đầu vào gồm: môn, lớp, chương, chủ đề, số câu, độ khó, loại nội dung cần dùng: text/table/graph/formula, số đáp án, có/không lời giải. | Input completion rate, request validation error rate. |
| 8. Retrieve + Fusion context | Lấy cả kiến thức và phong cách đề thi. | Retrieve từ 2 nguồn: giáo trình để lấy kiến thức đúng, đề thi cũ để lấy văn phong và độ khó. Nếu câu hỏi liên quan bảng/biểu đồ, ưu tiên chunks có `content_type = table/graph`. | Context relevance score, source coverage, multimodal retrieval success rate. |
| 9. Sinh MCQ | Tạo câu hỏi trắc nghiệm chất lượng. | Prompt LLM sinh theo schema cố định: câu hỏi, 4 phương án, đáp án đúng, giải thích đáp án, lý do từng distractor sai, misconception mà distractor nhắm tới, nguồn tham chiếu. | Factual correctness, distractor quality score, one-correct-answer rate, schema valid rate. |
| 10. Tự kiểm định chất lượng | Giảm câu hỏi sai hoặc distractor yếu. | Chạy LLM-as-judge hoặc rule checker: kiểm tra chỉ có 1 đáp án đúng, distractors hợp lý, câu hỏi bám context, độ khó đúng yêu cầu, không copy nguyên văn đề cũ. | Pass rate, hallucination rate, duplicate/plagiarism rate, difficulty alignment score. |
| 11. Giáo viên duyệt | Đảm bảo chất lượng sư phạm. | UI cho giáo viên Accept/Edit/Reject. Giáo viên có thể sửa distractor, độ khó, lời giải. | Teacher acceptance rate, edit rate, reject rate, average review time. |
| 12. Lưu feedback | Cải thiện hệ thống theo thời gian. | Lưu câu nào được chấp nhận, chỉnh sửa, từ chối và lý do. Dùng feedback để cải thiện prompt, rubric kiểm định, metadata và retrieval. | Feedback coverage rate, quality improvement over time, repeat error rate. |
