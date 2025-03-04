+ $ Cross Validation allows us to **compare different machine learning methods** (e.g. K-Mean, Linear Regression, etc..) and get a sense of how well they will work in practice. 
+ ? We don't know **if the last 25% of the testing data, is different from the first 25% of the data.** R
+ $ Rather than worry about which part would be best for testing, **cross-validation uses them all, one at a time** and summarize the result at the end. 
note: The term **each parts**, **each sample and each block** are the same. 
![[Pasted image 20250302182359.png]]


**Step 0:** Split data into 3 parts: trainning set 60%, cross-validation 20%, test set 20%
![[Pasted image 20241104161426.png]]
note: some time it called the development set / dev set.

### K-Fold Validation Example
+ ? We have 4 parts in this example, This is called Three-Fold Validation
**Step 1:** Divided the data into 4 parts
**Step 2:** For each iteration (4 iterations): -> choose each block for testing, the rest for training.
	Choose 3 parts for training and 1 part for validation (visualization):
	![[Pasted image 20241105150428.png]] 
**Step 3**: Aggregate the results from all 5 iterations to compute a final performance metric.

In the end, every block of data is used for testing and we can compare methods by seeing how well they performed.
![[Pasted image 20250302182916.png]]

