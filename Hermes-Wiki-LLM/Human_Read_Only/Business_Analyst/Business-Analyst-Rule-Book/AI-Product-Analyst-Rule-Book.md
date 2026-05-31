# AI Product Rule Book

_Cẩm nang thiết kế, định hình và ra quyết định cho Business Analyst (BA) & Product Owner (PO) trong kỷ nguyên AI._

## MỤC TIÊU TỐI THƯỢNG

> Biến những yêu cầu mơ hồ, cảm tính của Stakeholder thành một **Problem Statement** rõ ràng, định hình giải pháp AI chuẩn xác và đưa ra quyết định đầu tư thông minh (**Go / Not Yet / No-Go**).

## CHƯƠNG 1: TƯ DUY CỐT LÕI (CORE MINDSET)

### 1. Bản chất của AI Product

Sản phẩm tích hợp AI bản chất vẫn là một sản phẩm hoàn chỉnh. Nó kế thừa chứ không thay thế các nguyên lý phát triển sản phẩm truyền thống. Tuy nhiên, tích hợp AI đòi hỏi một mô hình tư duy khác biệt:

- **Tính bất định (Probabilistic vs. Deterministic):** Khác với phần mềm truyền thống hoạt động dựa trên các logic cố định 100% (nếu A thì luôn ra B), hệ thống AI hoạt động dựa trên xác suất và thống kê. Đầu ra của AI có tính bất định.
    
- **Quản lý kỳ vọng (Expectation Management):** Vì AI có thể sai, BA/PO cần thiết kế giao diện và trải nghiệm (UI/UX cho AI) giúp người dùng hiểu rõ giới hạn của mô hình và dễ dàng kiểm soát, sửa sai.
    
- **Xử lý lỗi chủ động (Error Handling & Fallback):** Luôn phải thiết kế sẵn phương án dự phòng khi mô hình AI đưa ra kết quả có độ tự tin thấp (ví dụ: tự động chuyển sang quy trình thủ công do con người phê duyệt).
    

### 2. Rào cản gia nhập & Độ khó khi tích hợp AI (AI Barrier)

- **Low Barrier (Dễ tiếp cận - Khó phòng thủ):** Việc chỉ gọi các API có sẵn (như OpenAI, Anthropic...) để xây dựng tính năng ăn liền rất dễ thực hiện. Ai cũng có thể làm được, do đó khó tạo ra lợi thế cạnh tranh lâu dài.
    
- **Higher Barrier (Khó sao chép - Giá trị bền vững):** Đòi hỏi sự thấu hiểu sâu sắc về mô hình (Understand the Model), thiết kế UX chuyên biệt cho AI (UX for AI), kiểm soát lỗi chặt chẽ (Handle Errors) và quản lý kỳ vọng của người dùng (User Expectations).
    

### 3. Nguyên tắc tìm đúng vấn đề

- **Triết lý chủ đạo:** Tìm đúng vấn đề trước khi tìm giải pháp (Mô hình Double Diamond — Don Norman / British Design Council 2005).
    
- **Nguyên tắc phản trực giác (Counter-intuitive Rule):**
    
    > _"Never solve the problem I am asked to solve."_ — Don Norman, _The Design of Everyday Things_
    
- **Cảnh báo chiến lược:** Giải pháp xuất sắc cho một vấn đề sai lệch có thể đem lại hậu quả tồi tệ hơn việc không có giải pháp nào.
    
- **Khởi nguồn sản phẩm:** Luôn bắt đầu từ bài toán thực tế của doanh nghiệp và nỗi đau của người dùng, không bắt đầu từ công nghệ AI.
    
- **Lộ trình chuẩn:**
    
    $$\text{Vấn đề} \rightarrow \text{Quy trình vận hành} \rightarrow \text{Chỉ số đo lường} \rightarrow \text{Giải pháp AI}$$

### 4. Ba bài học thực tế từ thị trường

- **Lệch năng lực cốt lõi (Ví dụ từ Cursor):** Họ đã dũng cảm từ bỏ mảng AI thiết kế cơ khí (không phải thế mạnh sâu sắc về nghiệp vụ) để tập trung hoàn toàn vào AI Code Editor — nơi đội ngũ của họ am hiểu tường tận từng nỗi đau và quy trình làm việc của lập trình viên.
    
