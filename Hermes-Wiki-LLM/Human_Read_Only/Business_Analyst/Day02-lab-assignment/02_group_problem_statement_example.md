# 02 — Group Problem Statement
## Group Convergence

### Bước 3.1 — Trình bày top 3 của từng thành viên

| # | Người đưa ra | Candidate problem | Người gặp vấn đề | Điểm nghẽn | Cảm nhận nhanh |
|---|--------------|-------------------|------------------|------------|----------------|
| 1 | Thanh | Soạn câu hỏi trắc nghiệm (MCQ) từ slide | Giảng viên | Nghĩ đáp án nhiễu (40 phút) + định dạng LMS (15 phút) | Workflow rất rõ, tiết kiệm 120-180 phút/tuần |
| 2 | Thanh | Soạn báo cáo đánh giá chuẩn đầu ra (CLO) | Giảng viên | Tổng hợp điểm theo CLO + viết phân tích | Cuối kỳ rất đau, nhưng chỉ 1-2 lần/học kỳ |
| 3 | Thanh | Trả lời câu hỏi sinh viên lặp lại | Giảng viên | Tìm tài liệu cũ, gõ lại câu trả lời | Hàng ngày, nhưng tác động đơn lẻ nhỏ |
| 4 | Khánh Toàn | Tìm slide/tài liệu lớp cũ | Sinh viên | Tài liệu rải rác email, Drive, chat | Mất 20-30 phút, dễ lấy nhầm file cũ |
| 5 | Khánh Toàn | Tổng hợp ghi chú từ nhiều buổi học | Sinh viên | 2-3 giờ tổng hợp, khó xác định ý chính | Metric "nắm 80% nội dung" mơ hồ |
| 6 | Khánh Toàn | Chuẩn bị bài tập nhóm nhiều nền tảng | Nhóm sinh viên | Input rải rác Discord, Drive, Notion | Mất 60 phút, dễ sót |
| 7 | Hiếu | Đọc & tổng hợp paper nghiên cứu | Researcher | Không note có cấu trúc → đọc lại 60 phút | Chỉ cho researcher, không phổ cập |
| 8 | Hiếu | Theo dõi deadline nhiều môn | Sinh viên | Deadline rải rác nhiều LMS | 15-20 phút/tuần, có thể dùng Rule |
| 9 | Hiếu | Viết update tiến độ cho advisor | Sinh viên NC | Nhớ lại + tổng hợp từ nhiều nguồn (45 phút) | Pattern tổng hợp, nhưng ít người gặp |
| 10 | Anh Quân | Tổng hợp feedback phỏng vấn | HR | Nhiều format (Anh/Việt, note rời) | Data nhạy cảm, khó lấy thật |
| 11 | Anh Quân | Soạn email từ chối ứng viên | HR | Thay tên, vị trí thủ công | Có template là đủ, không cần AI |
| 12 | Chi | Tổng hợp đơn order trưa từ chat | HR/Admin | Lội chat, nhập Excel thủ công (25 phút) | Dễ thực nghiệm, tác động hàng ngày |
| 13 | Chi | Chia tiền, thu tiền, đối chiếu | HR/Admin | Tính ship, check ngân hàng (15-20 phút) | Thất thoát 2-3% |
| 14 | Chi | Nhập menu từ ảnh/link quán mới | HR/Admin | Gõ tay tên món, giá | Mỗi lần đổi quán 10-15 phút |
| 15 | Cường | Tóm tắt paper thành note có cấu trúc | Researcher/Sinh viên | Đọc và tự viết note có cấu trúc (10 phút) | Workflow rõ, tiết kiệm 25-45 phút/paper |
| 16 | Cường | So sánh nhiều paper/method vào bảng luận điểm | Researcher/Sinh viên | Bóc tách và chuẩn hóa thông tin giữa nhiều paper | Rất tốn công khi chuẩn bị literature review |
| 17 | Cường | Truy vết claim, con số và nguồn trích dẫn | Researcher/Sinh viên | Tìm đoạn gốc trong nhiều PDF (5 phút) | Tránh sai lệch lập luận, giá trị kiểm chứng cao |

### Bước 3.2 — Cluster

