
**OBJECTIVES**
![[Pasted image 20241122200553.png]]

**Optimization Algorithms**
Transformation: origin data change over a linear matrix hence transform

Hàm ko Liên Tục
![[Pasted image 20241122201058.png]]

Hàm Liên Tục
![[Pasted image 20241122201043.png]]
> Đạo hàm là di chuyển từ 1 điểm tới 1 điểm nhỏ/lớn nhất yêu cầu hàm có t/c liên tục.

### Challenges
+ ? Local minima, Global minima, Saddle points
![[Pasted image 20241122201234.png]]
note: cực đại giống cực tiểu, chỉ là thêm dấu trừ tr'c hàm.
+ ? Làm sao để tránh những vùng cực tiểu cực bộ (local minima), yên ngựa (saddle point) và đạt đc điểm cực tiểu toàn cầu (global minima).
![[Pasted image 20241122202008.png]]

**Problem with learning rate**
large learning rate can miss global minimum on a non-convex cost function. While large learning rate sometime help to avoid local minimum. 
![[Pasted image 20241122202501.png]]

**Remember Derivative positive on the right, and negative on the left**. *Thus x will increase itself if x is negative and x will decrease itself if x is positive*. (add substract sign to visualize)
![[Pasted image 20241122203107.png]]

Stochastic Gradient Descent
![[Pasted image 20241122204211.png]]
Update $\theta$ each iteration (m-sample *Batch*, N-sample *mini-batch*) help loss plot look smoother. Bc value change slowly, not alot each update.


# Adaptive Learning Rate

**Learning Rate Decay**: A technique used in machine learning to **gradually reduce the learning rate of a model during training.** *This reduction can occur either at fixed intervals, continuously over time, or when a specific threshold or condition (e.g., no improvement in validation loss) is met.*
![[Pasted image 20241122210630.png]]

use $k$ to control LR changing speed. The larger k is the slower LR changes are.
![[Pasted image 20241122211153.png]]

**Làm sao để cho learning rate tự động giảm 1 cách khoa học (vd: dùng 1 hàm)**

Để LR giảm dần thì K phải tăng dần . Kí hiểu t ~ K
![[Pasted image 20241122212703.png]]

Assign K as the sum of "Derivative of each step" (Cộng dồn đạo hàm của w) 
![[Pasted image 20241122213554.png]]
Rewrite K or the sum of x's derivate as $s_{t}$ (viết lại tổng đạo hàm của x là $s_{t}$), we have $$s_{t} = s_{t-1} + g_{t} ^2$$where $t-1$ is the previous derivative index (đạo hàm của step tr'c đó). 
![[Pasted image 20241122213927.png]]
Since K or $s_{t}$ can be zero, we add a $\epsilon \approx 0.000001$ value.

$$x_{t} = x_{t-1} - \frac{n}{\sqrt{ s_{t} +\epsilon}}$$
**Adagrad for Multiple Variables**
![[Pasted image 20241122215029.png]]
The same but apply partial derivative $w.r.t$  $x$ and $y$.

**Vectorization Adagrad** 
![[Pasted image 20241122215230.png]]
+ ! **Disadvantage:** since $s_t$ is **sum of x derivative** the learning can be too small making it computationally expensive to reach the global minimum. ![[Pasted image 20241122215650.png]]Even if the slope is high. ![[Pasted image 20241122215905.png]]
+ ? **How to solve this problem where** learning rate become too low after n number of step.
+ $ **Moving Average**
Cộng dồn tại vị trí thứ k
-> Tính trung bình từ vị trí thứ k (k $\in \mathbb{Z}$). 
	Nghĩa là chỉ lấy tổng đạo hàm của n giá trị trước nó ![[Pasted image 20241122220648.png]]

Ví dụ, chỉ cộng dồn 1 đoạn chứ ko tính toàn bộ tổng đạo hàm của x. Chỉ tính tổng 1 khoảng đạo hàm của x.
![[Pasted image 20241122220844.png]]

![[Pasted image 20241122221053.png]]
**This actually RMSProp** (*suprise*)
![[Pasted image 20241122221406.png]]

Although, RMSProp not ensure convergence because .... 
![[Pasted image 20241122221541.png]]
**Summary**
![[Pasted image 20241122222107.png]]

**Original Goal:** Giá trị learning rate cần phù hợp cho các vị trí khác nhau. How to achieve a adaptable learning rate for gradient descent function.

---

**Quizz**
![[Pasted image 20241122222643.png]]

Timeseries vì đó là dữ liệu thu thập đc theo thời gian (kinda like sequence data and often store in table)
![[Pasted image 20241122222738.png]]

