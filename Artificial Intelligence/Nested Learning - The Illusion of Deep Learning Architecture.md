# Nested Learning (Làm Slide)
## Abstract
Nested Learning - machine learning model with a set of nested, multi-level, and/or parallel optimization problems, each of which with its own “context flow".
<-> Existing learning method learns from data through compressing their own "context flow"

![[Pasted image 20260110161418.png | 190]]

Design Philopsophy:
-> More "levels" resulting in higher-order in-context learning + effective continual learning capabilities.

## Core Contribution Overview
### (1) Expressive Optimizers
Gradient-based optimizers, such as Adam, SGD with Momentum, etc., are in fact associative memory modules.
+ ? The momentum term in SGD compresses the history of gradients into a memory state to predict the next update. Therefore, an optimizer is just a learning module operating on a "context flow" of gradients

![[Pasted image 20260111201333.png]]
+ ? Similar to associate Input Error to the Gradient

In the training process itself, specifically the *backpropagation process*, can be modeled as an *associative memory.* **The model learns to map a given data point to the value of its local error**, serve as a measure of how "Suprising" or unexpected that data point was.
![[Pasted image 20260122082909.png]]

![[Pasted image 20240930164241.png | 554]]


+ ? What does it mean to say "The model learns to map a given data point to the value of its local error"
	*"mapping a data point to its local error"* means the model is actively trying to associate **"This specific input"** with **"The mistake I made on it."**
		By *updating the weight* ($W_{t+1}$), the models is *"storing" the connection between the Specific Input data and that "Error" its causes* -> By using the Weight, next time the model sees that data point (Key), it recalls the correction (Value) to adjust its behaviour.
	-> **Weight store Connection of (Input (Key) -> Error (Value))** in a neural network.
![[Pasted image 20260111202804.png]]
-> backpropagation can be viewed as an associative memory that maps each data sample to the error of its corresponding prediction

Prove backprop with momentum are 2 level associated memory.
![[Pasted image 20260111203553.png]]

The same apply to Attention Module in Transformer with 2 layers of Linear, 1st layer for updating weight of Keys K,Q,V while the second update MLP params.
![[Pasted image 20260111204711.png]]

### (2) Self-Modifying Learning Module:
Sequence model that learns how to modify itself by learning its own update algorithm
![[Pasted image 20260122091332.png]]
**Black-box:** Hides internal gradient flows and treats the model as a flattened image.
**White-box:** Makes internal gradient flows transparent, showing how each component updates itself.
**Mechanism:** 
+ Stacking static layers to extract features.
+ Nesting optimization problems where "inner" loops optimize local objectives (e.g., in-context learning).

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



![[Pasted image 20260111205410.png]]
(Pretrain) Frozen Layer -> MLP (learn new)
Instead of Frozen, how about we update the Pretrain Weight rarely over time.

![[Pasted image 20260102215707.png | 555]]


![[Pasted image 20260111205226.png]]

- **$x_t$**: The input data at time step $t$ (e.g., a token in a sequence).

- **$y_t$**: The final output of the CMS chain for that specific time .

- **$k$**: The total number of levels (or blocks) in the system.

- **$f_l$**: The **frequency** of the $l$-th level. This defines how "fast" or "slow" this specific block is. A high frequency means it processes information quickly; a low frequency means it changes slowly.

- **$C^{(l)}$**: The **Chunk Size** for level $l$. This is the specific number of steps this block waits before updating. It is calculated as the maximum context length divided by the frequency ($C^{(l)} := \frac{max_i C^{(i)}}{f_l}$). Lower frequency = Larger chunk size.

- **$MLP^{(f_l)}$**: The actual Neural Network block (Multi-Layer Perceptron) assigned to frequency $f_l$.

- **$\theta^{(f_l)}$**: The learnable **parameters (weights)** of that specific MLP block.

- **$\eta_t^{(l)}$**: The **learning rate** for level $l$ at time $t$. This controls how much the memory changes during an update.

- **$f(\cdot)$**: The error signal or gradient function (e.g., $\nabla \mathcal{L}$) derived from the objective function (like next-token prediction).


### **2 - The Formulas Line-by-Line**
The CMS is defined by two processes: **Processing the Data (Forward Pass)** and **Updating the Memory (Backward Pass/Update Rule)**.
![[Pasted image 20260111205226.png]]
#### **1. The Forward Pass (Equation 70)**
This formula describes how information flows through the hierarchy of memory blocks to generate an output. Where each layer update less frequence than the previous.
$$y_{t} = MLP^{(f_{k})} \left( MLP^{(f_{k-1})} \left( \dots MLP^{(f_{1})}(x_{t}) \right) \right)$$


