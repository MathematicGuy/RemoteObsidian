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


### Optimization and Backpropagation: A Preliminary Example
![[Pasted image 20260130125843.png]]
+ ? Explain the second $W_{t+1}$ equal to ... wth $u_{t+1}= \dots$
	-> Backprop is a form of Associate Memory that map its input to the Error rate that it receives for the backprop process. 

### Nested Learning
![[Pasted image 20260201223134.png]]
Gradient-based optimizers, such as Adam, SGD with Momentum, etc., are in fact associative memory modules.
+ ? The momentum term in SGD compresses the history of gradients into a memory state to predict the next update. Therefore, an optimizer is just a learning module operating on a "context flow" of gradients

In the training process itself, specifically the *backpropagation process*, can be modeled as an *associative memory.* **The model learns to map a given data point to the value of its local error**, serve as a measure of how "Suprising" or unexpected that data point was.
![[Pasted image 20260122082909.png]]


+ ? What does it mean to say "The model learns to map a given data point to the value of its local error"
	*"mapping a data point to its local error"* means the model is actively trying to associate **"This specific input"** with **"The mistake I made on it."**
		By *updating the weight* ($W_{t+1}$), the models is *"storing" the connection between the Specific Input data and that "Error" its causes* -> By using the Weight, next time the model sees that data point (Key), it recalls the correction (Value) to adjust its behaviour.
	-> **Weight store Connection of (Input (Key) -> Error (Value))** in a neural network.
![[Pasted image 20260111202804.png]]
-> backpropagation can be viewed as an associative memory that maps each data sample to the error of its corresponding prediction

Prove backprop with momentum are 2 level associated memory.
![[Pasted image 20260111203553.png]]
Gradient Descent with momentum is a 2-level associative memory
+ The inner-level learns to store gradient values into its parameters
+ The outer-level updates the slow weight $W_{t}$ with the value of the inner-level memory
Momentum term itself is an associative memory that compress the past gradients into its parameters\


The same apply to Attention Module in Transformer with 2 layers of Linear, 1st layer for updating weight of Keys K,Q,V while the second update MLP params.
![[Pasted image 20260111204711.png]]
*Another Example:* Distillation create 2-levels learning structure where a small student network acts as an inner 
learner distilling knowledge from a larger teacher network (the outer learner)

![[Pasted image 20260110161418.png | 190]]

![[Pasted image 20260131155857.png]]
**Formal Definition:** Frequency $f_A$ is defined as the number of updates a component $A$ performs per unit of time (where one unit is typically one step over one data point).

**Ordering ($A \succ B$):** A component $A$ is considered "faster" than $B$ ($A \succ B$) if $A$ has a higher frequency, or if $A$'s computation is required to update $B$.
![[Pasted image 20260107144114.png]]

**The Gap in Deep Learning:**
    - **Frequency $\infty$ (Fast):** In a standard Transformer, Attention updates its state for _every single token_. It has infinite frequency relative to the static weights.
    - **Frequency $0$ (Slow):** The MLP weights are frozen after pre-training. Their update frequency during inference is zero.
    
**The CMS Solution:** This definition drives the **Continuum Memory System (CMS)**, which fills the gap between $\infty$ and $0$ by introducing layers that update every 10, 100, or 1,000 steps (chunks).

![[Pasted image 20260107144054.png]]


**Definition 3 talk GENERAL**
![[Pasted image 20260201223752.png]]
Intuition: **Each Levels k solve its own specific local problem based on its own speed, without straying too far from your current state.**

$$ \theta_{i, t+1}^{(k)} = \arg \min_{\Phi_i^{(k)}} \left( \underbrace{\mathcal{L}_i^{(k)}(\Phi_i^{(k)}; \mathbf{x}_{t+1})}_{\text{Term A: The Local Job}} + \underbrace{\frac{1}{2\eta_{i, t+1}^{(k)}} |\Phi_i^{(k)} - \theta_{i, t}^{(k)}|_2^2}_{\text{Term B: The Stability Constraint}} \right) $$
- **$k$ (The Level):** This represents the **frequency** or speed. A component at level $k=1$ might update every step (Fast), while level $k=3$ might update every 1,000 steps (Slow).
- **$i$ (The Component):** There can be multiple independent problems inside one level.
	e.g. Transformer Attention Head 1,2,...,N each act as a independent components $i$ 
	For example:
		**Head 1** might optimize for "Grammar relationships / Ngữ Pháp" (local context).
		**Head 2** might optimize for "Semantic reference / Ngữ Nghĩa" (global context).


