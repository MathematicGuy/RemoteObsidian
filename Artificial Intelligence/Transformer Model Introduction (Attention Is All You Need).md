## Chapter 5: Transformer Models
### Word Embedding
>Embed each word with one-hot encoder and multiply its weight through a Activation function.
>In this example, Activation Function themselves doesn't change words value. e.g. f(0.09) = 0.09
>-> This way we can encode all words in a sentence using a single set of Weight.
+ ? Note that all the weights of the sentence is determind by Backpropagation step. At the start all these weight are innitialize randomly, but through training Backpropagation optimizes these values one-step-at-a-time and results in these final Weights.
![[Pasted image 20250314123831.png]]

### 5.3 Positional Encoding
In this example, we've got a new vocabulary and we're creating 4 Word Embedding values, per word.
However in practice people often create thousands of embedding values per word. 

In this case, the number that represent the **word order come from a sequence of alternating Sine and Cosine squiggle** each **squiggle give us the specific position values for each word's embeddings** where **Y is the Embedding Position** of **a word** and **X is the Input Word Position** 
 
+ ? Specifically, for the **1st word represent as 1 on the X-axis**, having its **Y-axis represent the position of each embedding values** respectively as 0, 1, 0, 1 . 
	+ 1st embedding is the y coordinate 0 from the green squiggle.  
	+ 2nd embedding is the y coordinate 1 come from the orange squiggle .  
	+ 3rd embedding is the y coordinate 0 come from the blue squiggle .  
	+ 4th embedding is the y coordinate 0 come from the red squiggle .  
+ $ Encode each token/word  embedded values  
![[Pasted image 20250314125912.png]]
**For the 2nd word, we simply get the x-axis coordinate for the second word and y-axis coordinates on all squiggle to identify 2nd words embedding value** respectively as: 0.9, 0.4, 0.1, 0.9.  The same for the 3rd word, we get the embedding value on the y-axis that matches with the 3rd x-axis coordinate. And so on 
![[Pasted image 20250314132711.png]]
+ ? Because the **Sine and Cosine coordinate is repetitive, it possible that 2 words have the same position** (e.g. -0.9 for both eats and pizza). However as the squiggle get wider and larger for embedding positions and **more embedding values we have the wider the squiggles get. Thus even with the more repeat values, each input word ends up with a unique sequence position values**.     
![[Pasted image 20250314130830.png]]
Finally, we add the Positional value to the Embedded value to get Positional Embedded value of the whole sentence.  
![[Pasted image 20250314132957.png]]
+ ? **If the word 3rd word `Pizza` and 1st word `Squatch` get swap**, we **just swap the Embedding value** of `Pizza` with `Squatch` but the **Positional Value stay the same.** And we simply **end up with new Positional Encoding for 1st and 3rd word.** This way Positional Encoding allows a Transformer to keep track of word order.   ![[Pasted image 20250314133450.png]]

Let's summarize with a simple example for the word "let's go". For 2 words we simply get the the Positional Encoding of the 1st sine (green) and cosine (yellow) that match the
+ 1st word position on the x-axis for word 'let's
+ 2nd word position on the x-axis for the word 'go'
![[Pasted image 20250314133753.png]]
To consolidate the math diagram. We use the **Sine** and **Cosine** and **plus** symbols represent the **Positional Encoding.**
![[Pasted image 20250314134659.png]]

### 5.1 Self-Attention Mechanism 
+ @ Now we know how to keep track of word position. Let's talk about how a Transformer keep track of the relationships among words using **Self-Attention by seeing how similar each word is to all of the words in the sentence, including `itself`.**![[Pasted image 20250314180207.png]] 
+ ? Once the similarity are calculated they are used to determine how the Transformer encodes each word. For example, if you look at the sentences about `pizza` and the word `it` was more commonly associated with `pizza` than `oven`. That is the main idea of how Self-Attention work, let look at the detail.

### 5.2 Self-Attention Encoder
The first thing we do is to multiply 2 encoded value `1.87` and `1.09`  with 2 pair of weight repectively. We do this twice because we started out with 2 position encoded values that represent the word `let's`.
+ ? If we want 2 values to represent Let's, why don't we just use the 2 values we started with? Explain after little bit. 
![[Pasted image 20250314180958.png]]

