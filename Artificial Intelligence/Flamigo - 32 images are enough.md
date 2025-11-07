**Keypoints:**
+ Flammingo focus on fine-tuning the Gated Attention layer where it act as a Translation layer between Text and Image Token 
+ Flammingo Vision Encoder layer is like CLIP but better. 
+ Vision Encoder and LLM model block are frozen for stability while training the Gated ATTN layer. 
+ Flammingo understand temporal information (ie. time and space information).


Learn from few-shot example. 
Can understand temporal information (information between frames)
![[Pasted image 20251029101449.png]]

**Want the Learnable blocks to function as a sort of translation between token feature and visual image.** 
![[Pasted image 20251029101849.png]]
Vision Encoder use Resolution Base Encoder - similar to CLIP model but better. 
Each frame encoder independently. Flat to 1D -> Perceiver Resampler -> feed into Dense Gated Cross-Attention. 
+ ? The idea is to actually modify the architecture of the Frozen LLM and insert new trainable layers to embed the visual information into the llm. 
![[Pasted image 20251029102300.png]]

![[Pasted image 20251029102412.png]]

![[Pasted image 20251029102434.png| 444]]

 Define a Image as a Chunk. 