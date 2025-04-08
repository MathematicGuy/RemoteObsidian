![[Pasted image 20250323102340.png]]
![[Pasted image 20250323102405.png]]
![[Pasted image 20250323102255.png]]![[Pasted image 20250323102313.png]]
![[Pasted image 20250323102322.png]]

# Pre-train step that set BERT from Original Encoder
### Maskes Language Model (MLM)
Mask -> hide words you want the model to predict.
+ @ Mask out k% of the input words, and then predict the masked words. (recommend k = 15%) 
+ ? In detail Masking step work as follow:
	+ Randomly select a portion of the token (15%) 
		+ 80% are replaced with `[MASK]`
		+ 10% are replaced with a random token
		+ 10% are left unchanged.
	+ The model is trained to predict the original tokens at those masked position. 
	+ This forces BERT to learn deep **bidirectional context** i.e. each position can attend to both left and right context. 
+ ? Basically teach model to guess a random masked words in a sentence, this mean maybe this time the word "man" is masked, next time another word like "milk" might be masked. This allow BERT to both learn whole sentence context and keep guess masked word at the same time.  

Why **15% masking:**
	+ **Too Little Masking** make the model too expensive to train (Because you have to train BERT to guess more)
	+ **Too Much Masking** make sentence losing its context make prediction almost impossible unless the model are pretrain before that. 
	![[Pasted image 20250323102842.png]]

### Next Sentence Prediction (NPS)
+ ! Later variants RoBERTa remove NPS and found that it was not strictly necessary for good performance. However this still a part of the original BERT. 
+ ? Learn the relationship between sentence and predict the next sentence given the first one. 
![[Pasted image 20250323112934.png]]

+ ? **BERT perform at sentence level** referring to BERT **handle entire sentences as a single unit**, rather than focusing on token-by-token tasks.
- **Single Vector Representation of a Sentence**
    
    - BERT can convert an entire sentence into a single embedding vector (often via the hidden state of the `[CLS]` token or by averaging the token embeddings).
        
    - This “sentence-level” representation captures the overall meaning or context of the entire sentence.
        
- **Sentence-Level Tasks**
    
    - Once you have a single embedding representing the whole sentence, you can perform tasks such as:
        
        - **Sentence Classification** (e.g., sentiment analysis, topic classification).
            
        - **Next Sentence Prediction (NSP)** (determining if sentence B logically follows sentence A).
            
        - **Semantic Similarity** (comparing embeddings of two sentences to see how similar they are).
            
- **Contrast with Token-Level Tasks**
    
    - BERT is also used at the **token level** (e.g., Named Entity Recognition, Part-of-Speech tagging), where the model produces an embedding for each token and makes predictions per token.
        
    - “Sentence-level BERT” generally refers to models or usage patterns that **pool** token embeddings to form one “global” representation for classification, regression, or similarity judgments over the entire sentence.

## BERT input Embeddings
![[Pasted image 20250323113014.png]]
+ $ Can be used for text classification as well. For example, classified if 2 sentence "my dog is cute" and "he likes playing" are **semantically similar**. 

+ ? How does BERT distinguish the inputs of a given pair. 
+ $ The answer is to use Segment embedding, using a seperator token `[SEP]` to annotate the spliting point of the sentence. 

### 5. Fine-Tunning BERT (after pre-trained)
#### 5.1 Task-Specific Head 
Bert can be fine-tuned to downstream taskes (sub task) by adding a small feed-forward layer or classification layer on top of the `[cls]` token representation (i.e. the 1st token in every sentence that capture the overall sequence meaning)
+ **Text Classification / Sentiment Analysis:** Apply a classifier on top of the `[cls]` representation.
+ **Named Entity Recognition:** Apply a token-level classification on top of each token's representation. 
+ **Question Answering:** Predict start and end token positions within the passage (that have most similar semantic meaning to the question)

#### 5.2 Parameter Sharing
BERT typically fine-tunes ***all* parameters** (the Transformer layers + new-specific layer (i.e. classifier)) together. This approach consistenly yields superior performance across many NLP tasks. 

### Key Advantages of BERT
+ **Bidirectional Context:** BERS uses a deep Bidirectional approach, different from left-to-right and right-to-left only model which lack ability to generalize both size context simutanuously.
+ **Strong generalization:** BERT was pre-trained on massive corpora (e.g. English wikipedia, BookCorpus) 

---
# Detail Explaination

## Transformer Architecture
### Input Embeddings
![[Pasted image 20250323141221.png]]
We define d_model = 512 to represent the size of the embedding vector of each word (i.e. Query, Key, Value)

