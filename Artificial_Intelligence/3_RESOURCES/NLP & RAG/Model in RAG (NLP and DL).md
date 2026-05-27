## Embedding Model
![[Pasted image 20250323094817.png]]
 
**Transformer like RNN and LSTM, only read in 1 direction** (left to right). That the born of BERT or **Bidirectional Encoder Representations from Transformers** resolve this issue. 

Main Problem with BERT is that it computationally expensive in **performming long sentences predition**, in other word "**long sentence/text similairty search**"
![[Pasted image 20250323095703.png]]

That where **SBERT** or **Sentence Bidirectional Encoder Representation Transformers** take place. 
+ $ Fast retrieval and similarity comparison between sentences (i.e. **produce a single embedding per sentence**)
+ Accurate **sementic representation** that **correlates well human judgements of textuals similarity.**
![[68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f76322f726573697a653a6669743a313430302f302a416a582d7866613455764e5675396a732e6a7067.png]]

---
## [[Retrieval Augmented Generation RAG - Embedding, Sentence BERT, Vector Database]] 
## [[Sentence Transformer Evolution]]

### Inference
+ ? This forms the final stage of your RAG pipeline:
	- **Retrieval**: SBERT retrieves the most relevant PDF text chunks.
	    
	- **Generation**: A generative model composes the answer based on the query and the retrieved context.

---
### Save Contents
**Plan:** Read BERT + SBERT main ideas -> Code BERT -> Code SBERT -> Understand Matryoshka Embedding Models -> (Main Content) 

**Primary Contents (prequisites for main content):**
+ [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka)
+ [[BERT]] - Bidirectional Encoder Representation Transformers
+ [[SBERT]] - Sentence Bidirectional Encoder Representation Transformers
+ [Prompting General Knowledge](https://huyenchip.com/2024/01/16/sampling.html)


**Main Contents**: [Improving RAG Retrieval by 60% with Fine-Tuned Embeddings](https://www.youtube.com/watch?v=v28Pu7hsJ0s)

**Secondary Contents:** 
+ [Sentence Embedding - Sentence Similarity, Semantic Search and Clustering Code Note](https://github.com/PradipNichite/Youtube-Tutorials/blob/main/Youtube_Course_Sentence_Transformers.ipynb) + [Code Explanation](https://www.youtube.com/watch?v=OlhNZg4gOvA)

**Improvement Content:**
+ [Reranking with Cross Encoders, and Cohere API](https://www.youtube.com/watch?v=ZFbaA9eM0uo)
+ [Customize SBERT document](https://sbert.net/docs/sentence_transformer/training_overview.html#trainer)
+ [Unleasing Power of BERT](https://arize.com/blog-course/unleashing-bert-transformer-model-nlp/)
+ [Transformers From Scratch + Pre-training and Transfer Learning With BERT/GPT](https://youtu.be/acxqoltilME?si=cXNSpTwz5NR2M7HO)

**Improve Understanding**
+ [BERT from Scratch using Pytorch](https://www.youtube.com/watch?v=v5cyVwAXR1I)
+ [Coding SBERT with pytorch](https://www.youtube.com/results?search_query=Coding+BERT+from+scratch)
+ [Pre-Train BERT from scratch: Solution for Company Domain Knowledge Data with  PyTorch](https://www.youtube.com/watch?v=IcrN_L2w0_Y)
+ [MordernBERT fine-tunning Example](https://colab.research.google.com/drive/1iWIruk02fGib9RZWdS51SJStIrHx4hMK?usp=sharing#scrollTo=Kphi220PlmDb)


**correlation:** https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D6uu4sFl1avE&psig=AOvVaw1ZdOV58rZGiwm5PtRzVja7&ust=1742962822024000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCLia6uCwpIwDFQAAAAAdAAAAABAK