- **Sản phẩm tốt** $\neq$ **Thị trường lớn (Ví dụ từ Artifact):** Dù là một ứng dụng đọc tin tức tích hợp AI xuất sắc về mặt kỹ thuật, nhưng quy mô thị trường quá hẹp và hành vi người dùng không đủ lớn để thương mại hóa thành công.
    
- **Định vị đúng điểm đau (Ví dụ từ NotebookLM):** Họ không cố tạo ra một AI đa năng giải quyết mọi việc. Thay vào đó, họ định vị cực tốt: tập trung giải quyết nhu cầu hỏi đáp, tóm tắt trên kho tài liệu cá nhân của người dùng và đối chiếu nguồn gốc bằng trích dẫn chuẩn xác để giải quyết triệt để nạn "tin giả/ảo giác" của AI.
    

## CHƯƠNG 2: KHÁM PHÁ VÀ ĐỊNH NGHĨA VẤN ĐỀ (DIAMOND 1)

> **"Phân kỳ để thấu hiểu sâu sắc, Hội tụ để lựa chọn chính xác."**

```
   DISCOVER (Phân kỳ)               DEFINE (Hội tụ)
     /---------\                     /---------\
    /   Quan    \                   /   Gom     \
   /    sát,     \                 /    nhóm,    \
  <   Phỏng vấn,  >               <     5 Whys,   >
   \   Khảo sát   /                 \  Problem   /
    \           /                   \  Statement/
     \---------/                     \---------/

```

### Giai đoạn 1: DISCOVER (Phân kỳ) - Khám phá (Mở rộng góc nhìn)

Mục tiêu là thu thập tối đa thông tin về bối cảnh và hành vi người dùng thông qua các phương pháp:

- **Quan sát thực tế (Observation):** Theo dõi cách người dùng thực hiện công việc hàng ngày trong môi trường tự nhiên của họ.
    
- **Phỏng vấn người dùng (User Interview):** Trò chuyện trực tiếp để đào sâu cảm xúc, động lực và khó khăn.
    
- **Khảo sát (Survey):** Thu thập dữ liệu định lượng trên diện rộng.
    
- **Nhật ký hành vi (Diary Study):** Người dùng tự ghi lại trải nghiệm của họ theo thời gian thực trong nhiều ngày/tuần.
    
- **Phân tích dữ liệu / Nhật ký hệ thống (Data/Log Analysis):** Tìm kiếm các điểm bất thường hoặc hành vi thói quen dựa trên dữ liệu lịch sử.
    
- **Bản đồ các bên liên quan (Stakeholder Mapping):** Xác định rõ ai là người chịu ảnh hưởng, ai là người vận hành và ai là người ra quyết định phê duyệt ngân sách.
    

### Giai đoạn 2: DEFINE (Hội tụ) - Định nghĩa (Chọn lọc dựa vào dữ liệu)

Mục tiêu là chắt lọc các thông tin thô thành các insight có giá trị và định hình bài toán rõ ràng:

- **Sơ đồ đồng cảm / Gom nhóm ý tưởng (Affinity Mapping):** Nhóm các quan sát tương đồng để tìm ra các mô-típ điểm đau (pain point patterns).
    
- **Kỹ thuật đặt câu hỏi 5 Whys:** Liên tục đặt câu hỏi "Tại sao" để tìm ra nguyên nhân gốc rễ (Root Cause) của vấn đề.
    
- **Ma trận Tác động – Nỗ lực (Impact-Effort Matrix):** Ưu tiên giải quyết các vấn đề có tác động lớn nhưng yêu cầu nỗ lực thực hiện ở mức vừa phải (Quick Wins).
    
- **Biểu quyết bằng chấm tròn (Dot Voting):** Đồng thuận nhóm nhanh chóng để chọn ra vấn đề nhức nhối nhất cần ưu tiên.
    
- **Câu hỏi mở hướng giải quyết (How Might We - HMW):** Chuyển đổi điểm đau thành cơ hội thiết kế (Ví dụ: _"Làm thế nào chúng ta có thể giúp sếp duyệt nhanh 50 email xin nghỉ chỉ trong 3 phút?"_).
    
