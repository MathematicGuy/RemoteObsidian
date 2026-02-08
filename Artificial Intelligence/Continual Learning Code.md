****Code Tree Lora (rank 8) + Orthogonal Loss:** [https://github.com/Jennifer1907/Tree_LoRA_Ortho](https://github.com/Jennifer1907/Tree_LoRA_Ortho)
![[Pasted image 20260204121726.png# left | 344]]
**Kết quả:**
+ Trước khi thêm Orthogonal Loss:
	All Average: 30.0991
	Last Average: 27.7614
	BWT: -17.6536
	
+ Sau khi thêm Orthogonal Loss: 
	All Average: 32.4216 
	Last Average: 27.9307 
	BWT: -16.9429



## Dataset
[Permuted MNIST](https://www.kaggle.com/code/dlarionov/continual-learning-on-permuted-mnist#Part-2.-Catastrophic-Forgetting-on-permuted-MNIST):  {num_tasks} different permutations of the MNIST dataset are generated, each of which represents a separate task. Permutations are obtained by randomly rearranging pixels for each image in the original dataset in the same way for each task. The same neural network is trained on each task sequentially. Quality on each task is measured between task transitions.

 
## CMS
Note: Adam + Muon + CMS = Multi-scale Momentum Muon (M3)
![[Pasted image 20260111211050.png]]
For each $k-iteration$, $O_t^{(2)}$ (CMS) update in parallel with $O_{t}^{(1)}$ (Muon), but if Chunk size $\hat{C}$ is not met, $O_{t}^{(2)}$ just return 0. ![[Pasted image 20260112141205.png]]
### Adam Optimizer - [[25M8W1 - Gradient Descent with Momentum]]
### Muon Optimizer (use Newton-Schulz orthogonalization)
**Intuition:**  Instead of tweaking each weight separately, Muon zooms out and optimizes entire _matrices_. 
-> helps every part of the network *learn more equally,* instead of letting just a few features dominate. 

**Preliminaries Definition (tiền đề)**
+ [[Linearly Dependent and Independent]], is dependent if a vector cannot be scale or multiple by 1 or a set of vector  - in 1 or multiple dimension.
+ *Orthogonal Matrix* is special bc it *only rotates things* not stretches or squishes them. If there's no stretching in any direction in any direction, it mean all of the "stretch factors" (all singular values) must be extractly 1.


This idea generalizes to higher dimensions. This idea generalizes to higher dimensions. The number of singular values equals the number of rows or columns of the matrix (its rank). 
-> As the matrix become orthogonal, diagnol value converged into 1. 
![[Pasted image 20260204155844.png# left | 655]]
Note:
+ Convergence of `M @ M.T` to Identity. Last plot show representation of identity matrix that converge towards 1. 
+ Muon take more compute by `@ M.T` but reduces the total time and data needed to read SoTA performance -> So fast training still. 

**Muon best LR** value is 0.07 and affect on training time is negligible. Note: Muon have $O(n^3)$ time complexity. 
![[Pasted image 20260204152924.png | 555]]

![[Pasted image 20260204152732.png | 355]]


**Compare to Adam Optimizer**
![[Pasted image 20260204152530.png]]
-> Adam is much more sensitive, require precise lr. 

*Adam:* adjusts weight amount for each parameters
*Muon:* makes weight update matrices orthogonal which improves neural net learning

----

