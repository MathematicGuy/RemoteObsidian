**Abstract:** Assign category (i.e. label) to new point base on which ever categories (i.e. other points) is closer to its. 
![[Pasted image 20250203094853.png]]
0) Given there're already 2 categories.
1) Innitialize k (k's position).
2) Compute distance between k and other points.
3) Select *K-Nearest Neighbor* by sorting top k distances from closest to farthest. (e.g. A: 0.5, B: 0.7, A: 0.8) 
4) Within *K-Nearest Neighbour*, get the most frequent class (i.e. category A)
5) Assign class label of k based on the most frequent class.

**Example**
![[Pasted image 20250203101009.png]]
>With input as k = 2.4 (*i.e. x_test*) we get distances from k to all points. Then selecting top k, with k=1 we choose top 1 closest distance to k (don't need to sort), with k=3 we choose top 3 closest distance "0.7, 0.9, 1" to k then selecting most frequent Label 0 since 0.7 and 0.9 are both label 0. Finally assign k as Label 0. 


