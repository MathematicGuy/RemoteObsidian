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
Survey Papers:
+ [[Heatmap Pooling for Action Recognition]]
+ [[Investigate Normalization Method in Action Recognition problem]] 

1. Smooth Representation -> understand Core Ideas -> Draw the whole Architecture Transparent about input and output Dimension. 
2. Effect of each Improvement ->Result Result.
3. Deadline overview -> not looking to be the first, rather in the top 5. 

**Priorities**
- [ ] Sketch LS-ViT Architecture with Input and Output Dimension + Trick to reshape vector dimension note


**LS-VIT Block Architecture**
Input -> SMIF (pixel level motion) -> ViT Backbone (Patch Embed) -> Temporal Pooling  (Temporal Pooling)


#### **A. MixUp (Pha trộn tuyến tính)**
**Cơ chế:** Thay vì đưa vào mạng 2 ảnh riêng biệt (Ví dụ: Ảnh A là "Kick Ball", Ảnh B là "Run"), MixUp sẽ tạo ra một ảnh mới bằng cách chồng mờ 2 ảnh này lên nhau theo một tỷ lệ λ (lambda).
![[Pasted image 20260105215122.png]]
- Các mô hình CNN/ViT thường hay "học vẹt" bằng cách chỉ nhìn vào một đặc điểm nổi bật (ví dụ: cứ thấy màu xanh lá cây là đoán "đá bóng").
    
- CutMix che mất một phần ngẫu nhiên của ảnh, ép mô hình phải **nhìn vào các phần khác** của bức ảnh để nhận diện hành động (học ngữ cảnh toàn cục).

### **B. CutMix (Cắt và Dán)**
**Cơ chế:** Thay vì chồng mờ (gây nhiễu ảnh), CutMix cắt một hình chữ nhật từ ảnh B và dán đè lên ảnh A.
- Các mô hình CNN/ViT thường hay "học vẹt" bằng cách chỉ nhìn vào một đặc điểm nổi bật (ví dụ: cứ thấy màu xanh lá cây là đoán "đá bóng").
    
- CutMix che mất một phần ngẫu nhiên của ảnh, ép mô hình phải **nhìn vào các phần khác** của bức ảnh để nhận diện hành động (học ngữ cảnh toàn cục).

Tối ưu hàm mất mát (Loss Function): Thay thế CrossEntropyLoss tiêu chuẩn bằng Label Smoothing Loss (với ϵ ≈ 0.1). Kỹ thuật này ngăn mô hình trở nên quá tự tin vào các nhãn nhiễu, đặc biệt hiệu quả với các hành động có tính nhập nhằng cao trong HMDB51

Trực quan hóa Spatio-Temporal Attention: Xuất trọng số từ module LMIModule hoặc các lớp Attention để tạo bản đồ nhiệt (heatmap) đè lên video, giúp minh bạch hóa việc mô hình đang tập trung vào vùng không gian hay khung hình thời gian nào khi ra quyết định.

#### **TSN-style Sampling / Segment Sampling)**
1. Chia video (100 frames) thành T đoạn bằng nhau (ví dụ 16 đoạn).
2. Trong **mỗi đoạn**, chọn ngẫu nhiên **1 frame**.
- $ **Bao phủ toàn bộ video:** Đảm bảo từ đầu đến cuối video đều có đại diện.
	
- $ **Đa dạng hóa dữ liệu (Data Augmentation tự nhiên):** Ở epoch 1, đoạn thứ nhất bạn lấy frame 2. Ở epoch 2, đoạn thứ nhất bạn có thể lấy frame 4. Mô hình sẽ được nhìn thấy nhiều biến thể của video hơn mà không cần tăng bộ nhớ.

