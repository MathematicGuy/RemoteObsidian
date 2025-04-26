Note: 
+ ? Central to the language of regression are the notions of one designated **dependent variable and one or more predictor variables.** In the **height-vs.-weight example**, we can **think of the weight as the dependent variable and the height as the predictor variable**. For that example, the **goal of a regression algorithm would be to return the best (best in some average sense) value for the weight for a given height.**
+ [Regression Tree Mathematic Fomula](https://web.pdx.edu/~arhodes/advml5.pdf)

Plan:
1) Explain the broad overview, regression terminology. (remember to relate concept with real life situation)
2) Explain using deeper mathematicall term (Matrix multiplication and Jacobian and so)
3) After they understand the Matrix stuff, simply combine Regression Tree concept with Math Equation along with graph visualization.
4) Q&A
5) Rate my Lecture

---

```ad-abstract
Regression Tree is like **Linear Regression but apply for Discrete of the Data**.

**Linear Regression vs Regression Tree**
![[Pasted image 20250316164933.png]]
```


### Problem Exist, Problem (that they) Solve. 
+ ? Since **each leaf corresponds to a average Drug Effectiveness in a different cluster of observation**.
+ $ The tree does a better job reflecting the data than the straight line. 
![[Pasted image 20250316154023.png]]
+ ? But isn't that I can just look at the Graph to the Drug Effectiveness ? What the big deal about regresssion tree. 
+ $ When we have **3 or more predictors like Dosage, Age and Sex to predict Drug Effectiveness, drawing a graph is very difficult if not impossible.** 

---

**Regression Trees** for non-linear problem (real word problem)
**Classification Tree:** Classifies Discrete Categories. (Yes / No)
**Regression Tree:** Classifies Continuous Value by taking their average (e.g. Y for this X in range `[0, 10]`) 
+ ? Example: For this Drug Dosage range how effective Drug will be ? ![[Pasted image 20250316153753.png]]
+ $ To understand why Regression Tree look like that, let build them from the ground up.

### Regression Tree
+ $ First let **focus on the 2 observations with the smallest Dosages** on **x-axis**. Their **average is 3 and that correspond to the dotted red line.** 
+ ? The point on the far left (value = 0) is the only 1 with Dosage < 3.  
	+ So the left is 0 when the Dosage is < 3.
![[Pasted image 20250316155808.png]]


+ ? The average Drug Effectiveness for all the points with Dosages >= 3 is 38.8. So the right leaf is 38.8. 
![[Pasted image 20250316155958.png]]
+ @ **Split the data into two regions in mathematical term**: $$R_{1} = \{X | X_j < s\} \space \text{and} \space \{R_{2} = X | X_j \geq s\}$$ where $s$ is the **Drug Dosage**


+ ? We can visualize and know how bad the prediction is by calculate the **residual sum square error between the observed value and predicted values** (i.e. a dotted line or residual line) 
+ $ So **basically calculate Prediction's Loss value** like calculating Loss in the Neural Network. 
![[Pasted image 20250316160153.png]]
![[Pasted image 20250316155551.png]]
$$\sum^{p}_{i \in R_{j}}(y_{i} - \hat{y}_{_{R_{j}}})^2$$
where
+ p is the number of Predicted value. 
+ y is the observe value 
+ $\hat{y}_{i}$ is the predict value 


Save the sum of squared residual we just calculate for later comparison. 
![[Pasted image 20250316155624.png]]

+ ? This "**choosing the red average line to find the best seperation**" step **repeat for all adjacent point, pair by pair**.  
![[Pasted image 20250317071430.png]]

