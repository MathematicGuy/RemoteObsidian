# Hướng Dẫn Xác Định Bài Toán AI

> Mục tiêu: biến một ý tưởng mơ hồ kiểu “làm AI cho vấn đề X” thành một bài toán rõ ràng, có workflow, có dữ liệu, có metric, có ranh giới rủi ro, và có quyết định **Go / Not Yet / No-Go**.

---

## 0. Tinh thần cốt lõi

AI không phải điểm bắt đầu. AI là một lựa chọn sau khi bài toán đã được hiểu đủ rõ.

Một bài toán AI tốt không bắt đầu bằng:

> “Dùng chatbot được không?”  
> “Có nên làm AI Agent không?”  
> “Có thể dùng LLM để tự động hóa không?”

Nó bắt đầu bằng:

> “Ai đang đau?”  
> “Họ đang làm việc gì?”  
> “Bước nào trong workflow đang nghẽn?”  
> “Thiệt hại đo được là gì?”  
> “Dữ liệu có đủ không?”  
> “Nếu AI sai thì chuyện gì xảy ra?”

Seed điều hành:

> **Problem first. AI second.**

---

# 1. Đầu ra cuối cùng cần có

Sau khi phân tích, bạn cần tạo ra 5 artifact chính:

1. **Problem Scan**  
   Danh sách nhiều vấn đề tiềm năng, chưa vội chọn giải pháp.

2. **Problem Card**  
   Mô tả ngắn gọn một candidate problem đủ rõ để pitch và bị phản biện.

3. **Workflow Before / After**  
   Quy trình hiện tại và quy trình tương lai có AI hoặc tự động hóa.

4. **Problem Statement v1**  
   Bản phát biểu bài toán đã qua validation, có metric và boundary.

5. **Decision**  
   Kết luận: **Go / Not Yet / No-Go**, kèm lý do.

Nếu không có 5 artifact này, bạn chưa thực sự “xác định bài toán AI”. Bạn mới chỉ đang có một ý tưởng.

---

# 2. Quy trình tổng thể

```text
Scan rộng vấn đề
→ Chọn top candidates
→ Viết Problem Card
→ Vẽ current workflow
→ Xác định bottleneck
→ Validate pain
→ Research solution hiện có
→ Vẽ future workflow
→ Xác định AI intervention point
→ So sánh No AI / Rule / Workflow / Agent
→ Viết Problem Statement v1
→ Quyết định Go / Not Yet / No-Go
```

Luồng tư duy đúng:

```text
Pain thật
→ Workflow thật
→ Bottleneck thật
→ Metric thật
→ Data thật
→ Risk thật
→ AI nếu cần
```

Luồng sai:

```text
AI trend
→ Demo nhanh
→ Gán đại một user
→ Viết problem statement cho hợp lý
→ Pitch như thể đã validate
```

---

# 3. Phase 1 — Scan rộng vấn đề

## Mục tiêu

Tìm nhiều vấn đề thực tế trước khi chọn một vấn đề để đào sâu.

Không được bắt đầu bằng giải pháp. Không được viết “làm chatbot cho sinh viên” như một problem. Đó là solution-first.

## 4 lăng kính để scan

| Lăng kính | Câu hỏi cần hỏi | Dấu hiệu tốt |
|---|---|---|
| **Lặp lại** | Việc gì xảy ra hằng ngày, hằng tuần, hằng tháng? | Có tần suất rõ |
| **Tốn thời gian** | Việc gì mỗi lần làm đều mất nhiều công? | Có số phút/giờ cụ thể |
| **AI có thể tốt hơn** | Việc gì cần hiểu ngữ cảnh, ngôn ngữ, phân loại, tổng hợp, suy luận? | Có dữ liệu phi cấu trúc hoặc mơ hồ |
| **Pain từ người khác** | Ai đang phàn nàn, hỏi lại, bỏ sót, hoặc workaround? | Có lời phàn nàn, ticket, chat, survey, log |

## Bảng scan

| #   | Lăng kính | Problem quan sát được | Ai đang đau? | Dấu hiệu thật | Ghi chú |
| --- | --------- | --------------------- | ------------ | ------------- | ------- |
| 1   |           |                       |              |               |         |
| 2   |           |                       |              |               |         |
| 3   |           |                       |              |               |         |
| 4   |           |                       |              |               |         |
| 5   |           |                       |              |               |         |
| 6   |           |                       |              |               |         |
| 7   |           |                       |              |               |         |
| 8   |           |                       |              |               |         |
| 9   |           |                       |              |               |         |
| 10  |           |                       |              |               |         |

