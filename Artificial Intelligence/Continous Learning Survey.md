**Continous Learning -** Learn constantly without forgetting.
 
**Nested Learning -** new ML paradigm (eg. Google HOPE architecture) by structuring models as nested optimization problems with different update speeds, mimicking brain memory to prevent catestrophic forgetting and build **"living memory" for AI** (good at Needle in a Haystack problem). 
	Inspired from the brain's layered memory consolidation (*fast for short-term*, *slow for long-term*)

LLM remain static after training. 
**All NN are associative memory system** that compress their own context flow. 

Gradient Descent with momemtum is indeed a low-level optimization process, where the memory is optimized by simple gradient descent algorithm. 

![[Pasted image 20251222215957.png]]
**-> Catastrophic Forgetting:** Model forget old task the second it learn the new one. 
+ ! Danger in Medical when docter update a new infor leading to a performance decrease in old infor.  


**Stability vs Plasticity**
![[Pasted image 20251222220050.png]]
The more you learn, the more you forget so you have to tradeoff between learning new things and forgetting old things.
![[Pasted image 20251222220212.png | 444]]

### Five keys Strategies
![[Pasted image 20251222220310.png]]

#### Regularizations
-> add penalty for changing old knowledge. 
![[Pasted image 20251222220332.png]]

![[Pasted image 20251222221216.png | 255]]


#### Replay-Base approach: most Effective right now.**  
![[Pasted image 20251222220352.png]]

#### Optimization-Base approach
Like Fast GPS for learning. Find a optimization algo for learning new knowledge without damaging the old.
![[Pasted image 20251222220632.png]]

#### Representation-Base approach
**Learn the Alphabet before you learn to write a novel.** Base model -> Teach basic knowledge first then more advance, abstract knowledge later. 
![[Pasted image 20251222220651.png]]

#### Architecture-Base approach 
AI **Structure Growth for each new task**. Although it have **perfect memory but its really heavy** (cost more compute).  
+ @ Idea: Don't overwrite - Expand or isolate diff information.
+ ? MoE - Mixture of Expert.
![[Pasted image 20251222220720.png]]








----
#### Terms & Definitions
**Joint Training:** baseline model **trained** on data from **all tasks simultanously.** 

**Learning (Plasticity):** Gravity pulling the ball down into a valley (low error for the current task).

**Forgetting:** When the ball moves to a new valley for Task B, it is no longer in the valley for Task A.

**Forward Transfer (FWT):** The influence of **previously learned tasks on the performance of future tasks** (positive FWT means knowing Task A helps learn Task B faster).

**Backward Transfer (BWT):** The **influence of learning a new task on the performance of previously learned tasks.** Negative BWT indicates catastrophic forgetting; positive BWT indicates that learning a new task actually improved performance on an old one.

**Regularization (EWC):** **Attaching a spring to the ball anchored at the bottom of Task A's valley**. The spring is stiff **(hard to pull) for important parameters and loose for unimportant ones.** This allows the ball to move toward Task B's valley but prevents it from leaving Task A's valley entirely.


**Herding:** a deterministic strategy for selecting **which samples to store in memory (for replay)** based on finding **samples that best the approx class mean in feature space.** 

**Methodological Approach** (Taxonomy - phân loại)
+ **Replay-based Approach:** Focuses on approximating and recovering old data distributions to train alongside new data.
+ **Optimization-based Approach:** Explicitly manipulates the optimization program (e.g., gradients).
+ **Architecture-based Approach:** Uses specific network structures to reduce interference. 
	+ Model Decomposition: Seperates the model into task-sharing and task-specific components. 
	+ Modular Netowork: Parralel sub-network for different tasks.
	+ Parameter Allocation: dedicate specific subspaces of params to specific tasks. (e.g., using masks to *freeze weights for old tasks*)

