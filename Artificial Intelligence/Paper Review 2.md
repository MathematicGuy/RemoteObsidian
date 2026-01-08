### Overview
- **Reviewer Zbjt (The Benchmarker):** Accepts CLIP but argues you compared it to the wrong baselines. If you use a powerful engine like CLIP, you must race against other CLIP-based Ferraris (like RAPF, MG-CLIP), not against standard ResNet sedans. They feel your current results look strong only because the competition (Continual-CLIP) was weak.

- **Reviewer UmQx (The Skeptic):** Believes using CLIP invalidates the experiment due to **Data Leakage**. *Because CLIP was trained on 400 million image-text pairs* from the internet, the reviewer *suspects it has already "seen" the classes in your incremental tasks (CUB-200, Stanford Cars, etc.)*. If CLIP already knows these classes, your model isn't really "learning" them incrementally; it's just remembering pre-training.

**Reject Levels Note** 
- **1:** Strong Reject
- **2:** **Weak Reject** (Almost dead but still standing) - UmQx 
- **3:** **Borderline Reject** (The reviewer is leaning "No", but is hesitant) - Zbjt 
- **4:** Borderline Accept
- **5:** Weak Accept
- **6:** Strong Accept

### TODO
#### Zbjt
**Major Weakness**
- [ ] `1 Thanh` Zbij *Specifically requested* to compare against [5] **RAPF [ECCV 2024]** and [6] **MG-CLIP [ICCV 2025]**. because only benchmark agaisnt Continual-CLIP is not great. 
	
- [ ] `2` **Explain** How we select M "archetypes" for each class
	
- [ ] `3` **Benchmark Table Reformatting:** Split the main results table into two distinct sections: "CLIP-based Methods" vs. "Non-CLIP Methods" to ensure a fair comparison.
	
- [ ] `4` **Improve Experiment section flow** so the reader feel easier to read and explain why choosing such baseline.  

#### UmQx
**Major Weakness**	
- [ ] `5` **Limited Novelty:** explaining why **Class-IL** grouping (your method) is harder and different from **Task-IL** grouping (existing methods). Cite and Compare [1]
	
- [ ] `6 Thanh` Compare with **SOTA CIL** method like [2], [3], [4] 
	
- [ ] `7` Check **CLIP Data Leackage** in CUB-200, Standford Cars, etc.. -> To prove the model really "learning Incrementally not just remembering pre-training"


[1] Continual Learning of a Mixed Sequence of Similar and Dissimilar Tasks. NeurIPS 2020,
[2] **RanPAC** - Ranpac: Random projections and pre-trained models for continual learning. NeurIP-2023.
[3] Continual learning using a kernel-based method over foundation models. AAAI-2025.
[4] **GACL -** GACL: Exemplar-free generalized analytic continual learning. NeurIPS-2024.
[5] **RAPF -** Huang, Linlan, et al. "Class-incremental learning with clip: Adaptive representation adjustment and parameter fusion." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2024.
[6] **MG-CLIP -** Huang, Linlan, et al. "Mind the gap: Preserving and compensating for the modality gap in clip-based continual learning." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2025.


### Gemini Review
#### Zbjt (Borderline Reject)
- **Score:** Borderline Reject (Moderate Confidence)
- **Key Criticism:**
	
    - ! **Unfair Fight:** As mentioned above, you compared your method mostly against `Continual-CLIP`, which isn't the strongest competitor anymore. They specifically requested you compare against **RAPF [ECCV 2024]** and **MG-CLIP [ICCV 2025]**.
        
    - ? **Hyperparameter Clarity:** They are confused about how you selected `M` (the number of archetypes). If this number is arbitrary, it weakens the reproducibility of your work.
        
    - ? **Significance of Gains:** On datasets like Stanford-Cars, your *ablation study showed very small improvements when adding components*. The reviewer questions if these gains are *statistically significant or just random noise*.

#### UmQx (Weak Reject)
- **Score:** Weak Reject (High Confidence)
- **Key Criticism:**
    
    - ? **Novelty is Questioned:** They argue that **grouping tasks/classes by similarity is already common** in _Task-Incremental Learning_ (Task-IL). You need to **explicitly explain** why your _Class-Incremental_ (Class-IL) Max-Cut **approach is fundamentally different or harder than existing Task-IL similarity methods**.
        
    - **Missing Non-CLIP SOTA:** They want to see how your method stacks up *against recent state-of-the-art (SOTA)* methods that _don't_ rely on CLIP, such as **RanPAC [NeurIPS 2023]** and **GACL [NeurIPS 2024]**.
        
    - **The "Unnecessary" Argument:** The reviewer suggests that if you just used a better baseline (like RanPAC), you might find that grouping classes isn't even necessary to get good results.


