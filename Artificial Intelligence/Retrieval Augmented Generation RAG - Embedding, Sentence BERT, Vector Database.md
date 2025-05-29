# Intro to Large Language Model
![[Pasted image 20250324120456.png]]
![[1Qww2aaIdqrWVeNmo3AS0ZQ.png]]

### What is the language model ? 
![[Pasted image 20250324120930.png]]

### How do we train and inference a Language Model ? 
**Training**
+ ? Often trained on a large corpora of text (i.e. collection of document). Often LM aer trained on the entire Wikipedia and million of web pages. This allow the model to acquire as much knowledge as possible. 
note: We usually use a transformer-based neural network as language model.

**Inference**: for decoder model like ChatGPT, we use prompt and let the LM generate the rest by iteratively adding tokens. ![[Pasted image 20250324121228.png]]
+ ! **You are what you eat.** Model can only output text and information that it trained upon.  To teach new concepts, we need to fine-tune the model. 

### The cons of fine-tuning
+ Can be **Expensive**.
+ That why **number of parameters of the model may not be sufficient to Capture All the knowledge we want to teach** it. That's why Gemini was introduced with 2B, 7B and 25B.
+ **Fine-Tuning is not additive. It may replace existing knowledge** of the model with new knowledge. e.g. a heavily fine-tune japanese language model originally trained on English may "forget" English as it 1st language. *:)) sound like human*

That where Prompt Engineering is needed. It is possible to "teach" a language model how to perform a new task by playing with the prompt. e.g. "few-shot" prompting:
![[Pasted image 20250324134457.png]]

### QA with Prompt Engineering
+ ! Require a lot of tokens. 
![[Pasted image 20250324134721.png]]

### Pros of fine-tuning
+ $ Higher quality results compared to prompt engineering. 
+ $ Smallar context size (input) during inference since we don't need to include the context and instructions. 

# RAG pipeline
## QA with RAG 
**Store Knowledge Step**
1) Retrieve large collection of text from Documents, Web Pages. Then split into chunks. 
2) Embedding such that each vectors capture the meaning of each sentence. 
3) **Store** all Embedding vectors to a Vector DB.

**Query Step**
4) Embed query and perform **Search** over the Vector Database. 
5) Select **Top-K** result.
6) Output the Context. 

**Prompt Step**
7) Create a Prompt Template like in Prompt Engineering.  
8) Then we paste the Query and the Context to the Prompt Template. 
9) Feed LLM the whole Prompt Template to get the Answer.  
![[Pasted image 20250324143508.png]]

# Word Embeddings
### Why do we use vectors to represent words ? 
+ ?  Since **vectors can capture similarity & differences through space**, with word embed as vector, we hope to see angle between words with similar meaning is small while angle of word with diff meaning is big. So embeddings **"capture"** the meaning of the words. 
+ $ If the embedding model have been train correctly, its can capture word meaning though space as we wanted. 
![[Pasted image 20250324144159.png]]


note: lead from RNN, LSTM to Transformer 
### Word Embedding: the ideas
+ ? With **synonyms tend to occur in similar context** (surround by the same words) 
	+ For Example: "professor", "teacher" usually appear around "school", "univeristy", "lecture", etc.. 
+ $ The inverse can also be true: **words that occur in the same context tend to have similar meanings.**  This called distributional hypothesis (giả thuyết phân phối)
+ $ This mean to **actually capture the meaning of word, we also need access to its context** (i.e. text surround it)  
+ @ This is why we employ the **Self-Attention mechanism in the Transformer model to capture contextual information** (thông tin ngữ cảnh) for every token by relates every token to all other tokens in the sentence. 

### Word embeddings: the Cloze task 
+ ? **Cloze task:** bài điền vào chỗ trống. Basically given the context, what is the word in the blank. ![[Pasted image 20250324150228.png]]
+ $ This is how we train BERT: we want the **Self-Attention mechanism to relate all the input token with each other**, **so that BERT has enough information about the "context" of the missing word to predict it**. ![[Pasted image 20250324150404.png]]

