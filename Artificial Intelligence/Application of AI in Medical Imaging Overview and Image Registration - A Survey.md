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
> [[EHRs]] include patient's digital clinical notes and informations.

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
+ ? This section focuses on the challenges and the corresponding solutions in the development of AI-assisted MPT in recent years (i.e ≤ 2024 )
	(A) Two independent areas of medical imaging
	![[Pasted image 20250217132905.png]]
	![[Pasted image 20250217132936.png]]
	![[Pasted image 20250217132952.png]]
	![[Pasted image 20250217133015.png]]
	![[Pasted image 20250217133153.png]]
	![[Pasted image 20250217133037.png]]
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
	    [[Histogram Equalization]] (note chi tiết ở cuối trang): ![[Contrast-limited-adaptive-histogram-equalization-method-a-low-contrast-input-image-b.jpg]]
	    **CLAHE** (**Contrast Limited Adaptive Histogram Equalization**):  divide the image into *n* 8x8 tiles, then **apply Histogram Equalization into each tile**. ![[Pasted image 20250209182759.png]]
    
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

**note:** 
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

### 3.3.3. Medical Image Registration
Data: 2D + 3D Image using CNN to detect and reduce false-positive 
Công Thức: Affine Transformation 
![[Pasted image 20250217072315.png]]

**Bước 1: Trích xuất đặc trưng (Lấy điểm đặc trưng)**
- **Ảnh cố định** (tham chiếu) và **ảnh di chuyển** (cần biến đổi) được **nhập vào mạng đăng ký**.
- **Mạng trích xuất các điểm đặc trưng**, đại diện cho các cấu trúc quan trọng (ví dụ: cạnh, đường viền, điểm đặc biệt).
- Các đặc trưng này có thể được phát hiện bằng:
    - **Phương pháp truyền thống:** SIFT, SURF, ORB, Harris Corner Detection.
    - **Phương pháp học sâu:** CNN, U-Net, VoxelMorph.  
+ $ **Mục đích:** Xác định các đặc trưng quan trọng trong cả hai ảnh để thực hiện căn chỉnh

**Bước 2: Tính toán ma trận tương đồng (Ghép nối đặc trưng)**
- Một **ma trận tương đồng** được xây dựng để tìm **cặp đặc trưng tương ứng** giữa hai ảnh.
- **Các tiêu chí đo độ tương đồng phổ biến:**
    - **MSE (Sai số bình phương trung bình)** → Dùng cho ảnh cùng loại (ví dụ: CT-to-CT).
	    (Before Transformation - After Transformation)
    - ![[Pasted image 20250216183443.png]]
    - **MI (Thông tin tương hỗ)** → Dùng cho ảnh khác loại (ví dụ: MRI-to-CT).
    - **NCC (Tương quan chéo chuẩn hóa)** → Đánh giá mức độ tương quan giữa cường độ pixel.  
+ $ **Mục đích:** Đánh giá mức độ khớp giữa ảnh di chuyển và ảnh cố định.


**Bước 3: Tính toán phép biến đổi không gian (Trường biến dạng)**
- **Các tham số biến đổi** được tính dựa trên các điểm đặc trưchuyển được lấy mẫu lại bằng các kỹ thuật nội suy:
    - Nearest Neighbor (Gần nhất)
    - Bilinear Interpolation (Nội suy song tuyến)
    - Bicubic Interpolation (Nội suy ba khối)
- Ảnh sau biến đổi giờ đây đã **căn chỉnh với ảnh cố định**.  
+ $ **Mục đích:** Tạo ra ảnh đã được đăng ký phù hợp với ảnh tham chiếu.

---
### [Histogram Equalization](https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html) and [CLAHE](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html)
**Histogram Equalization**
![[Pasted image 20250117081811.png]]
	1) Get the highest gray value 5 and its bits (bit size that can represent 5)
	2) Initiate gray levels range = $2^{bits}$. e.g. $2^3=8$ 
	3)  Start Calculating: 
	+ **PDF:** Probability Distribution (*value_i / the total_value*)
	+ **CDF:** Cumulative Distribution (*cumulative sum*) annotate as $S_{k}$
	+ $S_{k} \times max(\text{gray level})$: Multiply CDF with the highest gray level 
	+ **Histogram equal level:** approximate value upward (i.e. `.ceil()`  in python)
	4) Replace old pixel values with new pixel values.

