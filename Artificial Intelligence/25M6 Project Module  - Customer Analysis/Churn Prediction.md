**Overview** 
**Shopping customer demand personalization** (Business Pain), urge the need for a "Customer Segmentation" system to prioritize product for each customer segment and needs to boost revenue. By define the right customer segment, commercial company cound:
+ **Optimize their marketing strategy** to each specific customer segment. 
+ **Increase Customer Retention** by providing their most demanding product right at the start.
+ **Optimize Resource Allocation** from Valuable Customer Segment to optimize profit.   


**Outline**
*1 - Business Context (Motivation, Data Analysist)*
+ ? Approach - Understand the Problem Like a **Strategist**.
	 What business inefficiency does segmentation solve ?

*2 - Methodology*
**Data**
+ Data cleaning
+ Feature Engineer base on customer behaviour
+ ? Approach - Understand Data like an **Data Analyst**
	What patterns and signals are hidden in customer behaviour

**Data Transformation**
+ Box-Cox (new method) + Standardization
+ PCA (for visualization only)
+ K-Means 
+ ? Approach - Understanding Transformation like an **ML Engineer**
	Why normalize, reduce skew, Why use K-Means, Why 16 features, Why PCA

*3 - Visualize Result for Insight and Application* 
*4 - Business Application/Strategy*
**Understand Result**
+ ? Approach - Understand the Result like a **Store/Product Owner**.
	How can I ultilize these discovered segments to improve my business

*5 - Improvement* 
+ DBSCAN / GMM clustering
+ more feature (by season)
+ segment product by user (segmentation to product level)
+ recommendation system using LLM
+ ? Approach - Internalize the Math like a **Researcher**. 
	Why does the chosen method logically produce the discovered segment ? 

These layered approach *mirror how real ML teams work:*
	business -> analytics -> modeling -> deployment -> impact

**Core Ideas**
	Analyze Customer Behaviour -> Segment/Classifier Customer -> Increase ROI
	Feature Engineering
	Box-Cos transformation
	Feature Scaling for K-Means
	PCA

---
## Project : Customer Segmentation with K-means Clustering

**Data information**
![[Pasted image 20251209194035.png]]

**Data Structure**
![[Pasted image 20251209194252.png]]

**Data Risk Assessment**
![[Pasted image 20251209194306.png]]
Vì sao lại đánh giá - đánh giá rủi ro tiềm ẩn, để phân tích về mặt business. 
	Tránh TH mô hình đẹp nhưng thiếu ý nghĩa về mặt business intepretation.

**ML Life Cycle Include**
![[Pasted image 20251209194559.png]]

![[Pasted image 20251209195812.png]]
*Hiearchical Clustering và K-Means (most common)* là 2 thuật toán dc sử dụng nhiều nhất. DBSCAN và Gaussian Mixture cũng thú vị nma ít hơn. 

**Pros and Cons and Solutions**
![[Pasted image 20251209200149.png]]
K-Means sensitive to Distribution and scale of the data. **Does not handle skewed distributions well.** especially when the data come with price. 
	Because K-Means use L1 or **Manhattan** distance its assume the data is a circle/sphere thus data have variance/spread in all dimension/features.  
![[Untitled 9.png]]


**Sihoutte Score**
Tính điểm bằng cách xét giữa **khoảng cách** tới **Cụm Hiện tại và Cụm khác gần nhất.** Tương quan giữa Cụm hiện tại và Cụm khác gần nhất.
![[Pasted image 20251209203026.png]]

**Box-Cos Transformation**
Điểm yếu của K-Means là Skewed dataset chưa đc chuẩn hóa. Mà hành vi mua sách của 1 số khách hàng VIP có giá trị cực lớn -> skewed. 
+ Với Box-Cox -> Standardize, Stablize Variance. Limited effect outlier.
![[Pasted image 20251209203350.png]]
$\lambda$  - giúp thay đổi hình dạng của Phân Phối. Giống trong Gaussian.  ![[Pasted image 20251209204719.png]]

**PCA (First Principle Component Analyst)** 
+ ? Giảm chiều mà vẫn giữ các thông tin quan trọng. 
+ $ Giúp loại bỏ các thành phần Nhiễu. Biến đổi dữ liệu cao chiều về 2D hoặc 3D để dễ quan sát.
![[Pasted image 20251209205012.png]]
Tuy nhiên trong bài này, PCA dùng để đánh giá chất lượng phân cụm chứ không thay thế 16 features gốc trong clustering. 
	Có thể dùng PCA để giảm chiều dữ liệu rồi dùng chiều đấy luon. 

**Cấu trúc Proj rõ ràng** 
+ **notebooks** thử nghiệm chứa *toàn bộ quy trình cả phân tích, thử nghiệm và training lẫn inference*. e.g. cleaning data, feature engineer, modeling.
+ **src code** chỉ bao gồm *inference*. e.g. Data Cleaning, Feature Engineer, EDA, K-Means.
+ **documents** *giải thích tổg quan dự án*. e.g proj description, README.md

**Project Workflow**
![[Pasted image 20251209205657.png]]
+ **Box-Cox để chuẩn hóa skewed data** nhưng không **đưa các Feature về 1 khoảng giá trị**, nên mình tiếp tục dùng **Standard Scale.** 

![[Pasted image 20251209211756.png]]
+ *Đánh giá Cụm 1:* **Elbow Score** dùng để đánh giá **số lượng Cụm/Clusters** trên tốc độ giảm của Loss (ie. WCSS) ![[Pasted image 20251209212332.png]]where $P_{i}$ represent point in $C_{i}$ cluster.  
	ie. Loss giảm bao nhiêu với số lượng Cụm là K. 

