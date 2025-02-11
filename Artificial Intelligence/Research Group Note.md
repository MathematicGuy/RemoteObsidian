note:
+ TA Thanh Huy - Medical Image Analysis (collab vs CMU)
+ **heuristic analysis:** đánh giá chủ quan theo kinh nghiệm.

---

## Brief Summarization:

### 1. Intro
- AI in Medical field **driven by advancement in IoT, 4/5G technology and computing power.**
- AI help improve **medical efficiency, reduce costs, and medicare**.

### 2. AI in Medical Informatics
+ Discuss key AI techniques such as **machine learning, NLP, deep learning, reinforcement learning, and heuristic analysis**.
+ Introduces AI frameworks (e.g. TF, Pytorchm) used in healthcare with clear ad/disadvantage. 
+ AI modeling methods + their integration in medical application.

### 3. The Application of AI in the Medical Field
+ $ The study highlights six major applications of AI in healthcare

**A. AI in Genomics**
+ AI-driven **gene sequencing and mutation detection** improve precision medicine.
+ ML in **Disease prediction and patient survival analysis**. 
+ DL in **Identifying genetic markers (dấu hiệu di truyền)** for diseases. 


**B. AI in Drug Discovery**
+ AI expedites **drug design, screening, and repurposing**.
+ ML identifying new drug-target interactions (xác định  tương tác của các loại thuốc có khả năng liên kết với mục tiêu nghiên cứu)
+ Enhances **virtual screening** to find **potential drugs faster**.


**C. AI in Medical Imaging**
+ AI *supports* **medical image segmentation, classification, and registration**.
+ DL **detects early signs of cancer and lung diseases**. 
+ **Improve image enhancement, retrieval and automated report generation**. 


**D. AI in Electronic Health Records (EHRs)**
> [[EHRs]] include patient's digital clinical notes and  informations.

- AI processes structured and unstructured EHR data for **disease prediction**.
	
- NLP extracts valuable insights from clinical texts (*văn bản lâm sàn ghi chép về tình trạng sức khỏe của bệnh nhân*).
	
- AI predicts **patient readmission, mortality rates, and treatment responses**.


**E. AI in Health Management**
+ Remote Healthcare
+ improve data privacy and security 

**F. AI in Medical Robotics**
+ *Assistant* in **Precision surgeries and rehabilitation**.
+ Diagnosti robots enhance medical decision-making.
+ Intelligent robot offer telemedicine

### 4. Challenges and Opportunities
- **Opportunities:** AI can revolutionize healthcare by enhancing **efficiency, precision, and accessibility**.
- **Challenges:**
    - **Data Privacy & Security:** Protecting sensitive patient data.
    - **Ethical Concerns:** AI decision-making in critical health scenarios.
    - **Technical Limitations:** Need for improved AI interpretability.
    - **Regulatory & Market Fragmentation:** Lack of standardized AI healthcare policies.

### 5. Future Outlook
- AI is expected to **advance predictive healthcare, automate diagnostics, and enhance robotic-assisted surgeries**.
- Future research will focus on **explainable AI, better data security, and improved AI-driven drug development**.


---

