# Evaluation Metrics for regression
+ ? From emtrics to loss functions

Loss Function using: Linear, SVM, Decision Tree
+ ? note: we cannot calc accuracy for regression model.
*buổi sau nói hiệu quả/suất của các giải thuật loss*

Dùng nhiều loại kiểm tra lỗi khác nhau để kiểm tra độ chính xác:
![[Pasted image 20241109201338.png]]
$e^{b}_{t}$ : b as base line


# Scale-Dependent Errors
### Mean Error (ME)
+ ? Just Calc the mean
$$ME = \frac{1}{n}\sum^{n}_{i=1} (y_{i} -\hat{y_{i}})$$
-> So if the ME < 0, that mean our predicted value (machine predict value) is larger than the training value (i.e. actual value)
![[Pasted image 20241109201925.png]]


**Disadvantages:**
+ **Neg and Pos value can cancelled eachother. ME = 0 so we cannot evaluate our Model -> Misleading accuracy.**
+ Bc of the cancellation property, this func is sensitive ot outliers (super large or small number)


### Mean Absolute Error (MAE)
![[Pasted image 20241109202203.png]]
+ $ **Solve Error Cancellation problem above**. 
> Bc the predicted and actual value cancell eachother but not negative. So the closer to 0 MAE is, the better our prediction is. 
![[Pasted image 20241109202403.png]]
+ Equal weight errors because MAE is less sensitive to outlier and all value is divided to 5 (i.e. total loss)

+ ! Problem: if 2 MAE are equal. 
	 both MAE = 11. ![[Pasted image 20241109203211.png]]
	But predict 1 are more stable (5,5,5,5,5) and predicted 2 are more disbulant. ![[Pasted image 20241109203318.png]]
+ $ Therefor MAE **provides the average error magnitude but does not give information about the variance and bias.**
> Chọn 1 làm mô hình tốt nhất.
#### Casestudy
![[Pasted image 20241109203709.png]]
note: If not remove outlier, model can be overfitting. (go across all point, even the outlier)
+ $ doesnt reflect the actual value when their are outliers.


### Mean Square Error (MSE)
+ $ **Advantage** is MSE penalize large errors bc errors are squared.
+ ! **Disadvantage**: In constract, outliers also squared so MSE is sensitive to outlier, notify lead to overfitting.
Also it Scale dependent errors: this mean it prone to error if data are not re-scale using normalized and standardized technique.


### Mean Absolue Percentage Error (MAPE)
$$MAPE = \frac{100}{n}\sum^{n}_{i=1}\left(\left|\frac{y_{t} - \hat{y_{t}}}{y_{t}}\right| \right)$$
![[Pasted image 20241109205535.png]]
> Chọn 1 là mô hình tốt nhất.

> Giá trị có thể > 100%
![[Pasted image 20241109205519.png]]

+ $ **Advantage**: do **tính theo % nên MAPE Scale-Independent** và dễ hiểu. Giải quyết vấn đề scale-dependent ở MSE là nhạy cảm vs outlier.
+ ! **Disadvantage**: Nếu **actual value = 0 MAPE sẽ undefined/infinite** (giải pháp sẽ là cộng thêm 1 giá trị epsilon bé 0.00001 để chống gtri ~0).

#### Casestudy
![[Pasted image 20241109205846.png]]
+ ! **Cannot define Over or Under estimate/foirecasting** since MAPE take absolute value thus value larger and smaller than the mean by 10 will end up with the same result = 10%. **Both contribute equally to error metric.**
+ ? For instance, cannot define error for low & high drug usages -> super dangerous ofcourse.

![[Pasted image 20241109210354.png]]
+ ! **Depend on Actual Value scale.** **All error are treated equally (Asymmetrical Error Treatment) but not reflect the actual error** 
![[Pasted image 20241109210449.png]]

# Symmetric Mean Absolute Percentage Error (sMAPE)
![[Pasted image 20241109223046.png]]
![[Pasted image 20241109210703.png]]
> Chọn 3 làm mô hình tốt nhất.
+ $  **Giải quyết đc TH: Actual value = 0**. And solve symetric problem above, sMAPE **treated over and under estimate more equally.** -> less bias for sMAPE.



#### Case Study
![[Pasted image 20241109211332.png]]
note: cần bik over hay under để tăng hay giảm kết quả dự đoán.
+ ? Liệu có Loss function nào để giải quyết vấn đề ko xác định đc under/over estimate.

Modify version to solve dividing to 0 error and super smaller number problem.
![[Pasted image 20241109211604.png]]

# Relative Errors
>2 Cách tính mean: thông thường và hình học

**MRAE**
![[Pasted image 20241109211846.png]]