+ ? The **plot below** show all **Sum Squared Residual of all the seperation** (i.e. red dotted line). 
+ $ That it, now we **repeat until we have calculated the sum of squared residual for all of the remaining threshold.** (e.g. SoS residual of the 2nd and 3rd value, SoS residual of the 3rd and 4th value, etc.) ![[Pasted image 20250316160618.png]]
$$\sum^{J}_{j=1} \sum^{p}_{i \in j}(y_{i} - \hat{y}_{_{R_{j}}})^2$$
+ ? Then, we take the **smallest Sum of Squared residuals**. That mean `Dosage <= 14.5` will be the root of the tree.  ![[Pasted image 20250316160933.png]]

+ $ In summary, we splot the data into 2 groups by finnding the threshold that gave us the smallest sum of squared residuals. (Tổng bình phương giữa kết quả quan sát và các kết quả dự đoán)
+ @ In other word,**find the split point s** that minimizes the **sum of squared residuals (RSS)**. $$\arg \min_{x}  \sum^{J}_{j=1} \sum^{p}_{i \in j}(y_{i} - \hat{y}_{_{R_{j}}})^2$$
+ ? **$arg_{min}$** means "find the argument (variable) that gives the minimum value," NOT "choose the smallest number from a sum."


Reference fomula:
![[Pasted image 20250316182144.png]]
Now we repeat all the step above.  
+ ? We could **split these 6 observation into 2 smaler groups just like we did before**, then **calc the Sum of Square residual for different threshold**, and **chosing the threshold with the lowest sum of squared** residuals, that is `dosages <= 14.5` with `SoS value equal 20`. (i.e. the first node before the 14.5 threshold). 
+ ? Because the 1st `dosages <= 14.5` observation can't be split anymore, we will call this note a leaf.
![[Pasted image 20250316161201.png]]
+ ? However since the **remaining 5 observation go to the other node, we can split them once more**. 
+ $ In Constract, the left leaf contain 4 **observations that all have the same Drug Effectiveness**, so we **don't need to split them into smallar groups**.  
![[Pasted image 20250316161755.png]]

+ ? You can test the Regression to check if it accurate, but **if it too accurate** like 100% it **probably overfit and will not perform well with new data.**  
![[Pasted image 20250316162047.png]]

In Machine Learning, we say the model has no **Bias** (thiên vị) but potentially large **Variance** (đa dạng) 
+ $ A simple technique to solve this problem is to **only split observations when there are more then some minimum number**. The minimum **Threshold usually 20 but for this example, let set the minimum observations for split is 7.**  
+ ? In other word, since there are **only 6 observations with Dosage < 14.5  we will not split the observation in this node**. Instead that node will become a **Leaf.** ![[Pasted image 20250316162704.png]]
$$R_{j} = \arg_{min}  \sum^{J}_{j=1} \sum^{p}_{i \in j}(y_{i} - \hat{y}_{_{R_{j}}})^2$$
 + ? Since we have more than 7 observations, on the right side (Dosage >= 14.5), we can split them into 2 groups. 
 + $ And we do that by finding the threshold that gives us the smallest sum of squared residual (like before).
+ ? Because the **node on the left** indicate `< 29` have **less than 7 nodes**, we make it a **Leaf** with **average Drug Effectiveness of 2.5%** 
![[Pasted image 20250316163948.png]]


+ ? For the other half, since we have **more than 7 observations we can split them into 2 groups.** by finding the threshold that gives us the minimum sum of squared residuals.
+ $ Because both half contain less than 7 observations, this is the last split. With both half have their **average Drug Effectiveness** as value: left for Dosage < 23.5% is 52.8% effectiveness, where the right is 100% effectiveness when Dosage >= 23.5.
![[Pasted image 20250316164254.png]]
![[Pasted image 20250316164402.png]]
+ @ That how you build a tree using a single predictor **Dosage** to predict **Drug Effectiveness**![[Pasted image 20250316164739.png]]

