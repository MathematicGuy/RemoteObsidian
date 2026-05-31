# Day 02 Lab — Worksheet

> File này là hướng dẫn chính cho toàn bộ lab 4 tiếng. Bộ gợi ý, hướng dẫn công cụ, prompt mẫu và checklist tự kiểm đã được đặt trực tiếp vào từng phase để bạn không phải nhảy qua nhiều file.

## Nguyên tắc

1. **Problem first, not AI first.** Đừng bắt đầu bằng chatbot/agent. Bắt đầu bằng actor, workflow, bottleneck, metric.
2. **Cá nhân scan rộng, nhóm hội tụ.** Mỗi người chuẩn bị nhiều candidate problems; nhóm chọn một candidate đáng đào sâu.
3. **Vẽ workflow trước khi chọn AI.** Nếu chưa thấy bước nào nghẽn, chưa được chọn Rule / Workflow / Agent.
4. **Không cần AI vẫn là kết luận tốt.** Điểm nằm ở chất lượng lập luận, không nằm ở độ "ngầu" của solution.
5. **AI hỗ trợ, không thay quyết định.** Dùng AI để hỏi ngược, phản biện, vẽ lại, research. Người học tự kiểm và tự chốt.
6. **Tự làm trước, AI sau.** Những phần thể hiện suy nghĩ cá nhân như pitch, challenge và reflection không được để AI viết thay.

## Repo nộp bài

Mỗi học viên nộp một repo cá nhân:

```text
Day02-MãHọcViên-HọVàTên/
├── README.md
├── 01-individual-problem-scan/
├── 02-group-problem-statement/
└── 03-individual-reflection/
```

File phụ như ảnh workflow, Mermaid, survey screenshot, research notes đặt cùng prefix:

```text
01-individual-problem-scan-workflow-card-1.png
02-group-problem-statement-workflow.pdf
02-group-problem-statement-research-notes.md
```

Lưu ý: `02-group-problem-statement/` là **bản nộp nhóm**. Nhóm 3-4 người làm chung một bản cuối, sau đó mỗi học viên copy bản này vào repo cá nhân của mình.

## Output cuối cùng

| Phần | Ai làm | Cần có gì |
|---|---|---|
| `01-individual-problem-scan/` | Cá nhân | 5+ problems, top 3 Problem Cards, draft workflow trước/sau cho top 3 |
| `02-group-problem-statement/` | Nhóm | Nhật ký hội tụ, kiểm chứng nhanh, research giải pháp, workflow trước/sau, Problem Statement v0/v1, Rule / Workflow / Agent, quyết định cuối |
| `03-individual-reflection/` | Cá nhân | Vai trò trong nhóm, cách dùng AI, học được gì, nếu làm lại sẽ đổi gì |

## Tiêu chí đánh giá nhanh

Chi tiết rubric nằm trong `README.md`. Bảng dưới đây giúp bạn biết phần nào đang ảnh hưởng tới điểm khi làm worksheet.

| Nhóm / cá nhân | Thành phần | Điểm |
|---|---|---:|
| Nhóm | Workflow trước/sau | 15 |
| Nhóm | Problem Statement + metric + boundary | 20 |
| Nhóm | Độ phù hợp với AI + phương án thay thế | 15 |
| Nhóm | Chất lượng quyết định Go / Not Yet / No-Go | 10 |
| Cá nhân | Scan problem + top 3 Problem Cards | 12 |
| Cá nhân | Tham gia pitch + challenge | 12 |
| Cá nhân | Reflection cá nhân | 10 |
| Cá nhân | Kiểm tra hiểu bài cá nhân | 6 |

Bonus tối đa +10 điểm:

- +3 nếu scan rộng hơn yêu cầu và vẫn cụ thể.
- +3 nếu tương tác tích cực trên Discord hoặc trong nhóm.
- +4 nếu kiểm chứng/research vượt yêu cầu và giúp nhóm sửa lại problem, metric hoặc quyết định cuối.

