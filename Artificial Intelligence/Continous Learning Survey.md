[[Continual Learning Terms & Definitions]]
![[Pasted image 20251222215957.png]]
**-> Catastrophic Forgetting:** Model forget old task the second it learn the new one. 
+ ! Danger in Medical when docter update a new infor leading to a performance decrease in old infor.  


**Stability vs Plasticity**
![[Pasted image 20251222220050.png]]
The more you learn, the more you forget so you have to tradeoff between learning new things and forgetting old things. 

**Catastrophic Forgeting in Bayes Perspective**
When train on new task, model Gradient prioritize new task and forget old task -> Catastrophic forgeting. 
	Continual Learning -> balance Gradient for both task A & B.
![[Pasted image 20251222220212.png# left | 444]]
Old task posterior become prior for new task. 
![[Pasted image 20251225201719.png# left  | 333]]

### Continual Learning Evaluation Technique
![[Pasted image 20251225202510.png]]


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

---

![[Pasted image 20260107233331.png]]

**Prompt**
"hay cho mình ví dụ tính tay từng bước, cho từng task, đừng bỏ qua bước nào, và ghi rõ công thức"
![[Pasted image 20260108000431.png]]
K - số anchor point cho 1 task. 
Overfitt - ko học kiến thức mới mà ôn đi ôn lại kiến thức cũ. 
$\phi(e_{t})$ = phi của anchor