## Câu hỏi tự kiểm

- Problem này có người dùng cụ thể không?
- Có xảy ra đủ thường xuyên không?
- Có dấu hiệu thật hay chỉ là cảm giác?
- Có workflow hiện tại để quan sát không?
- Có thể đo được thiệt hại không?
- Nếu không dùng AI thì có cách giải đơn giản hơn không?

Nếu câu trả lời còn mơ hồ, giữ problem trong danh sách scan nhưng chưa chọn làm candidate chính.

---

# 4. Phase 2 — Chọn top candidates

## Mục tiêu

Từ danh sách scan rộng, chọn 3 vấn đề đáng đào sâu nhất.

## Tiêu chí chọn top 3

| Tiêu chí | Câu hỏi kiểm tra |
|---|---|
| Actor rõ | Ai đang chịu pain? Có phải một nhóm cụ thể không? |
| Workflow rõ | Có thể vẽ quy trình hiện tại 3–7 bước không? |
| Bottleneck rõ | Bước nào đang chậm, lỗi, tốn công hoặc gây gián đoạn? |
| Impact đo được | Có thể đo bằng thời gian, chi phí, lỗi, SLA, conversion, chất lượng không? |
| Có data/input | Có tài liệu, log, file, email, form, feedback, transcript, database không? |
| Có thể so sánh solution level | Có thể so sánh No AI / Rule / Workflow / Agent không? |
| Scope vừa đủ | Có thể prototype hoặc validate nhỏ trong vài ngày/tuần không? |

## Bảng chọn top 3

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc | Quick gut |
|---|---|---|---|---|
| 1 | | | | No AI / Rule / Workflow / Agent / Chưa biết |
| 2 | | | | No AI / Rule / Workflow / Agent / Chưa biết |
| 3 | | | | No AI / Rule / Workflow / Agent / Chưa biết |

---

# 5. Phase 3 — Viết Problem Card

Problem Card là bản mô tả đủ ngắn để pitch, nhưng đủ rõ để bị phản biện.

## Template Problem Card

```text
Problem 1 câu:
[Actor] mất [thời gian/chi phí/chất lượng] khi làm [tác vụ] trong [workflow], đặc biệt nghẽn ở [bước nghẽn], dẫn đến [impact].

Actor:
[Ai đang đau?]

Thời điểm / bối cảnh:
[Khi nào vấn đề xảy ra?]

Current workflow 3–7 bước:
1.
2.
3.
4.
5.

Bottleneck:
[Bước nào nghẽn nhất? Vì sao?]

Impact:
[Thiệt hại đo được hoặc ước lượng được]

Success metric:
[Muốn cải thiện chỉ số nào, từ mức nào xuống/lên mức nào?]

Non-AI alternative:
[Nếu không dùng AI, có thể dùng template, rule, dashboard, checklist, training, process fix không?]

AI hypothesis:
[AI có thể hỗ trợ bước nào, output là gì, ai kiểm tra?]

Quick gut:
[No AI / Rule / Workflow / Agent / Chưa biết]
```

## Ví dụ cấu trúc tốt

```text
Mỗi tuần giảng viên mất 120–180 phút để soạn bộ câu hỏi trắc nghiệm từ slide bài giảng, trong đó bước nghĩ đáp án nhiễu chất lượng và định dạng file LMS tốn nhiều thời gian nhất, dẫn đến chậm ra quiz hoặc đề có chất lượng phân loại thấp.
```

Vì sao tốt:

- Có actor: giảng viên.
- Có task: soạn câu hỏi trắc nghiệm.
- Có input: slide bài giảng.
- Có bottleneck: nghĩ distractor và format LMS.
- Có baseline: 120–180 phút.
- Có impact: chậm quiz, chất lượng đề thấp.

## Ví dụ chưa tốt

```text
Làm AI giúp giảng viên tạo đề thi nhanh hơn.
```

Vì sao yếu:

- Không rõ giảng viên nào.
- Không rõ loại đề gì.
- Không có workflow.
- Không có bottleneck.
- Không có baseline.
- Không có rủi ro nếu AI sai.

---

# 6. Phase 4 — Vẽ current workflow

## Mục tiêu

Hiểu quy trình hiện tại trước khi nghĩ giải pháp.

Seed:

> **Workflow reveals the bottleneck.**

Nếu không vẽ workflow, bạn không biết AI nên đứng ở đâu.

## Template current workflow

```text
CURRENT STATE — [tổng thời gian]

[1 Bước đầu: __ phút]
→ [2 Bước tiếp theo: __ phút]
→ [3 Bước tiếp theo: __ phút]
→ [4 Bước nghẽn chính: __ phút]  <-- bottleneck
→ [5 Bước cuối: __ phút]
```

