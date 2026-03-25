*1st Priority:* FOCUS on Understand the current paper. 
*2nd Priority:* Risk Assessment and Feasibility.
*3rd Priority:* Turn information into Slides for Saturday Representation. 

## Brief Overview - Introduction
SoTA approaches to FCRE relied on memory-based methods - *frequently suffer from overfitting to the limited samples* stored in memory buffers -> prone to *Overfitting and Prevent positive BWT.* 
	Weak in few-shot learning scenario as the *scarcity of data amplified this weakness* , limit the model from learning on new task and hinders helpful data augmentation. 
+ ? Problem: *Replay sample can be ambiguous, may not always be representative of the entire class.* 

 **3 Contributions to solve this Problem:** 
1.  *Generate Comprehensive Description for each Relation:* add description for replay sample, serve as *stable class represetnation in the latent space during training.* 

2. *Design a Bi-Encoder Retrieval Learning Framework* integrate Description-Pivot learning process to *Maximize the proximity between a sample and tis corresponding description.* 

3. *Descriptive Retrieval Inference (DRI) strategy* to enhanced representation which *"retrieves" the most fitting relation* using a reciprocal rank (e.g. Top-K) fusion score that integrates both class descriptions and class prototypes.
	+ Class Description:
	+ Class Prototypes:
-> retrieval-based paradigm 



## Concise Overview
Provide a concise overview of the methodology or approach used in the study, including the data sources, data collection and analysis methods, and any statistical techniques

### Problems
**The "Old" Way: Example-Based Replay**
Traditional models use a **Memory Buffer** that stores a few "unrepresentative" samples (like 5 random sentences) for each old relation.
+ ! If those 5 sentences are weird or don't cover the whole meaning of the relation, the model gets confused and "overfits" to those specific bad examples.

### Methodology 8
 **Proposed solution:** 
 + $ besides relying on potentially unrepresentative past samples, we *leverage our knowledge of the past relations themselve* by adding detailed description for each relation. 
+ @ Add description for replay sample, serve as stable class represetnation in the latent space during training. 



### Approaches



### Data sources
Experiment with BERT on 2 widely used benchmark for Relation Extraction: 
+ FewRel (Han et al.2018): 10-way 5-shot
+ TACRED (Zhang et al. 2017): 5-way 5-shot


### Data collection


## Primary Findings and Experiment Results
Highlight the primary findings or results of the research. Use *clear and straightforward language* to communicate these findings. If the paper includes figures, tables, or graphs, refer to them as needed.
![[Pasted image 20260325155737.png | 555]]



## Summary and Assessment
Conclude your summary with a closing statement that provides an overall assessment of the paper, such as its *significance, relevance, or potential for future research*





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

*Feasible:* yes, have access to LLM and academic resource. 

----
### What Next ?
Note: 
+ Analyse how Ad fomulate his research question across multiple subject. 

*Fomulate our Own Research Question* - from what we learned from this paper on "Continual Relational Extraction" topic in "Data Scarcity" environment. Formulate a clear and focuses research question.
-> Method to Improve on the current topic -> Mentor feedback -> Finalize RQ (research question). 

*Example Question to ask:*
RQ1: How to *improve the performance* of existing `Continal Relational Extracction` Method methods under various `X` conditions and complex `data` properties?

RQ2: How to *obtain a real-time processing* for current state-of-the-art `Continal Relational Extracction` based deep learning methods?

RQ3: How to *design an automatically learning the network architecture*, its activation
functions, and its parameters from data ?

After understand the fundamental of the current Research Topic, assest the difficulty of my RQ (e.g.  "Continual Relational Extraction for Hand Gesture Recognition" topic in "Data Scarcity" 
-> Make sure the chosen topic have a *clear research gap.* 
+ ? After Feedback, Refine all of your Research Question. 

**Example Use Case - Text-Image Retrieval System** 
In Depth Review of the Current (specific) Topic -> Have a *Clear Vision how the Whole System* and Pipeline work 
![[Pasted image 20260325154937.png | 666]]
And Track performance of SoTA paper accuracy. Then Verifying the feasibility of Research Topics, these include:
+ Ethical and Legal Consideration
+ Collaboration Oppotunities (in your Contry and Relationship)
+ Risk Assessment 
	+ How much time will this take ? 
	+ What is the Cost ?
+ Feasible Study (List our fact)
