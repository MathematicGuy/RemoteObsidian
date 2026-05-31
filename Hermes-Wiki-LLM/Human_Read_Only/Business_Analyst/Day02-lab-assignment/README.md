# Day 02 Lab — Tìm Đúng Bài Toán Cho AI

> Từ vấn đề thật quanh mình → workflow rõ → Problem Statement đủ chặt → chọn Rule / Workflow / Agent → quyết định Go / Not Yet / No-Go.

## Tài liệu trong folder này

Folder này chỉ giữ các file cần thiết:

| File | Dùng để làm gì |
|---|---|
| `01-worksheet.md` | File hướng dẫn chính cho toàn bộ lab 4 tiếng. Bộ gợi ý, hướng dẫn công cụ, prompt và checklist tự kiểm đã được tích hợp trực tiếp vào từng phase. |
| `02-deliverable-example.md` | Ví dụ bài nộp hoàn chỉnh để học viên nhìn được output cuối cùng trông như thế nào. |

## Cấu trúc repo nộp bài

Mỗi học viên nộp **một repo cá nhân**:

```text
Day02-MãHọcViên-HọVàTên/
├── README.md
├── 01-individual-problem-scan/
├── 02-group-problem-statement/
└── 03-individual-reflection/
```

Trong đó:

- `01-individual-problem-scan/`: bài cá nhân, gồm scan 5+ problems, top 3 Problem Cards, draft workflow trước/sau.
- `02-group-problem-statement/`: **bản nộp nhóm**. Nhóm 3-4 người làm chung một bản gồm nhật ký hội tụ, kiểm chứng/research, Problem Statement, Rule / Workflow / Agent, quyết định cuối, workflow trước/sau. Mỗi học viên copy bản cuối vào repo cá nhân của mình.
- `03-individual-reflection/`: reflection cá nhân về AI, vai trò trong nhóm, và bài học sau lab.

Nếu có file phụ như ảnh workflow, Mermaid, survey screenshot, research notes, đặt cùng prefix với phần liên quan:

```text
01-individual-problem-scan-workflow-card-1.png
02-group-problem-statement-workflow.pdf
02-group-problem-statement-research-notes.md
```

## Đọc file nào để làm gì?

1. Mở `02-deliverable-example.md` trước để nhìn một bản nộp tốt trông như thế nào.
2. Làm theo `01-worksheet.md` từ Phase 1 đến Phase 7. Worksheet là hướng dẫn suy nghĩ theo từng bước, không chỉ là form để điền.
3. Khi nộp, repo cá nhân cần có đủ 3 phần: problem scan cá nhân, bản nộp nhóm, reflection cá nhân.

## Tiêu chí đánh giá (100 điểm)

Điểm của mỗi học viên gồm **điểm nhóm 60 điểm** và **điểm cá nhân 40 điểm**. Điểm nhóm là điểm cho bản nộp nhóm; mỗi học viên vẫn copy bản cuối vào repo cá nhân của mình. Bài làm không cần chọn Agent mới được điểm cao. Điểm nằm ở việc nhóm hiểu đúng bài toán, lập luận rõ, biết vì sao nên hoặc không nên dùng AI.

Ngoài 100 điểm chính, học viên có thể có **tối đa +10 điểm bonus**.

### A. Điểm nhóm — 60 điểm

| Thành phần | Điểm | Cần thể hiện rõ |
|---|---:|---|
| Workflow trước/sau | 15 | Vẽ được workflow hiện tại và workflow sau tối ưu. Nhìn ra bước nghẽn, ai làm bước đó, mất bao lâu, bàn giao qua ai, AI hoặc tự động hóa nằm ở bước nào. |
| Problem Statement + metric + boundary | 20 | Problem Statement có người gặp vấn đề, workflow, điểm nghẽn, tác động, success metric và boundary. Metric có hiện trạng ban đầu, mục tiêu sau cải thiện và cách đo, không chỉ viết "nhanh hơn" hoặc "tốt hơn". Boundary nói rõ phạm vi làm và không làm. |
| Độ phù hợp với AI + phương án thay thế | 15 | So sánh được No AI / Rule / Workflow / Agent. Giải thích vì sao chọn mức đó, vì sao không chọn mức còn lại, AI được phép làm gì, phần nào cần người kiểm tra. |
| Chất lượng quyết định | 10 | Quyết định Go / Not Yet / No-Go có lý do dựa trên bằng chứng, research hoặc giả định được ghi rõ. Không quyết định chỉ vì "muốn làm AI". |