## Bảng workflow chi tiết

| Bước | Actor | Input | Output | Công cụ đang dùng | Thời gian/tần suất | Lỗi/rủi ro | Ghi chú |
|---|---|---|---|---|---:|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

## Câu hỏi cần trả lời

- Bước nào mất nhiều thời gian nhất?
- Bước nào dễ sai nhất?
- Bước nào gây chờ đợi hoặc handoff chậm?
- Bước nào cần judgment của con người?
- Bước nào chỉ là thao tác cơ học?
- Bước nào có dữ liệu đầu vào rõ?
- Bước nào có output đúng/sai rõ?

---

# 7. Phase 5 — Lượng hóa pain point

## Mục tiêu

Chuyển “đau” thành số đo.

Seed:

> **Pain unmeasured is pain imagined.**

Nếu không đo được pain, bạn không chứng minh được giá trị của giải pháp.

## Các loại metric phổ biến

| Loại metric | Ví dụ |
|---|---|
| Thời gian | 120 phút/tuần, 15 phút/ticket, 2 giờ/báo cáo |
| Chi phí | 40 giờ nhân sự/tuần, 10 triệu/tháng |
| Lỗi | 12% form sai, 8% import lỗi, 5 lỗi nghiêm trọng/tháng |
| SLA | 30% request trễ hạn, phản hồi sau 24h |
| Chất lượng | 60% feedback bị đánh giá chung chung |
| Conversion | 20% user bỏ ngang onboarding |
| Rủi ro | Sai sót có thể gây khiếu nại, phạt, mất uy tín |

## Công thức impact cơ bản

```text
Impact = số người bị ảnh hưởng × tần suất × thời gian/cost mỗi lần × mức độ nghiêm trọng
```

Ví dụ:

```text
20 giảng viên × 2 giờ/tuần = 40 giờ/tuần
40 giờ/tuần × 4 tuần = 160 giờ/tháng
```

## Câu hỏi phản biện

- Số liệu này đến từ đâu?
- Là đo thật, phỏng vấn, log, hay ước lượng?
- Có bao nhiêu người xác nhận?
- Có người nào phản bác không?
- Nếu vấn đề được giảm 50%, có đủ đáng làm không?

---

# 8. Phase 6 — Validate pain và research giải pháp hiện có

## 8.1 Quick validation

Không cần validation lớn ngay từ đầu. Nhưng phải có bằng chứng ngoài cảm giác cá nhân.

### Cách validate nhanh

| Phương pháp | Khi dùng | Câu hỏi nên hỏi |
|---|---|---|
| Quick interview | Muốn hiểu sâu workflow | “Lần gần nhất bạn gặp vấn đề này là khi nào?” |
| Micro survey | Muốn biết vấn đề có phổ biến không | “Bạn gặp vấn đề này bao nhiêu lần/tuần?” |
| Log/ticket/review | Có dữ liệu hệ thống | “Có bao nhiêu case lặp lại?” |
| Shadowing/observation | Muốn thấy thao tác thật | “Người dùng thật sự làm từng bước ra sao?” |
| Artifact review | Có file, form, báo cáo, output cũ | “Output hiện tại đang lỗi/chậm/mơ hồ ở đâu?” |

## Bảng validation

| Nguồn | Số mẫu | Tín hiệu xác nhận | Tín hiệu phản bác | Nhóm sửa problem thế nào |
|---|---:|---|---|---|
| Interview | | | | |
| Survey | | | | |
| Log/ticket | | | | |
| Observation | | | | |

## 8.2 Evidence strength

| Mức | Ý nghĩa | Quyết định phù hợp |
|---|---|---|
| Weak | Chỉ là cảm nhận cá nhân | Chưa nên build |
| Medium | 2–5 người xác nhận, workflow tương đối rõ | Có thể làm prototype nhỏ |
| Strong | 10+ người, log/file thật, metric rõ | Có thể MVP |
| Very Strong | Pilot nhỏ có kết quả trước/sau | Có thể pitch đầu tư nghiêm túc |

## 8.3 Research giải pháp đã có

Trước khi build, phải biết ngoài thị trường đã có gì.

| Tool/case/pattern | Họ giải quyết bước nào? | Điểm mạnh | Khoảng trống | Bài học cho mình |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Câu hỏi cần hỏi:

- Đã có tool nào giải quyết vấn đề này chưa?
- Họ giải quyết toàn bộ workflow hay chỉ một bước?
- Họ dùng AI, Rule, Workflow hay Agent?
- Người dùng vẫn còn đau ở đâu?
- Khoảng trống của mình có đủ rõ không?
- Nếu dùng tool có sẵn rẻ hơn, có cần tự build không?

---

# 9. Phase 7 — Vẽ future workflow

## Mục tiêu

Thiết kế quy trình tương lai, trong đó AI chỉ xuất hiện ở đúng bước cần AI.

Không viết:

```text
AI xử lý toàn bộ quy trình.
```

Phải viết:

```text
Bước 2: AI trích xuất thông tin.
Bước 3: Người dùng review.
Bước 4: Rule-based script export file.
```

## Template future workflow

```text
FUTURE STATE — [tổng thời gian kỳ vọng]

[1 Người dùng upload/input: __ phút]
→ [2 Rule/script xử lý phần deterministic: __ phút]
→ [3 AI hỗ trợ phần mơ hồ/ngôn ngữ: __ phút]
→ [4 Human review/edit: __ phút]  <-- boundary
→ [5 Export/gửi/lưu: __ phút]

Fallback:
Nếu AI sai/không chắc/output kém → [quy trình quay về]
```

## Bảng before/after impact

| Metric | Trước | Sau kỳ vọng | Cách đo | Ghi chú |
|---|---:|---:|---|---|
| Tổng thời gian | | | | |
| Số bước thủ công | | | | |
| Tỷ lệ lỗi | | | | |
| Chất lượng output | | | | |
| Tỷ lệ phải sửa lại | | | | |
| Risk mới | | | | |

## Câu hỏi quan trọng

- AI đứng ở bước nào?
- Input của AI là gì?
- Output của AI là gì?
- Ai review output?
- Nếu AI sai, ai phát hiện?
- Nếu AI không chắc, nó có dừng lại không?
- Có fallback thủ công không?
- Có log/audit trail không?

---

# 10. Phase 8 — Chọn mức giải pháp: No AI / Rule / Workflow / Agent

## Nguyên tắc

Không chọn giải pháp phức tạp hơn nếu giải pháp đơn giản hơn đủ dùng.

Seed:

> **Complexity must pay rent.**

Mỗi lớp phức tạp phải chứng minh được giá trị.

## 4 mức giải pháp

### 1. No AI / Process Fix

Dùng khi vấn đề chủ yếu do quy trình, thiếu template, thiếu checklist, thiếu ownership, hoặc thiếu training.

Ví dụ:

- Chuẩn hóa form nhập liệu.
- Viết SOP.
- Làm dashboard.
- Tạo checklist.
- Training người dùng.

Chọn No AI khi:

- Logic rõ.
- Không có dữ liệu phi cấu trúc đáng kể.
- Vấn đề nằm ở quy trình, không nằm ở nhận thức/ngôn ngữ/suy luận.
- AI chỉ làm sản phẩm phức tạp hơn.

### 2. Rule-based

Dùng khi input/output rõ, điều kiện rõ, đúng/sai rõ.

Ví dụ:

```text
Nếu số ngày nghỉ > số ngày phép còn lại → từ chối.
```

Chọn Rule khi:

- Có quy tắc ổn định.
- Không cần hiểu ngữ cảnh sâu.
- Không cần sinh nội dung linh hoạt.
- Rủi ro sai cần kiểm soát chặt.

### 3. Workflow Automation with AI

Dùng khi AI hỗ trợ một hoặc vài bước trong workflow, nhưng con người vẫn kiểm soát quyết định quan trọng.

Ví dụ:

```text
AI đọc email → trích xuất thông tin → điền form → người quản lý duyệt.
```

Chọn Workflow khi:

- Có một bước cần hiểu ngôn ngữ/ngữ cảnh.
- Workflow tổng thể vẫn rõ.
- Cần human-in-the-loop.
- Không cần AI tự lập kế hoạch dài.

### 4. Agentic AI

Dùng khi AI cần tự lập kế hoạch, gọi công cụ, chọn bước tiếp theo, xử lý môi trường thay đổi.

Ví dụ:

```text
AI nhận yêu cầu → kiểm tra lịch → tìm người thay thế → gửi email → cập nhật hệ thống → báo kết quả.
```

Chọn Agent chỉ khi:

- Có nhiều bước phụ thuộc lẫn nhau.
- AI cần quyết định bước tiếp theo.
- Có tool/API rõ.
- Có boundary cực kỳ rõ.
- Có audit, rollback, human override.

## Ma trận quyết định nhanh

