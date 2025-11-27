![[Pasted image 20251108200850.png]]
# Evaluation Metrics for regression
+ ? From metrics to loss functions
![[Pasted image 20241121103348.png]]
$e^{b}_{t}$ : b as base line

Loss Function using: Linear, SVM, Decision Tree
+ ? note: we cannot calc accuracy for regression model. Dùng nhiều loại kiểm tra lỗi khác nhau để kiểm tra độ chính xác:
*buổi sau nói hiệu quả/suất của các giải thuật loss*

# Scale-Dependent Errors
+ @ Dependent on the scale of the series (??scale of the series)
## Mean Error (ME)
$$ME = \frac{1}{n}\sum^{n}_{i=1} (y_{i} -\hat{y_{i}})$$
+ @ **Intuitive Definition:** Measures how far predictions are from actual values on average, considering whether the model tends to overpredict or underpredict.
+ ? **Example Intuition:** If ME = -5, predictions are, on average, 5 units below actual values. 
+ & **Use Case:** Checking the average over or underestimation by a model.
![[Pasted image 20241109201925.png]]
+ $ **Advantage:** Indicates systematic bias in predictions.
+ ! **Disadvantages:**
	+ **Neg and Pos error can cancel out eachother.** ME = 0 so we cannot evaluate our Model -> Misleading accuracy, not true goodness of the model.
	+ Bc of the cancellation property, this func is sensitive ot outliers (super large or small number)

## Mean Absolute Error (MAE)
+ $ Solve neg and pos cancelling out eachother problem. 
![[Pasted image 20241109202203.png]]
>*Solve Value Cancellation problem in ME* 
- @ **Intuitive Definition:** Calculates the average magnitude of errors without considering direction (over/underestimation).
- ? **Example Intuition:** MAE = 10 means the model is off by 10 units on average.
+ & **Use Case:** Assessing average error magnitude (e.g., predicting house prices).
> Bc the predicted and actual value cancell eachother but not negative. So the closer to 0 MAE is, the better our prediction is. 
![[Pasted image 20241109202403.png]]
+ Equal weight errors because MAE is less sensitive to outlier and all value is divided to 5 (i.e. total loss)

+ $ **Advantage:** Intuitive and robust to outliers compared to MSE.
+ ! **Disadvantage**: Does not penalize larger errors more than smaller ones. Make 1 large error (prediction) carried the whole calculation.
	Problem: if 2 MAE are equal. both MAE = 11. ![[Pasted image 20241109203211.png]]
	But predict 1 are more stable (5,5,5,5,5) and predicted 2 are more disbulant. ![[Pasted image 20241109203318.png]]
+ $ Therefor MAE **provides the average error magnitude but does not give information about the variance and bias.**
> Chọn mô hình 1 làm mô hình tốt nhất.

### Casestudy
![[Pasted image 20241109203709.png]]
note: If not remove outlier, model can be overfitting. (go across all point, even the outlier)
+ $ Doesnt reflect the actual value when there're outliers.

## Mean Square
### Mean Square Error (MSE)
![[Pasted image 20241121094140.png]]
- @ **Intuitive Definition:** Averages the square of each error, penalizing larger errors more heavily.
- ? **Example Intuition:** MSE = 25 means the average squared error is 25, emphasizing that big errors are significant.
+ & Comparing model fits (e.g., energy consumption prediction).

+ $ **Advantage** is MSE penalize large errors **bc errors are squared.** However, this is a 2 edge sword when there're outliers. 
+ ! **Disadvantage** is MSE also magnified the outlier. Hence sensitive to outliers and lead to unstable loss function. e.g. 1 value larger x10 the rest can can break the loss function. 
Also it **Scale dependent errors:** this mean it *prone to error if data are not re-scale using normalized and standardized technique.*