| Cluster | Candidates included | Pattern chung | Ghi chú |
|---------|---------------------|---------------|----------|
| A — Tạo nội dung mới từ tài liệu có cấu trúc | MCQ từ slide, Báo cáo CLO, Nhập menu từ ảnh | Sinh câu hỏi / báo cáo / data từ input có sẵn | Cần AI sáng tạo nội dung, có tính lặp cao |
| B — Tổng hợp dữ liệu phi cấu trúc từ nhiều nguồn | Trả lời SV lặp, Tổng hợp ghi chú, Tổng hợp paper, Order từ chat, Tóm tắt paper (Cường #15), So sánh nhiều paper (Cường #16) | Gom chat/email/note/paper rải rác → bảng/báo cáo/note có cấu trúc | Pattern phổ biến, workflow tuyến tính, dễ RAG/Rule |
| C — Tìm kiếm / truy xuất thông tin | Tìm slide cũ, Theo dõi deadline, Truy vết claim (Cường #17) | Tìm file/deadline/claim trong nhiều nơi (email, Drive, LMS, PDF) | Có thể giải bằng Rule/Search/RAG đơn giản, không cần AI phức tạp |

Nhóm thảo luận và quyết định chọn Cluster A vì:
- Candidate MCQ có workflow cụ thể nhất.
- Tác động lớn (hàng chục giảng viên x 120 phút/tuần).
- Chưa có công cụ tốt trên thị trường cho giảng viên Việt Nam (hỗ trợ tiếng Việt, bám sát slide).

### Bước 3.3 — Shortlist

| Candidate | Vì sao vào shortlist | Rủi ro / điều chưa rõ |
|-----------|----------------------|------------------------|
| Thanh#1 (MCQ) | Workflow 7 bước rất rõ, metric 120 phút → 25 phút, có thể dùng slide thật của Thanh | AI có sinh đáp án nhiễu chất lượng không? Hallucination? |
| Thanh#2 (CLO) | Rất đau nhưng chỉ 1-2 lần/học kỳ, không phải lặp lại hàng tuần | Cần tích hợp LMS để lấy điểm chi tiết, phức tạp |
| Chi#12 (order) | Dễ demo, ai cũng hiểu | Tác động chỉ 1 người/ngày, không scale bằng MCQ |

### Bước 3.4 — Score để đồng thuận

| Candidate | Actor rõ | Workflow rõ | Pain có evidence | Impact đo được | Làm trong lab | So sánh R/W/A | Nhóm hiểu domain | Tổng |
|-----------|----------|-------------|------------------|----------------|----------------|---------------|------------------|------|
| Thanh#1 (MCQ) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 35 |
| Chi#12 (order) | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 32 |
| Hiếu#1 (paper) | 4 | 5 | 4 | 3 | 4 | 5 | 4 | 29 |
| Anh Quân#10 (feedback) | 5 | 5 | 4 | 4 | 3 | 5 | 4 | 30 |

**Candidate nhóm chọn: Thanh#1 — Soạn câu hỏi trắc nghiệm (MCQ) từ slide bài giảng**

**Vì sao chọn:**  
- Có workflow rõ nhất (6 bước, baseline 120 phút cho 20 câu).  
- Có baseline thời gian đo được, metric thành công cụ thể.  
- Có thể validate nhanh với giảng viên thật (Thanh có mạng lưới đồng nghiệp).  
- Có thể research các tool/pattern có sẵn (Quizizz AI, ChatGPT, GIFT format).  
- Có thể vẽ before/after workflow rất rõ, bottleneck nằm ở 1-2 bước cụ thể.

**Nếu có disagreement, nhóm xử lý thế nào:**  
Chi ban đầu bảo vệ bài order vì dễ demo. Thanh trình bày lại về scale impact: 40 phút/ngày x 1 HR = ~3h/tuần, trong khi 120 phút/tuần x 20 giảng viên = 40h/tuần. Hiếu và Khánh Toàn đồng tình với phép tính này. Anh Quân trung lập. Chi sau đó chấp nhận vì thấy lý do về impact và tính khả thi pilot rõ ràng hơn.

---

## Quick Validation

| Nguồn | Số người | Tín hiệu xác nhận | Tín hiệu phản bác | Nhóm sửa problem thế nào |
|-------|----------|-------------------|-------------------|--------------------------|
| Quick interview (Thanh phỏng vấn 2 giảng viên) | 2 | Cả 2 đều soạn MCQ thủ công, mất 2-3 giờ/bộ. Đau nhất là nghĩ đáp án nhiễu. | 1 người nói "dùng ngân hàng đề cũ là đủ". | Thu hẹp: AI dùng để draft nhanh từ slide mới, không thay hoàn toàn ngân hàng đề cũ. |
| Mini poll trong lớp (Khánh Toàn poll sinh viên sư phạm) | 8 | 7/8 từng thấy giảng viên vất vả ra đề; 5/8 muốn có tool hỗ trợ giảng viên. | 1 nói "có AI thì giảng viên lười đi". | Không phản bác nghiêm túc, giữ nguyên problem. Bổ sung boundary: AI chỉ draft, giảng viên duyệt cuối. |
| Research competitor (Nhóm tìm tool hiện có) | 3 tools | Quizizz AI, ChatGPT đều có tính năng sinh câu hỏi. | Không tool nào xuất được file GIFT chuẩn cho Moodle + sinh đáp án nhiễu chất lượng. | Xác nhận khoảng trống: cần workflow kết hợp AI draft + rule export + human review. |

**Insight sau validation:**  
Pain thật không nằm ở việc "viết câu hỏi" đơn thuần. Pain nằm ở đoạn biến khái niệm trong slide thành đáp án nhiễu chất lượng — bước đòi hỏi sáng tạo nhưng lại tốn 40/120 phút. Các tool hiện có hoặc quá đơn giản (Quizizz) hoặc quá mở (ChatGPT), chưa có giải pháp "AI draft + human review + export chuẩn" cho giảng viên Việt Nam.

---

## Research giải pháp

| Nguồn / tool / case | Link | Họ giải quyết phần nào? | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---------------------|------|-------------------------|-----------|----------------------|-----------------|
| Quizizz AI | https://quizizz.com | Tạo câu hỏi từ văn bản/PDF | Nhanh, giao diện đẹp, có sẵn | Câu hỏi đơn giản, đáp án nhiễu sơ sài; không xuất file GIFT/Aiken cho Moodle | Cần thêm tính năng export định dạng chuẩn LMS |
| ChatGPT + prompt engineering | (phổ biến) | Sinh câu hỏi từ slide text | Linh hoạt, rẻ, tùy chỉnh được đáp án nhiễu | Không tự định dạng LMS; dễ hallucination (sinh kiến thức sai) | Pattern an toàn: AI draft + người review + rule export |
| Moodle GIFT format | https://docs.moodle.org | Nhập đề hàng loạt vào LMS | Chuẩn, được Moodle hỗ trợ rộng rãi | Giảng viên ngại học cú pháp, hay sai format thủ công | Có thể dùng rule-based để sinh GIFT từ output AI |
| ReAct pattern | (nghiên cứu AI) | Vòng lặp thảo luận AI ↔ người dùng | Cho phép tinh chỉnh liên tục, nâng cao chất lượng draft | Cần thiết kế prompt cẩn thận, dễ lạc hướng nếu không có boundary | Áp dụng vòng lặp ReAct để giảng viên và AI cùng "bàn" ra đề |

**Research takeaway:**  
Không nên build một agent tự chạy toàn bộ quy trình ra đề ngay. Hướng hợp lý hơn là Workflow: AI draft câu hỏi + đáp án nhiễu → giảng viên review và feedback qua vòng lặp ReAct → rule-based export ra file GIFT. Pattern "AI draft, người thật review" xuất hiện trong hầu hết tool tốt, và phù hợp với bài toán có human-in-the-loop như ra đề thi.

---

## Workflow Before/After

### CURRENT STATE — 6 bước, khoảng 120 phút

| Bước | Actor | Input | Output | Thời gian | Bottleneck |
|------|-------|-------|--------|-----------|------------|
| 1 | Giảng viên | Slide bài giảng (10-20 trang) | Nội dung đã đọc | 20 phút | - |
| 2 | Giảng viên | Nội dung slide | Danh sách khái niệm cần kiểm tra | 15 phút | - |
| 3 | Giảng viên | Khái niệm | Câu hỏi (stem) + đáp án đúng | 25 phút | - |
| 4 | Giảng viên | Câu hỏi | 3 đáp án nhiễu (distractors) | 40 phút | Bottleneck chính |
| 5 | Giảng viên | Bộ 4 đáp án | File định dạng Aiken/GIFT | 15 phút | Bottleneck kỹ thuật |
| 6 | Giảng viên | File GIFT | Đề đã upload LMS | 5 phút | - |

### FUTURE STATE — 5 bước, khoảng 22 phút

| Bước | Actor | Xử lý bởi | Input | Output | Thời gian |
|------|-------|-----------|-------|--------|-----------|
| 1 | Giảng viên | Thủ công | Upload slide (PDF/PPT) | File slide | 1 phút |
| 2 | Hệ thống | AI | Slide | Trích xuất khái niệm + draft câu hỏi + đáp án nhiễu (v1) | 2 phút |
| 3 | Giảng viên & AI | Vòng lặp ReAct | Draft v1 | Giảng viên góp ý, AI sửa → draft v2, v3… | 15 phút (tối đa 3 vòng) |
| 4 | Hệ thống | Rule | Bộ câu hỏi đã duyệt | Xuất file GIFT/Aiken | 1 phút |
| 5 | Giảng viên | Thủ công | File GIFT | Upload LMS, test nhanh | 3 phút |

**Fallback:** Nếu sau 3 vòng ReAct AI vẫn sinh sai kiến thức hoặc giảng viên không hài lòng → giảng viên tự viết thủ công bằng template Word.

**Bottleneck mới:** Review + edit. Đây là bottleneck chấp nhận được vì đó là điểm kiểm soát chất lượng.

### Before/after impact

| Metric | Trước | Sau kỳ vọng | Ghi chú |
|--------|-------|-------------|---------|
| Tổng thời gian | 120 phút | Dưới 30 phút | Target chính |
| Số bước | 6 | 5 | Giảm effort ở bước viết đáp án nhiễu |
| Bước thủ công | 6/6 | 2/5 | Giảng viên vẫn review và upload |
| Bottleneck chính | Nghĩ đáp án nhiễu (40 phút) | Review/edit qua ReAct (15 phút) | Human boundary |
| Risk mới | Không có | Có hallucination risk | Cần review trước khi export |

---

## Problem Statement v0

| Field | Nội dung |
|-------|----------|
| Actor | Giảng viên đại học phụ trách môn lý thuyết, cần ra đề trắc nghiệm định kỳ (tuần hoặc cuối kỳ). |
| Workflow | Đọc slide → xác định khái niệm → viết câu hỏi + đáp án đúng → nghĩ đáp án nhiễu → định dạng GIFT → upload LMS. |
| Bottleneck | Bước nghĩ đáp án nhiễu mất khoảng 40 phút vì giảng viên phải tự biến khái niệm thành các lựa chọn "gây nhiễu" hợp lý nhưng vẫn sai. |
| Impact | Tổng workflow mất khoảng 120 phút/tuần cho 1 giảng viên; một khoa 20 người → 40-60 giờ/tuần; đề thi chất lượng kém ảnh hưởng đến phân loại sinh viên. |
| Success Metric | Giảm tổng thời gian từ 120 phút xuống dưới 30 phút; 0 lỗi định dạng GIFT khi import LMS; giảng viên đánh giá đáp án nhiễu "tốt" (Likert ≥4/5). |
| Boundary | Không tự duyệt câu hỏi; không tự upload LMS; không thay giảng viên quyết định nội dung cuối; chỉ dùng data từ slide được cung cấp. |

---

## Rule / Workflow / Agent

| Mức | Phương án | Khi nào đủ | Rủi ro | Chọn? |
|-----|-----------|------------|--------|-------|
| Rule | Template câu hỏi cố định, auto-fill khái niệm từ slide, fixed format GIFT | Đủ nếu chỉ cần format, không cần sinh nội dung mới | Không giải quyết bottleneck "nghĩ đáp án nhiễu" | Không chọn làm toàn bộ, nhưng dùng cho bước export GIFT |
| Workflow | Script trích xuất khái niệm → AI draft câu hỏi + đáp án nhiễu → Giảng viên review qua ReAct → Rule export GIFT | Hợp vì workflow tuyến tính, AI chỉ hỗ trợ bước ngôn ngữ/sáng tạo | Draft sai/nhạt, cần giảng viên review kỹ | Chọn |
| Agent | Agent tự đọc slide, tự chọn khái niệm, tự sinh đề, tự đánh giá chất lượng, tự upload LMS | Chỉ cần nếu workflow nhiều nhánh, cần tự quyết định bước tiếp theo | Quá rộng, khó kiểm soát chất lượng đề thi, rủi ro hallucination cao | Chưa chọn |

**Mức chọn: Workflow**

**Vì sao:**  
- Data extraction (trích khái niệm từ slide) có thể dùng rule/script đơn giản.  
- Narrative generation (sinh đáp án nhiễu) cần AI hỗ trợ ngôn ngữ và sáng tạo.  
- Giảng viên vẫn review nên risk kiểm soát được.  
- Chưa cần agent vì workflow không cần tự lập kế hoạch động.

---

## Problem Statement v1

| Field | Nội dung |
|-------|----------|
| Actor | Giảng viên đại học phụ trách môn lý thuyết. |
| Workflow | Upload slide → AI trích xuất khái niệm + draft câu hỏi + đáp án nhiễu (v1) → Vòng lặp ReAct (GV feedback, AI sửa) → GV duyệt → Rule xuất GIFT → upload LMS. |
| Bottleneck | Viết đáp án nhiễu từ khái niệm mất 40 phút và dễ trễ deadline soạn đề. |
| Impact | Khoảng 120 phút/tuần/giảng viên; khoa 20 người → 40-60 giờ/tuần; đề thi kém chất lượng ảnh hưởng đánh giá sinh viên. |
| Success Metric | Giảm tổng thời gian xuống dưới 30 phút; 0 lỗi format GIFT; giảng viên đánh giá đáp án nhiễu "tốt" (Likert ≥4/5) sau tối đa 3 vòng chỉnh sửa. |
| Boundary | AI không tự duyệt câu hỏi, không tự upload LMS, không thay giảng viên approve nội dung cuối. |
| AI intervention point | Sau khi slide được upload và trích xuất khái niệm, trước bước giảng viên viết đáp án nhiễu. |
| Mức chọn | Workflow: rule/script trích xuất data, AI draft narrative, giảng viên review. |
| Rủi ro & người thật kiểm tra | Risk: hallucination, đáp án nhiễu sai kiến thức, narrative nhạt. Người thật review: giảng viên phải kiểm kiến thức và edit trước khi export. |

---

## Final Decision

| Câu hỏi | Yes / Not Yet / No | Ghi chú |
|---------|-------------------|----------|
| Actor và workflow đã rõ chưa? | Yes | - |
| Baseline và success metric đã đo được chưa? | Yes | 120 phút → 30 phút |
| Có data/input đủ dùng chưa? | Yes | Slide thật của Thanh |
| Nếu AI sai, hậu quả có chấp nhận được không? | Yes | Giảng viên phát hiện qua vòng lặp, không gây hại trực tiếp |
| Có người review/owner vận hành không? | Yes | Chính giảng viên |
| Có cách non-AI đơn giản hơn không? | Not Yet | Ngân hàng đề cũ không bám sát slide mới |

**Decision: Go**

**Lý do:** Problem rõ, workflow rõ, metric rõ. Có non-AI components (rule export GIFT, human review). AI nằm ở một bước cụ thể (draft đáp án nhiễu), không ôm toàn bộ workflow. Human review rõ qua vòng lặp ReAct. Pilot khả thi ngay với slide thật, không cần data nhạy cảm.

**Pilot nhỏ nhất:**  
1. Lấy 1 slide bài giảng (khoảng 10-15 trang, môn lý thuyết).  
2. Chạy workflow bán thủ công: paste nội dung slide vào prompt ReAct chuẩn.  
3. AI sinh 5 câu hỏi + đáp án nhiễu (draft v1).  
4. Nhập feedback ("câu 2 đáp án nhiễu C quá dễ", "câu 4 nên hỏi về ứng dụng").  
5. AI sửa theo feedback, ra v2. Lặp tối đa 3 vòng.  
6. Đo thời gian thực tế (từ lúc upload slide đến lúc có file GIFT đạt yêu cầu).  
7. Đánh giá chất lượng: chấm điểm đáp án nhiễu (1-5).

**Exit / rollback:**  
- Nếu giảng viên vẫn phải viết lại hơn 70% draft trong 2 lần pilot liên tiếp, hạ xuống template + manual.  
- Nếu AI bịa kiến thức hoặc sinh đáp án nhiễu sai sự thật, không cho dùng trực tiếp trong đề thi.

---

