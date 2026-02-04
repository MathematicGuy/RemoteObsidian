**Code Tree Lora (rank 8) + Orthogonal Loss:** [https://github.com/Jennifer1907/Tree_LoRA_Ortho](https://github.com/Jennifer1907/Tree_LoRA_Ortho)
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

