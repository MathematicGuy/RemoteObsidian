![[529203986_532562106580681_3142090675945004784_n.png]]

## 1. Slide thuyết trình (Presentation Slides)
- **Goal:** Summarize the key content about Multi-Modal LLMs.
- **Team workflow:**
	  
    - **Research subgroup (2–3 members):** Collect information (*definition, history, use cases, current research papers, trends, pros & cons, challenges*).
	     
    - **Slide designer (1–2 members):** Convert research into clear, concise slides with visuals (charts, diagrams, examples).
	    
	- **Reviewer (1 member):** Ensure slides flow logically and fit time limi
	
Note: Đọc hết là tùy chọn, Cần phân chia rõ ràng. 

**3 Paths for Multi-Model** 
1) **LLM + Tools (API, custom function, micro-service API)** ![[Pasted image 20250816204134.png | 555]]

   
2) **LLM + Adapters (MLP, Projection layer)** 
	-> **MLP within Encoder and Decoder** of the Transformer Architecture **is a Adapter**.
	Instead of external tools, we attach **adapters (small neural networks)** to the LLM that convert non-text inputs into embeddings the LLM can understand. 
	Frozen & Hot Parameters (Trainable/Untrainable) ![[Pasted image 20250816205400.png | 544]] 
	![[Pasted image 20250816205550.png | 544]]
	+ Better customization
	+ Data efficiency. But Require training data. 
	+ **Data Engineering** heavy. 
	
3) **Unified Models** (Very Advanced)  - only vector
	Training from scratch (mixing modalities at pre-training)
	
	**Pros:** Less Computation and faster inference time, because there everything just passing through a single model. like GPT-4o.
	**Cons**: Very Anvanced technical challanges, resources heavy like million of dollars. 
	Example: LLaMA 3.2 Vision for Image-based tasks, 

**Definitions of MM-LLM**


## 2. Video thuyết trình nhóm (Recorded Video Presentation)
-> Ai làm phần nào thì nói phần đấy. 

## 3. Báo cáo công việc (Work Report)
(On Excel for simplism)
+ **Goals:** report your research process, which resources you used and what you contributed. 
+ **Team workflow:**
	+ **Coordintor (1 mem):** Outline the structure of the report
	+ **Contributors (all mems):**  

----

## [[Paper Reading - Understanding Naturalistic Facial Expressions with Deep Learning and Multimodal Large Language Models]]