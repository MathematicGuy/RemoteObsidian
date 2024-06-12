## Decision Tree

## Split
![[Pasted image 20240612143617.png]]
	10 records of class 0
	10 records of class 1
	![[Pasted image 20240612143637.png]]
	Example: Gender (Yes, No) (Yes are male, No are Female)
	+ *C0: 6* mean there are 6 Customer (Row) in class C0
	+ C1: 4 mean there are 4 Customer (Row) in class C1


![[Pasted image 20240612140012.png]]

**1. Calculate Entropy of the Target Variable (Risk):**
- Total samples: 8
- High-risk samples: 5
- Low-risk samples: 3

![[Pasted image 20240612140045.png]]
> Entropy of a Single Note
+ Entropy(Risk) = - (5/8) * log2(5/8) - (3/8) * log2(3/8) ≈ 0.954

**2. Calculate Information Gain for Each Attribute:**


![[Pasted image 20240612142548.png]]


## Bagging (*B*oostrap *agg*rega*ting*) 



## Random Forest

