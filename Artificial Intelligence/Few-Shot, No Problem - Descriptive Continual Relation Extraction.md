1.  **The Taxonomy & Classification:** *Goal: How do the authors categorize the existing work ?*

*What are the main "branches" of this field according to the paper ?*
Main branches in Continual Relation Extraction in Continual Learning listed in the paper: 


*Is there a diagram or tree structure provided? (Briefly describe it).*


*Which branch is currently the most popular or dominant?*



2.  **Evolution of the Field (Timeline):** *Goal: Understand the history and the \"milestone\" papers.*
*What was the "Before" vs. "After" moment in this research area ?*



*List 3-5 seminal papers (bài báo quan trọng) mentioned that seem essential to read later (briefly summarize the main ideas of the papers).*
Main Papers that this Paper base on: 
+ FewRel
+ CPL
+ BERT (Devlin et al., 2019): base model for evaluation 


3.  **Current State-of-the-Art (SOTA):** *Goal: Identify what is currently working best.*
*What are the standard datasets used for benchmarking?*
Experiment with BERT on 2 widely used benchmark for Relation Extraction: 
+ FewRel (Han et al.2018): 10-way 5-shot
+ TACRED (Zhang et al. 2017): 5-way 5-shot
+ *N-way:* number of classes (or relations) the model must distinguish between a single task. 
+ *K-shot:*  

*What are the common evaluation metrics (e.g., mAP, Accuracy, Perplexity) ?*
Common Evaluation Metrics: 
+ Overall Accuracy across t-task. 


*What is the current \"ceiling\" or performance limit mentioned ?*


4.  **Open Challenges & Future Directions:** *Goal: This is your source for a Research Question.*

*What problems do the authors say are still \"unsolved\"?*

*What are the limitations of current SOTA methods (e.g., cost, bias, data scarcity) ?*
+ FCRE (relied on memory-based methods) - requently suffer from overfitting to the limited samples stored in memory buffers -> Overfitting prevent positive BWT of previous learned knowledge. 
	Weak in few-shot learning scenario as the scarcity of data impedes learning on new task and hinders helpful data augmentation. 

*Are there any \"emerging trends\" the authors suggest looking into ?*



5.  **Potential Niche Selection:** *Goal: Narrowing down the scope.*
*Based on this survey, which specific sub-topic (narrow branch) interests the group most?*
**Reasoning:** Why is this niche promising? (e.g., lack of research, high impact, availability of data).


6.  **Personal Critical Reflection:**
*Did this survey miss any recent developments you are aware of ?*
+ How relatable and similar this method is *compare to Anthropic's Contextual Retrieval.* 

*How difficult is it to enter this field (entry barrier) ?*

*Application Use Case after reading the paper:* I understand the current paper trying to solve "scarcity of samples available for learning", basically mean could this model learn to detect/classified/understand this new class given K-example. 
+ *Rare Disease DIagnosis (Medical Imaging)* - hospital wants to detect 3 extremely rare bone conditions (N=3) but the hospital only has 10 confirmed scans (example) for each (K=10) -> *detect 3 samples of the new Class using just 10 examples.*
+ 


---

Cô tổng hợp và kết nối thông tin như thế nào ? 
Sau khi nghiên cứu 1 phương pháp continual learning, feature trong CV có khác với feature trong NLP hay không ?  

**Definition:**
*Reciprocal Rank:* relevant document at position R by Rank: $\frac{1}{R}$
+ RR score at top 1 = 1/1 = 1.
+ RR score at top 2 = 1/2 = 0.5 and so on.

**Research Aproach:** find SOTA 1 papers and solve their weakness on X problem ie, Few-Shot 

In order to improve on these methods, we must not completely disregard them or dwell on their weakness, but *rather contemplate their biggest strength.* 
-> Why do so many methods use the memory bugger in the first place ? 

Finding Insight -> *Based on this observation (insight)* we proposed a straightforward method: ...method explain...

Then list out Contributions: 1,2,3

**Background**
Problem Fomulation 


**Proposed Method**
what are the key challange you trying to solve e.g. *scarcity of samples available for learning.* 


**Q&A:** combine DCRE method with "Prompt-aware of Frame Sampling for Efficient Text-Video Retrieval" method. 
-> To find the Query Image better using DCRE constractive learning. For example, give the Model 4 examples of the desired Objects -> Help me the model the find the desired Object better from N frames. 

**Current Goals:** Fomula the problem for this 1 use case by simplied the problem.  