[[Nested Learning Overview Note]]

**Final Presentation Structure:**
	Title
	abstract | main Idea 1 | explain 1 -> explain 2 -> deeper explaination   
	abstract | main Idea 2 | explain 1 -> explain 2 -> deeper explaination   
	abstract | main Idea 2 | explain 1 -> explain 2 -> deeper explaination   

**Plan: Explore (1 + 2 part) -> Structurelize**
+ Keep Explore - Write down with my own though (concrete & help transfer my ideas to other better) not copying the HIGH LIGHT. 
+ Structurelize
# Nested Learning 
## Abstract 
Nested Learning - machine learning model with a set of nested, multi-level, and/or parallel optimization problems, each of which with its own “context flow".  
<-> Existing learning method learns from data through 
compressing their own "context flow" 

![[Pasted image 20260110161418.png | 190]]

Design Philopsophy: 
-> More "levels" resulting in higher-order in-context learning + effective continual learning capabilities. 


## Core Contribution Overview
### (1) Expressive Optimizers 
Gradient-based optimizers, such as Adam, SGD with Momentum, etc., are in fact associative memory modules. 
+ ? The momentum term in SGD compresses the history of gradients into a memory state to predict the next update. Therefore, an optimizer is just a learning module operating on a "context flow" of gradients

### (2) Self-Modifying Learning Module: 
Sequence model that learns how to modify itself by learning its own update algorithm

### (3) Continuun Memory System
>Control the update frequency of each levels. CMS creates a **spectrum of memory modules** updating at different rates, allowing the model to prioritize and retain information at varying timescales. 

**What Spectrum of Memory Module Means ?**
For Context, traditional DL like Transformers, memory is *binary (chose only 1:  short-term or long-term).* 
 **Short-Term Memory:** The Activations / KV Cache (Attention). This is highly volatile and limited by the context window.
 **Long-Term Memory:** The Weights (MLP layers). These are static (frozen) during inference and only updated during the massive pre-training phase -> so new update don't break old gradient. 
-> CMS breaks this binary, instead of "Frozen Weight vs Activate token", CMS replaces FFN/MLP with a *chain of MLP blocks*, where each block operates at a different update frequency. 
![[Pasted image 20260107144054.png]]
**Spectrum** mean you have a hierarchy of layers ranging from **High-Frequency to Low-Frequency.** Where the 
+ high-frequency block *update weights every token or small chunk*. Act as a "Working memory" that adapts instantly to the **immediate** input stream. 
+ slow-frequency update weights very rarely *every 1M tokens*, acts like "long-term storage", only when the information are consolidate enough does the model change it fundamental world-view. 
$$y_{t} = MLP^{f_{k}}(\dots MLP^{f_{k}} (o_{t})\dots)$$
+ $ In simple Term, CMS allow each MLP to Update by different TIME STEP.
+ ? Why and how CMS can help with longer context length and generally continual learning ?

![[Pasted image 20260110173918.png]]
![[Pasted image 20260102215707.png | 555]]



## Core Philosophy: Architecture and Optimization are the same thing
> "Old Philosophy" (Traditional Deep Learning) vs "New Philosophy" (Nested Learning) 

### Multi-level Optimization Problem