#### **2. The Update Rule (Equation 71)**
This is the core "Continuum" logic. It dictates that blocks do **not** update at every step. They **update only when their specific "time chunk" is full.**
$$\theta_{i+1}^{(f_{t})} = \theta_{i}^{(f_{t})} - \begin{cases} \sum_{t=i-C^{(t)}}^{i} \eta_{t}^{(t)} f(\theta_{t}^{(f_{t})}; x_{t}) & \text{if } i \equiv 0 \pmod{C^{(l)}} \\ 0 & \text{otherwise} \end{cases}$$

- **$\theta_{i+1}^{(f_{t})} = \theta_{i}^{(f_{t})} - \dots$**: Weight update (New Weight = Old Weight - Change).

- **$\text{if } i \equiv 0 \pmod{C^{(l)}}$**: Checks if the current time step $i$ is a multiple of the **Chunk Size $C^{(l)}$.**
	
	**Meaning:** "Is it time to update yet?" If the chunk size is 100, this block only updates at step 100, 200, 300, etc.

- **$\sum_{t=i-C^{(t)}}^{i} \dots$** If it _is_ time to update, the model sums up the gradients (learning signals) from the **entire past chunk** (from $t = i - \text{ChunkSize}$ to now).
	
    **Meaning:** Instead of reacting to the last token, the block compresses the "experience" of the last 100 tokens into a single update. This creates a stable, long-term memory update.

- **$\eta_{t}^{(t)} f(\theta_{t}^{(f_{t})}; x_{t})$** Calculates the gradient (error) for a single specific moment $t$ inside that chunk, scaled by the learning rate $\eta_{t}^{(t)}$.
	
- $0 \text{ otherwise}$ If the *condition is not met* (e.g., at step 99 of a 100-step chunk), the *change is 0.*
	
    **Meaning:** The memory remains **frozen** and persistent during the chunk, acting as a stable storage of knowledge until the next scheduled update.

## Key Contribution
![[Pasted image 20260111211501.png]]
Figure 5: A comparison of Hope architectural backbone with Transformers (Normalization and potential data-dependent components are removed for the sake of clarity)

### Coninuum Memory System (CMS)
**Meta-Learned Initialization (The Starting Point)** Standard models often start with random or zero-initialized memory states.
+ ? **How it works:** unlike standard linear transformers (which often start at zero), CMS uses the lower-frequency levels (or pre-training) to provide a "smart" initial state $\theta_0^{(f_{s+1})}$ that allows faster adaptation.

![[Pasted image 20260111210629.png]]
![[Pasted image 20260110173918.png]]
![[Pasted image 20260111210635.png]]

Nested Learning is a perspective to develop CMS.
![[Pasted image 20260111205226.png]]

#### **1. The Forward Pass (Equation 70)**
$$y_{t} = MLP^{(f_{k})} \left( MLP^{(f_{k-1})} \left( \dots MLP^{(f_{1})}(x_{t}) \right) \right)$$

#### **2. The Update Rule (Equation 71)**
[[M3 Multi-scale Momentum Muon - What to FOCUS ON]] 
Note: Adam + Muon + CMS = Multi-scale Momentum Muon (M3)
![[Pasted image 20260111211050.png]]
+ ? Remove **single** momentum vector ($m_t$​) and replace it with a **Continuum Memory System (CMS)** structure.
Note: For each $k-iteration$, $O_t^{(2)}$ (CMS) update in parallel with $O_{t}^{(1)}$ (Muon), but if Chunk size $\hat{C}$ is not met, $M_{t}^{(2)}$ does not change. 
![[Pasted image 20260111213153.png]]

![[Pasted image 20260112141205.png]]


**CMS Varient**
![[Pasted image 20260111213219.png]]

![[Pasted image 20260111213208.png]]

![[Pasted image 20260111213153.png]]


![[Pasted image 20260111211524.png]]
A comparison of Hope architectural backbone with Transformers (Normalization and potential data-dependent components are removed for the sake of clarity).


**Time-Complexity & Result**
![[Pasted image 20260110174758.png | 585]]

![[Pasted image 20260111211723.png]]


![[Pasted image 20260111211903.png]]


# Left-Untouch
## Neurophysiology Motivation
### Neuroplasticity

### Multi-Time Scale Update

### Uniform and Reusable Structure

### Memory Consolidation (Online / Offline)

---

![[Pasted image 20260122091647.png]]