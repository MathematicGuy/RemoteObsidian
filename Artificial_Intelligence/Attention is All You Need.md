


**Multi-head Attention** layer **act the same way** as a **Linear Layer** but much more efficient, in comparison for
+ MhA use **x1000 less Computation than Linear**
+ MhA have **x4.000.000 less Parameters than Linear**
[How Attention Mechanism Works in Transformer Architecture](https://www.youtube.com/watch?v=KMHkbXzHn7s)
[[Transformer Neural Networks Derived from Scratch]]

---
### How Attention Got So Efficient `[GQA/MLA/DSA]`
![[out_attn.png]]
+ ? In token prediction task, original Attention recalculate Q,K,V matrix for every new token, this require a lot of Memory: ![[Pasted image 20260307164555.png]]
A solution is to *cache* Key and Value, this method called *KV Caching*. However the required Memory would be enourmous:![[Pasted image 20260307164726.png]]
To reduce required memory, new method called *Multi Query Attention (MQA)* ask if we could *reduce the number of cache for K&V while keeping Q unchanged across heads.* Although this reduce memory significantly, the *model loss its ability to capture complex relationship between tokens* -> performance degrade.
	e..g. Q remain unchange, Keep only 1 copy of K & V then paste them across dimension (d_k, d_v).
![[Pasted image 20260307165323.png]]
+ ! Problem: cache only 1 K,V..
+ $ How about we *cache a group of Key & Value (a numbers of key and value) instead of 1 and duplicated them across attention heads*. This method called *Grouped-Query Attention (GQA),* its group Key & Value across Attention Head.
	e.g. Keep only 2 distince Key and Value for each tokens. The Key & Value are then shared across Attention Heads (Note that QKV dimension remain unchange)
![[Pasted image 20260307165513.png]]
-> Balance between memory efficiency and multi-head accuracy.


----

*Self-attention by default is permuation Equivariant* when it processes input as an unordered set, meaning ==changing the order of input tokens reorders the output in the same way==. The output tokens are in the same order as the input.
+ @ Input order change but Output order remain unchanged. $f(PX)=Pf(X)$

**Set Transformers:** For *tasks requiring permutation invariance* (where the output shouldn't change if inputs are shuffled), *aggregation* methods like pooling (sum/mean) are applied _after_ the equivariant self-attention layers.
+ @ Input order == Output order. $f(PX)=f(X)$ where $P$ mean applying Permutation to the function.


**Why Multi-Head-Attention and not 1 Head ?**
1) For Faster parallel computation, 1 GPU for each head.
2) Each Head capture a different relationship between word (note: each head calc self-attention), ie. relationship between 1 word to all word in a sequence). Because each head are trained across multiple sequence allowing each head to capture a different aspect of meaning between word.
	For example, the word making in "River Bank" learn by "Red Head" and "Bank-ing app" learn by Head_2 have 2 completly different meaning.

Note that Head are seperated from QKV with full embedding dimension, so each head is just QKV but with less embedding dimension
![[Pasted image 20260319153030.png | 888]]
-> basically instead of calc a large QKV matrix, we seperated into smaller multiple one, each with it own value.
![[Pasted image 20260319153449.png]]
After Attention Score of each head is calculate, they will be concat back into 1 single matrix.
![[Pasted image 20260319153654.png | 666]]
![[Pasted image 20260319153718.png | 666]]

+ ! Cons: each head have fewer dimension -> smaller representational capacity and fewer parameters to capture nuanced patterns within its specific perspective.

The visualization show different word dependency with different Head Color.
![[Pasted image 20260318155558.png]]


**First of Why Normalization ?**
1) First Issue: *Exploding/Vanishing Gradient*
In standard Neural Network, the gradient accumulate during the forward and backward pass. Because each layer has parameter and receives gradient of loss with respect of those parameters. The gradient magnitude depend heavily on the output loss, if the loss if large then during backpropagation, the gradient past back to the earlier layers would also be very large (Expoding Gradient) or very small (Vanishing Gradient), this make training very unstable & inefficient.

To counter this problem, we normalize the Activation Value to their distribution (ie. value range) become more stable (not too large or too small)


2) Second Issue: *Internal Covariance Shift*
 + ? As earlier layers update their weights during training, the distribution of activations fed into later layers keeps changing, making learning a moving target. Because traditional AI model heavily depend on Data Distribution's patterns and the activation value are mapping the input value from layers to layers, the input value distribution also become unstable as the activation value become unstable.

As the training goes on and weight udpated, the model may see inputs with a different mean and variance or a skewed shape. While the layer trying to adapt, the data distribution keep drifting, so the layer is constantly adapting to a moving target (moving data distribution) -> Slow down Convergence and make optiomization harder.
![[Pasted image 20260319154359.png | 888]]




**Why Layer Normalization: Batch Normalization vs Layer Normalization**
Note: Normalization are apply to Features (e.g. after the Conv or Multi-Head Attention), not raw value.
+ *Batch Norm* work well when *Features across batches shared similar statistic (same class, different domain)*. For example, In CNNs, *features/pattern at the same channel across different images tend to follow similar distributions (ie. edge, textures)*, so batch statistics are meaningful.
![[Pasted image 20260306153436.png | 444]]

