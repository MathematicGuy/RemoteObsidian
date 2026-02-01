Note: Scout and check the slides first and organize ideas. Don't just learn in Linear, overview the material first. 
	Miros framework.

Modern Transformer base LLM suffer from Anterograde Amnesia which make every experience is a new experience, *they do not truely "learn" beyond their current context.* 
-> Only remmeber context from pretrain, don't learn new knowledge from live conversation because they will forget it in the next converstation. 

MoE with CMS is a Design Choice. 
How AI learn and memorize (Associate Memory)
### [[L1 vs L2 Regression and Loss Revision]].

---
### Associative Memory
is the ability to remember relationship between related abd unrelated evens/items/.... 
	ability to remember and connect ideas. 
Think of it as a dictionary, we have keys and values. *Learning is the process of acquiring the mapping.* (ie. *map the right key to value*, like human connect ideas or associating information)
![[Pasted image 20260130121818.png]]
Another update rule for the architecture and the memory that we have.


![[Pasted image 20260130122439.png]]
The init params try to compress the context while the inner loop try to adopt/learn some of the context using gradient descent. 
	-> Linear Attention is a form of 2 levels optimization problem, 1 is the Training process and 1 is the Adoption of the memory to the context.  

### MIRAS: A General Framework for Designing Archirectures
![[Pasted image 20260130122855.png]]
**Memory Architecture ->** compress the context into their params. More powerful architecture more Memory you have. 
**Attention Bias ->** Internal Objective that Measure the Quality of Mapping. 
**Retention Gate ->** How do you want to retain the knowledge from the past e.g. do u want forget gate or retain all the information in the past ?  
**Memory Algorithm ->** How do we want to learn the internal process ? Do we want GD or more powerful algo like GD with momentum or even a non-parametric solution like Softmax Attention ? That another Design choice. 

### Modern Architecture as Associate Memory
![[Pasted image 20260130124249.png]]

![[Pasted image 20260130124229.png]]
**Oja rule -** improve the Hebian rule that discussed by adding the regularization term 
**Omega rule -** objective agnostic
	"objective-agnostic" mean a algo operates independently of any spectific goal, predefined target or optimization criteria. For example, a Flexible Optimization algorithm that adapt through click-rate and likes to promote best selling product.
-> Insted of optimizing the current state of memory of the key and values like Kt and Vt it optimize the memory for a local window of the past keys and values. 
-> Not online learning, bc it need to map some of the past keys and values. Note: online learning mean only learning new/up-to-date knowledge without past knowledge.
+ $ Like Sliding Window Linear Attention: Instead of just updating the mem w.r.t $V_{i,}K_{i}$ we update to a past set of keys and values.
+ ? What online and offline learning in this slide mean ? Why the architecture related to online and offline ? Isn't its just data, not architecture ?

### Optimization and Backpropagation: A Preliminary Example
![[Pasted image 20260130125843.png]]
+ ? Explain the second $W_{t+1}$ equal to ... wth $u_{t+1}= \dots$
	-> Backprop is a form of Associate Memory that map its input to the Error rate that it receives for the backprop process. 

### Nested Learning
![[Pasted image 20260131155857.png]]
$f$ as update frequency
Another Example: 
+ Distillation create 2-levels learning structure where a small student network acts as an inner learner distilling knowledge from a larger teacher network (the outer learner)

![[Pasted image 20260131155842.png]]
Nested System: 
	Each block have its own gradient flow, locally solve a new problem that we define based on an Optimization process and Objective  
+ regularization tại thời điểm $t$: trọng số mới không khác biệt quá nhiều.  


**How levels can be Inter-connected ?**
Direct Connection of Levels (Prametric):
A simple Way is through Direct conditioning of the output of the slow network on the ouput of the fast network.
![[Pasted image 20260131160629.png]]
-> Fast-Level: Linear Attention. Slow-Level calc Attention QKV.

Based on the **Nested Learning (NL)** paradigm and the architectures of **CMS (Continuum Memory Systems)** and **TreeLoRA** described in the sources, here is a visualization of a **Base-Transformer integrated with TreeLoRA and CMS**.

![[Pasted image 20260131170037.png]]

Fast or Slow Frequency first is a design choice. 
Understand the fomula and conenct it with TreeLoRA to see how I can use Nested Learning perspective to apply Nested Learning architecture in TreeLoRA -> Perfect presentation with theory and application.



### **The Concept: "The Organized Memory"**

In this integrated architecture, we replace the standard static MLP block of a Transformer with a **CMS-TreeLoRA Hybrid Block**.

