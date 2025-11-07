**Pre-training** - already train on a certain type of dataset. 
![[Pasted image 20251029113251.png]] 
-> When the **underlying model was good enough (train on huge amount of data) its can perform multiple task that it wasn't even train on.** 

**Fine-Tunning (train on a specific dataset to specific task)** - Refinement by training on narrower dataset, specific to a particular task or domain.
-> Pre-training understand the general knowledge, Fine-tunning for in-depth understanding of a field. 
![[Pasted image 20251029114349.png]]
There **2 popular fine-tunning categories:**
+ **Instruction Tunning:** labeled dataset consist of instruction-answer pairs. -> For Better Response, usually used for customer service or teaching. 
+ **Finetunning for classification task:** labeled dataset (e.g. spam/ham) consists of text & associated labels -> Improve classification ability. Often used for detection task. 

**How should you Fine-Tune:**
- ImageOCR
- Image Description 
- Image Grounding
- Video Fine Tunning