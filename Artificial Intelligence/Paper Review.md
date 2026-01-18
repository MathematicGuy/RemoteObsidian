### Review
![[Pasted image 20260107215418.png]]


![[Pasted image 20260107215434.png]]

**Ours**
![[Pasted image 20260114085509.png]]


**MG-CLIP [2025]**
![[Pasted image 20260107223112.png]]


**RAPF [ECCV 2024]**
![[Pasted image 20260107223139.png]]



**Avg:** The mean accuracy across all incremental stages.
**Last:** The accuracy after the final task is learned.

|Benchmark|Metric|**SGC**|**RAPF**|**MG-CLIP**|
|:--|:--|:-:|:-:|:-:|
|**CIFAR-100**|**Avg**|**87.36%** (B-10)|86.19% (B-0)|87.00%|
|_(10 Tasks)_|**Last**|**80.95%** (B-10)|79.04% (B-0)|80.57%|
||||||
|**ImageNet-100**|**Avg**|—|**87.51%**|87.31%|
|_(10 Tasks)_|**Last**|—|**80.23%**|78.38%|
||||||
|**ImageNet-R**|**Avg**|—|86.28%|**87.58%**|
|_(10 Tasks)_|**Last**|—|79.62%|**82.67%**|
||||||
|**ImageNet-1K**|**Avg**|—|81.73%|**81.88%**|
|_(10 Tasks)_|**Last**|—|72.58%|**73.68%**|
||||||
|**CUB-200**|**Avg**|**86.18%** (Inc-10)|83.04% (Inc-20)|—|
||**Last**|Not Reported|76.34% (Inc-20)|—|
||||||
|**VTAB**|**Avg**|—|—|**94.67%**|
|_(5 Tasks)_|**Last**|—|—|**91.53%**|






**1. Replay vs. Non-Replay Strategy**

- **SGC (Pseudo-Rehearsal):** SGC achieves the highest numbers on CIFAR-100 and CUB-200, but it relies on **Dual-Strategy Distributional Rehearsal (DSDR)**. This means it generates synthetic features (using GMMs and archetypes) to "rehearse" old knowledge.
- **RAPF (Feature Replay/Storage):** RAPF uses Gaussian distributions to model old classes. While it claims to not store raw images, **MG-CLIP** argues that RAPF requires storing a covariance matrix for every class ($nd^2$), which creates a memory overhead that grows with the feature dimension.
- **MG-CLIP (Replay-Free):** MG-CLIP explicitly claims to outperform replay-based methods (like RAPF and CLAP) on difficult benchmarks (ImageNet-R, VTAB) **without** requiring additional replay data or storage.

**2. Stability vs. Plasticity**

- **ImageNet-100:** RAPF performs slightly better than MG-CLIP here. This suggests that RAPF's strategy of actively adjusting representations using text guidance may be slightly more effective on standard object datasets when memory storage is allowed.
	
- **ImageNet-R (Robustness):** MG-CLIP significantly outperforms RAPF (by ~3% in Last Accuracy) on ImageNet-R. This dataset contains diverse art styles (cartoons, graffiti), suggesting that MG-CLIP's strategy of **preserving the modality gap** retains the pre-trained model's generalization capabilities better than RAPF's adaptation method.

**3. Zero-Shot Retention**

- **MG-CLIP** emphasizes preserving the **Zero-Shot** capability of the original model. After training on CIFAR-100, MG-CLIP actually _improved_ the model's zero-shot performance on ImageNet-1K by 2.85% compared to the original CLIP.
	
- In contrast, **RAPF** (and other replay methods) experienced significant performance declines on zero-shot tasks after training, suggesting they may overfit to the incremental tasks at the expense of general knowledge.

----

**CIFAR-100:** A dataset containing 60,000 tiny images (32x32 pixels) across 100 classes (e.g., vehicles, animals). It is a standard benchmark for testing a model's ability to learn distinct categories from low-resolution data.

**ImageNet-1K (ImageNet):** A large-scale dataset with roughly 1.2 million images across 1,000 diverse categories. It tests the model's scalability and ability to handle complex, real-world visual data.

**ImageNet-100:** A subset of ImageNet-1K containing only 100 classes. It is used for faster experimentation while maintaining the high resolution and complexity of ImageNet images.

**ImageNet-R (Rendition):** Contains 30,000 images of 200 ImageNet classes, but in different styles (art, cartoons, graffiti, embroidery). It tests the model's **robustness** and ability to generalize across different visual domains (domain shift).

**CUB-200 (Caltech-UCSD Birds):** A fine-grained dataset containing 11,788 images of 200 bird species. It challenges the model to distinguish between very similar sub-categories (e.g., different types of sparrows).

**VTAB (Visual Task Adaptation Benchmark):** Used specifically by **MG-CLIP**, this suite includes diverse tasks (natural, specialized, and structured images). It evaluates how well a model adapts to tasks significantly different from its pre-training data