# Percentage Errors
+ @ Base errors are scaled by actual time series values 
## Mean Absolue Percentage Error (MAPE)
$$MAPE = \frac{100}{n}\sum^{n}_{i=1}\left(\left|\frac{y_{t} - \hat{y_{t}}}{y_{t}}\right| \right)$$
![[Pasted image 20241121095028.png]]
- @ **Intuitive Definition:** Calculates the **average percentage error between predictions and actual values.** Basically use **% instead of number for error** by comparing actual and prediction value.  
- ? **Example Intuition:** MAPE = 20% means predictions are off by 20% on average compare to the actual values.
+ & **Use Case:** *Evaluating errors relative to actual values* (e.g., sales forecasts).

![[Pasted image 20241109205535.png]]
> Chọn 1 là mô hình tốt nhất.

+ ! Giá trị có thể > 100% vì hiệu của gtrj dự đoán và gtrj thật luôn dương.
![[Pasted image 20241109205519.png]]
+ $ **Advantage**: do **tính theo % nên MAPE Scale** Independent và dễ hiểu. **Giải quyết vấn đề scale-dependent** ở MSE là **nhạy cảm vs outlier.**
	+ $ Scale on actual value so it give out Independent evaluation % for each dataset. 
	+ $ Easy to understand since it compare base on %. 
+ ! **Disadvantage**: Sensitive to 0. If **actual value $y_{t}=0$ MAPE is undefined/infinite** (giải pháp sẽ là cộng thêm 1 giá trị epsilon bé 0.00001 để chống gtri ~0).

#### Casestudy
![[Pasted image 20241109205846.png]]
+ ! **Cannot define Over or Under estimate/forecasting** since MAPE take absolute value thus value larger and smaller than the mean by 10 will end up with the same result = 10%. **Both contribute equally to error metric.**
+ ? For instance, cannot define error for low & high drug usages -> super dangerous ofcourse.
![[Pasted image 20241109210354.png]]
+ ! **Depend on Actual Value scale.** **All error are treated equally (Asymmetrical Error Treatment) but not reflect the actual error** 
![[Pasted image 20241109210449.png]]

## Symmetric Mean Absolute Percentage Error (sMAPE)
+ $ **Improvement:** reduce bias toward a bigger/smaller value. More symetric, reduce bía, but not solve this problem definitely.  $\text{predict\_actual\_diff} / \text{predict\_actual\_Average}$
![[Pasted image 20241109223046.png]]
- @ **Intuitive Definition:** **Balances the relative percentage error** to both **actual and predicted values to avoid over/under bias.**
- ? **Example Intuition:** sMAPE = 15% means the error is about 15% of the average size of actual and predicted values. 
+ & **Use Case:** Alternative to **MAPE** **for** **symmetrical error handling**.

![[Pasted image 20241109210703.png]]
> Chọn 3 làm mô hình tốt nhất.
+ $  **Giải quyết đc TH: Actual value = 0**. And solve symetric problem above, sMAPE **treated over and under estimate more equally.** -> less bias between predict and actual value.

+ $ **Giảm bớt độ Bias so với MAPE nhưng vẫn bị lỗi khi so với 0**. e.g. 20 so với 100 là 66.67% giúp mô hình đc đánh giá công bằng và ổn định hơn.    
![[Pasted image 20251108211505.png]]

### Case Study
![[Pasted image 20241109211332.png]]
+ ! Kết quả lớn và bé đều ra 1 kết quả khi over và under predict vì giá trị luon dương -> **Không thể bik over hay under để tăng hay giảm kết quả dự đoán. Giống MAPE** -> Không thể cải thiện model. 
+ ? Liệu có Loss function nào để giải quyết vấn đề ko xác định đc under/over estimate.

### sMAPE Modified Version
Modify version to **Solve dividing to 0 error** and **super smaller number problem.**
![[Pasted image 20251108212431.png]]


