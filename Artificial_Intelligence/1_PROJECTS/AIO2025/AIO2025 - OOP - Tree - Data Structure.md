**Tree Structure Overview**
![[Pasted image 20250624084033.png|500]]
+ Left Node Value < Right Node Value. 
+ Right Node > Root Node
+ A Full Tree consist of root node, children node.  
+ Tree inside another Tree call Subtree
+ A Full Binary Tree, each node in the last layer must have 2 leafs or no leaf at all.
+ Like any programming format, Root node index started from 0.
+ ? Note: a node can have more than 2 childrens. e.g. 3, 4 childrens under a nodes.

**Detail insight about Tree Data Structure**
![[Pasted image 20250624093357.png# left|550]] ![[Pasted image 20250624093443.png# right |350]]
```python
# This is how tree store in code
Tree = {
	'A': ['B', 'C'],
	'B': ['D'],
	'C': ['E'],
	'D': [],
	'E': []
}
```

OOP (Object Oriented Proramming) - Lập trình hướng đối tượng or Lập trình xoay quanh đối tượng. 
**O - Object.** Like real world object like a cars with attributes like color, model, behaviour, you can create Object like that too using Class. Where Object is an instance (thực thể) of a Class. Just imagine Class is the design, Object is the real thing. 
**O - Oriented.** Entire design and software is centered around these "objects". 
**P - Programming**. Yeah, it's brainstorming and coding.
![[Pasted image 20250624094705.png]]
Tree OOP design should be broken down into the lowest level, like NODE, the fundamental building block of a Tree.  

+ @ **Use Recursive** when you want to go deeper into Tree like Structure Object and automatically return if there nothing to return or a condition is meet.   ![[Pasted image 20250624104536.png]]
+ ? **Example:** Think A as a Object contain B and C. Each time you access A or children's of A (i.e. B, C) you apply a function. That Recursive.   
```python
Tree = {
	'A': ['B', 'C'],  
	'B': ['D'],
	'C': ['E'],
	'D': [],
	'E': []
}
```

## Traversal of Binary Tree
### BFS (Breadth First Searc h)
> Traverse all the nodes at the current depth before moving on to the vertices at the next depth level. 

### DFS (Deep First Search)
> The algorithm starts at the root node and explores as far as possible along each branch before backtracking (and repeat).


## Stack Data Structure Using List
### Stack


### Stack Operation
