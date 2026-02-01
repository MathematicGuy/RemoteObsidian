Note: Scout and check the slides first and organize ideas. Don't just learn in Linear, overview the material first. 
	Miros framework.

Modern Transformer base LLM suffer from Anterograde Amnesia which make every experience is a new experience, *they do not truely "learn" beyond their current context.* 
-> Only remmeber context from pretrain, don't learn new knowledge from live conversation because they will forget it in the next converstation. 

MoE with CMS is a Design Choice. 
How AI learn and memorize (Associate Memory)


## IMPORTANT
Is Nested Learning a Good paper ? Prove from Rebuttal (Borderline rejected) & Reddit Comments 
Explain 3 Nested Learning Definition (Associate Memory, Update Frequecy, Nested System) and what does this mean in designing M3 algorithm. 
-> What we want to focus in is M3 Algorithm. Because this paper offer a design perspective for HOPE but not tested in Computer Vision task.

Can I apply "Nested Learning M3 algorithm" with "Scaling Vision with Sparse Mixture of Experts" 

### [[L1 vs L2 Regression and Loss Revision]].

---
### Associative Memory
is the ability to remember relationship between related abd unrelated evens/items/.... 
	ability to remember and connect ideas. 
Think of it as a dictionary, we have keys and values. *Learning is the process of acquiring the mapping.* (ie. *map the right key to value*, like human connect ideas or associating information)
![[Pasted image 20260130121818.png]]
Another update rule for the architecture and the memory that we have.



![[Pasted image 20260130122439.png]]
The init params try to compress the context while the inner loop try to adopt/learn some of the context using gradient descent. 
	-> Linear Attention is a form of 2 levels optimization problem, 1 is the Training process and 1 is the Adoption of the memory to the context.  
![[Pasted image 20260131091404.png | 444]]


### MIRAS: A General Framework for Designing Archirectures
![[Pasted image 20260130122855.png]]
**Memory Architecture ->** compress the context into their params. More powerful architecture more Memory you have. 
**Attention Bias ->** Internal Objective that Measure the Quality of Mapping. 
**Retention Gate ->** How do you want to retain the knowledge from the past e.g. do u want forget gate or retain all the information in the past ?  
**Memory Algorithm ->** How do we want to learn the internal process ? Do we want GD or more powerful algo like GD with momentum or even a non-parametric solution like Softmax Attention ? That another Design choice. 

### Modern Architecture as Associate Memory
![[Pasted image 20260130124249.png]]

![[Pasted image 20260130124229.png]]
**Oja rule -** improve the Hebian rule that discussed by adding the regularization term 
**Omega rule -** objective agnostic
	"objective-agnostic" mean a algo operates independently of any spectific goal, predefined target or optimization criteria. For example, a Flexible Optimization algorithm that adapt through click-rate and likes to promote best selling product.
-> Insted of optimizing the current state of memory of the key and values like Kt and Vt it optimize the memory for a local window of the past keys and values. 
-> Not online learning, bc it need to map some of the past keys and values. Note: online learning mean only learning new/up-to-date knowledge without past knowledge.
+ $ Like Sliding Window Linear Attention: Instead of just updating the mem w.r.t $V_{i,}K_{i}$ we update to a past set of keys and values.
+ ? What online and offline learning in this slide mean ? Why the architecture related to online and offline ? Isn't its just data, not architecture ?

### Optimization and Backpropagation: A Preliminary Example
![[Pasted image 20260130125843.png]]
+ ? Explain the second $W_{t+1}$ equal to ... wth $u_{t+1}= \dots$
	-> Backprop is a form of Associate Memory that map its input to the Error rate that it receives for the backprop process. 

### Nested Learning
![[Pasted image 20260131155857.png]]
$f$ as update frequency
![[Pasted image 20260201145601.png]]
*Another Example:* Distillation create 2-levels learning structure where a small student network acts as an inner learner distilling knowledge from a larger teacher network (the outer learner)

+ ? Explain all 3 Definition Here
![[Pasted image 20260131155842.png]]
Nested System: 
	Each block have its own gradient flow, locally solve a new problem that we define based on an Optimization process and Objective  
+ regularization tại thời điểm $t$: trọng số mới không khác biệt quá nhiều.  

### Nested Learning: Knowledge Transfer
**How levels can be Inter-connected ?**
![[Pasted image 20260131160629.png]]
**Direct Connection of Levels (Prametric):**
	A simple Way is to Conditioning of the output of the Outer Loop (slow network) based on the computation of the inner loop, that 1 way of knowledge transfer. 
	State of $M_{t}$ compute within the inner-loop.
-> Fast-Level: Linear Attention. Slow-Level calc Attention QKV.


**Direct Connection of Levels (Non-Parametric)**
e.g. Attention in Transformers
![[Pasted image 20260201152121.png]] 
The Attention layer don't have any updatable parameters but the output of the general model depends on the context in the inner loop of the attention. 

**Knowledge Transfer via Backpropagation**
Backpropagation
2-level variant recovers MAML
	two levels  the the slow network can learn the initial state of the fast network and so it's equivalent to the model agnostic meta-learning.

![[Pasted image 20260201152442.png]]
Nested Learning can be see at the
+ level on the architecture side (Context is the Token)
+ level on the optimization process (Context is the Gradient generated by the Architecture)

### Implication: Optimizers
![[Pasted image 20260201152650.png]]


![[Pasted image 20260201153613.png]]
+ ! Projection layers are fixed similar to MLP block. 
+ $ Self-Referential, every single part of the model is adaptive. Changing based on the context and also it's updated through the context. (Not persistant and fixed)

![[Pasted image 20260201154044.png]]
+ ? Update more caused Catastrophic Forgetting -> Leave the memorization to the Slow Frequency Layer and focus updating on the Fast Frequency Layer. 


