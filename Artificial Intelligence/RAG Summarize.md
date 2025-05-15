+ @ **Key Word:** layoutlm, graph rag, [NER label variation](https://arxiv.org/pdf/2312.15751), SciREX,  scientific information extraction, 


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


**NAIVE RAG (Short-Term Solution for Retrieving documents by query)**
1) INDEX
	Divide doc into meaningful chunks and store them in a vector form that can be retrieved easily, all vectors save to vector database
	 + Before read and store Docs into Vector DB, we should remove unescessary contents in the document. (e.g. white pages, some useless contents)
	   
2) RETRIEVAL
	 To know what the LLM need to retrieved, we first look at the user query. 
	 + Lexical Search: word to frequence match. -> fail to understand the semantic meaning of words.
	 + BERT model: Encoder only Transformer -> provide measurement for finding similarity in the document and the input query -> find relevant information between query and document. 
	
	Step-by-step:
	+ Create query (for query document)
	+ Reformat response 
	
	
3) GENERATION
	relevant document provided to the LLM for further processing. Yes, it replied on the LLM.
	+ LLM have to find a balance between `Following Information` and `Transform information Into a Response` 
	+ without any fine-tunning, LLM will able to response to your quesiton with RAG
	
	Step-by-step:
	+ Import llm from hugging face
	+ Add instruction Prompt, combine instruction prompt with query (e.g. "You are a ... act as a ....please answer this question" + query)
	+ Use CUDA -> Generating response 
+ [simple rag implementation with hugging face](https://towardsdatascience.com/how-to-improve-llms-with-rag-abdc132f76ac/)

**NEURAL RETRIEVAL**


+ ? **Optimization Retrieval**: 
	+ ? Leiden Algorithm to segment similar information into a cluster -> Faster retrieval using Knowledge Graph  ![[Pasted image 20250311111227.png]]
	+ ? **Top-K Retrieval:** Instead of retrieving once, Retrieves top-k results.    
	-> Make mistake much more traceble and preventable because irrelevant information can be ignore. ![[Pasted image 20250311111336.png]]
	+ ? **Optimize Response:** A Re-Writing LLM to help condense or even transform query (original infor) into key information which then transformed into vectors which again used to compare and search within in the vectors database or the knowledge graph to retrieve accurate information.
 

**Hybrid Search**
![[Pasted image 20250311111807.png]]

![[Pasted image 20250311111836.png]]


