## Section 1: Discrete Random Variables
**Book1:** Undergrade, Highschool difficulty
**Book3+4:** Bachelor & Master
**Book4+5:** Master and Higher (Theory behind statistic)
![[23fa284840f0d5f308ef5f1daa487aee.jpg|400]]

Note: khi viết docs, giải thích vì sao từng công thức vì sao lại như thế. 
### (Discrete) Random Variables
![[Pasted image 20250717135645.png# left | 400]]


**Continous Random Variables** 


**Probability Mass Function**
`Pr` - represent the probability of a countable events (events must be discrete)
	e.g. `p(x) = Pr(X = x)`
	
**Probability Distribution Function** 
+ ? Notate as `F[n]`. PDF of an event 
![[Pasted image 20250717140717.png| 500]]


**Đánh giá:** bài nói chỉ dừng lại ở trạng thái Nhận Biết, áp dụng công thức, ôn lại kiến thức, chưa thể hiểu tốt bản chất lý thuyết, cơ chế đằng sau từng công thức với nội dung bài giảng. Tham khảo khóa học XSTK cho AI của Andrew Ng để cải thiện.

### Mathematical Expectations
**Expectation $E(X)$**  
(Chỉ số cho biết 1 hoặc nhiều events có xác suất xảy ra cao nhất)
![[Pasted image 20250717141635.png| 500]]
Chứng minh cho $E[\alpha X] = \alpha E[X]$ với $\alpha$ là hệ số.

**Mean $\mu$**
![[Pasted image 20250717165114.png| 500]]
$E[X]$ **also called the mean of X**


**Variance $\sigma^{2}$ or $S^2$**
bình phương để ko bị âm nữa. 1 cách khác để tính Varaince là tách cả X và $\mu$ bình phương ra và tính như bình thường. 
$$Var(X) = E[(X - \mu)^{2}] = \sum_{k}(x_{k} - \mu)^2p(x_{k}) $$

**Standard Deviation $\sigma$ or $S$**
-> Connect to Variance
![[Pasted image 20250717144558.png | 500]]

**Standard Deviation Overview**
![[Pasted image 20250717144929.png]]


**Continuous Random Variables**
CRV sử dụng Rieman method để tính tích phân qua việc tính diện tích hình chữ nhật cho từng giá trị rồi cộng lại với nhau) -> Diện tích đằng sau đường cong. 
+ ? Trong XSTK, mình phải dùng tích phân Lebesgue vì trong XS, kích thước của từng hình chữ nhật không đồng đều với nhau nhưng về cơ bản thì vẫn chia ra từng hcn nhỏ rồi tính tổng. Nói chung, chỉ khác nhau ở cách tính giá trị kì vọng.
	có thể nói giống Rieman Method nhưng nó Dynamic hơn. 
![[Pasted image 20250717152736.png| 500]]
**VÍ dụ thực tế:**
Biến ngẫu nhiên rời rạc: bốc từng viên kẹo ra rồi đếm rồi tính sum. 
Biến ngẫu nhiên liên tục: khó hơn vì tính liên tục của nó, nên các giá trị ko có đều với nhau.
![[Pasted image 20250717153401.png|500]]

### Convariance & Correlation
#### Covariance (Hiệp số phương sai)
Covariance là tích của X và Y hiệu với giá trị kì vọng của chính nó.  Khoảng cách của X và Y so với giá trị kì vọng tương ứng. Tổng của X trừ cho giá trị kì vọng của X nhân với Y trừ cho trị kì vọng của Y.
	N - 1 là hệ số sau khi đã điều chỉnh. Vì bản chất là mình đã dùng 1 điểm mang đi so sánh với Mean, nên tổng số biến sẽ trừ đi 1 biến đó.  
	
![[Pasted image 20250717154250.png| 500]]
+ $ Vì hiệp số phương sai tính variance giữa 2 biến với nhau dùng tích. Nên Covariance $S$ của chính X  chính là Variance ($S^2$) 
$$\frac{\sum{(x-\mu_{x})}{(x - \mu_{x}})}{n-1} = \frac{\sum{(x-\mu_{x})^2}}{n-1}$$
![[Pasted image 20250717155019.png]]

[00]: X và chính nó
[01]: covariance của x và y  
[10]: covariance của x và x
[11]: covariance của y và y

#### Correlation (Hiệp số tương quan)
![[Pasted image 20250717155401.png]]
