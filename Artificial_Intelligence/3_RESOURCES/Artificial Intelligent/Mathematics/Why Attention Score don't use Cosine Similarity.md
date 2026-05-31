### 1. [[Cosine Similarity]]
$$\frac{A.B}{||A||.||B||}$$
(note you can see A and B as q and k, it just annotation)
measures the alignment (angle) between 2 vectors A and B, independent of their magnitude. Where
+ $A. B$ (Dot Product): Measure how much 2 vectors "overlap" in direction. (i.e. their direction similarity)
+ $||A||$ and $||B||$ (Vector Magnitudes): Normalize the vectors so that the result focuses on directional similarity rather than magnitude. This is because *vector consist of 2 components, direction and magnitude, by dividing the magnitude what left of is vectors direction.*
+ **Division by** $||A||.||B||$: Convert the result to a **value between -1 and 1**
+ $ In short, **Cosine Similarity Evaluates Direction of vectors while Disregarding their Magnitude.** 
+ ! This ignore **Attention Mechanism where we care about both direction (similarity) and magnitude (strength of importance)**. If we normalize everything with $||q||.||k||$ we **might lose valuable magnitude information.**  
	Many word transfer a similar meaning (similarity) without magnitude, we cannot know which word is the relavent to the current context.
+ ! Softmax Needs Logits in a Certain Range, **Cosine similarity** produces values between **-1 and 1**, which are much smaller and could make softmax too **flat** (bc Cosine Similarity value are too close to each other) thus reducing focus (i.e. not softmax won't focus on a specific vector) 


### 2. Role of $d_{k}$ in Attention Scaling 
In Self-Attention, the raw attention scores are computed as 
$$q.k^T$$
To **stabilize training**, we just scale attention score by its own vector dimension $d_{k}$:
$$\frac{q.k^T}{d_{k}}$$
note:
+ q and k have the same dimension $d_{k}$
+ bc when multipling multiple values, the whole value scale-up) 
+ $ This prevent large dot product values from making softmax *too sharp* (i.e assigning almost all attention to one token) or *too flat* (i.e probabilty distributed equally) 


### Summary: Why use $d_{k}$ Instead of Cosine Similarity

| Factor                       | Cosine Similarity $$\frac{q \cdot k}{\|q\| \cdot \|k\|}$$ | Scaled Dot-Product Attention $$\frac{q \cdot k}{\sqrt{d_k}}$$ |
| ---------------------------- | --------------------------------------------------------- | ------------------------------------------------------------- |
| **Magnitude Sensitivity**    | Removes magnitude (only measures direction)               | Preserves magnitude information                               |
| **Softmax Behaviour**        | Produces values between -1 and 1 (softmax too flat)       | Keeps values in a stable range                                |
| **Computational Efficiency** | Requires extra norm calculations                          | Simple scalar division                                        |

### Impact of $d_{k}$ 

| **$d_k$ Size**                    | **Impact on Attention Scores**           | **Impact on Softmax**                                   | **Impact on Training**                                      |
| --------------------------------- | ---------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| **Small $d_k$ (e.g., 2-16)**      | Small raw dot product values             | Softmax becomes flat, reduced focus on important tokens | Training may be slower or less focused                      |
| **Moderate $d_k$ (e.g., 64-128)** | Balanced dot product range               | Softmax works well, with clear focus on relevant keys   | Optimal training dynamics, stable gradients                 |
| **Large $d_k$ (e.g., 512-1024)**  | Large dot product values (needs scaling) | Softmax becomes sharper, focusing on fewer keys         | Risk of gradient instability or overfitting without scaling |
