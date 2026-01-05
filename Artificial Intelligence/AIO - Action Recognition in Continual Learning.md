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
+ [[Investigate Normalization Method in Action Recognition problem]] 

1. Smooth Representation -> understand Core Ideas -> Draw the whole Architecture Transparent about input and output Dimension. 
2. Effect of each Improvement ->Result Result.
3. Deadline overview -> not looking to be the first, rather in the top 5. 

**Priorities**
- [ ] Sketch LS-ViT Architecture with Input and Output Dimension + Trick to reshape vector dimension note


**LS-VIT Block Architecture**
Input -> SMIF (pixel level motion) -> ViT Backbone (Patch Embed) -> Temporal Pooling  (Temporal Pooling)

![[Pasted image 20260104034450.png]]

