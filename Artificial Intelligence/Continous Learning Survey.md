
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
Add penalty for changing old knowledge, penalize importance weights.
![[Pasted image 20251222220332.png]]
+ ? **Related to human:** stick to well-know definition, understanding new information base on the old ones. 
+ $ Fast, low effort. 
+ ! Eventually block learning when all important infors slot are filled. 

#### Replay-Base approach: **most Effective right now.**  
**Ideas:** replay old data while training new data. (quite the same as human)
![[Pasted image 20251222220352.png]]
+ ? **Related to human:** Spaced repetition (Anki), Rehearsal old infors after learning new infors, Mixed problem set flashcards. 
+ $ -> Very Effective, update old information along with new information.
+ ! More computes, time consuming. 

#### Optimization-Base approach
Like Fast GPS for learning. Find a optimization algo for **learning new knowledge without damaging the old.** 
![[Pasted image 20251222220632.png]]
+ ? **Related to human:** Learning with explicit constraints. *Proof-based learning*. Like studying math. *I'll learn this new method, but it must not violate the old theorem.*
+ $ Strong theoretical grounding, high precision. Like how Mathematicians learn - not how begineers do. 
+ ! Slow, Hard to scale. 

#### Representation-Base approach
**Learn the Alphabet before you learn to write a novel.** Base model -> Teach basic knowledge first then more advance, abstract knowledge later. 
![[Pasted image 20251222220651.png]]
+ ? **Related to human:** Learn the foundation and general knowledge before expand to more advance knowledge.


#### Architecture-Base approach 
AI **Structure Growth for each new task**. Although it have **perfect memory but its really heavy** (cost more compute).  
+ @ Idea: Don't overwrite - Expand or isolate diff information.
+ ? MoE - Mixture of Expert.
![[Pasted image 20251222220720.png]]
+ ? **Related to human:** Seperate notebooks per subject, *mental modularization* different mental 'models' for each subject (eg. Math brain vs Language brain). Context dependecy recall. 
+ $ Clean seperation for each task. 
+ ! **Lack connections:** Ace exams but fail to connect ideas across fields, like Specialist.


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

