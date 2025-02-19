[[OpenPose vs MediaPipe - How They Work and Key Differences]]

1. **Dữ liệu đầu vào (Classroom Camera):**
    
    - **Mục đích:** Cung cấp dữ liệu hình ảnh thô cho hệ thống.
        
    - **Phương pháp:** Sử dụng camera để ghi lại video hoặc chuỗi hình ảnh của lớp học.
        
2. **Phát hiện người (Person Detection):**
    
    - **Mục đích:** Xác định vị trí của người trong khung hình, loại bỏ các thông tin không cần thiết từ hậu cảnh.
        
    - **Phương pháp:** Có thể sử dụng các phương pháp như:
        
        - **Faster R-CNN, YOLO, SSD:** Các mô hình object detection dựa trên deep learning.
            
        - **HOG + SVM:** Histogram of Oriented Gradients kết hợp với Support Vector Machine.
            
        - **Background subtraction:** Trừ nền để phát hiện đối tượng chuyển động.
            
3. **Ước lượng dáng điệu (Pose Estimation):**
    
    - **Mục đích:** Xác định vị trí các khớp trên cơ thể người (keypoints) từ hình ảnh hoặc video.
        
    - **Phương pháp:** Các phương pháp phổ biến bao gồm:
        
        - **OpenPose:** Phương pháp dựa trên Part Affinity Fields (PAFs) để kết nối các keypoints.
            
        - **PoseNet, HRNet:** Các mô hình deep learning khác cho ước lượng dáng điệu.
            
4. **Dữ liệu khung xương (Skeleton Data):**
    
    - **Mục đích:** Biểu diễn dáng điệu của người dưới dạng một bộ khung xương được tạo từ các keypoints đã được ước lượng.
        
    - **Phương pháp:** Kết nối các keypoints tương ứng để tạo thành khung xương.
        
5. **Dữ liệu khung xương đã chỉnh sửa (Corrected Skeleton Data):**
    
    - **Mục đích:** Loại bỏ nhiễu, xử lý các keypoints bị thiếu hoặc sai lệch để có được dữ liệu khung xương chính xác hơn.
        
    - **Phương pháp:** Có thể sử dụng các kỹ thuật sau:
        
        - **Temporal smoothing:** Làm mịn dữ liệu theo thời gian.
            
        - **Interpolation:** Nội suy để bổ sung các keypoints bị thiếu.
	    - **Kalman filter:**
		    - **Giảm nhiễu:** Bộ lọc Kalman có thể giúp loại bỏ nhiễu này và tạo ra một đường dẫn mượt mà hơn cho chuyển động của các khớp.
		    - **Dự đoán vị trí của các keypoint bị thiếu dựa trên các keypoint đã được phát hiện trước đó** và mô hình chuyển động. (Giống việc xác định 4 góc từ 3 trong nhận diện thẻ CCCD)
		    - **Dự đoán chuyển động:** Bộ lọc Kalman có thể được sử dụng để dự đoán vị trí của các khớp trong tương lai -> dự đoán hành động, hành vi.
            ![[figure-kalman-filter-algorithm-scalar.png]]
            ![[Pasted image 20250116152939.png]]
            ![[Pasted image 20250116153214.png]]
1. **Tiền xử lý dữ liệu khung xương (Pre-processing Skeleton Data):**
    
    - **Mục đích:** Chuẩn bị dữ liệu khung xương cho bước trích xuất đặc trưng.
        
    - **Phương pháp:** Các kỹ thuật tiền xử lý có thể bao gồm:
        
        - **Normalization:** Chuẩn hóa dữ liệu về một khoảng giá trị nhất định.
            
        - **Data augmentation:** Tăng cường dữ liệu bằng cách xoay, lật, phóng to, thu nhỏ,...
            
7. **Trích xuất đặc trưng (Feature Extraction):**
    
    - **Mục đích:** Trích xuất các đặc trưng đại diện cho dáng điệu từ dữ liệu khung xương đã được tiền xử lý.
        
    - **Phương pháp:** Bài báo sử dụng ba loại đặc trưng:
        
        - **Vị trí khớp được chuẩn hóa (Normalized Joint Location):** Chuẩn hóa tọa độ của các keypoints.
            
        - **Khoảng cách giữa các khớp (Joint Distances):** Tính toán khoảng cách Euclidean giữa các cặp keypoints.
            
        - **Góc của xương (Angle of Bones):** Tính toán góc giữa các xương.
            
8. **Mô hình DNN (DNN Model):**
    
    - **Mục đích:** Phân loại hành vi dựa trên các đặc trưng đã được trích xuất.
        
    - **Phương pháp:** Sử dụng mạng nơ-ron sâu (DNN), cụ thể là các lớp fully connected (FC) để học và phân loại hành vi.
        
9. **Phân loại hành vi (Behavior Classification):**
    
    - **Mục đích:** Gán nhãn hành vi cho dữ liệu đầu vào.
        
    - **Phương pháp:** Sử dụng đầu ra của mô hình DNN để dự đoán nhãn hành vi.
        
10. **Kết quả hành vi (Behaviour Result):**
    
    - **Mục đích:** Cung cấp kết quả phân loại hành vi.


