## Descriptive Statistic
### Sample Mean vs Population Mean
![[The Organic Chemistry Tutor - Sample Mean and Population Mean - Statistics [cmtBUWCC-6A - 1161x653 - 3m14s].png# left | 500]]
+ ! Trong thực tế, **không phải lúc nào mình cũng có đủ toàn bộ dữ liệu**, việc thu dữ liệu 8 tỷ người cho 1 dự án cá nhân là gần như không thể và mất thời gian. 
+ ? Làm sao để **Mean trên cùng 1 tập dữ liệu nhưng nhỏ hơn $\approx$ kết quả Mean trên dữ liệu đầy đủ**.   

```ad-success
**Sample Mean $\mu$** là **Mean của 1 tập con** trong toàn bộ tập dữ liệu $\rightarrow$ giá trị càng xấp xỉ Mean càng tốt. e.g. tính mean của 1000 người thay vì 8 tỷ người.

**Mean $\bar{X}$** là Mean tính trên toàn bộ tập dữ liệu. e.g. *tính mean của toàn bộ 8 tỷ người.* 
```

```ad-summary
+ Sample là thuật ngữ trong Thống kê, trong khi Population chỉ là 1 tham số.  
+ Sample Mean càng gần với Population Mean càng tốt -> giúp giảm số điểm dữ liệu để tính toán.
```


*Ôn tập:*
+ Mean là **giá trị trung bình** từ *dữ liệu thực tế* đã thu thập được. (ko bao gồm xác suất). 
+ Expected Value là **giá trị trung bình mà ta mong đợi** *trước khi thu thập dữ liệu thực tế* (Mean nhưng nhân thêm với xác suất cho mỗi biến)
	
+ Variance cho biết độ lệnh / phân bố của dữ liệu so với giá trị trung bình.
	Bằng cách lấy giá trị tuyệt đối của hiệu từng điểm so với Mean. Để đạt được điều này, ta lấy Variance bình phương, rồi căn bậc hai để có giá trị chuẩn. Giá trị này được gọi là Standard Deviation (i.e. căn bậc hai của bình phương variance).
	
+ $ Vì **Sample mean chỉ tính trên 1 tập con**, nên nó sẽ **bị lệch so với Population Mean**. Dẫn đến Variance của Sample Mean sẽ luôn  
![[Pasted image 20250723130215.png]]
+ ? Câu hỏi, làm sao để Sample Mean gần với Population Mean nhất mà không phải lấy thêm Mẫu (i.e. tăng số lượng n).
![[Pasted image 20250723140318.png# left | 500]]

### Explain (n - 1) with Degree of Freedom
+ $ Lấy (n - 1), vì khi tính Estimated Variance ta lấy mọi mẫu trừ đi Sample Mean ngoại trừ chính nó (i.e. $\bar{x} - \bar{x}$), vì trong 1 tập, Sample Mean sẽ là 1 giá trị trong tập đó. Trong Degree of Freedom, ta nói mình đang loại trừ 1 TH để tính ra được Estimated Variance, việc loại trừ đi 1 giá trị tương đương với việc loại trừ 1 phép tính để tính ra được kết quả. 


Degree of Freedom: số biến mình có thể thay đổi trong 1 hàm số để đưa ra kết quả. Ví dụ mình có 1 hàm f(x, y) = xA + By  sau khi tối giản hàm đó mình hàm f(x) = xA. Vậy x là giá trị duy nhất mình có thể thay đổi trong hàm nói cách khác mình chỉ có 1 bậc tự do (degree of freedom). 

Tương tự như thế trong XSTK, khi với 1 đồng xu 2 mặt, tung 100 lần, hỏi số lượng Ngửa và Sấp là bao nhiểu.

**VD 1:**  Trong TH trên Degree of freedome sẽ là 2, vì ta chỉ cần có hai cách tối thiểu để xác định số lượng Ngửa và Sấp, ví dụ khi biết số mặt sấp ta có thể suy ra số mặt ngửa, và ngược lại.
	Nhưng nếu ta đã biết số xu ngửa thì có thể xác định ngay đc số xu sấp bằng cách lấy 100 trừ đi, nên Degree of freedom sẽ là 1, vì hàm xác định số mặt ngửa chỉ cần 1 thông tin là X để xác định số mặt ngửa
		.   
		Trong thuật toán, ta có thể nói Degree of Freedom là số lượng Tham số tối thiểu để có được đầu ra mong muốn. 

**VD 2:** Cho 1 túi cho 3 viên bi xanh, đỏ và cam, hỏi viên bi cuối cùng bốc đc có màu gì.
	Nếu bốc 2 viên bi, ta sẽ chắn chắn biết viên còn lại là cam. Vậy nên bậc tự do sẽ là 2 vì ta chỉ cần có 2 thông tin để biết được viên bi thứ 3,  

### Explain (n - 1) with Geometric:
![[Pasted image 20250725071928.png| 200]]

![[Pasted image 20250725074132.png|500]]

**The Pattern**
![[Pasted image 20250725075221.png|350]]


## Advanced Descriptive Statistics
### Coefficient vs Regression
+ ? **Correlation describe** the relationship of 2 **independent variable** while **regression describe** **dependent** one (e.g. ax + b = y). 
+ $ In this part, we'll learn how Correlation measures the strength and direction of a relationship between 2 or more variables.   
![[Pasted image 20250726134438.png|300]]

Relationship between variable describe using **Pearson Correlation $(r)$**, which **describe the strength of a relation from a coefficient between value from -1 to 1.** Where
+ -1 indicates **Highly Negative Relationship** (e.g. both x, y decrease). As o**ne variable decreases, the other decrease proportionally.**
+ 0 indicate **no relationship**, Correlation close to 0 say the changes of value in 1 doesn't relate changes of value of the other.   
+ 1 indecates **Highly Positive Relationship** (e.g. both x, y increase). As one variable increases, the other increase proportionally.
+ ? **Notice:** **Pearson Correlation assumpt the relation between data where the data approximately normally distributed, its also sentive to outlier** and **only apply for linear relationships.** If the relationship is non-linear, the correlation coefficient (i.e. value -1 to 1)  may not accurately reflect the association between the variables. 
+ $ For non-normally distributed data, see Spearman's rank correlation. 
![[Pasted image 20250726134203.png| 500]]


**Correlation doesn't mean Causation**, if the ice-cream price go up and shark accident occurrence rate both go up in the summer doesn't mean they are the cause of the other. 
-> Research using Correlation to **investigate naturally occuring variables may be unethical or impracticale to test/experiment.**
+ ? Example: you cannot force someone to stop selling ice-cream to see if those shark will stop attacking people. Or catch and force people to stop smoking to see weather smoking causes lung cancer.       

Before calc correlation between variables, let revision about Variance. As you know, variance is the average squared deviations from the mean $\sigma^2$, the square help us to avoid negative but if we calc the variance for height in meter, the variance would be in $m^2$ -> Doesn't express original value meter $m$.

To express the original value meter, we can take the square root of variance $\sqrt{\sigma^{2}}= \sigma$. This call **Standard Deviation.**

### Covariance
+ $ Apply Variance for multiple variables, that basically what Co-variance mean, multiple-variance. 
+ Covariance allow us to see relationship between variables (e.g. x, y) 
![[Pasted image 20250726145222.png# left | 555]]
+ ! Because **Covariance is base on variance**, so its really describe the relationship between variables's variance, thus **if we scale variables value, covariance will scale along too**. This make Covariance hard to interpret since large/small value always convey large/small covariance,  covariance can't fully interpret relationship between multiple-variable. 
+ ? So, how can we only measures the relationship between variables since Covariance convey both variables relationship and variance.

+ $ A simple way solution is to **normalize Covariance by divide to their Variance instead of their total population number**. This remove the scaling factor while preserve the hidden relationship behind. 
$$p_{X, Y} = \frac{Cov(X, Y)}{\sigma_{X} . \sigma Y}$$
This equation is called **Correlation Coefficient (Hệ số tương quan).** Examples:
![[Pasted image 20250726153258.png|555]]

This is only the Use Case for Linear data, for other case, you can use these equations:
![[Pasted image 20250726151608.png|500]]

Because Expected Value have Linear property for function:
If $g(x) = aX$ then $E[g(x)] = E[aX] = a.E[X]$ where $E[const] = const$. And Covariance divide itself by Variance (which contain the Expected Mean). If we was replace x and y with a function, the functions would divide to eachother.
**Example:** 
![[Pasted image 20250726154236.png|555]]

![[Pasted image 20250726154536.png|555]]



