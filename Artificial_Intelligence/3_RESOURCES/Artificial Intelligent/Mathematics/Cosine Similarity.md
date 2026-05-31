### 1. Cosine Similarity Fomula
$$\frac{A.B}{||A||.||B||}$$
measures the alignment (angle) between 2 vectors A and B, independent of their magnitude. Where
+ $A. B$ (Dot Product): Measure how much 2 vectors "overlap" in direction. (i.e. their direction similarity)
+ $||A||$ and $||B||$ (Vector Magnitudes): Normalize the vectors so that the result focuses on directional similarity rather than magnitude. This is because *vector consist of 2 components, direction and magnitude, by dividing the magnitude what left of is vectors direction.*
+ **Division by** $||A||.||B||$: Convert the result to a **value between -1 and 1**
+ $ In short, **Cosine Similarity evaluates direction of vectors while disregarding their magnitude.** 
 a
### 2. Intuition: Why use this
+ If **A and B are Aligned** (point in the same direction) -> Cosine similarity = 1 (maximum similarity)
	![[Pasted image 20250309042952.png]]
+ If **A and B are Perpendicular/Orthogonal** (point in the same direction) -> Cosine similarity = 1 (maximum similarity)
	![[Pasted image 20250309042906.png]]
+ If **A and B are Opposite (point in the opposite direction)** -> Cosine similarity = -1 (complete dissimilarity)
	![[Pasted image 20250309042943.png]]

