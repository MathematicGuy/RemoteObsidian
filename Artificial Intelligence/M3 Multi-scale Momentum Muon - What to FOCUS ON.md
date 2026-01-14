To understand **Section 7.2** effectively as a new researcher, you should approach it by breaking down the **motivation** (why they built it), the **theoretical lens** (how they view optimizers), and the **mechanism** (how the math works).

Here is a guide on what to focus on, the key papers to skim, and a breakdown of the formulas.

### 1. The Core Concept: Why "M3"?

Most standard optimizers (like Adam or SGD with Momentum) have a "short memory." They rely on an Exponential Moving Average (EMA) of gradients.

- **The Problem:** Because the older gradients decay exponentially ($\beta^t$), the optimizer "forgets" what the loss landscape looked like 1,000 steps ago. It only knows the immediate past.
    
- **The Solution (M3):** The authors apply their **Continuum Memory System (CMS)** logic to the optimizer itself. They create two "lanes" of memory:
    
    1. **Fast Memory ($M^{(1)}$):** Standard momentum (updates every step).
        
    2. **Slow Memory ($M^{(2)}$):** Long-term memory (updates slowly, aggregating gradients over large "chunks").
        

### 2. What to Focus On (The Prerequisites)

To understand this section "as a whole," you do not need to read every citation in depth. Focus on these three pillars:

#### A. Adam Optimizer (The Baseline)

The text explicitly builds on **Adam**. You must understand:

- **Momentum:** Accumulating gradients to smooth out the update trajectory.
    
- **Variance:** Accumulating the _squared_ gradients to normalize the learning rate.
    
- **The "Associative Memory" View:** The paper re-frames Adam. Instead of just "math," they view Adam as a memory module that is "learning" to map gradients to their variance.
    
    - _Advice:_ Don't get stuck on the complex math in Appendix B. Just understand the intuition: **The optimizer is "learning" the geometry of the loss landscape.**


#### B. The "Muon" Optimizer (The Mechanic)

The algorithm uses a function called `Newton-Schulz`. This comes from the **Muon optimizer** (Jordan et al. 2024).

- **What it does:** It is a matrix operation that "orthogonalizes" or normalizes a matrix. Think of it as a very sophisticated way of scaling the gradients so they don't explode or vanish, forcing them into a stable "metric space."
    
- _Advice:_ You don't need to derive Newton-Schulz. Just understand it as a **"Cleaning/Normalization Step"** that prepares the momentum matrix before it's applied to the weights.
    

#### C. The "CMS" Logic (The Novelty)

This is the paper's unique contribution. Focus on how they split the timeline into **chunks**.

- Instead of updating everything every step, the **Slow Memory ($M^{(2)}$)** waits for a chunk of steps ($\hat{C}$) to pass, sums up everything that happened, and _then_ updates.

---
### Compare Nested Learning and CMS 
Solve the question is

---

### 3. Understanding the M3 Fomula (Algorithm 1)
**Adam**, **Muon**, and **CMS** combine to form the M3 optimizer:
$$\Theta_{t} \leftarrow \Theta_{t-1} - \eta \cdot \underbrace{\frac{\overbrace{O_{t}^{(1)}}^{\text{Muon}} + \overbrace{\alpha O_{t}^{(2)}}^{\text{CMS}}}{\sqrt{\underbrace{V_{t}}_{\text{Adam}} + \epsilon}}}_{\text{M3 Combination}}$$

### **1. Adam: The Adaptive Denominator**

**Contribution:** Variance-based Scaling ($\sqrt{V_t}$)

- **Math:** $V_t = V_{t-1} + \beta_2 g_t^2$
    
- **Role:** It scales the learning rate inversely proportional to the gradient variance ($L_2$ norm of past gradients). This ensures the step size is adapted per-parameter, just like in the standard **Adam** optimizer.

### **2. Muon: The Orthogonalized Numerator**

**Contribution:** Newton-Schulz Orthogonalization ($O_t$)

- **Math:** $O_t^{(1)} \leftarrow \text{Newton-Schulz}(M_t^{(1)})$
    
- **Role:** Instead of using the raw momentum $M_t$, it applies the Newton-Schulz iteration to orthogonalize the momentum matrix. This effectively replaces the "magnitude" of the gradient with a "pure direction" matrix that has singular values close to 1, a technique borrowed directly from the **Muon** optimizer.


### **3. CMS: The Multi-Scale Aggregation**

**Contribution:** The Slow Memory Term ($\alpha O_t^{(2)}$)

- **Math:** $M_t^{(2)} = M_{t-1}^{(2)} + \beta_3 \sum_{\text{chunk}} g_i$
    
- **Role:** It introduces a second, parallel memory track ($O^{(2)}$) that updates at a slower frequency (summing gradients over a chunk/context window). Adding this long-term memory to the fast memory ($O^{(1)}$) is the core implementation of the **Continuum Memory System (Independent Variant)**.

----

#### First Varient
![[Pasted image 20260111213219.png]]
**"initial state of the MLP block in level s+1 is meta-learned in level s"** (Yellow)
	**Meaning:** The weights of the faster block (Level s+1) *don't start at random. They start at a specific value ($\theta$​) determined by the slower block (Level s).*
	
 **"higher-order in-context learning ability"** (Green)
		**Meaning:** Because the model has multiple levels of these "teachers" and "students," it essentially learns "how to learn" at multiple speeds simultaneously. It's not just adapting to tokens (standard ICL), but adapting its own parameters hierarchically.
    
**"each of the levels has its own context flow and re-initialized"** (Green)
	**Meaning:** This is the "Reset." The fast level only remembers things for a short time (its specific context flow). Once that context ends, it wipes its memory and goes back to the "factory settings" provided by the level above it.

#### Second Varient
![[Pasted image 20260111213208.png]]
**"initial state... connected through backpropagation in the lowest frequency level"** (Yellow)
	 **Meaning:** The "Starting Weights" for all blocks aren't learned dynamically by the immediate parent. They are learned by the **Level 1 (Lowest Frequency)** block. This makes Level 1 the ultimate foundation of the model.
	
**"C(1) is the context length... lowest frequency level"** (Yellow)
    **Meaning:** This refers to the longest possible context (usually the entire pre-training dataset).
    
**"meta-learned in the lowest frequency, the most persistent knowledge... compression of the same context flow"** (Green)
    **Meaning:** This highlights the stability of this variant. Because everything anchors back to Level 1, the model retains "Persistent Knowledge" effectively. All levels are essentially working together to compress the same stream of data, just at different resolutions


![[Pasted image 20260111213153.png]]
**"independent blocks with different context length"** 
	**Meaning:** This is the core feature. You have a "Short-Term" expert, a "Medium-Term" expert, and a "Long-Term" expert running in parallel.
$Agg(\cdot)$ -> Aggregate all models (e.g. Expert) to compute the output.



![[Pasted image 20260110174758.png | 585]]



![[Pasted image 20260111215447.png | 344]]