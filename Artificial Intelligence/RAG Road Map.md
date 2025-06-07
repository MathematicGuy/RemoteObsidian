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


### [HCM AI - AIO Custom Course](https://drive.google.com/drive/folders/1TAWPTAE2QavFTYvNkn7P4K0gitfCJnIC)

### Here's a 9-hour crash course curriculum for learning to build LLM applications. All resources are free (Thay Dong recommendation)
𝗣𝗔𝗥𝗧 𝟭 - 𝗔 𝗚𝗘𝗡𝗧𝗟𝗘 𝗜𝗡𝗧𝗥𝗢 𝗧𝗢 𝗟𝗟𝗠𝗦 (1h 30m)
Intro & overview of language models, next-word prediction, embeddings, cosine similarity, semantic search
Resources: 
📺 30m: Simple Introduction to LLMs (Matthew Berman) bit.ly/4bBzsOn
📖 40m: A Very Gentle Introduction to LLMs without the Hype (Mark Riedl) bit.ly/3x7g1xD
📺 10m: How do LLMs work? Next Word Prediction with the Transformer Architecture Explained (Louis-François Bouchard) bit.ly/4e553JY
📺 10m: What is Semantic Search? (Luis Serrano) bit.ly/4bUAX9O
---
𝗣𝗔𝗥𝗧 𝟮 - 𝗧𝗥𝗔𝗡𝗦𝗙𝗢𝗥𝗠𝗘𝗥 𝗔𝗥𝗖𝗛𝗜𝗧𝗘𝗖𝗧𝗨𝗥𝗘 (1h 30m)
Encoder-decoder architecture, masking, attention, transformers, GPTs
Resources:
📺 30m: But what is a GPT? Visual intro to transformers (3Blue1Brown) bit.ly/452JZQ6
📺 20m: Sequence-to-Sequence (seq2seq) Encoder-Decoder Neural Networks, Clearly Explained! (Josh Starmer) bit.ly/4c08M9z
📺 10m: The Attention Mechanism (Luis Serrano) bit.ly/4e5O75N
📺 15m: Transformer Models (Luis Serrano) bit.ly/3WYVvdj
📺 15m: Generative Pre-trained Transformer (GPT) (Databricks) bit.ly/3VmAMil
---
𝗣𝗔𝗥𝗧 𝟯 - 𝗣𝗥𝗢𝗠𝗣𝗧 𝗘𝗡𝗚𝗜𝗡𝗘𝗘𝗥𝗜𝗡𝗚 (2h 0m)
Zero/one/few-shot, chain-of-thought, self-consistency, generated knowledge, prompt chaining, ReAct
Resources:
📺 60m: Prompt Engineering Overview (Elvis Saravia) bit.ly/3V3FIXV
📖 90m: Prompt Engineering Guide (DAIR) bit.ly/3Pf1dCV
📖 30m: Brex's Prompt Engineering Guide (Brex) bit.ly/3V2elO6
⚒️ 0m: LangChain Hub bit.ly/4c0wpiw
---
𝗣𝗔𝗥𝗧 𝟰 - 𝗖𝗛𝗔𝗜𝗡𝗜𝗡𝗚, 𝗥𝗔𝗚, 𝗩𝗘𝗖𝗧𝗢𝗥 𝗗𝗕𝗦, 𝗔𝗚𝗘𝗡𝗧𝗦 (2h 30m)
Langchain, RAG, vector databases, LlamaIndex, Open AI functions
Resources:
📺 30m: The LangChain Cookbook - Beginner Guide To 7 Essential Concepts (Greg Kamradt) bit.ly/4e2ozX9
📺 30m: The LangChain Cookbook Part 2 - Beginner Guide To 9 Use Cases (Greg Kamradt) bit.ly/4bQoMLo
⚒️ 0m: Learn LangChain (Greg Kamradt) bit.ly/455XTRB
📖 30m: Advanced RAG (Hugging Face) bit.ly/3KmzkpO
📺 5m: Vector databases are so hot right now. WTF are they? (Fireship) bit.ly/4aMqRH8
📺 10m: Question A 300 Page Book (w/ OpenAI + Pinecone) (Greg Kamradt) bit.ly/4bRGzSA
📺 20m: Talk to Your Documents, Powered by Llama-Index (Prompt Engineering) bit.ly/4bZ6K9F
📺 30m: From OpenAI Function Calling to LangChain Agents (Automata Learning Lab) bit.ly/3R8x35h
---
𝗣𝗔𝗥𝗧 𝟱 - 𝗙𝗜𝗡𝗘𝗧𝗨𝗡𝗜𝗡𝗚 (1h 30m)
Feature-based finetuning, LoRA, RLHF
Resources:
📖 15m: Finetuning LLMs (Sebastian Raschka) bit.ly/4c0JckY
📖 15m: Fine Tuning vs. Prompt Engineering LLMs (Niels Bantilan) bit.ly/3VlJWvi
📺 30m: Reinforcement Learning from Human Feedback: From Zero to chatGPT (Hugging Face) bit.ly/453p1QV
📖 15m: Complete Guide On Fine-Tuning LLMs using RLHF (Labellerr) bit.ly/3VnRA8K
📖 15m: LoRA (Hugging Face) bit.ly/4aKfr6X

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


