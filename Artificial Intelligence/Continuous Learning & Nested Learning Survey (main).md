## [[Continous Learning Research Plan Board]]

## [[Continual Learning Survey]]
**Continous Learning -** Learn new information continously without forgetting old information.
**Memory Hiarchy:** Cache or Intermediate Memory (RAG) -> Long Term -> Pernament (Continous Learning).
### [[Continous Learning and Catastrophic Forgetting]]
### [[Mathematical of Continual Learning]]

## [[When Continual Learning is useful]]
[[Continous Learning vs RAG in solving Catastrophic Forgeting]] 
+ ? Why they are not substitutes.
+ $ **Want the model remember new infors directly (ie. update its params)**. *RAG* is just a tool for retrieving new infors, *retrieving too much then we started to have A PROBLEM called hallucination.* Yes, **RAG can be use as a 2nd Brain but there're limitation**.
### [[Class Incremental Learning Survey]]

### [[Continual Learning Code]]

## Idealization

### [[Orthogonal Projection Loss (2021)]]
### [[Tree LoRA]]

### [[Nested Learning - The Illusion of Deep Learning Architecture]]
**Nested Learning -** new ML paradigm (eg. Google HOPE architecture) by structuring models as **nested optimization problems with different update speeds**, *mimicking brain memory* to prevent catestrophic forgetting and build **"living memory" for AI** (*good at Needle in a Haystack* problem). 
	Inspired from the brain's layered memory consolidation (*fast for short-term*, *slow for long-term*)
![[Pasted image 20251223091039.png]]
	**All NN are associative memory system** that compress their own context flow. 
	**Gradient Descent with momemtum** is indeed a **low-level optimization process**, where the memory is optimized by simple gradient descent algorithm. 

---

### A Comprehensive Survey of Continual Learning Theory Method Application

| Method Categories (Rank by Popularity) | Paper Count | Source |
| -------------------------------------- | ----------- | ------ |
| Replay                                 | 74          | 1      |
| Regularization                         | 28          | 1      |
| Representation                         | 31          | 1      |
| Optimization                           | 28          | 1      |
| Architecture                           | 36          | 1      |


----
**Note:** 
+ **Continual Learning Library:** Avalance vs LibContinual, when to use which.
+ Research Direction Survey proposal  
+ Team work proposal
+ Top Researcher on Continual Learning and Future Research direction for LLM
+  [Kullback-Leibler (KL) divergence](https://www.geeksforgeeks.org/machine-learning/kullback-leibler-divergence/) can be used to test Distribution shift, 
+ Why LoRA is so efficient for CL


### [[Introduction and Motivation for Continual Learning]]
Continuous learning model that handles evolving data distributions and new tasks

---

**Catastrophic Forgetting Example:**
+ Multiple fine-tunning 
+ CIL, DIL, TIL