## Quy ước dùng AI trong lab

| Phần | Có thể dùng AI không? | Cách dùng đúng |
|---|---|---|
| Scan cá nhân | Có, sau khi tự scan trước | Hỏi thêm góc nhìn, rồi tự chọn ý nào là pain thật. |
| Problem Card | Có | Dùng AI để phản biện, không để AI tự bịa problem thay mình. |
| Pitch + challenge | Không dùng để nói/thay mình | Trình bày và phản biện bằng hiểu biết của bản thân. |
| Research | Có | Dùng AI/search để tìm nguồn, nhưng phải kiểm link và ghi rõ giả định chưa chắc. |
| Workflow | Có | Có thể dùng AI/Mermaid để vẽ lại flow, nhưng phải tự kiểm từng bước. |
| Reflection | Không dùng để viết thay | Có thể dùng AI để gợi ý câu hỏi tự soi, nhưng câu trả lời phải là trải nghiệm thật của mình. |

## Gợi ý công cụ nhanh

| Phase | Tool có thể dùng | Dùng để làm gì | Lưu ý |
|---|---|---|---|
| Phase 1 | ChatGPT / Claude / Gemini, Google, review app/forum | Gợi ý thêm problem nếu bí | Tự scan trước; bỏ ý không có trải nghiệm thật. |
| Phase 2 | ChatGPT / Claude | Phản biện Problem Card | Prompt rõ: "chỉ ra điểm yếu, đừng khen". |
| Phase 4 | Google, Perplexity, tài liệu chính thức, survey/interview nhanh | Kiểm chứng pain, tìm giải pháp đã có | Không dùng số liệu nếu không kiểm được nguồn. |
| Phase 5 | Giấy/bảng, Mermaid, Excalidraw, FigJam | Vẽ workflow trước/sau | Vẽ tay cho rõ tư duy trước, số hóa sau nếu cần nộp đẹp hơn. |
| Phase 6 | ChatGPT / Claude | Hỏi phản biện Rule / Workflow / Agent | Không để AI chốt thay. Nhóm phải tự quyết định. |
| Phase 7 | Không bắt buộc | Chỉ dùng để gợi ý câu hỏi tự soi | Không copy reflection do AI viết. |

---

# Phase 0 — Worked Example (15')

Mở `02-deliverable-example.md` để xem một bài hoàn chỉnh. Khi đọc, chú ý:

- cá nhân scan rộng như thế nào,
- top 3 Problem Cards cụ thể ra sao,
- nhóm hội tụ từ nhiều candidates về một bài như thế nào,
- research giải pháp giúp nhóm tránh nghĩ trong chân không ra sao,
- workflow trước/sau thể hiện bottleneck, boundary và phương án quay về nếu AI sai như thế nào,
- Problem Statement v0/v1 khác nhau ở đâu.

Self-check:

- [ ] Tôi hiểu nhóm chỉ chọn **candidate problem**, không chọn ngay Problem Statement.
- [ ] Tôi hiểu deep-dive gồm validation, research, workflow, metric, PS và AI decision.

---

# Phase 1 — Individual Scan: tìm 5+ problems (25')

## Mục tiêu

Mỗi người scan rộng ít nhất 5 problems từ trải nghiệm thật. Đây là phần phân kỳ cá nhân.

Bonus:

- 8+ problems: bonus nếu vẫn cụ thể.
- 10+ problems: bonus tốt nếu đa dạng lăng kính và có dấu hiệu thật.
- Không bonus cho list dài nhưng toàn ý chung chung.

## 4 lăng kính để scan

Một problem có thể rơi vào nhiều lăng kính. Không cần phân loại hoàn hảo ở bước này. Dùng lăng kính để mở rộng quan sát, rồi bước sau mới filter.