- **Phát biểu bài toán (Problem Statement):** Phát biểu ngắn gọn, rõ ràng về vấn đề cần giải quyết.
    

### Quy trình thiết kế lấy con người làm trung tâm (HCD - Human-Centered Design)

_(Vòng lặp 4 bước liên tục của Don Norman)_

1. **Observation (Quan sát):** Lựa chọn đúng đối tượng mục tiêu. Quan sát họ trong cuộc sống và công việc bình thường để hiểu các tình huống thực tế họ gặp phải.
    
2. **Ideation (Tạo ý tưởng):** Đưa ra thật nhiều ý tưởng đột phá, không bị ràng buộc bởi các hạn chế kỹ thuật hay ngân sách ở bước đầu. Tránh phê bình ý tưởng của bản thân hoặc người khác. Đặt câu hỏi hoài nghi về mọi thứ đang tồn tại.
    
3. **Prototype (Tạo mẫu thử):** Tạo nguyên mẫu cực nhanh (giấy, Figma, wireframe...) cho giải pháp tiềm năng. Mục tiêu là kiểm nghiệm giả định nhanh nhất và rẻ nhất trước khi bắt đầu lập trình.
    
4. **Test (Kiểm tra):** Ngồi quan sát trực tiếp cách người dùng tương tác với bản mẫu thử trong thực tế mà không giải thích hay can thiệp.
    
5. **Iteration (Lặp lại):** Tinh chỉnh thiết kế và nâng cao liên tục dựa trên kết quả kiểm tra.
    

## CHƯƠNG 3: PHƯƠNG PHÁP KHẢO SÁT VÀ SÀN LỌC BÀI TOÁN AI

Sử dụng Tư duy nguyên bản (First Principle Thinking), đi từ Vấn Đề Gốc Rễ, Cơ Bản (Funcdamental) -  Đôi khi Insight bắt đầu từ những câu hỏi hiển nhiên. 

### 1. Tìm bài toán AI ở đâu?

Tập trung nhận diện vấn đề thực tế xung quanh; tuyệt đối chưa vội đề xuất hay thảo luận về giải pháp công nghệ ở bước này. Một bài toán có tiềm năng ứng dụng AI thường có 4 đặc tính:

- **Tác vụ lặp lại (Repetitive):** Các công việc diễn ra thường xuyên, có tính chu kỳ cao. Cần tìm ra công đoạn nào có thể chuẩn hóa để hướng tới tự động hóa.
    
- **Tiêu tốn thời gian (Time-consuming):** Khối lượng thông tin cần xử lý quá lớn; thời gian của con người bị hao phí nhiều ở các bước như tìm kiếm, đọc hiểu, chờ đợi phản hồi hoặc định dạng dữ liệu.
    
- **Lợi thế của AI (AI Advantage):** Các tác vụ đòi hỏi khả năng xử lý ngôn ngữ tự nhiên, phân tích ngữ cảnh mơ hồ, dịch thuật, phân loại cảm xúc hoặc tổng hợp thông tin từ đa nguồn dữ liệu không cấu trúc.
    
- **Điểm đau người dùng (User Pain Points):** Điểm khiến người dùng thường xuyên phàn nàn, mệt mỏi, gây tắc nghẽn (bottleneck) toàn bộ quy trình vận hành.
    

### 2. Tư duy đặt những câu hỏi nguyên bản (First Principles)

Những insight mang tính đột phá thường bắt đầu từ việc đặt câu hỏi hoài nghi những điều hiển nhiên:

- **Isaac Newton:** Quả táo rơi xuống đất — _vậy Mặt Trăng có đang "rơi" tự do về phía Trái Đất hay không?_
    
- **Edwin Land (Polaroid):** _Tại sao chúng ta không thể xem ảnh ngay lập tức sau khi chụp mà phải đợi rửa phim?_
    
- **Joe Gebbia & Brian Chesky (Airbnb):** _Liệu những phòng ngủ trống trong nhà người dân có thể dùng làm dịch vụ lưu trú cho khách du lịch thay thế khách sạn hay không?_
    

