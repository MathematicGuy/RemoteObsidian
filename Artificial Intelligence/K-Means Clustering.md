> k as in k total time 

Number of Cluster = number of solution/output/type

**Step 1: Select the number of clusters you want to identify in your data. This is the "K" in "K-mean clustering"**
> K = 3. That mean to say we want ot identify 3 clusters.
![[Pasted image 20240605171949.png]]


**Step 2: Randomly select 3 distinct data points**
> Color circle are 3 initiate clusters
![[Pasted image 20240605172036.png]]

**Step 3: Measure the distance between the 1st point and the three initial clusters**
Distance from the point to
 + Blue cluster
 + Green cluster
 + Yellow cluster
![[Pasted image 20240605172140.png]]


**Step 4: Assign the 1st point to the nearest cluster**
> In this case, the nearest cluster is the blue cluster
![[Pasted image 20240605171145.png]]

> Now we to the same thing for every other unassigned point
![[Pasted image 20240605171145.png]]

>After all the points are in clusters, let calc the mean value (centroid of a cluster)
![[Pasted image 20240605171346.png]]


**Step 5:** Calculate the Mean of each cluster (Centroid of each cluster)
> Calc by sum up all the points adn dividing by the number of points.
![[Pasted image 20240605171645.png]]

![[Pasted image 20240605172707.png]]

So **is the current cluster the best K-Means Clustering?** 
> Since K-means clustering can't "see" the best clustering, its only option is to keep track of these clusters, and their total variance, and do the whole thing over again with different starting points.

So, back to the beginning re-do all the algo again...
![[Pasted image 20240605173000.png]]
> K-Means Clustering pick 3 initial cluster and then clisters all the remaining points, calc the means of each Cluster and the reclusters based on the new means. This **repeats until the clusters no longer change.**
![[Pasted image 20240605173248.png]]

+ ? How to decide the best K
![[Pasted image 20240605173335.png]]
> Let start with K = 1, it the worst  case scenario. We can quantify its "badness" with the total variation.

![[Pasted image 20240605173403.png]]
> Let try K = 2, the variance look much better now

![[Pasted image 20240605173537.png]]
> Each time we add a new cluster, the total variation within each cluster is smaller than before. And when there is only one point per cluster, the variation = 0

To find the best K, we need to find the 'elbow plot'
> **Elbow Plot:** There will be a K having a huge reduction after it, but after that reduction the variation doesn't go down as quickly. 
![[Pasted image 20240605173557.png]]



