[[Decision Tree Archive]]
[[Regression Trees and Regression Tree Prunning]]
[[Decision Tree DIY]]
[[Gini Index vs Entropy]]

Gradient Boosting Machine: cây sau đc xây (cải thiện) dựa vào cây tr'c.   

## Classification and Regression Trees (CART)
![[1665584415139.jpg]]


---

[Decision Tree Read More](https://towardsdatascience.com/decision-trees-explained-entropy-information-gain-gini-index-ccp-pruning-4d78070db36c/)
![[Pasted image 20240806121053.png]]
	Decision trees are helpful, not only because they are a visual representation that help you visualize what you are thinking, but also because design of a decision tree requires a documented thought process. Decision trees help formalize the brainstorming process so we can identify more potential solutions.

+ @ **Classification Tree Model** are **Non-parametric models**, are the ones that **cannot be indexed by a fixed number of parameters**. **The number of parameters describing the model/hypothesis usually grows with the dataset.**  

---

Decision Tree **classified things into categories** -> Classification Tree
![[image.webp]]
Decision Tree **predict numerical value** -> Regression Tree  
![[image/Untitled 5.png]]
**Internal Nodes:** These **nodes** **represent questions** or tests applied to a **specific attribute of the data.**

**Branches:** **Each branch represents the possible outcomes of the test** at an internal node.

**Leaf Nodes:** These **represent the final decision or prediction made by the tree.**

### Decision Tree Example
How to quantify the impurity -> By using [[Gini Index]] (Linear)/Entropy/Information Gain
**Gini Impurity** (điểm không thuần khiết/tạp chất gini) - **Purity:** thuần khiết
+ ? **the prob of "YES"** in "Cool As Ice" leaf only calc the prob of "YES" in the current leaf. The same for the probability of "No".
![[Pasted image 20250302163723.png]]
![[Pasted image 20250302163744.png]]

Because the amount of people on the left was 4 and right was 3
![[Pasted image 20250302163826.png]]

### Total Gini Impurity of 2 Leafs
$$\text{Total Gini Impurity} = 
(\text{Left Leaf Gini Impurity}.\text{Left Leaf Probability}) 
+ 
(\text{Right Gini Impurity} \times \text{Right Leaf Probability})$$

We start by calc the weight of the leaf on the left. We divide the total people on the left: 4 by the total peoples on the right and left: 4+3=7 and multiply the Gini Impurity in the left: 0.375
![[Pasted image 20250302164224.png]]
Do the same for the right. (Right Total) / (Total both side) * Gini Impurity
![[Pasted image 20250302164303.png]]
So the **Gini Impurity for Popcorn Leaf is 0.405.**

![[Pasted image 20250302164411.png]]
Like wise **for Love Soda, we got Gini Impurity of 0.214**

For calculating Gini value by age (numerical value), first thing we do is sort the rows by Age, from lowest to highest value. 
![[Pasted image 20250302164531.png]]
Then we calculate the average age for **adjacent people**. (Ex: $\frac{7+12}{2}=9.5$, $\frac{12+18}{2}=15$)
Lastly we calculate the Gini Impurity values for each average age.
![[Pasted image 20250302164734.png]]
To calculate the Gini probability of Age = 7, we first categorize people   
+ who Age **$< 9.5$** 
+ who Age **$\geq 9.5$** into 2 categories 
For example, there only 7 under 9.5 and is not loves cool as ice, so number of No is 1. 
![[Pasted image 20250302164828.png]]
And there are 6 people who Age >= 0.5 so we categorized them to the left. And count the number of Yes or No. 

Next we calculate the Gini Impurity of both side.
![[Pasted image 20250302165626.png]]
![[Pasted image 20250302165719.png]]
Now we calculate the Weighted Average of the two Impurities to get the Total Gini Impurity
![[Pasted image 20250302165809.png]]
This repeat for all Ages in the table. And we find 2 lowest impurity candidate of 0.343 are 15 and 44. So we **can pick either on,** in this case we pick 15. 
-> So the **Gini Impurity for Age (column) is 0.343**
![[Pasted image 20250302165905.png]]

In Summarize we got:
**Gini Impurity for love popcorn as 0.405.**
**Gini Impurity for Love Soda as 0.214** -> Leaf with lowest Impurity (tạp chất)
**Gini Impurity for Age (column) as 0.343**
>Because Loves Soda has the lowes Gini Impurity overall, its Leaves have the lowest impurity. So we put "Loves Soda" branch at the top of the tree.  
![[Pasted image 20250302170904.png]]
>There are 3 people who Loves Sode that also Loves Cool as Ice and 1 doesn't. So this leaf is Impurity. 
+ ? Impurity is when a leaf answer/choice is not absolute/clear, like 100% Yes or 100% No. 
![[Pasted image 20250302171009.png]]
So let's see if we can **reduce the Impurity by splitting the people that Love soda based on Loves Popcorn or Age.**
+ Because there are **2 people who Love Soda and Popcorn**, so there are 2 total people on the left.
+ The remainining **2 people who Loves Sodas and do not Love Popcorn** end up on the right.
So we get the **total Gini Impurity for this Popcorn split (only) is 0.25**
![[Pasted image 20250302171940.png]]
For like above, we **only consider 4 Ages who Love Soda**. And calculate the Impurity of each leaves.
![[Pasted image 20250302172955.png]]
We see both leaves have no Impurity at all, the **Gini Impurity for Age < 12.5** is 0. 
Now because **0 is less than 0.25, we use Age < 12.5 to split this Node into Leaves**
![[Pasted image 20250302174356.png]]
Because there're no Impurity left. We can assign output for each leaf base on the majority of the people:
![[Pasted image 20250302174811.png]]
Now, when there new data comes along. We just run the data down our tree.  
![[Pasted image 20250302174850.png]]

Remember, at the start there only 1 person make it to this Leaf. So few that it's hard to have confidence that it will do a great job making predictions with future data -> Possible for overfit -> [[Regression Trees and Regression Tree Prunning]]
![[Pasted image 20250302175051.png]]
So we prune that leaf. This give a better sense of accurary of our prediction because we know that only 75% of people in leaf "Loves Cool As Ice" -> we put the leaf as "Loves Cool As Ice" as label for the Decision Tree model. 
![[Pasted image 20250302180237.png]]
+ ! When we build a tree, we don't know in advance if it is better to require 3 people per leaf or some other number, so we test different values with something called [[Cross Validation]] and pick the one that works best.

---

If the sample is **completely [[homogeneous]] the entropy is zero** and if the sample is an **equally divided it has entropy of one.**
![[Pasted image 20250302185206.png]]

---
### Compare Entropy and Gini Impurity in Decision Tree

**Entropy**
![[Pasted image 20250302191824.png]]
![[Pasted image 20250302191829.png]]
![[Pasted image 20250302191838.png]]


**Gini Impurity**
![[Pasted image 20250302190349.png]]

- **Range**:
    - Entropy lies in the range $[ 0,log⁡_{2}(C)]$ For binary classification ($C=2$), the maximum is 1 (when $p=0.5$).
    - Gini for a node with C classes has range $[\,0, 1-\frac{1}{C}\,]$. For a binary classification with $p=0.5$, the maximum Gini impurity is 0.5
    - $ **Gini Impurity is generally more computationally efficient than entropy.** The graph of **entropy increases up to 1** and then starts decreasing, while **Gini Impurity only goes up to 0.5** before decreasing, thus **requiring less computational power.** The range of entropy is from 0 to 1, whereas the range of Gini Impurity is from 0 to 0.5.
	  ![[Pasted image 20250302190440.png]]  
- **Sensitivity**:
	- **Entropy tends to penalize impure nodes** (i.e., near-even splits) more heavily than Gini does when the classes are evenly mixed. This is because the $\log_2$ in **entropy grows more quickly than the linear term in Gini** as $p$ approaches 0.5.
	    ![[Binary_logarithm_plot_with_ticks.svg.png]]
	- Gini tends to give slightly higher values for moderate degrees of impurity, which can affect which split is considered “best.”
```ad-summary
- **Entropy and Gini measure “impurity” in different ways**: Entropy uses the log-based definition of **information content**, while Gini measures the **probability of misclassification**.
.
- **Practically**, **both usually produce similar splits and result in similar performance**.
.
- **Existed Biases**:
    + **Entropy** more heavily penalizes near-even splits (i.e., encourages more “decisive” splits), which can help in certain minority-class conditions.
    + **Gini** can be slightly faster and is sometimes considered more straightforward as a measure of node “purity” (misclassification probability).
```

---

### Prunning
> reduce overfitting

