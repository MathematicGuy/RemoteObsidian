![[Pasted image 20260208154157.png]]

### 1.1 SGD with Momentum
**Gradient Descent ban đầu:**
$\theta = \theta - \eta \nabla_{\theta}J(\theta)$ có $\theta$ là tham số của mô hình cần cập nhật và $\nabla_{\theta}J(\theta)$ là đạo hàm của $\theta$.

+ @ Theo góc nhìn vật lý, do learning rate cố định, GD thông thường không thể vượt qua đc các Local Minimum mọi lúc đc, trong khi đó nếu có thêm 1 lực vật lý như là Đà (momentum) thì GD có thể dễ dàng vượt lên các Local Minimum không quá dốc.   

![[Pasted image 20260208144237.png | 444]]

![[Pasted image 20260121211427.png | 444]]

Để cập nhật Gradient với Momentum ta đơn giản gộp chung phép tính đạo hàm với biến Momemtum $\gamma v_{t-1}$ lại thành 1 biến gia tốc $v_{t}:$  
$$v_{t} = \gamma v_{t-1} + \eta \nabla_{\theta}J(\theta) = \gamma v_{t-1} + \eta \nabla_{\theta}J(\theta)$$
$\gamma:$ Momentum. thường có giá trị 0.9 (ie. dùng 90% giá trị momentum), dùng để kiểm soát số % momentum dùng để tính Gradient.
$\eta:$ learning rate của đạo hàm
$v_{t-1}:$ là vận tốc tại thời điểm trước đó. $v_{t}$ là hiện tại
$\theta:$ vị trí hiện tại của hòn bi.
$\nabla J(\theta):$ "slope / đạo hàm" của điểm trước đó.
-> Ta cập nhật tham số như bình thường: $\theta = \theta - v_{t}$ (Note: Initial $v_{t}$ is set to zero).

Tuy Momentum giúp vượt qua Local Minimum để đi đến Global Minimum tốt hơn nhưng cũng chính vì Momentum mà nó mất quá nhiều Iteration để ổn định vị trí tại điểm cực tiểu chính.

![[Pasted image 20260121205747.png | 555]]

