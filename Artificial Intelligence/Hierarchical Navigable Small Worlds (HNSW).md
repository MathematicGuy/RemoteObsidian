+ ? **Trade Precision for Speed**. HNSW is an evolution of the Navigable Small Worlds algorithm for **Approximate Nereast Neighbor**, which based on the concept of **Six Degrees of Seperation**.  
![[Pasted image 20250606154211.png | 550]]

+ ? **Six Degrees of Seperation:** ![[Pasted image 20250324163339.png]]

## Probability Linked List
![[Pasted image 20250324165235.png]]
+ ? Skip List is built upon Sorted Linked List to counter the slows Searching problem O(n) by jumping across the subsequent layers instead of searching number by number. 
- **X**: **Queried Number** (i.e. number we want to search for)
- **a**: is the **Entry Point** (i.e. current node’s value)
- **b**: is the **Neighbor of node a** (i.e. Next Node)
- **DOWN, RIGHT**: Directions for pointer movement (and **LEFT** later in the algorithm).
- **H**: Current layer, where **H ≠ H₀** *means not the bottom/last layer*, and **H₀** represent the bottom layer.

**For every Search:**
1) **Search start from the top** of the Hiarchy (Top layer)
2) **IF** $H \neq H_0:$ (**If not the Last layer**)
    - If the _next node to the right_ exists and its value ≤ X → **RIGHT**
    - Else (next node’s value > X or no next node) → **DOWN**
- **At the bottom layer (H = H₀):**
    - If a < X and there is a next node → **RIGHT**
    - If a = X → Search successful, X is found
    - If a > X or no next node → X is not in the list

































---
**HNSW in real world** ![[Pasted image 20250324162950.png]]

+ ? Each **Node** is a **Chunk of Text.**
+ $ **Navigable Small Worlds** algorithms build a graph that mimic six degress of separation by **connects close vectors with each other but keeping the total number of connections small.**  e.g. every vector can connectd up to 6 other vectors. ![[Pasted image 20250324163651.png]]Where each Node represent a Text

### Nagivable Small Worlds: idea 1 searching for K-NN 
+ ? So how to we query in this graph.
+ $ **Goals:** **find the best node** that is **most similar to the query**.
	1) **Randomly chosen a entry point** (as the best node).
	2) **Compare similarity of the query and chosen node**. and all of its **neighboring node**. 
	3) If one of the friend node have **better similarity score, we MOVE the "best node" there**.  (e.g. node 2 have better similarity score so move to node 2)![[Pasted image 20250324164037.png]]
	4) **Repeat until all the friend nodes don't have a better similarity score** than the best node.  ![[Pasted image 20250324164216.png]]
+ ? For inserting a new node, we **query for best node then connect the new node to the top k**. (Like above but connect to best node).
 
#### HNSW: idea 2 - SKIP LIST
![[Pasted image 20250324165235.png]]
- **X**: The number we want to search for.
- **a**: The current node’s value.
- **DOWN, RIGHT**: Directions for pointer movement (and **LEFT** later in the algorithm).
- **H**: Current layer, where **H ≠ H₀** means not the bottom layer, and **H = H₀** means the bottom layer.

**For every Search:**
1) **Search start from the top** of the Hiarchy (Top layer)
2) **IF** $H \neq H_0:$ (**If not the Last layer**)
	+ IF `Current` is **smaller or equal** to `Search` (`a < X`)  -> **DOWN**
	+ ELIF `Current` is **greater than  `Search` (`a > X`) or there no next node**  -> **RIGHT**
	+ ELIF `Current` > `Search` < `Next` -> Move to 
	**ELIF:**
	+ **IF** `Current` is equal to `Search` (`a < X`)  -> **BREAK**

### HNSW: idea 1 + 2 Hierarchical Navigable Small Worlds
![[Pasted image 20250324171413.png]]
+ Repeat the search with randomly chosen starting points (on the top layer) and then keep the top K among all the visited nodes. 
+ ? Basically searching each layer and save the local best. 