## 3.3 The Application of AI in Medical Imaging
+ $ Trong Medical Processing Technology, AI dùng CV để tối ưu và trợ giúp phân tích ảnh y tế để cung cấp thêm cơ sở để bác sĩ đánh giá tình trạng bệnh nhân.
+ ? This section focuses on the challenges and the corresponding solutions in the development of AI-assisted MPT in recent years (i.e $\leq 2024$ ) 
	**(A)** Two independent areas of medical imaging![[Pasted image 20250209162029.png]]
	+ **Imaging approaches:** ![[Pasted image 20250209145728.png]]
		+ **X-ray:** sử dụng bức xạ tia X để tạo ra hình ảnh 2D của các cấu trúc dày đặc như xương. *(Rẻ, dùng nhiều)*
		+ **Ultrasound:** sử dụng **sóng âm tần số cao** để tạo ra hình ảnh theo thời gian thực của các cấu trúc bên trong. *(an toàn)*
		+ **MRI**: sử dụng từ trường mạnh và sóng vô tuyến để **tạo ra hình ảnh mô mềm chi tiết.** (đắt, ít sử dụng)
		+ **PET**: sử dụng chất đánh dấu phóng xạ để **đo hoạt động trao đổi chất trong mô.** (có phóng xạ)
		+ **Microscopy:** kính hiển vi quan sát các cấu trúc nhỏ ở cấp độ tế bào.
		+ **CT:** sử dụng chùm tia X từ nhiều góc độ để tạo ra hình ảnh 3D chi tiết.
		+ **Endoscopy:** sử dụng ống mềm có gắn camera để quan sát các cơ quan bên trong.
		+ **Histopathology:** Sử dụng phương pháp kiểm tra mẫu mô bằng kính hiển vi (sinh thiết) để nghiên cứu bệnh.
	
	+ **processing approaches:**
		Image classification, detection and segmentation: ![[64aeb4a43a30bf1bbefd523f_types of image segmentation.webp]]
		 	
	 	**Image Enhancement:** cải thiện chất lượng ảnh giúp mô hình học và xử lý tốt hơn nhờ thay đổi cường độ sáng, tương phản của ảnh v.v. ![[Pasted image 20250209164932.png]]
		
		**Image Registration:** chuyển đổi góc nhìn dựa trên các điểm tương đồng giữa hình 2 hình ảnh.
		1) Xác đinh cạnh/viền của object/text trong 2 ảnh. 
		2) Chọn n điểm xung quanh các viền của các object/text trong 2 ảnh. 
		3) Tính số điểm tương đồng từ n điểm đó.![[Pasted image 20250209195459.png]]
		4) Biến đổi góc nhìn (perspective transformation) sử dụng phương pháp **[[Affine Transformation]]** - [reference](https://theailearner.com/2020/11/04/affine-transformation/). 
			![[images.png]]
			![[Pasted image 20250209181515.png]]
		
		**Image Generation:** Synthetic data là 1 phương pháp data augmentation nhằm giải quyết Bất cân bằng dữ liệu:  ![[Pasted image 20250209171345.png]]
		+ ? Các phương pháp **Image Augmentation** đơn giản biến đổi ảnh có trước trong khi **Synthetic Image** tạo hình ảnh hoàn toàn mới.
		+ **Augmentation Image** ![[Pasted image 20250209170825.png]]
		+ **Synthetic Image using DGAN (Deep Generative Adversarial Network):** Bao gồm 1 Generator để tạo dữ liệu ảnh tổng hợp dựa trên ảnh gốc và 1 Discriminator để phân biệt ảnh thật và giả, ảnh giả được output khi Discriminator không thể phân biệt ảnh thật và giả.![[jimaging-09-00069-g001.png]]
		

**(B)** Difficulties and solutions encountered in AI-based medical image processing technology.![[Pasted image 20250209162121.png]]
>**Hạn chế và Giải Pháp:**

1. **Thiếu dữ liệu y tế công khai** (Bác sĩ quá bận để gán nhãn dữ liệu) → **Chất lượng dữ liệu thấp**.
    
    - **Giải pháp:** Học bán giám sát (semi-supervised learning) người + máy, học không giám sát (unsupervised learning), sử dụng mạng GAN để tổng hợp dữ liệu (i.e. synthetic data)
      semi-supervised learning: ![[1_snZhMEQFhoJwbM5c0CPOAw.png]]
      
2. **Vấn đề đạo đức, dữ liệu không đảm bảo chất lượng**.
    
    - **Giải pháp:** Áp dụng các phương pháp **tiền xử lý dữ liệu** như làm sạch nhiễu, kiểm định chất lượng.
      
3. **Dữ liệu đầu vào kém chất lượng dẫn đến mô hình kém hiệu quả ("Garbage in, garbage out")**.
    
    - **Giải pháp:** Tăng cường dữ liệu (Data Augmentation), cải tiến thuật toán thích ứng (Adaptive Algorithm) -  e.g. CLAHE  
	    [[Histogram Equalization]]: ![[Contrast-limited-adaptive-histogram-equalization-method-a-low-contrast-input-image-b.jpg]]
	    CLAHE (**Contrast Limited Adaptive Histogram Equalization**):  **CLAHE** divide the image into *n* 8x8 tiles, then **apply Histogram Equalization into each tile**. ![[Pasted image 20250209182759.png]]
    
4. **Khác biệt về cơ thể giữa người nước ngoài và người Việt Nam → Label bị Sai lệch -> Labeling Bias**
    
    - **Giải pháp:** Phân tích dữ liệu đa miền (Cross-domain Data Analysis), cải thiện phương pháp gán nhãn bằng học bán giám sát.
	
5. **Trách nhiệm và độ tin cậy** → Mô hình AI y tế chỉ nên được sử dụng dưới sự giám sát của chuyên gia thay vì thay thế trong các tasks quan trọng.

### 3.3.1. Detection and Classification
**Data:** ảnh gray scale (e.g., MRI, CT, X-ray, etc.) dạng 2D hoặc 3D voxels. Trích xuất từ file **DICOM** (file chuyên cho dữ liệu y tế), các ảnh thường đc phân loại do có độ phân giải khác nhau vì pixel của các mô da có độ tương đồng cao khi độ phân giải ảnh thấp. 
	vd: mắt người nhìn tốt ảnh 8-bits là từ 0-256, DL học tốt ảnh 12-bits từ 0-4096 -> 1 ảnh ~ 23mb.

reference: [pixels from digital photos to medical images](https://www.marychin.org/pixvox.html)
![[Pasted image 20250209153910.png]]

**Survey Image**
![[Pasted image 20250209152851.png]]
**Ảnh tham khảo cho TH segment:** 
![[12859_2023_5235_Fig1_HTML.png]]
**2-stage Deep Learning Method** để phát hiện và phân loại các nốt sần trên phổi trong **chụp CT (ảnh chụp cắt lớp)**

note: 
+ MIP - Phương pháp Chiếu Cường Độ Tối Đa trong y tế để tăng cường khả năng hiển thị cấu trúc "phổi", trong ảnh MIP đc áp dụng cho từng lớp cắt ảnh CT khác nhau. 
+ **Nodules/Nốt sần** là vùng mô bất thường. 

**Bước 1: Maximum Intensity Projection ([MIP](https://3dqlab.stanford.edu/what-is-a-mip/)) - Phần a)**
+ **Đầu vào:** Mô hình lấy các lát cắt trục từ ảnh chụp CT.
+ **Xử lý MIP:** Áp dụng Chiếu cường độ tối đa (MIP) trên các lát cắt có độ dày khác nhau (1 mm, 5 mm, 10 mm, 15 mm)
	**Thin slices** (1mm, 5mm) → Chụp các chi tiết nhỏ như các nốt nhỏ.
	**Thick slices** (10mm, 15mm) → Cung cấp cái nhìn tổng quan rộng hơn về các cấu trúc lớn hơn trong khi giảm noise.
	
+ **Mục đích:**
	+ MIP tăng cường các vùng sáng (ví dụ: nốt sần) bằng cách hiển thị pixel cường độ tối đa dọc theo trục xem.
	+ Giúp phân biệt nốt sần phổi với mạch máu, vì mạch máu trông dài ra trong khi nốt sần tròn.

**Bước 2: Trích xuất và hợp nhất tính năng đa thang đo - Phần b)**
+ **Đầu vào:** Các hình ảnh MIP được truyền qua các lớp CNNs.
+ **Hợp nhất tính năng:** Các features của từng ảnh MIP được hợp nhất để cung cấp biểu diễn toàn diện hơn về vùng phổi.
+ **Mục đích:**
	+ Các độ dày lát cắt khác nhau cho phép mô hình **chụp các nốt nhỏ và lớn** một cách hiệu quả.
	- Ngăn ngừa kết quả dương tính giả bằng cách **giảm các cấu trúc giống mạch máu**

**Bước 3: Phân loại bằng CNN 3D (Phần c)**
+ **Đầu vào:** Các tính năng được hợp nhất được xử lý bởi bộ phân loại CNN 3D.
+ **Softmax Classification:** Lớp cuối cùng áp dụng hàm softmax để phân loại đối tượng được phát hiện thành:
	+ Nốt sần
	+ Không phải nốt sần (ví dụ: mạch máu, nhiễu hoặc mô bình thường) 
	
+ Giảm dương tính giả: CNN 3D giúp tinh chỉnh các dự đoán bằng cách xem xét bối cảnh không gian.

### 3.3.2. Medical Image Segmentation
*I'm Empty*

### 3.3.3. Medical Image Registration
Data: 2D + 3D Image using CNN to detect and reduce false-positive 
Công Thức: Affine Transformation 

**Bước 1: Trích xuất đặc trưng (Lấy điểm đặc trưng)**

- **Ảnh cố định** (tham chiếu) và **ảnh di chuyển** (cần biến đổi) được **nhập vào mạng đăng ký**.
- **Mạng trích xuất các điểm đặc trưng**, đại diện cho các cấu trúc quan trọng (ví dụ: cạnh, đường viền, điểm đặc biệt).
- Các đặc trưng này có thể được phát hiện bằng:
    - **Phương pháp truyền thống:** SIFT, SURF, ORB, Harris Corner Detection.
    - **Phương pháp học sâu:** CNN, U-Net, VoxelMorph.  
+ $ **Mục đích:** Xác định các đặc trưng quan trọng trong cả hai ảnh để thực hiện căn chỉnh.


**Bước 2: Tính toán ma trận tương đồng (Ghép nối đặc trưng)**

- Một **ma trận tương đồng** được xây dựng để tìm **cặp đặc trưng tương ứng** giữa hai ảnh.
- **Các tiêu chí đo độ tương đồng phổ biến:**
    - **MSE (Sai số bình phương trung bình)** → Dùng cho ảnh cùng loại (ví dụ: CT-to-CT).
    - **MI (Thông tin tương hỗ)** → Dùng cho ảnh khác loại (ví dụ: MRI-to-CT).
    - **NCC (Tương quan chéo chuẩn hóa)** → Đánh giá mức độ tương quan giữa cường độ pixel.  
+ $ **Mục đích:** Đánh giá mức độ khớp giữa ảnh di chuyển và ảnh cố định.


**Bước 3: Tính toán phép biến đổi không gian (Trường biến dạng)**
- **Các tham số biến đổi** được tính dựa trên các điểm đặc trưng đã khớp.
- **Các loại phép biến đổi:**
    - ? **Affine Transformation** (Biến đổi affine) → Co giãn + Nghiêng (cho phép thay đổi hình dạng nhẹ).
    - **Rigid Transformation** (Biến đổi cứng) → Xoay + Tịnh tiến (bảo toàn hình dạng).
	- **Non-Rigid Transformation (Deformable Registration)** → Biến dạng dựa trên **trường biến dạng**.  
	    vietsub: Biến đổi phi tuyến (???)
+ $ **Mục đích:** Tìm phép biến đổi tốt nhất để giảm thiểu sai lệch giữa hai ảnh.


**Bước 4: Lấy mẫu lại ảnh và thực hiện biến đổi**
- **Phép biến đổi tối ưu** được áp dụng cho ảnh di chuyển.
- Ảnh di chuyển được **lấy mẫu lại** bằng các kỹ thuật nội suy:
    - Nearest Neighbor (Gần nhất)
    - Bilinear Interpolation (Nội suy song tuyến)
    - Bicubic Interpolation (Nội suy ba khối)
- Ảnh sau biến đổi giờ đây đã **căn chỉnh với ảnh cố định**.  
+ $ **Mục đích:** Tạo ra ảnh đã được đăng ký phù hợp với ảnh tham chiếu.


**3.3.4. Other Applications of AI in Medical Imaging**
*I'm Pass*


---

Note: mentions that you can merge and combine 2 model together. 
Detail overview about part 3.3. The Application of AI in Medical Imaging
**Input Image:** DICOM file convert to PNG Image
Medical Image Technology (MIT)
	Applied OCT, Ultra Sound, MRI
Medical Image Processing (MPT)


