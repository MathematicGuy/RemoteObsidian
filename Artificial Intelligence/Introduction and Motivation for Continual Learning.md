### Transitioning to Lifelong Learning
**Static ML Workflow**
![[Pasted image 20260210133245.png]]
**Concept Drift:** Real-world concepts change over time (e.g., the design of laptops), making static snapshots insufficient
+ ? Can we just Iterate standard ML workflow continously ? No
+ ! Simply looping is insufficient bc the data distribution shifts -> failure model
![[Pasted image 20260210141132.png]]
`Flesch et al. Modelling continual learning in humans with Hebbian context gating and decaying task signals', preprint, 2022`
Trad ML algo heavily dependence on Data Distribution, or else it will get biases. 
-> Machine learning typically shuffles data & performs poorly when data is ordered.

### Major Challenges in Open World Learning
**Problems:**
1. **Catastrophic Forgetting:** training with new data completly leed to complete tweak/adjustment in model weights -> forgot old task while learning new task.   
2. In Realtime learning where data get train and validate continuously, model have **no access to revisiting of prior "task" data** ! -> Solution: Replay
![[Pasted image 20260210141507.png]]

3. **Open World / Out-of-Distribution (OOD):** fail when encountering unknown classes (e.g. fashion classifier seeing an animal)
	Most ML models are overconfident. They "don't know when they don't know" ![[Pasted image 20260210142104.png]]

**4. The Reproducibility and Drift / Open World Workflow (The Training Cycle)** 
Even if a new set of ImageSet dataset are preprocessed exactedly like the old one, if we take the old model trained on old data and evaluate its on new data, the accuracy still drop.   
-> Traditional steps is insufficient because new challenges (Drift, Forgetting, Openness) break the standard algorithms at every stage. Bc the model was frozen in time (static), but the real worlds data distribution shifted as new data was added. 
+ ? given that the model wasn't retrained entirely, bc that too expensive and inefficient.
![[Pasted image 20260210142943.png# left | 455]]
`Mundt et al, "A Wholistic View of Continual Leaming with Deep Neural Networks: Forgotten Lessons and the Bridge to Active and Open World Leaming, preprint arXiv:2009.01797`
**What if we want to add data over time ?**
	How to pick data ?
	Does the data belong to the task ?
	How similar is the data ?
	How optimize accumulated error (is this even what we want ?)
+ ? What kind of data would you intuively pick ? 



**Challange: Adapting models**
![[Pasted image 20260210143841.png]]
`Wu & Liu et al. *Firefly Neural Architecture Descent: A General Approach for Growing Neural Networks", NeudPS 2020`
But is our initial model choice and its practical
	realization still good enough ?
	What if complexity changes ?
	Or even the inductive bias should be altered ?
	
**Advanced Learning Strategies**
+ *Active Learning:* In the datastream, which data the model should prioritize to learn next. Should it picking "hard" examples or maximizing novelty (new and unique). (e.g. Titans, the model learn data base on sample entropy, only learn new/hard example)
	*Intuition:* Instead of picking the knowledge its already know on the Buffer (resevoir method), the model target its specific weakness rather than reviewing data it already understands.  
		high novelty data contain new concept or new category that the model unaware of.  
	*Risk (why this is difficult):* hard example often get confused with noise and unuseful information as they both "hard to predict". 
	
+ *Curriculum Learning:* like human, the model trained on easy samples firsts (like frequency word or simple image) and the hard samples later -> improve performance and learn faster. 
	*Intuition:* Teach the model the basic first (image with simple background) so it can generalize the ideas/features first, then progressively add harder example (image with noise/clutter) for it to learn the core feature + noise. ![[Pasted image 20260210164316.png# left | 344]] *Example:* Ranking LLM trained with vs without curriculum on Wikipedia
	1)  The curriculum-trained model skips examples with words outside of 5k most frequent words
	2) Then skips examples outside 10k most frequent words and so on
	![[Pasted image 20260210165532.png# left | 344]]`Wang et al. "A Survey on Curriculum Leaming•, TPAMI 2021`
	
+ *Dynamic Capacity:* the model growth as new data added. (e.g. new data saved to new params)

### Course Roadmap & Objectives
![[Pasted image 20260210144122.png]]
`Kudithipudi et al, "Biological underpinnings for lifelong leaming machines', Nature Machine Intelligence (4), 2022`
Note from the video: 
+ **Holistic Goal:** build system learning continously like human 
+ **Software:** A future lecture will be dedicated to the software and frameworks that enable these continual learning systems.
+ **Future Topics:** Open World Learning, Active Learning, Zero-shot Learning, Domain Adaptation, and Transfer Learning, eventually integrating them into a unified Lifelong Learning framework.

*Continual dependencies & sunergies*
![[Pasted image 20260210171813.png]]

Key word for Continuos Learning Topic - how are they interconnect
![[Pasted image 20260210171920.png]]
`Mundt et al. CLEVA-Compass: A Continual Learning Evaluation Assessment Compass to Promote Research Transparency and Comparability", ICLR 2022`


---


### Continous Learning to Continous Learning Modle
[Continous Learning Model example](https://www.reddit.com/r/singularity/comments/1hcm93m/were_likely_much_closer_to_continuouslearning/) 
1.	Recognize it’s failing or underperforming on the task 
	-> Active Learning
2.	Hypothesize what kind of training or experience it needs to improve 
	-> LLM ? 
3.	Agentically search for existing datasets and create reinforcement simulations tailored to its specific deficits 
	-> RAG / Agentic System
4.	Run those simulations, fine-tune itself, and try again—without any hand-holding from developer 
	-> Reinforcement Learning
