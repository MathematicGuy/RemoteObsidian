Evaluation Metrics for Classification Problems
+ ? Goals: find the best metrics for a your classification problems.

**Binar Classification Metrics**
![[Pasted image 20241123200625.png]]
Evaluation type:
	Exact Match Ratio
	0/1 Loss
	Hamming Loss
	Accuracy, Recall, Precision, F1-Score

# Accuracy Metric
![[Pasted image 20241125044957.png]]


note: Heuristic Algorithm mean simple agorithm 
![[Pasted image 20241123202138.png]]
+ ? Simple algorithm like Heuristic return high accuracy if the data are unbalance in it advantage (i.e. y=0). If y=1 accuracy would be super low.  
skewed class ~ imbalanced data (simply bias data)
+ ! **Disadvantage:** **Accuracy metric don't reflect real performance** if the data are imbalanced 
![[Pasted image 20241123201846.png]]


# Confusion Matrix
+ $ Để khắc phục nhược điểm trên, ta dùng Confusion Matrix:
![[Pasted image 20241123202817.png]]

**False Positive Rate (FPR)**: Kq Sai nhưng lại dự đoán là kq Đúng
![[Pasted image 20241123203406.png]]
**FPR High:** TH dự đoán sai tăng nma sẽ ko bỏ sót những bệnh nhân bị cancer $\to$ **có thể chấp nhận FPR ở 1 mức nào đó** để đảm bảo ko có bệnh nhân nào bị bỏ sót.


**False Negative Rate (FNR)**
![[Pasted image 20241123203633.png]]
FNR High: phát hiện sót

