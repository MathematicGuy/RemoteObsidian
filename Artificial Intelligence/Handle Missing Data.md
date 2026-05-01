Mình vừa phỏng vấn 8 ứng viên Data Analyst tuần này. 7 người fail cùng 1 câu hỏi: "Em xử lý missing data như thế nào?"
Câu trả lời tiêu chuẩn (và sai):
- "Em fillna() bằng mean/median"
- "Em drop hết missing values"
- "Em dùng KNN imputation"
Họ trả lời THUẬT TOÁN trước khi hiểu BỐI CẢNH.
Người duy nhất pass hỏi ngược lại mình 3 câu:
- Missing này là MAR, MCAR hay MNAR?
- Business impact nếu drop vs nếu fill sai là gì?
- Stakeholder cần accuracy hay coverage?
Đây là điều phân biệt junior với senior. Junior nghĩ data cleaning là kỹ thuật. Senior hiểu đó là business decision.
Ví dụ thực tế từ dự án retention model tuần trước:
- 30% user không có income data
- Junior: "Anh ơi em fill median nhé"
- Senior: "30% này là freelancer không khai thu nhập. Nếu fill median, model sẽ nghĩ họ giống nhóm income trung bình và predict sai behavior. Đề xuất: tạo category riêng 'income_unknown' hoặc dùng proxy feature là spending pattern"
Impact: AUC tăng từ 0.72 lên 0.79 chỉ vì cách handle missing đúng.
3 câu hỏi mình luôn hỏi trước khi xử lý missing data:
- Tại sao data missing? (User behavior, system error, hay privacy choice?)
- Missing pattern có correlation với target variable không?
- Cost của false positive vs false negative trong business context này là bao nhiêu?
Kỹ thuật là dễ. Google là ra fillna(), SimpleImputer, MICE. Khó là biết KHI NÀO dùng cái gì và TẠI SAO.
Bạn handle missing data như thế nào trong dự án gần nhất? Có bao giờ quyết định KHÔNG fill missing mà để nguyên không?