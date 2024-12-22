note:
+ use google new SOTA model to hight light study path and solutions and reason why
+ additional: Maybe walk throught AI using Time Series ?
+ **AI in Image Steganography**
	Abstract: **Steganography** (thuật ẩn chữ) is the practice of **encoding secret information into innocuous content** in such a manner that an **adversarial third party would not realize that there is hidden meaning.**
	(mã hóa thông tin bí mật thành nội dung vô hại)


# AI in Medical
**Keywords:** AI, health, deep learning, machine learning, natural language processing, federated learning

### Intro:
**Challenges:** associated with traditional ML methodologies, such as logistic regression or support vector machine (SVM) methods, is the need for feature engineering. 
+ ? Feature engineering is the process of obtaining higher level feature representations from raw patient features.
+ $ DL address this problem by adopting an end-to-end learning architecture, using raw patient data as an input and mapping it to outcomes through multiple layers of nonlinear processing units (i.e., neurons). Allow minimize human contribute in feature engineering.

### Available dataset (a lot)
**5 major types of data used in AI for health: **
+ multi-omics data, 
+ clinical data, 
+ behavioral/wellness data,
+ environmental data,
+ research and development data.

### 3 AI for Common Biomedical Data Types
#### 3.1 Multi-omics Data
+ ? mean **different** **“-omics” data**, such as *genomics, proteomics, transcriptomics, epigenomics, and microbiomics* are jointly collected and analyze

>Multi-omics offer a comprehensive understanding of biological processes.

#### 3.2 Clinical Data
+ ? Including medical images, electronic health records (EHRs), and physiological signals.
##### 3.2.1 Medical Images
+ $ **Conventional ML** approaches for a**nalyzing medical images are often based on feature engineering**, where **features or descriptors of the medical images are extracted** and then fed into the learning models for different tasks such as **segmentation or classification.**
#### 3.3 Behavioral Data
>Investigate the relationship between behavior data and health.

Ex:
+ Identified associations between Twitter posts and the risk of cardiovascular disease (bệnh tim mạch)
	users with **cardiovascular disease can be characterized by the tone, style, and perspective of their tweets**, as well as some basic demographics (cách nói chuyện)
+ Tencent, the Chinese tech giant, claims to have developed a vision system that can spot Parkinson’s Disease in 3 minutes [61](https://pmc.ncbi.nlm.nih.gov/articles/PMC6697503/#ORwang-61)
+ Health care apply computer vision technology to analyze clinician behaviors, such as hand-hygiene compliance

**Challenges:** **difficulty of obtaining the ground truth labels**. For example, we can judge whether a person is likely to have depression from his/her posts on social media. However, we can only confirm the disease from the person’s EHR (**Electronic Health Record**)
	yes, privacy problem

---

# Research Team 

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


---
# Adversarial attacks 
+ ? **Adversarial attacks** are a **type of machine learning attack that manipulate input data** to **trick a model into making incorrect predictions.**

## Topic: Survey on Adversarial Attack and Defense for Medical Image Analysis: Methods and Challenges

**Introduction:** 
Thực chất các mô hình DL tồn tại rất nhiều lỗ hổng về bảo mật, Một số cách tấn công mô hình rất phổ biến đó là tạo nên **advesarial example** bằng các t**hêm "noise" hay sử dụng các véc tơ để bóp méo ảnh đầu** vào khiến cho ảnh tuy không có gì thay đổi với nhận thức của con người nhưng có thể khiến cho máy nhận định sai nhãn
> **Deep Learning** nhạy cảm đến nỗi việc thay đổi **ngay cả 1 điểm của ảnh (1 pixel) cũng có thể khiến cho mô hình phán đoán sai.**



---
### [Note](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/ipr2.12419?fbclid=IwZXh0bgNhZW0CMTAAAR0QyqiJkvVF23d7Oq627EsCku2zohhWEk3wjcwf_0DbrqTDmAnmtisBMEU_aem_Klk-6L7MiAjiKRJKPJVIYA)
Loss Function for Inbalance Dataset

**Weighted Entropy Loss**
vùng tổn thương nhỏ hơn nhiều lần so vs vùng nền.

Tối ưu vùng dự đoán và vùg thực tế

Tverskz Loss
phân loại não thất

vấn đề: mất cân bằng dữ liệu. 

Weight Cross-loss Entropy