### B. Điểm cá nhân — 40 điểm

| Thành phần | Điểm | Cần thể hiện rõ |
|---|---:|---|
| Scan problem + top 3 Problem Cards | 12 | Scan ít nhất 5 problems từ trải nghiệm thật, dùng nhiều lăng kính, có người gặp vấn đề và dấu hiệu thật. Top 3 Problem Cards đủ rõ để pitch với nhóm. |
| Tham gia pitch + challenge | 12 | Pitch vấn đề của mình ngắn gọn, rõ người gặp vấn đề / workflow / điểm nghẽn. Khi nghe bạn khác, có đặt câu hỏi hoặc challenge đúng trọng tâm để giúp nhóm chọn bài tốt hơn. |
| Reflection cá nhân | 10 | Ghi trung thực AI đã hỗ trợ gì, sai/hời hợt ở đâu, mình đã sửa gì bằng nhận định của bản thân. Reflection có nói rõ vai trò, đóng góp của mình trong nhóm, điều học được và nếu làm lại sẽ đổi gì. |
| Kiểm tra hiểu bài cá nhân | 6 | Tự giải thích được mạch problem → workflow → metric → boundary → độ phù hợp với AI. Nếu được hỏi nhanh, trả lời được vì sao nhóm chọn Rule / Workflow / Agent và Go / Not Yet / No-Go. |

### C. Bonus — tối đa +10 điểm

| Phần bonus | Tối đa | Khi nào được cộng |
|---|---:|---|
| Scan rộng hơn yêu cầu | +3 | Có 8-10+ problems cụ thể, đa dạng lăng kính, không phải list dài nhưng chung chung. |
| Tương tác tích cực | +3 | Trả lời câu hỏi thảo luận, gửi bài tập nhanh lên Discord, đặt câu hỏi tốt, hoặc challenge giúp bạn/nhóm làm rõ bài toán hơn. |
| Kiểm chứng / research vượt yêu cầu | +4 | Có phỏng vấn nhanh, survey nhỏ, log thật, nguồn đáng tin cậy, hoặc kiểm chứng giúp nhóm sửa lại problem, metric hoặc quyết định cuối. |

### D. Mức xếp loại

| Mức | Điểm | Ý nghĩa |
|---|---:|---|
| Không pass | < 50 | Bài còn solution-first, chưa nắm được problem, workflow, metric hoặc độ phù hợp với AI. |
| Vừa đủ pass | 50-64 | Có đủ phần cơ bản nhưng nhiều chỗ còn mơ hồ, metric hoặc boundary chưa chắc. |
| Hiểu khá | 65-79 | Làm được đa số yêu cầu, logic tương đối rõ, còn thiếu bằng chứng hoặc so sánh phương án thay thế chưa sâu. |
| Hiểu đầy đủ | 80-89 | Workflow, Problem Statement, độ phù hợp với AI và quyết định cuối nhất quán; metric và boundary rõ. |
| Rất tốt | 90-100 | Bài có bằng chứng tốt, lập luận chặt, biết giới hạn của AI, reflection cá nhân sâu và trung thực. |

## Flow lab 4 tiếng

```text
Phase 0  Worked Example                  15'
Phase 1  Individual Scan                 25'
Phase 2  Top 3 Problem Cards             35'
         Break                            10'
Phase 3  Group Convergence               30'
Phase 4  Validation + Research            30'
Phase 5  Workflow + Problem Statement     45'
         Break                            10'
Phase 6  Rule/Workflow/Agent + Decision   25'
Phase 7  Individual Reflection            15'
```

## Điều quan trọng nhất

- Nhóm **không chọn Problem Statement ngay**. Nhóm chọn một **candidate problem** để đào sâu.
- Problem Statement chỉ được viết sau khi đã validate, research, vẽ workflow và làm metric rõ hơn.
- Rule không kém Agent. Nếu Rule hoặc Workflow giải đúng bài toán với ít rủi ro hơn, đó là lựa chọn tốt.
- AI chỉ hỗ trợ tư duy. Người học vẫn phải tự kiểm nguồn, tự chốt lập luận, tự chịu trách nhiệm với quyết định.

---

*Day 02 Lab v2 — Batch 02*
