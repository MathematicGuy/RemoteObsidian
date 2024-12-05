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

+ ? False Negatives are actual Positive but classified as Negatives hence why they appear in the denominator, 
+ & **Recall** measure the fraction of *spam email* that were correctly *classifed as spam* which is why recall another name is **probability of detection.** (out of all that can be detect, how many of them you've detected)

  
**False Positive Rate (FPR):** Out of all true negative out there, how many of them has your model *classified incorrectly* as positive. (Trên tổng số đáp án sai bao nhiêu đáp án sai bạn phân loại là đúng) 
$$\text{FPR} = \frac{\text{incorrectly classified actual negative}}{\text{all actual negative}}
= \frac{FP}{TN+FP}$$

+ ?  False Positives are actual Negative but classified as Positive hence why they appear in the denominator. 
+ & **FPR** measures the fraction of *legitimate email* that were classified as *spam* thus FPR is also know as **probability of false alarm**.


**Precision:** Out of all classified as true how many of them were actually true.
$$Precision = \frac{\text{correcly classificed actualy postives}}{\text{everything classified as positive}}= \frac{TP}{TP + FP}$$


+ $ Precision improves as false positives decrease, while recall improves when false negatives decrease. But as seen in the previous section, increasing the classification threshold tends to decrease the number of false positives and increase the number of false negatives, while decreasing the threshold has the opposite effects. As a result, precision and recall often show an inverse relationship, where improving one of them worsens the other.


note: threshold start from left to right (low to high)
+ $ By adjusting the threshold seperate 2 side above we see that:
	The Lower (lefter) the threshold is,  accuracy increase (Low FN) but recall decrease (Low TP). 
	The Higher (righter) the threshold is, accuracy decrease (High FN) but recall increase (High TP)

---

# Use Case
**Usecase for Seperate Data, we observe**
+ @ **Overview:** by adjusting the threshold you can increase precision or recall base on your needs. Example for real-time task like self-driving cars you prefers decrease threshold for higher recall, for accuracy demanding task like Attendance system you increase threshold for higher precision.  

+ $ **Threshold Decrease** $\to$ True/False Positive Increase (Accept More Incorrect/FP as Correct/P) $\to$ **Favour Recall**: increase overall true prediction at the cost of accepting more false predictions. (muốn dự đoán đúng nhiều hơn thì phải chấp nhận sai nhiều hơn)
+  Analogy: Risky Child (Favouring Recall)
+ & **Use Case:** Automated Car accept to observe light pole as human (False Positive) to avoid potential accident. The same for predicting potential cancer patient. 


+ $ **Threshold Increase** $\to$ True/False Negative Increase (Accept More Correct as Incorrect) $\to$ **Favour Precision**: Increase overall precision at the cost of having less correct predictions (muốn dự đoán chính xác hơn thì phải chấp nhận số dự đoán đúng ít hơn) 
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