| Lăng kính | Câu hỏi gợi mở | Ví dụ |
|---|---|---|
| **Lặp lại** | Việc gì cứ xuất hiện đều đặn mỗi ngày/tuần/tháng?<br>Nếu phải làm thêm 10 lần nữa, phần nào tôi muốn chuẩn hóa hoặc tự động hóa?<br>Người mới vào có phải hỏi lại cùng một quy trình không? | Báo cáo tuần, nhập liệu, tổng hợp câu hỏi |
| **Tốn thời gian** | Việc gì mỗi lần làm đều nặng, dù không nhất thiết xảy ra thường xuyên?<br>Thời gian mất ở đâu: tìm thông tin, đọc hiểu, tổng hợp, chờ người khác, format, hay sửa lại?<br>Nếu giảm 50% thời gian thì có đáng kể không? | Đọc tài liệu dài, tìm quyết định cũ, review PRD |
| **AI có thể tốt hơn** | Việc gì cần hiểu ngữ cảnh, đọc/viết ngôn ngữ, phân loại, so sánh, tổng hợp hoặc gợi ý đúng lúc?<br>Nếu AI chỉ hỗ trợ một bước trong workflow, bước nào đáng hỗ trợ nhất?<br>Nếu AI sai ở bước đó thì hậu quả là gì? | Search tài liệu, gợi ý next step, tóm tắt nhiều nguồn |
| **Pain từ người khác** | Ai ngoài tôi đang bị kẹt hoặc phàn nàn lặp lại?<br>Họ thường nói câu gì, hỏi lại điều gì, hoặc bỏ sót bước nào?<br>Có dấu hiệu thật không: ticket, Slack/Discord, comment, survey, phản hồi trực tiếp? | Hỏi lại deadline, không hiểu task, support ticket lặp lại |

Cách phân biệt nhanh:

- `Lặp lại` bắt đầu từ câu hỏi: việc này xảy ra bao nhiêu lần?
- `Tốn thời gian` bắt đầu từ câu hỏi: mỗi lần làm tốn bao nhiêu công?
- Một problem vừa lặp lại vừa tốn thời gian thì càng đáng đưa vào danh sách scan.

Nếu bí, tự hỏi:

- Tuần trước tôi mất nhiều thời gian nhất vào việc gì?
- Việc gì tôi hay trì hoãn vì nhàm chán hoặc rối?
- Người khác hay hỏi tôi câu gì lặp lại?
- Có workflow nào ở trường/công ty ai cũng biết là chậm?
- Có app nào tôi dùng và thường nghĩ "giá như nó hiểu mình hơn"?

Một số điểm bắt đầu dễ quan sát:

| Bối cảnh | Có thể nhìn vào đâu? | Câu hỏi gợi mở |
|---|---|---|
| Học tập | Bài tập, tài liệu, deadline, câu hỏi lặp lại trong lớp | Phần nào làm tôi mất thời gian vì phải đọc, tổng hợp, hỏi lại hoặc đoán ý? |
| Công việc / thực tập | Báo cáo, họp, handoff, ticket, review, nhập liệu | Việc nào lặp lại đủ nhiều nhưng vẫn cần hiểu ngữ cảnh trước khi xử lý? |
| Nhóm / CLB / dự án | Phân công, theo dõi tiến độ, feedback, tổng hợp quyết định | Chỗ nào mọi người hay hiểu khác nhau hoặc bỏ sót việc cần làm? |
| Sản phẩm đang dùng | Search, onboarding, support, form, notification | Điểm nào user phải tự nối nhiều thông tin rời rạc để hoàn thành việc? |

## Ngân hàng gợi ý problem

Nếu vẫn bí ý tưởng, đọc nhanh các gợi ý dưới đây rồi quay lại trải nghiệm thật của bạn. Không copy nguyên văn; hãy viết lại theo người dùng, workflow và dấu hiệu thật mà bạn quan sát được.

