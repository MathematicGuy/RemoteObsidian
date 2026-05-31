# Ví dụ bản nộp — Weekly Report trước và sau AI

> Ví dụ này cho thấy một bài nộp Day 02 hoàn chỉnh trông như thế nào. Không copy nội dung ví dụ; hãy học cách đi từ problem scan → workflow → research → Problem Statement → Rule / Workflow / Agent → quyết định cuối.

Case ví dụ: **Tổng hợp weekly report**

Nhân vật ví dụ: Minh, Junior Product Manager tại một công ty SaaS khoảng 50 người. Mỗi tuần Minh phải tổng hợp số liệu từ Jira, Google Sheets và Slack để viết báo cáo tuần cho Engineering Manager và CEO.

## Vì sao đây là ví dụ tốt?

- Có actor cụ thể.
- Có workflow lặp lại hằng tuần.
- Có bottleneck rõ.
- Có metric thời gian.
- Có thể so sánh Rule / Workflow / Agent.
- Có thể vẽ before/after workflow.

---

# 01 — Individual Problem Scan

## Scan rộng

Minh scan 10 problems, vượt mức tối thiểu 5.

| # | Lăng kính | Problem quan sát được | Ai đang đau? | Dấu hiệu thật |
|---|---|---|---|---|
| 1 | Lặp lại | Mỗi thứ Hai tổng hợp Weekly Report từ Jira, Sheets, Slack | PM, EM, CEO | Mất khoảng 90 phút/tuần |
| 2 | Lặp lại | Copy sprint velocity từ Jira vào slide update | PM | Lặp lại mỗi tuần |
| 3 | Tốn thời gian | Review PRD 10-15 trang trước khi comment | PM reviewer, design lead | 45 phút/bản |
| 4 | Tốn thời gian | Viết meeting notes sau cross-team meeting | PM, team member | 30 phút/buổi |
| 5 | AI có thể tốt hơn | Notion không gợi ý priority theo deadline/context | PM, team member | Task nhiều nhưng priority mơ hồ |
| 6 | AI có thể tốt hơn | Slack search tìm decision cũ rất khó | Cả team | 10-15 phút/lần tìm |
| 7 | Pain từ người khác | Designer phải hỏi lại vì spec từ PM mập mờ | Designer, PM | Hỏi lại 2-3 lần/spec |
| 8 | Pain từ người khác | CEO hỏi update nhưng report chưa sẵn | CEO, PM | Hay bị trễ deadline thứ Hai |
| 9 | Tốn thời gian | Tổng hợp monthly KPI từ nhiều dashboard | PM, manager | Lặp lại mỗi tháng |
| 10 | Lặp lại | Viết standup update mỗi sáng cùng format | PM | 5-10 phút/ngày |

Vì sao phần scan này mạnh:

- Có scan rộng trước khi hội tụ.
- Có nhiều lăng kính khác nhau.
- Mỗi problem có actor và dấu hiệu thật.
- Không bắt đầu bằng "làm chatbot" hoặc "xây agent".

## Top 3

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc |
|---|---|---|---|
| 1 | Weekly Report | Workflow rõ, mất nhiều thời gian, có metric tốt | Narrative "đủ tốt" đo thế nào |
| 2 | Review PRD | Có pain thật, AI có thể giúp đọc/tóm tắt | Quality improvement khó đo |
| 3 | Slack Search | Nhiều người đau, impact rộng | Data access khó, scope có thể quá lớn |

## Problem Card #1 — Weekly Report

**Problem 1 câu:**  
Mỗi thứ Hai PM mất khoảng 90 phút tổng hợp Weekly Report từ nhiều nguồn, trong đó bước viết narrative tốn nhất và dễ trễ deadline.

**Actor:**  
Junior PM chịu trách nhiệm gửi weekly report cho Engineering Manager và CEO.

**Thời điểm / bối cảnh:**  
Thứ Hai hằng tuần, trước buổi leadership sync.

**Current workflow:**

```text
1. Export Jira sprint data
2. Lấy metrics từ Google Sheets
3. Đọc Slack recap tuần
4. Tổng hợp vào Google Docs
5. Viết narrative: insight, highlight, risk, next action
6. Self-review + format
7. Gửi email cho stakeholders
```

**Bottleneck:**  
Bước 5 — viết narrative từ raw data mất khoảng 25 phút và hay bị blank page.

**Impact:**  
90 phút/tuần cho 1 PM. Team có 3 PM nên tổng công sức có thể khoảng 270 phút/tuần. Báo cáo trễ làm leadership thiếu bối cảnh trước buổi sync.

**Success metric:**  
Giảm tổng thời gian từ 90 phút xuống dưới 30 phút, không tăng số câu CEO/EM phải hỏi lại.

