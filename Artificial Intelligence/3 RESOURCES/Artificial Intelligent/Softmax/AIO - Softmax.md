note:
+ Hadamard devision (Element-Wise product)
+ Softmax is like logisitc regression
+ $k$-th mean element at position $k$. The same for other letter $a,b,c,d,i,j,etc\dots$ 
+ [[Why Do Neural Network love Softmax]]
+ [Sigmoid vs Softmax](https://towardsdatascience.com/sigmoid-and-softmax-functions-in-5-minutes-f516c80ea1f9) (Sigmoid is for 1 class, Softmax is for multi-class)

# Softmax Regression
> Giống Logistic Regression nhưng để phân loại nhiều lớp/đặc trưng (multiple class). Vd trong Logistic Regression nếu z=3 có xs là 0.88 thì TH còn lại là z=1 sẽ là 0.12, vậy tổng các xs là 1 đối vs 2 TH. Với Softmax, nếu có n TH thì tổng xs của n TH là 1 như vd ở dưới:     
![[Pasted image 20241106050754.png]]
  Công thức
![[Pasted image 20241106051757.png]]

**One-hot encoding** (Use for Matrix Multiplication)
![[Pasted image 20241105210031.png]]
>index = 0 -> y tại vị trí 0 bằng 1
>index = 1 -> y tại vị trí 1 bằng 0


>The softmax function, often used in the final layer of a classification NN model for classification tasks, **converts raw output scores - also known as logits - into probabilities by taking the exponential of each output and normalizing these values by dividing by the sum of all the exponentials**.
![[images 1.png]]

### Softmax Loss function Intuition
**Goal:** classifiying multiple class using Cross-Entropy loss. 
	$\arg \max_{\theta}(L(\theta))$ $\to \arg \max_{\theta}$ symbol basically mean find $\theta$ so that $L(\theta)$ is maximize.

**Given:** 
A data set with $\mathbb{N}$ independent samples
Each sample $x^{(i)}$ has a **true class label** $y^{(i)}$ which can be one of $k$ possible classes (e.g. class 1, 2, 3, 4, etc...)
note:
+ **true class label** can be called "**class** in general context" and "**label** in ML context" in short. And label it is for our case: 
+ $x^{(i)}$ is the feature vector (input) corresponding to the $i$-th example in your dataset.

**true label** mean only 1 label is true out of all labels. 
+ So $y_{1}=1$ meaning that class 1 is the correct class
+ Thus $y_{2}=0, y_{3}=0, y_{4}=0$ are not the correct class.
In mathematical terms, we **encode the true label** $y$ as **one-hot** vector $[y_{1}, y_{2}, y_{3}, y_{4}]$ where **exactly one of the entries is 1** (indicate the correct class), and **the rest are 0**.


Say for 4 label y = { 1, 2, 3, 4 }. 
>We know the probs of each label can be calc using Softmax: ![[Pasted image 20241106060300.png]]
   In logistic regression, we use Bernoulli Distribution
![[Pasted image 20241106060334.png]]
>In Softmax, to classified multiple class, we use Join Probability ([[Product of Multiple Independent Events]]) **for Y label is independent and for the sake of matrix/vector multiplication with [[one-hot encoding]] applied later**)
>![[Pasted image 20241106060500.png]] 
+ ? **Example:**
>= $a_{1}^{y_1^{(i)}}.a_{1}^{y_2^{(i)}}.a_{1}^{y_3^{(i)}}.a_{1}^{y_4^{(i)}}$ 
>Because , there is only 1 true label Y in each sample X. So if $P(Y=1|X)$ is true, then all others probability are False: 
>= $a_{1}^1.a_{2}^0.a_{3}^{0}.a_{4}^{0}$ 
>= $a_{1}$. c
+ $ **Simplify Equation using product sign** $P(Y|X) = \prod^{c}_{k=1}P(y=c|x)$ 
	this represent prob of Y to happened given sample X.

Note: $\theta$ represent Neural Network weight
$P(Y|X)$ can be rewrite as $h_{\theta}(X)$  $$\prod^{c}_{k=1}h_{\theta}(X)_{k}^{y^{(i)}}$$where $h_{\theta}$ is the probability of $h$ to happend given input $X$ and weights $\theta$ with $c$ represent total number of label and $k$ represent $h_{\theta}(x)$ index (i.e. label index). Finally $y^{(i)}$ equal 0 or 1 represent the plausibility of $h$ (khả năng xảy ra của $h$). Also yes, $y^{(i)}$ can be use to represent one-hot encoding vector.

