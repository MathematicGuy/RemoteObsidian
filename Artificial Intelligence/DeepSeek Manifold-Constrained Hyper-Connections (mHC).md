**References:**
	[ResNet]https://arxiv.org/abs/1512.03385 
	[Identity Mapping](https://arxiv.org/abs/1603.05027)
	[Hyper-Connections](https://arxiv.org/abs/2409.19606)
	[mHC](https://arxiv.org/abs/2512.24880)
	
+ @ Push the boundaries of *neural network architecture stability and scalability*.

**ResNet (He. et al 2015)** use 1x1 Conv to Compress Feature Dimension (ie. Channel of a Feature across all Channel in the Faeture Map). Through a Bottleneck architecture where the first 1x1 Conv compress dimension (256 -> 64 channels) then perform 3x3 conv to extract total features, finally decompress total feature from 64 back to 256.     
+ ? You can look at **1x1 Conv as a "BottleNeck" module to Preserve Number of Features Filter (ie. kernel)** as the model get deeper by **"compress (input), extract features & decompress (extracted input)"**
![[Pasted image 20260106125208.png | 455]]
+ @ **Solve Gradient Vanishing problem.** Allowed networks to jump from ~20 layers to 152+ layers.  


**Identity Mapping (He. et al 2016)** - Improvement to Skip Connection
+ ! After Resnet, they found that the placement of activation function (ReLU) and normalization (BatchNorm) in the *original ResNet interfered slightly with the "clean" information flow through the shortcut connections.*   
+ $ **Main Ideas:** theoretical derivation showed that **Information propagates best when the shortcut connection is a pure identity mapping (with no scaling or gating).**
	  
	They proposed the "Pre-activation" ResNet. **Instead of putting BatchNorm and ReLU** *after* the convolution (Post-activation), they *moved them before* the convolution. This leaves the shortcut path completely open, **creating a direct path for gradients to propagate from the very last layer to the very first.** ![[Pasted image 20260106131909.png ]]
+ @ An improvement to Skip-Connection: proved that **deep networks train best when the signal path is clean.** This allows gradients to flow directly from the loss function to the early layers -> Improve training even in deeper network and reduce overfitting. $$x_{l+1} = x_{l} + F(x_{l})$$
+ ? A example of [[Identity Mapping Violation]] if the information stream *mixed 2 stream of information*.$$\mathbf{x}_{l+1} = \underbrace{0.7 \cdot \mathbf{x}_{spatial}}_{\text{Pre-trained Stream}} + \underbrace{0.3 \cdot \mathbf{x}_{motion}}_{\text{SMIF/LMI Stream}} + \mathcal{F}(\dots)$$


**Hyper-Connection (Zhang et al 2024** - serve as an *alternative to residual connection* from ByteDance
+ ! Standard residual connections force a **fixed connection strength** (1x1 additivity) which can lead to a "Seesaw efffect between gradient vanishing and *representation collapse*" (where *all layers end up learning similar features*) 
+ $ Theoretically, hyper-connections **allow the network to adjust the strength of connections between features at different depths and dynamically rearrange layers.**
+ ? Driven by the limitations of residual connections, an important question arises: *Can neural networks autonomously learn the optimal strength of connections to improve performance ?*

The core idea of hyper-connections (HC) is to propose learnable depth-connections and width-connections.  
![[Pasted image 20260106133112.png]]

**Transformer with Hyper-Connection**
![[Pasted image 20260106141754.png | 455]]


**The Problem** - [reference](https://www.reddit.com/r/LocalLLaMA/comments/1q21wqw/a_deep_dive_in_deepseeks_mhc_they_improved_things/)
**Resnet** standard design forces a rigid 1:1 ratio between the input and the new computation, **preventing the model from dynamically adjusting how much it relies on past layers versus new information**.

**The Innovation**
ByteDace tried to break this rule with "Hyper-Connections" (HC), **allowing the model to learn the connection weights instead of using a fixed ratio**.
- **The potential:** *Faster convergence and better performance* due to flexible information routing.
- **The issue:** It was incredibly unstable. *Without constraints*, signals were amplified by **3000x** in deep networks, *leading to exploding gradients.*

**The Solution: Manifold-Constrained Hyper-Connections (mHC)**
DeepSeek solved the instability by constraining the learnable matrices to be *"Double Stochastic" (all elements $\geq$ 0, rows/cols sum to 1).*

**The Results**
- **Stability:** Max gain magnitude dropped from **3000 to 1.6** (3 orders of magnitude improvement).
- **Performance:** mHC beats both the standard baseline and the unstable HC on benchmarks like GSM8K and DROP.
- **Cost:** Only adds ~6% to training time due to heavy optimization (kernel fusion).

### mHC Explained: From Residuals to Hyper-Connections
Solve the problem: model learn worst as its goes deeper.

**mHC:** allow the model learn the strength of its residual connection.
From Hyper-Connection. Instead of learning from 1 residual connection, we learn from n times residual.   

**But it’ll be expensive so we first aggregate x1 → x4 using a weighted combination $x_{l}^{pre}$.**  
	The layer then process this aggregated features to produce an output. As there's only one output residual mapping from the layer
![[Pasted image 20260106163732.png]]
**Information exchange between residual stream is quite limited.** To address this, we introduce a **learnable linear transformation between the residual streams** $h_l^{(n)}$. Here, the transformation is parameterized by a 4x4 weight matrix. We can interpret the transformation as a feature router
-> By specifying the weights, we form flexible connection patterns that route features from one residual stream to another. Also allow the model adaptedly control and combine the information. 

**Math behind Hyper-Connection**
![[Pasted image 20260106164439.png]]
*First params -> static mappings:* global ones that do not depend on the input referrend. 
*Second params inside tanh -> dynamic mapping:* input dependent parameters referred.

![[Pasted image 20260106164650.png | 344]]

Converge 1.8 times faster than the base line.
![[Pasted image 20260106164827.png]]

However, when DeepS seek attempt to adapt this technique for their model training, they observe significant training instability.
![[Pasted image 20260106164931.png]]
The first term corresponds to the features at a shallow layer successively transformed by the feature mixing matrices across the intermediate layers. The second term consists of the sum of the outputs from all previous residual functions.


Suppose the initial value is one and the feature at layer L involves the successive multiplications of a scalar H. Let's see how the value evolves over the layers. When the value of edge is one, we have identity mapping. The output at a layer L is still one. However, if we increase the value of edge to 1.1, the output value exhibit a dramatic 100 fold increase.
![[Pasted image 20260106165015.png | 555]]

Conversely, when edge is less than one, the output value rapidly decays as it pass through the layers. The instability becomes even more significant when edge takes on negative values causing the output to oscillate dramatically. But how do we stabilize the trending? To do so, we need to ensure that these linear mappings are well behaved. For example, the feature mixing matrix can have arbitrary numbers because it is unconstrained.
+ $ The key idea is to make this matrix a doubly stoastic matrix. also known as the Burko polotope. The requirement is that all elements must be positive and each row and column must sum to one. **This effectively stabilize the trending preventing exploding or vanishing gradient problems.* ![[Pasted image 20260106165240.png]]
+ ? But how do we make this matrix doubly stochastic ? The first step is to make all the elements positive.

To achieve this, we **apply an exponential function** for each individual element. The exponentiation ensures that each output is strictly *positive* and *increases monotonically (with its input)*. But now when we **sum up all the rows and all the columns, their values are now one**. We use a simple **iterative algorithm**
that alternately **rescale all rows and all columns of the matrix to sum up to one.**
	Note: monotonically increase mean A & B increase together or A increase & B remain. but not decrease. 
![[Pasted image 20260106165343.png]]

But after scaling, the sum of each row is still not one. Therefore, we *rescale the sum of each row to one. But after rescaling all rows to sum to one, that changes the sum of the columns.* Fortunately, we can apply the alternative *rescaling iteratively.* With only a few iterations, we make the feature **mixing matrix very close to a doubly stoastic matrix**. It's very simple.
![[Pasted image 20260106165509.png]]
+ ? To make this sound more academic, we refer this process as *projecting the feature mixing matrix onto the manifold of doubly stoastic matrices*. Basically made them well behaved. This algorithm is known as the **synch knob algorithm.** 
![[Pasted image 20260106165557.png]]

For the other two matrices, the deepseek paper also made some *slight adjustments in terms of their parameterizations.* Here is the parameterizations of the hyperconnections papers discussed before. Here is the one from deepseek. The **key difference** is that they **change the activation function from tanh() to sigmoid().**
![[Pasted image 20260106165609.png]]
The primary reasons are twofold.
+ First, this avoids *negative coefficients.*
+ Second, the *new parameterizations*
This ensures that the aggregation and expansion weights are bounded. The values cannot be larger than one or two. Compared to the original parameterizations, the new design makes the linear mappings more well behaved.

![[Pasted image 20260106172010.png]]
But **why is there a scalar two here ?**  Remember that this is the weight we use to rescale the layer output before adding back to each residual stream. At the initializations, the parameters alpha and bias vector B are set to be small numbers. This means that **initially the input to the sigmoid is very close to zero and therefore the output is very close to 0.5.** **Multiplying it by two ensures** that at the beginning of the training the **hyperconnections behave exactly like the standard residual connections.**  $$0.5 \times 2 = 1$$
