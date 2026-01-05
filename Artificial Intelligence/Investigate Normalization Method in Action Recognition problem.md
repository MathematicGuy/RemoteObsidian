#### IDD in Action Recognition
+ **Identical Distribution:** both **train and test dataset likely to have similar mix of all actions** and a variety of people.  
+ Independence: one existence not affect the ot
+ $ Assessing the IID property of data before using it for machine learning and, if needed, improving *the IID property is crucial for accurate and reliable results.* e.g. [using data sampling, data augmentation, data preprocessing](https://medium.com/@kapooramita/the-power-of-iid-data-in-machine-learning-and-deep-learning-models-49651afb7882). 
	NO, we could not use regular SMOTE bc they synthetic data by adding a average value between 2 similar frame or action - [[Problem with SMOTE]].

#### The Significant of IDD in ML and DL
**Deep learning models particularly sensitive to the IID property of data**. These models are complex and **highly dependent on the data they are trained on.** 
+ ! Non-IID data can lead to biased or unreliable models, resulting in low accuracy and incorrect results.


**Example of non-IDD case: [1](https://www.cs.jhu.edu/~ayuille/JHUcourses/VisionAsBayesianInference2025/20/Lecture20_BeyondMLparadigm.pdf)** 
AI vision algorithms are very successful when measured on standard academic performance benchmarks. Their performance appears to be superhuman. 
+ ! **But they are less successful in the Real World.** In a recent talk A. Karpathy (Vision Group Tesla) reported that AI algorithms could not detect stop signs. But stop signs are designed to be easy to detect!
+ ? What is the problem? AI algorithms do not generalize from their training set to the real world.![[Pasted image 20251231162532.png]]

![[Pasted image 20251231162635.png | 444]]

+ ? For example model learning **person-specific quirks (đặc điểm nhất định) rather than the general action itself.**  ![[Pasted image 20251231161941.png | 444]]
Not identically distributed bc the training set has data from specific group of people the model will never see during testing. 

#### Evaluating and Enhancing the IID Property of Data
+ **Data Sampling:** Choosing a representative subset to ensure data is IID. 
+ **Data Augmentation:** Generate new training examples from existing data -> Enhance the IID property of data by increasing diversity of training data. 
+ **Data Preprocessing:** transforming the data to make it more IID, such as **normalizing the data to have mean of 0 and a standard** 

## Normalization Technique to Reduce Statistical shift (mean/variance) when the task changes in Continual Learning 
**Alternative Title:** Mitigating Catastrophic Forgetting via Statistics-Free Normalization, Reduce Moment Estimates (mean/variance) when the task changes in Continual Learning.
+ $ **Goal:** Reduce changes to the original weight even as new tasks are learned. 
+ ! **Challange:** Prevent the model from learning or adapting too much to new tasks (Catastrophic forgetting) while still learning effectively. *This is where specialized normalization like Continous Normalization come in.* 

### [Normalization Technique](https://viblo.asia/p/normalization-and-normalization-techniques-in-deep-learning-QpmleJyn5rd) in Incremental learning Task 
![[Pasted image 20251231174249.png]]



**Batch Normalization (BN)**
1. normalization activation func output $$\hat{z} = \frac{x - \mu }{\sqrt{ \sigma^{2} + \epsilon }}$$
2. $$y_{i} = \gamma \hat{z_{i}} + \beta$$
- **The Issue**: In CL, data isn't i.i.d. (independent and identically distributed), causing BN's moment estimates to shift heavily, leading to worse performance on old tasks (catastrophic forgetting). 
+ ? Because Batch normalization **relies on computing mean and variance ($\mu, \sigma$) within each mini-batch**, if the mini-batch size is too small the estimates of mean and variance become noisy, reducing its effectiveness. This may make the training **unstable or lead to poor performance.** [3](https://dzdata.medium.com/the-different-types-of-normalizations-in-deep-learning-03eece7fa789)
	
- **Workaround**: Techniques often involve careful management of running averages or combining with memory replay to expose the model to older data, counteracting BN's bias.


**Layer Normalization & Group Normalization**:
+ Alternative to BN: normalize across (channels/layers instead of batchs), less reliant on batch statistics, making them potentially more stable in non-staionary CL env.  
+ ? Unlike batch normalization, LN does not depend on the mini-batch size. It works effectively for small batch sizes and for single-sample training (e.g., in online learning). Moreover, **because it normalizes each sample independently it is particularly effective in sequential processing models** (like RNN) where the sequence length and structure may vary.

**Continual Normalization (CN)**
- **Problem Addressed**: Standard Batch Normalization (BN) uses *running statistics biased towards the current task*, hurting performance on past tasks.
	
- **Solution**: CN modifies BN for the online CL setting, keeping the benefits of BN (stable training) while reducing its negative cross-task effects, working well with replay methods.


![[Pasted image 20260101092307.png]]
+ ? $\gamma$ (scaling) and $\beta$ (shifting) (update the same as like weight as bias). Where *1 Scale* the original Normalization value and *1 shift to Stabalize* the normalization value.
+ $ **Affine Parameters:** Unlike the GN step, this step _does_ use the learned affine parameters (`self.weight` and `self.bias`) and tracks/uses the global `running_mean` and `running_var` 
+ @ **Purpose:** This step allows for knowledge transfer across tasks. **By calculating statistics across the mini-batch, the model can generalize better**. However, because the input (`out_gn`) was already **spatially normalized**, the **batch statistics are less biased towards the specific distribution of the current task**, reducing the "cross-task normalization effect" that usually causes forgetting in standard Batch Norm.

![[Pasted image 20260101095031.png]]


**Batch/Group Norm:** 
`(Batch, Channel, Height, Width)`
**Layer Norm** (Chiều đang dùng cho code ViT)
`(Batch, Temporal, Channels)`  - Temporal 
![[Pasted image 20260101091112.png]]


![[Pasted image 20260101090854.png]]
![[Pasted image 20260101093234.png]]



---
**References**
[1] - [The Power of IID Data in Machine Learning and Deep Learning Models](https://medium.com/@kapooramita/the-power-of-iid-data-in-machine-learning-and-deep-learning-models-49651afb7882)
[2] - [[Problem with SMOTE]]
[3] - [Normalization in Deep Learning](https://dzdata.medium.com/the-different-types-of-normalizations-in-deep-learning-03eece7fa789)