+ ? Now that we have Query values for the word `let's`. We use them to calc the similarity between it self and the word `go`. And we do this by creating 4 new values  just like we did with Query called key values, 2 key values represent `let's` and 2 key values represent `go`.         
+ $ Having all Key values for both `let's` and `go`, to find which word are more related, we simply **compare similarity values between them:
	+ `let's` to `let's`  (it self)  
	+ and `let's` to `go`  **using Dot Product**.   ![[Pasted image 20250314181759.png]]
	  This tell us that `let's` is much more similar to itself then `go`. Then we want `let's` to have more influnce than the word `go`, and we do this by apply the Softmax function to them. ![[Pasted image 20250314182718.png]]
	 
 + $ **Because we want 100% of the word `let's` to encode `let's` and 0% to represent the word `go`.** We create 2 more values that we cleverly called **Values** to represent the word `let's` and 2 more value represent the word `go`. **Then Multiply/Scale them to it's Softmax value respectively.** Lastly add them together.
	 + ? `let's`: $[2.5, -2.1] \times 1$ 
	 + ? `go`: $[2.5, -2.1] \times 0$ 
	 + ? `let's go`: $[2.5, -2.1]$
	 + $ In short, we first calculate the `Similarity Scores` between `Query` and `Keys` to determine which key is more similar to the query. Then we scale each `Value` by their calculated `Similarity Score` to indicate their important. Lastly **add them together to represent the Self-Attention values** for `Let's`   ![[Pasted image 20250314182924.png]]
	 + @ Now it's time to calculate Self-Attention score for the word `go`

+ ? Good news is that we don't need to re-calculate all valus. Instead we **just need to create the `Query` for the word `go` and do the math**. *Inhale*, first we find the **similarity score** between `go` to itself and `let's` using Dot Product then apply softmax. And scale `Value` of both `let's` and `go` by the similarity score then add them together.  ![[Pasted image 20250314184709.png]]

+ ? Before moving on, let's clear out a few detail about **Self-Attention**. All `Queries` use the same set of Weights for each input word (e.g. Query of `let's` and `go` use the same set of weight). Likewise we **reuse the same set of Weights for calculating Self-Attention Keys and Values** for **Each Input Word**.
+ ? Also, we calculating the `Queries`, `Keys` and `Values` for each word at the same time. Allow parallel computating in Transformer.

Now that we understand how to calc Self-Attention, let shrink the math model down.
![[Pasted image 20250314185911.png]]

+ ? Wait, why we use 2 values to represent `let's`, why don't we just use the 2 Position Encoded value we started with again?
 + $ First, the **new Self-Attention** values **of each word contain input from all of the other words** (in the sentence), and this helps give each word context. 
 + ? This mean, the **Self-Attention** allow the model to **understand the relationship between among words**.  
 + $ Also, if we think of **Self-Attention** cell as **Weights** for calculating **Queries, Keys** and **Values**. Then we can create a **stacked of Self-Attention cell**, in order to **Capture Different Relationship Among words** that we apply the Positional Encoded to. In the paper, they **stacked 8 Self-Attention cells** and **they called this Multi-Head Attention.**  
+ ? 8 heads because 8 GPU clusters are common and can compute in parallel. The embedding dimension are 512 and that leaves each head has 64 query size.


+ $ To **Encode the input**. We **take the Positional Encoded value and add them to the Self-Attention value**. These connection called **[[Residual Connections]]**. 
+ ? They make it **easier to train complex neural networks** by **allowing the Self-Attention layer to established relationships among the input words** without having to also preserve the Word Embedding and Positional Encoding information. 
![[Pasted image 20250314192503.png]]

![[Pasted image 20250314193136.png]]
+ $ These 4 features, 
	+ allow the **Transformer** to encode words into number. 
	+ encode position of the words.
	+ encode the relationships among the words. 
	+ easy and quickly train in paralle.  

