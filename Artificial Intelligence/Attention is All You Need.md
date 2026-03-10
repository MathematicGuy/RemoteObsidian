**Multi-head Attention** layer **act the same way** as a **Linear Layer** but much more efficient, in comparison for 
+ MhA use **x1000 less Computation than Linear**
+ MhA have **x4.000.000 less Parameters than Linear**
[How Attention Mechanism Works in Transformer Architecture](https://www.youtube.com/watch?v=KMHkbXzHn7s)
[[Transformer Neural Networks Derived from Scratch]]

---
### How Attention Got So Efficient `[GQA/MLA/DSA]`
![[out_attn.png]]
+ ? In token prediction task, original Attention recalculate Q,K,V matrix for every new token, this require a lot of Memory: ![[Pasted image 20260307164555.png]]
A solution is to *cache* Key and Value, this method called *KV Caching*. However the required Memory would be enourmous:![[Pasted image 20260307164726.png]] 
To reduce required memory, new method called *Multi Query Attention (MQA)* ask if we could *reduce the number of cache for K&V while keeping Q unchanged across heads.* Although this reduce memory significantly, the *model loss its ability to capture complex relationship between tokens* -> performance degrade.     
	e..g. Q remain unchange, Keep only 1 copy of K & V then paste them across dimension (d_k, d_v).  
![[Pasted image 20260307165323.png]]
+ ! Problem: cache only 1 K,V.. 
+ $ How about we *cache a group of Key & Value (a numbers of key and value) instead of 1 and duplicated them across attention heads*. This method called *Grouped-Query Attention (GQA),* its group Key & Value across Attention Head. 
	e.g. Keep only 2 distince Key and Value for each tokens. The Key & Value are then shared across Attention Heads (Note that QKV dimension remain unchange)    
![[Pasted image 20260307165513.png]]
-> Balance between memory efficiency and multi-head accuracy.
 