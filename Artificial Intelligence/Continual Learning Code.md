![[Pasted image 20260204121726.png# left | 344]]

---

**Câu Hỏi Nghiên cứu:**
Khi nào cần áp dụng Continual Learning: Is this system required long-dependency context ? e.g. need LLM to solve needle-in-a-haystack problem, required to finetune 1 model continously. 
**Mục đích nghiên cứu:** Xây dựng 1 mô hình có khả năng Học Kiến Thức Mới mà Không Quên Kiến Thức Cũ.
**Key Research Direction:** 
Ví dụ: CLFace - A Scalable Framework for Continual Face Recognition. 
-> Mô tả bài toán càng rõ càng nhiều ng giúp đc hơn.
Mục tiêu là Có được 1 bài toán cụ thể. 









---
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

OPL bypasses the classifier weights and applies geometric constraints directly to the intermediate features fi​ within a training mini-batch.

enforces **inter-class separation** and **intra-class clustering** at the mini-batch level.
![[Pasted image 20260228181522.png | 355]]
1) **Feature Extraction:** input mini-batch of imgs and outputs intermediate feature vectors.
2) **Normalization:** $l_{2}\text{ norm}$ 
3) **Intra-Class Clustering (same class):** OPL calculates the *cosine similarity (represented as s) between all pairs of features* belonging to the _same_ class **within the mini-batch**. The loss function **pushes this value towards 1**, ensuring same-class samples *cluster tightly.*
4) **Inter-Class Seperation (diff class):** OPL clc cosine similarity $d$ between features in diff classes. use abs value $|d|$ and push value towards 0. Ensuring diff class features **become orthogonal (perpendicular) to each other**. 
5) **Combine Intra-Inter class component** we got OPL loss func $\mathcal{L}_{OPL}=(1-s)+\gamma.|d|$ ($\gamma$ as hyperparam)
+ @ OPL Summary: if the *same class then cluster tighly*, else *different class push towards orthogonal* $$\mathcal{L}=\mathcal{L}_{CE}+\lambda.\mathcal{L}_{OPL}$$ just plus OPL.

Proposal - Feature Analysis like OPL and Orthogonality Visualization 
![[Pasted image 20260228181827.png]]
![[Pasted image 20260228181848.png | 444]]


## TreeLoRA
Note: TreeLoRA improve base on Orthogonal-LoRA not OPL-LoRA. Ours research base on TreeLoRA & OPL (Orthogonal Projection Loss) Note: make sure to compare OPL with OGD.
**Core Ideas:**
+ **Hierachical Task Structure:** organized tasks into a tree where top layers capture shared, low-level patterns and deeper layers capture task-specific semantics patterm. (Intuition enough) 
+ **Gradient Similarity Grouping:** group base on task's gradient direction. Similar tasks share knowledge by the shallow/top layers, while conflicting tasks are seperate into different branches. 
	-> OPL group *similar tasks of the same class* into *tight cluster*, diff class orthogonal. 
	+ ? Build Tree base on that *tight cluster.* Where *Orthogonal class* (ie. conflicting tasks) are seperate into diff branches. 
	
+ **Bandit-Based Efficiency:** use multi-armed bandit algorith (*Lower Confidence Bound or LCB*) to quickly find the most relevant branch in the tree. (belance between trying new or less-used branches) 
	
+ **Spare Updates:** because tasks are seperated explicitly, the model only need to update a small portion of params (LoRA adapters) for each new tasks. -> Reduce training time and storage and compute.
	+ $ *Efficient Update:* Reduce compute and time by only update specific LoRA adapters. 
	+ Adaptive Regularization: gradient diff between current task and selected previous group ? (explain bc this is important)

**Tree Evolution and Storage** (Check Later)
After the task is learned, the tree itself is updated to include the new information:
- **Inserting New Adapters:** The newly learned sparse parameters (adapter) are recorded and inserted into the tree at the leaf node of the nearest branch.
- **K-D Tree Splitting:** If a group grows too large, the node is split using the **median of gradient similarity** (L1-norm) to ensure the tree stays balanced and adaptive.
- **Merging Strategy:** If storage limits are reached, highly similar leaf nodes can be merged into a single adapter to save space.