$$ \mathcal{L}_i^{(k)}(\Phi_i^{(k)}; \mathbf{x}_{t+1}) $$
- **$\mathcal{L}$ (The Objective):** This is the specific goal of _this_ component.
    _Example:_ If this component is a linear layer, the goal is "minimize prediction error."
    _Example:_ If this component is an optimizer, the goal might be "minimize gradient variance."
	
- **$\mathbf{x}_{t+1}$ (The Context Flow):** This is the **data** this specific component sees.
    _Crucial Insight:_ Different levels see different data. The "inner loop" sees raw tokens. The "outer loop" sees gradients generated by the inner loop.


$$ \frac{1}{2\eta_{i, t+1}^{(k)}} |\Phi_i^{(k)} - \theta_{i, t}^{(k)}|_2^2 $$
**$|\dots|_2^2$ (Proximity):** This forces the new parameters ($\Phi$) to stay mathematically close to the old parameters $\theta_t$ Basically do not change the weights too drastically.



**Definition 4 talk Specific: Standard Gradient Descent is also Associative Memories**,
![[Pasted image 20260201223807.png]]
**Goals:** $\arg \min_{\Phi}:$ find the optimal $\Phi$ (new set of weight) becomes the new memory state $\theta_{t+1}$.

**Term A: The "Learning" Component**
$$ \langle \Phi_i^{(k)} \mathbf{k}_{t+1}^{(i)}, -\nabla \mathcal{L} (...) \rangle $$
- **$\mathbf{k}_{t+1}$ (The Key / Input):** This is the input data or signal the component just received.
- **$-\nabla \mathcal{L}$ (The Value / Surprise):** This represents the **negative gradient** (or the error signal). The paper redefines this as the "Value" or "Surprise." It tells the model _how wrong_ its prediction was and in which direction to correct it,.
- **$\langle \cdot, \cdot \rangle$ (Dot Product):** This measures alignment. By minimizing this term, the model attempts to make its output ($\Phi \mathbf{k}$) align as closely as possible with the correction signal ($-\nabla \mathcal{L}$).
- **Intuition:** "Update the memory so that when I see this Input ($\mathbf{k}$) again, I produce an output that reduces the Error ($-\nabla \mathcal{L}$)."

**Term B: The "Stability" Component**
$$ \frac{1}{2\eta_{i, t+1}^{(k)}} |\Phi_i^{(k)} - \theta_{i, t}^{(k)}|_2^2 $$
- **$|\Phi - \theta_t|_2^2$ (Proximity):** This measures the distance between the _new_ proposed weights ($\Phi$) and the _old_ weights ($\theta_t$).
- **Intuition:** "Do not change the weights too drastically." This term **acts as an anchor (or inertia),** ensuring the model incorporates the new information (Term A) without destroying everything it learned previously (Catastrophic Forgetting).

  
**Simplified:** Backpropagation is just Associative Memory.
$$ \underbrace{\theta_{new}}_{\text{New Memory}} = \underbrace{\theta_{old}}_{\text{Old Memory}} + \underbrace{\eta}_{\text{Learning Rate}} \times \underbrace{\text{Error Signal (Value)}}_{\text{Surprise}} \times \underbrace{\text{Input (Key)}}_{\text{Context}} $$
By multiplying the **Input** and the **Error** and adding it to the weights, the model "stores" the association between that specific situation and the correction needed.
-> Every layer in a deep learning model is just a memory unit updating itself to remember: _"When I see **X**, the error is **Y**."_.


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

































----
### Archive
#### Modern Architecture as Associate Memory
**Oja rule -** improve the Hebian rule that discussed by adding the regularization term 
**Omega rule -** objective agnostic
	"objective-agnostic" mean a algo operates independently of any spectific goal, predefined target or optimization criteria. For example, a Flexible Optimization algorithm that adapt through click-rate and likes to promote best selling product.
-> Insted of optimizing the current state of memory of the key and values like Kt and Vt it optimize the memory for a local window of the past keys and values. 
-> Not online learning, bc it need to map some of the past keys and values. Note: online learning mean only learning new/up-to-date knowledge without past knowledge.
+ $ Like Sliding Window Linear Attention: Instead of just updating the mem w.r.t $V_{i,}K_{i}$ we update to a past set of keys and values.
+ ? What online and offline learning in this slide mean ? Why the architecture related to online and offline ? Isn't its just data, not architecture ?
