[source](https://weaviate.io/blog/late-chunking) - [datacamp Implement turtorial](https://www.datacamp.com/tutorial/late-chunking)
![[Pasted image 20260507182021.png]]

**Late Interaction** (embedd the entire document by token)
![[Pasted image 20260507180413.png | 666]]
Computation comparison between Naive Chunking vs Late Interation.
![[Pasted image 20260507180213.png | 888]]
+ @ Late Chunking offer a **BALANCE between COST and PERFORMANCE** in Advanced Chunking approach like Late Interaction.
+ ? Require long-context embedding model like [jina-embeddings-v2-small-en](https://huggingface.co/jinaai/jina-embeddings-v2-small-en)

To answer the query `what do customers need to prioritise ?`.
-> We need to return **both** of the above chunks for a gold standard answer. However, with the *naive approach we end up with two separate chunks that are not neighboring one another.*
-> But when we apply **late chunking we end returning the two exact paragraphs** over which the query is **most relevant.**
![[Pasted image 20260507181205.png]]

![[Pasted image 20260507181132.png | 888]]


## What this means for users building RAG applications ?
+ lessens the requirement for very tailored chunking strategies
+ **cost-effective** path forward for users doing *long context retrieval.*
+ **Simple/Testable Implementation:** can be implemented in under 30 lines of code and require no modification to the retrieval pipeline
+ *Can result in a reduction of the total number of documents required to be returned* at query time.
+ enable *more efficient calls to LLMs by passing less context that is more relevant.*