**HMDB51 Dataset** 
	X = {I_1, I_2,...,I_n}, n_videos contain **51 classes of actions** from movies/web videos.
	**Characteristic:** Is highly Imbalance. "Walk" action is most bias -> need specific data augumentation and loss functions. 
	 
**Prediction Format:** P( Action | X ) = %
**Classess:** 51 action class
**Tackle Features -** Brightness, Blur, Constrast and Color Distribution.

| **Component**  | **Function**      | **Intuition**                                               |
| -------------- | ----------------- | ----------------------------------------------------------- |
| **HMDB51**     | Dataset           | 51 classes of actions from movies/web videos.               |
| **SMIF**       | Short-term Motion | Focuses on "what changed" between frame $T$ and $T+1$.      |
| **LMI**        | Long-term Motion  | Links information across the whole video duration.          |
| **PatchEmbed** | Tokenization      | Converts visual data into a format Transformers can "read". |
#### A. Data Preprocessing & EDA
**Frame Extraction** using *torchcodec.decoders.VideoDecoder* instead of regular frame processing *to optimize memory and performance (cpu & cuda)* 
+ ? Video have different Length 
	*$\to$ Uniform Sampling* - extract frame at equal interval  
	*$\to$ Temporal Padding* - repeating the last frame for short video to ensure a fixed input of $T=16$ frames.

**[Handle Data Imbalance](https://isi-web.org/sites/default/files/2024-02/Handling-Data-Imbalance-in-Machine-Learning.pdf#:~:text=Undersampling%20is%20a%20resampling%20technique%20used%20to,given%20equal%20importance%20in%20the%20learning%20process.) between walking and other activity**
	*Oversampling* of the Minority class *and Undersampling* of the Majority Classes using **SMOTE**.
![[Pasted image 20251226164042.png]]


#### B. Architecture (LS-ViT)
The model processes the video through several specialized stages:

`Feature Extraction Layer`
1. **SMIF (Spatial-Motion Interaction Fusion):** This module *calculates the pixel-level difference between adjacent frames* to **create a "motion map,"** helping the **model focus on moving regions.** (Important)
	
2. **Patch Embedding:** Splits frames into small 2D patches and projects them into a vector space.

`core block - like ViT`
3. **LS-ViT Blocks:** A series of Transformer layers that utilize:
	+ **Multi-Head Self-Attention (MSA):** Allows patches to relate to one another.
	+ **LMI (Long-term Motion Interaction):** A module that captures dependencies across the entire sequence of frames.
	
4. **Classifier Head:** A linear layer that takes the averaged global tokens (CLS tokens) from all frames to output the final action probability.

#### C. Training & Regularization
+ **DropPath:** Unlike standard Dropout, this "Stochastic Depth" technique **randomly drops entire residual paths to prevent overfitting** in deep networks.
	
+ **Optimization:** Uses the **AdamW** optimizer and **CrossEntropyLoss** with *mixed precision (GradScaler) to speed up training*.

---
## Human Action Recognition (HAR) Method Survey
Survey Papers:
+ [[Heatmap Pooling for Action Recognition]]

### Investigate Normalization Method in Action Recognition problem
#### IDD in Action Recognition
+ **Identical Distribution:** both **train and test dtset likely to have similar mix of all actions** and a variety of people.  
+ Independence: one existence not affect the ot
+ $ Assessing the IID property of data before using it for machine learning and, if needed, improving *the IID property is crucial for accurate and reliable results.* e.g. [using data sampling, data augmentation, data preprocessing](https://medium.com/@kapooramita/the-power-of-iid-data-in-machine-learning-and-deep-learning-models-49651afb7882). 
	NO, we could not use regular SMOTE bc they synthetic data by adding a average value between 2 similar frame or action - [[Problem with SMOTE]].

#### The Significant of IDD in ML and DL
**Deep learning models particularly sensitive to the IID property of data**. These models are complex and **highly dependent on the data they are trained on.** 
+ ! Non-IID data can lead to biased or unreliable models, resulting in low accuracy and incorrect results.

**Example of non-IDD case: [1](https://www.cs.jhu.edu/~ayuille/JHUcourses/VisionAsBayesianInference2025/20/Lecture20_BeyondMLparadigm.pdf)** 
AI vision algorithms are very successful when measured on standard academic performance benchmarks. Their performance appears to be superhuman. 
+ ! But they are less successful in the Real World. In a recent talk A. Karpathy (Vision Group Tesla) reported that AI algorithms could not detect stop signs. But stop signs are designed to be easy to detect!
+ ? What is the problem? AI algorithms do not generalize from their training set to the real world.![[Pasted image 20251231162532.png]]

![[Pasted image 20251231162635.png | 444]]

+ ? For example model learning **person-specific quirks (đặc điểm nhất định) rather than the general action itself.**  ![[Pasted image 20251231161941.png | 444]]
Not identically distributed bc the training set has data from specific group of people the model will never see during testing. 

#### Evaluating and Enhancing the IID Property of Data
Data Sampling: 

## Normalization Technique to Reduce Statistical shift (mean/variance) when the task changes in Continual Learning 
**Alternative Title:** Mitigating Catastrophic Forgetting via Statistics-Free Normalization, Reduce Moment Estimates (mean/variance) when the task changes in Continual Learning.

+ $ **Goal:** Reduce changes to the original weight even as new tasks are learned. 
+ ! **Challange:** Prevent the model from learning or adapting too much to new tasks (Catastrophic forgetting) while still learning effectively. *This is where specialized normalization like Continous Normalization come in.* 
### [Normalization Technique](https://viblo.asia/p/normalization-and-normalization-techniques-in-deep-learning-QpmleJyn5rd) in Incremental learning Task 
![[Pasted image 20251231174249.png]]

**Continual Normalization (CN)**
- **Problem Addressed**: Standard Batch Normalization (BN) uses running statistics biased towards the current task, hurting performance on past tasks.
	
- **Solution**: CN modifies BN for the online CL setting, keeping the benefits of BN (stable training) while reducing its negative cross-task effects, working well with replay methods.

**Batch Normalization (BN)**
- **The Issue**: In CL, data isn't i.i.d. (independent and identically distributed), causing BN's moment estimates to shift heavily, leading to worse performance on old tasks (catastrophic forgetting).
	
- **Workaround**: Techniques often involve careful management of running averages or combining with memory replay to expose the model to older data, counteracting BN's bias.

**Layer Normalization & Group Normalization**:
+ Alternative to BN: normalize across (channels/layers instead of batchs), less reliant on batch statistics, making them potentially more stable in non-staionary CL env.  


---
**References**
[1] - [The Power of IID Data in Machine Learning and Deep Learning Models](https://medium.com/@kapooramita/the-power-of-iid-data-in-machine-learning-and-deep-learning-models-49651afb7882)
[2] - [[Problem with SMOTE]]