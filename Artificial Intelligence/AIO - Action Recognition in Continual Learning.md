**HMDB51 Dataset** 
	X = {I_1, I_2,...,I_n}, n_videos contain **51 classes of actions** from movies/web videos.
	**Characteristic:** Is highly Imbalance. "Walk" action is most bias -> need specific data augumentation and loss functions. 
	 
**Prediction Format:** P( Action | X ) = %
**Classess:** 51 action class
**Tackle Features -** Brightness, Blur, Constrast and Color Distribution.

| **Component**  | **Function**      | **Intuition**                                               |
| -------------- | ----------------- | ----------------------------------------------------------- |
| **HMDB51**     | Dataset           | 51 classes of actions from movies/web videos.               |
| **SMIF**       | Short-term Motion | Focuses on "what changed" between frame $T$ and $T+1$.      |
| **LMI**        | Long-term Motion  | Links information across the whole video duration.          |
| **PatchEmbed** | Tokenization      | Converts visual data into a format Transformers can "read". |

#### X. Planning 
- [ ] Extract Frames and Understand Frames input Dimension
- [ ] Create Training/Testing Dataset
- [ ] Test Training on small dataset
- [ ] Understand how wirtten method work
- [ ] Understand ViT next morning and Connect Ideas. 


#### A. Data Preprocessing & EDA
**Frame Extraction** using *torchcodec.decoders.VideoDecoder* instead of regular frame processing *to optimize memory and performance (cpu & cuda)* 
+ ? Video have different Length 
	*$\to$ Uniform Sampling* - extract frame at equal interval  
	*$\to$ Temporal Padding* - repeating the last frame for short video to ensure a fixed input of $T=16$ frames.

**[Handle Data Imbalance](https://isi-web.org/sites/default/files/2024-02/Handling-Data-Imbalance-in-Machine-Learning.pdf#:~:text=Undersampling%20is%20a%20resampling%20technique%20used%20to,given%20equal%20importance%20in%20the%20learning%20process.) between walking and other activity**
	*Oversampling* of the Minority class *and Undersampling* of the Majority Classes using **SMOTE**.
![[Pasted image 20251226164042.png]]


#### B. Architecture (LS-ViT)
The model processes the video through several specialized stages:

`Feature Extraction Layer`
1. **SMIF (Spatial-Motion Interaction Fusion):** This module *calculates the pixel-level difference between adjacent frames* to **create a "motion map,"** helping the **model focus on moving regions.** (Important)
	
2. **Patch Embedding:** Splits frames into small 2D patches and projects them into a vector space.

`core block - like ViT`
3. **LS-ViT Blocks:** A series of Transformer layers that utilize:
	+ **Multi-Head Self-Attention (MSA):** Allows patches to relate to one another.
	+ **LMI (Long-term Motion Interaction):** A module that captures dependencies across the entire sequence of frames.
	
4. **Classifier Head:** A linear layer that takes the averaged global tokens (CLS tokens) from all frames to output the final action probability.

#### C. Training & Regularization
+ **DropPath:** Unlike standard Dropout, this "Stochastic Depth" technique **randomly drops entire residual paths to prevent overfitting** in deep networks.
	
+ **Optimization:** Uses the **AdamW** optimizer and **CrossEntropyLoss** with *mixed precision (GradScaler) to speed up training*.

---
## Human Action Recognition (HAR) Method Survey
**Applicatiton:** everything related to human action. A LOT.
**Hướng mở rộng để cải thiện Accuracy cho bài toán HAR:** RGB frames, depth images, pose sequences, textual descriptions, human parsing, and point clouds.

### Comparison between existing methods and HP-Net 
![[Pasted image 20251228181644.png]]
**(a) Các phương pháp dựa trên Feature Map thô với ảnh RGB** 
-> dễ bị *ảnh hưởng bởi nhiễu và các yếu tố can thiệp từ môi trường.*
+ ? e.g. đưa nguyên cả bức ảnh vào máy tính, nó không chỉ nhìn thấy người đang hành động mà nhìn thấy cả hình nền (cây cối, xe cộ, ánh sáng đèn).

**(b) Các Phương pháp sử dụng pose-estimation sử dụng dữ liệu khung xương với thông tin giới hạn** (+ ví dụ vì sao lại giới hạn)  
-> Hỗ trợ nhận diện hành độg chi tiết (fine-grained) kém.
+ ? e.g. Dữ liệu này chỉ là các "que và chấm" đại diện cho tay chân. Nó loại bỏ hoàn toàn thông tin về hình dáng bề ngoài và vật thể. *Ví dụ như hành động cầm thìa và nắm tay sẽ giống hệt nhau nếu cái thìa sẽ ko đc bao gồm* -> mất thông tin. 

**(c) Phương pháp tổng hợp đặc trưng sử dụng Mạng Hợp Nhất (Fusion): Pose-Estimation + CNN**
-> Tốt nhưng quy trình "chồng chéo" nhiều bước này khiến máy tính *chạy chậm và tốn tài nguyên.*

**(d) Phương pháp sử dụng Heatmap**  
Sử dụng biểu đồ nhiệt để *thể hiện xác suất vị trí các khớp.*
-> Thường chứa dữ liệu dư thừa và pháp sinh chi phí lưu trữ cao. 
+ ? 1 ảnh *heatmap thường có kích thước lớn* (số pixel = toàn bộ cái ảnh) nhưng *thông tin hữu ích (vị trí khớp tay) chỉ là 1 điểm sáng nhỏ xíu, phần còn lại là màu đen (vô nghĩa).* Việc lưu trữ và xử lý cả vùng màu đen vô nghĩa gây lãng phí tài nguyên tính toán và bộ nhớ. 

**(e) Our HP-Net proposed**  
![[Pasted image 20251228184316.png]]
**Module 1: HP-Net tích hợp Feedback Pooling Module (FPM)** 
+ @ **Trực giác:** Làm sao để chỉ trích xuất thông tin quan trọng xung quanh các khớp -> Áp dụng Pooling xung quanh các tọa độ khớp.
+ ? Bằng cách sử dụng Tọa độ khớp (từ pose-estimation) để khoanh vùng và **CHỈ TRÍCH XUẤT THÔNG TIN XUNG QUANH khớp đó.** 
+ $ HP-Net thu về Heatmap hiệu quả hơn bằng cách **giảm thông tin dư thừa trong khi vẫn giữ lại các thông tin liên quan.** 
  
**Module 2: Làm giàu đặc trưng hình ảnh với Text: Text Refinement Modulation Module (TRMM)** - Cần 1 Người đọc source prefer trog file pdf để xem Feature Text + Feature Ảnh giúp mô hình học tốt hơn ntn. 
+ @ **Trực giác:** Sử dụng cả thông tin của Text để giúp  
+ ? Kết hợp đặc trưng hành động trích xuất từ HP-Net với đặc trưng của Text Label (encode bằng Text Encoder)
-> Sử dụng văn bản để dẫn dắt đặc trưng thị giác tốt hơn. 
![[Pasted image 20251228190051.png# left | 333]]

**Kết Quả:**
![[Pasted image 20251228185647.png]]