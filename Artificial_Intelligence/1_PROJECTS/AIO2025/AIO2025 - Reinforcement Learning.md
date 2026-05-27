# RL Foundation
## Introduction to RL
Model in RL don't have Loss function. 
it interact with an ENV -> have feedback -> Take action -> receive reward if done right 
+ good action reinforce
+ need a policy that maximize long-term reward.
![[Pasted image 20260415202958.png | 555]]
Dữ liệu Input duy nhất là Dữ Liệu nó học từ Mô Trường (tự tạo ra trong lúc chạy)
+ ? *RL considers as a whole problem* instead of subproblems
	Goal *directed agent interacting with an uncertain environment*
	Start with *complete, interactive, goal-seeking agent*
	*Goals are explicit*

"RL considers as a whole problem instead of subproblems"
+ ? Dữ liệu Agent nhận vô là gì phụ thuộc vào Observation Space -> Dữ liệu là cái agent quan sát đc trực tiếp tại thời điểm hiện tại *-> Dynamic Live Action Data*
![[Pasted image 20260415203724.png]]
Ko phải học 1-1 -> overfitting mà học để khi gặp tình huống gần giống thì vẫn xử lý đc.
+ ! Constrain: ko lập quy luật -> giúp model tự tìm ra quy luật. 
+ $ Thu thập dữ liệu từ mọi hành động trong quá khứ -> Đánh giá hành động nào giá trị nhất. 
+ @ Bản chất của RL là *học cách Đánh Giá.* 

![[Pasted image 20260415205503.png]]

**How Agent see Goals** Action -> State -> cacl Reward of that Action -> back to Action
-> The Goals is to have the Largest "Actions -> Rewards" Chain.
![[Pasted image 20260415210123.png]]
$\gamma$ represent the discount -> make action in the future have Less Effect -> Prioritize current action. 

### Exploration / Exploitation tradeoff
Exploration - try sth new
Exploitation - prioritize that Winning Move

Policy quyết định dự vào Value Function.
![[Pasted image 20260415213850.png]]
Target - reward nhận từ môi trường.

![[Pasted image 20260415214531.png | 399]]
N(a) = số lần chọn 1 States. CHọn 1 lựa chọn càng nhiều thì Reward càng nhỉ. 

**Tracking a Non-Stationary Problem**
![[Pasted image 20260415214644.png]]
-> Cân bằng lại, mọi Lựa Chọn đều quan trọng như nhau dù có đc chọn nhiều hay ít hơn,
Simplified công thức ra đc in general $Q_{t+1}$ 
$\alpha$ - value in range $(0, 1)$ 
-> ý nghĩa thứ 2 của discount - cho biết cái reward signal trong tương lai có vai trò như nhau.

*True Value Function -> Estimate Final Reward Distribution* ![[Pasted image 20260415215152.png]]
*Q - Optimistic Initial Values*
Q high -> explore more
Q low -> explore less

**Upper-Confidence-Bound Action Selection (UCB)** 
![[Pasted image 20260415215408.png]]
-> Control Degree of exploration (refers to the extent to which the *agent prioritizes trying actions with uncertain reward* estimates over actions known to yield high rewards)


More Uncertainty but *might found more Reward and Experience,* eventually surpass greedy method.
![[Pasted image 20260415215548.png | 344]]


## MDP & Policy Representation
$E$ -> epected value -> average outcome
![[Pasted image 20260415220655.png]]

## Value Function


## Bellman Equation
+ @ Ý tưởng chính: States $v_{\pi}$ là giá trị đại diện (expected value) lấy tổng của các giá trị Trung bình dưới nó -> ý tưởng áp dụng cho cả g, v, q 

*Bellman Equation*
Node $$v_{\pi}$$Sum tất cả các Giá trị trung bình chạy ở States bên dưới)
![[Pasted image 20260415220908.png]]

$$R_{t+1} + \gamma G_{t+1}$$
trong đó $G_{t+1}$ là ĐỆ QUY.

![[Pasted image 20260415221158.png]]

Q value vẫn thế - node trên gộp node dưới (đại diện cho các node ở dưới)
![[Pasted image 20260415221345.png]]
Low, high -> weight
Wait -> action

**Policy Evaluation (Prediction)**
![[Pasted image 20260415221817.png]]


![[Pasted image 20260415222135.png | 485]]



# Model-Free RL
## Monte Carlo


## TD Learning


## Q-learning & SARSA


## Deep Q-Learning & Practice