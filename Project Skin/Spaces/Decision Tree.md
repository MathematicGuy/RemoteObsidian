## Example
![[Pasted image 20240612172033.png]]
+ Choose a attribute to be the top, Other attributes are split out into branch
+ More than 1 value can be use to represent a branch. Like Single and Divorced  

## Design Issues of Decision Tree Induction
#### How should training records be split
+ Method for specifying test condition
		+ Depending on attribute types: binary, nominal, ordinal, continuous
		+ Depending on number of ways to split: 2-way split, multi-way split
+ Measure for evaluating the goodness of a test condition
#### When should the splitting procedure stop?
+ Stop splitting if all records belong to the same class or have identical attribute values

## Split
![[Pasted image 20240612143617.png]]
	10 records of class 0
	10 records of class 1
	![[Pasted image 20240612143637.png]]
	Example: Gender (Yes, No) (Yes are male, No are Female)
	+ *C0: 6* mean there are 6 Customer (Row) in class C0
	+ C1: 4 mean there are 4 Customer (Row) in class C1

### How to determine the best split
Greedy approach (use when data are more bias to 1 side)
-> *Nodes with purer class* distribution *are preferred*
+ $ Example of Node Impurity
	![[Pasted image 20240612173452.png]]
+ Method to measures Node Impurity. (In this doc, let use Entropy)
	![[Pasted image 20240612173531.png]]

![[Pasted image 20240612173613.png]]
> M as the children weight. 


+ $ Choose the attribute test condition that produces the highest gain 
	![[Pasted image 20240612173803.png]]
+ Or equivelant, lowest impurity measure after splitting (M) 
+ Example: 
	![[Pasted image 20240612173849.png]]
	(P represent Gini impurity entropy)
	After splitting on both A and B, we need to decide which split is better. This is where the "Gain" calculation comes in: 
	+ ? Compare Gain from M1 and M2, a *Higher Gain indicates a better split*, as it means the impurity has been reduced more significantly.
	
```ad-summary
**Key Points**
	- The goal of splitting is to create purer nodes.
	- Impurity measures assess the mix of classes within a node (lower is better).
	- Gain quantifies the reduction in impurity achieved by a split (higher is better).
	- The attribute with the highest gain is chosen for the split.
```

### Measure of Impurity: Entropy
> Entropy at a given node t:
> ![[Pasted image 20240612174716.png]]
### Compute Entropy of a Single Node
![[Pasted image 20240612142548.png]]
+ ! Entropy for children is 0 -> Higher information gain. Because we have eliminate an option which direct us to reason the solution faster (give more information to the solution)

### Compute Information Gain After Splitting
**Information Gain (GAINsplit):** This measures the reduction in impurity (e.g., Gini impurity or entropy) achieved by splitting on a particular attribute. It's calculated as:![[Pasted image 20240612175137.png]]
> `GAINsplit = Impurity(parent) - [ Weighted average Impurity(children) ] `

### Split Information (splitINFO):
> This measures the entropy introduced by the split itself. It considers how many partitions (child nodes) are created and how evenly the data is distributed among them. It's calculated as:
	![[Pasted image 20240612180133.png]]
	where:
	+ ni = number of records in partition i
	+ n = total number of records

### Gain Ratio: **:** This is the Information Gain normalized by the Split Information:
	![[Pasted image 20240612180234.png]]

```ad-summary
**Key Points**

- Gain Ratio helps prevent overfitting by penalizing overly complex splits.
- It's a good choice when dealing with attributes that have a large number of values.
- The best attribute for splitting is the one with the highest Gain Ratio.
```
+ ? So is Decision Tree Based Classification good?
![[Pasted image 20240612180824.png]]


![[Pasted image 20240612140012.png]]

**1. Calculate Entropy of the Target Variable (Risk):**
- Total samples: 8
- High-risk samples: 5
- Low-risk samples: 3

![[Pasted image 20240612140045.png]]
> Entropy of a Single Note
+ Entropy(Risk) = - (5/8) * log2(5/8) - (3/8) * log2(3/8) ≈ 0.954

**2. Calculate Information Gain for Each Attribute:**


