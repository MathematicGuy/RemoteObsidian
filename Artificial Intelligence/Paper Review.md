### Context
Novelty == Original
1. **Incremental Class Grouping via Max-Cut**
	Instead of treating new classes as a single block, the method organizes them into semantically coherent groups
	+ It constructs a similarity graph based on class prototypes and uses the **Max-Cut optimization** algorithm to partition classes into dissimilar groups.
	
-> This turns a complex classification problem into smaller, specialized sub-tasks.

2. **Dual-Strategy Distributional Rehearsal (DSDR)**
	To replace stored real data, the model generates synthetic features (pseudo-rehearsal).
	
	Unlike standard methods that use a single mean prototype, DSDR uses two strategies to ensure high fidelity:
	- **Archetype-based Interpolation:** Captures the global manifold structure by interpolating between representative class archetypes.
	+ **Gaussian Mixture Model (GMM) Sampling:** Captures local density and variance.
-> The final pseudo-features are a balanced mixture of these two strategies.

3. **Group-Focused Modular Training**
	The architecture uses a **frozen feature backbone** (specifically CLIP ViT-B/16 in the experiments) to maintain stable feature extraction
	
	+ It employs a **dynamic modular architecture** where new *fully connected networks and classification heads are added for new groups*.
	+ Training uses a **sparsity-inducing regularizer** that only updates the "active" groups for a given batch, preventing interference with inactive groups (knowledge preservation).

**Forgetting:** The method demonstrated significantly lower forgetting scores (10.99%) compared to the baseline CLG-CBM (14.32%) on CIFAR B-10 Inc-10

### Review
![[Pasted image 20260107215418.png]]
+ ! **Unfair Comparison:** As mentioned above, you compared your method mostly against `Continual-CLIP`, which isn't the strongest competitor anymore. They specifically requested you compare against **RAPF [ECCV 2024]** and **MG-CLIP [ICCV 2025]**.
	Reviewer specifically requested you compare against **RAPF [ECCV 2024]** and **MG-CLIP [ICCV 2025]**.
	
+ ? **Hyperparameter Clarity:** They are confused about how you selected `M` (the number of archetypes). If   this number is arbitrary, it weakens the reproducibility of your work.
![[Pasted image 20260107215425.png]]


![[Pasted image 20260107215434.png]]
+ ! **UmQx**: Believes using CLIP invalidates the experiment due to **Data Leakage**. Because CLIP was trained on *400 million image-text pairs* from the internet, the **reviewer suspects it has already "seen" the classes in your incremental tasks (CUB-200, Stanford Cars, etc.).** *If CLIP already knows these classes*, your model isn't really "learning" them incrementally; it's just remembering pre-training.
	
+ ! **Novelty is Questioned:** They argue that grouping tasks/classes by similarity is already common in _Task-Incremental Learning_ (Task-IL). You need to explicitly explain why your _Class-Incremental_ (Class-IL) Max-Cut *approach is fundamentally different or harder than existing Task-IL similarity methods.*
	
+ **Missing Non-CLIP SOTA:** They want to see how your method stacks up against recent state-of-the-art (SOTA) methods that _don't_ rely on CLIP, such as **RanPAC [NeurIPS 2023]** and **GACL [NeurIPS 2024]**.
	if you just used a better baseline (like RanPAC), you might find that grouping classes isn't even necessary to get good results.
	
![[Pasted image 20260107215444.png]]



**MG-CLIP [2025]**
![[Pasted image 20260107223112.png]]


**RAPF [ECCV 2024]**
![[Pasted image 20260107223139.png]]

---

**Task-Incremental Learning (TIL)** involves learning distinct tasks sequentially, usually with known task IDs and separate output heads (easier), while **[Class-Incremental Learning](https://www.google.com/search?client=firefox-b-d&q=Class-Incremental+Learning&mstk=AUtExfD_Ukv3O9mCkfQ_rS-hNRNcX49at4F5kucV6dYKZpRXPFjkk8BOu2UmIh7ukNhogNV4eEvZcOWZjM3i6tRvu1WLTY_2oO4Q5q2tEian1NoCfZQ5oGKdQxNw2ZLAI-L33iRuuAiObug5PXyA0u8gIpWX05E25Y3Ba4p6xgehyzX1816pSuf3SgyP-hZPNhFeF-2S0-vnI5SmM8R5SmAModChVyGrFmuJMY3-hOL6mE1IGPYGU86Q4W4C9X_H73-n5Hs2iKqYonll-TTYyBbf6cBJ&csui=3&ved=2ahUKEwjI_9O-4PmRAxVWGVkFHUvPBV0QgK4QegQIARAD) (CIL)** grows the number of classes within a single, ever-expanding classification problem, requiring cross-task discrimination without explicit task IDs (much harder). The core difference: TIL separates tasks (e.g., "cat vs. dog" then "car vs. bike"), while CIL merges them (e.g., "cat vs. dog" then "bird vs. plane," where all 4 classes must be distinguished later)
