Mình vừa phỏng vấn 8 ứng viên Data Analyst tuần này. 7 người fail cùng 1 câu hỏi: "Em xử lý missing data như thế nào?" Câu trả lời tiêu chuẩn (và sai):
- "Em fillna() bằng mean/median"
- "Em drop hết missing values"
- "Em dùng KNN imputation"

Họ trả lời THUẬT TOÁN trước khi hiểu BỐI CẢNH.
Người duy nhất pass hỏi ngược lại mình 3 câu:
- Missing này là MAR, MCAR hay MNAR ?
- Business impact nếu drop vs nếu fill sai là gì ?
- Stakeholder cần accuracy hay coverage ?

Đây là điều phân biệt junior với senior. Junior nghĩ data cleaning là kỹ thuật. Senior hiểu đó là business decision.
Ví dụ thực tế từ dự án retention model tuần trước:
- 30% user không có income data
- Junior: "Anh ơi em fill median nhé"
- Senior: "30% này là freelancer không khai thu nhập. Nếu fill median, model sẽ nghĩ họ giống nhóm income trung bình và predict sai behavior. Đề xuất: tạo category riêng 'income_unknown' hoặc dùng proxy feature là spending pattern"

Impact: AUC tăng từ 0.72 lên 0.79 chỉ vì cách handle missing đúng.
3 câu hỏi mình luôn hỏi trước khi xử lý missing data:
- Tại sao data missing ? (User behavior, system error, hay privacy choice ?)
- Missing pattern có correlation với target variable không ?
- Cost của false positive vs false negative trong business context này là bao nhiêu ?

Kỹ thuật là dễ. Google là ra fillna(), SimpleImputer, MICE. Khó là biết KHI NÀO dùng cái gì và TẠI SAO. 
Bạn handle missing data như thế nào trong dự án gần nhất? Có bao giờ quyết định KHÔNG fill missing mà để nguyên không ?

----

Sự khác biệt giữa Junior và Senior đúng như bạn nói: **Kỹ thuật là dễ, tư duy bối cảnh mới khó**.

Để trả lời câu hỏi của bạn về dự án gần nhất và tình huống không fill missing:
1. Dự án gần nhất: Phân tích tỷ lệ huỷ dịch vụ (Churn Prediction)
- **Bối cảnh:** Dữ liệu hành vi người dùng trên App.
- **Vấn đề:** Cột `last_login_date` bị missing khoảng 5%.
- **Tư duy:** Không phải cứ thấy missing là `fillna()`.
- **Xử lý:**
    - **Phân tích (Root Cause):** Nhóm missing này _thực chất_ là nhóm chưa bao giờ login kể từ khi đăng ký tài khoản (User mới hoàn toàn, hệ thống ghi nhận lỗi logic).
    - **Quyết định:** Tạo ra một giá trị mặc định là `1970-01-01` hoặc biến thành biến nhị phân `is_first_time_user` thay vì dùng median/mean (làm sai lệch thời gian login trung bình).
- **Kết quả:** Mô hình hiểu được đây là nhóm "New user" và có hành vi đặc thù.

1. Tình huống: QUYẾT ĐỊNH KHÔNG FILL MISSING (Để nguyên). Trong một dự án xây dựng hệ thống **Credit Scoring (Chấm điểm tín dụng)**:
- **Dữ liệu:** Cột `credit_limit_at_other_banks` (Hạn mức tín dụng ở ngân hàng khác) bị missing 40%.
- **Tại sao không fill?**
    - Missing ở đây là **MNAR (Missing Not At Random)**: Khách hàng không có nợ xấu hoặc không dùng thẻ ngân hàng khác, hoặc họ cố tình không khai báo.
    - Nếu dùng `mean/median`, mình sẽ tạo ra một giá trị ảo, làm sai lệch rủi ro.
    - Nếu drop 40% data, mô hình mất đi thông tin quý giá của một nhóm lớn.
- **Giải pháp:** **Giữ nguyên NULL** và sử dụng thuật toán **XGBoost/LightGBM**. Các thuật toán này có khả năng tự học được "hướng đi" của giá trị thiếu (tự phân loại nhóm NULL vào nhánh tối ưu).
- **Impact:** AUC của mô hình cao hơn hẳn so với việc cố tình điền 0 hoặc điền trung bình.

---
Tóm lại
Với mình, **Missing Data = Information**.  
Trước khi `fillna()`, câu hỏi mình tự đặt ra là: _"Liệu việc thiếu dữ liệu này có mang lại insight gì về hành vi không?"_
