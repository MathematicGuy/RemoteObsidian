
### 1. Nguyên tắc tìm đúng vấn đề

- **Triết lý chủ đạo:** Tìm đúng vấn đề trước khi tìm giải pháp (Mô hình Double Diamond — Don Norman / British Design Council 2005).
    
- **Nguyên tắc phản trực giác (Counter-intuitive Rule):** > "Never solve the problem I am asked to solve." – Don Norman, _The Design of Everyday Things_
    
- **Cảnh báo chiến lược:** Giải pháp xuất sắc cho sai vấn đề có thể còn tệ hơn không có giải pháp.
    
- **Khởi nguồn sản phẩm:** Khởi nguồn từ bài toán, không bắt đầu từ AI (Ba bài học thực tế về am hiểu lĩnh vực, quy mô thị trường và định vị giải pháp).
    
- **Lộ trình chuẩn:** Vấn đề $\rightarrow$ Quy trình vận hành $\rightarrow$ Chỉ số đo lường $\rightarrow$ Giải pháp AI.
    

### 2. Ba bài học thực tế từ thị trường

- **Lệch năng lực cốt lõi (Ví dụ từ Cursor):** Từ bỏ mảng AI thiết kế cơ khí để tập trung vào AI code editor – nơi đội ngũ am hiểu sâu sắc quy trình nghiệp vụ.
    
- **Sản phẩm tốt $\neq$ Thị trường lớn (Ví dụ từ Artifact):** Ứng dụng đọc tin tức tích hợp AI xuất sắc, nhưng quy mô thị trường quá hẹp để thương mại hóa thành công.
    
- **Định vị đúng điểm đau (Ví dụ từ NotebookLM):** Tập trung giải quyết nhu cầu hỏi đáp, tóm tắt trên tài liệu cá nhân và đối chiếu nguồn gốc bằng trích dẫn.
    

## CHƯƠNG 2: KHÁM PHÁ VÀ ĐỊNH NGHĨA VẤN ĐỀ (DIAMOND 1)

### 1. Diamond 1 — Tìm đúng vấn đề

> Phân kỳ để thấu hiểu sâu sắc, Hội tụ để lựa chọn chính xác.

#### Giai đoạn 1: DISCOVER (Phân kỳ) - Khám phá (Mở rộng góc nhìn)

- Quan sát thực tế (Observation)
    
- Phỏng vấn người dùng (User Interview)
    
- Khảo sát (Survey)
    
- Nhật ký hành vi (Diary Study)
    
- Phân tích dữ liệu / Nhật ký hệ thống
    
- Bản đồ các bên liên quan (Stakeholder Mapping)
    

#### Giai đoạn 2: DEFINE (Hội tụ) - Định nghĩa (Chọn lọc dựa vào dữ liệu)

- Sơ đồ đồng cảm / Gom nhóm (Affinity Mapping)
    
- Kỹ thuật đặt câu hỏi 5 Whys
    
- Ma trận Tác động – Nỗ lực (Impact-Effort)
    
- Biểu quyết bằng chấm tròn (Dot Voting)
    
- Câu hỏi mở hướng giải quyết (How Might We)
    
- Phát biểu bài toán (Problem Statement)
    

### 2. Quy trình thiết kế lấy con người làm trung tâm (HCD)

_(4 bước lặp lại bên trong mỗi Diamond — Don Norman)_

- **Observation (Quan sát):** Những người được quan sát phải phù hợp với đối tượng mục tiêu. Quan sát khách hàng tiềm năng trong cuộc sống bình thường, hiểu các tình huống thực tế họ gặp phải.
    
- **Ideation (Tạo ra ý tưởng):** Tạo nhiều ý tưởng, sáng tạo không bị ràng buộc bởi các hạn chế. Tránh phê bình ý tưởng của bản thân hay người khác. Đặt câu hỏi về tất cả mọi thứ.
    
- **Prototype (Tạo mẫu thử):** Tạo nguyên mẫu nhanh cho mỗi giải pháp tiềm năng. Mục tiêu là kiểm tra nhanh nhất có thể trước khi build.
    
- **Test (Kiểm tra):** Ngồi quan sát cách người dùng tương tác với Prototype trong thực tế.
    
- **Iteration (Lặp lại):** Tinh chỉnh và nâng cao liên tục.
    

## CHƯƠNG 3: PHƯƠNG PHÁP KHẢO SÁT VÀ SÀN LỌC BÀI TOÁN AI

### 1. Tìm bài toán AI ở đâu?

_Bắt đầu từ việc quan sát các hoạt động thực tế xung quanh. Tập trung nhận diện vấn đề; chưa vội đề xuất giải pháp._

- **Tác vụ lặp lại (Repetitive):** Việc diễn ra thường xuyên; công đoạn nào cần chuẩn hóa để hướng tới tự động hóa?
    
