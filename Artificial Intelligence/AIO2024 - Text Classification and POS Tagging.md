## Introduction to Text Classification and POS Tagging
**Semi-Structure Data**
flexible data: NoSQL, CSV, JSON

Non-Structure data -> Natural Language, easy to understand.

![[Pasted image 20250204202950.png]]
note: xem Lại Module 6 để hiểu phần Preprocessing

# Text Classification
**Tokenization:** turn sentence into many unique letter

![[Pasted image 20250204203950.png]]
`specials` for specifing special token.

+ ? Why use [yield](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/) instead of `return` ?
-> Use when returning a large amount of data. `yield` return data in smaller batch to avoid crash, especially in server.

![[Pasted image 20250204204738.png]]
+ ? Vectorize word, what about undefined word like `sell`. Well that where special token come in. 
+ $ Undefined word get tokenize into special token. 

+ ? Problems ? different input dimension for each sentence.
	![[Pasted image 20250204205102.png]]
+ $ Solution ? Create a fixed input dimension with length equal to the longest sentence length.
![[Pasted image 20250204204738.png]]
Like tokenizing empty space in short sentence as special token 1.


(1, 5, 2) == (batchsize, sequence_length, embedding_dims) where 
embedding_dimes mean vectorized token hence the embedding process.
Output layer is (1, 2) meaning there're 2 classification labels, usally Yes and No. 
![[Pasted image 20250204212108.png]]

# Part-of-Speech Tagging (PoS Tagging)
**Tagging** hence the process of **assigning grammar rule to each token**. 


# Vectorization
![[Pasted image 20250204214704.png]]
Additional step: Label tokenized vectors
+ ? What if there not enough Label? Like token `<pad>` for example 
+ $ Need to add a additional Label and Label Index.
![[Pasted image 20250204215029.png]]

First line: cut off sentence within the sequence_length (fixed sentence length)
Second line: Add missing word to short sentence (maybe ?)
![[Pasted image 20250204215132.png]]


+ ? Why not embedding just 1 token but many at once. 
+ $ Because a word can have multiple meaning, embedding and process single word can create misunderstanding making it unable to understanding word in different context.
	Example: The fly fly in the sky -> 2 fly have diff meaning in this context.  

![[Pasted image 20250204221550.png]]
Note: apply Softmax for each token in output layer out of (1, 4, 4) ~ 15 tokens (count from 0).


Need to Permute before output data to Cross Entropy Loss Function (If I using Pytorch, remember to change position back to (bs, seq_len, classes) at the end)
![[Pasted image 20250204222139.png]]

note: check Graph Embedding 


1) Extract 2 sens from corpus (i.e library of sentence)
2) tokenize 2 sens (convert the whole sens to unique letter)
3) vectorize 2 tokenized sens (convert unique letter to their corresponding integer)
	vectorize the samples 
4) embedding 2 vectors ()

---

## Deep Architectures for POS Tagging

**Tokenize a sentences**
![[Pasted image 20250205201536.png]]

**Embedding**
![[Pasted image 20250205201756.png]]
**Vectorization**: convert each word into its corresponding integer (i.e. input_id)
![[Pasted image 20250205201936.png]]

note: Input Shape is fixed in Deep Learning
**Convert each Vector into a Tensor**
![[Pasted image 20250205202127.png]]

Retrieve sample from embedded parameter
![[Pasted image 20250205202214.png]]
**Single output:** Sigmoid -> output shape (20, 1)
**Multiple output:** Softmax -> Output shape (20, 2) -> 20 output and 2 label/features
![[Pasted image 20250205202329.png]]

22 total parameters, 10 nodes in hidden layer, 2 output nodes with bias for each output nodes. -> 10x2 + 1x2 = 22.   
![[Pasted image 20250205203406.png]]


**note:** in pytorch channel (c) position first.
	numpy (sequence_length, channel)
	pytorch (channel, sequence_length)
permute(0, 2, 1) -> change original position (0, 1, 2) to (0, 2, 1) by index.

Conv1d calc using sliding windown technique: multiply w with 1st input row but there still 1 value left in row -> multiply w to 1st input row starting from index 2 to index n (i.e. last index)  
![[Pasted image 20250205210456.png]]
![[Pasted image 20250205211048.png]]

### Example 3: Text Classificaiton with MLP
(1, 3) - 2 output + 1 bias  (linear)
output: true/false -> use softmax (3, 2) 
k: number of examples
![[Pasted image 20250205211928.png]]
Linear (3, 2) - Input 3 nodes, Output 2 nodes
note: Pytorch Conv1d input format $(C_{in}​, C_{out}, Kernel)$ so we permute(0, 2, 1) to convert 
![[Pasted image 20250205212012.png]]

### Example 4: Text Classification with RNN
Convert from 3 to 2 -> use Linear(3, 2)
![[Pasted image 20250205215435.png]]

What I learned: How to convert diff dims to desired dims. e.g. (4, 4) -> (4, 3) 


Ignore_index = 0 -> value with index = 0 get ignore. e.g. y=0 have 0.97 and one-hot have index =1;
![[Pasted image 20250205225055.png]]


![[Pasted image 20250205225607.png]]
+ nn.Linear(input_size, output_size) 
+ `torch.randn((32, 6, 5))` -> 32 samples, 6 word, 5 number (i.e. tensor size) where each word get represent by 5 number.


