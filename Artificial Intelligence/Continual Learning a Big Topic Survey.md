### 1. The Taxonomy & Classification - How do the authors categorize the existing work ?
*What are the main "branches" of this field according to the paper ?*
![[Pasted image 20260324190239.png]]
Continual Learning, CL in short. A field focus on teaching AI "learning how to learn" (meta learning). Each CL sub-field enhance the model ability to learn. 

For context, Catastrophic Forgeting (CF) where model forget old task while learning new task without re-training on the whole dataset is the main problem in CL. Research have to find a method that satisfied the Stability (remember Old task) and Plasticity (learn new task) tradeoff. Approaches to solve CF often requires researcher to combine multiple CL methods (e.g Replay, Architecture, Representation, Regularization and  Optimization) that synegize with eachother to solve a specific sub-problem in CL or a downstream task like "Multi-Domain Sentiment Classification, Continual Relational Extraction in scarce data scenario, Continual Object Recognition in Robotics, etc..". 
![[Pasted image 20260214200246.png | 678]]

*Which branch is currently the most popular or dominant ?*
Replay is the most Dominant branch with High performance ceiling and low-skill entry difficulty. Often use in Downstream CL task (e.g. Multi-Domain Sentiment Classification, Continual Relational Extraction in scarce data scenario, Continual Object Recognition in Robotics). 

| Method Categories (Rank by Popularity) | Paper Count |
| -------------------------------------- | ----------- |
| Replay                                 | 74          |
| Regularization                         | 28          |
| Representation                         | 31          |
| Optimization                           | 28          |
| Architecture                           | 36          |


### 2. Evolution of the Field (Timeline) - Understand the history and the "milestone" papers.
*What was the "Before" vs. "After" moment in this research area ?* 

In term of Evaluation dataset
+ ! Before: CL was highly unstructured and lacked a shared framework, a lot of SoTA without clear proof understand 1 evaluation frameowkr. 
+ ? After: CL formalize 3 fundamental scenarios: Task-Incremental, Domain-Incremental, and Class-Incremental Learning.

In term of Goals
+ ! Before: Most research simply focus to overcome Catastrophic Forgetting (CF) by freezing important weights (note: weights update when model updating is 1 of the main reason of CF) or regularising params to protect old knowledges (regularization  introduce 2 loss function, Loss for old knowledge and Loss for new knowledge). 
+ ? After: Researcher community realised that an excess of memory stability hurts the model's ability to learn new things. Research shift to a proper stability-plasticity trade-off alongside inter-task generalizability (ie. learn task A also help model to learn task B) like "Flat Minima".   ![[Pasted image 20260215105345.png]] *-> In Flat Minima* when features are widely distributed there are more room to insert new classes or task without them overlapping with old ones. 


In term of Scale from "Training LLM from Scratch" to "Updating LLM"
+ ! Before CL replying on expanding the architecture of MLP, CNN by adding new neurons for new task (e.g. Constrain a group of Neurons to learn a different task -> Scale them up) or branches (kind of like Classification Tree). ![[Pasted image 20251222220720.png]]
+ ? After the explosion of LLM (Transformer), paradigm shift toward "Continual Pre-Training" for updating mass-scale of params without destroying LLm zero-shot capabilities by leveraging *PEFT, LoRA* adapter to instruct frozen backbones rather than retraining or expanding entire network, *Prompt-Tuning* to guide model for specific task, *Constractive Loss* to optimize the latent space by pulling similar features together while pushing disimilar features further (kind of like K-Mean). 
	Note: Loss in Constractive Learning map data into high-dim space where similarity is maximized while K-Mean isn't. 

