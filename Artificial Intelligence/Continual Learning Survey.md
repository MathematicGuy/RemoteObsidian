Note: cần benchmark để đo đạc vấn đề (chỉ rõ vấn đề mà benchmark cho thấy)

![[Pasted image 20260214200246.png]]
a. mô tả bài toán continual learning. 
b. Tradeoff mong muốn cho Stability và Plasticity (Generalizability) 
c. Các phương pháp được áp dụng lên toàn bộ quy trình ML để đạt đc Tradeoff mong muốn. 
d. Continual Learning đc áp dụng trên mọi lĩnh vực đảm bảo mô hình có khả năng học và thích ứng với dữ liệu liên tục trong thực tế mà ko Catastrophic Forgetting.
+ ? Easy solution for Catastrophic Forgetting is to retrain the model entirely but create huge computational and storage overheads.

![[Pasted image 20260215100028.png]]
Note: slide mô tả weight mô hình thay đổi sau khi học phân phối dữ liệu mới. So sánh cách học truyền thống và cách học continual learning. 

### Sec. 2 Continual Learning Approaches & Scenarios
**introduce the setups of continual learning,  including its basic formulation, typical scenarios and evaluation metrics.**

#### Replay
+ $ Recovering old data distribution to prevent catastrophic forgetting. 
+ ? *Replay acts as a direct constraint on the gradient updates.* By mixing old data with new data, the optimization is forced to find the gradient that minimize loss between current task and replayed samples. 
	in other term, recovers the distribution of old features/tasks through replay.
![[Pasted image 20260215095432.png | 677]]


**Gradient Rectification** method like **GEM (Gradient Episodic Memory)** explicitly use replay data to constrain parameter updates. They ensure update vector for new task has *non-negative angle* (2 task moving in opposite direction) to prevent valid knowledge from being overwritten.
	Like in [[Vector Dot Product]] If
+ $g^{t}_{\text{current}}.g_{\text{replay}} \geq 0$ or angle $0^{o} \leq \theta<90^o$ 
	then 2 gradient are pointing in the same direction, indicate learning new task also helps improve old task. This is **Positive Forward/Backward Transfer** (Forward mean **old task help learning new task** and Backward mean learning new task help old task). Intuition is learning how to balance on a bycicle also help with learn how to ride a bike.  
	![[Pasted image 20260215213938.png | 344]]
	
+ $g^{t}_{\text{current}}.g_{\text{replay}} = 0$ or angle $\theta = 90^o$ The gradient are orthogonal, changing params for new task has NO Effect on the old task.
	
+ $g^{t}_{\text{current}}.g_{\text{replay}} < 0$ or angle $90^{o} \leq \theta < 180^o$
	the dot product are negative indicate the gradients vector move in opposite directins. New task's gradient actively increasing the loss on the old task -> Catastrophic Forgetting.
	 
GEM's allow update for similar gradient and project gradient (force orthogonality to opposite gradient) to prevent forgetting. 
	
A-GEM explicitly check for this "opposite direction" scenario. 

**Synergy:** Replay is highly synergistic with **Regularization** (specifically Knowledge Distillation). Many state-of-the-art methods (e.g., iCaRL, DER) combine replay with distillation to mitigate the bias caused by limited buffer sizes.


#### Architecture
*Parameter Allocation* (assigning specific neurons or weights to specific tasks, often using masks)
*Model Decomposition* (seperating the model into task-specific component like *MoE*)
-> avoids conflict from overlapping parameters completely. gradient of new task doesn't affect the gradient of the old task. 

![[Pasted image 20260215095648.png]]

#### Representation
Encourage model to learn representations that are sparese, orthogonal, and widely distributed. 
![[Pasted image 20260215095707.png]]
+ $ help Replay work more effectively


