**Classification:** base on the inputs predict sth categorical (like spam or not spam label)
**Regression:** base on the inputs predict a number (like assign an accurate number)

![[Pasted image 20250420191858.png]]
![[Pasted image 20250420191911.png]]


Tabular Form -> Decision Tree.
Tyoes of Data Names: (but kind of the same) 
+ Table/Dataset/DataFrame/Matrix 
+ Columns/Characters traits/Attributes/Features

## Literature Review + Code
**Splitting Labels:** Find the best feature that best seperates the <=50k and >50k earners, moving left to right. 
![[Pasted image 20250426170424.png]]
But for Race & Hours Per Week, we got the perfect split. So **what features does the algorithm picked, the answer is the *first* optimal feature they find, trees are greedy !**. Given our training data, **RACE IS USED AT THE ROOT NODE.**
![[Pasted image 20250426170554.png]]


Gini Impurity (using [[Gini Index]]) can also be understand as the prob for the model making mistakes. High is bad, Low is good.
![[gini_impurity_image.png]]

 
 




