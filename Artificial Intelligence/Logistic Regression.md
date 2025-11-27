
## Lecture Analysis
### From Linear Regression to Logistic Regression
+ @ **Main Problem:** explain how to choose the right Loss function, start from Linear Regression to Logistic Regression. **How to design a Learning Algorithm ?**
Linear Regression Revision (intuition + calculation + ideas)
$\hat{y} = H(x) = \sum_{i=0}^j \theta_i X_i$


+ ? [What is "First Order" in First Order Trend](https://www.reddit.com/r/AskEngineers/comments/1kdz6on/first_order_effect_for_the_eng_word_geeks_what/): 
	+ **"To first order"** is **colloquial for** the notion that you're **discussing the biggest effects and ignoring others.**
	+ Mathematically, **"first order (1D)" suggests the first term of a taylor expansion, ignoring higher order (ie 2D, 3D, 4D, etc...)**. In perturbation theoreis first order is the base theory, maybe with only a linear term for correction. There are other specific definitions, but it's not a single well defined concept.

Give new problem -> The need for Logistic Regression...
+ Goal: Fit the data best. Find the func that describe (predict) the data pattern. Author solve this problem by using a already proven fomula. 
+ Try with Linear Regression -> not fit bc of straight line. 
+ Try with Logistic Regression -> see better result. 
 ![[Pasted image 20251109212724.png]]**NOTE:** Sigmoid Function. (Thêm phần giải thích sâu và CM công thức trong section Tại Sao). 
**Step of Logistic Regression**
1) Initialize Parameters
2) Calculating y -> Calculate Sigmoid z
3) Calculate Loss base on $\hat{y}$ and $y$ 
4) Calculate Parameters Gradient 
5) Update Parameters Gradient (w and b)
![[Pasted image 20251109222411.png]]
Tính đạo hàm theo x rồi tính đạo hàm theo y. Hoặc ngược lại, kq như nhau thoi. 

Logistic Growth Fomula review (giải phương trình vi phân) -> Sigmoid -> Dùng Sigmoid vì nó đưa dải giá trị về 0 và 1. Dễ phân loại khi có Threshold.  
(Giải thích vì sao Sigmoid hoạt động, 1) là đáp ứng nhu cầu 2) giải thích dưới mặt toán học)
![[Pasted image 20251109212913.png]]
Sau khi biết cách làm -> Cần cập nhật trọng số -> Tính đạo hàm 
![[Pasted image 20251109212948.png]]
Đạo hàm MSE 
![[Pasted image 20251109213622.png]]
	Thầy giảng thiếu phần nhược điểm của MSE ?? 
![[Pasted image 20251110000357.png]]
Khi tính đạo hàm ta thấy MSE ko phù hợp để làm hàm mất mát vì ... nó là non-convex. 
+ ? 1 Hàm Loss non-convex sẽ:
		+ sẽ là 1 hàm không lồi. Nghĩa là nó có nhiều local-minimal (giải thích thêm phần này sử dụng Coursera) khiến thuật toán sử dụng Gradient Descent bị mắc kẹt ko tiến đến đc Global minimal. 
	+ Đạo hàm rất nhỏ vì công thức sử dụng Nhân, nên càng cập nhật nhiều sẽ càng chậm -> hiện tượng này gọi là Vanishing Gradient, đạo hàm ít tới mức có thể coi như là không cập nhật gì. 
	+ Hàm mất mát không có ý nghĩa thống kê vì nó đc thiết kế cho bài toán Regression với mục tiêu dự đoán các giá trị biến động liên tục. Trong khi Logistic Regression là 1 bài toán phân loại dự đoán xác suất thuộc về 1 lớp nhất định. (Regression có nhiều giá trị, Classification có 1 số giá trị nhưng vẫn có thể đếm đc), sử dụng Cross-Entropy, 1 hàm thuần xác suất để phân loại nhị phân sẽ có ý nghĩa thống ke tốt hơn. 
+ ? Giải thích tính Convex của 1 hàm bằng cách chứng minh liệu 1 hàm có convex hay không. i.e. đạo hàm bậc nhất và đạo hàm bậc 2. Nếu đạo hàm bậc 2 > thì Convex, =0 sẽ ... < 1 sẽ ... Note: tính convex theo số lượng tham số $w_{0}, w_{1}, etc..$

2u - 4 = 2(3x + 2) - 4 = 6x
dg(f)/df * df(x)/dx = (2f-4) * 3 
= (2*(3x + 2) - 4) * 3 = (6x + 4 - 4) * 3 = 6x * 3
 