In term of ours Theoretical Misunderstanding - source: [Mathematic of Continual Learning](https://youtu.be/jwGOSGphIF4?si=FKOv4rqYreRtPb4D)
+ ! Before: CL is the modern solution for Modern Deep Learning. 
+ ? After CL actually started in the 1960 rooted from LMS & Adaptive Signal Processing (e.g. Kalmen Filter)  
LMS introduce **"Principle of Minimal Disturbance."** Which is the ancestor of modern regularization in CL. States that a system should adapt to reduce error on a current training pattern with the "Smallest extent possible" of disturbance to stored information. - update on current task while trying not to deviate from what was learned previously. 
![[Pasted image 20260223154110.png]]
Modern heuristic techniques—like Gradient Projection and even Linear Attention in Transformers—are mathematically equivalent to classical algorithms like the Affine Projection Algorithm and Least Mean Squares (LMS)
![[Pasted image 20260223154140.png]]


*List 3-5 seminal papers (bài báo quan trọng) mentioned that seem essential to read later (briefly summarize the main ideas of the papers).*

**OGD (Orthogonal Gradient Descent)** - a *Optimization approaches*, preserves the old gradient directions and rectifies the current gradient directions orthogonal to them. This ensures the update is "safe" for previous tasks.

**Nested Learning** (M3 Optimizer, HOPE Architecture (Titan + CMS + M3))
*Explain in Paper:* In Nested Learning, a ML Model as a set of nested, multi-level, and/or parallel optimization problems, each of which with its own “context flow”. By that  mean, the author design more learning algorithms with more “levels” where each Layer have a different update frequency.

**In plain English**: Nested Learning is a new way of thinking about deep learning models. Instead of viewing neural networks as fixed architectures, it treats them as nested optimization problems where different parts update at different speeds - like having fast, short-term memory and slow, long-term memory working together.
![[Pasted image 20260324210100.png]]
![[Pasted image 20260324210957.png | 233]]


-


### 3. Current State-of-the-Art (SOTA) - Identify what is currently working best.
*What are the standard datasets used for benchmarking?*
+ For Incremental Learning task in Computer Vision: CIFAR-100, ImageNet-100, MNIST (Permuted MNIST, CUB-200. 
+ For Few-shot Continual Relation Extraction: FewRel (10-way, 5-shot), TACRED (5-way, 5-shot). 


*What are the common evaluation metrics (e.g., mAP, Accuracy, Perplexity) ?*
OP (%) - Overall Performance (Overall Accuracy up to the current task), higher the better.
BWT (%) - Backward Transfer, lower the better
Time (s) - Training Time


*What is the current \"ceiling\" or performance limit mentioned ?*
1. **Scarcity of Labeled Data** - Most of the current continual learning settings assume that incremental tasks have sufficiently large amounts of labeled data, which is often expensive and difficult to obtain in practical application

2. **Task-Agnostic Inference (what you predict might not what you trained on)** in CIL, train the model to classified Class that might not in the current training batch (e.g. Task 4 train on "Tiger and Dog" but the model have to predict if the sample "a cat or dog" from Task 3) -> Trainset & Testset lable might not match.  
	Task-agnostic inference requires the model to choose from all classes seen across all tasks


### 4. Open Challenges & Future Directions - This is your source for a Research Question.

*What problems do the authors say are still "unsolved" ?*
1. **Catastrophic Forgetting:** training with new data completly leed to complete tweak/adjustment in model weights -> forgot old task while learning new task.     
![[Pasted image 20260210141507.png]]


4. **Open World / Out-of-Distribution (OOD):** fail when encountering unknown classes (e.g. fashion classifier seeing an animal)
	Most ML models are overconfident. They "don't know when they don't know" ![[Pasted image 20260210142104.png]]

*What are the limitations of current SOTA methods (e.g., cost, bias, data scarcity) ?*
+ Data Scarcity and Annotation Cost: Most continual learning setups assume that tasks provide sufficiently large amounts of labeled data
	-> Demand to research Few-Shot Continual Learning (FSCL) and unsupervised/semi-supervised scenarios where labeled data is extremely limited. 

+ Bias and Overfitting from Limited Memory when using Experience Replay. 

+ Resource and Computational Costs: Scability in Architecture-based approaches and Computation overheads in Generative Replay. 

+ NP-Hard: mathematically mean finding an optimal shared parameter space that accommodates all new task without intefering with old ones. As more tasks are added, the feasible "safe" space also narrow down or entirely non-existent. 


*Are there any "emerging trends" the authors suggest looking into ?*

+ Shift from Memory Stability to Plasticity and Generalizability -> Adaptive Model that generalize better when there distribution shift between tasks.  
	Like the Titan model, focus only on what is Important at the current time.

+ Flat loss landscapes - flat landscape (wide local/global minima) reduce sensitivity in parameter changes when learning new tasks (e.g. 3 tasks have the same Minima)

+ MoE - each sub-model trained for a different task, the researcher focus on directing which task to which model rather than optimize the model itself.

+ Orthogonal LoRA (O-LoRA) - Orthogonal help avoid udpate conflict while LoRA for optimize parameter update. 


### 5. Potential Niche Selection - Narrowing down the scope
*Based on this survey, which specific sub-topic (narrow branch) interests the group most?*
Approaches: 
+ Representation (Constractive Learning)
+ Replay (Feature Replay)
+ Architecture (LoRA)
+ Optimization (Orthogonal method like GEM, OPL)

### 6. Personal Critical Reflection
*Did this survey miss any recent developments you are aware of ?*
The paper miss Nested Learning

*How difficult is it to enter this field (entry barrier) ?* 
reference: [NotebookLM](https://notebooklm.google.com/notebook/a5a4f271-a225-4f32-bd54-7a4a580df8cc) and Experience
Generally *Hard to Very Hard for a Begineer:* 
+ Require deep understanding of how AI model learn (teaching the model learning how to learn)
+ Without Mentor guidance, its *Very Hard Fomulate Specific Research Question* required *multi-disciplinary* knowledge in AI from 
	+ Out-of-Distribution Data (OOD), Non-Stationary Data in ML.
	+ LLM, NLP/CV to Fine-tuning. While balance memory, compute efficiency, and privacy. 
	+ General Understanding about each Continual Learning approaches Method, How ML/DL learn, Modify the Base model (CNN, Transformer, BERT, ViT).  ![[Pasted image 20260312180513.png]] For example, connect a specific problem from NLP/CV with CL.
	
+ Often, you have to *combine multiple approach in a CL paper*.


+ Security Speaking - Continual Learning is very Prone to Prompt Injection ([What so hard about continual learning](https://www.seangoedecke.com/continuous-learning/))