| | Độ mơ hồ thấp | Độ mơ hồ cao |
|---|---|---|
| **Độ phức tạp thấp** | Rule / Workflow đơn giản | Workflow có AI hỗ trợ |
| **Độ phức tạp cao** | Workflow điều phối nhiều bước | Agent có thể phù hợp, nhưng phải có boundary mạnh |

## Bảng so sánh solution level

| Mức | Phương án cụ thể | Khi nào đủ | Rủi ro | Chọn? |
|---|---|---|---|---|
| No AI | | | | |
| Rule | | | | |
| Workflow | | | | |
| Agent | | | | |

Câu hỏi bắt buộc:

- Rule có giải được 70–80% case không?
- Nếu Workflow đủ, vì sao cần Agent?
- Nếu Agent sai, ai dừng nó?
- Có thể hạ cấp giải pháp để giảm rủi ro không?

---

# 11. Phase 9 — Thiết kế boundary và fallback

AI Product không chỉ cần output tốt. Nó cần biết khi nào phải dừng.

Seed:

> **Boundary before autonomy.**

## Các loại boundary

| Boundary | Câu hỏi |
|---|---|
| Decision boundary | AI được phép tự quyết gì? Không được quyết gì? |
| Confidence boundary | Khi nào AI phải nói “không chắc”? |
| Human review boundary | Output nào bắt buộc người duyệt? |
| Data boundary | AI được dùng dữ liệu nào? Không được dùng dữ liệu nào? |
| Action boundary | AI được phép ghi/sửa/gửi/xóa gì? |
| Communication boundary | AI được phép nói trực tiếp với user cuối không? |
| Legal/ethical boundary | Sai sót có thể gây hậu quả pháp lý, tài chính, học thuật, sức khỏe không? |

## Template boundary

```text
AI được phép:
-
-

AI không được phép:
-
-

Human-in-the-loop bắt buộc ở bước:
-

Fallback khi AI sai hoặc không chắc:
-

Ai chịu trách nhiệm cuối cùng:
-
```

## Dấu hiệu boundary yếu

- “AI tự động làm hết.”
- “Nếu sai thì người dùng sửa sau.”
- “Chắc model đủ thông minh.”
- “Có thể thêm review sau.”
- “Cứ demo trước đã.”

Nếu thấy các câu này, phải quay lại thiết kế boundary.

---

# 12. Phase 10 — Data và Evaluation Plan

## 12.1 Data readiness

AI cần dữ liệu. Nhưng không phải cứ có dữ liệu là đủ.

| Câu hỏi | Trả lời |
|---|---|
| Dữ liệu nằm ở đâu? | |
| Format là gì? | PDF / Excel / DB / email / chat / image / audio / log |
| Có quyền dùng không? | |
| Có dữ liệu mẫu thật không? | |
| Có nhãn/ground truth không? | |
| Có dữ liệu lỗi/edge case không? | |
| Dữ liệu có nhạy cảm không? | |
| Dữ liệu có cập nhật thường xuyên không? | |

## 12.2 Evaluation Plan

Nếu không đo được AI đúng/sai, không nên tự động hóa nghiêm túc.

| Loại evaluation | Ví dụ |
|---|---|
| Accuracy | Trích xuất đúng bao nhiêu field? |
| Human acceptance rate | Người dùng chấp nhận bao nhiêu % output? |
| Edit distance | Người dùng phải sửa nhiều hay ít? |
| Hallucination rate | Bao nhiêu output bịa hoặc không có nguồn? |
| Citation/source check | Output có trích đúng nguồn không? |
| Format error | File export có lỗi cú pháp không? |
| Latency | Mất bao lâu để trả kết quả? |
| Cost per task | Mỗi lần chạy tốn bao nhiêu tiền? |
| User trust | Người dùng có tin và dùng lại không? |

## Template evaluation

```text
Bộ test ban đầu:
- Số mẫu: ___
- Nguồn mẫu: ___
- Ai đánh giá đúng/sai: ___
- Metric chính: ___
- Ngưỡng pass: ___
- Edge cases: ___
- Cách ghi nhận lỗi: ___
```

Ví dụ:

```text
Với bài toán tạo MCQ:
- 10 slide thật
- 200 câu hỏi AI sinh
- 3 giảng viên đánh giá
- Metric chính: % câu hỏi đúng theo slide, % distractor plausible, % lỗi format GIFT
- Ngưỡng pass: 85% câu hỏi usable sau chỉnh sửa nhẹ, 0 lỗi format import LMS
```

---

# 13. Phase 11 — Viết Problem Statement v1

Problem Statement v1 chỉ được viết sau khi đã có workflow, validation, metric, data, boundary và solution level sơ bộ.