### 5.3 Transformers Decoder 
+ ? Just like the Encoder but for output vocaulary, which consists of the Spanish words. We start by calculating the **Self-Attention** score for the `<EOS>` token (note:  people may use `<SOS>` for `Start of Sentence` or `Start of Sequence` to intialize the process and that fine too, but for this example let's use `<EOS>`) ![[Pasted image 20250315091058.png]]![[Pasted image 20250316072836.png]]

And like wise, when we decode and translate the input, we want a single unit that we can copy for each translate word for the same reason.   
+ ! Set of **Weights** we used for **Decoder Self-Attention** `Query`, `Key` and `Value` is different from the sets we used in the `Encoder`. 

+ ! When we're translating a sentence, it **vital to keep track of the relationships *between* the input sentence and the output.**  
+ ? (*indian accent*) **"Don't you tell me what to do"** and **"you tell me what to do"** transfer opposite meaning. When translating, it super important for the **Decoder** to **keep track of significant word in the input**. 
+ $ So the main idea of **Encoder-Decoder Attention** is to **allow the Decoder to keep track of the Important words** in the input. like `Don't`


+ ? Just **like in the Encoder**, we create **2 values** for `Query` in the **Decoder**  
![[Pasted image 20250316072647.png]]
+ ? and **2 values for each words in the Encoder** called `Key` values.

+ ? For **Encoder-Decoder Attention** value, we **calculate the similarity score** between the `<EOS>` token  in the **Decoder** and each word in the **Encoder** using **Dot Product** just like before. Then we apply the **Softmax** function to calc probabilty distribute of each **similarity score**. Finally add the pair of scaled values together to get the **Encoder-Decoder Attention** values![[Pasted image 20250316073303.png]]![[Pasted image 20250315094502.png]]
+ ! **Note:** The set of **Weights** that we use to calc the **Queries, Keys and Values** for **Encoder-Decoder Attention** are **different from the sets of Weights we use for Self-Attention**. However, just like **Self-Attention** the sets of **Weights** are copied and **reused for each word**.  ![[Pasted image 20250315095301.png]]
+ ? Also, we can stack **Encoder-Decoder Attention** just like we can stack **Self-Attention** to keep track words in complicated phrases.

 + $ After having **Encoder-Decoder Attention score**, we **add another set of** **Residual Connections** to allow **Encoder-Decoder Attention** to **focus on relationships** between the **input word and the output word** without having to preserve the **Self-Attention** or **Positional-Encoder** in the ealier layers.![[Pasted image 20250315095948.png]]
+ ? Lastly, we **need a way to take these 2 values that represent the `<EOS>` token** in the **Decoder**  and select 1 of the 4 output tokens, `ir`, `vamos` or `<EOS>`.
+ $ To **Classifies which word are translated to**, we **run the 2 values through** a **Fully Conencted Layer** that has 1 input for each value that **represent the current token**. And when we do the math, we get 4 output values which represent `vamos` after we run though a **Softmax** function. 
![[Pasted image 20250316063403.png]]
note: `vamos` is the Spanish translation for `let's go`


+ ! But we not done yet, the translation is correct but the **Decoder** doesn't stop until it outut the `<EOS>` token. 
+ $ We need to plug the translated word `vamos` into a copy of the **Decoder's Embedding** layer.  ![[Pasted image 20250315184141.png]]


1) Like before, first we calc the Word Embedding for `Vamos
2) Then add the Positional Encoding
3) And calculate the **Self-Attention** values for `vamos` using the exact same `Weights` that we use to calculate the `<EOS>` token. Follow by a **Residual Connection** that add the **Postional Embedding values** (i.e. embedding value before calc attention score) 
4)  Re-calculate the **Encoder-Decoder Attention** of `vamos` by  between `let's` and `go` using the same sets of Weights for `<EOS>` token.
5) Lastly, we run the values that represent `vamos` through the same `Fully Connected Layer` and `SoftMax` that we used for the `<EOS>` token. 
![[Pasted image 20250316062619.png]]



### 5.4 Lab: Implementing Attention, Self-Attention, Positional Encoding, and Transformer