-> Tò Mò Trước, Đánh giá Sau.

## CHƯƠNG 4: KHUNG PHỎNG VẤN VÀ CÂU HỎI CHIẾN LƯỢC

### 1. Câu hỏi gợi mở rộng tư duy

Trước khi quyết định lựa chọn một bài toán cụ thể, BA cần đặt các câu hỏi gợi mở để giải phóng lối mòn tư duy:

- Giả định hiển nhiên nào trong quy trình này cần được lật ngược lại ?
    
- Có cách tiếp cận nào hoàn toàn mới và khác biệt cho vấn đề này không ?
    
- Nếu được thiết kế lại quy trình này từ đầu và không bị giới hạn bởi hệ thống cũ, chúng ta sẽ làm thế nào ?
    
- Tại sao bài toán này bắt buộc phải dùng AI ? Nếu giải quyết bằng code logic truyền thống (Rule-based) thì sao ?
    
- Quy trình phức tạp hiện tại đang tồn tại là do nghiệp vụ bắt buộc hay chỉ vì thói quen lâu năm ?
    
- Có câu hỏi cốt lõi hay rủi ro nhạy cảm nào đang bị mọi người né tránh thảo luận không ?
    

### 2. Discovery Interview: 5 câu hỏi cốt lõi dành cho Stakeholder

Để xác định mức độ nghiêm trọng và tính khả thi của dự án, BA bắt buộc phải hỏi Stakeholder 5 câu hỏi sau:

1. **Vấn đề nhức nhối (Pain Point) là gì?** Tần suất lặp lại của vấn đề này trong ngày hoặc trong tuần diễn ra ra sao?
    
2. **Quy trình (Workflow) hiện tại như thế nào?** Công cụ cụ thể nào được sử dụng ở từng bước, và ai bàn giao công việc cho ai?
    
3. **Thiệt hại (Cost) do vấn đề này gây ra là gì?** Hãy lượng hóa cụ thể về thời gian xử lý bị lãng phí, thiệt hại tài chính trực tiếp, vi phạm cam kết dịch vụ (SLA) hay làm sụt giảm tỷ lệ chuyển đổi (conversion)?
    
4. **Hậu quả nếu hệ thống AI sai sót là gì?** Khâu nào bắt buộc phải có con người tham gia kiểm soát và phê duyệt trực tiếp (HITL - Human-in-the-loop), khâu nào AI chỉ cần đưa ra gợi ý hỗ trợ?
    
5. **Ai là người có quyền phê duyệt ngân sách dự án (nói YES)?** Chỉ số hiệu quả cốt lõi (metric) và mức độ rủi ro (risk) tối đa nào sẽ trực tiếp quyết định việc họ đồng ý đầu tư?
    

> 🚨 **LƯU Ý TỐI MẬT CỦA BA:** > Nếu đối tác (Stakeholder) không thể mô tả được quy trình vận hành hiện tại và không lượng hóa được chi phí thiệt hại khi xảy ra sai sót, mọi đề xuất hay giải pháp AI ở thời điểm này đều chỉ là phỏng đoán cảm tính, hoàn toàn thiếu căn cứ thực tế.

## CHƯƠNG 5: BỐN CÂU HỎI TRỌNG TÂM & QUY TRÌNH RA QUYẾT ĐỊNH

Trước khi bắt tay vào xây dựng sản phẩm AI, BA phải dẫn dắt đội ngũ trả lời mạch lạc **4 câu hỏi trọng tâm** đi kèm với việc xác thực dữ liệu và quy trình:

```
                  [ 4 CÂU HỎI TRỌNG TÂM ]
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
   1. Có thực sự cần AI?             2. Giải pháp ở cấp độ nào?
   (Rule vs. AI)                     (Rule, Workflow, Agent)
            │                                 │
            ├─────────────────────────────────┘
            ▼
   2. Problem Statement đủ rõ? ───────► 4. Quyết định thế nào?
   (Problem Card đạt chuẩn)            (Go, Not Yet, No-Go)

```

### 1. Xác thực dữ liệu (Data Validation)

