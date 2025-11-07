**Multi-head Attention** layer **act the same way** as a **Linear Layer** but much more efficient, in comparison for ChatGPT:
+ MhA use **x1000 less Computation than Linear**
+ MhA have **x4.000.000 less Parameters than Linear**

[How Attention Mechanism Works in Transformer Architecture](https://www.youtube.com/watch?v=KMHkbXzHn7s)

### Transformer Neural Networks Derived from Scratch
+ ? Motivation behind the Transformer

100 years ago, human invented way to **represent word numerically using one-hot vector**. Position of each work doesn't matter so long as each
![[Pasted image 20250313164055.png]]
word is consistently associated with the same unique vector. 
![[Pasted image 20250313164025.png]]

+ ? Each layer of CNN capture the essence of the image.  
The true cause of which CNN faild to learn from text is a bit more subtle (tinh tế)   
+ The Neural Network output a vectors by that represent by sequences of 3 words that occur at each position. (run though 3 words at a time)
	![[Pasted image 20250313165124.png]]
+ Each layer combines information from larget and larger groups until the final layer contains information from the entire input. ![[Pasted image 20250313164351.png]]
+ ? The thing is though, it's really dififcult to do this whole combine multiple vectors into 1 single vector representation thing. Neural network can learn to do it but only if all relation are strongly related to each other. 
+ ! If there're many **weak related relationships**, neural network tends to **get confuse about what information it get to keep**.

What `related` mean in here, is that knowning value of 1 input should help you to better predict the value of the others. In images, this would meaning knowning the color of a pixel should allow you to predict what color the neighbouring pixels will be.  ![[Pasted image 20250313170241.png]]
This is generally true for natural images, where nearby pixels have similar colors. Which is why CNN have no problem learning from images.  
![[Pasted image 20250313170336.png]]

+ ? What about texts, would knowning word occurs in given position help u to predict what the neighbouring word are. Well, it is true that words in a sentence are related to eachother but this wasn't always the case. ![[Pasted image 20250313170635.png]]
For example, it's wasn't for until the last layer the word "dog" met "tail" and before "tail" CNN will attempt to combine other words in the sentence which are less related and get itself confuse.  
![[Pasted image 20250313173223.png]]
+ $ This is the problem that transformers seek to resolve: CNNs can't handle long range relation. The **idea for transformer is simple, just replace Conv layer with Pair-wise Conv layer**.  

In pair-wise convolution layer, we apply a neural net to each pair of words from the sentence.  
![[Pasted image 20250313173715.png]]
Now pairs that **unrelated to eachother doesn't matter**, **so long that as somewhere we have pairs of the related words.**  
![[Pasted image 20250313180035.png]]

And we can repeat this step again to compute pair-to-pair vectors together (i.e. pair-wise again with all the pair-wise vectors above). 
![[Pasted image 20250313174212.png]]
Now each of these vector represent a group of 4 words in a sentence. Each time we would get a larger and larget group of words. 
![[Pasted image 20250313180227.png]]
	At the end we average all of the vectors (each horizontally, 1 word to all words) together to get the final prediction.  Each one of the resulting vectors is created by combining the words from the original sentence in a different order.   
+ ? This is the same as rearranging the input sentences into all possible permutations of the word. Then apply regular CNN to each permutation, and then averaging the output from each (permutation).    
 + $ The idea is that, somewhere in this list there must be a good ordering.  One where related words occur right next to each other, and hence can be efficienly combined by the CNN.  
(This simply mean, calculated the relationship of each words to all words in the sentence using CNN, whichever combination score is higher, is true)
![[Pasted image 20250313181106.png]]
But there a problem, it ignore the order of word in the sentence which is critical for language understanding. For example: "the fat cat" and "the cat fat".

+ @ **Solution - Adding Positonal Information:**  with each word is represented as a **one-hot vector** we need a second one-hot encoding added to indicate the word's position in the sentence.

#### **4. Self-Attention: The Core Idea of Transformers**

- The model becomes inefficient due to the **quadratic growth** in word pairs (e.g., 3 input words → 9 vectors after 2 layers).
- To fix this, **self-attention** is introduced:
    - Each word pair is assigned an **importance score** by a small neural network.
    - The score is used to **weight** the pair’s contribution.
    - Higher-scored pairs retain more information, while lower-scored pairs fade out.

---

#### **5. Optimizations for Efficiency**

- **Replace neural nets with linear functions** for efficiency.
- **Apply self-attention multiple times (multi-head self-attention)** to preserve multiple relationships.
- **Use residual connections, layer normalization, and byte-pair encoding** for stability and efficiency.