**naive method:** sử dụng random-walk để chọn giá trị dự đoán.
sử dụng baseline để xác định over/under estimate.  performance của nó so vs performance của baseline.

note: có normalization -> scale in-dependency. 
![[Pasted image 20241109212843.png]]
+ ! nếu predict = actual -> undefined. So it require a Baseline Model (Best model up to date) for comparison, which maz not always available.
> Solve by shifting current predicted value to the next predicted value (thus the first value is NaN)

![[Pasted image 20241109212849.png]]

note: so sánh giá trị dự đoán (current forecast) vs **benchmark forecast (thuật toán dự đoán/forecast tốt nhất hiện tại)** để kiểm tra độ hiệu quả.

+ ! Sensitive nếu denominator (mẫu số) quá nhỏ. Vd: nếu chia cho 0.2 MRAE sẽ rất lớn.
![[Pasted image 20241109213206.png]]

### GMRAE
![[Pasted image 20241109213635.png]]
![[Pasted image 20241109213333.png]]

99 samples lỗi nhỏ nhưng 1 samples lỗi lớn -> có 1 outlier. Làm sao để giảm cái outlier đó -> dùng mean
![[Pasted image 20241109213513.png]]

![[Pasted image 20241109223410.png]]
+ $ **Reduce the effect of very large errors, making it more robust to outliers.**
(khi nhân giá trị outlier )
#### Casestudy
![[Pasted image 20241109213844.png]]
+ ! Still dependent on the denominator. In time 2, although error is small but GMRAE notified larger error than time 1 while time 1 have bigger error.

# Relative Measures
![[Pasted image 20241109214033.png]]
### Relative Mean Absolute Error (RelMAE)
relative -> lấy trung bình cho cả tử, cả mẫu
![[Pasted image 20241109214018.png]]
![[Pasted image 20241109214231.png]]
**Casestudy**
![[Pasted image 20241109214208.png]]
![[Pasted image 20241109214732.png]]
> Yếu đối với lỗi lớn. Lỗi lớn áp mất lỗi nhỏ. Time 3 lỗi là 100 chiếm phần lớn so vs các gtri còn lại.

**Relative Squared Error (RSE)**
![[Pasted image 20241109214926.png]]

![[Pasted image 20241109215050.png]]
![[Pasted image 20241109215232.png]]
+ $ note: cứ có số mũ là sensitive vs outlier.

![[Pasted image 20241109215451.png]]


**Mean Absolute Scaled Error (MASE)**
![[Pasted image 20241109215601.png]]
+ ? chia cho giá trị thực tế mong đợi cho vs baseline. Dùng Baseline nên mẫu số áp dụng cho mọi Predicted.
![[Pasted image 20241109215824.png]]

Cho có chia nên vẫn bị lỗi chia cho 0
![[Pasted image 20241109215947.png]]

# Other Metrics
![[Pasted image 20241109220004.png]]

**Percentage Better (PB)**
![[Pasted image 20241109220137.png]]
+ ? Dùng để mô tả **Mô hình tốt hơn ntn so vs mô hình baseline**. 
+ ? If **PB(MAE) = 100% mean model performs exactly as well as the baseline.**

![[Pasted image 20241109223743.png]]
+ $ **Describe how often the model's error is smaller than the baseline**
(Baseline is like the global standard, often use to comparision)



**Root Mean Squared Logarithmic Error (RMSLE)**
![[Pasted image 20241109220204.png]]
log trc: thực tế, log sau dự đoán

#### Casestudy
![[Pasted image 20241109220247.png]]
![[Pasted image 20241109220509.png]]
+ $ **RMSLE Reduce Outlier influence.** vì RMSLE có normalize giá trj rồi.

# From Evaluation Metrics to Loss Functions

+ $ **MAE** is more robust to outlier
![[Pasted image 20241109220821.png]]

+ $ **MSE** Penalize Error heavier 
![[Pasted image 20241109220845.png]]
-> báo hiệu lỗi quá lớn nên mô hình có thể tập trung quá vào lỗi. Cố gắng fit đường thẳng vào điểm outlier và bỏ quên các điểm khác.
![[Pasted image 20241109221100.png]]
+ ? Có 10 điểm nhưng 1 điểm outlier, thì đg thẳng sẽ tập trung vào outlier và có thể bỏ quên 10 điểm kia <-> giảm hiệu quả của hàm cho vs 10 giá trị để dự đoán 1 giá trị outlier.

![[Pasted image 20241109221335.png]]
**Huber Loss**
![[Pasted image 20241109221223.png]]
+ ? Có cách nào để có 1 cái metrics (hàm loss) để dung hòa các disadvantage của các Evaluation Metrics kia.


