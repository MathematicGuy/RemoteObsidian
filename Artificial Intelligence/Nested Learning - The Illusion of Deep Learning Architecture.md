NL reveals that components like optimizers and attention mechanisms are actually associative memory modules that compress information at different frequencies

**Nested Learning, a new approach to machine learning that views models as a set of smaller, nested optimization problems, each with its own internal workflow**, in order to mitigate or even completely avoid the issue of “catastrophic forgetting”, where learning new tasks sacrifices proficiency on old tasks
	nested optimization problems -> not 1 system, but a system of interconnected (multi-level learning with each level optimized a problem), that are optimized simultaneously. 

Complex **ML model** is actually *a set of coherent, **interconnected optimization problems nested within each other** or running in parallel.* Each of these internal porblems has its own context flow - its own distinct set of infor which it is trying to learn. 

**Deep Learning work by compressing their internal context flows.** allowing to build model with deeper computational depth. 

**Inspiration**
+ Human brain adapts through **neuroplasticity** - a term to describe the remarkable capacity to **change its structure in response to new experiences**, memories and learning. 
+ **Associative memory - the ability to map and recall** one thing based on another (e.g. recalling a name when u see a face, where "name" & "face" are pairs of unrelated items)


In the training process itself, specifically the *backpropagation process*, can be modeled as an *associative meory.* **The model learns to map a given data point to the value of its local error**, serve as a measure of how "Suprising" or unexpected that data point was.  
	
+ ? What does it mean to say "The model learns to map a given data point to the value of its local error"
	*"mapping a data point to its local error"* means the model is actively trying to associate **"This specific input"** with **"The mistake I made on it."**
		By *updating the weight* ($W_{t+1}$), the models is *"storing" the connection between the Specific input data and that "Error" its causes* -> By using the Weight, next time the model sees that data point (Key), it recalls the correction (Value) to adjust its behaviour. 
	-> **Weight store Connection of (Input (Key) -> Error (Value))** in a neural network. 
	
+ ? What "Local Error" mean ? 
		*Local Error is the "measure of suprise"*  (like loglikelihood loss function) -> Thus high loss/error also mean high level of unpredictable/suprise) where the "local" term say this "Error" is calculated the specific error comming back from  from the next layer. 
		
	+ **Low Surprise (Entropy)** -> The predicting datapoint is purfect, gradient (error) is zero ->  nothing to memorize to update.
		   
	+ High Surpise if the prediction is wrong, the gradient is large. 
	
+ @ **The Associative Mapping:** The goal of the training process is to treat the **input (x) as a Key** and this **gradient term ($\nabla$) as a Value**

Nested Learning paradigm *reframe the training process* of an entire deep neural network with backpropagation *as a system of parallel optimization problems* **where each layer learns to map its specific input to its specific 'local surprise signal $\nabla \mathcal{L}$'** making the entire network a collection of these processes. 

![[Pasted image 20260102215707.png | 655]]
	HOPE fills the gap with multiple blocks that update at different **frequencies**:
	**Fast Blocks:** Update every few tokens, capturing immediate context.
	**Medium Blocks:** Update every few thousand tokens.
	**Slow Blocks:** Update over millions of tokens, capturing global trends.
	
The model uses a **"self-referential"** process where it *generates its own learning rates and weight decays, effectively learning how to learn.* ![[Pasted image 20260107140348.png | 655]]
Treats optimizer as something that can learn from its own memory/history. The optimizer become the learner itself. 

The previous layer refine the next layer, its like having a mind where each layer watching & improve the one below. Just like how human learn, we don't just stop at understanding the information but keep on refining it. 

Titan (base model) - only remember what "suprise & forget the rest", it update infor only in 2 layers and limited to first-order thinking. 

HOPE - the model that learns to learn. *Automatically learns what to keep, what to remember and what to forget.* Example of memory refinement:
![[Pasted image 20260107141716.png]]

+ ? How the Titans model behave ? Also Inspired by the human brain, its prioritize storing its mark as important, in other word, titan remember what is "suprise" and forget what is routine or didn't match it expectation. This make Titan expecially good at remembering unexpected event and information while forget the usual/routine one.
	just like how our brain remember special/unusual event than normal one.  
		
Titan big limitation are its only learn at 2 levels, store knowledge at level 1 and slightly adjusted it knowledge in level 2. And have fixed update rules like other deep learning model.  

-> This is where **HOPE (Hierarchical Optimizing Processing Ensemble)** come in 
Hope keeps Titans’ “surprise-based memory,” but adds **self-modification**. 

![[Pasted image 20260107144054.png]]

![[Pasted image 20260107153315.png]]

![[Pasted image 20260107144114.png]]

Understand CMS
Understand Preliminaries Fomula
Understand Ad-hoc Level Stacking: Bridging the Old and New (_Explain how to implement this without training from scratch._)

**Final Presentation Structure:**
	Title
	abstract | main Idea 1 | explain 1 -> explain 2 -> deeper explaination   
	abstract | main Idea 2 | explain 1 -> explain 2 -> deeper explaination   
	abstract | main Idea 2 | explain 1 -> explain 2 -> deeper explaination   

**Plan: Explore (1 + 2 part) -> Structurelize**
+ Keep Explore - Write down with my own though (concrete & help transfer my ideas to other better) not copying the HIGH LIGHT. 
+ Structurelize

-----
# Nested Learning Abstract



































