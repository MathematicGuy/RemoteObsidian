---
category: "3_RESOURCES/NLP & RAG/Template.md"
summary: "Hướng tiếp cận: Phân tích bài toán => Evaluation Metric => Tạo RAG Framework (Các bước cơ bản của RAG -> ghép Method vô sau) 
Ghép method ntn:
Dựa vào Input (Text, image, bảng hay cả 3) -> Vấn đề. ..."
keywords: []
confidence: "high"
analyzed_at: "2026-06-01T02:22:41.180660+00:00"
---
Hướng tiếp cận: Phân tích bài toán => Evaluation Metric => Tạo RAG Framework (Các bước cơ bản của RAG -> ghép Method vô sau) 
Ghép method ntn:
Dựa vào Input (Text, image, bảng hay cả 3) -> Vấn đề.
Hiểu Method (search hoặc đọc “Best Practices in Retrieval-Augmented Generation” -> ghép vô RAG Framework.
=> Từ Evaluation Metrics chọn Method cho từng Modules trong RAG đáp ứng với Yêu Cầu Đề Bài.

1. Hệ thống hỗ trợ biên soạn học liệu (Giáo dục)
Một trường trung học phổ thông đang tìm cách triển khai hệ thống tự động tạo sinh câu hỏi trắc nghiệm nhằm giảm tải áp lực cho giáo viên. Thách thức lớn nhất nằm ở tính chất đa dạng của học liệu: giáo trình bao gồm các tệp PDF chứa nhiều bảng số liệu kinh tế (table), biểu đồ (graph Image) và công thức phức tạp (math formula). Nhà trường yêu cầu hệ thống phải hiểu sâu nội dung để tạo ra các phương án nhiễu (distractors) thực sự chất lượng, đánh trúng các lỗi tư duy phổ biến thay vì chỉ đưa ra các câu trả lời sai ngẫu nhiên. Tuy nhiên, ngân sách của trường chỉ ở mức trung bình, ưu tiên chi phí vận hành hàng tháng thấp thay vì đầu tư máy chủ đắt tiền. Đặc biệt, hệ thống phải có khả năng mô phỏng chính xác văn phong, cấu trúc câu hỏi và tiêu chuẩn độ khó dựa trên kho lưu trữ đề thi lịch sử của nhà trường.

Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai ?
Dạng đề bài => Open-Ended. 
Vấn đề với đề bài => phải tự xác định độ phức tạp và độ khó của đề -> tự đặt ra Scope của bài toán. 

*Input:* Multimodal Document (image, text, table) - not model, modal
*Output:* MCQs in JSON format.
**Mô tả Phương pháp:** 
**Baseline:** sử dụng multimodal RAG để xử lý multimodal docs và tạo sinh câu trả lời trắc nghiệm. 
**Improve:** sử dụng multimodal RAG để xử lý multimodal docs, chia làm 2 luồng tạo sinh: 
+ Luồng 1 sử dụng Conversational RAG cho phép trò chuyện với RAG đến khi Output Format đạt đúng yêu cầu người dùng.
+ Luồng tạo sinh khi input file PDF.

**RAG Baseline Workflow:**
**Indexing:** Multimodal Document -> Multimodal Chunking -> Multimodal Embedding -> Vector db. 
**Indexing Improve:** add Meta-data.
**Retrieval:** Default Generation Query -> Embedded Query -> Similarity Search (FAISS) -> Retrieved Content/N-document-Chunks 
**Generation baseline (take Retrieved Content):** 
	*Ingestion LLM:* Structure Retrieved Content into JSON format. 
	*LLM Gen:* generate MCQs. 
	*LLM Judge:* evaluate LLM Gen.
**Generation Improve**



**Nêu rõ các bước Triển Khai:**
**Data Ingestion (trích xuất thông tin từ PDF)**
Chọn công cụ OCR phù hợp.
Sử dụng OCR model để trích xuất "Text, Công thức toán, Bảng và Ảnh" và chuyển sang dạng `.md` hoặc `.html`

**Chunking (text):** 
Chunk Text - Document-Structure Based Chunking (Chunk theo cấu trúc của Tài Liệu) 

**Embedding** -> dữ liệu chuyển về Text nên Embedding như bth. 

Retrieval
Vector Database => Milvus (for multimodal documents retrieval)
Multimodal Retriever => method ?

Generation
LLM Gen  - Tạo sinh câu hỏi Trắc Nghiệm.
Có 2 hướng tiếp cận: 
dùng VLM hoặc LLM. VLM thì cứ nhét thẳng ảnh, text và bảng vô (có thể sẽ chậm hơn vì xử lý cả ảnh).
Nếu dùng LLM thì cần chuyển Ảnh -> Text. 
LLM Judge - Đánh giá câu hỏi Trắc Nghiệm đã được tạo sinh.


RAG Baseline:
Evaluation Metrics: 
Check xem sinh ra có đúng Format yêu cầu của người dùng đề ra hay không ? -> AI Judge (Prompt con AI khác để check)
Check đúng format JSON hay không => dùng Regex cho nhanh
Đánh giá MCQs: 
Đánh giá Nội Dung Câu Hỏi gen ra có đúng format không ? 
Đánh giá chất lượng của Câu Hỏi có liên quan tới tài liệu hay ko ? 
Đáp án Gen ra có chính xác so với tài liệu gốc hay không ?
Đánh giá ĐÁP ÁN AI Gen ra 
+ Semantic Similarity (so sánh Embedding của Đáp án với Embedding của các Chunk Truy Vấn) - nếu Retrieve đc nhiều chứng cứ cho đáp án hay không ? 
+ Textual Entailment (Entailment, Contradiction, Neutral) - xác định Đáp Án gen ra  (Text) có liên quan tới Các Chunk (Evidence) đc truy vấn hay không.
+ Nếu LLM thông minh kết hợp với cả Ý Kiến của nó, nhưng điểm trừ là tăng Latency. 

Đo Hallucination (LLM chỉ có Local Knowledge): 
Nếu Hallucination Threshold > 80% thì Tra Google để xác nhận (tăng latency ?) -> có 1 phương pháp gọi là SAFE của google: Nếu nhiều Thông tin Tra cứu ủng hộ thì con AI đúng (khá giống con người).



2. Trợ lý hỗ trợ chẩn đoán và tra cứu phác đồ (Y tế)
Bệnh viện chúng tôi muốn xây dựng một công cụ hỗ trợ bác sĩ ra quyết định lâm sàng dựa trên kho bệnh án khổng lồ hiện có. Hệ thống phải đảm bảo an toàn tuyệt đối, thông tin đưa ra bắt buộc phải có trích dẫn từ các hướng dẫn y khoa chính thống và không được phép sai lệch vì liên quan trực tiếp đến tính mạng bệnh nhân. Do các quy định khắt khe về bảo mật y tế, toàn bộ dữ liệu bệnh nhân không được phép rời khỏi hạ tầng nội bộ của bệnh viện để xử lý ở bên ngoài. Với ngân sách đầu tư ban đầu khiêm tốn, chúng tôi yêu cầu AI phải hiểu được các mối liên hệ phức tạp giữa các chỉ số xét nghiệm dạng bảng biểu (table), kết quả chẩn đoán hình ảnh (image) và các ghi chú lâm sàng của bác sĩ. Bệnh viện chấp nhận việc hệ thống mất vài phút để phân tích, miễn là kết quả cuối cùng đạt độ xác thực và tin cậy cao nhất.
Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai ?



3. Hệ thống rà soát tuân thủ và phân tích rủi ro hợp đồng (Pháp lý)
Phòng pháp chế của một tập đoàn đa quốc gia muốn triển khai hệ thống tự động rà soát các dự thảo hợp đồng dựa trên bộ quy tắc ứng xử nội bộ và luật pháp hiện hành. Các văn bản này thường dài hàng chục trang với ngôn ngữ pháp lý lắt léo và các điều khoản liên kết chéo phức tạp cần được đối soát kỹ lưỡng để tránh các rủi ro mà con người dễ bỏ sót. Mọi quá trình xử lý dữ liệu phải diễn ra hoàn toàn nội bộ (on-premise) để đảm bảo bí mật kinh doanh tuyệt đối. Hệ thống cần đưa ra kết quả nhanh chóng để kịp thời hỗ trợ các luật sư ngay tại bàn đàm phán trực tiếp với đối tác. Tài nguyên hiện có bao gồm kho dữ liệu khổng lồ về các bộ luật, lịch sử các hợp đồng đã ký và các bảng quy định (table) điều khoản mẫu của tập đoàn.
Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai?



4. Hệ thống phân tích và xếp hạng hồ sơ ứng viên (Tuyển dụng)
Tập đoàn chúng tôi đang đối mặt với việc xử lý hàng ngàn hồ sơ ứng viên mỗi đợt tuyển dụng. Các hồ sơ này rất lộn xộn, từ tệp PDF, ảnh chụp cho đến văn bản thô, chứa nhiều định dạng bảng biểu kỹ năng và lịch sử làm việc khác nhau. Chúng tôi cần một giải pháp tự động bóc tách và xếp hạng ứng viên dựa trên mô tả công việc (JD) một cách khách quan nhất, loại bỏ cảm tính cá nhân và phải giải thích được lý do cụ thể tại sao ứng viên đó lại phù hợp. Do số lượng hồ sơ cực lớn, hệ thống cần ưu tiên khả năng xử lý hàng loạt với độ chính xác cao để không bỏ sót những tài năng tiềm năng. Tài nguyên hiện có bao gồm kho CV tích lũy qua nhiều năm và danh sách các tiêu chuẩn chuyên môn khắt khe được cập nhật liên tục.
Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai?




5. Hệ thống tra cứu tri thức nội bộ (Doanh nghiệp Công nghệ)
Chúng tôi muốn xây dựng một cổng thông tin tập trung để nhân viên có thể nhanh chóng tra cứu các quy trình vận hành (SOP) từ kho Wiki và các hướng dẫn kỹ thuật trên Slack. Hiện tại, thông tin bị phân mảnh khiến nhân viên mất nhiều thời gian để tìm được câu trả lời chính xác cho công việc hàng ngày. Hệ thống cần khả năng tổng hợp thông tin từ các đoạn hội thoại hoặc văn bản dài để đưa ra câu trả lời ngắn gọn, đúng ngữ cảnh. Yêu cầu quan trọng là phải đảm bảo quyền truy cập: nhân viên chỉ được thấy những tài liệu phù hợp với phòng ban của mình, không được tiếp cận các thông tin nhạy cảm của cấp quản lý. Chúng tôi ưu tiên một giải pháp ổn định, chi phí vận hành thấp và dữ liệu chỉ cần cập nhật định kỳ mỗi ngày thay vì phải cập nhật tức thời.
Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó, nêu các bước của giải pháp, nêu chi tiết cách triển khai?