| Bối cảnh | Gợi ý problem để suy nghĩ |
|---|---|
| Học tập | Tìm lại quyết định/câu trả lời cũ trong Discord; đọc tài liệu dài trước deadline; không biết bài nộp thiếu field nào; ôn tập từ nhiều nguồn rời rạc. |
| Đời sống cá nhân | Theo dõi chi tiêu rải rác nhiều app; lên kế hoạch đi lại/ăn uống cho nhóm; tổng hợp giấy tờ cá nhân; nhắc việc định kỳ nhưng hay quên context. |
| Thực tập / công việc mới | Hỏi lại quy trình onboarding; tìm người phụ trách đúng việc; viết update hằng tuần; hiểu task từ nhiều Slack/thread/tài liệu. |
| Người đi làm | Tổng hợp báo cáo tuần; chuẩn bị meeting recap; review tài liệu dài; phân loại ticket/support; tìm quyết định cũ trước khi làm tiếp. |
| Cải thiện sản phẩm đang dùng | Search kém; onboarding khó hiểu; notification không đúng lúc; form dài và dễ nhập sai; support phải hỏi lại cùng một thông tin nhiều lần. |

## Bảng scan

| # | Lăng kính | Problem quan sát được | Ai đang đau? | Dấu hiệu thật |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

Gợi ý cho `Dấu hiệu thật`: mất bao lâu, xảy ra mấy lần/tuần, bao nhiêu người gặp, có log/ticket/review/comment không, nếu không sửa thì hậu quả là gì.

## Nếu dùng AI ở phase này

Tự scan trước rồi mới hỏi AI.

Prompt gợi ý:

```text
Tôi là [vai trò] trong [bối cảnh].
Công việc hằng tuần gồm: [...]

Tôi đã nghĩ ra các vấn đề sau:
1. [...]
2. [...]
3. [...]

Hãy gợi ý thêm problem theo 4 lăng kính: lặp lại, tốn thời gian, AI có thể tốt hơn, pain từ người khác.
Với mỗi gợi ý, ghi actor, workflow sơ bộ và cách đo.
Đừng đưa ý tưởng quá rộng kiểu "xây trợ lý AI toàn năng".
```

Ghi vào reflection: AI gợi ý gì dùng được, ý nào bị bỏ vì không phải pain thật.

---

# Phase 2 — Top 3 Problem Cards + draft workflow (35')

## Mục tiêu

Từ 5+ problems, mỗi người chọn top 3 để chuẩn bị share với nhóm. Mỗi top problem cần có:

- Problem Card.
- Draft current workflow.
- Draft future workflow.
- Lý do vì sao bài này có impact.

## Chọn top 3

Tiêu chí chọn:

- Actor rõ.
- Workflow hiện tại có thể vẽ được.
- Bottleneck cụ thể.
- Impact có thể đo hoặc ước lượng.
- Có thể so sánh No AI / Rule / Workflow / Agent.
- Không quá rộng cho một buổi lab.

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Problem Card template

Lặp lại template này cho top 3.

Nếu cần một bản nhìn nhanh để pitch với nhóm, dùng dạng card này:

```text
┌──────────────────────────────────────────────┐
│ PROBLEM CARD #___                            │
│                                              │
│ Problem 1 câu: ___________________________   │
│                                              │
│ Ai đang đau? _____________________________   │
│                                              │
│ Workflow hiện tại:                           │
│ 1. ______ → 2. ______ → 3. ______ → 4. ___   │
│                                              │
│ Bước nghẽn nhất: ________  (___ phút/lần)    │
│                                              │
│ Đo thành công bằng gì? ___________________   │
│ Ví dụ: giảm 90 phút → dưới 30 phút           │
│                                              │
│ Quick gut: □ No AI □ Rule □ Workflow         │
│            □ Agent □ Chưa biết               │
└──────────────────────────────────────────────┘
```

