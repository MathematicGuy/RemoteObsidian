# Decision Tree
![[Pasted image 20240806100509.png]]
 Bc Bond only decision is 20, it 1 decision either ways so we just need 1 branch of 20. 

> Calc the Probability, we found the best expected value is 20.2. So the decision is to invest in Stocks.
![[Pasted image 20240806100603.png]]

+ ? Play or Not Example
	![[Pasted image 20240806101520.png]]


 Note: Make De scision Tree fromt Scratch and applied it to solve real world problem.
Define Entropy, Define Gain

+ ? Calc Entropy, Calc Gain of each Features, we got:  
![[Pasted image 20240806111352.png]]

![[Pasted image 20240806111430.png]]
+ ? Repeat and Calc Entropy of each Features then Calc the Gain of each Features (for each branch)  
![[Pasted image 20240806113035.png]]
![[Pasted image 20240806113120.png]]
**Final Result**: Node raning base on how important they are to the whole dataset. (how much information they give out)
	![[Pasted image 20240806113308.png]]
Time Complexity: $O(log_n)$. where n is the number of rows of data and the tree is assumed to be relatively balanced.
	Assuming number of features is m, the run time is $O(mnlog_n)$.


**How does the Decision Tree algorithm Work?**
- **Step-1:** Begin the tree with the root node, says S, which contains the complete dataset.
	
- **Step-2:** Find the best attribute in the dataset using Attribute Selection Measure (ASM).
	
- **Step-3:** Divide the S into subsets that contains possible values for the best attributes.
	
- **Step-4:** Generate the decision tree node, which contains the best attribute.
	
- **Step-5:** Recursively make new decision trees using the subsets of the dataset created in step 3. Continue this process until a stage is reached where you cannot further classify the nodes and called the final node as a leaf node.
	
+ **Visualize**![[main-qimg-a2967f1eaecd002401e501c3232841d5-lq.jpg]]


[Decision Tree Read More](https://www.quora.com/How-do-I-calculate-the-time-complexity-of-a-decision-tree-machine-learning-algorithm)
![[Pasted image 20240806121053.png]]
	Decision trees are helpful, not only because they are a visual representation that help you visualize what you are thinking, but also because design of a decision tree requires a documented thought process. Decision trees help formalize the brainstorming process so we can identify more potential solutions.