+ In NLP, each sequence (sentence) have a different semantics (ie. meaning) and each token could have multiple meaning (different representation across batches, like "bank" in river bank and the bank) -> Batch statistic become unstable when apply Batch Norm.
	What we could do is apply Normalization to **each token vector (red box) independently**, computing mean and variance across its **embedding dimensions (yellow box)**.
	+ ? In a simple POV, each token embedding layer represent 1 class, multiple embedding layer allow each token to have more meaning across each token in the sequence.
	Example, each token's dim (ie. each value in red) capture a different meaning/use-case of a word/token:
	- dim 12 → “animal-ness”
	- dim 87 → “financial context”
	- dim 203 → “syntactic role”
	Note that if each dim capture a different meain for a token, this mean we could seperate 1 embedding vector into multiple sub-embedding vector called Head with its dimension of "embedding_dim / head", so each head could learn a different semantic meaning of the token.
	-> Normalizing all Meaning/Use-case of a token.
![[Pasted image 20260306160245.png]]

![[Pasted image 20260306162302.png]]
Transformer's Input is a sequence of tokens (e.g. words) where each token has an embedding vector of size of the embedding dimensions. `(batch, seq_len, d_model)`

**LayerNorm in Transformers**  compute the *mean and std along the embedding dim for each token independently.* This way, **each token Embedding value remain stable across layers which is essential for effective attention calculations**
For each token:
$$y_{i} = \gamma_{i} \cdot \frac{x_{i} - \mu_{layer}}{\sqrt{ \sigma^{2}_{layer} + \epsilon}}+\beta_{i}$$
For all token (matrix form):
$$y = \gamma \cdot \frac{x - \mu_{layers}}{\sqrt{ \sigma^{2}_{layers} + \epsilon}}+\beta$$
-> While *$x_i$ (each token's embedding value), $\gamma$ and $\beta$* are *learned params* applied per feature (ie. per embedding dimension), the *mean $\mu$ and std $\sigma$ are not learned* but compute (deterministic).
-> Very useful for sequence base model where each sequence present a new distribution.
	Note: bc $\gamma$ multiplying and $\beta$ is adding to the feature matrix, they are vector size features.

----
### Training: Text Translation using Next Token Prediction Causal Mask
![[Pasted image 20260318174203.png]]
Note: logits is the similarity between Current context and Token Embedding. Its can be convert to probability using softmax e.g. $P = Softmax(logits)$, which eventually used to calc Attention Score.

**Step 1:**
+ Encoder receive English input text and capture the relationship between tokens (attention score of QKV) then Output Attention Score of Key and Value to the Decoder.   ![[Pasted image 20260318183012.png | 488]]
+ The Decoder receive the Italian input text and Apply the Causal Mask to ==ensures that each token in a sequence only attends to past and current positions, ignoring future tokens==. This *enforce the model to always predicting the next token using only what it has already seen* (ie. autoregressive constraint) ![[Pasted image 20260318194623.png | 888]]
-> Force the *Output Matrix* only contain the *Attention Score between the Current Token and Past Token* its for each token across the Matrix - [How Causal Mask Work](https://www.vizuaranewsletter.com/p/the-transformers). So when *mulplying Causal-Mask Attention Score with V*, only the current & previous token value get Amplified: ![[Pasted image 20260318195917.png]]Notice that 4th row have 1 zero, 3nd row have 2 zero -> That is the Masked Future Token.
+ ? Different language may have different word but the semantic meaning and relationship between word remain the same. So what if we calculate Attention Score between 2 languages, they should have the same Attention Score right ?
+ @ The *Output is the Italian Masked-Query (Q)* for the next Multi-Head Attention. e.g. calculate Self-Attention between Masked-Query of the Decoder with the Key & Value from the Encoder.
-> Efficiency Predicting, *which English token corresponding to the current Italian token sequence.*

**Step 2:** *Calc Attention Score between 2 languages*
The Decoder calculate Self-Attention Between "*Masked Query from the Decoder with Key and Value from the Encoder*.
+ ? This answer the question, for this given masked sequence (sequence with current token and past tokens) in Italian Language, *which is the Corresponding English Key should the Italian Query pay Attention to*, (after Softmax) then project those Translation Attention Score back to the English Value.
+ @ The Output is the Amplified Italian Logits between English and Italian
-> which English token corresponding to the current Italian Masked-Query sequence.

**Step 3:** *Positional Feed Forward (Apply Non-Linearity)* - [reference](https://www.reddit.com/r/deeplearning/comments/1gxtdow/experiment_what_happens_if_you_remove_the/)
**Feedforward layer intuition (linear + activation):**
+ @ In short, Feedforward use activation function like ReLU, GeLU to filter out unuseful value by a threshold determine by the activation function. e.g. ReLU filter all negative value for example, even though some of them is useful -> that why we use GeLU and SwiGLU.

When you calc Attention, you’re essentially converting the input sequence into a set of inter token relations which you then resolve into values.
-> The same as **key word search on an index based on a search query in Google/Youtube.**

The feedforward acts as the *post processor of extracted information to activate the "information/memory nodes"* based on relational information extracted from the Attention layer.
-> The same as taking the result of a search query and re-ranking the flat result (logit or softmax probability) into a sorted result from most meaningful to least meaningful.

Mathematically, the non-linear activation function like *ReLU, GeLU, etc act as a 'gate' for which information is relevant or not* (like a **filter with threshold**).
-> Non-Linear activations of a DNN that act as a threshold voltage in neurons in the human brain.

![[Pasted image 20260319160607.png]]
It takes each 768 dimensional input vector and projects it into a much larger space with 4 × 768 = 3072 hidden units. In matrix form this is a multiplication by a 768 by 3072 weight matrix plus a bias term. +
+ $ Intuitively, this expansion gives the model more capacity to construct rich intermediate features from each token representation before compression them again to 768.

**GeLU vs ReLU**
![[Pasted image 20260319161353.png]]
GeLU is smooth and more tolerant, its accept small negative value while discard negative value > than -2. ReLU reject every value smaller than 0.

*ReLU:* Even though it help calculation fast there are 2 issue, First, this causes "Dying ReLU" problem, when a neuron gets stuck and outputs 0 for all inputs (ie. some 0 are good, all 0 are bad) making the Neuron Deads (unable to update anymore). The Second problem is negative value still store information, it signified the current learning features is incorrect, bc large negative value cause vanishing gradient, small negative gradient could be use for such use.

*GeLU:* account small negative value has 2 consequences.
+ First, the func is differentiable everywhere (able to calc derivative), including at zero, which makes optimization smoother.
+ Second, the Neuron network doesn't not discard all information carried by small negative activations.
	help model distint zero and value close to zero.
-> While large negative value is bad, with the help of normalization which keep value at moderate range,  this help training more stable and slightly better performance.

**Shortcut connection (Residual)**
Effect of shortcut connections on gradients.
	Left: without shortcuts, *gradients vanish (0.00003, 0.00001).*
	Right: with shortcuts, *gradients remain large (0.45, 0.52),* *enabling effective learning* in earlier layers._
![[Pasted image 20260319163038.png]]
As we said before, even though normalize stablelize learning, vanishing gradient problem always a problem in DNN.
+ ? A shortcut connection simply add earlier block logits to later block output logits bypassing one or more nonlnear layers (of the later block).
+ $ Effective at keeping gradients from disappearing during backpropagation and *preserves stronger gradients in the earlier layers, which makes learning much more effective (smoother gradient).*
![[Pasted image 20260319163515.png | 666]]


**Step 4: Evaluation**
**Linear Layer:** help to project/associate the Decoder's Logits with the True value from the vocabulary. Then determine which value/token is most Important using Softmax.
	For *every embedding that it sees, what is the position of that word in the Vocabulary* so that we can understand what is the actual token that is output by the model.

Then you calc Loss and backproprogation from there.
![[Pasted image 20260319151902.png]]


#### Why Transformers Scale Better than RNNs and CNNs ?
Fundamentally, Transformer is designed with Scability both in term of efficiency training and size. Whereas RNNs process tokens sequentially, limit its own parallelism ability. Transformer process the entire sequence at once, with self-attention allowing each token to interact with every other token in the sequence -> Able Propagate the entire sequence in 1 pass. This parallel structure adapt naturally with modern hardware like GPUs and TPUs, enabling efficient parallel computation.

CNNs depend on their receptive fields and deep CNN stacks to capture long-range dependencies ie. capture local representation then combine them together later. Transformer capture the global context explicitly from the start -> help improvement more predictable.

Architecturally, Transformer Blocks (encoder/decoder) can be *stacked repeatedly with minimal modification, allowing depth and width to be increase systematically (bc output in the final layer project into a 1D Linear layer, concatinate information from every Decoder block ??) while Residual Connetion and Normalization within each Block normalize training even when hundreds of layers are used*  -> Remove vanishing gradient problem with parallelism. Have the ability to capture short/long-range dependency feature. Make transformer a general purpose backbone good for scale without extensive redesign. (ie. you could add 1 or 2 modification to the Transformer and have it scale)

#### Pretraining, Fine Tuning, and Transfer Learning in Transformers
As Attention help capture relationship between token, a *well train Transformer have general purpose capability, like a person with strong background knowledge* ready to do a specific task.
+ $ Representation within the model forming a reuseable foundation that can *suport many downstream task* (ie. specific finetuning task).
+ ! Beside those pros, transformer still suffer from bias from their training data, and can overfit from small dataset. Self-Attention is quadratic cost (i.e NxN matrix), as input sequences grow longer so are the memory and computation.

### Inference
![[Pasted image 20260319151946.png]]
Like in Training, in Inference the Decoder receive each token at a time and predicted it in 1 single pass. Stop with the `[SOS]` token.

**Inference Strategy**
![[Pasted image 20260319152123.png]]
