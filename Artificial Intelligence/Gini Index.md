+ ? In probability, **"replacement"** refers to **whether an item is put back into the pool of choices after it's been selected,  so the probability of selecting it remains the same on subsequent draws.** Without replacement means the selected item is not returned, altering the probabilities for future draw

```ad-success
**Gini Impurity** using *Gini Index which describe probability of picking 2 different class of an probability space*, same as Entropy, its used to **measure the inbalance in class distribution** by asking *"If I draw 2 samples from this node with replacement, what is the probability of picking 2 different elements ?"*.  With $p_{i}^2$ as the "same-class" probability, 1 represents certainty that sth happens; we substract the 'same-class' prob to get the 'different-class' prob.  
$$Gini = 1 - \sum_{i=1}^{C}p^{2}_{i}$$
Where 
+ 1 is the **probability** of something to happends, in other word the whole probability space (imagine a big square)
+ $p^2$ is the **probability of a independence event to happend**. (imagine a smaller square inside the big square)
+ $\sum_{i=1}^{C}p^{2}_{i}$ is the **sum of probability of each independence event to happend**.  
```
	
+ ? Basically Gini can tell the story **"which set is more diverse if each draws is independence ?"**  ![[Pasted image 20250423194831.png]]

The example below show the probability of the Leaf that is not both YES or both NO to happend. Let's go deeper fomula. 
![[Pasted image 20250423153731.png]]

+ $ Gini Impurity Fomula can be visualize (with 4 classes example) with 1 as the whole square represent the universal probability (contain all events occur), 
![[Pasted image 20250426161609.png]]
The **matched shape areas** represent event of **picking 2 identical element.** Hence the **prob of "picking different element" can be calc by substracting the prob of anything to the prob of "picking the identical element"**    
![[Pasted image 20250426161351.png]]
![[Pasted image 20250426162131.png]]
Another Example: 
![[Pasted image 20250426162345.png]]


## General Fomula
![[Pasted image 20250426162425.png]]

![[Pasted image 20250426162544.png]]



