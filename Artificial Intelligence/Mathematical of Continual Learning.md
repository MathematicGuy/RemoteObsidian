Adaline (Adaptive Linear Neuron) was 1 of the 1st algo for training NN (Neural network).

LMS introduce **"Principle of Minimal Disturbance."** Which is the ancestor of modern regularization in CL. States that a system should adapt to reduce error on a current training pattern with the "Smallest extent possible" of disturbance to stored information. - update on current task while trying not to deviate from what was learned previously. 
![[Pasted image 20260223154110.png]]
Note: Before was before Gradient-based and Backprop was Invented. 
+ ! LMS to multi-layer (non-linear) network was too hard, so research shift toward adaptive signal processing. 
	**Adaptive Filtering** Is Now a Mature Subject. Geometry become essential for improving convergence and memory. 
-> APA or Affine Projection Algorithm (1975) act as an extension of LMS that employs a "sliding windown" of memory (the B most recent sample). It constraints the model to explain recent samples well. 
![[Pasted image 20260223154140.png]]

**Setting**
![[Pasted image 20260224182029.png | 444]]

**Error Metric**
![[Pasted image 20260224182059.png]]

![[Pasted image 20260224182128.png | 555]]

## Part 1: Continual Regression - Least Mean Square (1960)
![[Pasted image 20260224182236.png]]
Establish connection with continued learning.  Minimizing the expected value. 
Note: Random xi yi at initialization.

**Least Mean Square 1**
![[Pasted image 20260224182550.png]]
The update equation Goal are the same for SGD, GD and LMS in solving continual learning problem. 
![[Pasted image 20260224182827.png]]
Even though we begun with LMS the reality was the other way around. 

Theorical Result for LMS
![[Pasted image 20260224182935.png]]
*Proof for the fomula above*
![[Pasted image 20260224183030.png]]

![[Pasted image 20260224183115.png]]
+ $ Main Point: we get a bound on the MSE and that bound is dependent on the step sized $\gamma$ and the smallest value of the covariance matrix. 
+ ? If we choose them carefully we can get an exponential rate of convergence for the MSE.  

**IID Assumption**
![[Pasted image 20260224183136.png]]
If I solving a Linear Regresison problem I can have exponential convergence. 

![[Pasted image 20260224183737.png]]

**LMS is (Linear) Attention**
![[Pasted image 20260224184528.png]]
??? Linear Attention -> Linear RNN ???  

![[Pasted image 20260224184641.png]]


## Part 2: Gradient Projection - Affine Projection Algorithm (1975, 1984)
Basic geometry (never forget, via constraints & in subspaces)

**From LMS to Affine Projection Algorithm (APA)**
![[Pasted image 20260224185628.png]]



