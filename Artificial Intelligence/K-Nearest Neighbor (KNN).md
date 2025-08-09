**Abstract:** Assign category (i.e. label) to new point base on which ever categories (i.e. other points) is closer to its. 
![[Pasted image 20250203094853.png]]
0) Given there're already 2 categories.
1) Innitialize k (k's position).
2) Compute distance between k and other points.
3) Select *K-Nearest Neighbor* by sorting top k distances from closest to farthest. (e.g. A: 0.5, B: 0.7, A: 0.8) 
4) Within *K-Nearest Neighbour*, get the most frequent class (i.e. category A)
5) Assign class label of k based on the most frequent class. (`len(class_0) > len(class_1)` -> điểm thuộc `class_0` )

**Example**
![[Pasted image 20250203101009.png]]
>With input as k = 2.4 (*i.e. x_test*) we get distances from k to all points. Then selecting top k, with k=1 we choose top 1 closest distance to k (don't need to sort), with k=3 we choose top 3 closest distance "0.7, 0.9, 1" to k then selecting most frequent Label 0 since 0.7 and 0.9 are both label 0. Finally assign k as Label 0. 

### Scaling 
KNN depend on the distant. 
Unnormalized 2D data example: when pedal Length is much higher than pedal width.

![[Pasted image 20250805220258.png|533]]
TH features bị chênh lệch quá nhiều -> sử dụng distance hoặc gradient -> học bị sai. 
Giải quyết sử dụng Normalization -> trừ cho Mean rồi chia cho Standard Deviation. 

![[Pasted image 20250805222130.png]]

**KNN for Spam or Ham Classification** 
![[Pasted image 20250805222423.png]]

**TF-IDF**
**TF**
![[Pasted image 20250805230241.png| 355]]
**IDF**
![[Pasted image 20250805230259.png| 354]]


![[Pasted image 20250805230709.png]]

+1 để có thêm giá trị. 

