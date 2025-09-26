![[Pasted image 20250922152452.png]]
- **Level-wise (XGBoost):** Trees are **grown level by level.** This ensures better control over overfitting since each level **balances the tree.** Small to Medium dataset
- **Leaf-wise (LightGBM):** It focuses on **growing the most promising leaf**, which often results in deeper trees but can lead to **overfitting on small datasets.** 
	- good with Big Dataset, Spare Data 
	- used 60% less memory to run compare to xgboost

Goals: Prepare intended to use images first then Context and Header. 
### Intro
Module thiết kế cho DS và DA (DT, GB, XGBoost), low code nhiều library. 
Data quá lớn, chạy lâu -> Deep Learning 
XGBoost -> data vừa, khi ko cần đợi quá lâu. Data text, bảng.  
Hiểu ở
+ mức độ Engineering (biết cách xài) là đc. 
+ mức độ nghiên cứu -> hiểu cthuc và biết cách phát triển từ gốc. 
Không cần tìm hiểu quá sâu. 

### Outline
1. Summarize improvement from DT -> XGBoost.
2. Go Deeper by explaining the Procedure/Pipelin of DT -> XGBoost.
3. Focus on the Improvement: 
	+ Histogram-based Threshold for LightXGBoost.
	+ Leaf-wise Growth
	+ Exclusive Feature Bundling
4. Finally: Case Study

### Machine Learning Tree-Based model Overview 
#### Loss Function for Regression
Decision Tree - dùng hàm tính loss của logistic regression. Tìm hàm khả vi, dùng nhiều hàm loss khác nhau, vì mục đích của nó chỉ là tính distance. 
Ada Boost - Feature selection
Gradient Descent đi theo hướng đạo hàm
XGBoost - sử dụng chuỗi Taylor để tìm 1 hàm xấp xỉ xung quanh 1 gtri cụ thể nào đó 
LightXGBoost - giống XGBoost nhưng nhanh hơn. 
#### Loss Function for Regression Classification
+ ? Note: Giải từ khía cạnh áp dụng
	Bài toán phân loại thì sử dụng xác suất vì phân loại nhị phân là 0 1. 
![[Pasted image 20250923144232.png]]

#### Tree Building Improvement over version fromt DT to XGBoost
**Level Wise** mở rộng theo độ sâu của cây, đi từng nhánh 1 từ trái sang. Ở độ sâu này có mở rộng đc ko, nếu đc thì mở ko thì dừng. 
**Leaf Wise:** mở rộng theo lá tốt nhất thay vì tất cả. Ngoài Leaf wise chúng ta sẽ học thêm 3 kỹ thuật khác Histogram, GOSS và EFB. Để xem nó có thể áp dụng cho những bài toán nào. 
	LightGBM kế thừa hàm loss từ XGBoost và dựa trên nền tảng từ Gradient Boosting  để tăng tốc độ. 

Bảng tóm tắt: Gradient Boosting sử dụng Gradient làm hàm bậc nhất  Còn XGBoost xử dụng hàm Taylor bậc 2 để tăng accuracy. Còn LightGBM thì có thêm 3 kỹ thuật nhằm tăng tốc và tối ưu bộ nhớ. 
![[Pasted image 20250923142331.png]]

###  Comprehensive Tree-based method procedure overview  
Giải thích 1 cách tuyến tính, không cần giải thích lại nhưng phần đã giải thích rồi (e.g. Sort của Random Forest nếu DT đã giải thích rồi). Giải thích từ Regression sang Classification (những bài phân loại thì dùng hàm xác suất)

Gradient Boosting, residual là giá trị đạo hàm của hàm loss, giải thích vì sao thêm dấu trừ (trừ từ thành cộng ?)
![[Pasted image 20250923143657.png]]
SSE *phân tách* dữ liệu theo cây. Giống MSE nhưng mà là Sum MSE -> SSE. 
Leaf Weight - đưa toán học qua để biến đổi cthuc. 
XGBoost - có Hessian để tính nhiều phép tính đạo hàm 1 lúc. 

### Review of Entropy. Review on Loss Function 
-> đo độ hỗn loạn (dễ dự đoán hay khó dự đoán) 
Giải thích từng thành phần của công thức H(X) (Entropy fomula)

Understand GB Loss (Square Function) - explain gradient descent in GB (Thêm ví dụ)
![[Pasted image 20250923144816.png | 444 ]]
![[Pasted image 20250923144929.png | 444]]

Note: Công thức cập nhật trọng số trong Cách tính Loss tương tự công thức cập nhật của Gradient Boosting nhưng khác ký tự thoi.  
![[Pasted image 20250923145217.png]]

Visualzie DT each Step. Summarize the hand calculation process, Add its to Appendix for people who want to revision. 
	 1 loại -> entropy = 0. Nhiều loại entropy lớn gần 1.  -> entropy trung bình của split -> tính gain của những threshold khác. -> Lấy threshold có IG lớn nhất. 
## Main Section: 
### Histogram-based Threshold
Liên tưởng từ việc cải thiện độ nét của ảnh. 1 ảnh gồm 256 pixel cả length và width -> copy thêm 1 dòng cho mỗi màu -> 512 sample. 
	Làm ngược lại so với các threshold trog bài toán regression. Thay vì chọn hết thì mình chỉ chọn 1 nửa số dataset thoi.  Bằng cách coi 2 cái sample liền kề nhau là 1 sample để tính threshold. Mỗi sample này gọi là 1 bins (vật chứa, khoảng chứa) vì nó chứa 2 giá trị.  
	
![[Pasted image 20250923151507.png]]
Giải thích ý tưởng của Histogram-based: THAY VÌ TÍNH THRESHOLD LẦN LƯỢT, thì mình sẽ GIẢM SỐ LƯỢNG THRESHOLD ĐI VỚI NHIỀU CÁCH KHÁC NHAU.
1. Chọn số bins (số sample trong 1 bins)
2. Tính độ rộng của bin bằng cách lấy max trừ min chia trung bình
3. Tính Các Cạnh của bin với công thức .... với k là số lượng Bin, và $e_{k}$ là giá trị của Mỗi cạnh, tính cạnh của bin từ $[min, max]$   

**Ví dụ thực tế:**
Tính bins cho cả Petal Width và Length để tạo cây. 
![[Pasted image 20250923152439.png]]

![[Pasted image 20250923152456.png]]

Chỉ lấy node có Gain lớn nhất để mở rộng. (Loss thấp nhất) Thay vì quay lại phát triển nhánh có Gain thấp như trước. -> Đánh đổi các Branch có Gain thấp để xây dựng cây nhanh hơn. 
	Khi thử nghiệm thì làm 1 cái chuẩn tr'c rồi thay thế các cái khác vào sau. 

**Exclusive Features Bundling**
Note: điểm yếu khi encoding Label như màu với số đấy là mình đang ngầm định nó có thứ tự là 0, 1, 2, tạo nên sự không công bằng. Nếu chia theo threshold ví dụ là 1.5 thì ta sẽ có "0, 1" + "2" hoặc  "1, 2" + "0" -> ta thấy "1" không được phân loại. 
![[Pasted image 20250923164528.png]]


 
 