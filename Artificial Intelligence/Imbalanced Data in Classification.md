## Data Imbalance
![[Pasted image 20250510133404.png]]
e.g. Negative have 200 while Positive only have 4 example
![[Pasted image 20250510133912.png]]

- [**Downsampling**](https://developers.google.com/machine-learning/glossary#downsampling) means Instead of taking all examples in the majority class for training, we **only take a portion of it by a factor of n** so that the data in neg & pos can balance out better. (e.g. factor of 10 is 1/10)
		+ ? Downsampling by a **factor of 10 would involve selecting a random subset of 20 neg samples out of 200 neg to match the 1 pos**, resulting in a less balanced dataset of 1 pos and 20 neg. 
	
- [**Upweighting**](https://developers.google.com/machine-learning/glossary#upweighting) means **adding an example weight to the downsampled class equal to the factor by which you downsampled**.
	+ ? Downsample by a factor of 10, the example weight should be 10.  

**Step 1: Downsample the majority class**  
+ ? Consider the original ratio of pos and neg is 1 pos label for every 200 neg label. *Downsampling by a factor of 10 help reduce the ratio to 1 pos for every 20 neg* (i.e. 5% ratio) which involve. Although the training set is still moderately imbalanced, the proportion of pos is much better than the original extremely imbalanced proportion (0.5%). 
**note:** data imbalance also information which help reduce overfitting so a bit of imbalance not always bad.  
![[Pasted image 20250510133802.png]]

**Step 2: Upweight the dowmsampled class**
+ ? After downsampling by a factor of 10, the example weight should be 10. (Yes, this might seem counterintuitive, but I'll explain why later on) added to each 
![[Pasted image 20250510140404.png]]
+ ? The term *weight* doesn't refer to mode paremeters (like w1, w2). Here, *weight* refers to example weights, which increase the importance of an individual example during training, for example weight of 10 mean the model treat the negative example 10 times as important (*when computing loss*). 
$$\text{example weight} = \text{original example weight} \times \text{downsample factor}$$

**note:** **prediction bias** is a value indicating **how far apart the average prediction is to the label average of labels in the dataset.** 
	not to be confucsed with the **bias term (b)** in ML models.  
```ad-example
**REGRESSION**
You’re predicting house prices.
- True average house price in the test set: **$300,000**
    
- Your model's average predicted price: **$270,000**
    
→ The **prediction bias = -$30,000** → your model **underpredicts on average**.
.
.
**CLASSIFICATION**
- **9000 "not spam"** emails
- **1000 "spam"** emails

After testing:
- **Actual proportion of spam**: 10%
    
- **Average model prediction for spam**: 4%
    
-> **Prediction bias** = **4% (predicted)** – **10% (actual)** = **-6% bias**
```
+ ? It **may seem couterintuitive to decrease the size of a class then increase its important.** After all, we are trying to improve the model performance on the minority class, so why upweight the majority class ? 
+ $ Because **Upweighting tends to reduce prediction bias**. That is Upweighting after Downsampling tends to reduce the delta between the average of your model's predictions and the average of your dataset's labels. 
```ad-seealso
You might also be wondering whether upweighting cancels out downsampling. Yes, to some degree. However, the combination of upweighting and downsampling enables [**mini-batches**](https://developers.google.com/machine-learning/glossary#mini-batch) to contain enough minority classes to train an effective model.

Upweighting the _minority class_ by itself is usually easier to implement than downsampling and upweighting the _majority class_. However, upweighting the minority class tends to increase prediction bias.

Downsampling the majority class brings the following benefits:

- **Faster convergence**: During training, the model sees the minority class more often, which helps the model converge faster.
- **Less disk space**: By consolidating the majority class into fewer examples with larger weights, the model uses less disk space storing those weights. This savings allows more disk space for the minority class, so the model can collect a greater number and a wider range of examples from that class.

Unfortunately, you must usually downsample the majority class manually, which can be time consuming during training experiments, particularly for very large datasets.
```

### Rebalance Ratios
**Like other hyperparameters** (e.g. weights). To determine how much you should downsample and upweight to rebalance the daaset, we **should experiment with the rebalancing ratio**. That said, the answers ultimately **depend on the following factors**: 
+ The **batch size**
+ The **imabalance ratio**
+ The **number of examples in the training set**. 
Ideally each batch should tain multiple minority class examples. Batches **don't contain sufficient minority classes will perform poorly**. The **batch size should at least larger then the imbalance ratio**. For example, if the imbalance ratio is 100:1, then the batch size should be at least 500. 

Note: xác định cấu trúc của phần tự giải thích để tránh mất thời gian note vs giải thích lại. 

## Method to handle Data Imbalancing
### Undersampling
>Decrease Majority class data size to balance out the size of 2 class. 
![[Pasted image 20250511151244.png]]

### Oversampling
**Random Oversampling** 
-> Re-Sample the Minority class data with their own data. e.g. re-select example from Minority class until both class balance out.  

**SMOTE**
![[Pasted image 20250511151528.png]]

**How it work ?** 
 
Entire History of Coputer Vision 



---

## Visualize Data Imbalancing

Say you have threshold probability called classification threshold where:
+ **Positive Class:** Examples with probability above the threshold value.
+ **Negative class:** Examples with lower probability value than the threshold.

### Confusion Matrix
![[Pasted image 20241126104924.png]]
+ TP: ví dụ đúng và mình phân loại nó là đúng
+ TN: ví dụ sai và mình phân loại nó là sai 
+ FP: ví dụ sai nhưng mình phân loại nó là đúng
+ FN: ví dụ đúng nhưng mình phân loại nó là sai

### Precision, Recal (TPR), FPR, Accuracy 
![[Pasted image 20241125162426.png]]
Note: all use case (&) are spam email classification

**Accuracy:** Out of all guesses, how many them are correctly guess.
 $$\text{Accuracy} = \frac{\text{total correct prediction}}{\text{total predicton}} = \frac{TP + TN}{TP + TN + FP + FN}$$


**Recall or True Positive Rate (TPR):** Out of all true positive out there, how many of them has your model correctly guess. (Trên tổng số đáp án đúng bao nhiêu trong số đó bạn phân loại là đúng)
$$\text{Recall (or TPR)} = \frac{\text{correctly classified actual positive}}{\text{all actual positive}}
= \frac{TP}{TP+FN}$$

+ ? False Negatives are actual Positive but classified as Negatives hence why they appear in the denominator.
+ & **Recall** measure the fraction of *spam email* that were correctly *classifed as spam* which is why recall another name is **probability of detection.** (out of all that can be detect, how many of them you've detected)


**False Positive Rate (FPR):** Out of all true negative out there, how many of them has your model *classified incorrectly* as positive. (Trên tổng số đáp án sai bao nhiêu đáp án sai bạn phân loại là đúng) 
$$\text{FPR} = \frac{\text{incorrectly classified actual negative}}{\text{all actual negative}}
= \frac{FP}{TN+FP}$$

+ ?  False Positives are actual Negative but classified as Positive hence why they appear in the denominator. 
+ & **FPR** measures the fraction of *legitimate email* that were classified as *spam* thus FPR is also know as **probability of false alarm**.


**Precision:** Out of all classified as true how many of them were actually true.
$$Precision = \frac{\text{correcly classificed actualy postives}}{\text{everything classified as positive}}= \frac{TP}{TP + FP}$$


+ $ Precision improves as false positives decrease, while recall improves when false negatives decrease. But as seen in the previous section, increasing the classification threshold tends to decrease the number of false positives and increase the number of false negatives, while decreasing the threshold has the opposite effects. As a result, precision and recall often show an inverse relationship, where improving one of them worsens the other.
+ 

note: threshold start from left to right (low to high)
+ $ By adjusting the threshold seperate 2 side above we see that:
	The Lower (lefter) the threshold is,  accuracy increase (Low FN) but recall decrease (Low TP). 
	The Higher (righter) the threshold is, accuracy decrease (High FN) but recall increase (High TP)

---

# Use Case
**Usecase for Seperate Data, we observe**
+ @ **Overview:** by adjusting the threshold you can increase precision or recall base on your needs. Example for real-time task like self-driving cars you prefers decrease threshold for higher recall, for accuracy demanding task like Attendance system you increase threshold for higher precision.  

+ $ **Threshold Decrease** $\to$ True/False Positive Increase (Accept More Incorrect/FP as Correct/P) $\to$ **Favour Recall**: increase overall true prediction at the cost of accepting more false predictions. **(muốn dự đoán đúng nhiều hơn thì phải chấp nhận sai nhiều hơn)**
+  Analogy: Risky Child (Favouring Recall)
+ & **Use Case:** Automated Car accept to observe *light pole or potential lightsource* as human (False Positive) to avoid potential accident. The same for predicting potential cancer patient. 
	![[Pasted image 20241222134510.png]]

+ $ **Threshold Increase** $\to$ True/False Negative Increase (Accept More Correct as Incorrect) $\to$ **Favour Precision**: Increase overall precision at the cost of having less correct predictions **(muốn dự đoán chính xác hơn thì phải chấp nhận số dự đoán đúng ít hơn)** 
+ Analogy: Cautious Child  (Favouring Precision)
+ & **Use Case:** Wine factory automate wine with ~99.99% favour in condition and handcraft wine with less favour to ensure quality of wine.  
![[Pasted image 20241125163957.png]]
![[Pasted image 20241125164503.png]]

# Classification ROC and AUC 
## Receiver-operating characteristic curve (ROC)
+ $ **ROC curve** is a visual representation of model performance across all threshold. 
	(the closer to (0,1) ~ ATPR the better )
+ ? The ROC curve is drawn by calculating the true positive rate (TPR) and false positive rate (FPR) at every possible threshold (in practice, at selected intervals), then graphing TPR over FPR
	![[Pasted image 20241126113906.png]]

## Area under the curve (AUC)
 + $ **Area under the ROC curve (AUC)** represent the probability that the model, if given a randomly chosen positive and negative example, will rank the positive higher than the negative..


+ @ AUC and ROC work well for **comparing models when the dataset is roughly balanced between classes**

### Precision-Recall curve
> When the **dataset is imbalanced, PRCsand** and the area under those curves may **offer a better comparative visualization of model performance**.
![[Pasted image 20241126114408.png]]


### AUC and ROC for choosing model and threshold
>AUC is a useful measure for comparing the performance of two different models, as long as the dataset is roughly balanced. The model with greater area under the curve is generally the better one.
![[Pasted image 20241126113558.png]]
>The curve on the right with a greater AUC, represents the better of the two models 

![[Pasted image 20241126115501.png]]
> Plot Overview: We see a fast rise in TPR as FPR go forward, indicate FP are cheap trading for TP, we able to choose threshold at C to achieve high accracy at lower FPR. 
> If TPR and FPR are roughtly balance then B is the best choice. And if TPR increase slow while FPR forward fast, A might be the best choice.

### Use Case: Accurary and Recall Tradeoff and AUC
![[Pasted image 20241126120700.png]]
![[Pasted image 20241126120708.png]]


![[Pasted image 20241126120857.png]]
![[Pasted image 20241126120901.png]]

### Other Use Case
>The more TPR we get for less FPR the better the Model perform. 
 
**Low Performance Models**
![[Pasted image 20241126121059.png]]

**High Performance Model** 
![[Pasted image 20241126121113.png]]


![[Conceptual-explanation-of-average-precision-AP-calculated-using-reference-and-predicted.png]]



