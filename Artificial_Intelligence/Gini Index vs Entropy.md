
| Aspect                                            | **Gini impurity (diff class prob)**                                                                 | **Entropy (information gain)**                                                                         |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Formula**                                       | $G(p)=1-\sum_{i=1}^K p_i^{\,2}$                                                                     | $H(p)=-\sum_{i=1}^K p_i\log_2 p_i$                                                                     |
| **Interpretation from first principles**          | $G(p)$ = probability that **two independent draws** from the node land in **different** classes     | $H(p)$ = **expected number of bits** needed to encode a class label drawn from the node                |
| **Range (binary case)**                           | $0 \le G \le 0.5$                                                                                   | $0 \le H \le 1$ bit                                                                                    |
| **Gradient near the edges**                       | Flatter for extreme probabilities (e.g. 0.95 vs 1) → slightly **less sensitive** to very pure nodes | Steeper near 0 and 1 → pushes splits a bit harder toward perfect purity                                |
| **Bias in practice**                              | **Tends to isolate** the **largest class first**, because **squaring** inflates big $p_i$           | Tends to prefer **balanced** splits where child nodes have similar class mixes (high information gain) |
| **Computational cost**                            | Adds, squares → very cheap (no transcendental functions)                                            | Needs $\log$; slightly slower (but negligible with modern libraries)                                   |
| **Units**                                         | Unit-less “mismatch probability”                                                                    | Bits (Shannon information)                                                                             |
| **Smoothness (for gradient-based tree variants)** | Quadratic → differentiable everywhere                                                               | Has an infinite slope at $p_i=0$ but still differentiable for $p_i>0$                                  |
| **Typical defaults**                              | CART (Scikit-learn), C4.5’s *gain ratio* denominator                                                | C4.5, ID3; many libraries offer it as an option                                                        |
| **Effect on final tree**                          | Often yields *shallower* trees with similar accuracy                                                | May produce *slightly deeper* trees but occasionally better class separation on rare classes           |
| **Empirical accuracy**                            | Usually within ±0.5 % of entropy on balanced data                                                   | Same; gains mainly show up on highly skewed or very small datasets                                     |
| **When practitioners switch**                     | Large data sets where speed matters; quick random forests                                           | Small, skewed data or when model interpretability benefits from more balanced splits                   |
| **Can be combined with class weights?**           | Yes – just weight the counts before computing sums                                                  | Yes – logs are applied after weighting                                                                 |

---

### 1 How a split score is computed

For either metric:

$$
\text{Gain}
=\underbrace{I(\text{parent})}_{\text{impurity before}}
-\Bigl(
\frac{n_L}{n_P}I(\text{left})
+\frac{n_R}{n_P}I(\text{right})
\Bigr).
$$

The tree picks the split with the **largest gain**.  Only the definition of $I(\cdot)$ differs.

---

### 2 Concrete numeric comparison (binary case)

Suppose a parent node has 60 % YES / 40 % NO.  
A candidate split yields:

| Node | YES | NO |
|------|-----|----|
| Left | 45  | 5  |
| Right| 15 | 35 |

**Gini gain**

$$
\begin{aligned}
G_P &= 1-(0.6^2+0.4^2)=0.48 \\
G_L &= 1-(0.9^2+0.1^2)=0.18 \\
G_R &= 1-(0.3^2+0.7^2)=0.42 \\
\text{Weighted} &=\frac{50}{100}0.18+\frac{50}{100}0.42=0.30\\
\Delta G &=0.48-0.30=0.18
\end{aligned}
$$

**Entropy gain**

$$
\begin{aligned}
H_P &= -0.6\log_2 0.6 -0.4\log_2 0.4 \approx 0.97 \text{ bits}\\
H_L &\approx 0.47 \text{ bits}\\
H_R &\approx 0.88 \text{ bits}\\
\text{Weighted}&=\tfrac{1}{2}(0.47+0.88)=0.675\\
\Delta H &=0.97-0.675 \approx 0.295\text{ bits}
\end{aligned}
$$

Both criteria say the split is good, but **entropy rewards it more strongly** because the right child is still moderately impure and entropy is steeper away from the extremes.

---

### 3 Practical guidelines

| If you care about … | Choose … | Rationale |
|---------------------|----------|-----------|
| Training speed on millions of rows / random forests | **Gini** | 20–30 % faster in practice |
| Slight edge on minority-class recall | **Entropy** | The log term penalises moderate impurity harder |
| Explanatory simplicity (fewer levels) | **Gini** | Tends to finish splitting once a dominant class is isolated |
| Theoretical link to information theory | **Entropy** | Directly measures expected message length |

*Reality check:* On most real-world tabular datasets both yield virtually identical test accuracy; tree depth and pruning strategy usually matter more.

---

### 4 Switching criteria in Scikit-learn
```python
from sklearn.tree import DecisionTreeClassifier

tree_gini   = DecisionTreeClassifier(criterion="gini",   random_state=0)
tree_entropy= DecisionTreeClassifier(criterion="entropy",random_state=0)
```

Everything else—max depth, min samples per leaf, class weights—stays the same.

---

### 5 Key take-away

Both Gini and entropy satisfy the **first-principle requirements** for an **impurity metric**:

1. **Zero when a node is pure.**  
2. **Maximal when classes are evenly mixed.**  
3. **Monotonically decreasing as purity increases.**

They merely quantify impurity through **different lenses**—mismatch probability vs. coding length—which leads to small, predictable biases but rarely changes the big picture of decision-tree performance.