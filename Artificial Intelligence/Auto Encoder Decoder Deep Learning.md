**Auto Encoder Decoder** - type of compressing information
>Compressing data to latent space using the Encoder then re-compress/re-construct them to its original form using the Decoder.

### Autoencoders main components
**Encoder** compress data into a latent space (a low dimensional space) which capture the essential features of the data. 

**Bottleneck** hold laten space date (i.e. features).

**Decoder** reconstruct the image from the low dimensional feature.

**Goals:** Training model such that the Decoder are better at reconstructing while the Encoder are better at compress those critical data.  
![[Pasted image 20250305092136.png]]

+ ? How are we **compare the differences of the images**.
+ $ Simple method is to compare pixels independently by calculate their differences and take their average (MSE) -> calc diff of each pixel then return their average. ![[Pasted image 20250305092115.png]]

### Latent Space 
The Encoder convert the image into latens space vectors (i.e. latent representation). 
+ $ This **allow us to visualised how each data** is encoded by **treating the activation of each neuron as a direction of a plane.** If a neuron is highly activated, it will more closer to 1. (e.g, neuron2 activated -> move closer to 1 in the y-axis)
+ ? If the autoencoder is very well trained, **each instance of this number 7** will go in the **same region of the latent space** 
+ ? Each instance of other class like number 4 also form a cluster, in a ideal situation this cluster (of 4) is suppose to be far apart from the clusters of other classes.
>What happend is during trainning, with each class occupying its own distinct region. 
![[Pasted image 20250305093405.png]]

In low dimension, although the laten representation is not perfect, this organisation allow us to use other classification algorithm such as nearest neighbours might give a decent result on this representation.  
![[Pasted image 20250305093559.png]]

+ ? The **dimension of the latent space is determind by the number of neurons** in the bottleneck layer. In other word, its the Encoder outputs.
 ![[Pasted image 20250305092822.png]]

+ ! If the latent space is too small, the Latent space may fail to encapture all of the data important features leading to poor construction quality.  ![[Pasted image 20250305093222.png]]
+ $ This essentially translate to: **Poor latent space organization == Poor Reconstruction quality**. Since **low dimension simply cannot comprehence the datapoint's real position**, leading to overlapped data, like 2D and 3D, 2D and 5D. 
	Compare 2D with 5D ![[Pasted image 20250305095601.png]] In 5D  (i.e. latent representation) instance 1's cluster is much more well organized. As we see, just a portion of instance 1 (i.e. class 1) is misclassified (i.e. green dots on the left). ![[Pasted image 20250305095642.png]]
	+ ? Btw, how are we visualised **5D space to 2D** plot, **simply put we project the latent space and keep only the 2 most important dimensions instead of 5 most important dimension.**   
	
	Even with 5D space, we have relatively sparse and diffuse clusters. Misclassified of the number 3 is poorly encoder resulting in it being reconstructed as a number 8. ![[Pasted image 20250305100304.png]]


### Real Life Application
MRI scan - Classified gender using MRI based on their latent representation. 
![[Pasted image 20250305102308.png]]
![[Pasted image 20250305102325.png]]

#### Limitation