+ @ Now let's talk about **how to build a tree to predict Drug Effectiveness using a bunch of predictors.**
+ ? Like Before, we **start by using Dosage to predict Drug Effectiveness**. Try different thresholds for **Dosage** and calculate the sum of squared residuals (SSRs) at each step. And **pick the threshold that gives us the lowest SSRs.** ![[Pasted image 20250316170754.png]]
+ ? Just like Dosage, we try **different threshold for Age and calculate the sum of square residual at each step and pick the minimum sum of squared residuals**.
![[Pasted image 20250316165128.png]]
The best threshold become a candidate for the root. 
![[Pasted image 20250316165508.png]]

For sex there only 1 threshold to try. So we use that threshold to calculate the sum of square residuals. 
+ ? Basically calculate the **average Drug Effectiveness for Female and Male Leaf.**  
![[Pasted image 20250316165559.png]]
![[Pasted image 20250316165653.png]]

+ ? Note: SSRs mean the sum of all SSR of 1 candidate. SSRs of `Dosage < 15` for example: ![[Pasted image 20250316171154.png]]

+ $ After collect all the Candidate, we **compare the sum of squared residual** (SSRs) for each candidate. And **Pick the candidate with the lowest value: `Age > 50` with SSR = 12.017** ![[Pasted image 20250316170446.png]]
+ $ Then we grow the tree just like before, except now we **compare the lowest sum of squared residuals from each predictor.**  ![[Pasted image 20250316174132.png]]

 
```ad-summary
In a Regression Tree, each leaf represents a numeric value.

Case 1: 1 Predictor and 1 Prediction
We determine how to divide the observations by trying different thresholds and calculating the sum of squared residuals at each step.
-> The threshold with the smallest sum of squared residuals become candidate for the root of the tree.

Case 2: Multiple Predictors and 1 Prediction
If we have more than 1 predictor we find the optimal threshold for each one. 
-> Pick the candidate with the lowest sum of squared residual to be the root.

Set Minimum number of Observation in a node to prevent Overfitting.
```


# Regression Tree Prunning
+ $ **Method:** **Cost Complexity Pruning or Weakest Link Pruning** to reduce overfit
![[Pasted image 20250316182357.png]]

All test data are pretty close but the 4 observation above is completely offset. This mean ours model is overfit.
+ $ One way to prevent Overfitting a Regression Tree to the Training Data is to remove some of the leaves. And **replace the split with a leaf that is the Average of a larger number of observations.** ![[Pasted image 20250316182607.png]]
+ $ Now all of the observations between 14.5 and 29 go to the leaf on the far right.
+ ? Even though the large Residual tell us that the new tree doesn't fit the Training Data. The sub-tree does much better job with the **Testing Data.** ![[Pasted image 20250316182737.png]]

+ $ Again, if we wanted to prune the tree more, we could remove two more leaves. ![[Pasted image 20250316183039.png]] Or replace the split with a leaf that is the average of all the observations. ![[Pasted image 20250316183102.png]]
+ ? To determine which Tree to use. The **first step in Cost Complexity Pruning is to calculate the Sum of Squared Residuals for each tree**. ![[Pasted image 20250316183242.png]] 


+ ? **SSR of the 1st Tree:**
+ ? SSR of  `Dosage < 14.5` leaf
![[Pasted image 20250316183210.png]]
SSR of `Dosage >= 29` leaf
![[Pasted image 20250316183326.png]]
![[Pasted image 20250316183400.png]]
![[Pasted image 20250316183546.png]]
![[Pasted image 20250316183518.png]]

+ ? We do the same for the **2nd Tree.** ![[Pasted image 20250316183713.png]]![[Pasted image 20250316183753.png]]

+ ? We do the same for the **3rd Tree and 4th Tree** ![[Pasted image 20250316183944.png]]![[Pasted image 20250316184016.png]]

