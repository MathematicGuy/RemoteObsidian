Concise example of **Identity Mapping Violation** specifically in the context of mixing your **SMIF** (Short-term) and **LMI** (Long-term) streams with your pre-trained **Spatial** stream.

### The Theory (Ideal Identity Mapping)
According to the Identity Mapping paper, the signal should flow through the network like this:
$$\mathbf{x}_{l+1} = \mathbf{x}_{l} + \mathcal{F}(\mathbf{x}_{l})$$
**Key:** The coefficient of $\mathbf{x}_{l}$ is exactly **1**. This preserves the original signal (ImageNet features) indefinitely deep into the network.

### The Violation (Naive Mixing of SMIF/LMI)
If you apply standard Hyper-Connections to mix your new temporal streams without constraints (mHC), the equation changes to a weighted sum (linear combination):
$$\mathbf{x}_{l+1} = \underbrace{0.7 \cdot \mathbf{x}_{spatial}}_{\text{Pre-trained Stream}} + \underbrace{0.3 \cdot \mathbf{x}_{motion}}_{\text{SMIF/LMI Stream}} + \mathcal{F}(\dots)$$

### Why this is a "Violation"
	
1. **Decay of Pre-trained Knowledge:** The coefficient **0.7** (instead of **1**) acts as a "gate."
    
2. **Exponential Vanishing:** After passing through just 10 such layers, the original ImageNet information remaining is $0.7^{10} \approx 0.028$ (only **2.8%** left).
    
3. **Result:** The "Spatial Understanding" 2 from your pre-trained backbone vanishes, being overwritten by the randomly initialized motion features. The model forgets "what" objects look like while trying to learn "how" they move.
    
**In summary:** Any mixing that scales the original residual stream by a factor $< 1$ (to make room for SMIF/LMI info) violates the Identity Mapping, causing the pre-trained features to vanish rapidly.