# Relative Errors
+ @ Scaling is done through dividing by errors from a benchmark method.
+ 2 cách tính mean: thông thường và hình học
+ Công thức đánh giá bằng cách **so sánh với 1 cái chuẩn nào đó, baseline nào đó.** 
## MRAE
![[Pasted image 20241109211846.png]]
- @ **Intuitive Definition:** *Compares your model errors to baseline model error (THAT IT)*, focusing on relative performance. => Xem mô hình perform tốt hơn trên actual hay trên baseline hơn. 
- ? **Example Intuition:** MRAE = 0.5 means the model’s errors are half the size of the baseline’s errors -> your model predict better bc the your model error = 1/2 baseline error.  
+ & **Use Case:** *Comparing model performance against a naive benchmark.* 

**Naive Method:** sử dụng *random-walk để chọn giá trị dự đoán*. *Sử dụng baseline để xác định over/under estimate, performance* của nó so vs performance của baseline.
Note: có normalization -> scale in-dependency. 
![[Pasted image 20241109212843.png]]
+ ! Nếu predict = actual -> undefined. So it require a Baseline Model (Best model up to date) for comparison, which maz not always available.
> Solve by shifting current predicted value to the next predicted value (thus the first value is NaN)

![[Pasted image 20241109212849.png]]
Note: so sánh giá trị dự đoán (current forecast) vs **benchmark forecast (thuật toán dự đoán/forecast tốt nhất hiện tại)** để kiểm tra độ hiệu quả.
+ ! **Sensitive nếu denominator (mẫu số) quá nhỏ**. Vd: nếu chia cho 0.2 MRAE sẽ rất lớn. khoảng cách giữa 45 và 9 giống nhau chỉ cần mẫu số thỏa mãn như ở dưới. 
![[Pasted image 20241109213206.png]]


### GMRMAE (Geometric mean of relative errors)
![[Pasted image 20241109213635.png]]
- @ **Intuitive Definition:** Takes the **geometric mean of relative errors, reducing sensitivity to outliers.** **Nhân theo %** cho mỗi Sample nên **khó bị Outlier hơn.** So sánh hiệu quả của model trên actual và baseline theo %, giống MRAE nhưng khó bị outlier hơn.
- ? **Example Intuition:** GMRMAE = 0.4 means the model's performance is better than the baseline by a consistent factor of 0.4.
+ & **Use Case:** **Aggregating relative errors with reduced sensitivity to outliers.**
+ ! Nếu 1 sample bằng 0 thì tất cả bằng 0. 
![[Pasted image 20241109213333.png]]
99 samples lỗi nhỏ nhưng 1 samples lỗi lớn -> có 1 outlier. Làm sao để giảm cái outlier đó -> dùng mean.

![[Pasted image 20241109213513.png]]

![[Pasted image 20241109223410.png]]
+ $ **Reduce the effect of very large errors, making it more robust to outliers.**
(khi nhân giá trị outlier )

#### Casestudy
![[Pasted image 20241109213844.png]]
+ ! **Still** **dependent on the denominator**. In time 2, although error is small but GMRAE **Notified larger error than time 1 while time 1 have bigger error.**

# Relative Measures
+ @ Consider the division of an error measure for the forecasting model, by that of a benchmarking method.
![[Pasted image 20241109214033.png]]
### Relative Mean Absolute Error (RMAE)
>relative -> lấy trung bình cho cả tử, cả mẫu
![[Pasted image 20241109214018.png]]
- @ **Intuitive Definition:** Measures MAE relative to the average size of actual values, providing context for errors.
- ? **Example Intuition:** RelMAE = 0.1 means the average error is 10% of the typical value being predicted.
- & **Use Case:** Measuring MAE relative to average actual values.
![[Pasted image 20241109214231.png]]