*1. Spare Representation* (e.g. *Drop Out)*
Sparsity means for any specific input, only a small subset of neurons in the representation layer are active (firing) - (kind of like parameter allocation in architecture-based approach)
+ ? If **Task A** uses neurons `{1,2,5}` and **Task B** uses neurons `{3,4,6}`, updating the weights to learn Task B will not disrupt the knowledge stored in the neurons used for Task A. Basically, isolating knowledge in different parts of the network. 
-> _Sparse Representation increases sparsity in weights, similar to Parameter Allocation, but might require more total weights._


*2. Orthogonal Representations* (conclusion based on GEM & A-GEM)
Orthogonal Approach enforce orthogonal to gradient moving in opposite direction to prevent catastrophic forgetting while allow Positive forward/backward transfer
+ ? Apply Orthogonal so vectors of different tasks are **perpendicular** to each other (their dot product is zero) as in [[Vector Dot Product]]. So the udpate direction of task A gradient doesn't affect the update direction of task B gradient.
Note: Only true for GEM, OGD/GPM block all overlap in the protected subspace.

*3. Widely Distributed (Uniformly Scattered)* -> Giảm biến động của Loss. 
This means the *"Wider local minimum or Flat loss landscape"* representations utilize the entire available feature space rather than being clustered in a small corner. They are *"maximally separated" or have high entropy.* In simple term, *aim for Flat Minima where a single solution works well for both.*
-> Designed to maintain high accuracy for both task, not to average them out to a lower value. 
![[Pasted image 20260215105345.png]]
+ ? **Effect of Flat Minima** when features are widely distributed there are more room to insert new classes or task without them overlapping with old ones. 

```ad-summary
**Sparsity** prevent neurons from overrwriting each other
**Orthogonality** prevents gradients from conflicting with each other
**Wide Distribution** prevent tasks from crowding each other in the feature space
```



#### Regularization
Modify the Loss function to constrain changes between weight changes, prioritizing stability and plasticity. 

Apply **Gradient Rectification,** keep update to stay within the **"null space"** of the old tasks **(areas where changing weights doesn't hurt old performance)**
+ Fail in Class-IL
+ Regularization often fail without Replay. 
![[Pasted image 20260215095605.png]]

#### Optimization
Explicitly manipulates the optimization process to maintain performance across task ie. Ensure new task update doens't affect old task.
![[Pasted image 20260215095724.png]]

**Gradient Projection:** Methods like OGD (Orthogonal Gradient Descent) and GPM (Gradient Projection Memory) project the gradient of the new task onto the subspace orthogonal to the gradient space of old tasks. This ensures the update is "safe" for previous tasks.

-> **Work best with Replay** (to approximate the old gradient space) or Representation learning (to ensure the gradient subspaces are orthogonal) and easier to seperate. 

## Synergy
**Baseline -** Replay baseline 

1. **Replay + Regularization:** Replay provides the data to approximate the old distribution, while regularization (distillation) enforces consistency on that data.
	
2. **Optimization + Representation:** Better representations (e.g., from pre-training) create orthogonal feature spaces, making it easier for Optimization methods (like Gradient Projection) to find non-interfering subspaces for new tasks. 
	
3. **Architecture + Replay:** Modular architectures often use a replay buffer or a generative model to decide which module (expert) to activate for a given input

![[Pasted image 20260215095931.png]]

![[Pasted image 20260215095947.png]]

### Sec. 3 Theorical Foundation
**we summarize the theoretical efforts on continual learning in response to its general objectives, which motivate the development of various continual learning methods**

**Theoretical Unification**
![[Pasted image 20260215095806.png]]




### Sec. 4
**we present a state-of-the-art and elaborated taxonomy of representative methods, analyzing their motivations and typical implementations**

### Sec. 5 and 6
**we describe how these methods are adapted to realistic applications in terms of scenario complexity and task specificity**


**TODO:** BenchMark
![[Pasted image 20260215225337.png]]

![[Pasted image 20260215225400.png]]

![[Pasted image 20260215230509.png]]

![[Pasted image 20260215225148.png]]