- **Dữ liệu có sẵn không?** (Dạng text, email, log hệ thống, excel, database...). Nếu chưa có dữ liệu lịch sử, dự án sẽ không thể huấn luyện, fine-tune hoặc có cơ sở để đánh giá độ chính xác của AI.
    
- **Chất lượng dữ liệu ra sao?** Dữ liệu có bị nhiễu, thiếu thông tin quan trọng hoặc định dạng không đồng nhất hay không?
    
- **Tần suất phát sinh dữ liệu mới?** Có đủ lớn để mô hình AI học hỏi, tối ưu và cập nhật liên tục hay không?
    
- **Quy tắc vàng:**
    
    $$\text{Garbage In} \rightarrow \text{Garbage Out}$$
    
    Không có nguồn dữ liệu sạch và chuẩn hóa, mọi giải pháp AI đều vô nghĩa.
    

### 2. Vẽ quy trình (Workflow Mapping)

- **Vẽ quy trình HIỆN TẠI (As-Is):** Mô tả chi tiết từng bước thủ công đang diễn ra thế nào, trách nhiệm thuộc về ai, thời gian hao phí trung bình ở mỗi bước là bao nhiêu.
    
- **Xác định điểm nghẽn (Bottleneck):** Tìm ra bước nào đang chiếm nhiều thời gian nhất hoặc có tỷ lệ xảy ra sai sót cao nhất trong quy trình.
    
- **Thiết kế quy trình TƯƠNG LAI (To-Be) có AI tham gia:** Định vị chính xác mô hình AI sẽ can thiệp vào bước nào, xác định rõ dữ liệu đầu vào (Input) và kết quả mong muốn đầu ra (Output) của AI.
    

## CHƯƠNG 6: PHÂN LOẠI CẤP ĐỘ GIẢI PHÁP AI (AI SOLUTION TYPOLOGY)

BA cần xác định rõ giải pháp cần xây dựng nằm ở cấp độ nào nhằm tối ưu hóa chi phí đầu tư và độ phức tạp kỹ thuật:

### 1. Ba cấp độ giải pháp (Solution Levels)

|Cấp độ|Định nghĩa|Ví dụ thực tế (Cùng kịch bản Duyệt phép)|
|---|---|---|
|**Rule-based (Dựa trên luật)**|Quy trình cứng nhắc, tuân thủ logic định sẵn nghiêm ngặt ($If\text{-}Then$). Không cần học từ dữ liệu.|Hệ thống tự động từ chối đơn xin nghỉ nếu: $\text{Số ngày xin nghỉ} > \text{Số ngày phép còn lại}$.|
|**Workflow Automation (Tự động hóa quy trình)**|AI xử lý các tác vụ phi cấu trúc tại từng nút thắt cụ thể trong chuỗi quy trình lớn hơn để kết nối các hệ thống.|AI tự động đọc email viết tay tự do của nhân viên, trích xuất ra các thực thể (Tên, Ngày nghỉ, Lý do) rồi điền tự động vào hệ thống HRM của công ty để sếp duyệt.|
|**Agentic AI (AI đại lý tự chủ)**|AI có khả năng tự suy luận, tự lập kế hoạch hành động và thực thi chuỗi tác vụ phức tạp với phản hồi trực tiếp từ môi trường.|Khi nhận mail xin nghỉ, AI tự check lịch dự án, tự gửi mail đàm phán với các thành viên khác để tìm người trực thay thế, tự cập nhật lại lịch làm việc chung và gửi thông báo hoàn tất cho sếp.|

### 2. Khung quyết định: Go / Not Yet / No-Go

- **GO (Triển khai ngay):** * Bài toán nghiệp vụ cực kỳ rõ ràng.
    
    - Dữ liệu lịch sử đã sẵn có và sạch sẽ.
        
    - Hậu quả lỗi của AI ở mức kiểm soát được hoặc đã thiết kế sẵn cơ chế con người can thiệp (HITL) hiệu quả.
        
    - Chỉ số hoàn vốn đầu tư ($ROI$) cao.
        