Phần nộp chi tiết vẫn dùng template bên dưới để không thiếu field.

```text
Problem 1 câu:

Actor:

Thời điểm / bối cảnh:

Current workflow 3-7 bước:
1.
2.
3.
4.
5.

Bottleneck:

Impact:

Success metric:

Non-AI alternative:

AI hypothesis:

Quick gut:
[ ] No AI / process fix
[ ] Rule
[ ] Workflow
[ ] Agent
[ ] Chưa biết
```

## Draft workflow cho mỗi top problem

Workflow có thể là ảnh, ASCII hoặc Mermaid. Không cần đẹp, nhưng phải đọc được.

Ví dụ ASCII:

```text
CURRENT STATE — 90 phút

[Export Jira: 10']
→ [Lấy metrics: 10']
→ [Đọc Slack: 15']
→ [Tổng hợp: 15']
→ [Viết narrative: 25']  <-- bottleneck
→ [Review: 10']
→ [Gửi: 5']

FUTURE STATE — 21 phút

[Auto-pull: 2']
→ [AI cấu trúc dữ liệu: 1']
→ [AI draft narrative: 1']
→ [PM review + edit: 15']  <-- human boundary
→ [PM gửi: 2']

Fallback: AI draft tệ → PM tự viết lại
```

Nếu nộp file riêng, đặt tên như:

```text
01-individual-problem-scan-workflow-card-1.png
```

## Chọn card muốn pitch nhất

Card tôi muốn pitch nhất:

```text

```

Vì sao:

```text

```

Câu hỏi tôi muốn nhóm challenge:

```text

```

## Nếu dùng AI ở phase này

Prompt phản biện:

```text
Đây là Problem Card của tôi:
[dán card]

Hãy đóng vai skeptical product manager và phản biện:
1. Actor có đủ cụ thể không?
2. Workflow có thật không?
3. Bottleneck có rõ chưa?
4. Metric có đo được không?
5. Rule/process fix đã đủ chưa?
6. Tôi có đang nhảy sang Agent quá sớm không?

Trả lời ngắn, tập trung vào điểm yếu.
```

---

# Break (10')

---

# Phase 3 — Group Convergence: từ 9-12 candidates về 1 (30')

## Mục tiêu

Nhóm 3-4 người sẽ có khoảng 9-12 candidate problems. Không vote ngay. Đi qua 4 bước hội tụ:

```text
Trình bày top 3
→ gom trùng / cluster
→ shortlist
→ chấm nhanh + đồng thuận chọn 1 candidate problem
```

Nhóm lúc này **chỉ chọn candidate problem**, chưa viết Problem Statement hoàn chỉnh.

Đây là phase **tự pitch và tự challenge**. Không dùng AI để viết lời pitch, đặt câu hỏi thay mình, hoặc quyết định thay nhóm. Nếu muốn dùng AI để tóm tắt notes, chỉ làm sau khi nhóm đã thảo luận xong phần chính.

## Bước 3.1 — Trình bày top 3

Mỗi người trình bày 3 candidates, mỗi candidate 1-2 phút:

- problem là gì,
- người gặp vấn đề là ai,
- workflow hiện tại nghẽn ở đâu,
- draft workflow tương lai thay đổi gì,
- vì sao bài này có tác động đáng kể.

| # | Người đưa ra | Candidate problem | Người gặp vấn đề | Điểm nghẽn | Cảm nhận nhanh |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |

## Bước 3.2 — Gom trùng / cluster

| Cluster | Candidates included | Pattern chung | Ghi chú |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |
| D | | | |

## Bước 3.3 — Shortlist

Hỏi:

- Có ai trong nhóm hiểu workflow thật đủ sâu không?
- Actor có cụ thể không?
- Bottleneck có phải một bước cụ thể không?
- Impact có thể đo không?
- Có thể vẽ before/after workflow không?
- Có thể so sánh Rule / Workflow / Agent không?
- Có quá rộng cho lab hôm nay không?

