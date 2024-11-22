## Introduction to Classification Loss
x, y: input, output tương ứng.

## Zero-One Loss Function
![[Pasted image 20241121113724.png]]
Điểm yếu: kể cả khi giá trị dương xấp xỉ 0 thì loss cũng là 1.

## Exponential Loss Function
(trong bài AdaBoost + Decision Tree)
note: Hinge Loss sử dụng trong SVM
![[Pasted image 20241121114018.png]]
+ ! **Limitation:** Exponential Loss penelize outlier/error heavily.
	Ex: Model focus on fitting to the outlier (that 1 red dot) too much, it causes overfitting.	![[Pasted image 20241121114817.png]]
+ $ Solution: Hinge Loss


## Introduction to KL Divergence
> **Kullback-Leibler divergence** metric (relative entropy) is a **statistical measurement** from information theory that is commonly used to **quantify the difference between one probability distribution from a reference probability distribution**.

Chứng minh KL Divergence ở góc nhìn Entropy, Cross-Entropy
![[Pasted image 20241121161628.png]]
+ ? Trong các bài toán Machine Learning/Deep Learning, do Entropy(P) là không đổi (P là phân phối target -> không đổi) nên tối ưu hàm KL_Divergence cũng tương đương với tối ưu hàm CrossEntropy. Nói các khác, việc bạn dùng KL_Divergence hay CrossEntropy trong Machine Learning là như nhau (trong các lĩnh vực khác thì không). 
+ $ Minimising the KL is equivalent to doing maximum likelihood in most circumstances


note: lý do vì sau sd hàm loss KL Divergence cho GAN, Autoencoder, Variation Autoencoder.
![[Pasted image 20241121115152.png]]
+ $ Main Idea: Tính khoảng cách giữa 2 Distributions.  
>Distance càng gần thì càng chính xác

