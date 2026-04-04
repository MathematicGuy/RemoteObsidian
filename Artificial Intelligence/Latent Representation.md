
![[Pasted image 20260403160525.png]]
To better understand the importance of latent space in deep learning, we should think of the following question: **Why do we have to encode the raw data in a low-dimensional latent space before classification, regression, or reconstruction?**

**The answer is data compression.** Specifically, in cases where our input data are high-dimensional, it is impossible to learn important information directly from the raw data.

For example:
+ *in an image classification task*, the input dimensions could be $512 \times 512 \times 3$ that correspond to $512\times512\times3=786,432$ input pixels. It seems impossible for a system to learn useful patterns for classification by looking at so many values. **The solution is to encode the high-dimensional input space to a low-dimensional latent space using a deep neural network.**
	
+ *in NLP,* word embeddings are numerical representation of words where similar words are close to eachother. And yes, word embedding are a types of compress information lie in a latent space where every word is encoded into a low-dimensional semantic vector.

![[Pasted image 20260403161553.png]]


**Latent Representation in Neural Network:**
1. Latent space is a low dimensional space produced by a NN system that tries to extract the important features from a higher dimensional input space. For example, a NN algorithm will try to reduce /compress a 512x512 images (which has 512x512x3 = 786432 number) to a vector (set of numbers) that have a lot less numbers. The advantage is that after this extraction/reduction/compression, another NN algorithm can then classify or do "other stuff" in a more manageable fashion.
    
2. Vectors in latent space should have the property that objects that are similar in the input space should be closer together (i.e., have a shorter dist between them).
    
3. A new object in the input space can be generated from an existing object by moving from the vector corresponding to the original object to a nearby vector in the latent space, and then somehow decompress/reconstruct that new vector into an object in the input space.