| Candidate | Vì sao vào shortlist | Rủi ro / điều chưa rõ |
|---|---|---|
| | | |
| | | |
| | | |

## Bước 3.4 — Score để đồng thuận

Chấm 1-5. Điểm không cần tuyệt đối; mục tiêu là ép nhóm nói rõ lý do.

| Candidate | Actor rõ | Workflow rõ | Pain có evidence | Impact đo được | Làm trong lab | So sánh R/W/A được | Nhóm hiểu domain | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

Candidate nhóm chọn:

```text

```

Vì sao chọn:

```text

```

Vì sao không chọn các candidate còn lại:

```text

```

Nếu có disagreement, nhóm xử lý thế nào:

```text

```

---

# Phase 4 — Quick Validation + Research giải pháp (30')

## Mục tiêu

Sau khi chọn candidate problem, nhóm cần kiểm tra nhanh:

- pain có thật không,
- người khác có gặp không,
- đã có giải pháp nào tương tự chưa,
- bài toán có nên giải bằng AI không.

## Bước 4.1 — Quick validation

Chọn ít nhất một cách.

### Option A — Quick interviews

Hỏi 2-3 người:

- Lần gần nhất bạn gặp vấn đề này là khi nào?
- Bạn đang xử lý bằng workflow nào?
- Bước nào mất thời gian hoặc khó chịu nhất?
- Bạn mất khoảng bao lâu?
- Nếu tốt hơn, bạn muốn điều gì thay đổi?

### Option B — Micro survey / Discord poll

Hỏi 5-10 người:

- Bạn có gặp vấn đề này không?
- Tần suất?
- Bước nào đau nhất?
- Hiện bạn workaround thế nào?
- Mức độ đáng giải quyết: 1-5?

Kết quả:

| Nguồn | Số người / số mẫu | Tín hiệu xác nhận | Tín hiệu phản bác | Nhóm sửa problem thế nào |
|---|---:|---|---|---|
| Interview | | | | |
| Survey / poll | | | | |
| Log / review / ticket | | | | |

## Bước 4.2 — Research giải pháp đã có

Tìm ít nhất:

- 2-3 existing solutions/tools/patterns.
- 1-2 nguồn tham khảo có hyperlink.
- Nhận xét: họ xử lý bước nào trong workflow, chưa xử lý bước nào.
- Bài học kéo về bài toán nhóm mình.

| Nguồn / tool / case | Link | Họ giải quyết phần nào? | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Nếu dùng AI research, dùng prompt:

```text
Nhóm tôi đang phân tích bài toán:
[mô tả ngắn]

Hãy tìm:
1. 2-3 tool/case/pattern đã giải bài toán tương tự
2. Họ giải quyết bước nào trong workflow
3. Rủi ro hoặc khoảng trống còn lại

Yêu cầu: ghi link nguồn cho claim quan trọng. Nếu không chắc, nói rõ không chắc.
```

Không dùng số liệu AI đưa ra nếu không verify được.

---

# Phase 5 — Workflow + Problem Statement (45')

## Bước 5.1 — Current workflow bản nhóm

Vẽ workflow hiện tại kỹ hơn bản cá nhân. Mỗi bước nên có:

- actor,
- input,
- output,
- thời gian/tần suất,
- handoff,
- bottleneck.

Dán workflow hoặc link file:

```text

```

| Bước | Actor | Input | Output | Thời gian/tần suất | Ghi chú |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Bottleneck chính:

```text

```

## Bước 5.2 — Future workflow bản nhóm

Vẽ workflow sau tối ưu. Cần thể hiện:

- bước nào Rule xử lý,
- bước nào AI/Workflow hỗ trợ,
- bước nào con người vẫn làm,
- boundary ở đâu,
- phương án quay về nếu AI sai.

Dán workflow hoặc link file:

```text

```

Before/after impact:

| Metric | Trước | Sau kỳ vọng | Ghi chú |
|---|---:|---:|---|
| Số bước | | | |
| Tổng thời gian | | | |
| Số bước thủ công | | | |
| Bottleneck chính | | | |
| Risk mới | | | |

## Bước 5.3 — Problem Statement v0

| Field | Nội dung |
|---|---|
| **Actor** | |
| **Workflow** | |
| **Bottleneck** | |
| **Impact** | |
| **Success Metric** | |
| **Boundary** | |

Prompt phản biện PS:

```text
Đây là Problem Statement v0 của nhóm tôi:
[dán 6 field]

Hãy chỉ ra field nào còn mơ hồ, metric đã đo được chưa, boundary đã rõ chưa.
Đừng viết lại thay tôi. Chỉ đặt câu hỏi và chỉ ra lỗ hổng.
```

---

# Break (10')

---

# Phase 6 — Rule / Workflow / Agent + Decision (25')

## Bước 6.0 — Ma trận độ phù hợp với AI để suy nghĩ nhanh

Ma trận này chỉ là công cụ phụ để suy nghĩ. Quyết định cuối vẫn phải dựa trên workflow, metric, boundary và rủi ro thật.

| | Độ mơ hồ thấp | Độ mơ hồ cao |
|---|---|---|
| **Độ phức tạp thấp** | Rule hoặc workflow đơn giản thường đủ | Workflow có AI hỗ trợ một bước có thể đủ |
| **Độ phức tạp cao** | Workflow điều phối nhiều bước rõ ràng, chưa chắc cần Agent | Agent có thể phù hợp, nhưng cần boundary, người thật kiểm tra và phương án quay về rất rõ |

Độ mơ hồ là gì?

- Thấp: có đáp án đúng/sai khá rõ, ví dụ phân loại theo 5 nhóm cố định.
- Cao: có nhiều cách trả lời vẫn chấp nhận được, ví dụ viết narrative tổng hợp từ nhiều nguồn.

Độ phức tạp là gì?

- Thấp: 1-2 bước, input/output rõ, ít nguồn dữ liệu.
- Cao: nhiều bước nối tiếp, nhiều nguồn dữ liệu, bước sau phụ thuộc kết quả bước trước.

Tự kiểm nhanh:

| Câu hỏi | Nếu có | Nếu không |
|---|---|---|
| Output có thể khác nhau mỗi lần mà vẫn chấp nhận được không? | Độ mơ hồ cao | Độ mơ hồ thấp |
| Cần phối hợp 3+ bước hoặc 3+ nguồn dữ liệu không? | Độ phức tạp cao | Độ phức tạp thấp |
| AI có cần tự quyết định bước tiếp theo không? | Có thể cần Agent | Rule/Workflow có thể đủ |

Bài toán của nhóm nằm ở ô nào?

```text

```

Vì sao?

```text

```

## Bước 6.1 — So sánh Rule / Workflow / Agent

| Mức | Phương án cho bài toán nhóm | Khi nào đủ | Rủi ro | Chọn? |
|---|---|---|---|---|
| **Rule** | | | | |
| **Workflow** | | | | |
| **Agent** | | | | |

Hỏi kỹ:

- Rule có giải được 70-80% case không?
- Workflow có đủ vì các bước khá rõ không?
- Có thật sự cần Agent tự lập kế hoạch/gọi công cụ/đổi bước tiếp theo không?
- Nếu AI sai, ai phát hiện và sửa?
- Có thể hạ mức từ Agent về Workflow hoặc từ Workflow về Rule không?

Mức chọn:

```text
[Rule / Workflow / Agent]
```

Vì sao chọn:

```text

```

Vì sao không chọn mức đơn giản hơn:

```text

```

## Bước 6.2 — Problem Statement v1

