*Gini* Impurity using Gini Index, **same as Entropy, its used to measure the inbalance in class distribution** by asking **"What is the Probability of picking 2 distinct/different elements"**. This index can be calculate by substracting 1 (total prob) to the sum of squared percentages of each class (i.e. prob of each class):
$$Gini = 1 - \sum_{i=1}^{C}p^{2}_{i}$$

+ ? Basically Gini can tell the story "which set is more diverse ?"  ![[Pasted image 20250423194831.png]]

![[Pasted image 20250423153731.png]]



The example below show the probability of the Leaf that is not both YES or both NO to happend. Let's go deeper fomula.

+ ? As you probably guessed, If 1 represent the total probability space, then substracting prob of "yes" and "no" leave us with the probability of "Yes" & "No" to not happend.