## Template Problem Statement v1

```text
[Actor cụ thể] đang gặp khó khăn khi [thực hiện tác vụ] trong [workflow cụ thể].

Hiện tại, họ phải [mô tả current workflow ngắn], trong đó bước [bottleneck] gây ra [thiệt hại đo được: thời gian/chi phí/lỗi/chất lượng/rủi ro].

Mục tiêu là cải thiện [success metric] từ [baseline] xuống/lên [target], trong khi vẫn đảm bảo [boundary/risk constraint].

Giải pháp phù hợp hiện tại là [No AI / Rule / Workflow / Agent] vì [lý do], với AI chỉ can thiệp tại [AI intervention point] và [human/fallback] chịu trách nhiệm kiểm soát rủi ro.
```

## Bảng Problem Statement v1

| Field | Nội dung |
|---|---|
| Actor | |
| Workflow | |
| Bottleneck | |
| Impact | |
| Baseline | |
| Success metric | |
| Data/input | |
| Non-AI alternative | |
| AI intervention point | |
| Solution level | No AI / Rule / Workflow / Agent |
| Boundary | |
| Fallback | |
| Owner/reviewer | |

---

# 14. Phase 12 — Quyết định Go / Not Yet / No-Go

## GO

Chọn **Go** khi:

- Actor rõ.
- Workflow rõ.
- Bottleneck rõ.
- Pain có bằng chứng.
- Baseline và success metric đo được.
- Dữ liệu có sẵn hoặc có thể lấy nhanh.
- AI có lợi thế rõ so với Rule/Process Fix.
- Rủi ro sai có boundary và fallback.
- Có cách đánh giá output.
- Có owner chịu trách nhiệm.

Nên ghi rõ Go ở mức nào:

```text
Go for prototype
Go for pilot
Go for MVP
Go for full build
```

## NOT YET

Chọn **Not Yet** khi:

- Ý tưởng có tiềm năng nhưng thiếu dữ liệu.
- Workflow chưa đủ rõ.
- Chưa có baseline.
- Chưa biết metric thành công.
- Chưa có evaluation plan.
- Boundary chưa chắc.
- Cần validate thêm với người dùng thật.

Not Yet không phải thất bại. Nó là quyết định đúng khi nền móng chưa đủ.

## NO-GO

Chọn **No-Go** khi:

- Pain không đủ mạnh.
- User không thật sự cần.
- Rule/process fix rẻ hơn và đủ tốt.
- Không có dữ liệu hoặc không được phép dùng dữ liệu.
- Không thể đánh giá đúng/sai.
- AI sai gây hậu quả quá lớn.
- Chi phí vận hành vượt giá trị tạo ra.
- Không có buyer hoặc owner rõ.

No-Go là kết quả tốt nếu nó giúp đội tránh xây sai thứ.

## Decision table

| Câu hỏi | Yes / Not Yet / No | Ghi chú |
|---|---|---|
| Actor và workflow đã rõ chưa? | | |
| Bottleneck có nằm ở một bước cụ thể không? | | |
| Baseline đã đo được chưa? | | |
| Success metric có target rõ không? | | |
| Có dữ liệu/input thật chưa? | | |
| AI có lợi thế hơn Rule/Process Fix không? | | |
| Nếu AI sai, hậu quả có chấp nhận được không? | | |
| Có human review/fallback không? | | |
| Có evaluation plan không? | | |
| Có owner/buyer rõ không? | | |

Decision:

```text
[Go / Not Yet / No-Go]
```

Lý do:

```text

```

Next step:

```text

```

---

# 15. Anti-patterns cần tránh

## 1. Solution-first

Dấu hiệu:

- Bắt đầu bằng “làm chatbot”.
- Bắt đầu bằng “làm agent”.
- Chưa có workflow đã nói architecture.
- Chưa có metric đã nói ROI.

Cách sửa:

> Quay lại Problem Card và current workflow.

## 2. No baseline

Dấu hiệu:

- “Nhanh hơn” nhưng không biết hiện tại mất bao lâu.
- “Chính xác hơn” nhưng không biết hiện tại sai bao nhiêu.
- “Hiệu quả hơn” nhưng không biết hiệu quả đo bằng gì.

Cách sửa:

> Đo hiện trạng trước.

## 3. No evaluation

Dấu hiệu:

- Không có test set.
- Không có ground truth.
- Không có metric AI-specific.
- Không biết hallucination được tính thế nào.

Cách sửa:

> Thiết kế evaluation plan trước khi build.

## 4. No boundary

Dấu hiệu:

- AI được phép tự làm quá nhiều.
- Không có điểm dừng.
- Không có human review.
- Không có fallback.

Cách sửa:

> Xác định AI được phép làm gì, không được phép làm gì, và ai chịu trách nhiệm cuối cùng.

## 5. Fake precision

Dấu hiệu:

- Score 5/5 mọi tiêu chí.
- Không ghi giả định.
- Không ghi tín hiệu phản bác.
- Không ghi rủi ro.

Cách sửa:

> Thêm Evidence Strength, Risk Register và Counter-evidence.

---

# 16. Checklist cuối cùng

Trước khi nói “đây là một bài toán AI tốt”, kiểm tra:

## Problem

- [ ] Actor cụ thể.
- [ ] Pain cụ thể.
- [ ] Tần suất rõ.
- [ ] Impact đo được.
- [ ] Có bằng chứng ngoài cảm giác cá nhân.

## Workflow

- [ ] Current workflow 3–7 bước.
- [ ] Có actor, input, output cho từng bước.
- [ ] Bottleneck rõ.
- [ ] Future workflow rõ.
- [ ] AI intervention point rõ.

## Metric

- [ ] Có baseline.
- [ ] Có target.
- [ ] Có cách đo.
- [ ] Có quality metric, không chỉ time metric.

## AI fit

- [ ] Đã so sánh No AI / Rule / Workflow / Agent.
- [ ] Đã chọn mức đơn giản nhất đủ dùng.
- [ ] AI có lợi thế thật sự.
- [ ] Không chọn Agent chỉ vì nghe “ngầu”.

## Data

- [ ] Có input thật.
- [ ] Có quyền dùng dữ liệu.
- [ ] Có dữ liệu mẫu để test.
- [ ] Có tiêu chí đúng/sai.

## Risk

- [ ] Biết AI sai thì hậu quả là gì.
- [ ] Có human-in-the-loop.
- [ ] Có fallback.
- [ ] Có boundary.
- [ ] Có owner chịu trách nhiệm.

## Decision

- [ ] Go / Not Yet / No-Go rõ.
- [ ] Lý do dựa trên evidence.
- [ ] Next step cụ thể.

---

# 17. Bộ prompt dùng AI đúng cách

## Prompt scan problem

```text
Tôi là [vai trò] trong [bối cảnh].
Công việc hằng tuần của tôi gồm: [mô tả].

Tôi đã tự nghĩ ra các vấn đề sau:
1. ...
2. ...
3. ...

Hãy gợi ý thêm problem theo 4 lăng kính:
- lặp lại
- tốn thời gian
- AI có thể tốt hơn
- pain từ người khác

Với mỗi problem, ghi:
- actor
- workflow sơ bộ
- bottleneck khả nghi
- cách đo impact

Không đưa ý tưởng quá rộng kiểu “xây trợ lý AI toàn năng”.
```

## Prompt phản biện Problem Card

```text
Đây là Problem Card của tôi:
[dán card]

Hãy đóng vai skeptical AI Product Manager.
Chỉ ra điểm yếu, không khen.

Kiểm tra:
1. Actor có đủ cụ thể không?
2. Workflow có thật và vẽ được không?
3. Bottleneck có rõ không?
4. Impact có đo được không?
5. Non-AI alternative có đủ chưa?
6. Tôi có đang nhảy sang AI/Agent quá sớm không?
7. Nếu AI sai thì rủi ro là gì?
```

## Prompt phản biện solution level

```text
Đây là bài toán và workflow của tôi:
[dán workflow]

Hãy so sánh 4 mức giải pháp:
1. No AI / process fix
2. Rule-based
3. Workflow automation with AI
4. Agentic AI

Với mỗi mức, ghi:
- Khi nào đủ
- Vì sao không đủ
- Rủi ro
- Chi phí phức tạp

Kết luận nên chọn mức đơn giản nhất đủ giải quyết bài toán.
```

## Prompt thiết kế evaluation plan

```text
Đây là AI hypothesis của tôi:
[dán AI hypothesis]

Hãy giúp tôi thiết kế Evaluation Plan:
- test set cần bao nhiêu mẫu
- ground truth lấy từ đâu
- metric chính
- metric phụ
- edge cases
- failure modes
- ngưỡng pass/fail
- ai nên đánh giá

Không dùng metric mơ hồ kiểu “tốt hơn” hoặc “thông minh hơn”.
```

## Prompt kiểm tra Go / Not Yet / No-Go

