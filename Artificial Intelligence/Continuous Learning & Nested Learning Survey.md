## [[Continous Learning Survey]]
**Continous Learning -** Learn new information continously without forgetting old information.

**Memory Hiarchy:** Cache or Intermediate Memory (RAG) -> Long Term -> Pernament (Continous Learning).

### The Root of Catastrophic Forgetting
#### Mathematical Perspective
[[VIsualize Catastrophic Forgetting]]
Note: forgeting can be visualize using performance graph like t-SNE. 

#### Technical Perspective
 

### Continous Learning vs RAG in solving Catastrophic Forgeting 
+ ? Why they are not substitutes.
+ $ **Want the model remember new infors directly (ie. update its params)**. *RAG* is just a tool for retrieving new infors, *retrieving too much then we started to have A PROBLEM called hallucination.* Yes, **RAG can be use as a 2nd Brain but there're limitation**.


#### Continous Learning (used during training)
**Parametric memory:** infos stored inside the weight $\theta$ (ie. params) of the model.
+ @ **Intuition:** like apply technique or method to remember better e.g. Memory Palace, Systematic Thinking etc.. *biological learning*. How can I keep remember more without forget about the old stuff ?
```ad-abstract
Continous Learning tries to change the model's **parameters over time without destroying previously learned functions.** 	

**First-principle objective**
We want a single parameters vector $\theta$ that remains good at multiple historical data distributions
$$
\theta \arg \min_{x} \sum^{T}_{t=1}L_{t}(\theta)
$$

```
	
+ **What CL treats as “memory”**
	- The weights $\theta$ themselves
	- Sometimes a _small auxiliary buffer,_ but the goal is still **parametric retention**
	  
+ **Failure mode it addresses**
	- **Catastrophic forgetting**
	- *Gradient interference*
	- Loss landscape drift 
	
 + ? e.g. Imagine when tweaking each weight result in a diff outcome, learning new knowledge is exactly like that bc **learning force the model to tweaking its weight.** 	
 + $ SO fundamentally the model doesn't not "forget" anything.
(Note: could we modify so the model only tweak the right params, in other word *categorize each knowledge domain to each params independently or expand model params for new infos*)

##### RAG (used during Inference)
**Non-Parametric (external) memory:** *Information stored outside* the model, store & access live.
+ @ **Intuition:** like **Note or searching the internet**. Why remember everything internally when you could just look it up ?
```ad-abstract
RAG avoids modifying model weights and instead **retrieves relevant information at inference time**.

**First-principle objective**
We approximate:
$$p(y∣x) \approx p(y \mid x, \text{retrieved context})$$
instead of encoding all knowledge into $\theta$.
```
	
+ **What RAG treats as “memory”**
	- A vector database / document store
	- Embeddings
	- Retrieval index
	
+ **Failure mode it addresses**
	- **Model knowledge cutoff**
	- *Hallucination*
	- Static parametric memory (Model stay the same, just interact with new information sooooo if the model is stoopid, this doesn't help)

#### In Some Context RAG should be use With CL and Some are Not
**RAG System: RAG + Continual Learning (analogy: Better Note + Better Brain)**
+ RAG handle fast-changing live knowledge
+ CL updates model Attention to relevant infos better base on new given knowledge:
	+ Retrieval embeddings
	- Routing policies
	- Scoring functions
	- Perception modules
	- Preference models 

**Action recognition / vision** -> CL is mandatory while RAG is irrelevant. Because there litlte document to retrieve in human behaviour.  
**Fraud detection** -> CL for non-stationarity, RAG for rules/history.
+ @ So to conclude:
	+ *Continous Learning* is about *how the brain changes*, aims to *improve model learning capability and stability* while
	+ *RAG* is about *what the brain reads*, aims to *solves knowledge scalability* (bc there always new infos). 


## Nested Learning
**Nested Learning -** new ML paradigm (eg. Google HOPE architecture) by structuring models as **nested optimization problems with different update speeds**, *mimicking brain memory* to prevent catestrophic forgetting and build **"living memory" for AI** (*good at Needle in a Haystack* problem). 
	Inspired from the brain's layered memory consolidation (*fast for short-term*, *slow for long-term*)
![[Pasted image 20251223091039.png]]


**All NN are associative memory system** that compress their own context flow. 

**Gradient Descent with momemtum** is indeed a **low-level optimization process**, where the memory is optimized by simple gradient descent algorithm. 



