Parametric Memor - LLM memory/knowledge stored within it param
Non-Parametric Memor - Knowledge outside of the LLM, from vectorDB or the internet. 
**Tools for each Phase:**
Indexing: 
+ [colpali blog](https://huggingface.co/blog/manu/colpali) - [colpali github](https://github.com/illuin-tech/colpali) - Extracting doc's content using VLM  ![[Pasted image 20260507142734.png | 333]]
+ [meili search github](https://github.com/meilisearch/meilisearch) - better indexing and embedding (support all type of search)  
SoTA small embedding model:
+ [jina-embeddings-v5-text](https://huggingface.co/jinaai/jina-embeddings-v5-text-small) (VI: 80.4%)



[[RAG Improvement Note]]



### FOCUS on Re-Explaining the whole RAG workflow in DETAIL
### Abstract workflow:
#### Phase 1: Indexing (similar to ETL) 
This part similar to ETL in Data Science (Extract-Transform-Load) -> the goal of this process is to transform raw document in multiple format into 1 unified format for system to Retrieved. 
**Input:** Raw Docs (text, pdf, html, csv files) 
**Output:** Chunk (ie. plain Text) and document's Metadata

1. **Document Loading (not chunking yet)** ![[Pasted image 20260507144843.png | 255]]
	**Goals:** Balance between **Signal-to-Noise Ratio** 
	+ **Content & Metadata Extraction:** process diff type of files to remove Irrelevant information while maintaining context.
		+ **Filtering Irrelevant Information -** remove unnecessary elements like page headers, footers, if u extracting a web then advertisements or watermarks -> basically *removing everything that don't contributing to the retrieval Context.*
		+ **Maintaining Context:** by ensuring structure of the document like markdown (header, paragraphs, list remain, headings, tables) remains intact -> retain the original meaning and flow of the content *-> Super important for effective retrieval and generation.* 
		+ Note: cleaning might involve removing repetitive content in legal docs or summarizing data-heavy table while keeping essential details intact.
	+ $ -> Remove Irrelevant, Compress Information while preserving original meaning and flow of the content.
	+ ? `metadata` is super important for Pre-filtering feature. e.g. if the user ask "what the company_nam 2024 revenue ?", the system could filter the answer right aways or scope down the retrieval search space to increase accuracy. 
	*Code Note:* extract docs -> inspect docs structure -> add docs's meta data and content into Dictionary
	
2. **Chunking (Text Splitting)** -  split docs into multiple sub-document call chunk that fit LLM context window. If do right, chunking help retrieved context retains meaning, coherence and relevance. Let explore some Chunking Strategies:	
	**Naive Chunking:** split texts into chunks ![[Pasted image 20260507164432.png | 555]]
	+ *Fixed-size chunking:* brute-force chunking, chunk text by its length -> light computation but break coherant if the text is long and awkwardly split ideas mid sentence. 
		-> bruteforce baseline. quick and simple, but low acc.
	+ *Recursive chunking:* chunk text by document structure like chunk by doc's heading, paragraphs or subsections as a chunk. Markdown and HTML naturally structure it content 
		-> *Document-based chunking easily preserve structure docs original* meaning and coherant but may struggle to create manageble, meaningful chunks for plaintext/un-structure.  
	+ **Semantic chunking:** this method split text into sentence, embedding them and merging sentence with high semantic similarity into chunks. This ensures each chunk have highly related contain and cohesive. 
		-> Computation intensive but excels at preserving context and relevance.
	
	**Advanced Chunking:** **address "loss of context" challange in Naive Chunking** by Enrich each chunks with additional context. In this part, we'll explore three advanced approaches for chunking and indexing: Contextual Retrieval, Late Interaction, and Late Chunking.
	+ *Contextual Retrieval (by Anthropic)* - Enrich each chunk using LLM with additional context using the ENTIRE document. 
		+ $ improve Embedding quality with document-wide context. ![[Pasted image 20260507164812.png | 700]] 
		+ ! Resource and Storage-Intensive. Because LLM for each chunk over the whole document context. High Storage Demand, not practicle for large-scale use.
	+ *[[Late Chunking]] (by Jina AI):* 
		+ $ embedding the entire docs first then splitting it into smaller embedding chunks after retrieval -> ensure each chunk retrains contextual infor from the surrounding text -> *Effective for handing long doc (like research paper)*, require long-context embedding model. late chunking reduces dependence on perfect semantic boundaries, with even basic fixed-token segmentation outperforming naive chunking with semantic cues. ![[Pasted image 20260507171347.png]] 
		+ @ **Late Chunking strikes a balance between precision and resource efficiency**, making it a versatile option.
 

3. **Embedding (Semantic Structure)** - good embedding model don't just convert text into vector. It capture the True context within the text, preversing it meaning. 
![[Pasted image 20260507151136.png | 600]]
*-> Fine-tuned* embedding model *capture the nuances and intricacies of a particular field.*
![[Pasted image 20260507163204.png | 600]]


(Additional Read: [Milvus - Impact of Embedding Dimension and Index type on the Vector Store performance](https://milvus.io/ai-quick-reference/what-is-the-impact-of-embedding-dimension-and-index-type-on-the-performance-of-the-vector-store-and-how-might-that-influence-design-choices-for-a-rag-system-requiring-quick-retrievals))
3. **Indexing -> Structure unorganized Embedding** data a new data structure for faster and more effective search. Like instead of search value by value, we first search the top group that contain the value, then the middle group,..., then the value itself. This is the same as human searching for content within a book, we don't index the text right away, we search for the book by content type (math, literature, stem, etc...), then the book by title, then the book's header, then the content itself.  
	+ @ Answer the question, I know that Chunk's embedding group into clusters by similarity, so what is the most efficient way to search the Query within those embedding clusters.
	+ ! Without indexing, the system would have to scan every document in its entirety whenever someone asks a question. You coudn't compare similarity between Q to every Chunks. Indexing help organized the embedding into group and apply algorithm for faster and more efficient search. 
	+ $ Essential VectorDB indexing in RAG is about **creating a searchable structure** that map embedding vectors to their raw data.  
	+ ? For example, instead of search for the vector most similar to 'Queen', you first identify which cluster the query belongs to and then search within that cluster alone. Indexing example using Meta's HNSW: ![[Pasted image 20260507160136.png | 555]] 
	Basically, Instead of 1,000,000 comparisons, *HNSW (like search in K-Mean but better)* might only perform **~50-100 comparisons** to find the answer.
+ Reference: [best practice for RAG indexing](https://www.meilisearch.com/blog/rag-indexing)
+ Note: [[Best Practice for RAG Indexing]]
	
4. **VectorDB** (support scalability, real-time, metadata filtering). Core feature of VectorDB. ![[Pasted image 20260507171959.png | 666]]
	VectorDB process data in 3 steps: 
	1. **Apply Structure to Embedding Clusters:** First it indexes embeddings using advanced structures such as HNSW graph or product quantization (PQ) -> optimized for high-dim data.
	2. **Query by structure using similarity search:** During query, identifies vectors most similar to the input using similarity search like Cosine Similarity, Dot product or Euclidean distance (So indexing is about Indexing with Structure).
	3. **Refined Search Results:** Searched results are refined by combining vector relevance with metadata-based filter giving highly accurate and context-aware outputs. 
	
	**Type of Similarity Search in Retrieval:**
	+ **Keyword Search** like TF-IDF (Term Frequency-Inverse Doc Frequency) or BM25 rank doc based on the important and frequency of terms.  
		Example: _A query containing “Excel” ensures documents explicitly mentioning “Excel” are prioritized._ 
		-> This search type ultilize *spare vector*  which are *numerical representation of text where each dimension represents a specific word or feature, if a feature not include it have value of 0.* (the same as one-hot encoding)
		
	+ **Semantic Search** use embedding model. Find semantically similar matches even when exact terms are absent. 
		Example: _A query like “team collaboration software” could retrieve results such as “tools for remote teamwork” by identifying semantic similarities even if exact words differ._
		
	+ **Hybird Search (Keyword + Semantic)** It uses a weighted balance between BM25 and semantic embeddings to deliver contextually relevant results while preserving the precision of keyword matching. 
		*Semantic Search* ensures context and intent are captured.
		*Keyword Search* guarantees critical terms are not overlooked.
		![[Pasted image 20260507174451.png | 700]]
	+ ? Example: A query like “Excel formula not calculating after update” benefits from hybrid search:
		-> Semantic search retrieves content about general calculation errors or updates.
		-> Keyword search ensures specific terms like “Excel” and “formula” are not missed.
	+ $ Final Score calculated as $$\text{Final Score}=(\text{Keywrod Score} \times \alpha)+(\text{Semantic Score}\times(1-\alpha))$$
		
	+ **Filtered Vector Search** - combines vector similiary search with metadata filtering to refine the results. Filtering step can be applied *before or after the vector* search rather than combining vector and keyword searches simultaneously. 
		+ ? Example: Imagine searching for product recommendations.
		-> Metadata Filter: Narrow results to products in the “electronics” category and created after 2020.
		-> Vector Search: Find items most similar to a given query (e.g., “wireless headphones”).

#### Phase 2: Retrieval
1. **Query Procesing**
	*Multi-Query* use LLM to decompose the Main Query into Multiple variance Sub-Query (like *asking Question for 1 Problem in multiple Perspective)*  ![[Pasted image 20260507183135.png]]  
	*HyDE (Hypothesis Document Enhancement)* request the LLM to give a Hypothetical Answer for the question first, then use Vector Embedding of this Hypothetical Answer for searching -> Help lessen the distance between "Question" and "Document that contain the Answer." ![[Pasted image 20260507183450.png]]
	1. **Similarity Search** use Hybrid Search then RRF (Reciprocal Rank Fusion) which is a post-processing algo that combine score from Vector/Key-word Search (BM25, TF-IDF) and Semantic Search (HNSW structure + Cosine Similarity search) ![[Pasted image 20260507184024.png]]
	
2. **Re-Ranking** 
	+ ! Problem: *top-k* retrieved docs we get above is not entire accurate bc they just *compressed information.* ![[Pasted image 20260507190925.png]]
	-> To ensure relavency we use a a DL model (Cross-Encoder) to score *Relavency Score between the Question and the Top-K Retrieved Docs.*  
	**Why ?**
	+ Bi-Encoder (in Indexing/Retrieval step) encode Question and Docs into 2 INDEPENDENT vector 
		-> fast but loss the contextual meaning and Semantic meaning between Question and Docusment (ie. question evidence).  
	+ Cross-Encoder (in this Re-Ranking step) **encode both the Question and the Docs SIMUTANEOUSLY** (like a human checking question and document). 
		-> **Allow direct evaluation: if a document answers the query.** Cross-Encoder concatinate question and document into 1 single sequence (e.g. `[CLS] Query [SEP] Document`) so every token in the query to "attend" to every token in the document in every layer of the transformer. 
		-> Allow the model to understand relationship between Cause-n-Effect dirrectly.  
		-> Applied to a small subset (25-50 docs) from the Top-k Retrieved doc to balance computation speed and high precision.
	+ $ **Bi-Encoder is Extremely slow but offer Reliable "Similarity Score"**, so it more resonable/effective to use it in the Retrieval Step ie. only compute similarity between the query with Top-K best document pair. 
	+ @ **Funnel Shape Strategies:** Retrieve top-50 docs by similarity (not so relavant/reliable) -> Re-Ranking to get Top-5 Most Relavant Docs with Cross-Encoder -> Input top-5 relavant docs to LLM. Help balance between performance and accuracy.  ![[Pasted image 20260507190950.png]]


#### Phase 3: Generation
1. **Context Preparation** 
	+ Context Stuffing: Combine top-k relavant docs into 1 single doc.
		+ ! Long Input and Increase Latency. Basically Unprocessed/Unstructured/**Un-Concise Input** -> Too much Inrrelavant information make LLM hallucinate. 
	 + **Context Selection & Compression:**
		+ $ **Context Selection,** based on LLM *"Loss in the middle"* problem, which make *LLM focus on the PROMPT FIRST & LAST* information so they forget the content in the middle. ![[Pasted image 20260507191549.png]]
		+ $ **Context Compression** use a small LLM or fine-tuned SLM to summerize the main ideas before input them into the Main LLM. ![[Pasted image 20260507191809.png]] 
	
2. **Prompt Engineering** - good context but bad prompt still result in a bad output. Here a few practice in Prompt Engineering. 
	*Zero-shot Prompting:*  Use a structure Prompt Template to Guide the LLM ![[Pasted image 20260507191925.png | 666]]
	*Few-shot Learning:* give a few example of your idea context-question-answer for the LLM  ![[Pasted image 20260507191935.png | 666]]
	*CoT (Chain-of-Though) Prompting:* guide the LLM to think step-by-step base on the given context (Show the LLM how to thing and reasoning) ![[Pasted image 20260507191946.png | 666]]
3. **Generation & Attribution**
	Compare to Regular LLM, RAG offer superior **reliability** since you could **Cite the Source.** To achieve this, we could: 
	+ Ask the LLM to cite the source directly base on the metadata within the Retrieved Chunk -> *Easier to Verify* if the Answer is True or Not. Reduce Risk and help to track Hallucination.
![[Pasted image 20260507192325.png | 777]]

## What is the Consequences if this Component Removed (Constractive Learning in Human)
Scenario 1: Remove Embedding model -> what is the Consequences)
Scenario 2: Remove Vector Store/ANN Indexing -> what is the Consequences)
Scenario 3: Remove the LLM :))) -> what is the Consequences)
Scenario 4: Remove Embedding model -> what is the Consequences)

## Code Documentation




**Trick** - reference: [best practice for RAG indexing](https://www.meilisearch.com/blog/rag-indexing)
	*Alway start with clean and meaningful data:* Never dump everything into the index. Remove duplicates and filter out low-value text, such as headers, navigation menus, or disclaimers. Cleaner input means cleaner retrieval and fewer irrelevant matches later.  
	Chunk by meaning not fixed lenght
	use Hybrid Search (combining keywords and vectors)
	always use metadata (good tags make datafiltering more powerful) try to use tags such as document source, type, date, section or access level -> help narrow down result quickly and stay grounded.  

Note: finally, design a RAG pipeline by yourself.

---
# Evaluation RAG System Design






