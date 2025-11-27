So sánh giữa 2 phân bố, True và False. 
![[Pasted image 20251115203343.png]]
How to measure the diff between 2 distribution ? need a **evaluation metric** - our metric needs to be **symmetric or asymmetric.**
![[Pasted image 20251115203636.png# left  | 344]]
Chia phân phối của từng lớp rồi lấy tổng trung bình. Nhưng giá trị sẽ bị skew bởi số lớn ie. 1/4 và 4 
![[Pasted image 20251115204512.png]]
Cần thiết kế 1 công thức để đảm bảo tính cân bằng trong dải giá trị -> Sử dụng Log. 
Note: 
+ P(x) xs của mỗi lớp trong phân phối 1
+ Q(x) xs của mỗi lớp trong phân phối 2. 
+ P(x) / Q(x) - So sánh phân phối 1 và 2 -> Để  xét độ quan trọng cho từng lớp trong phân phối 1 và 2. (Khoảng cách, độ tương đồng giữa pp1 và 2)
+ Nhân thêm P(x), mình sẽ tính được độ quan trọng của từng lớp (Amount of say)  giữa 2 phân phối (Grounth Truth và Prediction).
-> That KL Divergence. Tính khoảng cách giữa 2 phân phối. 
![[Pasted image 20251115205336.png# left  | 433]]

Entropy lớn -> bất ngờ lớn -> dataset ko thuần khiết và khó dự đoán. 
Cross-Entropy - nhiều phân bố. 
![[Pasted image 20251115211209.png]]
Tìm $\theta$ để kéo 2 cái Distribution lại gần nhau. 
![[Pasted image 20251115211548.png | 544]]

![[Pasted image 20251115212332.png | 544]]
Hinge Loss (cho SVM)
-> improve generalize well to unseen data, less prone to overfitting. 

**Label Smoothing**
![[Pasted image 20251115221607.png]]
Tự động chia đều các % cho các nhãn khác. 

Công thức tính xác xuất của các lớp khác.  
![[Pasted image 20251115221823.png]]

**Multi-Class vs Multi-Label**
![[Pasted image 20251115222419.png# left ]]
**Multi-Class** - mean there are many class but only 1 label can be Correct.
	Categorical Cross Entropy và Softmax - class xs cao nhất mới trả về khi sử dụng one-hot encoding. 
	 
**Multi-Label** - Multiple Lable mean there are many class and many label can be Correct. (Phân loại nhiều lớp sử dụng Binary Cross Entropy trong bài toán Logistic Regression vs chiến thuật One versus all)


**Pairwise Ranking Loss** - phân loại 2 label chó mèo muốn đc chọn thành 1 lớp. ->  Loại bỏ các Class thừa tr'c. Rồi phân loại 2 label chó mèo sau.
> Tối hơn thay vì chỉ dùng Hinge Loss thuần để phân loại.
![[Pasted image 20251115224029.png]]


