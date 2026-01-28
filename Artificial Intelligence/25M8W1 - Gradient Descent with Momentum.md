### 1.1 Momentum
**Gradient Descent ban đầu:**
$\theta = \theta - \eta \nabla_{\theta}J(\theta)$ có $\theta$ là tham số của mô hình cần cập nhật và $\nabla_{\theta}J(\theta)$ là đạo hàm của $\theta$.

+ @ Theo góc nhìn vật lý, do learning rate cố định, GD thông thường không thể vượt qua đc các Local Minimum mọi lúc đc, trong khi đó nếu có thêm 1 lực vật lý như là Đà (momentum) thì GD có thể dễ dàng vượt lên các Local Minimum không quá dốc.   
![[Pasted image 20260121211427.png]]
Để cập nhật Gradient với Momentum ta đơn giản gộp chung phép tính đạo hàm với biến Momemtum $\gamma v_{t-1}$ lại thành 1 biến gia tốc $v_{t}:$  
$$v_{t} = \gamma v_{t-1} + \eta \nabla_{\theta}J(\theta)$$
$\gamma:$ thường có giá trị 0.9 (ie. dùng 90% giá trị momentum), dùng để kiểm soát số % momentum dùng để tính Gradient.  
$v_{t-1}:$ là vận tốc tại thời điểm trước đó. $v_{t}$ là hiện tại
$\theta:$ vị trí hiện tại của hòn bi.
$\nabla J(\theta):$ "slope / đạo hàm" của điểm trước đó.
-> Ta cập nhật tham số như bình thường: $\theta = \theta - v_{t}$


Tuy Momentum giúp vượt qua Local Minimum để đi đến Global Minimum tốt hơn nhưng cũng chính vì Momentum mà nó mất quá nhiều Iteration để ổn định vị trí tại điểm cực tiểu chính.
![[Pasted image 20260121205747.png]]

### 1.2 Nesterov accelerated gradient (NAG)
+ $ Khắc phục vấn đề "Ổn định do Momentum gần điểm cực Tiểu", Nesterov accelerated gradient (NAG) ra đời để giúp hội tụ nhanh hơn. 
+ @ Ý tưởng chính là *dự đoán hướng đi trong tương lai (nhìn tr'c 1 bước).* Cụ thể là nếu cập nhật theo hướng của Momentum $\gamma v_{t-1}$ thì ta có thể xấp xỉ vị trí tiếp theo là $\theta - \gamma v_{t-1}$. Nói cách khác ta thay $\nabla(\theta)$ thành $\nabla (\theta - \gamma v_{t-1})$ vì $\theta$ đại diện cho vị trí, tham số hiện tại. 
![[Pasted image 20260121212359.png# left ]]
+ GD + Momentum: Cộng Momentum với *Gradient của điểm hiện tại.* 
+ NAG: Cộng Momentum với *Gradient dự đoán xấp xỉ trong tương lai.* 
 (Nguồn: [CS231n Stanford: Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/neural-networks-3/)) - ([Other Optimizer](https://www.ruder.io/optimizing-gradient-descent/))

Công thức gia tốc mới là:
$$v_{t} = \gamma v_{t-1} + \eta \nabla_{\theta}J(\theta - \gamma v_{t-1})$$
So sánh 2 thuật toán cho bài toán LR, ta thấy rõ NAG hội tụ nhanh hơn. 
![[Pasted image 20260121213508.png]]


c