**Why use Embedding Vectors to represent meaning of each token ?** 
+ ? If the **Embedding Vectors have been TRAINED correctly**, word with similar meaning will point at the same direction in space while word with different meaning will point at the different direction in space. ![[Pasted image 20250323141153.png]]

### Positional Encodings (PE) 
Add **Positional Embedding to each token** (like the Encoder) 
![[Pasted image 20250323141626.png]]
+ $ Only **compute the PE** **once** then **reuse them for every sentence**, no matter if it training or inference. Finally we add PE vector of the **same dimension** for each token.
+ ? **PE vector** goes as follow, 
	+ **Even** position (i.e. i % 2) use **sin**. 
	+ **Odd** use **cosine**. Then add PE vector to a sentence.
	+ Note: Use the same PE for all input sentence. 
![[Pasted image 20250323141728.png]]
	
### Self Attention and Causal Mask (Multi-head Attention)
#### Self-Attention Mechanism
note: dim mean the dimension of the vector, how many value a vector have. 
+ $ All of the showed vector are actually the representation of the whole matrix in real life. Basically each row represent a word of dim 512, 10 word in total and the whole sentence is a matrix shape (10, 512).  ![[Pasted image 20250323142617.png]]

In Self-Attention mechanism, **Query (Q), Key (K) and Value (V) are the same dimension matrix.** This allow the model to learn and relate words to each other. 
![[Pasted image 20250323143115.png]]
+ ? We calc **Raw Attention Score** by performing vector multiplication between vector Q and K to find the similarity between word (i.e. calc similarity value of a word to all word). 
+ ? Then apply softmax to convert each **Attention Score** **into a probabilty distribution.** (i.e. each token now represent the probability distribution vector between itself and every words in the sentence) This also effectively normalize all Attention Score and convert all values into 1 value range.  
+ ? Finally calculate the **Self-Attention Score** of each words by multiplying the **Distributed Attention Score** previously to **Value** V. That how we represent how much each word to all words should have.   
(please use GPT to re-explain later)


We use **Q, K, V to calculate the Attention value of each word in a sentence where Softmax apply to each token, effectively calculate the Attention Score of each word to all words in the whole sentence**  (yes, all calc can be perform sitanuously using GPU) Therefow allow the model to capture relationship among word.   
![[Pasted image 20250323143557.png]]


### The self-attention mechanism: the reason behind the causal mask
note: we will later see that BERT model Conditional Probability from both left and right context.  
+ ? **Causal Mask** aim to model **Conditional Probability**, each word should only depend on words that comes **before it** (left context) (j.e. word before China) ![[Pasted image 20250323150342.png]]
+ $ To achieve this, **simply replace all word after** with **negative infinity** before calculating softmax. In softmax, value close to $-\infty$ represent as 0, so the 1st token `[SOS]` should have Self-Attetion Score of $$\frac{e^{5.45}}{e^{5.45} + 0 + \dots + 0} = 1$$  (i.e. 100% Self-Attention Score) - (yes, $e^{-\infty}=0$$)
 + ? This way the model will not have access to any tokens after it. 
 
 When using Causal Mask, the Self-Attention Score **output dim remain the same**.
 note: each row is a vector dim 512 (i.e. 512 values) ![[Pasted image 20250323151337.png]]

## Introducing BERT
BERT's architectire is made up of layers of Transformer Encoder. 
![[Pasted image 20250323152539.png]]

+ ? Main **Differences** with Vanilla Transformer's Encoder:
	+ The embedding vector is 768 and 1024 for 2 models. (left-to-right, right-to-left)
	+ Positional Embedding **are absolute and learnt during trainng and limited to 512 position.** 
	+ The linear layer head changes according to the application. 
+ Used the **WordPiece** tokenizer, which also allows sub-word tokens. Vocabulary size is ~ 30.000 tokens.

### BERT vs GPT/LLaMA
*Unlike common language model (DECODER) like GPT/LLaMA*
1. BERT does not handle "special task" with prompt, but rather **by fine-tuning.** 
2. B in BERT stand for bidirectional, so BERT has been trained using both *left* nad *right* context.
3. BERT is not built specifically for text generation
4. BERT has **not been trained on the NTP** (Next Token Prediction) task **but rather**, on the **MLM and NSP task** mentioned above.

+ ? Example: For QA BERT you need fine-tuning ![[Pasted image 20250324102855.png]]


