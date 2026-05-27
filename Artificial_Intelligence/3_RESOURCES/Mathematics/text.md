### Trực giác về hàm Softmax Loss
**Mục tiêu:** phân loại nhiều lớp bằng Cross-Entropy loss. 
	$\arg \max_{\theta}(L(\theta))$ $\to \arg \max_{\theta}$ có nghĩa là tìm $\theta$ sao cho $L(\theta)$ đạt giá trị lớn nhất.


**Cho trước:** 
Một tập dữ liệu với $\mathbb{N}$ mẫu độc lập
Mỗi mẫu $x^{(i)}$ có **true class label** $y^{(i)}$, có thể thuộc một trong $k$ lớp (ví dụ lớp 1, 2, 3, 4, v.v.)
Lưu ý:
+ **true class label** có thể được gọi là "**class** trong ngữ cảnh chung" và "**label** trong ngữ cảnh ML" cho ngắn gọn. Và label trong trường hợp của chúng ta là:
+ $x^{(i)}$ là vector đặc trưng (đầu vào) tương ứng với ví dụ thứ $i$ trong tập dữ liệu.

**true label** có nghĩa là chỉ có một label là đúng trong tất cả các label.
+ Ví dụ $y_{1}=1$ nghĩa là lớp 1 là lớp chính xác
+ Do đó $y_{2}=0, y_{3}=0, y_{4}=0$ không phải là lớp chính xác.

Về mặt toán học, chúng ta **mã hóa true label** $y$ dưới dạng **vector one-hot** $[y_{1}, y_{2}, y_{3}, y_{4}]$, trong đó **chính xác một phần tử duy nhất là 1** (chỉ ra lớp chính xác), và **mọi phần tử khác là 0**.


Giả sử có 4 label y = { 1, 2, 3, 4 }. 
>Chúng ta biết xác suất của mỗi label có thể tính bằng Softmax: ![[Pasted image 20241106060300.png]]
>Trong logistic regression, chúng ta sử dụng Bernoulli Distribution
![[Pasted image 20241106060334.png]]
>Vì các y là **true label (biến độc lập)** trong tập X nên chúng ta sử dụng Join Probability 
>([[Product of Multiple Independent Events]]) để tính xác suất 
>![[Pasted image 20241106060500.png]] 
+ ? **Ví dụ:**
>= $a_{1}^{y_1^{(i)}}.a_{1}^{y_2^{(i)}}.a_{1}^{y_3^{(i)}}.a_{1}^{y_4^{(i)}}$ 
>Vì chỉ có một true label Y trong mỗi sample X. Do đó nếu $P(Y=1|X)$ là đúng thì tất cả các xác suất khác là Sai:
>= $a_{1}^1.a_{2}^0.a_{3}^{0}.a_{4}^{0}$ 
>= $a_{1}$. 
+ $ **Đơn giản hóa phương trình bằng ký hiệu tích** $P(Y|X) = \prod^{c}_{k=1}P(y=c|x)$ 
	Thể hiện xác suất của Y xảy ra với điều kiện đã cho là sample X.

$P(y=c|x)=p^{y}(1-p)^{1-y}$

Lưu ý: $\theta$ biểu thị trọng số của Neural Network
$P(y=c|x)$ có thể được viết lại thành $h_{\theta}(X)$, ta có $P(Y|X)$ mới là: $$P(Y|X) = \prod^{c}_{k=1}h_{\theta}(X)_{k}^{y^{(i)}}$$
Trong đó $h_{\theta}$ là xác suất của $h$ xảy ra với đầu vào $X$ và trọng số $\theta$ với $c$ là tổng số label và $k$ là thứ tự của $h_{\theta}(x)$ (tức là thứ tự của label). Cuối cùng $y^{(i)}$ bằng 0 hoặc 1 đại diện cho khả năng xảy ra của $h$. Ta thấy, $y^{(i)}$ có thể được sử dụng để biểu thị one-hot encoded vector.


