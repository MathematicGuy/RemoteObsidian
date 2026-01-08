**Goal:** Learn new Data without forgetting old data. *Aim to mimic human life long learning capability.*
**Continual Learning application:** CV - autonomous vehicles.

### Example Context for CL
	autonomous vehicles

Train on 2 dataset for each tasks -> minimize Loss for both task A (old) and task B (new).
+ ! results is Good perf task B but Worst perf task A. This called catastrophic forgetting/inference.
![[Pasted image 20251224152049.png]]

+ ? How to migate forgetting ? Train from scratch ? with both new and old data.
+ ! Drawbacks:
	+ **Times:** take days/weeks to train -> deplay in business context.
	+ **Computes:** waste of power and compute and access to good compute too.
	+ **Data availability:** trainingdata might be unavailable.
+ $ However, if human can learn incrementally, it must be possible for machine to do the same.

**Solution 1:** **Replay-based training** which train old training data along with new tasks data.
+ ! require more storing old data. Overtime, we'll need to storage.
+ @ **Dilema (trade-off): plasticity-stability** (new knowledge - old knowledge)

### Evaluating continual learning algorithms
+ ? Evaluation method to **test if model learn new data without forget old data **  To answer that cleanly, we want:
	- Tasks that are **clearly different**
	- But **not semantically different**
	- So difficulty comes **only from interference**, not from task complexity.

The method below create new data from itself (hence permutation).
+ $ **Data Permutation tasks**. Evaluate model performance on Permutation dataset after training on Task 1 dataset. ![[Pasted image 20251224152944.png]]
	$P_{2}X_{i}$ - permuted input = *Shuffle pixels for every images from task 1*.
	$y_{i}$ - original output (ie. MNIST output like Task 1)


+ $ **[[Incremental class learning (survey)]].** learn a base task set, then learn addition classes. ![[Pasted image 20251224153430.png]]
-> Không giống với thực tế lắm. Class incremental learning -> giống thực tế hơn.  q


+ $ **Multimodel learning:** learn an *image classification task then learn its audio classification.* Then **Classified using both of those Features** ![[Pasted image 20251224153535.png]]
	This can be difficult bc Features from Images is different from the audio features.

### Approaches for continual learning
![[Pasted image 20251224153854.png]]
- **Train whole network with regularization** -> Optimize new knowledge while penallize changes in old weight.
- **Dynamic architectures** (Add neurons) ie. Architecture growth for new tasks.
+ **Complementary Learning System** (memory + replay) - train new tasks along with old tasks (like human revision).


### 1. Regularization Approach: Learning without Forgetting (LwF)
	LitHoiem 2018 (simple regularization) - Focus on
	Penalize Old Task's Loss.

+ @ **Intuition:** Force the model to learn new knowledge without changing what it already know too much. (Giống chứng minh toán học dựa trên 1 tiên đề nào )
+ ? Shared params across tasks and some task specific params.
	At new task. Update all params, new params and old params.
	-> SO the new *task work well*, but *output of the old task on new data doesn't change too much.* (yeah, regularization)
	
![[Pasted image 20251224154411.png]]
Note: The fact that This is a modified CE-Loss, its actually the Distillation Loss.
+ $\lambda_{\theta}:$ quantified **plasticity to stability tradeoff.**
	+ *Hyperparam Low mean Plasticity High* -> Prioritize new knowledge, learning new task.
	+ *Hyperparam High mean Stability High* -> Prioritize keeping old task, learn less new task.

+ $\lambda_{\theta}\mathcal{L}_{old}(Y_{o}, \hat{Y}_{o}):$ said *new net do not differ from the old net*. Performance of the old task on new data shoudn't change too much

### 2. Optimization-Based Approach: [[Elastic Weight Consolitation (EWC)]]
	Kirkpatrick et all. 2017 - Compromised both new & old
	Loss, find the best of both world based on old task most
	important Weight.

