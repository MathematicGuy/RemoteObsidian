Usually the retrieval part. It's may be wrong or duplicate due to semantic search strategy looking for most similar docs, or only part of them is wrong leading to wrong replies. 
![[Recall_Precision_in_RAG_Diagram.png]]
>Precision and Recell in Document Retrieval are similar to Machine Learning, that is when you retrieves more information than the amount of relevant information your knowledgebase have to offer. 




There are *multiple complex factors in real-life documents contributes to the decrease in overall retrieveal accurary*, so various techniques are created to counter these issues:
1) **Long Documents**
	+ **Problem:** LLM context windown, token limitation, computing power lead to difficulty in processing and retrieving information from lengthy docs.
	+ **Solutions:**
		+ Chunking options:
			+ Sentence-based chunking
			+ Paragraph-based chunking
			+ Statistical chunking (see: [03_semantic_chunking.ipynb](https://github.com/guyernest/advanced-rag/blob/main/03_semantic_chunking.ipynb))
			  
		+ Hierarchical retrieval (e.g. parent-child chunk)
		+ Contextual retrieval 
		  
2) **Mismatch Between Questions and Document Formats:** 
	+ **Problem:** User queries may not align with the way information structured in docs.  
	+ **Solutions:**
		- Hypothetical Document Embeddings (HyDE)
		- Reverse HyDE (see: [04_reverse_hyde.ipynb](https://github.com/guyernest/advanced-rag/blob/main/05_reverse_hyde.ipynb))
	
3) **Domain-Specific Jargon** (thuật ngữ chuyên ngành)
	+ **Problem:** General LLMs may struggle with specialized vocabulary (such as coding syntax, mathematic fomular, specialized term)
	+ **Solutions:** 
		+ Incorpoerate domain-specific embeddings (see: [02_embedding_model.ipynb](https://github.com/guyernest/advanced-rag/blob/main/02_embedding_model.ipynb))
		+ Hybrid Search *(leverage keyword-based and sementic search technique)* (see: [06_hybrid_search.ipynb](https://github.com/guyernest/advanced-rag/blob/main/06_hybrid_search.ipynb))
		+ Fine-tune Embedding Model on domain-specific corpora. 
	
4) **Complex Documents**
	+ **Problem:** Handling docs with complex structure, like scanned documents. `e.g. use 1 model to describe the image, 1 model for retrieval.`
	+ **Solutions:** 
		+ *Multi-model retrieval* (see: [07_multimodal_pdf.ipynb](https://github.com/guyernest/advanced-rag/blob/main/07_multimodal_pdf.ipynb)):
			+ 1 Model for extracting information from images and other non-textual element within documents. 
			+ Integrate this information in RAG for more comprehensive serach capability.


![[506396273_687079714199523_2910371698844386261_n.jpg]]


---

**Problems:**
+ Spacing 