**CLAHE**
![[Pasted image 20250117070011.png]]
> **Histogram Equalization stretch the histogram to include all ranges** `[0, 255]`. **CLAHE** divide a image into `n 8x8 tiles/grids, then **apply Histogram Equalization into each tile**. 


## Affine Transformation in Image Registration
### Image Transformation
+ ? How to do all of these Transformation using JUST 1 MATRIX.
![[Pasted image 20250216162053.png]]

**Identity Matrix:** this do nothing at all $A \times I = I \times A$ 
![[Pasted image 20250216162130.png]]

**Changing in the upper left element:** perform horizontal scale. 
![[Pasted image 20250216162812.png]]

**Changing the bottom right element:** perform verticle  scale.
![[Pasted image 20250216163028.png]]
 
**When we make either elements negative** it produces a reflection
![[Pasted image 20250216163155.png]]
![[Pasted image 20250216163259.png]]

The **Upper right element corresponds to a horizontal sheer (X-Axis Sheer)** 
![[Pasted image 20250216163415.png]]
And the **Lower left is a vertical sheer (Y-Axis Sheer)**
![[Pasted image 20250216163458.png]]

+ ? **So where do rotation come from**
We start by sheer horizontally,
![[Pasted image 20250216163632.png]]
 then apply verticlally by the same amount
![[Pasted image 20250216163642.png]]

+ $ This is infact a popular way to implement image rotations, because all you do is translate each row by a different amount and then translate each collumn
+ ? note: divide the image by half then translate the 1st half left, 2nd half right. 
![[Pasted image 20250216163747.png]]
+ ? note: divide the image by half, 1st half down, 2nd half up
![[Pasted image 20250216163806.png]]

+ ? So this matrix create a rotation by 2 sheers. But how can we specify the **angle of rotation** ?
+ $ The $\sin(\theta)$ and $\cos(\theta)$ funciton could convert value into angle, it converts from an angles to the right shear amount.  
![[Pasted image 20250216164759.png]]
**Change the angle results**: image size change a bit as it rotate.
![[Pasted image 20250216164627.png]]
So we need to correct this size change, and it turns out scaling by the cosine function exactly counteracts this size change.
![[Pasted image 20250216170831.png]]
When combine together sine and cosine produce a perfect rotation. 
![[Pasted image 20250216170940.png]]

### 3D Matrix Transformation
Along the **diagnol entries are corresponding to x, y and z**
And **all the rest are Sheer**. (because each dimension have 2 others dimension so 1 * 2 = 2 ways to Sheer each dimension)
**The X-Axis**: 
+ ? sheer **toward the X-Axis and around the Z-axis** ![[Pasted image 20250216172012.png]]
+ ? sheer **toward the X-Axis and around the Y-axis** ![[Pasted image 20250216171252.png]]


**The Y-Axis:**
+ ? sheer **toward the Y-Axis and along the X-axis** ![[Pasted image 20250216173102.png]]
+ ? sheer **toward the Y-Axis and along the Z-axis**  ![[Pasted image 20250216173043.png]]


**The Z-Axis**
+ ? sheer **toward the Z-Axis and along the Y-axis** ![[Pasted image 20250216172329.png]]
+ ? sheer **toward the Z-Axis and along the X-axis** ![[Pasted image 20250216172321.png]]

Using all the value above, we can Rotate the image around the 
+ **Z-Axis** (Yawn) by
	**Rotate X around trục Z-axis**![[Pasted image 20250216174124.png]]
	**Rotate Y around Z-axis** ![[Pasted image 20250216174116.png]]
	The rest are of X, Y and Z value. As you can see **Z value remain, just X and Y changes to perform rotation**. ![[Pasted image 20250216173407.png]]

+ **Y-Axis** (Pitch) ![[Pasted image 20250216173418.png]]
+ **X-Axis** (Roll) ![[Pasted image 20250216173435.png]]

This should move the x origin to the right by 1, 
![[Pasted image 20250216175036.png]]
**If X and Y equal 0**, this is impossible **because all matrixes map the zero vector to itself**, this mean 2 by 2 matrix can't do translation. 
(ma trận nhân với ma trận đơn vị không thay đổi)
![[Pasted image 20250216175727.png]]

However there a trick , let add a 1 to the bottom to make the vector into a 3D vector.  
![[Pasted image 20250216175515.png]]

And as you can guess, translation in 2D is basically sheer along the X-Axis in 3D. 
![[Pasted image 20250216180742.png]]

We saw a connect between 2D and 3D, the sheer translate the rows. In 3D, If we slice the cube into planes, each slices is translate by a different amount by the sheer. 
![[Pasted image 20250216180500.png]]
So if we think of our 2D image as the face of the z equal 1 planes. We can do any 2D matrix transformation and any translation using these elements of the 3 by 3 matrix. 
![[Pasted image 20250216181042.png]]

The 2D vector represent in 3D are called homogeneous coordinates.
![[Pasted image 20250216181125.png]]
The same thing work for higher dimensions. (i.e. 3D represent 4D)
![[Pasted image 20250216181157.png]]

---
### [Hand on Example of Affine Transformation in Image Registration](https://youtu.be/pwFeeVXLhsE?si=SERLs5J2txJy6Ese)
**Example Image:** Align brain MRI image.
![[Pasted image 20250217074715.png]]
![[Untitled 1.jpg]]

**Affine Transformation**: the one we discuss. This method preserve the original image shape when transformed. 
1) **Estimate the Parameters a** for each point. Where $x', y'$ is the destination point we want $x, y$ to transformed to, by multiplying parameters $a$. (Kind of like a Neural Network right ?)
	+ ? Note: The *parameter matrix* function below can be written as 2 simple equation $x', y'$. 
	![[Pasted image 20250217080139.png]]
	+ ? The Image represent **matrix transformation for 1 (x, y) point**. If there're 4 points, this matrix transformation will apply to all 4 of them) 
	
	
2) **Feature Detection** 
+ $ Before apply the parameters above, let find which point are important enough to be transformed. 
+ ? Luckly [feature detection](https://onlinelibrary.wiley.com/doi/10.1155/2021/8509164) will tell you **which point is important.** (e.g. feature detect using U-NET in Medical Imaging)
	![[Pasted image 20250217082352.png]]
	**Left Image:** Fixed Image (i.e. Original Image)
	**Right Image:** Moving Image (i.e. Image need to be transform) 
+ ? And out of all the important point, choose *n* corresponding important points in the Moving Image and the Fixed Image (chọn n điểm tương ứng có ở 2 hình). Let choose 4 points for this example.   
	![[Pasted image 20250217080501.png]]
	
3) **Feature Matching**
+ ? Feature Matching is the transformation that we do   
	Apply the *parameter matrix* to 4 points. Then convert those equation back into a ugly matrix 
	+ ? If you confuse how those 8 equations turned into a ugly matrix. Let focus on the matrix, perform some dot product and you'll figure it out (i.e. multiply the 1st matrix's row to each value in vector $a$)
		$a=({a_{11}, a_{12}, a_{13}, \dots a_{23}})$
![[Pasted image 20250216182528.png]]

4) **Re-write that big Matrix above into a simple equation**
$$b = A.x$$where
+ $b$ is the 1st vector $x', y'$ 
+ $A$ is matrix in the middle 
+ $x$ is that $a$ vector 

+ @ Like a neural network, parameters A can be calculate using traditional method or a Neural Network so that $x$ fit $b$. 

---
### Affine Transformation: A Fundamental Image Registration Technique

### 1. What is Affine Transformation ?
Affine transformation is a **linear mapping technique** that preserves **points, straight lines, and planes** while allowing transformations like **scaling, rotation, translation, and shearing**. It is commonly used in **image processing, computer vision, and medical image registration** to align images.

Mathematically, an **affine transformation** can be represented as:

$$
T(x) = A x + t
$$

where:
- $x$ is the original coordinate vector **(x, y)**,
- $T(x)$ is the transformed coordinate vector **(x', y')**,
- $A$ is a **2×2 transformation matrix** (controls scaling, rotation, shearing),
- $t$ is a **translation vector** (shifts the image in x and y directions).

---

### 2. Types of Affine Transformations
Affine transformation consists of multiple operations:

5. **Translation (Shifting)**  
   Moves an image without changing its shape.
   $$
   x' = x + t_x, \quad y' = y + t_y
   $$
   - Example: Moving an image **5 pixels right and 3 pixels down**.

6. **Scaling (Resizing)**  
   Stretches or compresses an image.
   $$
   x' = S_x \cdot x, \quad y' = S_y \cdot y
   $$
   - Example: Scaling **by 2x in width and 1.5x in height**.

7. **Rotation**  
   Rotates the image by an angle $\theta$.
   $$
   \begin{bmatrix} x' \\ y' \end{bmatrix} =
   \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
   \begin{bmatrix} x \\ y \end{bmatrix}
   $$
   - Example: Rotating an image **by 45 degrees**.

8. **Shearing (Skewing)**  
   Slants the image along the x- or y-axis.
   $$
   \begin{bmatrix} x' \\ y' \end{bmatrix} =
   \begin{bmatrix} 1 & sh_x \\ sh_y & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \end{bmatrix}
   $$
   - Example: A **shear factor of 0.5** skews the image diagonally.

---

### 3. General Affine Transformation Matrix
A **2D affine transformation matrix** is:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & t_x \\
a_{21} & a_{22} & t_y
\end{bmatrix}
$$

which transforms a point $(x, y)$ into $(x', y')$ as:

$$
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
\begin{bmatrix}
a_{11} & a_{12} & t_x \\
a_{21} & a_{22} & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

- **$a_{11}, a_{22}$** control **scaling**.
- **$a_{12}, a_{21}$** control **rotation and shearing**.
- **$t_x, t_y$** control **translation**.

---

### 4. Affine Transformation in Medical Image Registration
In **medical imaging**, affine transformations are used to:
- **Align multi-modal images (CT, MRI, PET)** before analysis.
- **Track tumor progression** in follow-up scans.
- **Correct distortions** from patient movement.

Example: A **brain MRI scan** might be **affinely registered** to a reference scan to correct slight head movements.
![[image/Untitled.jpg]]