+ *Đánh giá Cụm 2:* **Silhoette Score** dùng để đánh giá chất lượng và tìm **số Cụm tốt nhất** bằng cách đo khoảng cách giữa các cụm. 
+ $ Kết hợp cả Elbow Score và Silhouette mình -> đc số Cụm tốt nhất. 

Trực quan hóa dạng 2D có thể cho thấy 1 số Cụm bị trùng/clip vs nhau vì thực tế các cụm đang ở không gian 3 chiều. -> Visualize ở 3D để kiểm tra. 
![[Pasted image 20251209213421.png]]

**Intuition:** sau khi phân cụm khách hàng, câu hỏi đặt ra là Thế nào là 1 "Phân Khúc"/"Cụm" khách hàng chất lượng, liệu có 1 công thức nào đó để đánh giá giống như bên kinh tế hay không. 

Câu trả lời là RFM, 1 framework tham chiếu đánh giá khách hàng dựa trên 3 yếu tố: 
**Recency (R) -** *độ active của khách hàng* dựa trên *ngày active/online gần nhất* -> tốt để đánh giá vì nếu càng lâu không mua hàng thì giá trị của khách hàng đó sẽ giảm. 
**Frequency (F) -**  số lần mua hàng để *tính độ trung thành* của khách hàng với shop -> Đúng vì kh mua nhiều có xu hướng mua sp mới hơn. Có thể dùg để *tính điểm Loyalty*.
**Monetary (M) -** *tổng chi tiêu trong shop*. -> Đúng vì tổng chi tiêu của khách hàng có *chứng minh giá trị của 1 khách hàng*. Có thể dùng để tính Giá trị *Vòng đời 1 khách hàng.* *(Insight:1 Khách hàng có tiềm năng tạo bao nhiêu lợi nhuận)* 
![[Pasted image 20251209213913.png]]
Phân cụm khách hàng Rule-Base.
![[Pasted image 20251209214658.png]]
Note: Nếu dùng DeepSeek cho dự án này, nó cũng có thể xác định RFM làm FE, nhưng KHÔNG CHUYÊN SÂU. Nếu chỉ dùng RFM đúng nhưng chưa đủ chuyên sâu. 
-> Insight: Tận dụng thông tin trên để gửi thông báo khuyến mãi đặc biệt cho các khách hàng rủi ro bỏ cao.

### Feature Engineer: 16 Features
+ ? **Tư duy thiết kế Features**, làm sao để mỗi Features nắm bắt được 1 khía cạnh của hành vi khách hàng. **Câu hỏi đặt ra là, mình cần nắm bắt hành vi gì từ khách hàng.**![[Pasted image 20251209232248.png]]
+ $ **Units Price** theo **Stock và Invoice.**  ![[Pasted image 20251209215236.png]]
	Vì mỗi *hóa đơn có thể có nhiều loại sản phẩm*, mỗi *loại sản phẩm có thể có nhiều số lg* -> Mình có thể phân loại theo 2 Feature chính (*Unit Price* theo *Hóa Đơn và Sản Phẩm*). 

+ Tính *Unit Price (giá trị) theo Hóa Đơn*
	+ ? Vì mỗi sản phẩm có thể mua vs số lượng nhiều. Nên mình ước lượng giá trị mỗi phẩm là *Giá Trị Trung bình của các sản phẩm*.  
	+ Tổng chi tiêu của Hóa Đơn
	+ Tổng chi tiêu trung bình của hóa đơn
	+ Số lượng hàng trong Hóa Đơn.
	+ Số lượng hàng trung bình của Hóa Đơn. 
	+ Số lượng Trung Bình của mỗi hàng trong Hóa Đơn. 
	+ Giá trị Trung Bình của mỗi hàng trong Hóa Đơn.
	
+ Tính *Unit Price theo Sản phẩm*
	+ Mức giá trung bình theo mỗi Sản Phẩm. 
	+ Số lượng Trung bình được mua trên mỗi sản phẩm. (ie. Với mỗi sản phẩm, số lg được mua của mỗi sp là bao nhiêu)
	+ Chi Tiêu Trung Bình trên mỗi sản phẩm. (Mỗi sản phẩm thường dc chi bao nhiêu tiền để mua, bao gồm cả giá trị trên số lượng sp)
	+ Tổng chi tiêu trung bình của sản phẩm. 

Khi báo cáo, luôn đưa ra tổng quan và kết luận nổi bật nhất trước. Sau đó phân tích sâu hơn (theo ngày và tháng)

Heatmap có thể dùng để Highlight mối tương quan giữa 2 quan hệ đơn giản và hiệu quả. Ví dụ, khách hàng thường mua vào giờ nào trong tất cả các ngày trong tuần. 
![[Pasted image 20251209232956.png]]
-> Để đưa ra Thông Báo hiệu quả. Có thể dùng để quản lý thông báo cho từng Phân Khúc khách hàng -> Tiết kiệm chi phí và hiệu quả hơn.  

Quy Luật Pareto (20/80) khi bán hàng. Thường thì trong mọi sản phẩm sẽ có 20% sản phẩm mang lại 80% doanh thu. -> Tập trung vào sản phẩm bán chạy nhiều hơn. 
![[Pasted image 20251209233203.png]]


**Motivation**
+ Tối ưu marketing (giảm giá) cho mỗi phân khúc khách hàng
+ Cải thiện hệ thống gợi ý sản phẩm cho từng phân khúc khách hàng.
+ Tối ưu quy trình phân phối tài nguyên để ưu tiên cho nhóm khách hàng mang lại lợi nhuận lớn nhất. 

**Các bước thực hiện**