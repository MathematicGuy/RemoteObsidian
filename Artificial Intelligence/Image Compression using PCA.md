step-by-step: https://youtu.be/FgakZw6K1QQ?si=wetpWgoyrAGX21jW
pca with python: https://youtu.be/Lsue2gEM9D0?si=5pOBaRiOsUqu07UY
pca main ideas: https://youtu.be/HMOI_lkzW08?si=CidwgYaZQWN-qDhz

---

A Web allow to post image and compress them.
+ Docker
+ PCA algorithm
+ ML

+ PCA (Principal component analysis) - phân tích thành phần chính
	đơn giản hóa 1 tập dự liệu lướn thành 1 tập dự liệu nhỏ trong khi vẫn duy trì các mô hình và xu hướng quan trọng.

**Opening**
+ **Assigned Problem**
	Cần giảm dung lượng của ảnh để tối ưu quá trình xử lý ảnh cho huấn luyện máy. 
+ **Implementation Content** (Nội dung thực hiện)
	1) Áp dụng thuật toán nén PCA  (Principal Component Analusis) để giảm dung lượng ảnh.
	2) Giải thích chi tiết về thuật toán PCA, cách thức hoạt động, hàm liên quan,
	3)  Video demo quá trình thực hiện.
	4) Đánh giá hiệu quả của thuật toán PCA trên tập dữ liệu ảnh mèo thu thập từ Kaggle.
**Body**
1) **Data** 
	+ 100 ảnh mèo.jpeg trên Kaggle. 
	
2) **Data Preprocessing** (Tiền xử lý dữ liệu) 
	+ Áp dụng các kỹ thuật tiền xử lý cơ bản như: thay đổi kích thước, chuẩn hóa dữ liệu,
	+ Giới thiệu các phương pháp tiền xử lý ảnh nâng cao sử dụng PCA, mạng nơ ron, học sâu (có thể) 
	
3) **Solving Models/Algorithms** (Các mô hình/thuật toán giải quyết)
	+ **Detail PCA Explaination:** Get into the math:
	    - Covariance matrix, eigenvectors, eigenvalues.
	    - How to choose the number of principal components.
	- **Reconstruction:** How will you reconstruct images from the reduced PCA representation?
	
4) **Model Recommendation:** (Đề xuất mô hình)
	- Giới thiệu thuật toán nén PCA: nguyên tắc hoạt động, ưu điểm và nhược điểm.
	- So sánh PCA với các phương pháp nén ảnh khác (ví dụ: JPEG, PNG).
		+ JPEG: 5-10%
		+ **PCA** có thể là lựa chọn tốt nếu bạn cần giảm kích thước ảnh một cách hiệu quả mà vẫn giữ được các đặc trưng quan trọng của ảnh
	
5) **Experiment and Evaluate Results:** (Thực nghiệm và đánh giá kết quả)
	+ Chọn thực nghiệm với các kịch bản dữ liệu khác nhau.
	+ Đánh giá KQ: VĐ, NĐ, Đề Xuất
	
**Conclusions:**
	1) Acceptable compress ratio to quality
	2) How does PCA compare in performance to other methods (JPEG, etc.)?
**Future Work:**
	1) A Web allow to post image and compress them.
		+ Docker (Publish and Update Website)
		+ PCA (Compress Image)
    2) Could you optimize implementation for speed?


# **Presentation**

+ **Top priority:** Futuristic Approached Presentation. 
	Applied some of the newest education technique (that student use)
	+ Cognition Load
	+ etc...list out later
	+ note: spend time to find the best way to transfer this 

**Presentation Technique & Roadmap** 
+ ! Focus on the Big Picture
+ **Why it matters**: why do we need this? starts with real-world benefits of image compression (e.g faster website loading, saving storage space, enhance AI trainning process).
	Quickly mention traditional methods (JPEG) and why we're using PCA now.
	
- **The "Aha!" moment:** Before getting into math, explain the core idea of PCA:
    - Finding the directions of most change (variance) in the image data.
    - Using those directions to represent images more compactly.
    
- **Visuals:** Show a simple diagram (arrows for principal components overlaid on a simplified image) to make this concept stick.

+ ! Break Down the Technical Stuff
	**Step by step:** Walk through the PCA process slowly:

1. Mean-centering your image data.
	
2. The covariance matrix (explain it as a measure of how pixels change together).
	3. Eigenvectors & eigenvalues (directions of most variance, and how much variance).
    4. Projecting, encoding, and reconstructing images.
	
- **Simple Math:** Use intuitive examples rather than heavy equations if your audience isn't very math-focused.
	
- **Code Snippets:** If appropriate, show small, well-commented code chunks to illustrate the implementation.

+ ! **Visualization**
- **Before & After:** Prepare a set of images:
    - Originals,
    - Compressed with PCA at different levels (showing the quality/compression tradeoff).
    - Maybe even compared to a standard JPEG of similar file size.
	
- **Live Demo :** Have a simple script where you can load an image and adjust the number of principal components in real-time to see image reconstruction.

note: Get feedback on this report.
**Additional Detail**
+ **Practice makes perfect:** pratice to strive for that flow I want
+ **Q&A**: Practice might have Question
+ **Don't overcomplicate**: FOcus on the core concepts and the result. My full reserach details can be in a written report. 

---
# What I need to do to make this happened

see the big big picture
get in the detail
break down each step of the detail to components, see how it work and work together
outline PCA algorithm
code PCA algorithm in python from scratch to understand it deeper
documented the process and result
evaluate the result. Find out the 
+ Acceptable compress ratio to quality (show how diff each results)
+ Better than others algorithm


---

# Archive
Mở Bài
+ Đặt vấn đề
+ Nội dung thực hiện
Thân Bài
1) Dữ liệu 
2) Tiền xử lý dữ liệu 
3) Các mô hình/thuật toán giải quyết
4) Đề xuất mô hình
5) Thực nghiệm và đánh giá kết quả
Kết Bài
(note: Vietname education is the worst because it can always be better)
