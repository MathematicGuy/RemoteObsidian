### **PROBLEM STATEMENT LIST: FPT STOCK PREDICTION**
+ ? Nhớ list ra nhưng điều thiết thực tế và thiếu hụt của Dataset. 
+ ! Nhớ bao gồm cả cách tính điểm. (tính MSE cho từng điểm trong vòng 50-100 ngày)
+ ? **Main Problem Statement (Liệt kê vấn đề chính nổi bật nhất):** Theo logic thì model học máy chỉ sử dụng dữ liệu cổ phiếu thuần thì việc dự đoán đúng 1 pattern nó chưa từng được học là gần như không thể. **Trong bài, cổ phiếu FPT giảm sâu tới -28.74%, 1 trend mà các mô tuyến tính không thể ngờ tới, nhất là khi TREND của cổ phiếu đang ĐI LÊN và chưa từng giảm Sau 1 Thời Gian Dài.**  
+ @ Vì thế mình cần có thêm các yếu tố thứ 3, như 1 quy luật trong cổ phiếu, threshold đảm bảo dự đoán cô phiếu sẽ âm, phân tích cảm xúc để xác định tính thiên vị của tin tức về công cty đó, vân vân và mây mây.
+ $ Vì bài toán yêu cầu chỉ dùng model tuyến tính, nên việc tích hợp các quy luật trong cổ phiếu là điều tất yếu để giúp mô hình hiểu khi nào là lúc giảm sau 1 thời gian tăng đều đặn.    
![[Pasted image 20251205132542.png]]
+ ? VÌ có rất nhiều kiến thức Kinh Tế về cổ phiếu, thay vì overload ng đọc, đi tới đâu giải thích tới đó. 

### **PROBLEM STATEMENT LIST: FPT STOCK PREDICTION (2020-2025)**

#### **1. TỔNG QUAN BÀI TOÁN**

- **Dữ liệu:** ~1150 mẫu (ngày giao dịch), bao gồm các biến: `time`, `open`, `high`, `low`, `close`, `volume`.
    
- **Giai đoạn:** 2020 - 2025 (Chứa đựng các giai đoạn biến động mạnh: COVID-19 crash, uptrend 2021, downtrend 2022, và phục hồi sau 2022).
    
- **Thách thức cốt lõi:** Dữ liệu quá ngắn (~4.5 năm) để training các mô hình Deep Learning lớn (như Transformer), nhưng lại yêu cầu dự báo xa (100 ngày ~ 9% tổng lượng dữ liệu).
    
- **Baseline hiện tại:** Chỉ dùng `Close` với mô hình Linear, bỏ qua toàn bộ thông tin quan trọng khác.

#### **2. VẤN ĐỀ CHÍNH (CRITICAL ISSUES) - CẬP NHẬT THEO DATASET**

- **2.1. Lãng phí tài nguyên dữ liệu (Waste of Information)**
    
    - **Vấn đề:** Baseline hiện tại chỉ dùng cột `Close`.
        
    - **Phân tích Dataset:** Bạn có sẵn `Open`, `High`, `Low` và đặc biệt là `Volume`.
        
        - **Volume:** Là "nhiên liệu" của giá. Giá tăng mà Volume giảm thường báo hiệu đảo chiều. Bỏ qua Volume là mất 50% thông tin thị trường.
            
        - **High/Low:** Cho biết độ biến động trong ngày (Intraday Volatility). Dữ liệu giai đoạn 2020-2025 biến động rất mạnh, High/Low chứa đựng thông tin về tâm lý sợ hãi/hưng phấn cực độ mà `Close` không thể hiện hết.
            
- **2.2. Chiến lược dự báo 100 ngày trên tập dữ liệu nhỏ (Small Data Horizon Problem)**
    
    - **Vấn đề:** Dự báo 100 bước (steps) chỉ với 1150 mẫu huấn luyện là tỷ lệ rủi ro cao.
        
    - **Phân tích:** Với mô hình hồi quy đệ quy (Recursive) hiện tại, chỉ cần bước dự báo thứ 5 hoặc 10 bị sai, thì đến bước 50-100, kết quả sẽ hoàn toàn vô nghĩa. Với tập dữ liệu nhỏ, mô hình không đủ lịch sử để học được các chu kỳ dài hạn (như chu kỳ kinh tế vĩ mô) để hỗ trợ cho việc dự báo xa như vậy.
        
- **2.3. Rủi ro Overfitting do chế độ thị trường (Market Regime Shifts)**
    
    - **Vấn đề:** Dữ liệu 2020-2025 trải qua các "Market Regimes" rất khác nhau:
        
        - 2020-2021: Tiền rẻ, tăng trưởng nóng.
            
        - 2022-2023: Lạm phát, lãi suất cao, điều chỉnh mạnh.
            
    - **Hậu quả:** Một mô hình đơn giản (Linear) học trên toàn bộ tập này sẽ cố gắng tìm một "đường trung bình" cho tất cả các giai đoạn, dẫn đến việc không dự báo đúng cho giai đoạn hiện tại (2025) nếu đặc tính thị trường thay đổi.
        

---

#### **3. VẤN ĐỀ KỸ THUẬT CỤ THỂ (SECONDARY ISSUES)**

- **3.1. Sai lầm trong xử lý chuỗi thời gian (Time Indexing)**
    
    - **Vấn đề:** File `submission.csv` yêu cầu `id` từ 1-100, nhưng file train lại có cột `time` (YYYY-MM-DD).
        
    - **Chi tiết:** Code baseline đang bỏ qua cột `time`. Trong chứng khoán, "Ngày trong tuần" (thứ 2 thường đỏ, thứ 6 hay chốt lời) và "Tháng" (hiệu ứng tháng 5, tháng 12) là các đặc trưng (features) quan trọng. Cần convert cột `time` thành các feature số học (DayOfWeek, Month, Quarter).
        
- **3.2. Thiếu các biến phái sinh (Derived Features)**
    
    - **Vấn đề:** Với dữ liệu giới hạn (chỉ 5 cột gốc), mô hình Deep Learning sẽ khó học.
        
    - **Giải pháp:** Cần tạo ra các biến phái sinh từ OHLCV để "mớm" kiến thức cho mô hình. Ví dụ:
        
        - `(Close - Open) / Open`: Lực nến trong ngày.
            
        - `(High - Low) / Close`: Biên độ dao động.
            
        - `Close / Moving_Average(20)`: Xu hướng ngắn hạn so với trung hạn.
            
- **3.3. Chiến lược Validation chưa phù hợp với dữ liệu mỏng**
    
    - **Vấn đề:** Nếu bạn cắt 100 ngày cuối để làm Validation (để khớp với yêu cầu dự báo 100 ngày), bạn sẽ mất gần 10% dữ liệu train quý giá.
        
    - **Hậu quả:** Mô hình thiếu dữ liệu mới nhất để học xu hướng gần đây. Cần cân nhắc chiến lược **Walk-Forward Validation** hoặc chỉ cắt 30-50 ngày để Validate xu hướng thay vì cắt đủ 100 ngày.
        