Note:
+ [[IID]] mean Independent and Identically Distributed: độc lập và ko phân phối
+ Homogenous (đồng biến) basically mean all function's variable change together. Example for $\lambda$ as the scaling factor, the whole funcion will be scale (that it) $$f(λx,λy)=λx+λy=λ(x+y)=λf(x,y).$$ 
Same as above, for the whole dataset for m IID datapoints: $(x^{(1)}, y^{(1)}), \dots, (x^{(m)}, y^{(n)})$ we got the product of all prob:
$$P(Y|X)=P(Y^{(1)}|X^{(1)}),\dots, P(Y^{(m)}|X^{n)}) = \prod^{m}_{i=1}P(Y^{(i)}|X^{(i)})$$
Simplified the fomula we got Softmax Likelihood Function:
$$\prod^{m}_{i=1}\prod^{c}_{k=1}h_{\theta}(X^{(i)})_{k} ^{y^{(i)}_{k}}$$
Like likelihood function in Logistic Regression, the **prob will get infinitely small and close to zero** as they multiply, so we need to **[[convert softmax log likelihood into sum of probability]]** using these logarithm rule to maximize it:
+ Log Product Rule: $\log_b(MN) = \log_b(M) + \log_b(N)$
+ Natural Log: $e^{\ln x} = x$
+ Log Power Rule: $\log_b(M^k) = k \cdot \log_b(M)$ 
$$-\sum^{m}_{i=1}\sum^{c}_{k=1} (y^{(i)} _{k}) \log(h_{\theta}(X^{(i)})_{k})$$
The function now become **Maximum Log Likelihood** because log function is [[homogenous]] (đồng biến) so $arg_{\theta} \max(L(\theta)) = arg_{\theta} \max(LL(\theta))$, this mean when the Loss function is maximize then Log Likelihood is also maximize) 