### 1.2 Nesterov accelerated gradient (NAG) - 1 hướng cải tiến 
+ $ Khắc phục vấn đề "Ổn định do Momentum gần điểm cực Tiểu", Nesterov accelerated gradient (NAG) ra đời để giúp hội tụ nhanh hơn. 
+ @ Ý tưởng chính là *dự đoán hướng đạo hàm trong tương lai 1 bước bằng cách trừ tham số $\theta$ hiện tại cho momentum $\gamma v_{t-1}$*, ta có thể xấp xỉ vị trí tiếp theo là $\theta - \gamma v_{t-1}$. Nói cách khác ta thay $\nabla(\theta)$ thành $\nabla (\theta - \gamma v_{t-1})$ vì $\theta$ đại diện cho vị trí và tham số cho đạo hàm hiện tại. 
![[Pasted image 20260121212359.png# left ]]
+ GD + Momentum: Cộng Momentum với *Gradient của điểm hiện tại.* 
+ NAG: Cộng Momentum với *Gradient dự đoán xấp xỉ trong tương lai.* 
 (Nguồn: [CS231n Stanford: Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/neural-networks-3/)) - ([Other Optimizer](https://www.ruder.io/optimizing-gradient-descent/))

Công thức gia tốc mới là:
$$v_{t} = \gamma v_{t-1} + \eta \nabla_{\theta}J(\theta - \gamma v_{t-1})$$
So sánh 2 thuật toán cho bài toán LR, ta thấy rõ NAG hội tụ nhanh hơn. 
![[Pasted image 20260121213508.png]]


### 1.3 RMSProp (t Mean Square Propagation) 
Note: $dW_{t} = \nabla W_{t}$ both mean derivative of $W_t$ but 1 is faster & easier to write and the one is more formal. 
+ ! *Vấn đề* của của "SGD + Momentum" *là Momentum của mỗi Mini-Batch* khiến hướng đi của nó bị dao động mạnh. Vấn đề là phải cập nhật nhiều hơn cần thiết. 
+ ? Vậy *có thể lấy trung bình không của 2 đạo hàm liền kề hay ko ?* (ie. $g_{t-1}$ và $g_{t}$)
+ $ Đây chính là ý tưởng của RMSProp, nó lấy gradient cũ và mới làm momentum, và chia đạo hàm hiện tại $g_{t}=\nabla_{\theta}J(\theta)$ (g for ) cho tích lũy bình phương đạo hàm (moving average):  $$v_{t}= \underbrace{\beta g_{t-1}}_{\text{gradient cũ}} + \underbrace{(1-\beta)g_{t}^2}_{\text{gradient mới}} = v_{t}= \beta \nabla W_{t-1} + (1-\beta)\nabla W_{t}^2$$ Rồi cập nhật trọng số với Tốc Độ học Thích Nghi dựa trên Đạo hàm 2 gần nhất. $$W_{t} = W_{t-1} - \frac{\alpha}{\sqrt{ v_{t} + \epsilon}}g_{t}$$
![[Pasted image 20260208144452.png | 288]]

![[Pasted image 20260208153735.png]]

+ $ *Điều chỉnh Step (cập nhật gradient) dựa vào độ lớn của các đạo hàm gần nhất*. Learning rate thích ứng với độ lớn trung bình của gradient gần đây (e.g. tốc độ thay đổi của gradient) -> *Adaptive nên Tốt trog điều kiện nhiều Nhiễu* như online learning và non-stationary problems. 
-> Handle Sparse Gradients on noisy problem
### 1.4 Adam Optimizer (Adaptive Movement Estimation algorithm)
+ @ Adam is essentially take the best of  "SGD + Momentum" and  "RMSProp". It trakes both the "speed" (momentum) and the "acceleration" (squared gradients)
	Note: $g_t = \nabla W_{t}$ and all $\beta$ are hyperparams, the  $\hat{}$  sign in math represent an **estimated, predicted, or special modified version** of that variable.  ![[Pasted image 20260208163637.png]]

**Step 1:** Calculate 2 Moving Average (2 mometum)
1. $m_{t}$ (1st Moment - Momentum): Average of gradients (like SGD with Momentum)
$$m_{t} = \beta_{1}m_{t-1} + (1-\beta_{1})g_{t}$$
2. $v_{t}$ (2nd Moment - Scaling): Average of squared gradients (like RMSProp)
$$v_{t} = \beta_{2}v_{t-1} + (1-\beta_{2})g_{t}^2$$

**Step 2: Bias Correction**
Since $m_{t}$ and $v_{t}$ start at 0, they are biased toward 0 at the beginnning of training. We correct this:
$$\hat{m_{t}}=\frac{m_{t}}{1-\beta_{1}^{t}} \space , \space \hat{v_{t}}=\frac{v_{t}}{1-\beta_{2}^{t}}$$

**Step 3: Udpate Weights**
$$W_{t} = W_{t-1} - \frac{\alpha}{\sqrt{\hat{v_{t}} + \epsilon}}\hat{m_{t}}$$






+ @ Note Code: mục tiêu không phải là biết cách implementation mà là xác định vấn đề và tìm giải pháp.


### 1.5 Muon Optimizer


### 1.6 Verify Muon vs Adam
+ @ Where Muon’s design really shines. The MoonShot team **optimized for large-scale training, not single-machine benchmarks.** 
	source: https://medium.com/@jenwei0312/reproducing-and-validating-distributed-muon-a-practical-verification-of-communication-0be4d1d9b893
	
+ ! Muon only work with 
+ ? When to use Muon ? Since Muon math requires matrices, you rarely use _only_ Muon. You use a **Hybrid (Muon + AdamW)** approach.
+ $ Distribution Muon: 
	- **Target:** Large-scale **Pre-training** from scratch.
	- **Architecture:** Transformers or ConvNets (models dominated by **2D/4D Matrix weights**).
	- **Setup:** Multi-node clusters where **Inter-node communication** (gradient reduction) is the bottleneck. Muon cuts communication volume by ~40%!).
	- **Batch Size:** Large global batch sizes (Muon thrives on stable statistics).
	
+ $ **Stick with (or Fallback to) AdamW:**
	- **1D Parameters:** Embeddings, LayerNorm gains, and Biases. (These _must_ use AdamW as they cannot be orthogonalized).
	- **Fine-Tuning:** If you are doing PEFT (LoRA), the trainable parameters are already small, so Muon’s overhead isn’t worth it.
	- **Small Scale:** If your model fits on one GPU, the complexity of distributed orchestration outweighs the benefits.
	
+ @ **Verdict:** If you’re training large models on multi-node clusters, Muon is worth trying. The 15% per-step overhead is manageable, and the communication savings will shine at scale.
	For small-scale training (<8 GPUs), stick with AdamW. The complexity isn’t worth it yet.


**Scaling to 4 GPUs in 1 Machine**
![[Pasted image 20260208155510.png | 555]]

**Scaling to 32 GPUs in 4 Nodes/Machine**
![[Pasted image 20260208155600.png | 555]]