- **NOT YET (Chuẩn bị thêm):**
    
    - Ý tưởng sản phẩm rất tiềm năng nhưng quy trình nghiệp vụ hiện tại chưa được chuẩn hóa.
        
    - Nguồn dữ liệu còn thiếu sót hoặc chưa được gom về một mối.
        
    - Cần lùi lại để chuẩn hóa quy trình thủ công và thu thập dữ liệu sạch trước.
        
- **NO-GO (Hủy bỏ dự án):**
    
    - Quy trình thực tế có rủi ro sai sót quá lớn, lỗi của AI có thể gây ra hậu quả pháp lý nghiêm trọng hoặc thiệt hại tài chính không thể cứu vãn.
        
    - Bài toán hoàn toàn có thể giải quyết triệt để và rẻ hơn bằng code logic truyền thống (Rule-based).
        
    - Chi phí vận hành, duy trì mô hình AI (API tokens, hạ tầng phần cứng) vượt quá giá trị kinh tế mà nó mang lại.
        

## CHƯƠNG 7: CẤU TRÚC PROBLEM STATEMENT & PROBLEM CARD

Mỗi bài toán AI trước khi trình duyệt phải được cụ thể hóa hoàn chỉnh vào một **Problem Card** tiêu chuẩn gồm 4 thành tố:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                               PROBLEM CARD                                │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. CONTEXT (Bối cảnh):                                                    │
│    [Đối tượng người dùng nào] đang gặp khó khăn khi thực hiện [tác vụ gì] │
│    trong quy trình vận hành [nào]?                                        │
│                                                                           │
│ 2. PAIN POINT (Điểm đau):                                                 │
│    [Vấn đề cụ thể gì] xảy ra khiến họ bị tổn thất [lượng hóa cụ thể về    │
│    thời gian / tài chính / chất lượng dịch vụ SLA]?                       │
│                                                                           │
│ 3. GOAL (Mục tiêu):                                                       │
│    Mong muốn cải thiện [chỉ số hiệu quả cụ thể nào] lên mức [bao nhiêu]?  │
│                                                                           │
│ 4. CONSTRAINT/RISK (Ràng buộc & Rủi ro):                                  │
│    Hệ thống bắt buộc phải tránh xảy ra [hậu quả nghiêm trọng nào]?        │
│    Cơ chế kiểm soát lỗi (Fallback) được thiết kế thế nào?                 │
└───────────────────────────────────────────────────────────────────────────┘

```

## CHƯƠNG 8: CÁC SAI LẦM THƯỜNG GẶP (ANTI-PATTERNS) KHI TÍCH HỢP AI

BA phải liên tục cảnh giác để tránh đưa dự án sa vào 4 sai lầm kinh điển sau:

```
                      [ ANTI-PATTERNS ]
                             │
      ┌──────────────┬───────┴───────┬──────────────┐
      ▼              ▼               ▼              ▼
Solution-first  No baseline    No evaluation   No boundary