Lưu ý:
+ IID nghĩa là Independent and Identically Distributed: độc lập và ko phân phối)
+ Homogenous (đồng biến) về cơ bản có nghĩa là tất cả các biến của hàm thay đổi cùng nhau. Ví dụ với $\lambda$ là hệ số tỷ lệ, toàn bộ hàm sẽ được tỷ lệ (chỉ là vậy) $$f(λx,λy)=λx+λy=λ(x+y)=λf(x,y).$$
Tương tự với dữ liệu với m điểm dữ liệu IID: $(x^{(1)}, y^{(1)}), \dots, (x^{(m)}, y^{(n)})$ ta có tích của tất cả các xác suất:
$$P(Y|X)=P(Y^{(1)}|X^{(1)}),\dots, P(Y^{(m)}|X^{n)}) = \prod^{m}_{i=1}P(Y^{(i)}|X^{(i)})$$
Đơn giản hóa công thức ta có hàm Softmax Likelihood:
$$\prod^{m}_{i=1}\prod^{c}_{k=1}h_{\theta}(X^{(i)})_{k} ^{y^{(i)}_{k}}$$
Như hàm likelihood trong Logistic Regression, **xác suất sẽ trở nên cực kỳ nhỏ và gần bằng không** khi chúng nhân với nhau, do đó chúng ta cần chuyển đổi tích thành tổng sử dụng tính chất của hàm log:
+ Log Product Rule: $\log_b(MN) = \log_b(M) + \log_b(N)$
+ Log Tự nhiên: $e^{\ln x} = x$
+ Log Power Rule: $\log_b(M^k) = k \cdot \log_b(M)$ 
$$-\sum^{m}_{i=1}\sum^{c}_{k=1} (y^{(i)} _{k}) \log(h_{\theta}(X^{(i)})_{k})$$
Hàm này bây giờ trở thành **Maximum Log Likelihood** bởi vì log function là đồng biến nên $arg_{\theta} \max(L(\theta)) = arg_{\theta} \max(LL(\theta))$, điều này có nghĩa là khi Loss function đạt giá trị tối đa thì Log Likelihood cũng đạt giá trị tối đa)

(Lưu ý: 
+ $LL$ có nghĩa là Loglikelihood, $L$ có nghĩa là Loss
+ Một lợi ích khác của việc sử dụng log là dễ dàng tìm đạo hàm hơn.
+ $k$-th là thứ tự phần tử. Nếu có 2 phần tử có k-th nghĩa là chúng được tính đồng thời tại phần tử k.

Trong phần trước, chúng ta hiểu rằng $y^{(i)}$ đại diện cho label thứ $k$ của $h_{\theta}(X^{(i)})_{k}$. 
+ ? Với mỗi sample $x^{(i)}$, mô hình sẽ xuất ra một vector xác suất cho mỗi lớp, được tính bằng hàm softmax: 
$$
\hat{y}^{(i)} = h_{\theta}(X^{(i)}) = [P(y = 1 | x^{(i)}), P(y = 2 | x^{(i)}), \dots, P(y = C | x^{(i)})]
$$

+ ? True label của mỗi sample $y^{(i)}$ được mã hóa thành một one-hot vector:
$$
y^{(i)} = [y_1^{(i)}, y_2^{(i)}, \dots, y_C^{(i)}]
$$

+ ? Trong đó $y_j^{(i)} = 1$ nếu $j$ là lớp chính xác và $y_j^{(i)} = 0$ trong trường hợp khác.

+ $ Viết lại biểu thức với $y^{(i)}$ như một one-hot encoding vector, ta có:
$$-\sum^{m}_{i=1}y^{(i)}\log(\hat{y}^{()})$$

Với nhiều sample, trong đó $X$ và $y$ đều là ma trận (đại diện cho tất cả các sample), hàm Loss Log likelihood có thể được viết:   
$$L = -\frac{1}{N}trace(Y^T\log(\hat{Y}))$$
Trong đó:
+ $Y$ là ma trận $N$ x $C$ chứa các one-hot encoded true label cho tất cả các sample
+ $\hat{Y}$ là ma trận $N$ x $C$ chứa xác suất dự đoán cho tất cả các lớp cho mỗi sample.
+ $\log(\hat{Y})$ áp dụng logarit từng phần tử của $\hat{Y}$.
+ [[trace]]: $trace(A)$ là **tổng của các phần tử trên đường chéo chính** (từ trên trái xuống dưới phải) **của ma trận (A).** Giả sử sau khi nhân ma trận, $Y^T\log(\hat{Y})$ trở thành ma trận A. 
	+ ? **Mỗi phần tử trên đường chéo** của ma trận $Y^T \log(\hat{Y})$ **tương ứng với mất mát cho mỗi sample riêng lẻ trong tập dữ liệu**, dựa trên true class và xác suất dự đoán cho lớp đó. Sử dụng **trace function

 để tính tổng các phần tử đường chéo này, cho tổng mất mát của tất cả các sample**. Bằng cách **chia cho $N$ (số lượng sample), chúng ta thu được mất mát trung bình trên toàn bộ tập dữ liệu.**


Phương pháp này hiệu quả vì nó tận dụng các phép toán ma trận để tính tổng mất mát, làm cho nó lý tưởng để xử lý các tập dữ liệu lớn dưới dạng vector.