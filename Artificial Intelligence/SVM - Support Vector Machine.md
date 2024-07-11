[[SVM HW]]

Face (green) / Non-Face (red)
![[Pasted image 20240625133833.png]]
> Can be written using (for 2D plane)
![[Pasted image 20240625133852.png]]

**A Linear Decision Boundary in 3-D space is a 2-D Plane**
![[Pasted image 20240625133959.png]]

**What is the optimal decision boundary ?**
> we do that using a safe zone or a margin: **width that u can extend until you hit features of both size**.
![[Pasted image 20240625134256.png]]
> Support Vectors: Closest data samples to the boundary
+ When points touching the boundary, its **supporting us to find the safe zone**. Thus we called them Support Vector. When we finding out those point, we can ignore all rest (points).

#Example:
**Given:**
![[Pasted image 20240625134620.png]]

**Find:**
![[Pasted image 20240625134657.png]]

## Finding Decision Boundary (W, b)
![[Pasted image 20240625134808.png]]

![[Pasted image 20240625135113.png]]


 ![[Pasted image 20240625135213.png]]