**Casestudy**
![[Pasted image 20241109214208.png]]
![[Pasted image 20241109214732.png]]
> **Yếu đối với lỗi lớn.** **Lỗi lớn áp mất lỗi nhỏ ie. 100**. **Time 3 lỗi là 100** chiếm phần lớn so vs các gtri còn lại.
+ ! Không phạt lỗi lướn như Lỗi Nhỏ. Lỗi lớn vẫn ảnh hưởng phần lớn của loss.

### Relative Squared Error (RSE)
![[Pasted image 20251108215708.png]]
- @ **Intuitive Definition:** Compares model performance to a baseline by focusing on squared errors.
- ? **Example Intuition:** RSE = 1.2 means the model’s squared errors are 20% larger than the baseline's.
+ & **Use Case:** Model comparison based on squared errors relative to baseline.

#### Casestudy
**Without Outlier** 
![[Pasted image 20241109215050.png]]
![[Pasted image 20241109215232.png]]
+ $ Note: cứ có số mũ là sensitive vs outlier.

**With Outlier**
![[Pasted image 20241109215451.png]]


# Scale Errors
+ @ Scales the error of a forecasting method by the in-sample MAE of a benchmark method such as the naive method.
## Mean Absolute Scaled Error (MASE)
![[Pasted image 20241109215601.png]]
- @ **Intuitive Definition:** *Compares the MAE (betwen predict at $i$ and $i-1$) to the error of a naive model*, making it interpretable across datasets. Tính performance của model bằng cách so sánh actual error với mọi error sau mỗi bước.   
- ? **Example Intuition:** MASE = 0.8 means the model’s errors are 20% smaller than a naive prediction strategy.
+ & **Use Case:** Comparing model performance across datasets (e.g., time series).
+ $ **So sánh sự khác biệt giữa 2 Sample liền kề** $y_i$ và $y_{i-1}$ **Tốt cho bài toán TimeSeries.**

+ ? Chia cho giá trị thực tế mong đợi cho vs baseline. Dùng Baseline nên mẫu số (denominator) áp dụng cho mọi Predicted vì baseline chỉ có 1.
![[Pasted image 20241109215824.png]]
- $ **Advantage:** Robust and interpretable across different scales.
- ! **Disadvantage:** Requires a baseline model; limited intuitiveness.

Do có chia nên vẫn bị lỗi chia cho 0
![[Pasted image 20241109215947.png]]


## Root Square
### Percentage Benchmark
So sánh sai số của mô hình của mình với các Benchmark. Nếu lớn hơn trả về 0, còn lại trả về 1.
![[Pasted image 20251108220534.png]]
+ ? Tốt hơn trả về 1, else 0. Rồi cộng tổng để tính số % đúng là bao nhiêu trên tổng số.
![[Pasted image 20251108220553.png]]

### Root Mean Squared Scaled Error (RMSSE)
![[Pasted image 20241121101823.png]]
- @ **Intuitive Definition:** **Similar to MASE but emphasizes large errors** by squaring them before comparison.
- ? **Example Intuition:** RMSSE = 1.5 means the model’s errors are 50% worse than the baseline on a squared scale.
+ & **Use Case:** Evaluating scaled error variability across models.

![[Pasted image 20241121101845.png]]
- $ **Advantage:** Emphasizes larger errors while being scale-independent. (scale-independet mean it working for big&small numbers)
- ? **Disadvantage:** Sensitive to outliers. (Unbalance if have outlier)


# Other Metrics
![[Pasted image 20241109220004.png]]
## Percentage Better (PB)
![[Pasted image 20241121104102.png]] 
- @ **Intuitive Definition:** Describe how often the model's error is smaller than the baseline, ignoring the size of errors.
	In short: Describe how often the model's error is smaller than the baseline
- ? **Example Intuition:** PB = 70% means the model is better than the baseline in 70% of the predictions.
+ & **Use Case:** Comparing multiple models on the percentage of better predictions.

+ $ **Advantage:** Provides a simple metric for model dominance.
+ ! **Disadvantage:** Ignores error magnitude.

