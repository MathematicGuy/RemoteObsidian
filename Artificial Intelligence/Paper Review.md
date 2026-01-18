### Review
![[Pasted image 20260107215418.png]]


![[Pasted image 20260107215434.png]]

**Ours**
![[Pasted image 20260114085509.png]]


**MG-CLIP [2025]**
![[Pasted image 20260107223112.png]]

![[Pasted image 20260117171201.png]]


**RAPF [ECCV 2024]**
![[Pasted image 20260107223139.png]]

![[Pasted image 20260115034547.png]]

![[Pasted image 20260115054059.png | 544]]

**Implement Details Comprison**
![[Pasted image 20260115054631.png]]

![[Pasted image 20260115054552.png | 522]] 


---
**Main Testing Decision:**

+ (IMPORTANT) Test Ours on **ImageNet-R (1.01GB) (YES),  ImageNet-1K (10.9GB) (YES) and ImageNet-100 (16.1GB) (YES)**
	-> For Citation we must run our Model on their chosen dataset. 
	Note: 
	+ Need clarify for Efficiency ? Ours train 60 epochs (x4 more), RAPF train 15 epochs but ours SGC training fresh classification heads (unlike RAPF's adapters).
	
+ **Zero-shot on Food-101:** MG-CLIP (85.7%), RAPF (17.18%), Ours (???)
	Zero-shot performance *after completing all class-incremental learning tasks on CIFAR-100*
	-> Measure catastrophic forgetting of pre-trained knowledge. Check if fine-tuning the model on CIFAR-100 damaged its ability to recognize other concepts (like food).
	
+ (Quick but require setup) **CUB-200 (Inc-10)** test on RAPF and MG-CLIP. However, we would need to clarify ours experiement method on their code. 
	-> Ensuring we *aren't accused of misrepresenting their official numbers* and respects their algorithm. Luckly, **MG-CLIP paper itself did exactly this, we could do the same.**
	 
In **Table 1** of the MG-CLIP said "The results are mainly obtained from references [12, 13] and **reproduced using their publicly available code**."
![[Pasted image 20260115052731.png]]

**Avg:** The mean accuracy across all incremental stages.
**Last:** The accuracy after the final task is learned.

| Benchmark            | Metric   |       **SGC**       |    **RAPF**     | **MG-CLIP** |
| :------------------- | :------- | :-----------------: | :-------------: | :---------: |
| **CIFAR-100**        | **Avg**  |  **87.36%** (B-10)  |  86.19% (B-0)   |   87.00%    |
| _(10 Tasks)_         | **Last** |  **80.95%** (B-10)  |  79.04% (B-0)   |   80.57%    |
|                      |          |                     |                 |             |
| **ImageNet-100**     | **Avg**  |      **TEST**       |   **87.51%**    |   87.31%    |
| _(10 Tasks)_         | **Last** |          —          |   **80.23%**    |   78.38%    |
|                      |          |                     |                 |             |
| **ImageNet-R**       | **Avg**  |      **TEST**       |     86.28%      | **87.58%**  |
| _(10 Tasks)_         | **Last** |          —          |     79.62%      | **82.67%**  |
|                      |          |                     |                 |             |
| **ImageNet-1K**      | **Avg**  |      **TEST**       |     81.73%      | **81.88%**  |
| _(10 Tasks)_         | **Last** |          —          |     72.58%      | **73.68%**  |
|                      |          |                     |                 |             |
| **CUB-200 (1.49GB)** | **Avg**  | **86.18%** (Inc-10) | 83.04% (Inc-20) |   TEST ?    |
|                      | **Last** |    Not Reported     | 76.34% (Inc-20) |      —      |


![[Pasted image 20260115043630.png# left]]
*Zero-shot performance* of the model on different downstream datasets *after completing all class-incremental learning tasks on CIFAR-100*
+ $ **Objective:** The goal was to measure **catastrophic forgetting of pre-trained knowledge**. Since the original CLIP model already performs well on Food-101 (zero-shot), this test checks if fine-tuning the model on CIFAR-100 damaged its ability to recognize other concepts (like food).
-> Test on ours SGC ? Competition and Valuable insight here. 
![[Pasted image 20260115044540.png]]



----

**CIFAR-100:** A dataset containing 60,000 tiny images (32x32 pixels) across 100 classes (e.g., vehicles, animals). It is a standard benchmark for testing a model's ability to learn distinct categories from low-resolution data.

**ImageNet-1K (ImageNet):** A large-scale dataset with roughly 1.2 million images across 1,000 diverse categories. It tests the model's scalability and ability to handle complex, real-world visual data.

**ImageNet-100:** A subset of ImageNet-1K containing only 100 classes. It is used for faster experimentation while maintaining the high resolution and complexity of ImageNet images.

**ImageNet-R (Rendition):** Contains 30,000 images of 200 ImageNet classes, but in different styles (art, cartoons, graffiti, embroidery). It tests the model's **robustness** and ability to generalize across different visual domains (domain shift).

**CUB-200 (Caltech-UCSD Birds):** A fine-grained dataset containing 11,788 images of 200 bird species. It challenges the model to distinguish between very similar sub-categories (e.g., different types of sparrows).

**VTAB (Visual Task Adaptation Benchmark):** Used specifically by **MG-CLIP**, this suite includes diverse tasks (natural, specialized, and structured images). It evaluates how well a model adapts to tasks significantly different from its pre-training data