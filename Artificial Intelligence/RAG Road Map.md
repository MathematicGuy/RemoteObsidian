## Overview

```ad-abstract
RAG: improve LLM text generation capability by combining its current with external knowledge.
```

```ad-question
**LLM model often come with problem of losing context** when processing large document. Retrieval-Augmented Generation (RAG) was invented to tackle this problem by only retrieving most relevant contents as inputs for LLM instead of the whole documents. 

Thus RAG allow us to bypass LLM context window probelm.
```

```ad-seealso
LLMs are like cars, if it stands in the middle of the deep forest we can point at it and laugh at how it's stupid and how it's better to just walk through the forest.

RAG and tools (as in tool-calling for llms) are the infrastructure comparable to roads. Many people don't realize that once the "car" gets on the proper "road", it is all of sudden very efficient at what it does.

We don't faster cars (e.g. GPT-5), infrastructure is all we need right now. e.g. DeepSeek R1 architecture, o1 architecture, etc...
```

Basically **RAG = Embedding Model (Encoder) + LLM**, to comsume contents RAG, I personally encourage you to learn the *basic of RAG from the top-down then understand the math from the ground-up*, this way you both understand why do we need RAG and what RAG comprise of both intuively (top-down) & logically (ground-up).

+ ? In short, here what you need to learn. Note: `==` mean `require`.  
	+ **RAG == Embedding Model (Encoder) + LLM**. (This mean *RAG reuiqre you to learn*)
		
	+ **Embedding Model (Encoder) + LLM == Sentence Transformer**
		
	+ **Sentence Transformer == Deep Learning + Basic NLP (Tokenization + Embedding)**
	
+ ! Why do I have to learn all these stuff Thanh ? Can't I just learn RAG from Top Down, the answer is YES but NO. :)) **You surely can understand RAG but that not the point, the point is HOW DO YOU USE RAG cause RAG a architecture, this mean you modify components inside RAG, therefor by learning Sentence Transformer you automatically learn RAG as well, in my opinion ;))**

**Note:**
+ Top-Down: allow you to understand concept intuition, what it does, why we need it.
+ Bottom-Up: allow you to understand how this concept is created.
+ **Highly Recommend content is Highly Recommended ;))**

**Highly Recommend Youtuber for understanding LLM :** [Umar Jamil](https://www.youtube.com/@umarjamilai/videos)

**Prequisites for RAG** (điều kiện, kiến thức tiên quyết để học RAG)
+ [MIT Intro to Deep Learning](https://introtodeeplearning.com/) **(Highly Recommend)** **- Teach Deep Learning from the Top Down**, which **include**: 
	+ Gradient Descent
	+ Activation Function
	+ Neural Network
		+ [Neural Network Bottom Up](https://www.coursera.org/learn/machine-learning-calculus/home/welcome) (this course give you the best mathematical foundation of Neural Network, will take some time to finish)
	+ RNN
		+ [RNN Fool Proof](https://youtu.be/y9PLF2GsD-c?si=ylGbUg0h48mS77KU)
		+ [RNN Bottom Up](https://nttuan8.com/bai-13-recurrent-neural-network/) (hard to eat, but not impossible)
	+ LSTM
		+ [RNN Intro + LSTM explain in detail](https://phamdinhkhanh.github.io/2019/04/22/Ly_thuyet_ve_mang_LSTM.html)
		
	+ Attention Mechanism in a nutshell 
	+ Transformer in a nutshell
	
+ Basic of NLP: Tokenization + Embedding (no link, i'm too lazy)
+ Attention Mechanism (required before learning Transformer)
	+ [Attention Mechanism Top Down by Starquest](https://youtu.be/PSs6nxngL6k?si=hBApBNdfUgwPV_Nb)  
	
+ **Transformer** (BOSS FIGHT) 
+ ? **Transformer along with Attention is quite tricky to understand**, so I'm **recommed you to learn them from 2 different viewpoints**. Both of these video teach Transformer from Top-Down to Bottom-Up.    
	+ [Transformer by Umar Jamil](https://youtu.be/bCz4OMemCcA?si=SxKUxR3VqYe2i94C) 
		+ ? Explain Attention Mechanism + Transformer (Encoder only)
		+ $ The best Transformer explaination I've seen. No further ado, HIGHLY RECOMMEND. 
		
	+ [Transformer by Startquest](https://www.youtube.com/watch?v=zxQyTK8quyY&t=1806s) (Encoder + Decoder)
		+ ? Explain linearly, give detail & clear example but the example become quite messy as you go on. 
		+ $ Excellently Explain how Positional Encoding work. He definitly the GOAT.
		
+ [BERT by the Umar Jamil](https://www.youtube.com/watch?v=90mGPxR2GgY) 
	+ $ The best BERT explaination I've seen


**History of Sentence Transformer** 
+ ? Explain the **evolution of Language Model** from **Tradition Method** using Statistic (TF-IDF) **to Modern Deep Learning method** like RNN to LSTM to B-LSTM (Bidirectional LSTM) to Transformer to BERT to SBERT (Sentence BERT). 
	- [Sentence Transformers Explain](https://www.youtube.com/watch?v=O3xbVmpdJwU)

## RAG Explaind Intuitively & In detail
+ [Retrieval Augmented Generation (RAG) Explained: Embedding, Sentence BERT, Vector Database (HNSW)](https://youtu.be/rhZgXNdhWDY?si=4ht6ocrBjo5fEpi5)
+ [[Model in RAG (NLP and DL)]]

## Coding from ScratchTurtorial
+ [Self-Attention with Pytorch](https://youtu.be/FepOyFtYQ6I?si=zH_JweohsxzWtBA2)
+ [RAG Coding from Scratch (Coding Turtorial)](https://youtu.be/qN_2fnOPY-M?si=C4ucjMsA27Ej7Piu)


## Courses and Resources
### [HCM AI - AIO Custom Course](https://drive.google.com/drive/folders/1TAWPTAE2QavFTYvNkn7P4K0gitfCJnIC)

### [[9-hour crash course curriculum for learning to build LLM applications. All resources are free]] (Thay Dong recommendation)


---
**Vocab**
+ **holistic:** fit for all, work in general (toàn diện)

---
## Full Stack RAG
![[Pasted image 20250606131129.png]]
**Query Transformation -** Structure your input query 
+ **Multi-Query:** add more query to your base/original query.
	![[Pasted image 20250606133819.png]]
+ **Parent Document Retriever** ![[Pasted image 20250606134005.png]]

**Index -**  Adjust data structures of your embedding
+ **Multi-Vector:** like multi-query, add multiple embedding to the normal embedding like embedding for summary , custom text, hypothetical question (câu hỏi giả thuyết).  
	![[Pasted image 20250606133841.png]]

**Retrieval Methods -** Retrieve or Get your documents from the knowledge base (folder)
+ **Top-K Similarity Search:** select top 5 best documents.
+ **[[Hierarchical Navigable Small Worlds (HNSW)]]:** HNSM is the improved version of HNS which base on the concept of 6 degree of seperations, with additional of [[Skip List]] for faster search speed. 
+ **Other Methods:** **MMR** ([[Maximum Marginal Relevance]]), **LSH** (Locality Sensitive Hashing) or **IVFPQ** (Inverted File Format with Product Quantization)

**Document Transform -** Compress Context of Relevant Information from your Retrieved Docs. 
![[Pasted image 20250606133911.png]]


