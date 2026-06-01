**Sovled Example:**
![[Pasted image 20240806130420.png]]

Step 1: Set K to define the number of cluster
-> K = 3
Step 2: Set all data as a single cluster
-> Cluster 1: {(2, 3), (3, 3), (6, 8), (8, 8), (7, 5), (9, 7)}
Step 3:
+ Use K-means with K=2 to split the cluster
+ Initial Centroids:
	Centroid 1: (2, 3)
	Centroid 2: (8, 8)
Euclidian Distance
$\sqrt{(x_2 - x_{1})^{2} + (y_{2}- y_{1})^2}$

First we Calc the distance of each point to each centroid.
![[Pasted image 20240806131101.png]]
Then we assign the it to the closest controid (A or B)
![[Pasted image 20240806130826.png]]
Then we calculate the new centroid base on the average of the Data Point in Cluster A and B respectively.
Ex: Average of Data Point in 
Cluster A: $centroid_{1}:\left( \frac{2+3+6}{2}, \frac{3+3+8}{3})\right.$  = (2.5, 3)
Cluster B: $centroid_{2}: \left(\frac{6+8+7+9}{4}, \frac{8+8+5+7}{4})\right.$ = (7.5, 7)
![[Pasted image 20240806132855.png]]
> Because K = 3, we need to divide (in half) one of 2 Cluster (A or B) again to get the 3rd Cluster. To do that, let Measure the distance for each intra cluster, this allow us to see which Cluster is more convergence. 
+ ? The more convergence a Cluster is, the closer to 0 their Sum of Square Distant is.

**Step 4: Measure the distance for each intra cluster.**
Sum of square Distance:
	![[Pasted image 20240806133229.png]]
	![[Pasted image 20240806133312.png]]


![[Pasted image 20240806133328.png]]


After splitting we repeat Step 3 again:
![[Pasted image 20240806133533.png]]
![[Pasted image 20240806133609.png]]
-> Now that we got the requirement Cluster K. we can stop here


