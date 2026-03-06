Note: 
+ *Standardization basically "Centering and Scaling"* where $\mu$ is the *mean of the feature that help center* the data and $\sigma$ is the *standard deviation of the feature that help scale* the data.
+ *Normalization* help *adjusting values measured on different scales to a symmetry/ scale* so High and Low values could be evaluation and treated more equally. 
	Example usecase: Use log to adjust 1000 and 10 to a same scale, normalize house price features so large scale values doesn't dominate smaller scale values.


### Scaling & Shifting
> transform every data point to smaller or larger value while still maintain the distribution between each data point.
![[Pasted image 20241015154308.png]]
>Choose a specific value over the data -> normalization 


### Normalization
![[Pasted image 20240719091104.png]]

**Example**
![[Screenshot 2024-10-15 152130.png]]





![[Pasted image 20240719091158.png]]
+ ! This is not normal distribution. Bc it a linear transformation

![[Pasted image 20240719091421.png]]

For example you have 2 point as 2 features and compute the distance between 2 features. But 1 feature have much bigger value than other feature. 
![[Pasted image 20241015155021.png]]

Higher value doesn't mean it more important -> by rescaling each features contribute roughtly to the distance.
![[Pasted image 20240719091629.png]]

# Standardization (Z-Score Normalization)
> Conducted to **Transform the data** to **have a mean of zero and standard deviation of 1**. Which mean data average is zero and average deviation from 0 is 1 (i.e. most of the data stay in range -1 to 1) ![[Screenshot 2024-10-15 153125.png]]
> where:
 
**Mean $\mu$:** $$\mu = \frac{1}{n} \sum^{n}_{i=1}x_{i}$$![[Pasted image 20241015160927.png]]

**Standard Deviation $\sigma$:**$$\sigma = \sqrt{ \frac{1}{n} \sum^{n}_{i=1}(x_{i} -\mu)^2}$$
![[Pasted image 20241015161047.png]]


+ ? Standardization is a **Linear Transformation**.
+ ? Implement using Skit-learn![[Pasted image 20241015153005.png]]
Z Board: Let me determine the distribution between 0 and 1 using the Area to the Left which is the sum of $z_{x}$ and $z_{y}$ coordinate. 
Ex: z = 0.507 then I choose $z_{x}=0.07$  and $z_{y}=0.5$
![[Pasted image 20240719092819.png]]

![[Pasted image 20240719092048.png]]
Deviation: độ lệch (tốc độ tăng trưởng của z/ khoảng cách tương đối giữa các điểm) 
Mean: giá trị trung bình của các điểm.
![[Pasted image 20240719092242.png]]

![[Pasted image 20240719092419.png]]
Let Convert the value to find the distribution for X < 49
![[Pasted image 20240719092643.png]]

For X in between in this example: 5.81 < X < 6.3. We just need to substract the smaller area to the bigger area. (Since the bigger area contain the smaller area. thus subtract the smaller will return us the between area)
> To solve this:
> 1) Standardization the Distribution using Z-Scores.
> 2) Subtract 2 standardized area. Done
![[Pasted image 20240719095011.png]]

### STANDARDIZATION vs NORMALIZATION
> **Scaling (standard or normalization) is required** when we use **machine learning algorithm used gradient calculation (e.g. ANN, Logistic Regression, etc...)**
+ ? However, scaling is not required for distance-based and tre-based algorithms suck as K-Means Clustering, SVD and K Nearest Neighbor, Decision Trees, Random Forest and XG-Boost.

Specifically for Neural Network (use Gradient Descent), **Normalization is preferred** since we **don't assume any data distribution**. 
**Standardization is preffered** 
	+ when **data follows gaussian distribution**.
	+  over normalization **when there are a lot of outliers**.

# Normalization in ML and DL
### Why Normalization
Various data in a dataset (i.e. high variance) make harder for the model to learn. For example, when you give 200 different kind of color for 1 types of flowers to the model.
![[Pasted image 20260306153436.png | 444]]
The *model would adjust its weight continously* (unstable & sensitive) to new input (batch) distribution change continously, this phenomenon called *"Internal Covariance Shift",* its make training unstable and slower convergence.
+ $ However if we Normalize (standardize) the flower's color for every batch using Layer Normalization (ie. normalize the color channels) it would:
	1. Stabilizes the training of the model by *avoiding exploding or vanishing gradient problems*.
	2. *Faster convergence* of the model