```

1. **Ưu tiên giải pháp (Solution-first):** Hào hứng nhảy vào xây dựng Chatbot, AI Agent hoành tráng trước khi làm rõ quy trình vận hành thực tế và xác định chính xác điểm nghẽn cần giải quyết.
    
2. **Mơ hồ hiện trạng (No baseline):** Không tiến hành đo lường và lượng hóa tổn thất của quy trình cũ trước khi áp dụng AI. Điều này dẫn đến việc không có căn cứ, số liệu đối chứng để đánh giá giải pháp AI mới có thực sự cải tiến hiệu quả hay không.
    
3. **Bỏ qua đánh giá (No evaluation):** Triển khai AI nhưng không thiết lập sẵn bộ kịch bản kiểm thử (test suite), thiếu các chỉ số đo lường độ chính xác chuyên biệt cho AI và không có phương án vận hành đối chứng (A/B testing).
    
4. **Mập mờ ranh giới (No boundary):** Không phân định rõ ràng phạm vi tự chủ tối đa của AI. Không xác định được thời điểm nhạy cảm bắt buộc phải dừng quy trình tự động để yêu cầu con người phê duyệt (Human-in-the-loop).
    

> 🚨 **QUY TẮC XỬ LÝ KHỦNG HOẢNG (TRIGGER RULE):** Nếu phát hiện dự án hoặc ý tưởng sản phẩm đang vấp phải bất kỳ sai lầm nào trong 4 Anti-patterns trên, toàn bộ đội ngũ phải **ngay lập tức dừng việc phát triển công nghệ**, quay trở lại bước **làm rõ Problem Statement** và xác thực lại dữ liệu.

## CHƯƠNG 9: KHUNG THỰC HÀNH LAB & VÒNG LẶP HỌC TẬP

Để rèn luyện tư duy thực tế, BA cần tuân thủ nghiêm ngặt lộ trình thực hành và cơ chế phản tư định kỳ:

### 1. Lộ trình thực hành chuẩn (Lab Agenda)

- **Bước 1: Khảo sát cá nhân:** Tự tìm kiếm và liệt kê ít nhất 5 bài toán thực tế xung quanh đời sống/công việc, hoàn thiện 3 bản **Problem Cards** thô.
    
- **Bước 2: Phản biện chéo nhóm:** Trình bày ý tưởng trước nhóm để các thành viên phản biện dựa trên 4 Anti-patterns, thống nhất lựa chọn ra 1 bài toán thực tế và có giá trị nhất.
    
- **Bước 3: Xác thực và Vẽ quy trình:** Tiến hành thu thập thông tin để xác thực dữ liệu lịch sử và vẽ chi tiết bản đồ quy trình $As\text{-}Is$ cùng quy trình $To\text{-}Be$ có AI can thiệp.
    
- **Bước 4: Xác định giải pháp & Ra quyết định:** Phân loại giải pháp (Rule / Workflow / Agent) và bỏ phiếu thống nhất quyết định cuối cùng (**Go / Not Yet / No-Go**).
    

### 2. Vòng lặp học tập: Nhật ký phản tư (Reflection Log)

Cuối mỗi ngày thực hiện dự án, từng cá nhân BA bắt buộc phải hoàn thành **Reflection Log** theo mô hình cấu trúc **3W**:

```
* WHAT (Tôi đã làm gì?):
    Hôm nay tôi đã thực hiện những hoạt động gì? Phát hiện ra điểm bất ngờ hay 
    sự thật ngầm hiểu (insight) thú vị nào từ thực tế?
    
* SO WHAT (Điều đó có ý nghĩa gì?):
    Phát hiện đó tác động thế nào đến việc định hình bài toán? Nó có làm thay đổi 
    giả định ban đầu của tôi về giải pháp AI hay không?
    
* NOW WHAT (Tôi sẽ làm gì tiếp theo?):
    Tôi sẽ thay đổi, cải tiến hay điều chỉnh hành động cụ thể nào trong ngày mai 
    để tối ưu hóa sản phẩm?

```

---

**Problem Statement:** AI20K-066: AI Trợ Lý Phát Hiện Sớm Khó Khăn Học Tập Của Học Sinh

**Domain:** K-12 Education - Early Intervention

**Problem Description:** Học sinh gặp khó khăn học tập (chậm tiến bộ, lỗ hổng kiến thức) thường được phát hiện muộn khi đã tụt lại xa, khó bắt kịp. Bài toán: AI phát hiện sớm khó khăn học tập: phân tích kết quả và quá trình học tập để nhận diện học sinh có dấu hiệu gặp khó hoặc lỗ hổng kiến thức cụ thể, giải thích vấn đề và gợi ý hướng hỗ trợ cho giáo viên, đề xuất tài liệu/bài tập bổ trợ phù hợp, theo dõi hiệu quả can thiệp. Có guardrail bảo mật dữ liệu trẻ em và dùng để hỗ trợ chứ không gán nhãn. Giúp giáo viên can thiệp kịp thời để không học sinh nào bị bỏ lại.
Tech Stack (định hướng): ML (learning analytics), OpenAI/Claude, FastAPI, dashboard. 

**Technical Skills:** ML + LLM

**MVP Requirements:** Yêu cầu tối thiểu: sản phẩm web/app hoàn chỉnh — deployed online (có URL truy cập), đăng nhập & phân quyền cơ bản, giao diện UI/UX hoàn chỉnh, quản lý user. Không chấp nhận: demo notebook, script CLI, prototype chỉ chạy localhost.

https://hermes-agent.nousresearch.com/docs