Note: (Baseline is like the global standard, often use to comparision)
Dùng để mô tả **Mô hình tốt hơn ntn so vs mô hình baseline**. 
![[Pasted image 20241109220137.png]]
+ ? If PB(MAE) = 100% mean model **outperform the baseline every single prediction**
+ ! **Caution:** While PB(MAE) = 100% is a strong indicator of superiority, it doesn’t account for how much worse the model could perform if PB(MAE) were less than 100%. For comprehensive evaluation, combine PB with metrics like MAE or MASE for a full picture.


## Root Mean Squared Logarithmic Error (RMSLE) - MVP
![[Pasted image 20241109220204.png]]
>1st log represent actual value, 2nd log represent prediction
- @ **Intuitive Definition:** Measures **relative errors on a logarithmic scale,** **emphasizing percentage differences rather than absolute ones.**
- ? **Example Intuition:** RMSLE = 0.2 means the average relative difference between the logarithms of predictions and actuals is 0.2.
+ & **Use Case:** Models where relative differences matter more than absolute ones (e.g., income prediction).
	
+ Làm sao để giảm thiểu ảnh hưởng của outlier đối với hàm Loss. 

#### Casestudy
![[Pasted image 20241109220247.png]]
![[Pasted image 20241109220509.png]]
+ $ **RMSLE Reduce Outlier influence.** vì RMSLE có normalize giá trj rồi.
- $ **Advantage:** Mitigates the impact of large outliers and handles relative growth well.
- ! **Disadvantage:** Not intuitive and assumes positive values only.

# From Evaluation Metrics to Loss Functions

+ $ **MAE** is more robust to outlier
![[Pasted image 20241109220821.png]]
Chỉ tính sự khác biệt chứ ko bình phương - less sensitive to outlier. 
+ Giảm outlier vì tính sai số thực so với giá trị thực tế. 

+ $ **MSE** Penalize Error heavier. Thus also sensitive to outlier. 
![[Pasted image 20241109220845.png]]
->Báo hiệu lỗi quá lớn nên mô hình có thể **tập trung quá vào lỗi. Cố gắng fit đường thẳng vào điểm outlier và bỏ quên các điểm khác.** Dẫn tới outlier dc xử lý tốt nhưng các điểm khác bị lỗi cao -> loss vẫn cao khi đánh giá lại sử dụng MAE.
![[Pasted image 20241109221100.png]]
+ ? Có 10 điểm nhưng 1 điểm outlier, thì đg thẳng sẽ tập trung vào outlier và có thể bỏ quên 10 điểm kia <-> giảm hiệu quả của hàm cho vs 10 giá trị để dự đoán 1 giá trị outlier.

Làm sao để xây dựng 1 hàm loss để đối phó vs outlier ? Kết hợp 2 hàm đánh giá ???
![[Pasted image 20241109221335.png]]
**Huber Loss** a combination of MAE and MSE.
![[Pasted image 20241109221223.png]]
+ ? Có cách nào để có 1 cái metrics (hàm loss) để dung hòa các disadvantage của các Evaluation Metrics kia.

![[Pasted image 20251108221506.png]]


---
# KL Divergence
![[Pasted image 20241114211803.png]]

nếu là hằng số là lúc optimization sẽ bỏ, chỉ quan tâm hàm nào có theta.
![[Pasted image 20241114211933.png]]

### The Formula for Binary Cross-Entropy ?

chỉ quan tâm tới tham số theta 1
![[Pasted image 20241114213959.png]]

![[Pasted image 20241114214011.png]]
![[Pasted image 20241114213932.png]]
Apply sigmoid function để scale $h(\theta)$ trog khoảng âm vô tận tới dương vô tận về $[0,1]$.

Chuyển convex function (khó đạt đc convergence) về convex function

### What is Hinge Loss ?
SVM (Supervised Vector Machine)
![[Pasted image 20241114215153.png]]

