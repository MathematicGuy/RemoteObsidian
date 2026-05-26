**Term and Definition**
1) **Co-Adaptation:** hapened when multiple neurons in the NN become too dependent on each other to learn features. 
+ ? Neuron **fail to learn independently useful features** and **instead rely on other neurons to "fix" their mistakes**
+ $ With Dropout neuron is force to learn more robust and independent features. This results in a more generalized model that performs better on unseen data.

2) **Thinned Version:** of a neural network **refers to a temporary sub-network create during dropout training** 

3) **Model Averaging**: common technique in NN where **multiple models are trained separaely and their predictions are average**.
+ ? **Dropout perform Model Averaging** by create many "sub- networks" within a single model by randomly dropping neurons.
+ $ Instead of training more models, **dropout training multiple thinned verions simultaneously.**

---

### Drop Out technique
+ ? Randomly "droping out" units (both hidden and visible neurons along with their connections) from the neural network during training.
+ $ This prevent units from *co-adapting* too much.
![[Pasted image 20250219103959.png]]

### 1. Why Drop out ?
Deep Neural Network have high learning capacity, making them prone to overfitting.

Standard techniques like L1/L2 and early stopping help but not always effective.

Dropout **forces individual neurons** to **learn independently useful features instead of relying on other neuron to "fix" their mistakes**.  

### 2. How Dropout work ?
+ **Training Phrase:** Each neuron is kept with probability $p$ (typically $p = 0.5$ for hidden layers)
	
+ **Test Phrase:** No drop out applied. Instead weight are scaled down by $p$ to balence the larger number of active neurons. 

### 3. Benefits of Dropout
+ Reduces overfitting.
	
- Works as a form of model averaging, improving generalization.
	
- Encourages neurons to learn more independent features.

### 4. Applications of Dropout
- Used in **vision tasks** (MNIST, CIFAR-10, ImageNet).
	
- Applied in **speech recognition** (TIMIT).
	
- Useful in **document classification** (Reuters-RCV1).
	
- Also effective in **genetics and computational biology**.