(note: 
+ $LL$ mean Loglikelihood, $L$ mean Loss
+ Other benefit of using log is easier derivative.
+ $k$-th represent element index so don't mind it much. If 2 element have k-th that mean they calc at the same time at k element.

In the previous part, we understand that $y^{(i)}$ represent a single label in $k$-th of $h_{\theta}(X^{(i)})_{k}$. So
+ ? For each sample $x^{(i)}$, the model outputs a vector of probabilities for each class, calculated using the softmax function: 
$$
\hat{y}^{(i)} = [P(y = 1 | x^{(i)}), P(y = 2 | x^{(i)}), \dots, P(y = C | x^{(i)})]
$$

+ ? The true label for each sample $y^{(i)}$ is encoded as a one-hot vector:
$$
y^{(i)} = [y_1^{(i)}, y_2^{(i)}, \dots, y_C^{(i)}]
$$

+ ? where $y_j^{(i)} = 1$ if $j$ is the true class, and $y_j^{(i)} = 0$ otherwise.

+ $ Rewrite the expression with $y^{(i)}$ as one-hot encoding vector we got:
$$-\sum^{m}_{i=1}y^{(i)}\log(h_{\theta}(X^{(i)}))$$

For multiple samples where $X$ and $y$ are both Matrix (which represent all of it elements), the Loss Log likelihood function can be:   
$$L = -\frac{1}{N}trace(Y^T\log(\hat{Y}))$$
where:
+ $Y$ is the $N$ x $C$ matrix of one-hot encoded true lables for all samples
+ $\hat{Y}$ is the $N$ x $C$ matrix of predicted probabilities for all classes for each sample.
+ $\log(\hat{Y})$ applies the logarithm element-wise to each entry in $\hat{Y}$.
+ [[trace]]: $trace(A)$ is the **sum of the elements along the main diagnol** (from top left to bottom right) **of matrix (A).** Say after matrix multiplication, $Y^T\log(\hat{Y})$ become matrix A.  
	+ ? **Each element along the diagonal** of the matrix $Y^T \log(\hat{Y})$ **corresponds to the loss for each individual sample in the dataset**, based on the true class and predicted probability for that class. Using the **trace function effectively sums these diagonal elements, giving the total loss across all samples**. By **dividing by $N$ (the number of samples), we obtain the average loss across the dataset.**

This approach is efficient because it leverages matrix operations to compute the sum of losses, making it ideal for handling large datasets in a vectorized form.

---
# AIO2024: Softmax

Nhiều tham số hơn (more parameters) thì có tiềm năng làm đc nhiều thứ hơn. Basically more data

What about a explicit task (1 việc riêng biệt) ?
>Có 2 loại phân loại nhị phân. Phân loại có 2 nodes output tốt hơn.
![[Pasted image 20241106201852.png]]
+ ? Tại sao ko dùng sigmoid, vì tổng của 2 nodes sẽ ko bằng 1 do nếu có 2 nodes sigmoid sẽ sinh ra xs cho cả 2 nodes.

Xuất phát từ tính giá trị xác suất $Z_{0}, Z_{1}$, thay tham số z.  
Nếu chọn 1 số bất kì thì chọn số tiêu biểu nhất, vd là $e^{z_{0}}$ vì với $z_{0} \in (- \infty, \infty)$ e sẽ ko âm. 
![[Pasted image 20241106202900.png]]

trừ đi m để chống số mũ quá bé. và e ~ 0
![[Pasted image 20241106203137.png]]

Thay y đối vs TH y=0 và y=1 vào loss function $L(\theta)$.  
+ y = 0 -> $-log(\hat{y}_{0})$ 
+ y = 1 -> $-\log(\hat{y}_{1})$
+ ? Do 2 bộ tham số độc lập nên xs cũng độc lập. Để y=1 và y=0 có khả năng xảy ra ta sẽ muốn xs của cả y=1, y=0 đều tiến gần 1.  (Khác với logistic regression là nếu 1 tham số xs tăng thì tham số còn lại sẽ giảm)
![[Pasted image 20241106203633.png]]
(note: chỉnh sửa hàm binary cross-entropy sẽ ra hàm loss trên)

**1-D features and 3 Class**
+ ? Output phụ thuộc vào số class y (label) ko phụ thuộc vào số input x.
![[Pasted image 20241106204646.png]]
+ ? mô hình trên có 6 tham số. Vì có 2 input vs 3 nodes.
![[Pasted image 20241106214447.png]]
+ ? mô hình trên có 15 tham số. Vì có 5 inputs và 3 nodes. 

theta viết dạng hàng, còn biến của $\theta$ viết dưới dạng cột. 
![[Pasted image 20241106205656.png]]
viết lại nhân ma trận của Z
![[Pasted image 20241106205903.png]]
thay $\theta$ ta có thể viết lại Z bằng:
![[Pasted image 20241106205957.png]]
Similiar for $\hat{y}$
![[Pasted image 20241106210245.png]]
(XEM LẠI CÁCH THETA ĐC BIỂU DIỄN)
+ check lại b của từng lớp lưu trong list ntn 

With one-hot encoding, loss function follow y:
+ y = 0 -> $-log(\hat{y}_{0})$ 
+ y = 1 -> $-\log(\hat{y}_{1})$
![[Pasted image 20241106211524.png]]
The loss function become:
![[Pasted image 20241106211739.png]]


![[Pasted image 20241106212526.png]]![[Pasted image 20241106212710.png]]

![[Pasted image 20241106213013.png]]
Cho NN 2 nodes, do L phụ thuộc vào 2 nodes y0 và y1 nên tính chain rule của tổng 2 nodes.
![[Pasted image 20241106212909.png]]
![[Pasted image 20241106213130.png]]
(The fomular remain for more categories/label)

maximize z0 if y0 is true.
Với mong muốn y=0 và mong muốn Loss giảm nghĩa là mình sẽ muốn giá trị xác suất của a0 tăng (z0 tăng) và a1 giảm (z1 giảm). (Vì mô hình quyết định a nào có xs cao hơn thì lấy) <-> a0 > a1
![[Pasted image 20241106220357.png]]
Example for increasing a0:
![[Pasted image 20241106220718.png]]
Example for decreasing a1 (remember that $\hat{y}_{j}=a_{j}$):
![[Pasted image 20241106220808.png]]

If we want y0 is true then
![[Pasted image 20241106221207.png]]

idea start from here then replace [0,0,0,1,1,1] with y and  [0,1,2,3,4,5] with range(N)
```python
y_hot[[0,1,2,3,4,5], [0,0,0,1,1,1]] = 1
# basically
y_hot[[0], [0]] = 1
y_hot[0, 0] = 1
```