**Finally Evaluation function Overview: LR using MSE -> BCE.**
+ @ Tập trung vào **giải thích Cách Tiếp Cận chứ không chỉ giải thích đơn thuần.** -> Hiểu sâu hơn và tự chủ đc nhiều hơn. Giúp ng đọc hiểu vì sao lại chọn Hàm Loss này mà ko chọn hàm loss khác.
MSE (tính chất và giải thích)
- Với X, Y tại vị trí này thì Hàm F bằng bao nhiêu. 
- Convex -> Luon luon lớn hơn hoặc bằng 0. Biết hàm L là Convex nhưng chưa biết nó làm gì. 
+ Điều kiện: giúp đánh giá model tốt với 
	1) Hàm Loss càng nhỏ model càng tốt. e.g. y(x) = 0.01 hoặc khi y tiến tới 1 chỉ định model tốt và Loss trả về giá trị nhỏ. 
	2) Hàm Loss càng lớn model càng tệ  e.g. y(x) = 0.9
+ Thử chọn các giá trị y = 0 để xem Loss tăng giảm ntn.  
+ ? **Thử Nghiệm 1:** Với **x=1 và y=-log(x)** ta thấy x càng lớn thì y càng nhỏ và ngược lại -> Đạt đk 1 + 2, phù hợp cho đánh giá cho x -> 1.    
+ ? **Thử Nghiệm 2:** Song song với đó với **x=1 và y=-log(1-x)** kết quả ngược hoàn toàn, nhưng vẫn đạt đk 1+2 khi x càng tiến gần 0 thì y càng lớn và càng gần 1 (xa 0) thì y càng cao
+ $ Từ 2 thử nghiệm trên mình kết luận được TN1 giúp tính Loss khi cần x tiến đến 1. và TN2 khi cần Loss tiến đến 0.
+ @ Từ từ đã, 1 và 0 có thể đại diện cho 2 lớp, sẽ thế nào nếu mình kết hợp hàm loss cho cả TH1 và TH2.   
![[Pasted image 20251109214802.png]]
Để mô tả, mình có thể viết dưới dạng if 1 else 0, nhưng trong viết báo khoa học, mình cần mô tả công thức dưới dạng 1 phương trình -> ta có đc công thức Binary Cross-Entropy. Ta-Da.
![[Pasted image 20251109215611.png]]
![[Pasted image 20251109215746.png | 444]]

![[Pasted image 20251109220050.png]]
![[Pasted image 20251109220101.png]]
$\hat{y}$ have range from 0 to 1 -> perfect for classification. Tính hàm Loss với y=0 và y=1 rồi tối giản công thức. Xác suất thuộc range(0, 1). Công thức $f(y, \theta, x)$ thầy nói là gộp (Nhân) lại thì đc cthuc này. Vì nếu đặt x là 0 hay 1 thì nó vẫn trả về đúng công thức if else như mong đợi. 
![[Pasted image 20251109220311.png]]
Do là nhân nên sẽ tiến đến 0 hoặc 1 -> expoding gradient hoặc vanishing gradient -> Sử dụng log để biến thành tổng -> Hàm này nói để maximize giá trị -> Mình muốn lấy Minimize thì thêm dấu trừ ở trước là xong. 
![[Pasted image 20251109221329.png]]
Phần tiếp theo -> CM Convex. 

**Ý tưởng của Logistic Regression**
So sánh MSE và BCE 
Sau cùng Traditional -> Vectorize và so sánh. 
![[Pasted image 20251109222829.png]]

1) Overview lý do cần LoRes vì nó fit đúng data. 
2) Giải thích các bước của LoRes và đạo hàm hàm Loss
3) Giải thích trực giác của cách chọn hàm Loss MSE -> BCE. Vì sao ko dùng MSE -> 1 hàm loss lý tưởng sẽ ntn.  
4) Giải thích hàm loss BCE theo 2 hướng
	1) Trực quan hóa từ vấn đề, tiếp cận bài toán từ nhu cầu tìm 2 hàm loss mới để thay thế MSE (vì nó non-convex) - giải thích convex ở đây...convexity là gì. 
	2) Sử dụng XSTK, đi từ cthuc Benoulli cho bài toán phân loại nhị phân.  
5) So sánh MSE và BCE 
	1) bằng cách tính Convexity 
	2) Loss phạt các dự đoán sai khác nhau ![[Pasted image 20251110010008.png | 333]] 
6) 1 Cách tiếp cận khác là sử dụng Entropy
7) [LoRes code](https://youtu.be/HovUiBPojwo?si=97UDcm7Hu37-cd5S)
