### Core Themes (Chủ đề được quan tâm chính)

- **Behaviour Detection:** Across various domains (general, healthcare, security).
    "human behavior detection," "anomaly detection," "suspicious activity recognition," "activities of daily living detection.
    
- **Computer Vision:** Applied to behaviour, medical images, and potentially time series visualization.
    "vision-based behavior analysis," "video anomaly detection," "pose estimation for behavior analysis."
    
- **Time Series Analysis:** Focusing on healthcare, specifically anomaly detection and prediction.
    "healthcare time series anomaly detection," "vital signs analysis," "disease progression prediction," "readmission prediction."
    
- **Medical Image Analysis:** Segmentation, analysis, and diagnosis.
    "medical image segmentation," "medical image classification," "deep learning medical imaging," "lung cancer detection CT."
    
- **Adversarial Attacks:** Specifically in healthcare contexts for both images and time series.
    "adversarial attacks medical images," "adversarial attacks healthcare time series," "robust medical AI."
    
- **Robustness/Security of AI in Healthcare.**


### Work Flow cho Dự án tiềm năng có thể phối hợp trong Tương Lai


**1. Dự án tập trung vào Behaviour Detection trong Y tế (kết hợp Time Series và Computer Vision):**

- **Tên dự án tiềm năng:** **"Nhận diện và Phân tích Hành vi Bất thường trong Môi trường Chăm sóc Sức khỏe"**
    
- **Mục tiêu:** Phát triển một hệ thống toàn diện để phát hiện các hành vi bất thường trong môi trường y tế, sử dụng cả dữ liệu hình ảnh (Computer Vision) và dữ liệu chuỗi thời gian (Time Series).
    
- **Phối hợp:**
    
    - **Thành:** Tập trung vào việc phát triển các mô hình Computer Vision để **nhận diện các hành vi bất thường của bệnh nhân** (ví dụ: ngã, vật lộn, biểu hiện đau đớn) hoặc nhân viên y tế (ví dụ: thao tác sai quy trình).
        
    - **Hà:** Tập trung vào việc **phân tích dữ liệu chuỗi thời gian** (ví dụ: nhịp tim, huyết áp, SpO2 (oxy trong máu)) để phát hiện các dấu hiệu bất thường có thể liên quan đến các sự kiện y tế khẩn cấp (ví dụ: sốc nhiễm trùng, đau tim).
        
    - **Linh:** Nghiên cứu các **phương pháp phát hiện hành vi bất thường trong các hoạt động sinh hoạt hàng ngày** (ADL) của bệnh nhân, có thể cung cấp bối cảnh quan trọng cho các phát hiện từ dữ liệu hình ảnh và chuỗi thời gian.
        
    - **Huân:** Nghiên cứu về tính mạnh mẽ (robustness) của hệ thống trước các tấn công đối nghịch (adversarial attacks) vào cả dữ liệu hình ảnh và chuỗi thời gian, đảm bảo độ tin cậy của hệ thống trong môi trường y tế.
		hoặc Nghiên cứu **Image Augmentation in Imbalanced Medical Dataset sử dụng adversarial attacks (Discriminator)**   
	
- **Tiềm năng phát triển:** Kết hợp thông tin từ camera giám sát (Computer Vision) và các thiết bị theo dõi sức khỏe (Time Series) để cung cấp một cái nhìn toàn diện hơn về tình trạng và hành vi của bệnh nhân.


**2. Dự án tập trung vào Ứng dụng Computer Vision trong Chẩn đoán và Phân tích Hình ảnh Y tế:** 
*(Phương, Tùng)*

- **Tên dự án tiềm năng:** **"Nền tảng Hỗ trợ Chẩn đoán Ung thư Phổi Tích hợp Dữ liệu Đa phương thức"**
    
- **Mục tiêu:** Xây dựng một nền tảng sử dụng AI để hỗ trợ các bác sĩ trong việc chẩn đoán ung thư phổi từ ảnh chụp CT, đồng thời khám phá các phương pháp tối ưu hóa và cải thiện hiệu suất của các mô hình phân tích hình ảnh y tế.
    
- **Sự phối hợp:**
    
    - **Nguyễn Ái Phương:** Tập trung vào việc nghiên cứu và áp dụng các kỹ thuật tối ưu hóa mô hình (ví dụ: active learning, semi-supervised learning) để cải thiện độ chính xác và hiệu quả của các mô hình phân đoạn và phân tích hình ảnh CT phổi.
        
    - **Trần Anh Tùng:** Tập trung vào việc phát triển và đánh giá các mô hình deep learning để tự động phát hiện và phân loại các nốt phổi nghi ngờ ung thư trên ảnh CT.
        
- **Tiềm năng phát triển:** Kết hợp với các nghiên cứu về Behaviour Detection (ví dụ: phát hiện các triệu chứng ban đầu của bệnh nhân thông qua quan sát) để cung cấp thông tin đầu vào cho quá trình chẩn đoán.
    

**3. Dự án tập trung vào Bảo mật và Tin cậy cho các Hệ thống AI trong Y tế:**

- **Tên dự án tiềm năng:** **"Phát triển Các Giải pháp AI An toàn và Tin cậy cho Chăm sóc Sức khỏe"**
    
- **Mục tiêu:** Nghiên cứu và phát triển các phương pháp bảo vệ các hệ thống AI trong lĩnh vực y tế khỏi các tấn công đối nghịch và đảm bảo tính tin cậy của các dự đoán và quyết định do AI đưa ra.
    
- **Sự phối hợp:**
    
    - **Phạm Đình Huân:** Nghiên cứu về các phương pháp tấn công đối nghịch (adversarial attacks) vào dữ liệu hình ảnh y tế và dữ liệu chuỗi thời gian, cũng như các biện pháp phòng thủ hiệu quả. Đồng thời, khám phá các khía cạnh bảo mật của việc sử dụng Large Language Models (LLMs) trong y tế.
        
    - **Nguyễn Lương Thanh Hà:** Nghiên cứu về độ tin cậy và khả năng giải thích của các mô hình AI dự đoán bệnh tật và các biến cố y tế, đặc biệt là khi đối mặt với dữ liệu nhiễu hoặc bị tấn công.
        
- **Tiềm năng phát triển:** Xây dựng các framework và công cụ để đánh giá và tăng cường tính an toàn và tin cậy của các hệ thống AI được triển khai trong môi trường y tế.