[KL Divergence Explain](https://www.youtube.com/watch?v=q0AkK8aYbLY&t=5s)
**Vì sao lại dùng KL-Divergence ?**
note: symmetric or asymmetric (đối xứng và bất đối xứng)
symmetric example: $|100 - 105| = 5$, $|105 - 100| = 5$ (đối xứng qua 5) - asymmetric if remove the absolute sign. 

Asymmetric Example 2:
Chia tỷ lê y_2023 vs y_2024.
![[Pasted image 20241121120214.png]]
 Nếu chia ngược y2024 cho y2023, ta thấy rằng Step 2 = 4 và Step 3 = 1/4 nhưng average loss ko thay đổi.

**Giả Thuyết:** nếu P(36-50) năm 2023 lả 2 thì P/Q=2/4 còn Q/P là 2.
**Vấn đề:** bất đối xứng có thể xuất hiện khi chia ngược lại. (quay lại vs 4, 1/4)
![[Pasted image 20241121121045.png]]
**Giải Pháp:** sử dụng Log 
![[Pasted image 20241121121214.png]]
**Giải Thích Lý Do:** Because [[Log Symmetric Property]] 
$$f(a) = \log(a), \quad f\left(\frac{1}{a}\right) = -\log(a)$$
![[Pasted image 20241121143635.png]]
Trong phân phối xác suất, ta chuyển $\frac{1}{n}$  sang $P(x)$
![[Pasted image 20241121144250.png]]



## Binary Classification Loss
Nếu hằng số ko phải $\theta$ sẽ bỏ, chỉ quan tâm đến tham số giúp đạt tới giá trị cực tiểu.
![[Pasted image 20241114211933.png]]
Cross-Entropy: so sánh 2 distributions
Entropy: tính distribution của chính nó


## Hinge Classification Loss
![[Pasted image 20241121171122.png]]
where:
- y is the true label (+1 or -1).
- f(x) is the predicted output (before applying the decision threshold).
>If > 1 then 0, If < 1, loss increase linearly.


Review SVM: The goal of SVM is not only to find a hyperplane that separates the two classes but to find an optimal hyperplane. 
![[Pasted image 20241121170550.png]]
+ $ Hinge Loss helps keep data from different classes at a safe distance. (Use in SVM)

**Manual Calc**
>Ex 1: blue dot in the right class ![[Pasted image 20241121170928.png]]

>Ex 2: blue dot in the wrong class (red class)![[Pasted image 20241121171555.png]]
>Loss is high.

>Ex 3: blue dot in the middle ![[Pasted image 20241121171639.png]]

```ad-success
**Maximizes the Margin:**

    Encourages a large margin between classes, leading to better generalization.

**Robust to Outliers:**

    Does not penalize examples that are correctly classified with a margin greater than 1, reducing sensitivity to noisy data.

**Efficient for Binary Classification:**

    Tailored for binary classification tasks, ensuring simplicity and relevance for SVMs.

**Mathematically Well-Defined:**

    Convex nature of hinge loss allows efficient optimization using gradient-based methods like SGD.
```

```ad-caution

**Not Probabilistic:** 

	Does not produce probabilities or calibrated outputs directly, which limits interpretability in some scenarios.

**Sensitive to Imbalanced Data:**

	Performance may degrade if the dataset has a significant class imbalance unless additional techniques are applied.
    
**Limited to Binary Classification:**

	Requires extension (e.g., one-vs-all or multi-class SVM) to handle multi-class problems, which increases complexity.
    
**Margin Bias:**

	Focuses on maximizing the margin, which might overlook some critical misclassifications if they lie close to the margin boundary.
```

## Binary Cross vs Cross-Entropy Loss
![[Pasted image 20241121171924.png]]

## Sparse Categorical Cross-Entropy


## Label Smoothing

**Why Label Smoothing ?**
> Cross-Entropy Loss is often effective in ideal cases
+ The number of samples for each class is balanced.
+ The features between classes have clear distinctions.

![[Pasted image 20241122093456.png]]


Example: Image Colorization task. One commond approaches is to treat **color prediction** for **each pixel** as **classification** problem.  
![[Pasted image 20241122092831.png]]

Fomula for Label Smoothing
![[Pasted image 20241122094059.png]]
**where** 
+ **C** is number of class 
+ $y_{true}$: One-hot encoded true label
+ $\alpha$: label smoothing parameter (e.g. $\alpha=0.001$)
![[Pasted image 20241122094938.png]]

```ad-example
Suppose:
+ Number of classes C=3.

+ True label Y: Class 1 (one-hot encoded as [1,0,0])

+ $\alpha=0.1$.

Smoothed labels:
$$ysmooth=[0.9,0.05,0.05]$$
```


+ $ **Benefits**
	
	**Regularization:** Acts as a form of regularization, improving model robustness.
	
	**Reduced Overfitting:** Models are less likely to memorize noisy or incorrect labels.
	
	**Better Gradient Behavior:** Encourages smoother gradient updates during training.

+ ? When to Use:
	
	When training on noisy datasets.
	
	For tasks requiring high generalization, like large-scale image classification.
	
	In models prone to overconfidence, such as deep neural networks.

## Multi-label Classification Loss
![[Pasted image 20241122095321.png]]
Multi-Class: 1 lable, many class 
Multi-Lable: Many label, many class 
Sigmoid + BCE use for Multi-Lable problems.

### Pairwise Ranking Loss
>Suitable for tasks where the order between labels is meaningful, such as recommendation systems or multi-label ranking by relevance.
![[Pasted image 20241122100349.png]]
>Active label <-> Irrelevant label (i.e. false prediction)
![[Pasted image 20241122100246.png]]
  f_j: positive
  f_k: negative 
![[Pasted image 20241122100754.png]]

## Practical Insights and Tips
![[Pasted image 20241122100953.png]]
![[Pasted image 20241122101002.png]]

Thường dùng trong Autoencoder (Probabilistic Autoencoder) 
![[Pasted image 20241122101055.png]]
![[Pasted image 20241122101148.png]]