+ @ We see that the SRR increase drastically as the tree was prune. But that the whole idea of prunes trees, to ***not*** fit Training Data as well as the full sized tree.
+ ? How do we compare these trees ? By calculating a **Tree Score** that is based on the SSR for the tree or sub-tree and a **Tree Complexity Penalty** $\alpha$ that is a **function of the number of leaves** multiply with T. (i.e. number of leaves)   ![[Pasted image 20250316184243.png]]
For now let's set $\alpha=10.000$, so tree with the most branch get penalty the most. Thus making the 2nd tree the best tree because it has the lowest Tree Score. 
![[Pasted image 20250316184827.png]]
0, 10000, 15000, 22000


Let's talk about how to prune the regression tree and how to find the best value for $\alpha$.
+ $ By using **Cross-Validation** ![[Pasted image 20250316190319.png]]
1) Build a **full size Regression Tree** **using all the data** (training + testing data)
2) **Calulating Tree Score base on Training and Testing data repectively**.
3) Create new Data. Repeat


**10-Fold Cross Validation** .
+ $ Value for $\alpha$ **on average, gave us the lowest Sum of Squared Residuals with the Testing Data**, is the **final value** for $\alpha$
+ ? First, using **all** of the data to build a **full size Regression Tree.** (training + testing data) ![[Pasted image 20250316185411.png]]
+ ? Then increase $\alpha$ value gradually after each prune. From 0 to 10.000 to 15.000 to 22.000 **and get Tree with the lowest Tree Score**. 


+ ? Now split Training and Testing Dataset.
**Calculating Tree Score only using the Training Data** ![[Pasted image 20250316185754.png]]
**Calculating Tree Score only using the Testing Data** 
![[Pasted image 20250316185923.png]] 
Now we go back and **create new Training and Testing data.** And repeat the process 10 times.
**10-Fold Cross Validation** .
+ $ Value for $\alpha$ **on average, gave us the lowest Sum of Squared Residuals with the Testing Data**, is the **final value** for $\alpha$. Finally pick the tree with the corresponding $\alpha$ value.


## 1. Pruning in Regression Trees?

There are two types of pruning:
1. **Pre-pruning (early stopping):** Stop splitting when a condition is met (e.g., minimum number of samples in a node).
2. **Post-pruning (cost complexity pruning):** Grow the full tree first, then remove branches that do not significantly improve performance.


## 2. How Does Post-Pruning Work?
### Step 1: Grow a Full Tree

- Start by **growing the regression tree fully** (i.e., until every leaf contains only a few samples or **no further reduction in RSS is possible).**
- This tree will **overfit** the training data because it captures too much noise.

### Step 2: Define the Cost Complexity Function
To decide which branches to prune, we introduce a penalty term to balance **tree complexity** and **error**:
$$\sum_{j=1}^{J} \sum_{i \in R_j} (y_i - \hat{y}_{R_j})^2 + \alpha |T|$$

where:
- $C(T)$ is the cost of the tree T,
- $J$ is the number of leaf nodes,
- $(y_i - \hat{y}_{R_j})^2$ is the sum of squared residuals (RSS),
- $|T|$ is the number of terminal nodes (leaves),
- $\alpha$ is a hyperparameter controlling the trade-off between tree size and fit.

### Step 3: Find the Best Subtree

To select the best subtree, we find the tree $T^*$ that **minimizes the cost function**:
$$\arg\min_{T} C(T) = \arg\min_{T} \left( \sum_{j=1}^{J} \sum_{i \in R_j} (y_i - \hat{y}_{R_j})^2 + \alpha |T| \right)$$

- The **$⁡\arg \min$** operator finds the tree $T^*$ that minimizes the trade-off between the model complexity $|T|$ and the fit (RSS).
- If $\alpha$ is **too small**, we get a **complex tree** (risk of overfitting).
- If $\alpha$ is **too large**, we get a **very simple tree** (risk of underfitting).


### Step 4: Perform Pruning
1. **Start with the full tree**.
2. **Iteratively remove branches** that lead to the smallest increase in RSS per additional node.
3. **Stop when the pruned tree achieves the best balance** between complexity and predictive performance.