**Non-AI alternative:**  
Template report + Jira dashboard + checklist có thể giảm format effort, nhưng chưa giải quyết tốt phần viết narrative.

**AI hypothesis:**  
AI hỗ trợ cấu trúc dữ liệu và draft narrative. PM vẫn review/edit trước khi gửi.

**Quick gut:**  
Workflow.

### Draft current workflow

```text
CURRENT STATE — 90 phút

[1 Export Jira: 10']
→ [2 Lấy metrics: 10']
→ [3 Đọc Slack: 15']
→ [4 Tổng hợp vào Docs: 15']
→ [5 Viết narrative: 25']  <-- bottleneck
→ [6 Review + format: 10']
→ [7 Gửi: 5']
```

### Draft future workflow

```text
FUTURE STATE — 21 phút

[1 Auto-pull data: 2']
→ [2 AI cấu trúc dữ liệu: 1']
→ [3 AI draft narrative: 1']
→ [4 PM review + edit: 15']  <-- human boundary
→ [5 PM gửi: 2']

Fallback: AI draft tệ → PM tự viết lại.
```

## Problem Cards #2 và #3 — tóm tắt

| Card | Actor | Bottleneck | Metric | Quick gut | Vì sao chưa chọn làm #1 |
|---|---|---|---|---|---|
| Review PRD | PM reviewer | Đọc 10-15 trang để hiểu context | 45 phút → 20 phút | Workflow | Quality metric khó hơn |
| Slack Search | Team member | Search keyword rồi đọc thread | 15 phút → dưới 2 phút | Agent / Workflow | Data access và scope rộng |

---

# 02 — Group Problem Statement

## Group convergence

Nhóm 3-4 người, mỗi người share top 3. Tổng cộng khoảng 9-12 candidates.

| Cluster | Candidate examples | Pattern chung |
|---|---|---|
| Báo cáo / tổng hợp thông tin | Weekly Report, meeting recap, lab progress summary | Gom thông tin từ nhiều nguồn rồi viết lại cho người khác đọc |
| Tìm kiếm / hỏi đáp tài liệu | Slack Search, LMS Search, FAQ lab | Tìm đúng thông tin trong nhiều nguồn rời rạc |
| Review / feedback | Review PRD, check Problem Statement, review assignment | Đọc bản nháp và chỉ ra thiếu sót |
| Planning / follow-up | Action item tracking, deadline reminder | Sau cuộc họp/lab có nhiều việc bị rơi |

## Shortlist và score

| Candidate | Actor rõ | Workflow rõ | Pain có evidence | Impact đo được | Làm trong lab | So sánh R/W/A được | Nhóm hiểu domain | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Weekly Report | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 34 |
| Slack Search | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 27 |
| Review PRD | 4 | 5 | 3 | 3 | 5 | 4 | 4 | 28 |

Nhóm chọn: **Weekly Report**.

Vì sao chọn:

- Có workflow rõ nhất.
- Có baseline thời gian.
- Có thể validate nhanh với các PM khác.
- Có thể research các tool/pattern có sẵn.
- Có thể vẽ before/after rất rõ.

Vì sao không chọn các bài khác:

- Slack Search: impact rộng nhưng data access phức tạp, dễ trượt sang hệ thống search/agent quá lớn.
- Review PRD: workflow rõ nhưng quality metric khó thống nhất trong thời gian lab.

## Quick validation

Nhóm hỏi nhanh 3 PM/PO quen biết.

| Nguồn | Số người | Tín hiệu xác nhận | Tín hiệu phản bác | Nhóm sửa problem thế nào |
|---|---:|---|---|---|
| Quick interview | 3 | 2/3 người viết weekly/monthly update thủ công; đều đau ở phần narrative | 1 người nói dashboard đã đủ cho team của họ | Thu hẹp problem: không phải "report automation", mà là "draft narrative từ data có sẵn" |
| Mini poll trong lớp | 6 | 4/6 từng phải tổng hợp report/update từ nhiều nguồn | Một số report không cần AI, chỉ cần template | Thêm non-AI alternative: template + dashboard |

Insight sau validation:

```text
Pain thật không nằm ở việc "lấy số" đơn thuần. Pain nằm ở đoạn biến nhiều nguồn rời rạc thành narrative đủ rõ cho người khác ra quyết định.
```

## Research giải pháp

Nhóm tìm các hướng đã có sẵn, không giả định phải tự build từ đầu.