- **Tiêu tốn thời gian (Time-consuming):** Khối lượng xử lý lớn; thời gian hao phí ở bước nào (tìm kiếm, đọc hiểu, chờ đợi, định dạng)?
    
- **Lợi thế của AI (AI Advantage):** Tác vụ đòi hỏi phân tích ngữ cảnh, xử lý ngôn ngữ tự nhiên, tổng hợp đa nguồn.
    
- **Điểm đau người dùng (User Pain Points):** Ai đang gặp khó khăn, phàn nàn hoặc bị tắc nghẽn liên tục?
    

### 2. Bài tập thực hành: Nhận diện điểm đau thực tế

- Từ trải nghiệm ngày học đầu tiên, liệt kê ít nhất 3 điểm đau (pain points) bạn quan sát hoặc gặp phải.


### 3. Những câu hỏi nguyên bản

_Đôi khi insight bắt đầu từ việc đặt câu hỏi cho những điều hiển nhiên:_

- **Isaac Newton:** Quả táo rơi xuống đất — vậy _Mặt Trăng_ có đang "rơi" tự do không?
    
- **Polaroid:** Tại sao _không thể_ xem ảnh ngay lập tức sau khi chụp?
    
- **Airbnb:** Liệu _không gian sống bỏ trống_ có thể dùng làm dịch vụ lưu trú?
    

## CHƯƠNG 4: KHUNG PHỎNG VẤN VÀ CÂU HỎI CHIẾN LƯỢC

### 1. Câu hỏi gợi mở

_Đặt câu hỏi gợi mở để mở rộng tư duy trước khi lựa chọn bài toán:_
- Giả định hiển nhiên nào cần được lật lại ?
    
- Có cách tiếp cận nào hoàn toàn mới cho vấn đề ?
    
- Nếu thiết kế lại từ đầu và không bị giới hạn ?
    
- Tại sao bài toán này cần AI? Nếu không thì sao ?
    
- Quy trình nào đang tồn tại chỉ vì thói quen ?
    
- Có câu hỏi cốt lõi nào đang bị né tránh ?


### 2. Discovery interview: 5 câu hỏi nên hỏi stakeholder

1. **Vấn đề nhức nhối (Pain Point) là gì?** Tần suất lặp lại trong ngày hoặc trong tuần ra sao?
    
2. **Quy trình (Workflow) hiện tại như thế nào?** Công cụ nào được sử dụng ở từng bước, và ai bàn giao công việc cho ai?
    
3. **Thiệt hại (Cost) do vấn đề này gây ra là gì?** Hao phí cụ thể về thời gian xử lý, chi phí tài chính, cam kết dịch vụ (SLA) hay tỷ lệ chuyển đổi (conversion)?
    
4. **Hậu quả nếu hệ thống AI sai sót là gì?** Khâu nào cần con người tham gia kiểm soát (HITL/phê duyệt), hay AI chỉ hỗ trợ đưa ra gợi ý?
    
5. **Ai là người có quyền phê duyệt dự án (nói YES)?** Chỉ số hiệu quả (metric) và mức độ rủi ro (risk) nào sẽ trực tiếp quyết định việc đầu tư?


> **Lưu ý tối mật:** Nếu đối tác (stakeholder) không mô tả được quy trình hiện tại và chi phí thiệt hại khi xảy ra lỗi, mọi đề xuất giải pháp AI đều chỉ là phỏng đoán thiếu căn cứ.

## CHƯƠNG 5: CÁC SAI LẦM THƯỜNG GẶP (ANTI-PATTERNS) KHI TÍCH HỢP AI

_(Dấu hiệu cảnh báo bài toán chưa được định hình rõ hoặc giải pháp AI được lựa chọn quá sớm)_
> 📌 **Ghi nhớ Quan trọng:** Trước khi đánh giá hay triển khai luôn luôn phải tự hỏi: **Giải pháp AI này có thực sự cần thiết hay không?**

### 4 Sai lầm cốt lõi (Anti-patterns) cần tránh:

- **Ưu tiên giải pháp (Solution-first):** Xây dựng chatbot/agent trước khi làm rõ quy trình vận hành và điểm nghẽn thực tế.
    
- **Mơ hồ hiện trạng (No baseline):** Không lượng hóa tổn thất hiện tại, dẫn đến mất căn cứ đánh giá hiệu quả cải tiến.
    
- **Bỏ qua đánh giá (No evaluation):** Không thiết lập kịch bản kiểm thử, chỉ số đo lường hoặc phương án đối chứng.
    
- **Mập mờ ranh giới (No boundary):** Không rõ phạm vi tự chủ của AI và thời điểm cần con người phê duyệt (Human-in-the-loop).

### 🚨 Quy tắc xử lý khủng hoảng (Trigger Rule):
> Nếu phát hiện hệ thống hoặc ý tưởng đang mắc phải các sai lầm trên, hãy **quay lại làm rõ Problem Statement** trước khi chọn công nghệ.