- **CMS Role (Time):** Splits learning into "Fast" (immediate adaptation) and "Slow" (consolidation) frequencies,.
- **TreeLoRA Role (Structure):** Organizes the "Slow" consolidation. Instead of overwriting long-term memory with a single average update (which causes forgetting), it dynamically routes the update to a specific branch of a LoRA tree based on gradient similarity,.

---

### **Architecture Visualization**
```
================================================================================
                INTEGRATED CMS-TREELORA TRANSFORMER BLOCK
================================================================================
INPUT (x_t)
  │
  ▼
[ SELF-ATTENTION LAYER ]  <-- (Frequency: ∞) Updates/Mixes every token
  │
  ▼
[ RESIDUAL + NORM ]
  │
  ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│   THE CMS-TREELORA "SMART" MLP BLOCK                                         │
│   (Replaces standard FFN)                                                    │
│                                                                              │
│   This block has two parallel tracks operating at different speeds:          │
│                                                                              │
│   TRACK A: FAST MEMORY (The "Worker")                                        │
│   [ Standard MLP / Fast Weights ]                                            │
│   • Update Freq: Every Step (f_1)                                      │
│   • Optimizer:   Muon / SGD (Reacts to immediate context)               │
│   • Role:        Adapts to current prompt/sentence instantly.                │
│                                                                              │
│             (+)  <-- Aggregation (Weighted Sum),                  │
│                                                                              │
│   TRACK B: SLOW MEMORY (The "Archivist" - TreeLoRA Integrated)               │
│   [ Tree of LoRA Adapters ]                                                  │
│   • Update Freq: Every Chunk (f_k) (e.g., every 1M tokens),       │
│   • Trigger:     Wait for Chunk Completion -> Calculate Cumulative Gradient  │
│   • Mechanism:   TreeLoRA Bandit Search                                │
│                                                                              │
│       1. Input: Cumulative Gradient of the Chunk (g_chunk)                   │
│       2. Search: Bandit Algorithm (LCB) finds best Branch              │
│       3. Selection:                                                          │
│          ROOT [Shared Knowledge]                                             │
│             │                                                                │
│             ├── Branch A [Math Tasks] -> Update Adapter A                    │
│             └── Branch B [Code Tasks] -> Update Adapter B                    │
│                                                                              │
│   • Role: Consolidates the chunk's knowledge into the specific               │
│           branch that matches the task, preventing interference.             │
└──────────────────────────────────────────────────────────────────────────────┘
  │
  ▼
OUTPUT (y_t)
```

---

### **Detailed Workflow of the Integration**

#### **1. The Fast Loop (CMS Layer)**

- **Source:**,,
- **Operation:** As tokens flow in, the **Fast Memory** (Track A) updates its weights immediately using a standard optimizer (like the Muon component of M3).
- **Goal:** To minimize the immediate prediction error for the current sentence.
- **State:** This memory is volatile; it might be reset or decay quickly after the context window shifts,.

#### **2. The Slow Loop (TreeLoRA Layer)**

- **Source:**,,
- **Operation:**
    1. **Accumulate:** The system accumulates gradients in the background for a specific **Chunk Size** (e.g., 1,000 steps). The Slow Memory is **frozen** during this time.
    2. **Trigger:** Once the chunk ends, instead of a simple addition ($M^{(2)} + \sum g$), the **TreeLoRA Logic** activates.
    3. **Route:** The **Bandit Algorithm** compares the chunk's gradient direction with the existing Tree Nodes (Root vs. Leaves). It finds the "Most Similar Task" in $O(1)$ time.
    4. **Update:** It performs a **Sparse Update** only on the selected LoRA adapter (branch).
- **Goal:** To store the knowledge from the last 1,000 steps permanently without overwriting (forgetting) the knowledge stored in other branches (e.g., overwriting "French grammar" with "Python syntax").

#### **3. The Aggregation**

- **Source:**,
- **Operation:** The final output of the MLP block is a weighted sum of the Fast MLP and the active TreeLoRA adapter. $$ y_t = \text{MLP}_{\text{Fast}}(x_t) + \alpha \cdot \text{TreeLoRA}_{\text{Selected}}(x_t) $$
- **Result:** The model has the "reflexes" of the Fast Learner and the "wisdom" of the organized TreeLoRA structure.

### **Why this Integration Works (Synthesis)**

- **CMS solves the "When":** It dictates that we shouldn't update long-term memory every second (which causes instability), but rather in consolidated chunks.
- **TreeLoRA solves the "Where":** It dictates that when we _do_ update long-term memory, we shouldn't just mash it into one matrix (which causes catastrophic forgetting), but route it to a specific semantic branch.
- **Efficiency:** TreeLoRA's Bandit search avoids calculating gradients for all past tasks, making it fast enough to run during the "Online Consolidation" phase of Nested Learning.