| Nguồn / tool / case | Link | Họ giải quyết phần nào? | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---|---|---|---|---|---|
| Atlassian Jira Reports | https://www.atlassian.com/software/jira/features/reports | Dashboard/report từ Jira data | Tốt cho số liệu structured | Không tự viết business narrative theo context Slack/Sheets | Rule/dashboard đủ cho bước lấy số, chưa đủ cho narrative |
| Slack AI | https://slack.com/help/articles/25076892548883-Guide-to-Slack-AI | Summary/search trong Slack | Tốt cho recap conversation | Chỉ là một nguồn, không gom toàn bộ Jira/Sheets/Docs | Có thể dùng như input cho workflow, không phải toàn bộ solution |
| Gemini in Drive | https://support.google.com/drive/answer/15141241 | Update/summarize nội dung file | Tốt cho tóm tắt tài liệu | Cần kiểm nguồn, không nên tự gửi output | AI draft cần người thật review |
| Fellow AI Meeting Notes | https://fellow.ai/features/ai | Meeting notes, action items, summaries | Tốt cho recap có cấu trúc | Không trực tiếp giải bài toán Jira/Sheets weekly report | Pattern tốt: AI draft, người thật review |

Research takeaway:

```text
Không nên build một agent tự chạy toàn bộ báo cáo ngay. Hướng hợp lý hơn là Workflow: tự động lấy/cấu trúc dữ liệu ở các bước rõ, dùng AI để draft narrative, PM review trước khi gửi.
```

## Workflow before/after

File nhóm nộp kèm:

```text
02-group-problem-statement-workflow.png/pdf/md
```

Nội dung workflow:

```text
CURRENT STATE — 7 bước, 90 phút

[1 Export Jira: 10']
→ [2 Lấy metrics từ Sheets: 10']
→ [3 Đọc Slack recap: 15']
→ [4 Tổng hợp vào Docs: 15']
→ [5 Viết narrative: 25']  <-- bottleneck
→ [6 Review + format: 10']
→ [7 Gửi email: 5']

FUTURE STATE — 5 bước, 21 phút

[1 Auto-pull Jira/Sheets: 2']  -- Rule/script
→ [2 AI cấu trúc input: 1']    -- Workflow step
→ [3 AI draft narrative: 1']   -- Workflow step
→ [4 PM review + edit: 15']    -- Human boundary
→ [5 PM gửi: 2']

Fallback:
AI draft sai hoặc nhạt → PM bỏ draft và tự viết lại.

Bottleneck mới:
PM review + edit. Đây là bottleneck chấp nhận được vì đó là điểm kiểm soát chất lượng.
```

Before/after impact:

| Metric | Trước | Sau kỳ vọng | Ghi chú |
|---|---:|---:|---|
| Tổng thời gian | 90 phút | Dưới 30 phút | Target chính |
| Số bước | 7 | 5 | Không chỉ giảm bước, mà giảm effort ở bước viết |
| Bước thủ công | 7/7 | 2/5 | PM vẫn review và gửi |
| Bottleneck chính | Viết narrative | Review/edit | Human boundary |
| Risk mới | Không có AI hallucination | Có hallucination risk | Cần review trước khi gửi |

## Problem Statement v0

| Field | Nội dung |
|---|---|
| **Actor** | Junior PM chịu trách nhiệm viết weekly report cho leadership. |
| **Workflow** | Mỗi tuần PM export Jira, lấy metrics từ Sheets, đọc Slack recap, tổng hợp vào Docs, viết narrative, review và gửi email. |
| **Bottleneck** | Bước viết narrative mất khoảng 25 phút vì PM phải tự biến raw data thành insight, highlight, risk và next action. |
| **Impact** | Tổng workflow mất khoảng 90 phút/tuần cho 1 PM; report dễ trễ deadline; leadership thiếu context trước sync. |
| **Success Metric** | Giảm tổng thời gian từ 90 phút xuống dưới 30 phút; không tăng số câu hỏi sửa/hỏi lại từ CEO/EM. |
| **Boundary** | Không tự gửi report; không tự bịa insight; không thay PM quyết định nội dung cuối; chỉ dùng data được cung cấp. |

## Rule / Workflow / Agent

| Mức | Phương án | Khi nào đủ | Rủi ro | Chọn? |
|---|---|---|---|---|
| **Rule** | Template report, auto-pull Jira/Sheets, fixed dashboard | Đủ nếu leadership chỉ cần số liệu | Không giải quyết narrative mỗi tuần khác nhau | Không chọn làm toàn bộ, nhưng dùng cho bước lấy số |
| **Workflow** | Script lấy data → AI cấu trúc → AI draft narrative → PM review | Hợp vì workflow tuyến tính, AI chỉ hỗ trợ vài bước ngôn ngữ | Draft sai/nhạt, cần PM review | Chọn |
| **Agent** | Agent tự lấy nhiều nguồn, phân tích, hỏi thêm, gửi report | Chỉ cần nếu workflow nhiều nhánh, nhiều tool, tự quyết bước tiếp theo | Quá rộng, nhiều permission/risk | Chưa chọn |

Mức chọn:

```text
Workflow.
```

Vì sao:

- Data collection có thể dùng rule/script.
- Narrative cần AI hỗ trợ ngôn ngữ và tổng hợp.
- PM vẫn review nên risk kiểm soát được.
- Chưa cần agent vì workflow không cần tự lập kế hoạch động.

## Problem Statement v1

| Field | Nội dung |
|---|---|
| **Actor** | Junior PM chịu trách nhiệm weekly report cho leadership. |
| **Workflow** | Export Jira → lấy metrics Sheets → đọc Slack → tổng hợp → viết narrative → review → gửi. |
| **Bottleneck** | Viết narrative từ raw data mất 25 phút và dễ trễ deadline. |
| **Impact** | Khoảng 90 phút/tuần/PM; report trễ làm leadership thiếu context. |
| **Success Metric** | Giảm tổng thời gian xuống dưới 30 phút; không tăng số câu hỏi sửa/hỏi lại từ leadership. |
| **Boundary** | AI không tự gửi report, không tự bịa số liệu, không thay PM approve. |
| **AI intervention point** | Sau khi data từ Jira/Sheets/Slack được gom lại, trước bước PM viết narrative. |
| **Mức chọn** | Workflow: rule/script lấy data, AI draft narrative, PM review. |
| **Rủi ro & người thật kiểm tra** | Risk: hallucination, bỏ sót insight, narrative nhạt. Người thật review: PM phải kiểm số liệu và edit trước khi gửi. |

## Final decision

Decision:

```text
Go với scope nhỏ.
```

Pilot nhỏ nhất:

- Dùng data mẫu từ 2 tuần report gần nhất.
- Chạy workflow bán thủ công: PM paste Jira/Sheets/Slack summary vào prompt chuẩn.
- AI draft narrative.
- PM đo thời gian edit và số lỗi phải sửa.

Exit / rollback:

- Nếu PM vẫn phải viết lại hơn 70% draft trong 2 tuần liên tiếp, hạ xuống template + dashboard.
- Nếu AI bịa số liệu hoặc trích sai nguồn, không cho dùng trực tiếp trong report.

Decision rationale:

- Problem rõ, workflow rõ, metric rõ.
- Có non-AI components.
- AI nằm ở một bước cụ thể, không ôm toàn bộ workflow.
- Human review rõ.

---

# 03 — Individual Reflection Example

## Đóng góp của Minh trong nhóm

| Hoạt động | Minh đã làm gì? | Kết quả |
|---|---|---|
| Scan cá nhân | Đưa ra 10 problems | Nhóm có nhiều candidate về reporting/workflow |
| Pitch | Pitch Weekly Report | Bài được vào shortlist |
| Challenge | Hỏi nhóm Slack Search có data access không | Nhóm loại bớt scope quá rộng |
| Workflow | Vẽ current/future workflow weekly report | Nhóm dùng làm workflow bản cuối |
| Research | Tìm Atlassian Jira Reports, Slack AI, Gemini Drive, Fellow | Nhóm thấy không cần build agent từ đầu |
| Rule / Workflow / Agent | Lập luận chọn Workflow, không chọn Agent | Nhóm thống nhất decision |

## Bảng dùng AI trong reflection

| Phase | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai/hời hợt ở đâu? | Tôi sửa gì |
|---|---|---|---|---|
| Scan | Gợi ý thêm problems theo role PM | Giúp nhớ thêm Slack Search, PRD Review | Gợi ý vài ý quá rộng | Bỏ các ý không có workflow thật |
| Workflow | Nhờ AI chuyển mô tả thành Mermaid | Nhanh hơn khi vẽ flow | AI gộp bước viết narrative và review | Tách lại vì bottleneck nằm ở narrative |
| Research | Tìm tool tương tự | Gợi ý Jira, Slack AI, Gemini, Fellow | Có claim tiết kiệm thời gian không nguồn | Chỉ giữ link tool chính thức, không dùng số liệu không verify |
| Problem Statement | Nhờ AI phản biện field mơ hồ | Chỉ ra metric quality yếu | AI đề xuất agent quá sớm | Nhóm hạ về Workflow |

## Bài học của Minh

- Problem tốt không phải problem nghe "AI" nhất, mà là problem có workflow và metric rõ.
- Vẽ workflow giúp thấy phần nào rule đủ, phần nào AI mới có ích.
- Agent không phải đích đến mặc định. Trong case này, Workflow hợp lý hơn vì có đường đi cố định và có PM review.
- Research không phải để copy tool, mà để thấy pattern: nhiều sản phẩm tốt đều để AI draft, người thật review.

Nếu làm lại:

```text
Tôi sẽ validate với nhiều PM hơn trước khi chốt metric 90 phút → 30 phút, vì baseline hiện tại chủ yếu đến từ trải nghiệm của tôi.
```

---

*Ví dụ bản nộp — Day 02 Lab v2*
