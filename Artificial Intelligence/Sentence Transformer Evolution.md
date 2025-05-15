![[Pasted image 20250325160344.png]]

+ ? RNN fail to understand the real meaning of word due to it fail to understand the sentence as a whole.  
 + ? Even when Bidirectional RNN try to address this, but with left and right context **learned seperately** then concatinated some of the **true context is loss**. 
![[Pasted image 20250325160446.png]]
+ ? **Transformer Networks (2017)** try to address these issue by using Multi-Head Attention and allow parallel token processing of the entire sentence. 
+ $ The Encoder layer take in entire sentence and output a encoded vector sitanuously, these encoded vector **better than RNN because they understand the bidirectional context thought Attention unit**.
+ ! Eventhough Transformer work well for sequence-to-sequence problem, to train a Transformer from scratch need a lot of data and **their architecture may not be complex enough** to solve many language **problem like Question Answering, Text Summarization, Translation, Intent Classification**.  

### BERT Networks
BERT address these concern with the ideology that **different NLP problems all rely on the same fundamental understanding of language.**  ![[Pasted image 20250326071919.png]]

BERT incluce 2 Phrases:
1. **Pre-Training:** Understand Language -> Focus on understandin g the language
2. **Fine-Tuning:** Understand Language specific task -> Focus on language specific tasks.

**Advantages over Transformers**:
+ $  So once model are train to understand text, we can just fine-tune the model for other specific task. This **solve the slow training problem where we must re-train the model from task to task.**
+ $ BERT also solve architecture complexity problem. BERT are tryly bi-directional stacks of Encoders, looking at context in both direction simultaneously. 
	Since BERT are pre-traini to be a language model, it better understand word representation. This mean that their embedding vector encapsulate meaning of words. ![[Pasted image 20250326073120.png]]
+ ! **Problem with BERT:** In Question Answering problem where BERT must compare **similarity score between Query with each Answers (i.e. most relevant Question)** though a Linear Layer (often softmax) then select the most relevant one. **This is not scalable, if there 100 million Answers** then we would need to run the 100 milion times. ![[Pasted image 20250326074750.png]]

So how do we make BERT viable (khả thi). Let's seperate the explaination into 4 Pass:
**Pass 1: High Level Idea** (intuition and solution)
+ Step 1: Convert **each existing question** to a single vector representation once. (pre-compute) 
+ Step 2: For new incomming question, convert it to a vector representation once. 
+ Step 2: Compare this new question with all previously stored question vectors using cosine similarity 
+ Step 3: Return the nerest neighbor of the most related question.
	So when a questions added we used BERT model only once.   


**Pass 2: Sentence Transformers**
+ **Step 1 : Pass new question into BERT to get a single vector that represent the question:**
	+ ? BERT only use word vector, so to convert words in sentence instead we need to find a way to aggregate these vectors. A formal way is use Mean Pooling, which is the most simple Sentence Transformer form, so the sentence it represent is really bad. (so poor that GloVe embedding may be better) ![[Pasted image 20250326081445.png]]

+ $ In order to have BERT to **create sentence vectors that actually have meaning** (i.e. encoded vector represent word really well), we need to further train it on sentence level tasks, such as:
1. Natural Language Inference (NLI)
2. Sentence Text Similarity (STS)
3. Triplet Dataset

+ $ In Quora (i.e. bog website) question setting, we would just **pass in every question though sentence transformer once and store it somewhere for future use** (in Embedding Space). 
+ ? So when a **new question come in**, we would pass it through sentence transformer to get the question vector representationa and then **determine the question with the highest cosine similarity then surface them as related**. Also we can fine the nereast neighbors. 