## Pre-Training Task:
+ ? **MLM (Masked Language Modeling)** and **NSP (Next Sentence Prediction)** are not 2 different variations of the BERT model, **they are 2 pre-training tasks used within the original BERT.** 
```txt
+------------------------------------------------+
|         Input Layer                            |
|  (Token + Segment + Position Embeddings)       |
|  e.g., [CLS] Sentence A [SEP] Sentence B [SEP] |
+------------------------------------------------+
              |
              v
+-----------------------------+
|      Transformer Block 1    |
| - Multi-Head Self-Attention |
| - Feed-Forward Network      |
| - Layer Norm + Residual     |
+-----------------------------+
              |
              v
            ... (Repeat for L layers: 12 or 24)
              |
              v
+-----------------------------+
|      Transformer Block N    |
| - Multi-Head Self-Attention |
| - Feed-Forward Network      |
| - Layer Norm + Residual     |
+-----------------------------+
              |
              v
+-----------------------------+
|         Output Layer        |
| (Final Hidden States for All Tokens) |
+-----------------------------+
              |
              v
+-----------------------------+
|    Task-Specific Outputs    |
| - MLM: Predict Masked Tokens via Softmax |
| - NSP: Classify [CLS] Token (IsNext/NotNext) |
+-----------------------------+
```

### Masked Language Model (MLM)
+ $ This model train by masking token (using `[MASK]`) and predicting the masked tokens. **Basically help model generalize language and understand context**. *kind of like human ngl*
+ ? Its randomly select a masked words in the sentence and the model must predict the right word given the left and right context.  
![[Pasted image 20250324103204.png]]
+ $ Pretraining procedure selects 15% of the tokens from the sentence to be masked. When a token is selected to be masked:
	+ 80% of the masked token replace with `[MASK]`.
	+ 10% are replaced with random words.
	+ 10% are remain unchanged.
![[Pasted image 20250324104018.png]]

#### MLM Training
+ ? MLM Training process are the quite like other model. Select a masked token, guess (using context from both left & right) then compute loss, finally run backpropagation to update the weight.    
![[Pasted image 20250324104101.png]]

### Next Sentence Prediction (NSP)
+ $ This model train to Seperate Sentences and Predict Next Sentence. Basically **help model to understand sentence relationship.** 
+ ? Model **predict if sentence A come right after sentence B or not** by labeling them: `IsNext` or `NotNext`  ![[Pasted image 20250324104815.png]]
note: remmeber BERT embedding size is 768
+ $ Given 2 predict if sentence B come after A. We need a token to **annotate seperation point between sentences** `[SEP]`, and a token to **capture the meaning of the 1st sentences** `[CLS]` (i.e. class token) to predict sentence B.   
+ ? Like token positional encoding, we do the same for sentences by adding a **Segment Embeddings** token for each sentence.  
![[Pasted image 20250324105028.png]]

#### NSP Training: Seperate Sentences
>Like Normal. Prediction -> Calc Loss -> Backpropagation 
![[Pasted image 20250324105735.png]]

+ ? To **calculate class token** `[CLS]`  in BERT, we simply **Do Not Use any Mask**. Thus allow model to **Learned All Relationship among words, specifically the Whole Sentence** (not restrictedly by word before it like before)  ![[Pasted image 20250324110139.png]]
+ @ **Methodologies:** When you asked for result you don't ask the employee, you ask the CEO.  
+ ? Output Sequence: ![[Pasted image 20250324110427.png]]


### BERT fine-tuning 
+ ! Main Different between the Original Encoder and BERT is that BERT use `[CLS}` token to capture the meaning of the whole sentence for 2 specific task: **Text Classification and Question Answeing.**

#### Text Classification: Assigning label to Text
+ ? Basically Multi-label task -> use Softmax for Loss.
![[Pasted image 20250324110751.png]]
#### Training
+ ? First we specify the `[CLS]` token, then input it to the Encoder (like normal). And pass Encoder outputs through the Linear Layer with 3 outputs features. Finally apply Softmax for prediction and calculate Loss.![[Pasted image 20250324111242.png]]

#### Question Answering: sentence A and B
![[Pasted image 20250324111520.png]]
+ $ The **first problem** "which one is the Context, which one is the Question" can be sovled easily using the segment embedding. 
1) First we concatinate the sentence and context together as inputs.  
2) Then seperate them using the separator token `[SEP]` (**like sentence prediction task**). So the Question is encoded as sentence A with the `[cls]` token, and Paragraph as sentence B.
![[Pasted image 20250324111540.png]]
 
+ $ The **second problem** is find a way for BERT to tell **where the answer starts and where it ends** in the context provided.  ![[Pasted image 20250324113327.png]]
+ ? During training: 
	- The true answer span (e.g., "Shanghai") is located in the context.
	    
	- The model is trained to predict **start and end token positions** that match this answer (purple).
	    
	- **Loss** is computed by comparing predicted positions vs. ground truth (e.g., start: TK10 → end: TK10).
		
	+ Finally **Backpropagation** to **update start and end token's weights**. 
