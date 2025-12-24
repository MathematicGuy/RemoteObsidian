## [[Continous Learning Survey]]
**Continous Learning -** Learn new information continously without forgetting old information.
**Memory Hiarchy:** Cache or Intermediate Memory (RAG) -> Long Term -> Pernament (Continous Learning).

## [[Continous Learning and Catastrophic Forgetting]]

## [[Continous Learning vs RAG in solving Catastrophic Forgeting]] 
+ ? Why they are not substitutes.
+ $ **Want the model remember new infors directly (ie. update its params)**. *RAG* is just a tool for retrieving new infors, *retrieving too much then we started to have A PROBLEM called hallucination.* Yes, **RAG can be use as a 2nd Brain but there're limitation**.

## Nested Learning
**Nested Learning -** new ML paradigm (eg. Google HOPE architecture) by structuring models as **nested optimization problems with different update speeds**, *mimicking brain memory* to prevent catestrophic forgetting and build **"living memory" for AI** (*good at Needle in a Haystack* problem). 
	Inspired from the brain's layered memory consolidation (*fast for short-term*, *slow for long-term*)
![[Pasted image 20251223091039.png]]


**All NN are associative memory system** that compress their own context flow. 

**Gradient Descent with momemtum** is indeed a **low-level optimization process**, where the memory is optimized by simple gradient descent algorithm. 



