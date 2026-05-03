[Best RAG github Ever](https://github.com/marcharaoui/RAG-from-scratch?source=post_page-----7770fce8ac81---------------------------------------)

**Retrieval requirements for different tasks.**
![[Pasted image 20260502144923.png]]

**Chunking Strategies for RAG:** - [source](https://www.linkedin.com/posts/avi-chawla_5-chunking-strategies-for-rag-explained-share-7412102176514342913-aT9J/) 
+ Token-level Chunking
+ Semantic-level Chunking 
+ Sentence-level Chunking -> Recursive Chunking
+ Document structured-based chunking (chunk by .md header)- Assumes that the document has a clear structure, which may not be true. Length also vary. 
-> Try to combine Document Structured-based chunking with Recursive Chunking. Basically break down the problem.
+ LLM-based chunking - quality but expensive. Overkill
![[Pasted image 20260502145938.png | 555]]
Note: [Tokenizaiton vs Chunking vs Embedding](https://tech-now.io/en/blogs/chunking-vs-tokenization-a-comprehensive-guide-for-ai-practitioners)

**HyDE** - Hypothetical Document Embedding ![[Pasted image 20260502151317.png | 444]] Use LLM to Pre-Answer the User Query first. *Optionally, generated answer can be concatinate with the original Query to enhance the Query Context.* hen Enhanced Query get input to RAG.
The novelty come after the Query get embed.
1. The system retrieves docs from knowledge base using Similarity Search on this Query's Vector.
-> Identify closely aligned content with the hypothetical answer rather relying solely on the user's initial query. (increase latency)
