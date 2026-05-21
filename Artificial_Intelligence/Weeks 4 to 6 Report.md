**Note:** 
+ Explain Regression (predict) vs Classification (classify)
+ Explain Linear Regression -> Leading to Logistic Regression 
+ Compare 2 Layers to 1 Layers, why it better.
+ Explain model
	Explain Logistic Regression
+ Explain how I "plot random data blob" for classification
+ Improvement at the end
	+ Vectorization (replace with numpy)
	+ Hessian Matrix and Neuton Method compare to Gradient Descent

---

# Plan:

### Explain Related Topics about 2 Layers Neural Network: 

**Purpose:** for Classification Problem.

**Architecture:** (Input/Hidden/Output) Layers, Syntax using 1 Layer NN.

**Methods (Breakdown):** 
+ **Normalization (NM)**: Eplain why data normalization is crucial before training NN. 
	
+  **Forward Propagation (FP)**: Explain how data flows through the network.
	
+  **Cost Function (What is a 'Example' , 'Loss' and 'Cost')**: Explain what a cost function is, concept of loss for individual examples, how the cost function aggregates it across all examples. (This can come right after FP bc cost is calc using forward pass outputs).
	+ **Introduce Log-Loss Cost Function** here, followed by explaining **regression** (linear and logistic) as background to understanding the cost function. This will provide clarity on how the cost function applies to classification tasks.
	
+ **Backward Propagation (BP)**: Explain how parameters are updated from the end using gradients.
	
+ **Update Parameters (UP)**: Explain how parameters are updated using the gradients from backward propagation.


**Algorithms and Formulas**: All Agorithms must Include the **3 W's (What does it do, Why do I use it, Where does it come from)**
	
+ **Sigmoid** Function
	
+ **Derivative, Partial Derivative, Second Derivative.**
	
+ **Log-Loss Cost Function**: Introduce Binomial Distribution and MLE to explain where log-loss comes from. Why log func is used to convert func from $\prod$ (multiplication) into $\sum$ (addition) leading to log-loss.
	
+ Introduce Jacobian Matrix and how it was used to represent Partial Derivative Matrix.   
	
+ Introduce **Newton Method** as a more advanced method for finding minima, which requires 2nd order derivatives (use it to contrast with GD e.g. more expensive for LLM and more). Then explain **Hessian Matrix** and how it's used for optimization in Newton's method.


**Implement Methods (Python)** 
+ Where to I start ?
+ Though Process ?
+ Problems and Answers
+ **Improvement: Vectorization using Numpy** 

(If possible): Apply this to a Real World Example

**Explain the Remaining Topics that I've learned:**
+ **Classification and Regression Methods**: like Feature Engineering, etc.
+ **Statistic & Possibility** (Bayes' Theorem, Conditional Probability, etc.)


**End with Future plan:** Understand Common Research Paper Mathematic Syntax. Decision Tree, Random Forest, SVD for Classification. Then Deep Learning (CNN)

---


![[Pasted image 20241025111106.png]]

- **Dependent Variable**: This is the outcome or the variable you're trying to predict or explain. It’s sometimes called the target or the response variable.
    
- **Independent Variables**: These are the input variables used to make predictions about the dependent variable. They are sometimes referred to as explanatory variables, features, or predictors.
    
- **Relationship**: Regression models aim to find a mathematical function that describes the relationship between the independent variables and the dependent variable. For example, in simple linear regression, this relationship is modeled as a straight line.
