**Hope**, a self-modifying architecture that surpasses existing state-of-the-art models in **long-context reasoning** and language accuracy

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
	
	What local Error mean ? 
		*Local Error is the "measure of suprise"*  (like loglikelihood loss function) -> Thus high loss/error also mean high level of unpredictable/suprise) where the "local" term say this "Error" is calculated the specific error comming back from  from the next layer. 
		
	+ **Low Surprise (Entropy)** -> The predicting datapoint is purfect, gradient (error) is zero ->  nothing to memorize to update.
		   
	+ High Surpise if the prediction is wrong, the gradient is large. 
	
+ @ **The Associative Mapping:** The goal of the training process is to treat the **input (**x**) as a Key** and this **gradient term ($\nabla$) as a Value**

Nested Learning paradigm *reframe the training process* of an entire deep neural network with backpropagation *as a system of parallel optimization problems* **where each layer learns to map its specific input to its specific 'local surprise signal $\nabla \mathcal{L}$'** making the entire network a collection of these processes. 

![[Pasted image 20260102215707.png]]