+ @ -> Slower changes in the Distribution so the training is smoother. 


### MLP Batch Norm
![[Pasted image 20251212154825.png]]
**Where Batch Norm was applied in MLP:**
1. **Linear Layer:** Computes "Raw" signal comming out of the linear layer $z=Wx+b$. This value is unstable, might be very large or small.
2. **Batch Normalization Layer:** Receives $z$ as input and normalizes it.
	 $z$ $\to$ Apply Batch Norm $\to$  $\hat{z_{i}}$ as $\text{Normalized} \space z$" $\to$ Output $y_{i} = \gamma \hat{z_{i}} + \beta$   as the final Normalization value.
3. **Activation Function (ReLU):** Receives the *normalized output from Batch Norm.*

*Batch Norm process include 2 step:*
To normalize all inputs $z$, we would need to calculate the normalization value of each $z$.
![[Pasted image 20251212155124.png]]
*For the Normalization layer to be more flexible*, we *implement 2 learnable parameters $\gamma$ (scaling) and $\beta$ (shifting)* (update the same as like weight as bias). Where *1 Scale* the original Normalization value and *1 shift to Stabalize* the normalization value.
$$y_{i} = \gamma \hat{z_{i}} + \beta$$
(*Output* annotate as $y_{i}$ to *seperate from the original unormalized value*)
The flexibility *help avoid these problem:*
1) **Restoring Parameters:** Simply *forcing every layer's input to be a standard normal distribution* (Mean=0.5, Std=0.5) might be *too restrictive and could limit the network's* ability to represent complex patterns. **These parameters allow the network to "undo"** the normalization **if it decides that the raw distribution was actually better for learning.**
+ ? Basically, some layers of the network doens't need to be normalize if it already optimal, in this scenario $\gamma = \sqrt{ \sigma^2_{B} }$ and $\beta = \mu_{B}$ which simplified $\hat{z_{i}}$ to $z_{i}$, the same value before Normalization -> No Normaliaztion.
![[Pasted image 20260306152754.png | 555]]

2) **Optimial Activation Range:** **Different activation function work best with different input ranges.** For example, if the network needs the inputs to be slightly shifted to the positive side to activate a ReLU more often, it can learn a positive $\beta$. If it needs the data to be more spread out, it can learn a larger $\gamma$.

3) **Recovering:** *In theory dividing $\gamma$ is the opposite of dividing $\sigma_{\beta}$ and adding $\beta$ is opposite of subtracting $\mu_{\beta}$.* Since the network learn both $\gamma$ and $\theta$ during backward propagation, it can recover the original input $z_{i}$ exactly. This guarantees that BatchNorm doesn't lose any information, it just recognize it to make training easier.
+ $ Conclusion: *Batch Normalization help stabalize weight and bias* value and *improve convergence* speed since value are minimize to only 0 and 1 *during Training*.
+ ? So we Batch Normalization optimize parameters during Training, *what about optimization method during Initializtion*. Well, we have "He Initialization".

**He Initialization** design solely for ReLU.
+ Keep variance stable from the start.
+ Better Gradient from the start.
+ Less Negative Weight and Bias from the start.

### Layer Normalization 
reference: 
+ [simple layernorm explain](https://youtu.be/W9g7j22MO-Q?si=_SvkI9Le50L7T2RW) 
+ [LayerNorm in CNNs vs in Transformer](https://dkleine.substack.com/p/understanding-layer-normalization)

Batch Normalization vs Layer Normalization
![[Pasted image 20260306162302.png]]
Transformer's Input is a sequence of tokens (e.g. words) where each token has an embedding vector of size of the embedding dimensions. `(batch, seq_len, d_model)`

**LayerNorm in Transformers**  compute the *mean and std along the embedding dim for each token independently.* This way, each token remain stable across layers which is essential for effective attention calculations (why ? )
$$y_{i} = \frac{x_{i} - \mu_{layer}}{\sqrt{ \sigma^{2}_{layer}}}*\gamma_{i}+\beta_{i}$$
-> While *$x_i$ (each token), $\gamma$ and $\beta$ remain the same* as Batch Norm to learned per feature (column), the *mean and std is applied to the Embedding dimension.*
-> Very useful for sequence base model where each sequence present a new distribution.
![[Pasted image 20260306160245.png]]
Note: bc $\gamma$ multiplying and $\beta$ is adding to the feature matrix, they are vector size features.    