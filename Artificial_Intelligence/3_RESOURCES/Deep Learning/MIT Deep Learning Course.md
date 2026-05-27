### [MIT Introduction to Deep Learning](https://www.youtube.com/watch?v=alfdI7S6wCY&t=19s)

A base function represent a Straight Line. Activation funciton introduce non-linearities into the network. Why? Because real world data is always non-linear, it complex but still, have patterns.
>Non-linearities allow (AI) model to approximate arbitrarily complex functions with enough depth.
![[Pasted image 20250309104043.png]]


---
### [Recurrent Neural Networks, Transformers, and Attention](https://www.youtube.com/watch?v=GvezxUdLrEk)

![[Pasted image 20250314071052.png]]
+ ! **Limitation:** 
+ Encoding bottleneck.
+ Slow no parallelization
+ Not long memory.

+ @ **Desired Capabilities:**
+ Continuous steam
+ Parallelization
+ Long memory.
+ Have Context

+ ? What if we could **tackle the sequence modeling problem without having to deal with the data timestep by timestep.**
![[Pasted image 20250314071311.png]]
**Idea I:** Feed everything into dense network -> No recurrence, Not scalable, No order, No long memory.
+ ? Can we **given a sequence, identify and attend to the important parts of that sequence**, more over **model the dependencies in that sequence that relate to each other**. This is the core idea for a superb mechanism called Attention. (Like skim reading)

#### Intuition behind Self-Attention
+ $ We inheriently have **ability as humans to think about an input and automatically zoom in and pick out thing that are salient** (nổi bật), that is important. 
+ ? How can we do this ? Well, First by identify which parts to attend to then Extract the features with high attention. 

>As a example for youtube search. We search each key (i.e. video title) by a query to compute Attention Mask (i.e. how similar is each key to the desired query). Then extracts values based on key with highest attention score ((i.e., the most relevant to your search query).  
![[Pasted image 20250314074421.png]]
>**Back to ours sequence modeling problem**. We have a series of words (a sentence) and we want to predict the next word. Knowing that we don't want to process the information timestep by timestep.
1) **Encode position information**
	Since we **fed data all at once** **(in parallel)**. So we need to **encode position information to understand order of each word in the sequence**. This called **Positional Embedding** **(preserve sentence context)** ![[Pasted image 20250314075245.png]]
	
2) **Extract query, key, value**
	**2.1)** **Encode position of all sentence include Query, Key (video title), Value (Video Context)**
		Now let take the Query, Key and Value just as we talk before with the Positional Embedding (calc above) representing our sequence in a positionally aware way.
	**2.2)** **Apply weight and bias to each Q, K, V can be learned respectively**
		The model then **apply a Neural Network layer to each of the Q, K ,V matrices, allowing them to capture difference aspects of the input information.** ![[Pasted image 20250314075755.png]]
	
3) **Compute attention weighting**
	The next step is to **compute similarity between the query and key** for each word pair in the sequence. 
	
	Mathematically in Linear Algerbra, we could use **Cosine similarity** to measure distances between vectors, this apply to matrices (i.e. collection of vectors) as well. ![[Pasted image 20250314080048.png]]
	note: each individual query and key in Similarity metric matrices represent as vector 
	![[Pasted image 20250314080220.png]]
	+ ? **What these similarity computation actuall mean ?** Simply **similar words** having **higher attention weight**, while words that are **less related having lower attention weight**.
	+ $ To **normalize these attention weights**, we apply **Softmax** function. his converts the attention scores into a probability distribution, where the sum of all attention weights equals 1. This ensures the model can make a weighted decision about which words are more relavent. 
		The key insight is that **changes in 1 attention weight will affect the attention scores for all other word**. For instance, if the word "tossed" is highly related to "ball", the attention weight between them will increase, and the attention weights between "tossed" and other words will decrease. 	 ![[Pasted image 20250314080347.png]]
	
4) **Extract features with high attention**
	+ ? Each rows of the value matrix represent a specific words (i.e. token) in the sequence. 
	+ $ Now, we can **Extract Features with High Attention** by **multiply Attention Weights matrices with Value matrices**, we get **an output of a "feature set over that input space"** (i.e. features of the input sequence) **that** **"reflects the relative elements of the sequence"** that are **"interrelated relative to each other"** (i.e. relavent based on their attention scores).  This process ensures that words (or tokens) that are more contexturelly important have a greater influence on the final representation. 
	![[Pasted image 20250314090053.png]]


**Summarize**
0) Fed all words in sentence all at once (in parallel) 
1) **Encode positional information** with Positional Embedding.
2) **Extract Query, Key, Value matrices** with Positional Embedding so each of them have their own weights and biases.  
3) **Compute Raw Attention Score $Q \times K^T$** (weights)  by **Calculate similarity** scores between queries and keys.
	**Softmax Normalization** to transform attention weight into probability distribution.
4) **Extract features with high attention** using Attention Weights
![[Pasted image 20250314091141.png]]
This is the foundational building block for Transformer. 
+ ? You can stack multiple attention head to together to increase the capacities of your network and extract different features.
![[Pasted image 20250314091330.png]]
**Application**
![[Pasted image 20250314091338.png]] 

### Visualizing Transformer and Attention