| Field | Nội dung |
|---|---|
| **Actor** | |
| **Workflow** | |
| **Bottleneck** | |
| **Impact** | |
| **Success Metric** | |
| **Boundary** | |
| **AI intervention point** | |
| **Mức chọn** | Rule / Workflow / Agent |
| **Rủi ro & người thật kiểm tra** | |

## Bước 6.3 — Final decision

| Câu hỏi | Yes / Not Yet / No | Ghi chú |
|---|---|---|
| Actor và workflow đã rõ chưa? | | |
| Baseline và success metric đã đo được chưa? | | |
| Có data/input đủ dùng chưa? | | |
| Nếu AI sai, hậu quả có chấp nhận được không? | | |
| Có người review/owner vận hành không? | | |
| Có cách non-AI đơn giản hơn không? | | |

Decision:

```text
[Go / Not Yet / No-Go]
```

Lý do:

```text

```

Nếu Go, pilot nhỏ nhất là:

```text

```

Nếu Not Yet, cần validate gì trước:

```text

```

Nếu No-Go, nên làm gì thay AI:

```text

```

---

# Phase 7 — Individual Reflection (15')

Reflection không chỉ là "tôi dùng AI thế nào". Bạn cần phản tư về vai trò của mình trong nhóm.

Reflection là phần cá nhân. Không dùng AI để viết thay câu trả lời. Nếu dùng AI, chỉ dùng để gợi ý câu hỏi tự soi hoặc kiểm xem mình còn bỏ sót ý nào.

## Tôi đã tham gia vào phần nào?

| Hoạt động | Tôi đã làm gì? | Kết quả / ảnh hưởng |
|---|---|---|
| Scan cá nhân | | |
| Pitch Problem Card | | |
| Challenge bài của bạn khác | | |
| Gom trùng / cluster | | |
| Chọn candidate problem | | |
| Validation / research | | |
| Workflow nhóm | | |
| Problem Statement | | |
| Rule / Workflow / Agent | | |
| Decision | | |

## Bảng dùng AI trong reflection

| Phase | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai/hời hợt ở đâu? | Tôi sửa gì bằng nhận định của mình? |
|---|---|---|---|---|
| Scan | | | | |
| Problem Card | | | | |
| Workflow | | | | |
| Research | | | | |
| Problem Statement | | | | |
| Rule / Workflow / Agent | | | | |
| Decision | | | | |

## Reflection câu hỏi mở

- Tôi học được gì khi nghe top 3 problems của các bạn khác?
- Nhóm có lúc nào bị solution-first không?
- Tôi có thay đổi ý kiến sau khi bị challenge không?
- Tôi đóng góp gì thật sự vào artifact cuối?
- Điều khó nhất khi viết Problem Statement là gì?
- Nếu làm lại, tôi sẽ challenge nhóm mạnh hơn ở điểm nào?

Reflection:

```text

```

## Tự kiểm cuối bài

- [ ] [12đ cá nhân] Cá nhân có 5+ problems và top 3 Problem Cards.
- [ ] [12đ cá nhân] Tôi đã pitch rõ và challenge nhóm đúng trọng tâm.
- [ ] Nhóm có nhật ký hội tụ từ candidates về 1 bài.
- [ ] [15đ nhóm] Nhóm có workflow trước/sau.
- [ ] [20đ nhóm] Nhóm có Problem Statement v0/v1 với metric và boundary rõ.
- [ ] [15đ nhóm] Nhóm có so sánh No AI / Rule / Workflow / Agent.
- [ ] [10đ nhóm] Nhóm có Go / Not Yet / No-Go và lý do rõ.
- [ ] [10đ cá nhân] Reflection cá nhân có nói rõ vai trò trong nhóm, cách dùng AI, điều học được và nếu làm lại sẽ đổi gì.
- [ ] [6đ cá nhân] Tôi tự giải thích được mạch problem → workflow → metric → boundary → độ phù hợp với AI.

---

*Day 02 Lab — Worksheet*