```text
Đây là Problem Statement v1:
[dán PS]

Hãy đóng vai investment committee.
Hãy quyết định Go / Not Yet / No-Go.

Chỉ dùng evidence có trong bài.
Nếu thiếu bằng chứng, ghi rõ thiếu gì.
Không được lạc quan quá mức.
```

---

# 18. Một ví dụ rút gọn

## Problem Card

```text
Mỗi tuần giảng viên mất 120–180 phút để soạn 20 câu hỏi trắc nghiệm từ slide bài giảng, trong đó bước tạo đáp án nhiễu chất lượng và định dạng file LMS tốn nhiều công nhất, dẫn đến chậm ra quiz và chất lượng đề không ổn định.
```

## Current workflow

```text
CURRENT STATE — 120 phút

[1 Đọc slide: 20']
→ [2 Chọn khái niệm kiểm tra: 15']
→ [3 Viết câu hỏi + đáp án đúng: 25']
→ [4 Nghĩ 3 đáp án nhiễu: 40']  <-- bottleneck chính
→ [5 Format Aiken/GIFT: 15']     <-- bottleneck kỹ thuật
→ [6 Upload LMS + test: 5']
```

## Future workflow

```text
FUTURE STATE — 25 phút

[1 Upload slide: 1']
→ [2 AI trích xuất khái niệm + draft câu hỏi: 2']
→ [3 Giảng viên review và chỉnh: 18']  <-- human boundary
→ [4 Rule-based export GIFT/Aiken: 1']
→ [5 Upload LMS + test: 3']

Fallback:
Nếu AI hallucinate hoặc câu hỏi kém → giảng viên bỏ draft và dùng template thủ công.
```

## Solution level

```text
Chọn: Workflow Automation with AI

Vì:
- Rule không đủ để sinh câu hỏi và distractor chất lượng.
- Workflow phù hợp vì AI chỉ draft, giảng viên duyệt.
- Agent quá rủi ro vì không nên để AI tự tạo và upload đề thi chính thức.
```

## Decision

```text
Go for prototype.
Not Yet for full product.

Lý do:
Pain rõ, workflow rõ, baseline rõ, AI có lợi thế ở bước sinh nội dung.
Nhưng cần test chất lượng câu hỏi, hallucination rate, distractor plausibility, và lỗi export LMS trước khi làm MVP.
```

---

# 19. Tóm tắt bằng 8 câu hỏi

Khi gặp bất kỳ ý tưởng AI nào, hãy hỏi theo thứ tự:

1. **Ai đang đau?**
2. **Họ đang làm workflow nào?**
3. **Bước nào nghẽn nhất?**
4. **Pain đo bằng gì?**
5. **Dữ liệu/input có thật không?**
6. **Không dùng AI thì sao?**
7. **Nếu AI sai thì hậu quả là gì?**
8. **Quyết định là Go, Not Yet hay No-Go?**

Nếu chưa trả lời được 8 câu này, chưa nên build.

---

# 20. Seed Vault rút ra từ hướng dẫn

## Problem first. AI second.

Không bắt đầu từ công nghệ. Bắt đầu từ nỗi đau thật.

## Workflow reveals the bottleneck.

Không vẽ workflow thì không biết AI nên đứng ở đâu.

## Pain unmeasured is pain imagined.

Không đo được pain thì không chứng minh được value.

## Baseline before ROI.

Không có hiện trạng thì không thể chứng minh cải thiện.

## Data before intelligence.

Không có dữ liệu đúng, sạch, đủ và được phép dùng thì AI không có nền móng.

## Boundary before autonomy.

Trước khi cho AI tự hành động, phải biết nó được phép làm gì và khi nào phải dừng.

## Complexity must pay rent.

Không chọn Agent nếu Workflow đủ. Không chọn AI nếu Rule đủ.

## Evidence earns investment.

Ý tưởng không được đầu tư vì nghe hay. Nó được đầu tư vì có bằng chứng.

---

# 21. Kết luận

Xác định bài toán AI không phải là tìm chỗ để dùng AI.

Nó là quá trình chứng minh rằng:

- có một nỗi đau thật,
- trong một workflow thật,
- với một bottleneck thật,
- tạo ra một thiệt hại đo được,
- có dữ liệu đủ dùng,
- có rủi ro kiểm soát được,
- và AI thật sự tốt hơn giải pháp đơn giản hơn.

Nếu bài toán sống sót qua các câu hỏi đó, nó đáng prototype.

Nếu không, quyết định tốt nhất có thể là **Not Yet** hoặc **No-Go**.

Một AI Product Analyst giỏi không phải người luôn nói “dùng AI được”.

Một AI Product Analyst giỏi là người biết khi nào **không nên dùng AI**.

