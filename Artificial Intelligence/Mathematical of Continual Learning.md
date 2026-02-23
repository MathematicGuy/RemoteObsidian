Adaline (Adaptive Linear Neuron) was 1 of the 1st algo for training NN (Neural network).

LMS introduce **"Principle of Minimal Disturbance."** Which is the ancestor of modern regularization in CL. States that a system should adapt to reduce error on a current training pattern with the "Smallest extent possible" of disturbance to stored information. - update on current task while trying not to deviate from what was learned previously. 
![[Pasted image 20260213211316.png]]
Note: Before was before Gradient-based and Backprop was Invented. 
+ ! LMS to multi-layer (non-linear) network was too hard, so research shift toward adaptive signal processing. 

	**Adaptive Filtering** Is Now a Mature Subject. Geometry become essential for improving convergence and memory. 
-> APA or Affine Projection Algorithm (1975) act as an extension of LMS that employs a "sliding windown" of memory (the B most recent sample). It constraints the model to explain recent samples well. 
![[Pasted image 20260213211554.png]]
![[Pasted image 20260213215516.png]]




Number of Benchmark been cited in paper
![[Pasted image 20260214013137.png]]