| **Philosophical Pillar**      | **Traditional Deep Learning View (The "Illusion")**                                                                                   | **Nested Learning View (The Reality)**                                                                                                                                          | **Practical Implication in NL**                                                                                                                                                                      |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Nature of Components**   | **Heterogeneous & Distinct:** Layers (Architecture) and Training Algorithms (Optimizers) are fundamentally different entities.        | **Uniform & Unified:** Architecture and Optimization are the _same concept_. Both are **Associative Memories** compressing a "context flow."                                    | **Deep Optimizers:** Optimizers are treated as neural networks (associative memories) that can be deepened (e.g., using MLPs instead of simple momentum) to better compress gradients.               |
| **2. Time & Memory**          | **Binary:** Short-term (Attention/Activations) vs. Long-term (Frozen Weights). This leads to "Anterograde Amnesia" after training.    | **Spectrum (Continuum):** Memory is a **Continuum Memory System (CMS)** with varying update frequencies (from fast gamma-like updates to slow delta-like consolidation).        | **Online Consolidation:** High-frequency layers adapt instantly to new tokens, while low-frequency layers consolidate patterns over millions of tokens, preventing catastrophic forgetting.          |
| **3. Learning Mechanism**     | **Static & External:** The model is a static artifact trained by an external "teacher" (optimizer) during a fixed pre-training phase. | **Recursive & Self-Referential:** The model is a "living" system of **nested loops**. It generates its own learning parameters (keys, values, learning rates) to modify itself. | **Self-Modifying Titans:** The "Hope" architecture generates its own optimization hyperparameters ($\eta_t, \alpha_t$) on the fly, effectively "rewriting its own learning code" based on the input. |
| **4. The Role of "Surprise"** | **Error Signal:** Gradients are merely error signals used to nudge weights, then discarded.                                           | **Memory Content:** Learning is the **compression of surprise**. Backpropagation is an associative memory mapping input data to its "Local Surprise Signal" (LSS).              | **Data Filtering:** If data is predictable (low surprise), the memory doesn't update. If data is surprising (high gradient), it triggers a memory update, naturally filtering for importance.        |
| **5. Definition of Context**  | **Fixed Window:** Context is limited to the immediate input window (e.g., 128k tokens). Pre-training is a separate past event.        | **Infinite Stream:** Pre-training is just **"In-Context Learning with an ultra-large context."** There is no boundary between training and testing.                             | **Lifelong Learning:** The model continuously metabolizes data. Fast loops handle the prompt; slow loops handle the "pre-training" data, treating both as context flows to be compressed.            |
| **6. Topology**               | **Fixed Graph:** The neural network structure (number of layers, connections) is fixed at initialization.                             | **Dynamic & Evolutionary:** The hierarchy can evolve. **Dynamic Nested Hierarchies (DNH)** allow the model to add/prune levels based on distribution shifts.                    | **Neuroplasticity:** The model can physically restructure itself (adding new memory modules) when the environment changes, ensuring sublinear regret in non-stationary tasks.                        |

### **Summary of the Paradigm Shift**

- **From:** A static tool built by engineers, where "learning" happens once and stops.
- **To:** A biological-like organism (a **Neural Learning Module**) composed of infinite loops of optimization, continuously metabolizing information at different speeds to achieve **Lifelong Intelligence**.


### Context Flow Compression


### Unified Learning Diagram 




## Neurophysiology Motivation
### Neuroplasticity


### Multi-Time Scale Update


### Uniform and Reusable Structure


### Memory Consolidation (Online / Offline)


## Key Contribution
### Coninuum Memory System (CMS)
```pseudo
\begin{algorithm} \caption{Multi-scale Momentum Muon (M3)} \begin{algorithmic} \STATE \textbf{Input:} Initial weights $\Theta_0$, objective $\mathcal{L}(\cdot)$, learning rate $\eta > 0$, Newton-Schulz steps $T$, momentum factors $1 > \beta_1, \beta_2, \beta_3$, $\alpha \ge 0$, $\epsilon > 0$, frequency $f$. \STATE Initialize momentums: $M_0^{(1)}, M_0^{(2)} \leftarrow 0$, $V_0 \leftarrow 0$; \FOR{lower-frequency iteration $k = 0, 1, 2, \dots$ } \STATE Slow Memory: $M_t^{(2)} = M_{t-1}^{(2)} + \beta_3 \sum_{i=(k-1)f}^{kf} g_i$; \STATE $O_t^{(2)} \leftarrow \text{Newton-Schulz}_T(M_t^{(2)})$; \FOR{$t = kf+1, kf+2, \dots, (k+1)f$} \STATE Compute Gradient: $g_t = \nabla_{\Theta_t} \mathcal{L}(\Theta_t)$; \STATE First Momentum: $M_t^{(1)} = M_{t-1}^{(1)} + \beta_1 g_t$; \STATE Second Momentum: $V_t = V_{t-1} + \beta_2 g_t^2$; \STATE $O_t^{(1)} \leftarrow \text{Newton-Schulz}_T(M_t^{(1)})$; \STATE $\Theta_t \leftarrow \Theta_{t-1} - \eta \frac{O_t^{(1)} + \alpha O_t^{(2)}}{\sqrt{V_t + \epsilon}}$; \ENDFOR \ENDFOR \end{algorithmic} \end{algorithm}
```




![[Pasted image 20260110175928.png]]

**Time-Complexity**
![[Pasted image 20260110174758.png | 585]]



## Hope Architecture 
### Self-Modifying Titans


### Continuum Memory Integration 
+ ? Integrate CMS into existing model (High Application)




