### Sentence Embeddings 
+ ? BERT can also do Sentence Embedding. 
![[Pasted image 20250324150445.png]]

### Sentence Embedding Comparison
+ $ Embedded vector in space compare using cosine similarity to **measure the cosine of the angle between the 2 vectors A & B** A **smaller angle results in a high cosine similarity score** while **bigger angle result in smallar cosine similarity.** With that in mind, we can find the most relevant answer to the our query.   
	+ **Q:** "how many parameters was there in grok-0 ?"
	+ **A:** "talk about how many parameters in grok-0"
	![[Pasted image 20250324151424.png]]
+ ? **A questions rise**: **nobody told BERT** that the **embeddings** it produces **should be comparable with the cosine similarity** (i.e. 2 similar sentences should be representd by vector pointing at the same direction). **How can we teach BERT to produce embedding vectors that can be measure using similarity** function like **cosine**. 

# Introducing Sentence BERT (SBERT)
![[Pasted image 20250324152318.png]]

**SBERT using Siamese network architecture** can be **though of a single model with the same configuration and weights shared** across sevaral parallel inputs. (**2 model 1 parameter**) 
![[Pasted image 20250324153249.png]]
+ $ **Sentence BERT: architecture** 
![[Pasted image 20250324160954.png]]
+ ? Note: you can use **mean-pooling** for Sentence Embedding *or* `[cls]` token. And apply a linear layer after pooling to reduce the size of the embedding vector. e.g. 765 to 512. 

### Strategies to teach new concepts to LLM
![[Pasted image 20250324161705.png]]

### Vector DB
Vector DB **stored embedding vector in fixed dimensions** such that we can then **query the database to find all the embeddings that the closest to a given query using distance metric** (e.g. cosine similarity, euclidean distance). The **database uses a variant of the** KNN (K Nearest Neighbor) algorithm  or another similarity serach algorithm.
+ Vector DB also used for finding similar songs, image or product. 
![[Pasted image 20250324161825.png]]

### K-NN: a naive approach
+ ? Comparing query with all vectors in VectorDB then sorting them by distance, only keeping the top K.
+ ! This approach is not scalable, if there are N embedding vector, each has D dimensions the computational complexity is **O(N * D), too slow.**
![[Pasted image 20250324162426.png]]

### Hierarchical Navigable Small Worlds (HNSW) 
+ ? **Trade Precision for Speed**. HNSW is an evolution of the Navigable Small Worlds algorithm for **Approximate Nereast Neighbor**, which based on the concept of **Six Degrees of Seperation**. 

+ ? Six Degrees of Seperation: ![[Pasted image 20250324163339.png]]

HNSW in real world ![[Pasted image 20250324162950.png]]

+ $ **Navigable Small Worlds** algorithms build a graph that mimic six degress of separation by **connects close vectors with each other but keeping the total number of connections small.**  e.g. every vector can connectd up to 6 other vectors. ![[Pasted image 20250324163651.png]]Where each Node represent a Text

### Nagivable Small Worlds: idea 1 searching for K-NN 
+ ? So how to we query in this graph.
+ $ **Goals:** find the node that is most similar to the query.
	1) Randomly chosen a entry point (as the best node).
	2) **Compare similarity of the query and chosen node**. and all of its **neighboring node**. 
	3) If one of the friend node have **better similarity score, we MOVE the "best node" there**.  (e.g. node 2 have better similarity score so move to node 2)![[Pasted image 20250324164037.png]]
	4) **Repeat until all the friend nodes don't have a better similarity score** than the best node.  ![[Pasted image 20250324164216.png]]
+ ? For inserting a new node, we **query for best node then connect the new node to the top k**. (Like above but connect to best node).

#### HNSW: idea 2 
![[Pasted image 20250324165235.png]]
Learn Skip List to understand this. 

### HNSW: idea 1 + 2 Hierarchical Navigable Small Worlds
![[Pasted image 20250324171413.png]]
+ Repeat the search with randomly chosen starting points (on the top layer) and then keep the top K among all the visited nodes. 



