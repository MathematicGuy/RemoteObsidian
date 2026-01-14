### Online CIL
Online mean One Pass CIL, where each batch can be processed once and then drop. 


## Math Notations
![[Pasted image 20260112145837.png | 355]]

**Data and Task Structure**

- **$B$**: Represents the total number of training tasks in the sequence.
    
- **$\{\mathcal{D}^{1}, \mathcal{D}^{2}, ..., \mathcal{D}^{B}\}$**: The sequence of training tasks that arrive over time.
    
	- **$\mathcal{D}^{b}$**: The dataset corresponding to the specific incremental step (or task) **$b$**.
    
- **$n_{b}$**: The number of training instances available in the $b$-th task.
    
- **$x_{i}^{b}$** and **$y_{i}^{b}$**: An individual training instance (e.g., an image) and its corresponding class label within task $b$. $x_{i}^{b}$ belongs to the $D$-dimensional feature space $\mathbb{R}^{D}$.


**Classes and Labels**

- **$Y_{b}$**: The label space (set of classes) specific to task $b$.
    
- **$Y_{b} \cap Y_{b^{\prime}} = \emptyset$**: This condition indicates that there are **no overlapping classes** between different tasks (e.g., if Task 1 has "birds", Task 2 will not).
    
- **$\mathcal{Y}_{b}$**: The cumulative set of all seen classes up to the current task $b$ (calculated as the union $Y_{1} \cup ... \cup Y_{b}$).


**Model and Optimization**

- **$f(x)$**: The classification model (mapping input $X$ to the cumulative label space).
    
- **$\mathcal{H}$**: The hypothesis space, representing all possible models the algorithm can choose from.
    
- **$\mathbb{E}$**: The expected value, used here to calculate the expected risk (error rate) over the data distributions.
    
- **$\mathbb{I}(\cdot)$**: The indicator function. It outputs **1** if the condition inside (e.g., prediction $f(x)$ does not match label $y$) is true, and **0** otherwise.
    
- **$\mathcal{D}_{t}^{b}$**: Represents the underlying data distribution of task $b$. The goal is to minimize error over the union of all distributions seen so far ($\mathcal{D}_{t}^{1} \cup ... \cup \mathcal{D}_{t}^{b}$).


