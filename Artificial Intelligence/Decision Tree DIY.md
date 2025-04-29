[[Lecture_07_on_Decision_Trees.pdf]]
**Classification:** base on the inputs predict sth categorical (like spam or not spam label)
**Regression:** base on the inputs predict a number (like assign an accurate number)

![[Pasted image 20250420191858.png]]
![[Pasted image 20250420191911.png]]


Tabular Form -> Decision Tree.
Tyoes of Data Names: (but kind of the same) 
+ Table/Dataset/DataFrame/Matrix 
+ Columns/Characters traits/Attributes/Features

## Literature Review + Code
**Splitting Labels:** Find the best feature that best seperates the <=50k and >50k earners, moving left to right. If there're **2 best feature, its pick the first one.**
![[Pasted image 20250426170424.png]]
But for Race & Hours Per Week, we got the perfect split. So **what features does the algorithm picked, the answer is the *first* optimal feature they find, trees are greedy !**. Given our training data, **RACE IS USED AT THE ROOT NODE.**
![[Pasted image 20250426170554.png]]


Gini Impurity (using [[Gini Index]]) can also be understand as the prob for the model making mistakes. High is bad, Low is good.
Gini Impurity perfer imperfect (so marbels can have weight)
![[gini_impurity_image.png]]

## Bining
 To calculate Gini for continuous feature such as Age, the tree must first use a process called **Bining** to convert the numeric feature into mutiple classes (e.g. Age < 30), the step go as follow:
 1) **Sort the numeric data** (in ascending order from Low to High, bottom to top)
 2) **Exam a bunch of Split points and choose the one with Lowest Gini Score** (i.e. orange arrow) 
	![[Pasted image 20250427140300.png]]
	Age < 30 was the first optimal gini found for Age feature. 
	Then this Gini is stored and compared against the gini indexes of other features, if this proves the lowest gini, the root node will be Age < 30. ![[Pasted image 20250427140443.png]]
+ $ Inshort the algorithm calc Gini Impurity of each features in order to find the best split for each branch. 

## Decision Trees in Python
**Differences between the DecisionTreeClassifier and CART:**
+ DecisionTreeClassifier only works with numeric data. Categorical features must be transformed (i.e. encoded) to numerics form.


**One-Hot Encoding**
use `get_dummies()` from `pandas` to one-hot encode categorical data, prefix for extra annotation before each class name (for clearer class name). 
![[Pasted image 20250427143034.png]]
One-hot encoded multiple columns (for columns name in cat_features)
![[Pasted image 20250427143234.png]]

We want the most impurity the top node, so the lower we go the higher the purity. 

**Value on the right implies True "Yes", on the left implies False "No".** 
+ But the *"value variable"* inside each leaf mean represent just that.
	+ **value at index 0** mean there're n class that **sastisfied root class condition.**
	+ **value at index 1** mean there're n class that are **not sastisfied root the class condition**.
	e.g. On the bottom right leaf, `value = [323, 3057]` mean there are **323 rows** that are less `<= 50K` and there're **3057 rows** have label `> 50K`. That is why **leaf class label are > 50k** because there're more of them. 
	e.g. On the bottom left leaf `value = 2815, 236` mean there are **2815 rows**  `<= 50K` and **236 rows** `> 50K`. That is why the **leaf class is <= 50K**. 
	
![[Pasted image 20250427150700.png]]


$$z = \frac{x_i - \mu}{\sigma}$$