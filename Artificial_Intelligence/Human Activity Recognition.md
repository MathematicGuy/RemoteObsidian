# A Survey
souce: https://medium.com/@zlodeibaal/action-recognition-in-the-wild-9eb7f12b4d12

+ ? There are 2 way to detect human action.
1. **Traditional Methods**: [[Traditional Action Detection using LSTM with Convolutional Network]]
	+ Traditional method such as using Histogram of Oriented Gradient (HOG) and Scale-Invariant Feature Transform (SIFT) to represent motion and  appearance then classifies actions with SVMs classifiers.
	+ Probabilistic Models: Techniques like Hidden Markov Models (HMMs) and Conditional Random Fields (CRFs) were employed to model temporal dynamics in actions, capturing the sequential nature of activities. 
	
2. **Deep Learning Based-Methods**
	+ **CNN:** learn spatial features from individual frames
		
	+ **RNN and LSTM:** to capture temporal dependencies in sequence of frames, effectively modeling the evolution of actions over time.
		
	+ **Two-Stream Networks**: These architectures process spatial (RGB frames) and temporal (optical flow) information separately through two CNNs, combining their outputs to enhance action recognition performance.​
	    
	- **3D Convolutional Networks**: By extending 2D convolutions to the temporal dimension, 3D CNNs simultaneously capture spatial and temporal features, offering a unified approach to action detection.
	
3. **Unsupervised and Self-Supervised Learning**
	+ **Autoencoders and Variatioanal Autoencoder (VAEs):** these model learn the essen of video data (laten representation) enabling anomaly detection and action recognition without extensive labeled datasets.
		
	+ **Contrastive Learning**: By learning to differentiate between similar and dissimilar pairs of video clips, models acquire robust features useful for action detection tasks.
	
4. **Motion Analysis and Video Tracking**
	- **Optical Flow-Based Methods**: By analyzing the motion of pixels between consecutive frames, optical flow techniques provide insights into movement patterns, assisting in action detection.​
	    
	- **Video Tracking**: Tracking objects or individuals across frames helps in understanding action sequences, especially in surveillance and monitoring applications.

+ ? **Question:** **"In general case" a frying pan in your hand doesn't mean anything**. But **knowing the context** we could know if the person is "fighting" in the PUBG, "cooking" in the kitchen or "selling" its in a store. In other word **identify relationship between object to object.**
	![[Pasted image 20250312210400.png]]
	By Combining logic between "Position" and "Object", you can assemble along actions or sequences of actions. 
	![[Pasted image 20250312171652.png]]

### Temporary Action (Hành động tạm thời)
+ ? Methods that work on "a video piece".
1) Working with a skeleton model of the object
	Person Skeleton
	![[Pasted image 20250312224116.png]]
	Animal Skeleton
	![[Pasted image 20250312224111.png]]
	Arm Skeleton
	![[Pasted image 20250312224105.png]]
	Face point model
	![[Pasted image 20250312224059.png]]
2) Working directly with video (Whole video, Selected Object like person, car, etc.)
3) Combined methods (Using ROI, Combining with obj detectors, Preprocessing technique (Optical Flow, etc..))

### Classification (classical approach)
+ ? Can use 3D Conv

Note: I can extract features from point coordinate using Conv ?
![[Pasted image 20250312224327.png]]

**Advantages of Using CNNs with Skeletal Data:**

- **Computational Efficiency:** Skeletal data is less complex than raw video data, leading to faster processing and reduced computational requirements.​
    
- **Robustness to Variations:** Focusing on joint positions makes the model more invariant to changes in appearance, lighting, and background, enhancing generalization across different environments.​

- **Effective Spatial Feature Learning:** CNNs excel at capturing spatial hierarchies, making them well-suited for learning the structural relationships between joints in skeletal data.​