### Lower Confidence Bound (LCB) - related to multi-armed bandit problem
+ @ Which "branch" of past knowledge is most compatible with the new task.
	in TreeLoRA, the "reward" is actually **gradient distance** (dissimilarity), so the goal is to _minimize_ this value to find the closest task match

$LCB$ for a *node* $k$ at time $t$ is defined as: (*This already solve the Threshold problem*)
$$LCB_{k}=\hat{\mu}_{k} - 2 \sqrt{ \frac{\log t}{n_{k}} }$$
$\hat{\mu_{k}}$ (*Exploitation Term*): average estimated similarity (gradient diff) between current task and the $k-th$ task group (tree branch). Low $\hat{\mu}_k$ value mean the current task $k$ is very similar to what stored inside this branch. 

$2\sqrt{ \frac{\log t}{n_{k}}}$ (*Exploration Term*) - account for Uncertainty. 
- $t$ is the total *number of iterations*.
- $n_k$​ is the *number of times this specific node k has been visited*.
- **Intuition:** If we haven't visited a branch very often ($n_k$​ is small), the "uncertainty" value becomes large. Subtracting a large number from $\mu^k$​ makes the overall $LCB_{k}$ smaller, which tricks the algorithm into "picking" that branch to see if it's actually a good match
+ @ If THIS BIG then $LCB_k$ *small*, hence *good match*. 


**TreeLoRA workflow**
*TreeLoRA captures task similarity through gradient direction* and gradient direction can only be determined after calculating gradients of all previous tasks with linear complexity. (ie. calc gradient between it and all previous task)

![[Pasted image 20260228201317.png|434]]
(2) ![[Pasted image 20260228201305.png | 344]]
(3) ![[Pasted image 20260228201348.png |429]]
(Section 3.3)
![[Pasted image 20260228201423.png | 444]]

## Cách để ra paper: nhìn vào vấn đề trong việc Ghép -> giải quyết vấn đề -> These are the Big Problems we need to ask:

### 1. OPL match the "Mini-Batch", but where does the mini-batch live in TreeLoRA ie. mini-batch route
+ ? mini-batch in OPL vs mini-batch in TreeLoRA. DO they compatible ?  

### 2. Feature Space Definition (Where does OPL live?)
+ ? Note: OPL calc features loss base on its features. `e.g. OPL(features, label)`
TreeLoRA inject sparse LoRA adapters at various attention layers. 
+ ? Where do you decide to inject OPL. to the `[cls` token embedding at the final layer before the MLP head. or the hidden states or the adapters. 
	OPL apply to the final layer by default, but it means OPL is optimizing the _combined_ output of the frozen pre-trained weights and the TreeLoRA sparse weights.

### Metric Mismatch: OPL use $L_{2}$ norm while TreeLoRA use $L_{1}$ norm

### Loss Balancing and Tunning ($\gamma$ and $\lambda$)
![[Pasted image 20260228203305.png | 544]]
You will need to balance $\gamma$ (*controlling inter vs. intra class focus inside OPL*) , $\lambda_{OPL}$​ (controlling OPL's strength vs. Cross Entropy), and $\lambda_{\text{Tree}}$​​ (*controlling the sparse parameter updates*). If $\lambda_{OPL}$​ is too high, the model might aggressively *separate current classes at the expense of the smooth tree-branching* logic TreeLoRA relies on
+ ? Theory: seperate current classes because OPL good at seperation

**Gemini Summary:** 
Integrating OPL into TreeLoRA will definitely improve class separation _within the current task being learned_. However, unless you supply it with past data (a memory buffer), OPL will be "blind" to past tasks, meaning it won't help prevent catastrophic forgetting between tasks—that burden will still rest entirely on TreeLoRA's routing mechanism.