**Pass 3: Sentence Transformer Training**
BERT is good at Word Representation, but we want a model that good at Sentence Representation. To achieve this we fine-tune BERT one 3 sentence related task:
1. **Natural Language Inference (NLI)**: take 2 sentence and determine if 
	+ sentence A **Entails** sentence B (**A implies B**)
	+ sentence A **Constradict** sentence B (**A opposite of B**)
	+ or just **Neutral** (i.e. **Neither Entails nor Constradict** above)  ![[Pasted image 20250326082509.png]]
	+ ? To train Natural Language Inference network we use Siamese Network (2 identical Sentence Transformers using the same weights)  ![[Pasted image 20250326084326.png]]
	 + ? **Training Steps:** 
		1) If we want to compare 2 sentences, we pass them though the different BERT networks to get word representations.
		2) Then convert word representations into sentence representation using Mean Pooling. 
		3) After that, **concatinate** the **"2 sentence vectors"** and **"their difference"** as input for the Forward Pass (Neural Network)![[Pasted image 20250326084957.png]]
		4) Finally, **output is a softmax classification** which can be 1 of the 3 class **"Entail", "Constradict", "Neither**" ![[Pasted image 20250326084940.png]]
	+ ? The **dataset would just be sentence pairs with 1 of the three class labels**. So we minimize the cross entropy loss. ![[Pasted image 20250326084927.png]]
	+ $ After fine-tuning, SBERT no longer classifies directly but produces meaningful embeddings using BERT + Mean Pooling. ![[Pasted image 20250326085327.png]]
	
```ad-summary
**During Training**: 
+ We use a Siemese Network (2 identical "BERT + Mean-Pooling" models) to fine-tune the model on sentence pair tasks like NLI (Natural Language Inference)

**During Inference**:
+ We no longer need Siamese Network
+ Only 1 SBERT model (BERT + Mean Pooling) is needed to encode sentences into meaningful embeddings.  
```


2. **Sentence Text Similarity (STS)**: Given 2 sentences, rate how similar they are. ![[Pasted image 20250326085840.png]]
	+ ? STS work the same as above but use Cosine Similarity Function as output. Like other network its Minimize Squared Error Loss to train the model. ![[Pasted image 20250326085920.png]]
	 
3. **Triplet Dataset**: Includes 3 sentence per example:
	+ **Anchor** sentence: (e.g. I loves to study) 
	+ **Positive** sentence: semantically similar or related (e.g. He loves to sleep)
	+ **Negative** sentence: semantically distant or unrelated (e.g. They not like us)
	![[Pasted image 20250326090055.png]]
	![[Pasted image 20250326090159.png]]![[Pasted image 20250326091905.png]]
	+ ? This work well because **positive example closer in the embedding space whereas the negative example is distant**. Thus, **[[Triplet Loss]]. training is a classic example of contrastive learning.** 
	
+ $ **Goal:** produce **embeddings where semantically related sentences cluster closer**, and **unrelated** sentences **move apart clearly** in embedding space.



**Pass 4: Sentence Transformer Inference**


---
### [fine-tunining BERT](https://thepythoncode.com/article/finetune-bert-for-semantic-textual-similarity-in-python)

[[Fine-Tuning BERT to SBERT Documentation]]

---
# Sampling
## Temperature
Basically **Softmax** but logit $z_{i}$ divided by $T$:  $$\frac{z_{i}}{T}$$ where $T$ is the **Temperature**. Softmax fomula with temperature:
$$P_{i} = \frac{e^{z_{j} / T}}{\sum^{K}_{j=1}e^{z_{j} / T}}$$
With logits computed from the last layer are `[1, 3]`
+ When $T=1$: equivilent to no temperature, or softmax probabilities are `[0.12, 0.88]` 
+ When $T = 0.5 < 1$:  the probabilities are `[0.02, 0.98]`, so output become more bias toward higher value.
+ When $T = 2 > 1$: the probabilties are `[0.27, 0.73]`, the model seem more balancely distributed. 
+ $ The **higher temperature is, the Less likely model is going to pick the dominance** option (value with highest logit), making model's output more creative but potentially less coherent. The **lower the temperature, the more Likely the model to pick the most dominance value** -> Model become more consistent but more boring.![[Pasted image 20250326153327.png]]
+ ? Base on your need, temperature of 0.7 is recommended for creative use cases, as it creativity and determinism. But oft you should experiment to find which value suit most.

A language model work with vocab size of 100,000. Which mean the probabilities of many token can be too small to be represent. Small number might be rounded down to 0, log scale help reduce this problem.  
![[Pasted image 20250326155959.png]]


**Re-Explain:** https://huyenchip.com/2024/01/16/sampling.html#temperature
## Top-K
+ ? Top-K is a sampling strategy to reduce computation workload by only choosing k best value, making text more predictable but less interesting. Softmax require 2 passes over all possible value: 1 