**Ideas:** When trainign on B **learn the Weight that are MOST IMPORTANCE to A,** then **penalize those Weight More.** Try to stay in low error region for A.
![[Pasted image 20251224160224.png# left | 455]]
+ $F_{B}(\theta):$ normal task B Loss Function.
+ $\theta_{i} - \theta^{*}_{A, i}:$ said I want the **Loss of task B at $i$ is close to the Loss of Task A at $i$.** *Penalize any deviation* from $\theta_{i}$ from $\theta^*_{A,i}$ using a quadratic.
+ $F_{i}:$ **Like Attention Score** in Transformer, **determine or Coefficient of $\theta$ (ie. Weights) more important than others.**
	*Treat Important/unimportant weights in diff way* that allow importance direction in task A treated diff than unimportant direction in task A.
+ $\lambda:$ plasticity-stability **trade-off hyperparam.**

+ @ **Original Idea:** Bayesian learning perspective.

**The Graph measures how well the model remember each Task Across the training timeline: train on A -> train on both A+B -> train on all A+B+C)**
	+ The X-axis represents **sequential training** (learning A → then learning B → then learning C)
	+ Y-axis: Remember %.
	+ Blank mean haven't train on task B/C at that training timeline.

+ **Top Panel (Task A):** Shows *how well the model remembers* the _first_ task it learned.
+ **Middle Panel (Task B):** Shows *how well it learns* the _second_ task.
+ **Bottom Panel (Task C):** Shows *how well it learns* the _third_ task.
![[Pasted image 20251224161400.png]]

### Architecture-Based Approach: Progressive Neural Network
	Rusu et al. 2016

Again, **network growth for new task.** Counter intuitive and expensive along the way.
![[Pasted image 20251224173432.png]]


### Replay-Based Approach: Generative Replay
+ ? Train a generative model to output syncthetic data that follows some distribution as training data. ie. Replay synthetic data along with new data.

Use **Old Model output as a part of training data,** Combine Synthetic data from old mode output with the "New Training Data" -> **Old Synthetic (generate by old model) + New Data from new Task**

+ @ **Intuition:** **Active Recall & Feynman Technique,** you don't just re-read a textbook (Replay Buffer), you re-explain the concepts to yourself, **you force yourself to generate the explaination from scratch.** -> *Consolidata Old infor while learning new infor.*
![[Pasted image 20251224173649.png]]
**Original Ideas:** Human strengthen connection from the new infors by connect it with the old infor. Think of information like a river, everything need to be connect, so we connect old infor with the new infor.
![[Pasted image 20251224174428.png]]


## Continual Learning Approachs Overviews
### Regularizations
Add penalty for changing old knowledge, penalize importance weights.
![[Pasted image 20251222220332.png]]
+ ? **Related to human:** stick to well-know definition, understanding new information base on the old ones.
+ $ Fast, low effort.
+ ! Eventually block learning when all important infors slot are filled.

### Replay-Base approach
**Ideas:** replay old data while training new data. (quite the same as human). This approach **Most Effective right now**.
![[Pasted image 20251222220352.png]]
+ ? **Related to human:** Spaced repetition (Anki), Rehearsal old infors after learning new infors, Mixed problem set flashcards.
+ $ -> Very Effective, update old information along with new information.
+ ! More computes, time consuming.

### Optimization-Base approach
Like Fast GPS for learning. Find a optimization algo for **learning new knowledge without damaging the old.**
![[Pasted image 20251222220632.png]]
+ ? **Related to human:** Learning with explicit constraints. *Proof-based learning*. Like studying math. *I'll learn this new method, but it must not violate the old theorem.*
+ $ Strong theoretical grounding, high precision. Like how Mathematicians learn - not how begineers do.
+ ! Slow, Hard to scale.

### Representation-Base approach
**Learn the Alphabet before you learn to write a novel.** Base model -> Teach basic knowledge first then more advance, abstract knowledge later.
![[Pasted image 20251222220651.png]]
+ ? **Related to human:** Learn the foundation and general knowledge before expand to more advance knowledge.


### Architecture-Base approach
AI **Structure Growth for each new task**. Although it have **perfect memory but its really heavy** (cost more compute).
+ @ Idea: Don't overwrite - Expand or isolate diff information.
+ ? MoE - Mixture of Expert.
![[Pasted image 20251222220720.png]]
+ ? **Related to human:** Seperate notebooks per subject, *mental modularization* different mental 'models' for each subject (eg. Math brain vs Language brain). Context dependecy recall.
+ $ Clean seperation for each task.
+ ! **Lack connections:** Ace exams but fail to connect ideas across fields, like Specialist.


### The Root of Catastrophic Forgetting
#### Mathematical Perspective
[[VIsualize Catastrophic Forgetting]]

----



![[Pasted image 20260106230855.png]]
1) Sampling các sample quên nhiều nhất. 
2) Tạo 1 buffer để học lại các sample quên nhiều nhất trong Sampling samples ~ sample có nhiều Entropy nhất. 
-> Sample nào quên nhiều nhất thì cho vào Buffer để huấn luyện cùng dữ liệu mới. 


**task boundary** ==marks the transition between distinct learning phases (tasks)==

![[Pasted image 20260106233351.png]]

![[Pasted image 20260106233340.png]]

Here is a prompt designed to generate a comprehensive visualization of the HAL workflow. You can use this prompt with Gemini (or any AI tool capable of rendering **Mermaid.js** or **Graphviz** diagrams) to create a "Dynamic View" of the architecture.

![[Pasted image 20260107002133.png | 544]]

![[Pasted image 20260107001954.png]]

![[Pasted image 20260107004214.png]]


![[Pasted image 20260107105213.png]]

![[Pasted image 20260107105342.png]]

