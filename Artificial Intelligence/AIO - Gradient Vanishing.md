**When activation function is Linear**

**Gradient Exploding:** gradient make each weight update excessively large. Lead to instabability in the network's learning process and preventing convergence (hội tụ).

**Gradient Vanishing:** gradient make each weight update excessively small. So small ~ 0 that weights lose their meaning.

Optimizer: help update gradient process better 

![[Pasted image 20241129204237.png]]

Step 1: Import libraries and setting computing device like CUDA
Step 2: Set random seed
Step 3: Load dataset FashionMNIST
	pytorch code command
	`download = False` -> test dataset
	`download = True`   > training dataset
Step 4: Val split and create DataLoader
Step 5: Build and init deep MLP
Step 6: Training
Step 7: Training Visualization
Step 8: Evaluation
	Sigmoid Problem

## Methods for Improving
0. Initialization (with Vanishing Model for example)

1. **Weight Increasing**


2. **Better Activation**


3. **Better Optimizer**


4. **Normalize Inside Network**


5. **Skip Connection**


6. **Train Layers Separately**

   
7. **Gradient Normalization**



