---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'



# Based on the mathematical formulations and architectural descriptions in the provided sources, specifically the "Hope Neural Learning Module" sections and the "Continuum Memory System" definitions, here is the feedforward workflow of the HOPE architecture drawn in text format.

### HOPE Architecture Feedforward Workflow

```text
+-----------------------------------------------------------------------+
|                       INPUT TOKEN (x_t) at time t                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                   STEP 1: SELF-MODIFYING TITANS MODULE                |
|           (Replaces Standard Attention / Sequence Mixer)              |
+-----------------------------------------------------------------------+
|                                                                       |
|  [A] Adaptive Projections (Self-Referential Generation)    |
|      The model uses previous memory states to generate its own        |
|      parameters for the current step (Keys, Values, Rates).           |
|                                                                       |
|      k_t = M_k(x_t)      (Adaptive Key)                               |
|      v_t = M_v(x_t)      (Adaptive Value)                             |
|      η_t = M_η(x_t)      (Adaptive Learning Rate)                     |
|      α_t = M_α(x_t)      (Adaptive Decay/Retention)                   |
|      q_t = x_t * W_q     (Query is typically a standard projection)   |
|                                                                       |
|  [B] Memory Update (Inner Loop Optimization)                    |
|      The memory matrix (M) updates itself using the generated         |
|      parameters and a gradient-based rule (e.g., Delta Rule).         |
|                                                                       |
|      M_new = M_old - [Update based on k_t, v_t, η_t, α_t]             |
|                                                                       |
|  [C] Memory Retrieval (Forward Pass)                            |
|      The output (o_t) is retrieved from the updated memory using      |
|      the query.                                                       |
|                                                                       |
|      o_t = M_memory(q_t)                                              |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   | o_t (Intermediate Output)
                                   v
+-----------------------------------------------------------------------+
|                  STEP 2: CONTINUUM MEMORY SYSTEM (CMS)                |
|           (Replaces Standard Static Feed-Forward/MLP Block)           |
+-----------------------------------------------------------------------+
|                                                                       |
|   The output passes through a chain of MLPs. Unlike static MLPs,      |
|   these update their weights at different "frequencies" (chunk sizes).|
|                                                       |
|                                                                       |
|   +--------------------------+                                        |
|   |  CMS Block 1 (High Freq) | <--- Updates every small chunk         |
|   |  Input: o_t              |      (Fast adaption)                   |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block 2 (Mid Freq)  | <--- Updates every medium chunk        |
|   |  Input: Output of B1     |                                        |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|              .....                                                    |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block K (Low Freq)  | <--- Updates rarely / Long-term        |
|   |  Input: Output of B(k-1) |      (Persistent knowledge)            |
|   +--------------------------+                                        |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        FINAL OUTPUT (y_t)                             |
+-----------------------------------------------------------------------+
```

### Explanation of Components

**1. Self-Modifying Titans (The "Head"):**
Unlike a standard Transformer where projections (Keys/Values) are fixed linear layers ($x \cdot W$), HOPE uses "Self-Modifying" memories. The model generates its own parameters ($k_t, v_t$) and optimization hyperparameters ($\eta_t, \alpha_t$) based on the input and the previous state of its parameter-generating memories. This allows the model to modify its own learning dynamics on the fly.

**2. Continuum Memory System (The "Body"):**
Instead of a static Feed-Forward Network (FFN/MLP) found in standard Transformers, HOPE uses a CMS.
*   **Structure:** It is a nested chain of MLPs: $y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$.
*   **Function:** Each MLP in this chain updates its weights at a different frequency ($f$). High-frequency layers update often (learning immediate context), while low-frequency layers update rarely (preserving long-term knowledge), preventing catastrophic forgetting.

Based on the mathematical formulations and architectural descriptions in the provided sources, specifically the "Hope Neural Learning Module" sections and the "Continuum Memory System" definitions, here is the feedforward workflow of the HOPE architecture drawn in text format.

### HOPE Architecture Feedforward Workflow

```text
+-----------------------------------------------------------------------+
|                       INPUT TOKEN (x_t) at time t                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                   STEP 1: SELF-MODIFYING TITANS MODULE                |
|           (Replaces Standard Attention / Sequence Mixer)              |
+-----------------------------------------------------------------------+
|                                                                       |
|  [A] Adaptive Projections (Self-Referential Generation)    |
|      The model uses previous memory states to generate its own        |
|      parameters for the current step (Keys, Values, Rates).           |
|                                                                       |
|      k_t = M_k(x_t)      (Adaptive Key)                               |
|      v_t = M_v(x_t)      (Adaptive Value)                             |
|      η_t = M_η(x_t)      (Adaptive Learning Rate)                     |
|      α_t = M_α(x_t)      (Adaptive Decay/Retention)                   |
|      q_t = x_t * W_q     (Query is typically a standard projection)   |
|                                                                       |
|  [B] Memory Update (Inner Loop Optimization)                    |
|      The memory matrix (M) updates itself using the generated         |
|      parameters and a gradient-based rule (e.g., Delta Rule).         |
|                                                                       |
|      M_new = M_old - [Update based on k_t, v_t, η_t, α_t]             |
|                                                                       |
|  [C] Memory Retrieval (Forward Pass)                            |
|      The output (o_t) is retrieved from the updated memory using      |
|      the query.                                                       |
|                                                                       |
|      o_t = M_memory(q_t)                                              |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   | o_t (Intermediate Output)
                                   v
+-----------------------------------------------------------------------+
|                  STEP 2: CONTINUUM MEMORY SYSTEM (CMS)                |
|           (Replaces Standard Static Feed-Forward/MLP Block)           |
+-----------------------------------------------------------------------+
|                                                                       |
|   The output passes through a chain of MLPs. Unlike static MLPs,      |
|   these update their weights at different "frequencies" (chunk sizes).|
|                                                       |
|                                                                       |
|   +--------------------------+                                        |
|   |  CMS Block 1 (High Freq) | <--- Updates every small chunk         |
|   |  Input: o_t              |      (Fast adaption)                   |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block 2 (Mid Freq)  | <--- Updates every medium chunk        |
|   |  Input: Output of B1     |                                        |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|              .....                                                    |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block K (Low Freq)  | <--- Updates rarely / Long-term        |
|   |  Input: Output of B(k-1) |      (Persistent knowledge)            |
|   +--------------------------+                                        |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        FINAL OUTPUT (y_t)                             |
+-----------------------------------------------------------------------+
```

### Explanation of Components

**1. Self-Modifying Titans (The "Head"):**
Unlike a standard Transformer where projections (Keys/Values) are fixed linear layers ($x \cdot W$), HOPE uses "Self-Modifying" memories. The model generates its own parameters ($k_t, v_t$) and optimization hyperparameters ($\eta_t, \alpha_t$) based on the input and the previous state of its parameter-generating memories. This allows the model to modify its own learning dynamics on the fly.

**2. Continuum Memory System (The "Body"):**
Instead of a static Feed-Forward Network (FFN/MLP) found in standard Transformers, HOPE uses a CMS.
*   **Structure:** It is a nested chain of MLPs: $y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$.
*   **Function:** Each MLP in this chain updates its weights at a different frequency ($f$). High-frequency layers update often (learning immediate context), while low-frequency layers update rarely (preserving long-term knowledge), preventing catastrophic forgetting.


# def Multi_Scale_Momentum_Muon_M3(Theta_0, Objective_L, eta, T, betas, alpha, epsilon, f):
    """
    DESCRIPTION:
    -------------------------------------------------------------------------
    This function implements the M3 optimizer, which applies the Continuum Memory 
    System (CMS) logic to optimization. 
    
    Standard optimizers (like Adam) effectively have a "short-term memory" because 
    gradients decay exponentially. M3 fixes this by creating two "lanes" of memory:
    1. A "Fast Lane" (First Momentum) that updates every step (standard behavior).
    2. A "Slow Lane" (Slow Memory) that aggregates gradients over a long "chunk" 
       (frequency f) before updating.
    
    The final weight update is a weighted combination of both the fast (short-term) 
    and slow (long-term) directions, normalized by Newton-Schulz iteration to 
    [cite_start]ensure the updates are chemically "pure" (orthogonalized)[cite: 2960, 2982].
    -------------------------------------------------------------------------
    """

    # Initialization
    # We initialize the "Fast" momentum (M1), "Slow" momentum (M2), and Variance (V) to zero.
    M1, M2, V = 0, 0, 0  
    Theta = Theta_0

    # ==============================================================================
    # LONG COMMENT (The Slow/Outer Loop):
    # [cite_start]This loop represents the "Lower-Frequency Level" of the CMS[cite: 2958].
    # Instead of reacting to every single bump in the loss landscape, this level 
    # waits for a full "chunk" of steps (defined by frequency `f`) to complete. 
    # It acts as the "Long-Term Memory" of the optimizer. By summing gradients over 
    # a long period, it captures the global direction of the optimization, ignoring 
    # temporary noise.
    # ==============================================================================
    k = 0
    while True: # Lower-frequency iteration loop
        
        # --------------------------------------------------------------------------
        # LONG COMMENT (Slow Memory Update):
        # [cite_start]Here we perform the "Associative Memory" update for the slow level[cite: 2958].
        # We aggregate ALL gradients from the previous chunk. This summation is the 
        # "context" that this memory level is compressing. 
        # Note: In the image/formula, the sum range is roughly the last `f` steps.
        # --------------------------------------------------------------------------
        sum_gradients = sum(gradients_from_last_chunk) # Aggregating context (gradients)
        
        [cite_start]M2 = M2 + betas[2] * sum_gradients             # Update Slow Memory with long-term context [cite: 2961]

        # --------------------------------------------------------------------------
        # LONG COMMENT (Newton-Schulz Normalization):
        # [cite_start]This step comes from the Muon optimizer[cite: 2588, 2590]. 
        # We treat the momentum matrix M2 as a mapping we want to "clean up." 
        # Newton-Schulz is an iterative method to approximate the matrix sign function,
        # effectively orthogonalizing the matrix (making columns/rows independent).
        # This prepares the "direction" to be structurally sound before applying it.
        # --------------------------------------------------------------------------
        [cite_start]O2 = Newton_Schulz(M2, steps=T)                # Normalize Slow Memory to get clean direction O2 [cite: 2962]


        # ==========================================================================
        # LONG COMMENT (The Fast/Inner Loop):
        # This loop represents the "Higher-Frequency Level" or the standard training 
        # [cite_start]loop[cite: 2959]. It runs `f` times for every 1 iteration of the slow loop.
        # This ensures the model still adapts quickly to immediate feedback while 
        # the slow loop holds the "long-term plan" constant.
        # ==========================================================================
        for t in range(k*f + 1, (k+1)*f):
            
            [cite_start]g_t = gradient(Objective_L, Theta)         # Compute current gradient (immediate context) [cite: 2971]

            # ----------------------------------------------------------------------
            # LONG COMMENT (Fast Memory & Variance):
            # [cite_start]This is essentially the standard Adam/Momentum logic[cite: 4033]. 
            # M1 (First Momentum) captures the short-term trend (exponential moving average).
            # V (Second Momentum) captures the "energy" or variance to scale the learning rate.
            # ----------------------------------------------------------------------
            [cite_start]M1 = M1 + betas[0] * g_t                   # Update Fast Momentum (Short-term memory) [cite: 2972]
            [cite_start]V  = V  + betas[1] * (g_t ** 2)            # Update Variance (Adaptive Learning Rate scaling) [cite: 2972]

            [cite_start]O1 = Newton_Schulz(M1, steps=T)            # Normalize Fast Momentum to get clean direction O1 [cite: 2972]

            # ----------------------------------------------------------------------
            # LONG COMMENT (The Combined Update):
            # This is the "Fusion" step. We don't just follow the fast direction (O1).
            # We add a fraction (alpha) of the slow, long-term direction (O2).
            # This acts like a "guide rail," keeping the optimization on the path 
            # dictated by the long-term trends, while O1 handles the immediate terrain.
            # The denominator is standard Adam-style normalization.
            # ----------------------------------------------------------------------
            [cite_start]direction = O1 + alpha * O2                # Fuse Fast (O1) and Slow (O2) directions [cite: 2972]
            [cite_start]step_size = eta / sqrt(V + epsilon)        # Calculate adaptive step size (Adam-style) [cite: 2972]
            
            [cite_start]Theta = Theta - step_size * direction      # Apply update to weights [cite: 2972]

        k += 1 # Move to next chunk

```python
def Multi_Scale_Momentum_Muon_M3(Theta_0, Objective_L, eta, T, betas, alpha, epsilon, f):
    """
    DESCRIPTION:
    -------------------------------------------------------------------------
    This function implements the M3 optimizer, which applies the Continuum Memory 
    System (CMS) logic to optimization. 
    
    Standard optimizers (like Adam) effectively have a "short-term memory" because 
    gradients decay exponentially. M3 fixes this by creating two "lanes" of memory:
    1. A "Fast Lane" (First Momentum) that updates every step (standard behavior).
    2. A "Slow Lane" (Slow Memory) that aggregates gradients over a long "chunk" 
       (frequency f) before updating.
    
    The final weight update is a weighted combination of both the fast (short-term) 
    and slow (long-term) directions, normalized by Newton-Schulz iteration to 
    [cite_start]ensure the updates are chemically "pure" (orthogonalized)[cite: 2960, 2982].
    -------------------------------------------------------------------------
    """

    # Initialization
    # We initialize the "Fast" momentum (M1), "Slow" momentum (M2), and Variance (V) to zero.
    M1, M2, V = 0, 0, 0  
    Theta = Theta_0

    # ==============================================================================
    # LONG COMMENT (The Slow/Outer Loop):
    # [cite_start]This loop represents the "Lower-Frequency Level" of the CMS[cite: 2958].
    # Instead of reacting to every single bump in the loss landscape, this level 
    # waits for a full "chunk" of steps (defined by frequency `f`) to complete. 
    # It acts as the "Long-Term Memory" of the optimizer. By summing gradients over 
    # a long period, it captures the global direction of the optimization, ignoring 
    # temporary noise.
    # ==============================================================================
    k = 0
    while True: # Lower-frequency iteration loop
        
        # --------------------------------------------------------------------------
        # LONG COMMENT (Slow Memory Update):
        # [cite_start]Here we perform the "Associative Memory" update for the slow level[cite: 2958].
        # We aggregate ALL gradients from the previous chunk. This summation is the 
        # "context" that this memory level is compressing. 
        # Note: In the image/formula, the sum range is roughly the last `f` steps.
        # --------------------------------------------------------------------------
        sum_gradients = sum(gradients_from_last_chunk) # Aggregating context (gradients)
        
        [cite_start]M2 = M2 + betas[2] * sum_gradients             # Update Slow Memory with long-term context [cite: 2961]

        # --------------------------------------------------------------------------
        # LONG COMMENT (Newton-Schulz Normalization):
        # [cite_start]This step comes from the Muon optimizer[cite: 2588, 2590]. 
        # We treat the momentum matrix M2 as a mapping we want to "clean up." 
        # Newton-Schulz is an iterative method to approximate the matrix sign function,
        # effectively orthogonalizing the matrix (making columns/rows independent).
        # This prepares the "direction" to be structurally sound before applying it.
        # --------------------------------------------------------------------------
        [cite_start]O2 = Newton_Schulz(M2, steps=T)                # Normalize Slow Memory to get clean direction O2 [cite: 2962]


        # ==========================================================================
        # LONG COMMENT (The Fast/Inner Loop):
        # This loop represents the "Higher-Frequency Level" or the standard training 
        # [cite_start]loop[cite: 2959]. It runs `f` times for every 1 iteration of the slow loop.
        # This ensures the model still adapts quickly to immediate feedback while 
        # the slow loop holds the "long-term plan" constant.
        # ==========================================================================
        for t in range(k*f + 1, (k+1)*f):
            
            [cite_start]g_t = gradient(Objective_L, Theta)         # Compute current gradient (immediate context) [cite: 2971]

            # ----------------------------------------------------------------------
            # LONG COMMENT (Fast Memory & Variance):
            # [cite_start]This is essentially the standard Adam/Momentum logic[cite: 4033]. 
            # M1 (First Momentum) captures the short-term trend (exponential moving average).
            # V (Second Momentum) captures the "energy" or variance to scale the learning rate.
            # ----------------------------------------------------------------------
            [cite_start]M1 = M1 + betas[0] * g_t                   # Update Fast Momentum (Short-term memory) [cite: 2972]
            [cite_start]V  = V  + betas[1] * (g_t ** 2)            # Update Variance (Adaptive Learning Rate scaling) [cite: 2972]

            [cite_start]O1 = Newton_Schulz(M1, steps=T)            # Normalize Fast Momentum to get clean direction O1 [cite: 2972]

            # ----------------------------------------------------------------------
            # LONG COMMENT (The Combined Update):
            # This is the "Fusion" step. We don't just follow the fast direction (O1).
            # We add a fraction (alpha) of the slow, long-term direction (O2).
            # This acts like a "guide rail," keeping the optimization on the path 
            # dictated by the long-term trends, while O1 handles the immediate terrain.
            # The denominator is standard Adam-style normalization.
            # ----------------------------------------------------------------------
            [cite_start]direction = O1 + alpha * O2                # Fuse Fast (O1) and Slow (O2) directions [cite: 2972]
            [cite_start]step_size = eta / sqrt(V + epsilon)        # Calculate adaptive step size (Adam-style) [cite: 2972]
            
            [cite_start]Theta = Theta - step_size * direction      # Apply update to weights [cite: 2972]

        k += 1 # Move to next chunk
```


# print("Hello")

```python
def Multi_Scale_Momentum_Muon_M3(Theta_0, Objective_L, eta, T, betas, alpha, epsilon, f):
    """
    DESCRIPTION:
    -------------------------------------------------------------------------
    This function implements the M3 optimizer, which applies the Continuum Memory 
    System (CMS) logic to optimization. 
    
    Standard optimizers (like Adam) effectively have a "short-term memory" because 
    gradients decay exponentially. M3 fixes this by creating two "lanes" of memory:
    1. A "Fast Lane" (First Momentum) that updates every step (standard behavior).
    2. A "Slow Lane" (Slow Memory) that aggregates gradients over a long "chunk" 
       (frequency f) before updating.
    
    The final weight update is a weighted combination of both the fast (short-term) 
    and slow (long-term) directions, normalized by Newton-Schulz iteration to 
    [cite_start]ensure the updates are chemically "pure" (orthogonalized)[cite: 2960, 2982].
    -------------------------------------------------------------------------
    """

    # Initialization
    # We initialize the "Fast" momentum (M1), "Slow" momentum (M2), and Variance (V) to zero.
    M1, M2, V = 0, 0, 0  
    Theta = Theta_0

    # ==============================================================================
    # LONG COMMENT (The Slow/Outer Loop):
    # [cite_start]This loop represents the "Lower-Frequency Level" of the CMS[cite: 2958].
    # Instead of reacting to every single bump in the loss landscape, this level 
    # waits for a full "chunk" of steps (defined by frequency `f`) to complete. 
    # It acts as the "Long-Term Memory" of the optimizer. By summing gradients over 
    # a long period, it captures the global direction of the optimization, ignoring 
    # temporary noise.
    # ==============================================================================
    k = 0
    while True: # Lower-frequency iteration loop
        
        # --------------------------------------------------------------------------
        # LONG COMMENT (Slow Memory Update):
        # [cite_start]Here we perform the "Associative Memory" update for the slow level[cite: 2958].
        # We aggregate ALL gradients from the previous chunk. This summation is the 
        # "context" that this memory level is compressing. 
        # Note: In the image/formula, the sum range is roughly the last `f` steps.
        # --------------------------------------------------------------------------
        sum_gradients = sum(gradients_from_last_chunk) # Aggregating context (gradients)
        
        [cite_start]M2 = M2 + betas[2] * sum_gradients             # Update Slow Memory with long-term context [cite: 2961]

        # --------------------------------------------------------------------------
        # LONG COMMENT (Newton-Schulz Normalization):
        # [cite_start]This step comes from the Muon optimizer[cite: 2588, 2590]. 
        # We treat the momentum matrix M2 as a mapping we want to "clean up." 
        # Newton-Schulz is an iterative method to approximate the matrix sign function,
        # effectively orthogonalizing the matrix (making columns/rows independent).
        # This prepares the "direction" to be structurally sound before applying it.
        # --------------------------------------------------------------------------
        [cite_start]O2 = Newton_Schulz(M2, steps=T)                # Normalize Slow Memory to get clean direction O2 [cite: 2962]


        # ==========================================================================
        # LONG COMMENT (The Fast/Inner Loop):
        # This loop represents the "Higher-Frequency Level" or the standard training 
        # [cite_start]loop[cite: 2959]. It runs `f` times for every 1 iteration of the slow loop.
        # This ensures the model still adapts quickly to immediate feedback while 
        # the slow loop holds the "long-term plan" constant.
        # ==========================================================================
        for t in range(k*f + 1, (k+1)*f):
            
            [cite_start]g_t = gradient(Objective_L, Theta)         # Compute current gradient (immediate context) [cite: 2971]

            # ----------------------------------------------------------------------
            # LONG COMMENT (Fast Memory & Variance):
            # [cite_start]This is essentially the standard Adam/Momentum logic[cite: 4033]. 
            # M1 (First Momentum) captures the short-term trend (exponential moving average).
            # V (Second Momentum) captures the "energy" or variance to scale the learning rate.
            # ----------------------------------------------------------------------
            [cite_start]M1 = M1 + betas[0] * g_t                   # Update Fast Momentum (Short-term memory) [cite: 2972]
            [cite_start]V  = V  + betas[1] * (g_t ** 2)            # Update Variance (Adaptive Learning Rate scaling) [cite: 2972]

            [cite_start]O1 = Newton_Schulz(M1, steps=T)            # Normalize Fast Momentum to get clean direction O1 [cite: 2972]

            # ----------------------------------------------------------------------
            # LONG COMMENT (The Combined Update):
            # This is the "Fusion" step. We don't just follow the fast direction (O1).
            # We add a fraction (alpha) of the slow, long-term direction (O2).
            # This acts like a "guide rail," keeping the optimization on the path 
            # dictated by the long-term trends, while O1 handles the immediate terrain.
            # The denominator is standard Adam-style normalization.
            # ----------------------------------------------------------------------
            [cite_start]direction = O1 + alpha * O2                # Fuse Fast (O1) and Slow (O2) directions [cite: 2972]
            [cite_start]step_size = eta / sqrt(V + epsilon)        # Calculate adaptive step size (Adam-style) [cite: 2972]
            
            [cite_start]Theta = Theta - step_size * direction      # Apply update to weights [cite: 2972]

        k += 1 # Move to next chunk
```


# Code Block

```python
def Multi_Scale_Momentum_Muon_M3(Theta_0, Objective_L, eta, T, betas, alpha, epsilon, f):
    """
    DESCRIPTION:
    -------------------------------------------------------------------------
    This function implements the M3 optimizer, which applies the Continuum Memory 
    System (CMS) logic to optimization. 
    
    Standard optimizers (like Adam) effectively have a "short-term memory" because 
    gradients decay exponentially. M3 fixes this by creating two "lanes" of memory:
    1. A "Fast Lane" (First Momentum) that updates every step (standard behavior).
    2. A "Slow Lane" (Slow Memory) that aggregates gradients over a long "chunk" 
       (frequency f) before updating.
    
    The final weight update is a weighted combination of both the fast (short-term) 
    and slow (long-term) directions, normalized by Newton-Schulz iteration to 
    [cite_start]ensure the updates are chemically "pure" (orthogonalized)[cite: 2960, 2982].
    -------------------------------------------------------------------------
    """

    # Initialization
    # We initialize the "Fast" momentum (M1), "Slow" momentum (M2), and Variance (V) to zero.
    M1, M2, V = 0, 0, 0  
    Theta = Theta_0

    # ==============================================================================
    # LONG COMMENT (The Slow/Outer Loop):
    # [cite_start]This loop represents the "Lower-Frequency Level" of the CMS[cite: 2958].
    # Instead of reacting to every single bump in the loss landscape, this level 
    # waits for a full "chunk" of steps (defined by frequency `f`) to complete. 
    # It acts as the "Long-Term Memory" of the optimizer. By summing gradients over 
    # a long period, it captures the global direction of the optimization, ignoring 
    # temporary noise.
    # ==============================================================================
    k = 0
    while True: # Lower-frequency iteration loop
        
        # --------------------------------------------------------------------------
        # LONG COMMENT (Slow Memory Update):
        # [cite_start]Here we perform the "Associative Memory" update for the slow level[cite: 2958].
        # We aggregate ALL gradients from the previous chunk. This summation is the 
        # "context" that this memory level is compressing. 
        # Note: In the image/formula, the sum range is roughly the last `f` steps.
        # --------------------------------------------------------------------------
        sum_gradients = sum(gradients_from_last_chunk) # Aggregating context (gradients)
        
        [cite_start]M2 = M2 + betas[2] * sum_gradients             # Update Slow Memory with long-term context [cite: 2961]

        # --------------------------------------------------------------------------
        # LONG COMMENT (Newton-Schulz Normalization):
        # [cite_start]This step comes from the Muon optimizer[cite: 2588, 2590]. 
        # We treat the momentum matrix M2 as a mapping we want to "clean up." 
        # Newton-Schulz is an iterative method to approximate the matrix sign function,
        # effectively orthogonalizing the matrix (making columns/rows independent).
        # This prepares the "direction" to be structurally sound before applying it.
        # --------------------------------------------------------------------------
        [cite_start]O2 = Newton_Schulz(M2, steps=T)                # Normalize Slow Memory to get clean direction O2 [cite: 2962]


        # ==========================================================================
        # LONG COMMENT (The Fast/Inner Loop):
        # This loop represents the "Higher-Frequency Level" or the standard training 
        # [cite_start]loop[cite: 2959]. It runs `f` times for every 1 iteration of the slow loop.
        # This ensures the model still adapts quickly to immediate feedback while 
        # the slow loop holds the "long-term plan" constant.
        # ==========================================================================
        for t in range(k*f + 1, (k+1)*f):
            
            [cite_start]g_t = gradient(Objective_L, Theta)         # Compute current gradient (immediate context) [cite: 2971]

            # ----------------------------------------------------------------------
            # LONG COMMENT (Fast Memory & Variance):
            # [cite_start]This is essentially the standard Adam/Momentum logic[cite: 4033]. 
            # M1 (First Momentum) captures the short-term trend (exponential moving average).
            # V (Second Momentum) captures the "energy" or variance to scale the learning rate.
            # ----------------------------------------------------------------------
            [cite_start]M1 = M1 + betas[0] * g_t                   # Update Fast Momentum (Short-term memory) [cite: 2972]
            [cite_start]V  = V  + betas[1] * (g_t ** 2)            # Update Variance (Adaptive Learning Rate scaling) [cite: 2972]

            [cite_start]O1 = Newton_Schulz(M1, steps=T)            # Normalize Fast Momentum to get clean direction O1 [cite: 2972]

            # ----------------------------------------------------------------------
            # LONG COMMENT (The Combined Update):
            # This is the "Fusion" step. We don't just follow the fast direction (O1).
            # We add a fraction (alpha) of the slow, long-term direction (O2).
            # This acts like a "guide rail," keeping the optimization on the path 
            # dictated by the long-term trends, while O1 handles the immediate terrain.
            # The denominator is standard Adam-style normalization.
            # ----------------------------------------------------------------------
            [cite_start]direction = O1 + alpha * O2                # Fuse Fast (O1) and Slow (O2) directions [cite: 2972]
            [cite_start]step_size = eta / sqrt(V + epsilon)        # Calculate adaptive step size (Adam-style) [cite: 2972]
            
            [cite_start]Theta = Theta - step_size * direction      # Apply update to weights [cite: 2972]

        k += 1 # Move to next chunk
```

# Excalidraw Data

## Text Elements
Titans is the base architecture that only have 2 layers. 
+ memorize "surprise/high entropy" event more than regular/routine one. The intuition is, rather 
than remembering everything, Titans only memorize noticeable event. 
- limited to First-Order Thinking.  ^ge4zfCWj

HOPE = Titan + CMS

CMS is the improved version of original MLP with multiple MLP + Attention layer nested together, each layers have a different update rate. ^PNQvSGQx

Conclusion: Does this solve Catastrophic Forgetting
 ^AIcWUyDr

Nested Learning (NL) ^YSAE9nLH

Core Philosophy ^6kbOqBIm

Multi-level Optimization Problem ^zYbEyGiJ

Context Flow Compression ^6gJZczB0

Unified Learning Diagram ^HIfw80w2

 RNN is a unified learning network from associate memory
perspective ^HpWBmNvt

Neurophysiology
Motivation ^dpriwnIt

Neuroplasticity ^obn50QDT

Multi-Time Scale Update (Brainwaves) ^jIuFE23k

Uniform and Reusable Structure ^tV43BXbX

Memory Consolidation 
(Online / Offline) ^SHZZZxbh

Hope Architecture ^OVYQ43af

Self-Modifying Titans ^k1464VEK

Continuum Memory Integration ^WhosjhS9

Parallelizable Training ^L8LXVHOl

Long-Context Reasoning ^tSc78HkD

Key Contribution ^HVZuLzot

Expressive Optimizer ^WNPQNLzn

Self-Modifying Learning Modules ^oLQJvhAy

Continuum Memory System (CMS) ^cfh7GiEG

Integrate CMS into existing model
(High Application / Prioritize) ^Cjfuwetk

HOPE Architecture Feedforward Workflow

+-----------------------------------------------------------------------+
|                       INPUT TOKEN (x_t) at time t                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                   STEP 1: SELF-MODIFYING TITANS MODULE                |
|           (Replaces Standard Attention / Sequence Mixer)              |
+-----------------------------------------------------------------------+
|                                                                       |
|  [A] Adaptive Projections (Self-Referential Generation)               |
|      The model uses previous memory states to generate its own        |
|      parameters for the current step (Keys, Values, Rates).           |
|                                                                       |
|      k_t = M_k(x_t)      (Adaptive Key)                               |
|      v_t = M_v(x_t)      (Adaptive Value)                             |
|      η_t = M_η(x_t)      (Adaptive Learning Rate)                     |
|      α_t = M_α(x_t)      (Adaptive Decay/Retention)                   |
|      q_t = x_t * W_q     (Query is typically a standard projection)   |
|                                                                       |
|  [B] Memory Update (Inner Loop Optimization)                          |
|      The memory matrix (M) updates itself using the generated         |
|      parameters and a gradient-based rule (e.g., Delta Rule).         |
|                                                                       |
|      M_new = M_old - [Update based on k_t, v_t, η_t, α_t]             |
|                                                                       |
|  [C] Memory Retrieval (Forward Pass)                                  |
|      The output (o_t) is retrieved from the updated memory using      |
|      the query.                                                       |
|                                                                       |
|      o_t = M_memory(q_t)                                              |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   | o_t (Intermediate Output)
                                   v
+-----------------------------------------------------------------------+
|                  STEP 2: CONTINUUM MEMORY SYSTEM (CMS)                |
|           (Replaces Standard Static Feed-Forward/MLP Block)           |
+-----------------------------------------------------------------------+
|                                                                       |
|   The output passes through a chain of MLPs. Unlike static MLPs,      |
|   these update their weights at different "frequencies" (chunk sizes).|
|                                                                       |
|                                                                       |
|   +--------------------------+                                        |
|   |  CMS Block 1 (High Freq) | <--- Updates every small chunk         |
|   |  Input: o_t              |      (Fast adaption)                   |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block 2 (Mid Freq)  | <--- Updates every medium chunk        |
|   |  Input: Output of B1     |                                        |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|              .....                                                    |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block K (Low Freq)  | <--- Updates rarely / Long-term        |
|   |  Input: Output of B(k-1) |      (Persistent knowledge)            |
|   +--------------------------+                                        |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        FINAL OUTPUT (y_t)                             |
+-----------------------------------------------------------------------+
```

### Explanation of Components

**1. Self-Modifying Titans (The "Head"):**
Unlike a standard Transformer where projections (Keys/Values) are fixed linear layers ($x \cdot W$), HOPE uses "Self-Modifying" memories. The model generates its own parameters ($k_t, v_t$) and optimization hyperparameters ($\eta_t, \alpha_t$) based on the input and the previous state of its parameter-generating memories. This allows the model to modify its own learning dynamics on the fly.

**2. Continuum Memory System (The "Body"):**
Instead of a static Feed-Forward Network (FFN/MLP) found in standard Transformers, HOPE uses a CMS.
*   **Structure:** It is a nested chain of MLPs: $y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$.
*   **Function:** Each MLP in this chain updates its weights at a different frequency ($f$). High-frequency layers update often (learning immediate context), while low-frequency layers update rarely (preserving long-term knowledge), preventing catastrophic forgetting. ^ctbse1L0

Define Multi-Scale Frequencies ^Crmgih2R

Check Clock t % C == 0? ^YlFiujdY

Update MLP Parameters Consolidate Memory ^GzD7i61g

Skip Update Maintain History ^xqYdYshQ

System State Updated ^t91MvjOu

Yes ^As1wS6KW

No ^U0OmfGr8

Define Outer Optimization Loop Compressing Gradients ^kEQt4VNU

Input: Gradients / Surprise Signal ^zhIuyHLo

Choose Memory Management for Gradients ^oVQs85F8

Momentum Hebbian Memory of Gradients ^SI1COjeJ

Adam / AdaGrad L2 Regression on Gradients ^Kfsm4Mh1

Muon / M3 Orthogonal Mapping of Gradients ^ihNFMEC2

Delta Gradient Descent Update depends on Weights ^x2qgoy49

Update Weights ^VbVaYdbC

Compress History - EMA ^FIFYFWeK

Normalize Variance - L2 Reg ^ESsY1OxV

Orthogonalize - Newton-Schulz ^pcyRvreP

Context-Aware Decay ^nUnHa2EP

Define Inner Optimization Loop Processing Tokens ^hXzYPV3N

Is the system Self-Referential? ^JcBo7hjx

Standard RNN / Attention Fixed Learning Rules ^hMtYuR7B

Self-Modifying Titans Model generates own η, α, and V ^TG9YG85f

Compute Forward Pass ^qwK9G46u

No ^6u51c6LT

Yes ^qHeE1PwC

Dual Form Update ^Rkoh8Dyy

Define Associative Memory Objective M* = argmin L over M of K, V ^bUSKjQdq

Choose Objective Function ^GLNUX6kV

Hebbian Update / Linear Attention M_new = M + v * k^T ^Xed2YRh6

Delta Rule / DeltaNet M_new = M with I - ηkk^T + ηvk^T ^iQ0RrWyO

Resulting Learning Logic ^hFM8vAcH

Dot-Product Similarity L = - ^b7GFHbjZ

L2 Regression Error L = ||Mk - v||^2 ^vIyCQvkt

Start: Design Neural Learning Module ^b2F9RUmB

Final HOPE Model Self-Referential + Multi-Scale Memory ^6XhFoh9L


Phase 4: Continuum Memory System - CMS ^PMTmC65H

Phase 2: Architecture - Inner Loop ^iqh7IJTk

Phase 3: Optimization - Outer Loop ^FP2k2nSl

Phase 1: The Fundamental Atom - Learning Rule ^eS1xeANh


```python
def Multi_Scale_Momentum_Muon_M3(Theta_0, Objective_L, eta, T, betas, alpha, epsilon, f):
    """
    DESCRIPTION:
    -------------------------------------------------------------------------
    This function implements the M3 optimizer, which applies the Continuum Memory 
    System (CMS) logic to optimization. 
    
    Standard optimizers (like Adam) effectively have a "short-term memory" because 
    gradients decay exponentially. M3 fixes this by creating two "lanes" of memory:
    1. A "Fast Lane" (First Momentum) that updates every step (standard behavior).
    2. A "Slow Lane" (Slow Memory) that aggregates gradients over a long "chunk" 
       (frequency f) before updating.
    
    The final weight update is a weighted combination of both the fast (short-term) 
    and slow (long-term) directions, normalized by Newton-Schulz iteration to 
    [cite_start]ensure the updates are chemically "pure" (orthogonalized)[cite: 2960, 2982].
    -------------------------------------------------------------------------
    """

    # Initialization
    # We initialize the "Fast" momentum (M1), "Slow" momentum (M2), and Variance (V) to zero.
    M1, M2, V = 0, 0, 0  
    Theta = Theta_0

    # ==============================================================================
    # LONG COMMENT (The Slow/Outer Loop):
    # [cite_start]This loop represents the "Lower-Frequency Level" of the CMS[cite: 2958].
    # Instead of reacting to every single bump in the loss landscape, this level 
    # waits for a full "chunk" of steps (defined by frequency `f`) to complete. 
    # It acts as the "Long-Term Memory" of the optimizer. By summing gradients over 
    # a long period, it captures the global direction of the optimization, ignoring 
    # temporary noise.
    # ==============================================================================
    k = 0
    while True: # Lower-frequency iteration loop
        
        # --------------------------------------------------------------------------
        # LONG COMMENT (Slow Memory Update):
        # [cite_start]Here we perform the "Associative Memory" update for the slow level[cite: 2958].
        # We aggregate ALL gradients from the previous chunk. This summation is the 
        # "context" that this memory level is compressing. 
        # Note: In the image/formula, the sum range is roughly the last `f` steps.
        # --------------------------------------------------------------------------
        sum_gradients = sum(gradients_from_last_chunk) # Aggregating context (gradients)
        
        [cite_start]M2 = M2 + betas[2] * sum_gradients             # Update Slow Memory with long-term context [cite: 2961]

        # --------------------------------------------------------------------------
        # LONG COMMENT (Newton-Schulz Normalization):
        # [cite_start]This step comes from the Muon optimizer[cite: 2588, 2590]. 
        # We treat the momentum matrix M2 as a mapping we want to "clean up." 
        # Newton-Schulz is an iterative method to approximate the matrix sign function,
        # effectively orthogonalizing the matrix (making columns/rows independent).
        # This prepares the "direction" to be structurally sound before applying it.
        # --------------------------------------------------------------------------
        [cite_start]O2 = Newton_Schulz(M2, steps=T)                # Normalize Slow Memory to get clean direction O2 [cite: 2962]


        # ==========================================================================
        # LONG COMMENT (The Fast/Inner Loop):
        # This loop represents the "Higher-Frequency Level" or the standard training 
        # [cite_start]loop[cite: 2959]. It runs `f` times for every 1 iteration of the slow loop.
        # This ensures the model still adapts quickly to immediate feedback while 
        # the slow loop holds the "long-term plan" constant.
        # ==========================================================================
        for t in range(k*f + 1, (k+1)*f):
            
            [cite_start]g_t = gradient(Objective_L, Theta)         # Compute current gradient (immediate context) [cite: 2971]

            # ----------------------------------------------------------------------
            # LONG COMMENT (Fast Memory & Variance):
            # [cite_start]This is essentially the standard Adam/Momentum logic[cite: 4033]. 
            # M1 (First Momentum) captures the short-term trend (exponential moving average).
            # V (Second Momentum) captures the "energy" or variance to scale the learning rate.
            # ----------------------------------------------------------------------
            [cite_start]M1 = M1 + betas[0] * g_t                   # Update Fast Momentum (Short-term memory) [cite: 2972]
            [cite_start]V  = V  + betas[1] * (g_t ** 2)            # Update Variance (Adaptive Learning Rate scaling) [cite: 2972]

            [cite_start]O1 = Newton_Schulz(M1, steps=T)            # Normalize Fast Momentum to get clean direction O1 [cite: 2972]

            # ----------------------------------------------------------------------
            # LONG COMMENT (The Combined Update):
            # This is the "Fusion" step. We don't just follow the fast direction (O1).
            # We add a fraction (alpha) of the slow, long-term direction (O2).
            # This acts like a "guide rail," keeping the optimization on the path 
            # dictated by the long-term trends, while O1 handles the immediate terrain.
            # The denominator is standard Adam-style normalization.
            # ----------------------------------------------------------------------
            [cite_start]direction = O1 + alpha * O2                # Fuse Fast (O1) and Slow (O2) directions [cite: 2972]
            [cite_start]step_size = eta / sqrt(V + epsilon)        # Calculate adaptive step size (Adam-style) [cite: 2972]
            
            [cite_start]Theta = Theta - step_size * direction      # Apply update to weights [cite: 2972]

        k += 1 # Move to next chunk
```

 ^v8kk69Fi

M_t: model at t timestep
p(T) distribute of any random variable ^ZYEDa0km

L1 (LASSO) and L2 (Ridge) regularization are techniques adding penalty terms to a model's loss function to prevent overfitting by shrinking coefficients, but they differ in how they penalize: L1 uses absolute values, forcing some weights to exactly zero (feature selection/sparsity), while L2 uses squared values, shrinking all weights towards zero but keeping them non-zero (smoother shrinkage, handling multicollinearity). L1 creates simpler, sparse models; L2 creates more stable, complex models with evenly distributed weights

multicollinearity - 2 feature highly correlated, 2 neuron learn the same thing.  ^jVH9eZyX

## Embedded Files
07c397817d2d4bec7cc511dce5b811a6825de140: $$y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$$

bb3399ca9760b7590722699b403515f7cf7a6611: [[Pasted image 20260107144114.png]]

58cfe8ead52ecde8f4ce51e393faef298b6a7a1b: [[Pasted Image 20260110180129_992.png]]

4d7dee62f6ec906199fe7fafb3cfcf6dea696f1b: [[Pasted Image 20260110181704_838.png]]

afd289b35667e0e17dce59715e25d12d776501a9: [[Pasted Image 20260110181802_009.png]]

0262edc012448a1ab479c38006cd7cecf21e7ac3: [[Pasted Image 20260110182043_514.png]]

b145df64c80cdd91491c8d07f86d48944eb56b67: [[Pasted Image 20260110182143_442.png]]

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tAAYaOiCEfQQOKGZuAG1wMFAwMogSbghlBAAWIwAzAGEAdQArdLLIWEQqqCwoTvLMbmd4gFYUgDZtcdqAZnn4+Z4U

gA5annGp/nKYUfieKfiEnnmAdnGt8aWeNfHdyAoSdW5xxJOU855ElL/ExJTBZrR5SBCEZTSbjxP6g6zKYLcFKg5hQUhsADWCCabHwbFIVQAxPEECSSUNIJpcNgMcp0UIOMQcXiCRI0dZmHBcIFchSIA1CPh8ABlWCIiSCDx81HorEtF6Sbi1FFozEIUUwcXoSWVUH0yEccL5NDxUFsLnYNT7E2w4qQOnCOAASWIxtQBQAuqCGuRsi7uBwhELQYRG

VgqrgAOJ8+mMw3MN2B4N2iBhBDEbg8WofWprKaJEEpxgsdhcNBTNaFroMJisTgAOU4YmhAPmKXmtXiaz4KcIzAAIpl+hm0A0CGFQZphIyAKLBbK5N2e0FCODEXDD6HnKbne6JFZLfOgvE09PcMf4Ccp/qYQYSAAqag5qD7qHUCFQVLCqG52EkagQbAoBED91A3VBOHwGBUEkXBGF4VB8FwGBa20VAAB0OAAalQbJ9HxQgjA/dDUxEOBSD7BAFH/S

FUByVU4BgEi6MYXJcPxUDYI4VBAmUINuQUekoFDBBMM4BA0PvSQP1DYC1FLF9mGoHiN2k0gMNyLieKyLJNCYUNlBYpgYHUAzlMfKIOGYCCOCg3CsgIojUA4NhhLEXBNGCIzcm0TDnEQwh9AA4g3zYVAADFCBYKBnAAeVIYgmFQKTQwxAy0JjSh7wGKoLOfV930/UIP1/f9+iAkC31gqAbLs2D4J4RDkNQjScLwxziNI0hyMo6iIUkOjcnRRjmIQV

iavwwIqusbS+KQ0hBOEYTDRsiTkukl9ciEeTOEU5TyHfdTMLA7jAjwvSKI4QyxuM0yrvMp8rNq6D2oopyXLckJPI/G6fI0/yiCC4dQoiqLUTihKkpSjg0qujLvU4KBhUI8RUHiHYUwaRHwtwIKoO4KtyhvKAAEEiGUMt0GCBpBlBYs3IIMmIUp6BzT5PRclwETSH9NAk3wM0KP8AhstvXLHusgqNq/ErRDKwDgKmsCasg6D6o/RqkJQlg0MwtqHL

ezrmDIiiwj62j6OGpiIG8iaOOm06EDmgShJE1bJI22TtuE3a+321SkuOrSzt0/SrqM0gTP/e7kol577MmlHnNc8wvq836oF1lwAqB9MQci6KIcS9Todh5R4ZTXAhCgNgACVwhR89xwQY8RIACXBSE7zR7QtlBWDmFFqAABlUqby8W5TIgYYDIN8GKABfXZSnKSoJAABXrABFehhUjLeRlBHpUegHLQRGNAxkmGY5kWZYeBhJYUgeFNrVQMYUl+U4

O0meZ7hSQ4poUzPGIK8csUwb5TBWOMZY8ROz5gxtWaS/Vu5rGRJXK6Wp0HVhlGqZk+IiRklJEgSc1JaSxiZLiAhbJyBWS5DyWmmNBQijFCfHUGYVSygQPKUBio0DKhTLgrEGotSplxLqFM+pJDxjdEA6s5pqRWmhLaasDpVwuiXHaJ4+BJAAH0WgAE0ABazBJCxVqHYGcAApSMzg276HmAAVQgHaL0mNfQIF5s5OeIYwwX3QLgNuMZpzEBkbPZMO

CEBnhNHuKYkwAHYPKMWOslNEi1BftWZJpZGwcGbCaG44xzjnF+LuEMA4hzRNQBeK81YpwMmIHOHSi5ChuOrKudcm4TTbl3O8A86NEjHjYKeEcVTm5HxyhINusV14zlQAAXljpZVAOEmgAFlhSYUwms4UikqoyX0ORNgjAQpZN2mwBoEEhahgIKgVZw916oGeOoXCQZhI+A/Hch5OESYyHoqWTCWskrxmBjXGoh1lIhD/E1bW1l1Y/lQI4BoDQmD0

VQO0jcH4DoSUyhQIeVQpkzPmYsmaKz1mbI4Ns3ZhVAqHOOagU53FzmXIhNc/Atz7mPLUANfQrzCDvPZV81APz+i5AUoC9SwK86goQOCui1IBrithXBEqCLCBIpRWxdF/QVL9G0HyLGuRkZEWhIg8oBqoA4zxm/Qm3QBhMwplUamjDMlMAZvge1LMa5wHZojLmhoeYjP5oLFlHARYTPQAS2ZCy8rcVJRsjgWz1lUs9gc9EdKGUQQuQRYWbLPmcueT

y/AbyvJ5u+b80Vu1xXOXCCCtgYK1IQvldC2sMFlXwsRcihhaK1wYp1diuE1c64N2NaOMZU926dyhCaXuGTygDyHqPGeo6J6tyXd4oUi9l69hGRANgW9zSEAABr1niFYtoiRIwtAAI7eBpo4tgaQj7wBPoFaIJCUz+LGIsFI2hswLB4A/eYkxuygjfs4Vssw/hrALPMHc5xsymqeAqTMnZ+6Tu7kkOEmDUaJIEKqLE+DWToEJH8Ujj6UxUhpGoxkh

G+i0M5Nyei+rmEiJPrBP8IFpT4e4chk0nC1SsaqOw4JfhpFGmhGaC0SibS4YgBQsJfMfGCKiSM1YUwsxAggYhmsJZODcCWDanTKScl5LRgBjsbYH4CLaT2zpaNul7j6UeXs5Tgh2eqZPVR9JnSukKFoiAFAdH6OMaY8xlibF2Icc41xk4QmNIXHkFpq6MThIFlPIZWIRkee9B4rxQaUzzoGIulLy6almsFJ4ndXxsDzESLueI5xiA8GILUPS2Bzj

YGwDA+IxAxDjE0GseI8RcAVi2IlOB5HqzYCEKiAw/YNy4G4CvcoSEbxVBgLomqCzPkAD1gAAAoGi6IxAASgXvtjC6FiCuWsrtg7R34hnf22wTbJ3LvXbyKgE7LiuhL0Ee4VGRQuhgDkV0eIMXex+IjE6LjG4ZtVEQIyAy7Nhqpc3cUZbFQd1TAAEJbzaJgfszAnSWFwCYngABpWr4VVn6Bx3yY+VRX01D5J+iY0xZgLFuHVqYKQziGbA4COIxxtw

fAa3V2o6TQQgLAagCsMwfhQKG1mOrExrNzvQ/puBM64EVjWEB2r2n4RYP4wRqhRHoD0foUx0hVGKG0ZoRya3vJvQsdYVUdjGhAhca4Tw2XoO8NcMExKcRHDJHCANOJvjKYFGWlgMo2T8mo/rrS5Eyp6N4PqYBKUostZSz6dqLJhlJnUbi67B8RY6vIBavTw53pZx+llMHG5yp2WUxqJ80uVp5Q6mznnPRLvyXUuDOGePMrkAfS40q8PgroQF1j1K

558rwQvEQE0JoRYAI8A85SJoS4JSAP5kSJoQvQGJgNA6xfkbxx4jSgB354HAeQcQ6m6jxTETV5Q4kLgKxsPgJuggER0cCuh+zAD+zKExzXnQBJidGwBaEcRgH7AJCfV6DZDPg/VGEKTiE/mmB+AawSSrwgDA0OGOG/kuBWESAfn3EIJlz4VQHeE+G+F+H+EBGBDQxQSVFk2Nxw1N2xHN0IWIXJFt3IRCQd3QHZDoUYxdyYSFGD21FDx9zVD9zoMI

KEXVHdxDylD1AjzEwTAkxjyk3jxk1BA7w0SS3cSnzyyU2rFDESn8QgFwApxEzjGT3yzTxGUOG+ASSKUMwZQJigTpjzwbCbFL23DWG3BgSOCbwqSyzHVqTi372aTQGXBTBrw8Lr33Ab2c2rBPEyzHyX1tTFgkBxFyV8BSTQH7DYHCCqlfElHgiaAW1wTgH/GwAinxDBWWmUEwhxTxWKKbDKNLAqKqOslMmsjqI/AaKiCaJaLaNIA6IMm6IRkNUbhN

G03NUtUFGtXGVvA9UdQQBpj5HpnMEZnJk9TZlBA5iiG5isI/0gGzVZV6PQBKOwAGM4CGOqNGNQHGNQEmNCAYhmPCnaJlU6MWMrkHXrlYBHVGRXXHUNA7g4OnT7ln0HiKwX2hPHwgGnhKxT3RwgO3SqCEEjEkHoEjgaC4BQJPkCCAm4NZ1GB+ABFmCWB8OfguGWEILfgrHGF7iOFZL5yWCA201oP0w7G0C000xWHRjgW2HYK7m4H3G0EWEVKVMVNz

CwwRB4MEW4zEIgEJAQHbFgT5EoxEPqW1IkIYwYWY1kI0PkK0M1N9141QFUO4zkLEVtOrCkQUzRkk0USMMdNk1MN82SO7wn1y0DWsM/zsIjGHmcNCWT2W26GfX0ztHAPKDTA8IARKWOAgUCN00piOEIOLxCOhGzEuFqAiMIL7GbxlVbziJ7wSKaUS2SK0XjITNQPEPQOB0gCgIgAMWFBJhnESA4GHiCS0RTLxM7KxyqEjFxH7ESFIB4CEApCJkTO/

1IHRCoFHMeBKC0S7J3S3mwH0HrBgFIEPRSy3NbJPm5HXNALKDHO3InO7NqCEFqHoEcRaEPRh3POgBXICTXLYA3OBzvJbMnIkE0BJkkGIEkB4HXicK/MZ1XOvNHJf3KDSK3B3DzFWBuHRkMyxJnxyIyxrJhKQTn1RLXQ81xPvNXh3V7P7MHOHIZx/NPjFnPjpLSTiCSA2DmGgx+GmHmFA24HOCSAVP3HbDCILD5OlwdIA1k2QVlLQCROrBpLQFkzU

O1N1P1KWENLIWo0oRZDoydykOdWXxYU1DYQUN4OUKVF4JdOE20NE09ID13UMLfkLxMO8zMKDJy0sLDNuIqC/wCWHgADUYzPS3DUyVM3gNhBtKw8wcyUlMwYE4rskiyTQCwhtuw+cewbDXNqzYiiK6z6l4sB9zCbMOla90Led9dLh0YR88jF9tju4IB6wa085h4QhSAOADJUB9t6xh5vs9Qspw0mqWqQo2ruROrw4eq+r9VEYjVUZVgliLVcZNiCY

GrdiJAxBcgmBDjXVjj3VTiqggpiBiBEQLjfVrid1CTiTSTySY8rlQ18BHjhrURWr2qJrDIpr+qwSa4ISVi3xSAhACjMSJ0ESe4FK50SLbxit8ih93955byt0bCd07AGh5hhRSB8AjAGK2y5MFYaSWLL4sxBtRSYMmSVhP5wj+KZNtBBsgQ6s+TlhtgsryghS0BK9RStNagoEH5jh0ltNZKp1UB5TlSRaOxDMlLUAVKtT+CJB1L+Tb9hCdK1LNAeA

GgeB19LSTLRFbK7SlCHSnSg9rTXSJF3SdCHLvS48XL/T3LAz3Rgz+RQy8KIzwxv9YoQq4z/N4LUB5hkyUQIr+EVdRdYrc9cy3gCygiOAS9uAgRxhtgFhxhDNKyYiYaKN6yEtNFgdgKvamKjKkaqgpgMRNBYor0ccnR9AbywCtzgLHznzXz3zPydzvycarz/yK6gLG7uy2AnQr024SYKcjEpglyLyIw/yALfsq6O6d1QhSAKd6wnRcQh6m7LzR626

J6Hyd1D0DADF8ADErEsa4LGKW6x7bzkLq9bNyrdxjhfh8zmbIBcK4barCKMTCsoa0TyKEaMd8SJAC6i6S6y7saT5iZaTCbDcaa4koNClDgPhtM342TtAYN0ZYNoM0F+dJLeETVZ1IABbu5wbIAJapauE1K9T5atK7dRCZbxCrdDLNabLzLda5R9brKjadbTb7Lk9HLY9pM/S3LHQPK7avK/QfLU9nb7DcBYpgq7KXC9CH7lNKlNgyzzhP5FGkq9N

yw+KQ7jMUq0Yor2cYRtMk6W88qMTe8GlEjGz+HUjz70iKqYRBLY6Bl0tR96rrwhqcQpp15/w8RBBmj9gBrcVXH7YPHBQ2BvHJBfHMZZq/qFqIncgNj8Y0BDNiZ1r0BNr+hkCQ63VkmIAjqTr30ptzr/VV8Ua0aMb967qQ0w0iinjAnPGQnzQwm+Qq4frh1UY0RAbV0EB4S5KwbMGpBIaR437ay760T+YKLICd0nyXy3yPyAGR7ryCb34jhCkwGYE

ybVgCxzgqbUBzglhtBik2wLgKxxKzg0H/d8wEgIE0EyNSNNgZTBaE7ahf0Kb4M1STd6G+C9LZbiGDTFb7cKHLcDKLTXcrTTKhM6GcFuNLL+EmHQXNCTbygPT2GLauHXL28bbB8LDBGnauz/KHD153bpGU8/b082w+d7gYEi8I7oQfgVHI6tHVhFGsClgKycr3Mhm1807irPLLGyrrHL7bGJhedYaiXHG6r0Sga4A2BZIM6uggdgdcMygUgtFgywA

5WugNhZh9dasAQdWdWbVFXlWty1WygNWE7N9dXdX9WwBnAHmnmNnahDWtFjWQdzn0YKxrmbnb6ygbWNXC97XlXT7UwohSAoAcdbDkc0B4yMAzHV8rqSSYAySlzsm2BEoqh8RNA1Ak2BRMB0x14pXeQmzOzPh1nEGgNMjmCrWf1sxuL7hBLNha2htzgA3x6UwchiAw2kcQDI3/NMgEsinNBUb0bMak38JU2JB03M2tz+RCAc3iA83ZIH9gdnAf0+d

P5S369kHwiq9FXf0CxKCG363IGGtm2P6IXuRSZR7pJcAhHQQ22SZL2Qgp6V7b38ApwKBKk2mgbs30xhQnZ07sWg3z2nRmBhREBLQCAAO23gPQPAIrB8AAOX6BmyLm4xmv70BwoOBYoMRVlYoKBwnqxs6qTLJ1TgH34OL5gEg2x7HOwUhcx2SDhkguaAFBsec8wFgdnTm6CVg1hf0oGt2YQ6Pn47nu5hbRalTVSMESPlLeCiGNKFaKNtK/nPnKHAW

bcZCtazK3TUzIXGH3naGtPIBEXCWOHnLOCeH1FbaUjqxJ8sWZGbDcXcBa4CW3Qo2vafaW33DlE5gjh1hphaXoQ0FaWo6bRyCGsub9HWWn6gaTGiqkj3RmzG7s6gGvzuyjADFNAZwYBIxCBf9NyEv1603u7e7+7B6D7m6V6kKuh7bUKukbHP4E7JhhWwq76CKjGgbEPobF9UO86JA0uMusucvZm0DmKMDL4khJh4GsxphCln4sxb6iDMxe5pg6Ojm

UHYNAROPMwgRhO3guDsMkQZP/m5afmFOyGTT/mzTndc7p2QXtbwXtP7T0HoW9PmH7vDOzakWDCfSrbzPO8SqzVHa7ORGIxa4JHw96lQrwyBB/b6DARY6khbmNH895LDggutHNhtWVhEfsqqy2X8rKROW4urOUKrG0L+X6v/5H62uGqqhVleVnBghGA2VYo4BhIgojANx/kOB150Rvpy6/Gnq6ei1CAGebpmfWfApCJOfdoee7B5wZrlioTonrPsZ

lr4nUBEm7UDqNr6JtqczMntf0AcnTqUxLi/UmBV8MOsOcO8O+R7iHrBf6fGeghUAWe2epefZuJZe+fGnwSWnuBP2OmunBaThcG+mUTX7kP8fga11RnT3KLdzCue6+6B6hvfz5nRvFmJtUhDx7gaO6Otm4FzgFT9dEHVu+TBSHT2cc+khFcqO0kOOCtNcTRVhe5twdxmDrn5v8HDvlOdTvnNLfnyG+/LvqHgWNOwWDOg3HvZcDaBNXup+jPZFkXfT

UWvNeHLP7abPp8gecXIzv9hRnOAO0zoQDmy2ilKXQ6ukHGXVczguzMlgkhMj5uDHcqU74jCqzGMXSqMU+W8wYREgDXRyvfRFb4UnG4rUEJK2laLsygzrBVmACVbA4VWzreDPA0mBM0LWGzc8ogKq5GsdyqAwAc/CzwWtKaO5MYK3x4Dt9ikHrPnI62BzOtq++pSgoCHr5ll1GnZcgT+koEQJqBHrHgCezAD21UQ57DtsAWUBLYe2MbZGgOxKbDsp

2o7E+BO1zoT4Z2ubfNt3AYGpAS2UCMthQSgzYDd2NbSBoe0ErHskBvtVtoyFEERtUAUbXtvREt6YdsOuHfDtWAUFptSAGbZQdO1nbzsC28XDgSu20GLB68zBD4AYOrb7tjBdwI9k23MEedtO57e9uuSvY3tLBxAZIf+VSFzNW6L7N9h+wBpftVBxAX9soH/a79AOIbaDmBzg6QdGQ1Q2DhBwqEddBmE8brlRSqANBYoTQQKvQCmDKBFsFJKoER3x

qZ8xge7EvpsC7D58Ng83N+AyW3DLBP4ApLmjfxZoOl2aYpLmhKV5rSkm+oNUTmJ0rzi19u0nd5rJxIZD9zuI/KhkC3U76d4WgePWk90dIws7ui/D7sZxX4/c0WG/b/gD28oAdbCLtAJPeCP7dtgcS9TMBYM87yVn4hSa+Opn87yVtwaPXJKjE7BYF0kfnFzLjyi6xZP+DZGVuOUhFJcOykI7sv0KsRGILAOONIHl0zqT0IwzAGenPQXpldl6iFQC

oGxq72Y6uGwOmk1yh6YlWu7/CGhHyQ7Yl36ldT+j13QBUiaRRgOkWnxzqkdxhcwVIMBkAEq4dwFYQvosEm7FJtwDNIDI32rCs1eA23fYd0zD499zhR3AfvJ1qSKdh+1CFTpITuHWc3csLG0o8On7PDZ+bwzTn6KX76F5EpnfhNbT+H/cQygIiocCNEb3gwerDKRomGFEn82aZZH4G2G0x+E2aQ2NEaZgFLfAwiEXPEdT1TqEjyhFjH/nZgaw2N5G

EwNYS13AFt4COATLareAih4gKAPxAwORCND54BeHY4mN2P/J9jU0g4vTItTmqZhZM6xNXlsRcY7FDeEAVJnrwyZ7UsmxvPJuUDN4XVOh3Q3of0MGHlMc0T1EoqOPCg9iJxA4hMEOO+pDpISrTQoUH2b49N+4/TTrhANhLYk4+MokkYn2/wsjZ689eDkMIQq5CxhVmFdrnzmACcNghfMsiX0PBINjmsGTbiaAWCikyy4XTAbHR27Tp4RXYdvmKTiS

S5XmGpCFoQwdFydSGxpGjBd1uFqcvRt3YMWHmokBiVCQYyfiGM+HL8vultMzr8Is7/DYxtnUAcD2/zOJJGsZQls11TAw8KwzLemsiN4BmikkEde/g1mKSCtmW0RQxmKIJ5ViuWNYknryzJ7/91gXNRrr+IA65F8RKYKAUTydY7l4BOAsoMgPwEnBuwFwSvCQObEGskBeAzsoJRppnAdmHYAKeeTGCaiYE4RMiRAjmAOtgprkotthKBCZ4j8urAiW

QM+Dw8EpiU5KQIKEHBtQ24bLtrYMkENl+2g7UpiOxTaKDPBk7fzN+znbqCYBZQYtmux0GhD9BbkwwVELrYxDTBcQqrjCPKBttrBlUuwVIMPE9C+hAwhqWO3QBKCs2xQvwRoLIFBCepIQ8tv8CfwIDBpI0uBCdLMHjSEheGJIQ+2vZ1CMhN0p9hn2rBBB8hIyQPkwlnalDqxCk4QVUJA41CmhkkyAFB3+mND4OzQr8a0LCDtCgJ6AYUBQDaDxAKcV

6JoFQAgnoARh+3BZuMP1yUd4RaSBCX/C2ZUFJu63I4Mgz5xdhMJ3tEUlsO5qSk+ahEoWhRyOEqkThUnSWr3zdH986JVwxiTcNU7SFWJE/OFhxIe5cSrKL3H0cbTFnvc2GXwwSSiyjGiSYxDtOMUDL8r78AkmgcEVVNJE/l3O8faHiSwAw3BBKOeW/vFUzGbMkewRdEdSzuCM0L+Bkt/s4w/594iRnUrOoxWS5MjJkToBoBQDQQUAeAq9fLhSJ3T1

hagkgWuOl3IiL1s6R9MOYyIK4SBN6+gbervTKYTlE5FXbkbgJ5a/9LJV9AATuCFG+UHJFY4ihKO/HSiUy4zfFAHKDkpAQ5Ko32dWDZwN89mdWM4OpgQzbh6O8lDUTgV0Fx0jm83C0fmSZm2jThnM+0X32O6D9TuDE3StzNH6ejjKDw2Wf6IYYvC5+wiBfnxPlkCTwx33YSevxVnctrOgPDWQmIjCaBkxCLEJJD18oZjtGQIZjukl8JUs2aglQsaX

lGyAI5uLsvHsY0J7mNieZ9CybV35YfBP4Zc0Vo5PbFVMIAjiTqgKFerjUuq/YKwHSFxg9EhqaCtVIQEwUdVsFuC30AryRhRN5xqvK1KtWXGkxVx649JrfwN7MxDqJAXJj6k5gHiJA8MxGcjNRl297qlTRqkQowWjU3q5C6IJQoHTNNnxAfV8bCU6bvjQ+vTFoVHwxIgD/x9ctDhAHTmZy96KopOdjJgk19OSMwweWjGQl/xUJ5fXudTLgTJBfgyu

d4JgMMzYNoQQlAVoAKKmEE7RnEs3AvMdH0SlaTEwWddwFBsTeJ28tQlC1eFSz3hR8yPArNPlCTIxv3PhpArVkSSFJd87/NgF1k/SYeCPSBjAmx6aSr+3tbMrbLpb2yYkAGXMCEJZblijJHLEyUT2q6k8YF//OBYCGbEx8/xwoyue0uckQK0p8rbAXQNlb4DHmhA7YKSzIyLBplqU+gXMrQFECllpGFZTuSGzJBfF2wMiXMBmWwC9l2YeBgAkODuK

SB55fZQkC+Djd/FJUlUCIIqniCIRz0uaeOxkFDts5bgxqR4K8HrTfBHUwto/i0G7TdBPFdYBEL3YnSTBjbAQWOQwBWD3lEgyEfYNyCr4BFSMlGWjP8zuDx2zU7wW1M2mdTrWO06BntL0Frs4VRg4aQe2RWvKQ2mQigNkIqF3sHpOQglV8telKL2mH0n9n+1Mk/SypDQ8DuDI1kgyYOkqhDpDK0UIAYZIFdADjgpweNmAJMegIuXRm41qSWMsYRMF

jqajYMT8GKvmDmFziuS7rOrGhJQbLBqZmwzmvTN2H801FAGVIJ/COBxJlg9wKBDbMUqzyCGeCWiZcOXnhKBZHoliZvMPlxKdOe8niaLJEypKT55QThqv2Vl/cr5AIvJcKIKUBJt5SeQlq5wNkTTjZHhPPoy2fiX8rZZmRyoWQaW8AOwuYS5i/0i5VyCqHs6sca2rqRzo5sczQPHI5E8rk5XQb2TjXbkRz8UcAFoDjkPL0BBglXTySuB6V8jYFhwO

4OwJWwjMRloot2eKPnyKrlV3ZNuDOrnX1gF1bc8kZADZxzBi+0lNsMUjuDTBMMr8TMD8ASB+rpgaSHcGf0dWvqkE74y4JRIO7zzuZi8p0T3hdHXDwNDQNYA0ESBjgaGsaxQrvMDFJL2Jya3QqmruIRjuGIkrNWZPEk79b5DnYgI/Llmpjj+pSysB8GgzvBw61Sppf/OhDvBLm7HROu2vaUxcv+qs3kfWPXUAZ9cVPdpUAwkCoBa49YesLslwBop0

FJCkKMECwVXRMIhoKABQHxAYgqk6IfQD+ATBDIrA2qV6ExA4CIAWAYHYSIwAIUoKJNUmmTXJuIV5wlNZC8OGpo02kAtNPoAwHpsEDgcjNBsEzWZs5AKxCAVmmcTQsWpxMlxyCphRwp15bVWFVS9hQ6gkA7ieFVxQpjujVUaqtVOqs8Q8SGq2bpNr4WTQyEc2KbpFrmmVO5s806afNBm3tMZswhBaLNoW3cXgz96KK0A70nIiDW6bqLPxNcqGUDR0

Vzxj1famOXHMS3D1IJvK4YAcCBAnBthFedYJWHzBbrIAb8b1bu3bC9Ix50GamcUl45ktVgHrDRe+JXYx0zghzZYPuDgXsy3mQSj5uBtCV8zV5FudedGpUExKk1FlXTk9q3lYbzaisjNVks34CMSN+Shzu1rkzPzXC6YmHqsB5o7gvg38pjQ1hY1oB6sRfTsJxraX7rjJXa0yTkv40OYS5QmwgqNorl7qfx1YcZcSNVZuTVlBc9ZaFMY4wg7gp265

pgx3bLcrgiwRYbVlqwwg1gLyzUm8s7YfK9ZXymqTulxVCK5t5QIlatJJUgq1BC7cFWDkhXUroVgUo6ZEIRVnSxpnkstaivbborPlk075aqvVWSBNV2q5aU1OBVTsyVYKgIUuypXrt9pElAaQboPZG7mV4u1ldys5WMg2VHK9PlBL5X/kChgqr0Z9JFVxcxVQHUGXKtD3EAJVtQiGUNqPXx8G5EgWuGsHXiF57wtcenLqsxkkczFZZa1aTQazk0YM

WzTkhzWzCUCVhFqx1bTOdU7CpSbqg4SzNZli0QNZwp7RcJO7Oizu/M8DSrTVoa1x+gOv7Qmow2xKgdn3dJUrLB1iTclkOvNQ51uopi5JLnT2qWsumKTa8WwDvgjzUnfBMdNioDLgQLBtr8dtOztaY09ma6E+HQiQNOXwCzl5yeWnOYfTzmXTP9M29siN1TnoBiAPUCgBwCdCLrAKa9Kdd/RJjMBY62AQ9IegTlAGuRIB3tVUCMRNBwomgKxKQGFC

/5h1s20dYBK/3oB1QHANoEYniC1wmg2B8rrgaNmgGVVEATACTBgBCAt4GIHHOFDYOcjW6S6wQSuugVrq+lEwSnnZIqGjKCd4fQ9VKJQ5579F0BiiLAfgNXqID82kBl/DzDxIG2eBLZoo2L53wGNJoyvi8PRjnbQatkwNRzODXBKXtvM8NUp1g3wbENp44WQvveYJL956haWSwyfnHywxaavDWv3KABkt92/G4sIz34giHCHACjbDoh7w7X5SkpYO

8HWAwg1JAIW/UNhLKK4oiuI5OsoZ43v6iNEAUnTYxzA34RNyhsTegGaoiB6mMAOsHiGUAmbVkKcegNL330ItBqKC9o8NDCbdG60fRgY0MaoWzi4RkWxcQwpi1ZMWFO1ENluNXFpazqvCzLVUEL3F6Ugpe8vflod5DVxjnRqY70cwj9HLNcx+RU+L+o9bt1cJNRTOkG2qH2lVO+GgBIT7cGf9f+hciYufbQS4kxfYw7Ah2brNSB1YN+DsxOD7NRKD

ijbQFir6XALm7rGgZWCZlVs/4sdHQUqXUwAZh9c80faGvH1QbJ972/SlGqFkxrQjb3HeTxiX0A6UNdlFNZEdw1nzMlBG7JVvxvlQ6tZDhNgMUoR3p4YEdjJYfNzzE2Ka1yVRtcUl5xxJoqICpBa/ti4QLul0hgTbIa5qo8FDGspQy/sgD07OpcA5ncusmVg4MTbrK5h6xxO+78Tiy5UsSf4HxCrTZ7ENtNKl2zTZdBJIkvG0TbyDAVxK53a1I2lu

7NBq7HXX1NhW+74V/uhtudJN2n6ppFu6XVbv9MF6i9JesvY7qBUtTIRrujXe7q6DLttdXu7jgWC3b0qhpp05M8bsEGm7fpF7FIY+zunh6OzVBvITHrenKL49wqsoaKvTHirU9We6VfUPHOAyFJmitQ20I0Nyj+QQgOdS5EcS1AVRlek3h3IY55hKOUwjYITN6YuVdwNNLsO2BCGaZKCNBDYV3ogTbCeavepmYcKOESdnDj28WW4YtwQawlXh78zP

vVo6z597JwI/9s/MhHklha/iVyaco8n8NF8wjTkoSNpD7OwpquLrJLVtlDZfx8tcokdnYVyjls5Ht7T5y368CXwcBmWMqMmmOlROlySnOQPyjUD6BzA6IZHUMix1iXH2detoO7pNAHASYFvH7BgiJD2poub0pvxECAE5cpIyKNbHss5z+RcbWm34uCXhLeh67p3IAQKkoM2o/uUiLfVoBIi8DDYIoz+AN4y2TiuJNPN6aBLwLY+peRPpXlqU4NCG

pDcBcZNT94lYFp4QfM8spLsNMF9NT8IQv8mIdiR3xGhaEDpGi1aY7I+nn1zrAGClSyALKax7FHHlg2W4FRcMlVHwFW++o/y0bEIKwBYrNsUTAuMIAOjPgP4uYCUTDixjVV4aEhFRB1X484WpXrQtibLGEma1Zhbr2m06ZktLMHY6bwKYW8d0DQFc/oDXMbng054yq9VZatuR6rj436lCRePDM3joNAbciS+PKGfjyllA2gfGAYGsDuq0xdBLgb6l

LFR58wysF7i5G0kNhpxYXhpoS4UdXfVE14rhEzABR0GQvHwNJOuHnt3517Z4ddEfbmJ9J77SLN9FxqZ+3E5fb9vB6cno86+0HXyfB2Ysd9vlfNQ4XoBin4rqmPnKWKsxqS7gAaqpZo0bUZ4EpVwF5hUdys0Xqj3asS3WLJ1JBdcDqw0wpONPlXTT6ghnRabcmnLGdoUqtrmEinZhLWeujyZIetNlBFGv6KW/5NlsxS1MNNLmgDZoHumWdsy9KT+m

gyZ4zLZGE5mQM1v/XnrfAsXV6fKmS6MVMuvtjukON5nTjkI5XbulV0u7IzpZ6M8EN139TOyVbRM9EIbai6PTOFs3T6cdtZnnbnQ6a7NYLNhmizg59qX7e2mVnepmRaDIALmB1nDd4dwPXba7O3T09pdx6VHqt38rutA58rAnuHNJ7RzKe2VROYUkyqAZUq2cwqvnPQzFzvFzQNqoMSEB5gmAeYJubxoGqdzY3AsFyTZIPxDztHfXMeejra4uwFLS

YBZcKSd7HmdMnvYzOtGC0XzYnN8+UDsu+XQbRIcG05YjXT7VagF5Df5YRsSznubJp+6vrSVRG4LMR+0Oi1VnIWgRDnVwZRsP2x2wD2FlFW/JIlLNzVakrsGjppumZG2kuIELhLVMdrCdb+7teHKXOEHiDpB8g2xaoMcWaDYB1USlx3RtAnQQgcKDODOApZRLUh8SzIckvbBSLvN3dfJej6KWuu/d2GRACoc0O6H8wM8teG4v6Gb1DHSXDpfWB6XA

Q24S1Woy5L3AdJ2FY5r00nk3AmZThs+0Gq5lg2PDN9v80SFcu+HH7kF1DSyfQ1v2LHHJwK+ja/sZL4LsRv+9muI0RXIcaFmADFbh3yTxTIyWDGrnpoymf5cuQZQ2qQdRSfgTNdB9xvyt8bV1up1h7znm7832WrRiAEL2EjOBHw2QVAMKAByoBHE59TCPthxzkBQwFAZVMwC+rulRjjVLJyL1ycfgCnBAD8MU7KrdVynfqKp4wBqfzGItMTJavQt6

uMK1jA1jY8Nc4XHVtze48awGiqCD2hAw90e+PfmsFaUFjTnJ4FBaeFOOnvaMpxU44C9PwgtTs+51ueN12trqinax8b2ukVe7I2ndRuj4fcG8HJBsgxQbEfsGq7kjwmtdbgkzCgM91uIA3msMWXbD/uTsO9ZNt8DvrQGpbcUm7DXalS29yTh+YvsOXINlIaDVPqhuRLzHmGxfdY/AsBHWGaNr0iDpCsuPoxbj7fR49QspHcA/ykBy/NktQP1gu4X4

LMIpsAbqbCp0zKsA3UAgdwrS6iwLdotYPid7Ni+nqd5oyXmjNFs0x/pFvB2xbKAn9GknCJq29Wct9V/gM1eq2op6tsgWFLLKP6UXipQpPq/Sk+SPrpt0jObY4FmukX5mZUta8julSJdYgsB9G2zPoBXbxx/MyGZWle3wzxZ32/4P9tQq4zlbY6UmcgYR2LpRs6Oxmb9Px3QKQ9ke2PeTsq7w3ad8lR/spVZ2aVdwAELHW3b67Q7jK2IcXcSHB72z

Zdyc/dMbeV3Fd0bGu/9Tj312hz305u39NbsznhRHdsGfKpz2POjrdBjEPWHvDrwpgV6GcBPf1VV7DVBYGYPPemF3XDL2zdTGgNMs7Mx5+4HexzXvMuqnzh9kTgPtZmn28GejsDQY7DVGPIbRIAC3PvuEgWntQRxNfDY/s4bYLTjn+9UFce1GAH8Y3FpoD+AYXj9WFlszDwa61YGC8p1RvZkY2IPUYg2WOj8GraxO8rnSiZQxaXP0HGDzB1g5Qcj3

H0cLXBskRI94tQBAqCwHHIek0BYHGHhcjmzYxhBsPUnzz2S2k+4c92lLrz7snR4Y9Mfzr3zwBtep4MMc7gNNXS1cH0uKPtmGrdTBUsLwQvqZ0lbR3txcP6Or7hjqk85aO6mP3L779+8S6Rs2OiXqN+x5S4xvUvf7tLkD4Kd33CmIPKQHx5kb8fE2CYCdeDAnRAx1Lo6SH+pUWIv17axXzNiV6zeldMP2P/LTjyk8VcSuMnEi/ELpusAhR64M2DyM

EEwiigAaFUb3A1fEXoL0vP4RkBJqqvMBcvLTtpkV5h3moFjvALq8M5WqjPVj/VhLZM62NxajeXC2Z5AH3H7GJACAad7O/neLv1n5xlBWl9IAZfKv2Xmr99Hyf1fFYMOppk8Y2tXOY+Nz/rXc+rn7WaLh1oTzuiI9MGWDIJp6QYaz4ikbrefLd3CYEoPWwXz1jT8Air5vXjbXNB1+Zfheg0ikvcfcHMEwEAgHtVE+yxSccuGfb7+Luk1Eu9G2PQLr

J0lx+/CMUuTO39zNWFZxsMupJ6ACD9i4yNUaKhHL7YLAkPxwOLZ/Lu2Ug8lxiVVTTN12Szfid0vCrcriYAq8QUYPACQt800ztFtrKDbwOZW5Lm1fGvdXlphW6zpF+S3xfMtyX/gPvXA+FfJAm14/i+/2u4X55QH9mJB+g+k3qZz0/W/ts+vLdwM63RAEDcnHc3Yb1Oz2/TtRu9lJbwO/GeDvxuw7ibut8DLRUO3zffrjN1O5ndzuF3tvtaT7dBUZ

3AhLvjduW/zsJmGVDZ2t5HcgdlSK7nZkPeR75AvS+zAqooQ3b7evyxzg7ru8O6nMl+x3R3uuYjV4tWIr094BoLUECqEOK9k9ld9PbI5rv9zC9oFyvYSbyl4k15hxYZgtFOrT3+9vYYBv70KlB9N71I7p/vf6fH3MP4x7LVfdAWzPSPz9z5eZNkv0ftnzHwB+x/Y3r56soUykYg+hzZJnpTC6jAgfEtVMriw8x2ApuoY6l9/JkgsF+C1Kce4r9ljF

/otOLSAx4M+DAQyEMRDMjwcJgDTg3HVJPGj34dhQNuCMRkAzAE0BFQVj1rFZXZJ3bAufUq3VMsGAT14c/jfPThkkAlALQCNLNUSSARSUlno0dRBRy2YPgOex3AGCdvUAFNPJYG09gbPTy+YDPHF2pMXLHw1M9/DNHwvsv3ZGx/c7HYHXs9z5Gl0vlnPM/1c8L/PnE88SfDWTflKCQpDiQVTNSQMsiLWnwAUEeJExw8WfPDwKtEnTm0S8cA7n1E0h

qVZAC0+xKyFDwhjDSH2xYoWyDdgFAV3iRRp4BADOdDOep1p4HAkonYQXA0p3cDfA1AC8DYoHwJEh/A/kEiZOrJYxGcNePqz681xCZ315evFLX68ZnGHWG8JrKoDr8G/Jvxb8zjMRSCDJoaCBCDnAz3lcCIgzwO8CGgXwPiDNvdaxfFu3a52D4MMA7wPUHnb4x49J3EAP4NBDYQyu9fnaT3+c7vQF0e89gZ71BcnrdT35JIXOgmz5vvT6zNt/vG0S

+AaaMtltVlSMsm4DF/XgOX9+Aoz0jVzSL7Ru44bGWUsdxAqzxX0pAtfUccN9LG3iMXPPG3A92wIm3ZdSlBOjB8/gBOgpsVgMi1IxfgWrEi9mfaL1Z9ajdnxLl9TbTB+NkvdlmVcyzcWymVBffWzOUJbFW3l9opTEON9sQ2X1xDpbfEM7IGWXYPcVIpcTibMvJQ2xhcfvbXx3IKQ5e2zwRaMsltsTfGO398sVKAFXxrfYN0JVQzPN3t8VBSPyd8i2

GP29043P3U99BKQ32bM0zX3zN9MzC339cIAYoMb9m/L5w9thQu31JVI3LaWj8YzKszLc87StxDtE/RFRTNFQlN1bN0/cu0z8oA67wt9O3Tax8Fe3EcyL8W7TuzulM9Id18oeHcViGDEAiiGwBGAXRGcBD0DgEjA2gK9EkBhQKYE0AKcWdSXdiOQb0mDFmBDASBSaFYArBOwKm020AudsHgZ1Mb4GrZKwSU2Pc97R8wPsp/bpmPtRaOf3PtmTLF1/

Nn3Nf3vs33EQPM9kfElwvs9/OWQx9vhWQMc95ApCw+DZLfGwg85rcHjUDb/JMlP035Ew02BCBNSULxUPAVwAVLgHZhwIcrKEP/8YQntT9l0AcRgMQt4BYFwAGgIh3AMEDPAxPCIAcKHoBagOegQB6wZwHoAGgSCjWBMAVZCaB14AxCHJoySAKTkSHLg27Iccc4C3gmgBoEPRxgWnBnA24eYCaBCASgRJhAqeIGUBEgG8OdDxDRAxwdeLSMHvAZwD

rEIBHEXAEwB6AcYCwjD0YgHGAYATAHXh7AnCNAj8Igj14sDEWuBnBiAIwHiAccNYFWR7wYgCEBuhEmA4Ba4UgBxxMAaMBAjoAyj3wNQKcCkgpoKWCi4sfnCjwXgeRCwIqpMKXPlwCVsGnQlcgw6v1lFeLM8IvD5gK8MoDq9D1VgxJgGEFsZjgQvn1weOKBmF04kAqQ0cq+WEw1xQaGeQX9yTEJT4C18XFxpNZaEzz8MGTLf3At7g1H17DyXA/xHD

eTUKxP8c1XGynCvg8YB+CH/OUnhFuwPPnXCFgMiw3VqqIbFkxX+UBWi4jwmVz/51MFkgzxkQ6Pgyc24c0A/B72P8AAgGvazUaoWoxACFQ5YTqPW8BnJIKGcotFYwqsVxdIPWMsg9wG3EBvfIPmccVNuDDCIwqMJjC4whMKTCUw92zTVRFR6iGpeotqIGjyoIaMeN2gvPzfFbnMPmMj2WE72ID9FVGk0A8AYeAMRzgIwCaB8AKYDggpgdVTPQjEUR

wI5GKLcxh1O5aDEmEH4YpG1s+caxSbFkgHZhYD8wGKgU9qw7vVrDJ/XyIbCr3V83B9QNQKPcNTgkKIECjudf0JdHgvsMs84o6KKHDEoql1HCgPJzwnDFAz4Lc9pgKD31kYPJcNKVG2PzyuBcxUJwToQnO/i0Z0YH4HzIOwfcMqiCROi3w8gAxiwgAMQXXCb8ZwVSMAMJ1HKDAiFI9DmfDXw98M/Dvw38P/DAI4eGAi1IsQw0itInUzJ1dI7Cn0iW

xMqwUtCA4MNO8qgBWK5olYlWOXI1YiR0zDxhC4FmAtRMsj3B2A7d1LZLlDsF7lY6GBEoIOAxyh+teAWyzvc8Yh90pMzg2HxMchAyKNhtBw5k1iiBw0QIyNhw2mOSi5AxCwFMmYjKJZjzgbKNkYPCO7TzBABRm30DKYPuWKNZ7TsANxyorjVw9pY8wMtibGM4AYJCwuS3timooal/Z8ABoGcB+jRFBgAuqGNHyASvKoHHjJ46eLVRZ48OHnjho+al

a8xojrwmjYtHIIyDuvGaJOJ0g0a3yY9jQoIkBHo56Nej3oz6O+jfoxgwBjdoipn2iUFZeKniU2NeLniJYX3gUVLnToN29ug6EF6CCA8dwGDY+MbWdiJAJ8JfCnQN8I/CvwyQB/C/wgCKAjxg9t0/QH4DUSwp5cH9RQYYY/+FmBsxaBkjiuwFYNY1XI3CXzAmQ+sMFpVgR5lNl5HTATuAjgpOKX8U4wmPOC15aGwR8ftSQPJjJZB4JRsEo6QJeDMb

FKPeDy4yK2UC1gauNhE0YeRwmxY6EL1XtwnLSWFi7I+81+ATA6ELMCEnPuMvprYkq1eNhlanS4cMSVEONZVXeVnV8ugI7S+A/JSXAtYikKXzpCRfZICcSdmFxN1Y3Ei21o5uSNjWKQLWO4HsSupBOgSAaEzvkdcNtb1kYSgklhNCSFQj0EDZWzbkNVCA/BwTl1lo8wFWjow2MPjDEw5MNTCQ3J3VFCPQx3yNCIVE0OztaVGUOrck/eUO99U3P30y

TeQ1fBvjcAF6LeiPor6L6En4/6LD9vbCM3FDqk8s0906ks0IrcC7BN2aSU/FlTbMshbs2bcHQrP17N32fsyAS2pL6S9D2XYv19D09f0NL9Awx2JMjAJbg0IB14NoFpBIwKxGIB+wUNCMRD0FIDgBIIw9ApxiAfngk9hhNvwzDQY5ID/gphSGPdYSTEOJ8ScJLMFgwPIqONRNR/O83FI0YvvUxiZ/a9xxiR9SHyCiCYo0jTjOw2fQ38ewqmJzid/N

QmzjQxBx25Mj/TfX/tJw2RPsIIPbCOv8PadmLv9YPdPA750kew03DkPXMBC9tJRYFzsopPHT/9o+AAJljSHbgxaBJAEJjaAEwxlNNi+gdWLYjZYpc0jB14BAD/CMQQ9B2jAY9SOoNwIrLSgiYIuCIQikIlCLQiMIrCJYi5IzSKxC6jbSOMT6ovUQ4cLEkeOfozk9Q3uilzKVJlS5U6yNXdtwTUVkdA49xTn9YGMIjk84FRYAAwKEx1Td8MYhhITi

AozFPxiuEnFNX9iMCKNJjREmKJJTnSfOPJS7PCRIc96Y8cLLjc1ZmOUCSYBRPCp08ZYTsU/0NSSF1W4/zx2Z5DX/yi9DwgxLZ8HU//iSAr6HCkMj0nEcVDAhAIQF017AqoNQAnQLajwVPebqKqBLxUdPHTbkBwJnT+gOdIfEVeRXm3jkg9r1SCxnLrzSYevWaO2N5o9LXN4FnCQCuSbk5QDuSHkp5JeS3k84A+SvkkRTfiLxRGGXSJ0tdNnSDoLd

POcAE7byATfAkBMRINFD1Oj47ovRSXNII6CNgj4I/QEQjkI1CPOB0IzCPlTdUs2LVEcEx5jwT64qGKzBnIibiuA7tewwKlKE/JGoTM8GJL+AuaJmXOZyaO4C1ZFSb1XYSU05OOh9U4jNIBZ4fbNMETt/FHzzj4o/f3ETKU14KkSaUmRM8dlAnVOJ9QHUn1KVFGDKmZZBY2tUKRUTCJ1LwNM74EfVhUztNFTqouLywCTEoeKRCbA5Q2sTFbBAXcSQ

pTxNSAdmHxPiRYk2zOszHExzJ/gvrGKUYykdSsGVJvVcJJBxIknHVoTrmejLIEfMslhYzo0iBE5Crpb0zTdqpQPwgBQwvJIQBIwgpI2jik7aOGT83B30Lc0QkHClD6k2ZLlCuwFpPTM2k9N2ySmca5NuT7kx5LJwn095M+Tvk3UNDdw/UZPV0JQj3WKzpk+P3d9ZQmt1GkWk+0Mz927MPSdDLraPU2SLooVRKFE9cxmT0B3Q5Obdjkyv36CiAmDN

4ta4SMFIBEgNoBJgt4DgHiBZAeIGwAeAGGHoB/wJoGu5COP5JBjdzQFNmFxcQjKHjYGLdhppBKKFJrN7gMPnhTd7VGIZl0YrBnfFGw9kPRSyTDjM4SuM7hNxTM0hoGwBEgJHP4zbgiz2ETKY6zzETng8TMkSS4nH1P8K0iuOUDSPOcIUzMktzjZSSberkUYNMdcL/l3/LRKKRY6IpDBSO0g8MMzu0tEM1iIAYeDWBh4Q9ECopkcCQVThuO8JgCHw

oiJIjLQciMojqIxIFoj6IxiOYjZIjgzAILY5hyScTEnCh49Go91IgStsmv34c+cgXKFzYoEXKwzFU72M7lcwf2ODSekct1RNYGX4C8SLgOBRhTa+TTy0cL3BKnYzMXKHyJ900jsMzSM41HLCMxAvNMNoRM6mLEz/3CTPxzUo9xxQt8fNfBSB+wGtNwt8kJXCKQfEptN0TGc2m2WA/4ayQGzV4LuNMCe4wxM1zObBvDLJgBIdNHiUFdeG5ACAYICI

AOeFb3vAjnZHEXiN4FvKFAggKXk7zu8kAg6td00aJ6sD0zrymjMgzcVPSz489N2MMtK+IDc9sg7KOyTss7Iuyrsm7Ou57eCoL7zyAAfPbzavZKBHzxBM6P95a7EDL60Q+MBJUNNs470GCYE9AClzSI2XKoiaIuiIYimImHVzkXQn2NwzGSbCnzBCMohJIzSE8jPilKMtGGCzokpmWVtuXKOI9ZgNdFwh9/crFLTTQo00j4Sw8pk28shM3fwLToLC

lLjy8cscNLjwrZPOSN6UlICm8yctlxyiEmeeyuA2cmn0pgbgDRKFjabP4CLzL6PRK7TK8ntKMSMKJ1LMzdcizKVc+fFVwF81XIXyJCHErxI8zfEnVn8S5CrEPRDFChzOcTVfOrELClbTVySskgFAvGBAsuQyiSaMnX0MKVHWjK+BTCz10WSMk6rOxUcklaPSy1owpM2iSknVMgBPbTrIjcxkilW6lYzaUNKzhs8rIWT0hJwqSyasgvTXzDs47NOy

4Ac7MuyMQa7MIBbs3LIqSSzHrImS+s3OxmSE/es2tDaQlszT9xssvxbdlkpt1wj23HP1mzr8/P09Cm7b0JWzR3I5OnMTk2SxuiFzL1N4tlAHHEAFVkWoCvQKcNYAQBwoFoESBh4JoGwAYANYCpx081v2Xd/kp7PBjXs0FPey5xCYAeVAQ++AXsYCsf0RTgc5FKPssYk+0hyQbNsLe0XLRHORzMMqKKxzc0wgtJTiCiI1ILgrOmLiMpMonLpTFnFI

AgCGC5lMty2aKnIJgMqa8zYLUrfmJBCC80zGUliTHQKZ9JYysSELuch8KRh2sNYDbgMQJYtFzbw/VJ5zOI7iN4j+IwSOEjRI8SMkjpI61LVzbUwkPtS+4tBAFSIiPly2tzE3jwbz9cqv09Tts/h0xLdwHErxKQSgkuxkEeCjmrUAbB3MAEncucQuVvVc2V+zeYzTxSswQPyKTSMXVsIDz2wmDW/Ms0jyyJSCC/sKILo8guJpiZA4uIoKCctKLx8a

C/4pkigS7z1+D08KgiuBoMdhybj9MfPKbjtJaYC+B92PQLLzn9fRLRKSdbSLQR62VxVo49coGgydh4TgGUBnAS8QGAqvUIE4Ae8yRECCJAeMqugkyxGBTL64NMveot4ucT3T1eTXkmjD46aLnzT4w+PPi5nS+KvT0AAYqGKRisYomKpimYrmKFi+YGFLX4haxQUcyxMuTKuxQssEBiyy/K60u3J522t9va6MgztFZ/L6L+HYkp4i+IgSKEiRIpoD

EiJIqSIdKRS2opwy1cYAvwSwC4jJ/RSM9yPITg6c0Sr44Cywp9yUeE4GWBoTQk0rwaqNAtxjock4KwKiYi4Ku48Cry3jVjS14tNLC0w/3jyrSxPPpdqCzWWUCgkJlKdKmC2AuAwhsU6TUlekW/QhC8Cb9AELOc0Mpqi0KZkr/gIiJ1zMT7JLkolZpCtENsSugeWw8StC7xObVXE/QoQFAs9zJ0KWK88gfhnyvyR5JxOdGDML7y1YW4qhsSjlfKDg

wSocKg9U3xsFnCvkNcK0sjLPWiikraNKShQjrJGSAi7rPGSupPrIrYwippIiLk3KO0qyVQ+StXwWy+CLbLxiyYumLZi+YsWKsig0MCKi3Cs1qTS3AotLy6Kj33CKbQ1JKXDyi1twz9gqns1bZX2XP0aLXcAvz2TFk9bI6KK/bPR5Leivku4MwKCCigoYKTBJwzwTFZihMG9HyKLCsdXZiRNDmCmTIqkMOww1EtMJF22EKwCYHm444tCp454Yg3Dh

5BKay0/KMUjAtTTYcoPN1L04ty0zjrg7OKNKKY4TKJTwKpKOccoK6RN+KZM2goboD9RgprjT+BOh4F2wblI4LdlH0q0YVgRhPdK8KsBS5ywykQrqi8E8QqgTXU/AN59oBGQuDtXMmXwcTLDRUgBAG8DYAotHq4X2erUU7VnerC8VET2V0qPZlNVOC8E3sMhKwHI74BRJBgaq7lYGtaqwayBjiQ4syoVkqZpGIpcKAza6gTZhjJXT1D/CgtyjNnfD

ytd8Gkq0ID1Ii56WVC5KzGoUql43JPDD3CzLNUrvC5yrV0qkilXcqA7OMwqqd2IbKaTmlUbKCrqi2Cq5VQq9ZPCq3Qnbx2TFsuK32SfQ9orWzOijbMj4J3F/NTBBi4eEcQhQfcs9jKSB7JwzcwA5VJo29GE0L4vgbAn1wy3FExRjx/JFOfNzipsMuKeA4jGvsV/YPJ1ISYg0qeKI8l4vzSwKkgqLTccktO+K6XUD1I0WYk2OWrgS/WsXC7QmHgMw

4MXXDgdAy6Eu4KkHa2ufhKCQiyDKRU46tDKCI/h33JDyY8lPJaSvCPvDVYuAOUF+HNuECojEIQGHgjAVyEJKHw7kEcQ2geUBfCK6jSKQMlzQ9CmBIwDCP3JCbVXMrqJc4AOwAKAWuAoAmIuACc5x682LtS4Q2vl8luPK6s5LLE9rgXKlVDWvrrG65utbrdVSdT+cswz+BWZ/gSBjMMQ4vRl7gZbRZUPcnFQGvoScGDUvQKtSzAr6rsC4z1Dyfasm

MEyQKgOsmqg6iCvILS0ygtx9YK6cJSBh4PWtZcsjZ0o8JWChuJ0d062tTKjb9VxWjT9JZEpuqxU3uOryOPZSVhK8AnnwycKcBAGqDEYCiE0Bq4ADICD/GFBUobqGoaEIA6G+dLHzSyifJSCKyg+JZhqythWyCRrRfLGtGy1fGYAtanWvwB4Gr2w/ShqFhscC0QdhvobpxNayvzpyy6LnKIMg3KfzN6oYJLqjyE8hfiyHabJu9nAJZghMfVNZmeZ7

rRExEoyq9CSssTgGqoBAztQgjji/4P622A6NMiQsM/cz+t6rA8n+v/Kx+Tf19riU/2qjyQG94uDqyC0OuA9GY+asZdaC1ZAzyz9EZC/84EbCrgcQcozC3DhSb4B0kCwI6qqiTqwiokshsM1VkxzMshrGVqKmxNkK7E+Qs0KTWI21erCBM21Yr6KuzPVZ2m81mczzLViq8aaaHxooSxSCwzMLSCVxtsLvKsoBGa/VXxomavgVGvSTEszFUt842G6n

ZqI/HSqCL9KoO3lZfKoyv8rTdMytpqNm9UMkbpi6RvgbfCgmq0qiaqP16zSa3mriSq3CmtrYhaqmpN81kibKqL2VFZMPKNk2PSaKFsxuyWz+3PkJVqEq1bO7tdG85P+NuyDuq7rCAHuoutQTDvwsai+E8rY5CZGGOBq6aPxTYDHKC0XMKQs+01IwDTV+qRB765+E2AaBWjmjiuqqHJ6rOM4Jr/LeEgl3/qc0v2qAbomiJqmqi4maogbrSpPMAcWY

/FkQr5a5ComB4MHOvpaqfIeK0yAuAZSSBG4vOoMyC6qVy6VjM2qKqaRdGpokK6myzIabrM9ySErqMqGOuZqWo5qm5vORltb1VmsqWiLLm5LOubta3Wp2auszmqLdgi00IMqiiwuyxEKsmmoxq3W2IvQBHECnGYBD0VA37ATG+5s0q8ssUL2a3KyZNLdmCPmo+biikaSzBha66Qlr/mtZOBapayKs0b5s3ZJaKFatorT1laxKo1keivu2XLuDaetn

r56xep+SwqrFqsxi+fDMW0l7F/1vquwHCXLcoEQ91Ja7yq1qxMyMW1tBydrW3Kx4D3EWkC93zD+tUptSm4oiU+MnloEzni/lvn5A62JrAaEmhmPLT0ov4tAoUgTtpjqkK1aptBecTe3eAEHYiyzBemFVtSpJTUbDTqKgcvJDKdWrUz1bi5A1vyNbY4eJuqrMp6sVYvqhQqVslC5xJoFEMIKQ0KUBeDp8TEOu5UXaswZduVJuwS1osLrW2dq9YQcL

DrYEbgXDr1sjfaXy5D1mp20jbNam5q9aykwsxcq02wrP9apkwNsGzGkkwXzafmn33N0qsumokar0aCMjAr0WoAQqNK8pNY7fWwrO5qY3b3WzbLQ3NtrY+OkytT9C20WpCrtO7turty290NlqIWmVpkr4q+trhbhRJtr3qW27smjbY2+NpMaoRCQGBiqAx/XWLF7ZpVlKQuOIAPBS+W2o+8XhI4ofMTix2t+qLigJo3av6jlp4S9Su4pRzd2tHKET

X7THIAbRMnHPiavixJvPbbSuCtoLdstmJFL7/e9qUTsOmOhxFPS1YjUyCm/hExEiab0s1aOc7Vs1MGdHnJRbu6+sF7q266uqtza6yVPrB14LeF6ojALgAwDzJIhoS8pLSnWNaDI7es+NH8xFpICIAFoH67Bu5urxqnO0UtXctgINLoD9LQvjvrswJluXsrzTT2V4E0t+oi7paKLp1K8XQarMcEu8PMiaD2vyxibC4i0pFaw6hQOSaU8iD1B50mjQ

LLJCTcrvYKAuLau0k4EEqKAxIQlEvdkAOwhvi8+0ybpjKaeCQBnBMAO8VYB4IN3kl4iIQa3IAmGxqjR6MetrVd4Jedng3Ft06hRGjKe3eKnz948Z2Piay/agXy8gi9L4Uo2mNrjaBwRzv3z34wnvR7Age8Sx6yelGEGs2gjRvdDQM943nKEW26KXLUq7smYBROpoHE7JOtMNGEsWjih86Xsjzq1ZC+aSieYUGTe2WDJ2wLoRTgu11VC7B9IfRZar

izdohsBq8KLi6HirOPzixqjHImrBW0BumrAPT7qSaL2hav+La4C3PCN5w6D1ZTOYypAfhKBSXGcUX25DzOA+UrRn9VqBIdvZyYejU140P9WAJ67F6TumHgt4KxGuy+DLrrli22uetWQF6zrtG6oFcbsR62HXplqaZut1J3rZelKqNzuDNgAL6i+yQBL6T6qTxtyTgVRN275HGBmpZNgBzNWE1HFBkGVNHLYPuYdPTUsi6gmm7rCiQ8oasAq/Rd3u

S7Pe1Lpjz0uz4stLRW6Cojrz/WgsP5pW6jUqRbgKYSJkgveSh/aP2oWiw8KCG8oa6M+zB2a6q8hHuwDG+yipR64ZIIBXjv4hoHXjDIMahc0uiDgGnigwcIAXT+FIAa/iZ4rqggH3qW5BTZYBheKGdmvM7onw6FfdL4aGe49JPjmeustEaL45fKbLUwZXtV6pO+RD2inqT+NXjQBlAcq1DIGAeCAsBxSgudgMmcr2878mXuSrFy/Ro1qSYOAFWRAq

T6KdBScg8pc6xStzqBSe/QmS860YC4B/Q1B8jkPcvIs3qhrjiy3sfLmZMLudrLumiWu6t2heW9rwmvfqe7xqk0te7zS4tMy6z2qgolblAveAK6460Esj7kG3MABtNgPmKY07+3ap4K20/4Df6uyP9sEK4er2QfDB64eviBR66vuVSJU6j167uybAAaBJAc4Gy4ZwaMBr7GSuvt/6wOvj25L5u3ko770hzIeyHCAXIf9TNeiXDtyR+3USQlAkm4Hl

xje5YB/bR/NkrVKbRd+q/K2WmHOi74cnUn1KrB3lpsGPeuwa97j2n3uP85qgPpSb/i4UFUDyckpUqQE6NkguBlGe/vUl32zRNpstgSgkWBlTUpqljoh4QsKHTpTsGZaTWmiwycl0wMBXTJ0/EGghhQLo36BdNfbG2R4g/Hs/TRUJ4Z/Sp094Zeovhn4ZLLFjHhoIG0gqstnyhG+fLIHWepfMvTV8MQYkGpBmQf7KNnRqkeGx0oEdeH8nD4ayBuqc

EcnLAEvgbAyPxe5zVrIEjkqGC4hkevDDsqsxRxb+2oFwJaR2olsfqrzU3v9xhKmdqpbGq98R+AeOO4FoS8wCZoCVE478rdrgo/qtu7HcHdvGG92vltsHQK+wdjzD+j7qy6XBsDxZiwRS/sUyo+9sBYEzgXOvQbX273OCHTMHwn5xqfCIeDKohr/suGf+kDsGxih//qckzWqDpsyCQ6jtg6wADivQ6PWJDrYqWm1Du0Lgx65lDGRR3uHrj1gPxpSk

UOvZX5HKW3guI7YxsUe5dEx51u9cLmujqxqJQKRqY7pOljo5qCs6NxCKSsoNrmT1OqjpRVzm8NoLH6aiQDRHJBqYGkHvW7Srk7nWBTqrGYVZTuOaTBb5o07Fkv5sqKS2sxtdCDOmWuKEq2yFtaLoWhtv+azO+FqEHrOhXp3RKwK9HwBVkK9ECpgHDbr1V0wx7LG4Wc39AUcEMLYBIkx+rpCOAdLOBSWZ4eW4fWE95P4FFJAEVPvSQ/FIeKaqCjW3

tdqeZbFJCa77fFM37n7NDTVHgGmYbe7HBo/r97su6Bq+CZJR0qP0WU+Oqjs35ObiFccxXQKT7C8iBFYJacs4dRKLh9EuAC1UjVKaAtUnwtMabU/us8HNu4AKaA2gKa3fYoABh3zkGS+o2ZLNgWOjUGPR2bupHJRQTxs6d0FibYmZURztSGqAm4B44UddGG8JaNAXC3BtgB8Y50Pcl8cqrZcU1S4CAJ44NlHgJzlti6kc+LuVHEuwBqgmBW6waFb3

u33p1GoG1wdoLHEVYZWrFE79E4oH4NRKwl8JzOrFpqqfTMa6ymgiqA7auXieuABJyQpS8hqddKdgsUH4iTRZIMKCwA+wTonYhEofAFKc24fqCFQ4AHwGOI6grwJ552ACiGEgiIX4azL0AWKbnSJiRKdyBkpzAFSmuqBQUymOAfbGynaIMQfym8AQqdQBipgiDKm/AiEZa8yy6LXp6j0inqS1hG6Z24VkR9nogBtx3cf3HDx3nqepqp+KcpQkpuiE

anWrcOBamspnKa6miAHqYUgipiiAGmUYVoJ4GOgikel6dG9cZkshgyic1TtU5kcNVMpPZgaxka68cdMnvLpGJoS2C8xjT/+amWJo+lRK04oAEH9rjiV2BrFrY0EPSyGbSG3R2TTBhn8u/rjJ2k0uCYbEard7gKqycPaNRg/uiN5hn4sWGfujz3+7E6x/WJM4EXQPrUDhwV1o52wZ+EuBApj/sldnR2EPDLNqiKZv0XUrepb7IBb0e+roOv0YYqTW

HyQHS2wSGZFiYpWGZ6Rdwerim5SbFYFzGEsoTojbCx9ABvT6sh9KazXklrLfTmOlO1k6Kxkmp5qc7AEAtChxvNqTH6x29jDbfTYTq3G1gHcb3GDxrsaebci71gzbXfQcYFreO+2dtDMJkWsBam3YtqmzMW/ToaKK2tO3nGTOu21XHKi5OdOS2+5ts3GpyK9CMQ0QTACjl1eqe3MbFGUgkvHecBJFpo+/NGEtqFSfnCYyb8DbgC7ZcWml/RjXBCUb

ZY44UdXCHlLYDZnAbNJBMGQ1BeXVaUi1fpwLuW8yce7t+3gG/cLJtLs/sQ6pwbLTdRyOuUCL81Cd9dKc7wfBKyo2e28nn+3ydRg2KNh3SRoe/BqPCi6o8dPreLICHsBSQYeHpEuJ/0YKGf+5pShTG+6brtibqqzqGCb5sIHiB75uoaLmiBPZj7ky5kXXsN9usSvCJusa2azJOq28peFmS6eXv0B5r8wEIiEUeeJiuwglMeLrBqeeCMyU73uFaYQU

mfDraUwPqvbFQQ0fUDEdeqJ7kNWi0eQ9wiePtC9QiOvKStgeh0fzrgpsidOrCh1+fjpkexhXxRpkWZHaj5YBrwigVMLGFIAqnBKFQAWgTTWaD/yclCwhnAdRY0XNFrRe0WdF3Rb0X9Fgxa0WsITCAAAfVAHMWLFyxasXrF8xadB+uxxHvBkoWKApwZwaTX2xMAV7B/AaoNnlAgbFvxesWTFvWEMXglkJdCWwl5wGMXuIfxeiWYlyxcCWol2JcSW/

F+gCCXwltJfSWwlyJbMWklyxeFBiIh5HiA0AYUBnBh4cKCnjYofsCdBwoAxDsXIwZKCdB7wEmHrAdkHDn7BHEYeFmQcl+JeyX/F/bHrgarMQGshRQTL25AQoYVD+RdoLwN/Yr0QGnRFbkVQVIA3sRJfiW1FjJbWX1lnRayWcl7ZZ2Xdlqxe6XzFgoBJgPQIVHXAJeeCFl42gELU4BrIfbE/j64TtD+QbkSMByAmAIYyWXll0xesWpID8Bam0UMIG

sgBxMwGEBrIYzS+IogfoBGIwoGoH9Re0NQGsh/yBJf2WvlqxfoQp8NJmsgZFvZFQBpsNclRQXqOAG6oWGpSFQBAqAgEBoSV2uAxQanNCGiWDlvZYZXGVulZRXLFjEE2wiUVZGOx3FzxasX9sEmDOXLND8BYaPlplYCWWVixfoB2V7bF0R6AblagARV8xb5WBVknrJXfAPwNFWxVjgB6WLFwAHbgKVduRdEHVblWFV7qn5XcAc5Y/BUBrqipX+gE1

a6XxV8xcABG4H1XOVx1eNXrFpVfNXBV1AEHA8AGAAUB64EVE947V2JfpXLFq9H1WPFmqAAAqBRd0Qr0Xla3hAaSOCpR4APajshZNYQUZBRl1AEOQrloCFLAPlsNY1WS1vZfpWCgHHBOWXhlNf2dtUfbBnT/UVAHjLzQUnvd4OeYNdLXi18xZ+WE4Akf0ANwCiEwBuqVZDewa8SWDyAgB/5a6pCoGFbeXgYPxa7Xc1lvOyAMVirxChZNPBUcB6IZw

BlgQoAGi8h9sCSHLhlIZvCiAJNWAZOxaVmxcXXS129dDWHVg1cNBexaVdxAQofyAKBa1j8F3WbIVADZWoAZSElX/11AD1WgN51agATl+9a1W716DaSXy1poCrWHAwNYogxoG5H2xASWRZzXm8hMBDXO1h9Z7WloOAGrhuqF7HlXdkQIGUaboEKC81dNQqDSJe1lNZmwuqZFag2rFwqBmXjIK9Zg2mVm9a43eN1AEXWSNjld0RjNfbAjXSNvjcg3t

ViTb42VljZbk25NyJek34lpTYgh2V+tYS1sgRwF7RYoauEI35VzCGk2Ul7CHk2TNjJa2WdlvJZnAHkHgDQAmgWKBnc7FxxEcRVkW5BnAcOWOXydeyYiJc3vh9ZBw3r1h9d5X+lpCEGXVvEZfkXhltyCkX0wZwHQ25F4gAUA80HHFyJ/N/jdSXTNjLZCXzN6TYk2w1/Dd02iNrkATAPiSQCkR4UP8D9RM0AVGYA0INBSIAsQcFc55WiT5BJXmNnpf

fBvwGvD2QooR5HQxrIcCA7QNUGqBIgfQBAHY3ckEhWYBmIfbA4wYYL4hRgaVnjZy3b1pbeW2S1sNdWWFNtbfMWw17JcpRktjLDRhuqDqYGhwoQICvQ3sMxYAAeDRaKdz6ayBugU15gH7WhQHFY0A5thdZZXslmdL020AQTeWWPVnGFRAfwZVc4BUtz7ZY3lkEzZwhtt1bYCXtt+1ch3El+gAR3YNllc22NlmHbW3dt8xf23ciBCH2xVkEgAihztp

Zeu3btz9Ye3iwF6HTBCAFdNm2tNALch3vt0zWrg0AHTdkAiNplBxx4gfZYR2Nt6Hf53At/xak3UdiHdF3ollHbF2YluHYsXtAeXfl3pdkXeF2F1pXeZWkd2Jal21dpnZ6WMd9Zax3ltnHYSmdkA7ZpBUACnG6p4y3sTO2xtsndQAbt9Rbu2yqayHIBAgOyC8Chy5wDSZdNHXYsWWd37dd4CtlWAuQccfbAxAxgS7Y9X1UksBeo2IDEBchAsdMBqB

wdgXfk2DdnLdl3tdz5eM3Mt3PYMXFN3LYM2JNozb1289svY0XstxlfCg7FkmGHhXeBxfXgHF7qg2xxNlbfS3y9jvYiXMIAAANe98lEJAB91ACJ6kIUNDqCmUHEAORxIRcHJRo16NZOB8nRAeYGwB4lCeh9sHtZIgO4a9hIgTsZAFn3MIOrcIAGtzNcsh1weRa7yOQGReyB1IQFqmg8165dX3iVhQFVWKVt7EYwqkYoQBQRIbkGbQWAbqgAASIdfQ

h0IbAA+wFFv/ZOxlISNH+XqiEiCYGQBsAeYhXoSbY9hRIDgD+XZ1rFHHWEV2AyXWPEVdf2w/9v9YA3NscA7XWIIEXvbWueMJjM00VldZbQCDoA5lRcATbGUggDggGaJmDqAFIPv13aGpRWdmqEy9sVoFfYAZsTCGEFtUJlHhXcD9FaYBnADA8549pg2GQP1oErSFB/yEYg2g/lmuEwhR2NeJfBPsRFcQg2BhFBgBQ0IKGwAEV7iEKhmgmAF8gE0D

gFn24gJRu/TV04EaJGvh9fYgAccFNmtgd9vfbgMrIfoGvYqt4/aa3ot4gFi38QeLdQBmqdTU01uqcKHCh6wRLfuQ3sLGHqRNoRrezWEoTCHP2rIS/drBID0RegP+t43bsPY18xdn2CvIQAa9d92NfgN7NSVBCgKt0MCq2WttAD/2W9jlfuQ9sQ7GOwnsTZCuwbsAVF6OHsJ7BI23sIA4+xrIE7D/3yjixdn3woBkALW3iWfaH2m0PNFaPPiFo+4g

x1/Q+sh32FBH62BDzCEG2u0UbfG25i//YaBwDtCBO3nAC49mWrjxVG7ROnc5BFRuqZzXepMIQKE03DND8EuIBgCA8eRPGD8B7EHj87aePoIF4663XdoIGgh9sO8SYAzAFTVsgEyr3aYBdNePf/JggYgGT3lIIFb+Rw4Hqb+IJjcwCqQgSGQHSh4BiNGKPxFwaMqhwoaRaiOc1xRY81lFigFUXO97k8r29luxcb3HF+8GcXXF7qijXX97xZ2c3wRl

dk3uTjvYL2ZNovb42S92U7lOVd6Jcs2ClopZKWyl1paqWal+sDqX7wBpaaWWlipfaXOltHY12PV4LepBqiYZeyOxl8tF6nplp44+QFl8HZ2329lU8y3eTrPbLWUVo5ZOWzVi1b6n0QfNc95bl+5f2IhtuDlQAXl2FY7XLT0XZ7W/lmbGqJhDkFfo3oIcQ4+JoV15fimpDww993UV5derJf9rFcKhcVrtAJWiVqhpJXn98IGUgbV05043izv0+lOH

1v9aE2MQd1d5Xgz71eFWuNxdcA2hN2VbFOPV/s5VXyV9VbvXF1kDaE2jV8c77PlV+CCtXw4Zs49Pxd6xbA2hNt1aXPLFz1ZDPfV5CADXqyCtA4BNztresWxNolCjXUAWNZaB41xNeTXoIAqDTX3ADNayPT9kKDv2Vji87921T9s8k3DlytdcOCRz9e6oG1pKGbXCV7HvZ53l3DatOUzhwP7XlGodcJ3R1+7f2PJ1xjfDgZ1/M9/5ldq09oOyz/rc

q8N18gC3XcgHdeKg912Ae6oj17QBPWggM9drgL11s7iXALoC/V3RdzlafWhN19ffh3QCC54PuIIg/pQWD4DckuwNiDZl2uL7i63P3QeDbAuU1pDZIVBjNlDQ2WT+Raw2anQvaQuNoAjaI3nsTxdfByN5DbpRqN7Fbo2wV3C8Mgrz1jY2h2NyOA4v2zzPYUvNV0XcE3pVkTbE3Lzoc/kuPL5jdL3vT6HcVPeN5Tdy3VNmqHU3vd2ne02g9k7HCuuN

5U9Cvc9309iWNT3gFs37No0/rAnNlzdWQ3N2KA83hQLzbc2SRvze2W4dvpYQABlu05P2c1yLfJOmTmLbi3RllI4eRTd07Dkuc9tK4y2MroK54uLF/Lc52aoIrYBWqoMrdk0djto/uQatopw8CGt8Q/JOWt5SAcu9kTrfPput6/b62vF1VHVQu0EbchOcgS0HCBpthnfm2iIRbcCuhrz06tO7roi913Bd2Ha+3cdpNG6ujt9qZymbdi7f437dinaw

vHt7M5e22US68Uv/r6dP4O/t9lYB3eVoHYEPQd/892XU9rbdeuHrkXaCv3L8xa13uL1G8x2hd5nfeuTd/HcahCd4nd+u7dh3f8hKdiOBp3HAenfe3Gdzy793bF6G8D2xrqrZ52+d9G+eu09wm4l3Mbjy+xv6ULG8CuFdxXbxvbryG4UuRb3G6Av8b/XYFvWb43dQBPri3f2wrdkndt2dtgG8d3abuE/d2m19E+92Ib/3bZ2ObvTa5uw9iPZluLF/

bGj3WAWPZqhsTxPbxOZz4a/MWQr9JfT2lN6W6GuZT/q9M35TiK+SuYN1K6DuwrjG+2Xq9+sFr3692dyb39sFvf8vs9728jufbnvb737DgfcJAh99HpH2XA8ff7Ep9vIBn259tCDgPkBjeLjg19jaA33H2bfbqP99pa5VQs1787PyL99LySgb9j8F/OIz2s66Mn96c70u39tqQChDQb/ZeOCDwA+APQDloHAOijwlDTPrIWA8X34DhYhtgkD8IBQP

0pl3nkPIV/Y4ggcDki/wPCDyS8A3SDwQ/NA21lwOoOmAU+/oO/9xg6iBJLtg/wAODkg7exRL7FdDArbwQ8KgMzmbEa2JDi5CkPH70gDkOCLtKe3uFrlKH621DigA0PflxqTZQa4dKb0PCznA6+OuqYgFMPlqCw5/XrDqCDsPMIRw7QhcR54YcCQRz4e6pPD7w7wem7/w5nSXqYI6ZRQjqLdauIj9q/kXYjmrQSOkjzq7SOQkTI/buc1vI+YACjlg

CXvZkFe/hRtkeY8qPo16o9qO1jho5K1q0F6maPYIVo6ZR2j1AE6OXVno/ux+j87Hexhju7D6PHsc7AmPzHz7FmPFH+8+jWlj3JE946j9Y6hRNjqw//BrIWa72OpDw467hjj9tDVRHltiEePTrhE7/2bjy9dQB7jiJ9yRoT5qF/2ut945yBPj4w9+P4r7VEBPbwYE/ZUKsRCH/IITsbahOf96yFhPGMOyERPBe5E66o8QXMtNvXb3E/xPc1wIHGgu

qEk+mJyTmRfmI4YYadwGEg7q14aYRlmCdQT02spEakRsRsoHV8cTpznSAPOdnD6B+RpQUoD+k5OjGT5k4w35Ftk4xAOTrk4zu09/2+sX+TpvaFOXFtxfHPwIHxalOGVwO6Of9dsO+g3IrpU69PHnzO+jv1T/JbRgtT0pfKXKl6pdqX6lxpeaXbkM046XqrwC9qv6roZcav5F8ZfPOoghfcuO3TnNkWXLT9O4+estk5+FuAz45dOWvVknsuX79yM8

QGHlmM+eXoHwtcR3kzzQ9QeSjtp7GgRD0FYcCczqFdQAD7mSAMOcDts4sWIHzFfxBsVqs/xX+gQlf2xiV5SAbPKV6ldifPbx6+AurFrs+lWez/c/tvJz+CEHOYN4c5dWZV3s4PONXj8AbPU7xV8sX5z6VcXOeVg15XPLV4w43OOzq053PpVvc6tf1Xm159XAIE88DWJl5G52XF1m84WQ7zh86fODzpNeMhU1uAHTXoIUI4dO2ntgHDOaX+68FuFX

hy4rWENqdIgv1NxtZgvW1nHoQv1tvDc0OULgdZnZh1zC+d3sLieKnW8LjaC5eQoCG/5fSz1dcEOKL69hIVqL79f3WPwQ9e0Bj1j16LRZNNi+CA5Xvl5TeG38xb4uEAZ9YNXBL99ZEvaLn9fEvAN5SBA3lIGS+z3k3sd6TfDl5S+rXoINS5Q3NLnh5ChdLk16heDLj8CMuYr2x7MuZUCy7zgrL2jasYsz6t/svOLq07Y2Xz1y79ORbgO4fXvLg1d8

vXXsXd/exbvq+xfPnv26RWhz6K8guNN7J4/AOdvTaSvoP8O/eeIP0JcGvvnqzeyufiXK8c3nN1zfc2DETzcs2fNn4fPfN37qhtPQt+047vmr1oi4fIjnZ4S2ktlLd6usXjD/0WsPrd7S3Id0a6tuJrkremu3tyrb0f5r2rdbuQH1a/mv1r99/a3pILa86d3wHrcCfpAYJ7OPUUY69KfTrybYuumbq65bPQPvF6+et3xW7WXfb/S56W9tj6/x3ed7

69ohKb/6+pund6lbpuviUG7e2GQZm5ZvdbqG4D3/t0NcB2/iEHaJewd/08h3OPzD+VuulsD6o+rF+W7cv0dl6+x23r1W8+uybonZCgnP5z8BuK34G/sgGb3TXBvfPyG5+2LbpD652Q93nbiWYvqHf5veb6q7i/tlxL5/fxbiW9lvpb+L5A/pb1r6z3zPszbq+bPkm8O2NbrW5y/yd/W6wvDb6CA92TbzE7Nu2bgPcq/g9tW5tvHsO28VXHb1KdRR

mnpPY9unrixai+stur94/NV4764/tFkO4CvUP6DYjvLvzD9xerF2O/jvYoBvaTuU7l5/Q+Hv7j6zvu9/vcH3h96wCLuLkCfclZDQaffsPZ9+faruf4mu8shblzw833iAJh+jWW7+rbbv4XkKAkepHkE5RQ43hN5uXB7iIGlfX9qaHHvfAqe+SfblgA8uwQD1yDAPgTqA7ke17ieKQG4froi3ulDne/WgUHjKc5foH6oiwfuIAV//2l3r+7IOb7vN

7qD777qCben7l+84PWD9CHYPYICX5/u+D/+8q9AH9p5ZeQHy97AfPsCB6geEz5qe5+4Hnx5/BEH5B73u0HsKF0PQBo+8MOcH8ODwezD8wEsPsVmw9IeHD6NacPKH/EZTWaH4kbrvOoBh98Pm7gI9YeQodh+k/GPlTGY/ojvh/iO0NwR8+RhHjI9aOxHs/fowpHkleZ/Jr2TQUeyHhY+Ue1vECHcf1H0o6aPRP3R4uR9Hwx62wRjkx9OwzHqY4sfj

Hqx/GPPF9v/se5jkv6UeXHv8/ceZwDY45Qtjy378esLgJ72vwIWTU0/wnk68Sfrj247if+oEp8uOknmFFePe0NJ+4h9sF38MgsnrTZyf8yvJ+UgCnryHBOEn54+p+d/7VBm/uqJE9IAUTwyAafEypp4T2WnvwIJP2nok8Mgunv8QenpSdOiHqgyRrwMtGgIN7pmUMoMvL0KhpNYpUjMVGQOvB5gChBHEIOpillMVjsFvAC5u35zGlAhtLH/A0EB9

UBYsJpt3NsNsCMwRDcLRwrgN5U0TIF0R2pWBD8JfpsRNGUDBiKQeaGERBKAKRoFqgtL7LLQiEEIQHegqN3RNjN+EjcFJ5vjNMwDPNHurZM4JlXNSFl90SNAI4KAIFRwoFvAUgEYBt5NOEeANWlqFguEvBgnV08IAJwiP2lVSrKZJgMq1GZuh5v1PWIghu/0z5idUL5t2QVaOFBEgLXBHEHTgcIkAwNYg+FmAOvBxgIFRYoOFBIwLRMjxqxFfsBrk

X5vrhtbFN1N6kItDvDACM5vADFnDwA3AR4CvAf31rcqMAywj+hNMMUhN7DfU/pt7QlZjmFC8GhUbho2lG5nQQe5sJRAQJWAvCIoxOAgYMR2lBhuwIspwiKsBasN3xpRmjNiMIICYdPKM1+rxkxAeBM7glJQZAUyY5AQvNjCG8EyZqvg2gKoD1AZoDtAeB4eAHJlYrFf0RkJeMMqP+MKunLhBnk/0lhOhRP4CU08Gjz4CGt/0sAs0pYgYJMhZsIt+

FGVIKiA3AKYDEcmrDcg1zuwMMBhmE/hmPEngR69WAK8DxjB8DjDhwNGvIkFS8I8wAan6UKWDzh+SKNM3gKM8qgII0ppgiMpnrNMZniiMEAZIAkAXOxUAQgB0AXABMAYkBsAe+kByo1RhliGxngYCDuIMCC2UJ8D0BsJEMwuL0pypL1b8j0FBBkkCNxikCJACkArEP1hesLUASYNgB6wCPYWJsQB6wNgBSAFegoAFf4u2hjJDatjIoEGDNrzCLpec

Abgm9CWRRSF41NqvcA/stTIyyHkCEpKxw4kLcAmZBwCM8BWBuAdsBeAfpMOEgIDBCIMCQJnD5RgQ918ClID5KJMCPhLMNiFiogE8gsMFgUsCNAVoC+QDoDMRgg1i1OH0MJpA4YeDuEBRIUV9gV/JQQmrhKBPV0uFlq0eFlzNjwt10xcnn1scIehJAICRJANMVS+kuZeyokAU2FvAYAFQt8SoeV8hnCEbgfmE7gV/Nd6kMEpgAWCiwSWCsgZpYcgR

2BnynYwQ0utpHKByR0BHsw+JpcA+SJQIh4qP4wYm+1VcB3wrQQ4Z+tDxw2gRfoSKl0CtJvP4l+ld1wNAMDMFqE0N5K71TSlPN5uOqMYJg4MZgQoDqUmQt1ZCoC1AcGDVgW54eAH2UIwYnNa0gE59cKCkqZLsNIGMmCtMLRwoSr+1HRvhVeFhU0WHI2DEJALMEgfvEqgJFAHqHE9ijtPEXeFGcwnsJAbkDhAtnK04S0AFoaTo+FWUAhDCUEhC2UCh

DKXmygMIfTwsIR8gcIVw0sJE8xi5s/AABNuB4QVCN1eL0wkmBNNBrEcQ0QTNMMwgUEqBnyCBQdgAhQSKCxQW0AJQVKCZQXKCVnuSDYIfhCoDkRCF9mz8KXgwhYzuRDheM4BKISpdDxiyDyRpACOQdACaRoblTIvw4KAOsgrEG3AGgDcA3pli1jgDAhOcE0DvgFVQrgE3ps6iTQikJQRDgHZFpwQ6Qf0PBg9GFq4+cHeokGOaCuSDcB6otGkL9P3M

7QTKMdSHuDzBly0lRoSkImieCvQQFZNRnhoSFteClAYGD7wSsDQwWsCdQqH01hv44BKFU1WwIBDZTNoFijHVE1MOHESJrD0swWBCknBBC4gRyVoIYLY7qjRUmmnRVAsr5CaOKAUjemwJnUp2QgMIyRwoftUfGsHMAqgyU1mprNmxqvh8AE6A24GshwoIcAUgAgBYoPEB6wFegYALUAjEPN4DEIfBSxtekrICQB2tKm0exgNJ0BHowExlAgCZEJwB

pHVg0kCto3GpQI5gFMBQ2oJ1zKi7MqgCkA8gPEBdEOcBAqFvBzgJoBMAODDmALUBD0EYANIaQAWgLb5QwA4BzoZUlzZu75f4JylswIUgD3HLMBpAkg6ugMpwiEaJL6AW0G3Lp1VklHMACvUUbqvhBGAFl9NpMwB5QOoBNTO0pv5hrV14CTAKAEYBSAPWA0EFYhJABiA1gFYgKcPEAGgOvAWgIRtnALgDVipfA6aIiY2OPSQDmLeM5cFcoaaNBhya

J0D17NTJiTLuxSKoqQyWB3NQaJLhd7MCA12FsAqqFKNUZoE1vzHFDhAcMDPtDjNolBID3QYjZpARIFZ5vv155hl1ZgZJkP9BAAjAOvBIwBiBCwfzkDEEmIKAPEBVkB8lXknQ5JYVOxO6qBw5iNuV6AABgmlvWBNAMPB6AE0A4AJoBB6IGwI6neDlgSGDL2gT4eAFYhlnkVC3Ju+Do6Ay1C8ECEfwT/52CtpIhXP1C2wPVDM+jUY+FtEDxYpBDetP

ECopg7F05tyDjIdwZFoctDVkKtDVgBtCtoTtC9oQdCjobINFQWMJ1MDuBf0FVRlQfWI3/MUD1QT+hH4HdDmWBjxTuskBSMl/IbJCcNnIewCuBC+VH9CyVcJtFC+gbFDHQfuCEoa6CJ5s7CX7NPM3YbICiFu91MoXMDfYf7DA4cHCXomHCI4VHC4ADHCk2PHDyIMoAk4SnCpNOnDM4dnDc4Xal84YsDcoUXCKFiXCrEPIlqFusMRkFAheaMcAWFm8

BUCtaNIQfswwfHTNzgXE4nAexF+HE0B5vKoAoKDe10JrmDfAcAFTIeQYLIVZCl6qWDeLBwBJAG3AjAOMBD0JaAkhpECV6r2kgQDECmwVBD+4fx5B4UMEGEfoAmETwAWEWQ5T6j7FQFr3AABG+18TOEMFuOWBRKDOgZSrRpjgHClvIjMAYMO5CD8EsxTihhguSK4odWF8AaAQso+AWpQbYU+5HeqICAKm6CgKi7DPQZ/Cpgd/D5Ab/CfYWiE/YQHC

g4eFAQ4SAjI4RTho4TwBY4f5goEYnCtVHAi04RnCs4TnCbyIhMqgGgjC4Y+CL/KXDZGpsCjRsg1ZhGbIDEbKZiAcUZ7IuERSbOzNHASFM2PNcCZET3DyKooZPRjFoqgIOABQCtBMIYU5frk8dJtrhC+kW7BBkW05tbpcdRkTRCzMHswcEm9VFlLqI2ATT1J8mxCteDPlGevCNJnjxCFouI0d0KPCVoWtCp4dtDdoftCM5PPCsRjN5GqOMiBkRRCh

kUv8zrlwNAMlt4bpnpDQEpyDDIU7ExJr9D/oYDDgYaDDwYZgBIYdDDYYfDDdVFpt8IIyA1RKp48MvBhrxlBgSxJXNecPKQhsOtUaOBTRtBrLhNbFU0B5DEDrJIMo44riiXytIiOwISj3EUdxPER7VvESMDfEa/D/Ee/DTwdBMbJiEjLwWEj/QZ1JIkYAiYkcAjAqOHD4kYkjkkZCJUkTAj0kboD4EVkikEbkjl5gXCHwflCnwVYg3aLgiSoVhIik

LVhyWFtU3gHXCyEW8APgHojvwen1mkbwtnAdRR8AJFAhAGJCDEN4ClUlXU5Yn9C24JGAhAOMVa4E0tFGKshNQN3QEAMltFdIxM6wckMDUlUASSEYgEAFvApwPQAKAMPA2gMKBxgMN0b0BzCJBuIjJ6nLFOEeZDLIWs5awRECT6JIizqi1DmwTz5WYb8iJANvQLUVajAFmfVnAFfQKOMcBfOPqZgZk3pzzPfVE+uphasLRxvIYgtHmFAw92H3I+SB

RJ2AT5ITRmlQ/WMYVHKC2Fl+tbDH4fFCXQfSikoXgsPQR/CREiqMzSulC4LByjZqlyiAEdEjYkfyjQEQkjwEUkjIEdGjoEbAiJUZkjEETki84TfI5UXlDi4WvhS4a5NEGrK0bhnRoEwSD0sdAdo4SvNRuXBKQzgUaiLgUZlWkbVE80XIi7htFMUFE0BpIGbsPoodsoAJhAAAKQ/EeZALIFIAAAflwhEGMAgWmmgxZuxqgCGKaASGMloaGLmRhwAW

RsMTXBKyMIIC4hSCGyMrKAjThGqIN2RqWnIGDZVmeVWH+RQMJBhYMIhhUMJhh6NAhR5QT56i6UgxWGPx2uGMQxcyGQxRGPUarIJ28UvSuiBkJEmRkIuS3ZFIA8wAaARiBaA9HiMAfQjWA09XXgSoidAh6HHSIfTIccgyXhP3jHBbM0fGXOCb0UPW5I//CioHwDUKr4x0mlAiB82YF5IUPQbmNLTZol8LdyvkhIqt8LXaAwyth6C2IQT8OnRYTVnR

EwxShQSO9BsE3ZRfoPXR/8KiRQCNDhO6MFR+6OFR1YFFRJ6NThCCOyRyCIZKqCKDBN6MwRd6OpEVM3TwGkwjKDC3yayHmVKn6O2KvOH2UewIcB/6NoRKqUIiRgH7A5wEIAxwDXmOYIJK7CPtRUAEdRzqIQArqPrA7qM9RV6G9R+AF9RdEzpKDE34c5kPuSJMHGAViE6oiQEkAmgEL0mADYA6mDYudA1YRWfnrBUiOAxvcLah8iNKG3yIW6+ikjAP

WL6xA2PLRWiMlwoLnzIX0wUYMQlsxpBCBS8UhcRlYBvMLwm4EM6COG2rE7AheHsRrGkuUT/BKQriPQElKKHmk6NthY80ShuCxix86OZR1kwmG0wK9hV4L/hESM3RaWLiRYCIgRccKPRaSOThp6IKx0qMvRt4IKR8qNvRKtHuSVWI8IpoJIWG6mv0j/WsBSoAE4WZHsB6YKCm5w0ahoU3Ah7SNahFFSEmPSIkAEFzzQzeTwOLaBqCHgF7Qe71whcu

I5QCuJkOv+2VxJAFVx1EOwGf1BIxRTXcU5GONElGPwGrEKRB8WmIGTPTmi0zwoGWIOGEamI0xWmJ0xemIMxRmP0AJmLkaMkNlx213lx8vx1xNy1qCVEKqC/8TeRc2V7h/A30hc3Tux5Q2Hh3ZAMQMAHGA9AECoOOHAwToH0xygBnA+gHiAgVDVomqhfBR4zMxNkJF0OEjY4tXSNUtmI1EQmiIRxtR0kmnh2KEpD5wIuAyoCGHNBfmNdcN8M4WW4P

XaO4InRGCynRWMxnRGOKXRsWMXR7sOXRxM1XRSWOP6DOm5RW6L5RAqLJxB6IpxCcLFR1OPyxUqIvRKCKvRjOLKxSw1AopcJ9xZSJoWcjDgwz7V/Rb6PoIRGSaxbNA0wtqjQaQEO4WIuKz65EzlimACvQBiGIABiFMQOAMgCPgIDRPOWDRoaPDRkaOjRsaI4A8aNMhFGj9RWaPkiD4T/gPAAMQ6tA9R4UBxwkYAzYMAE0AiQFWQFAH7AmABrBQ2P9

REiO4mF2Ilx+aJZhrYI1qX+J/xf+MkAABPlB5DiXhOBHgYm7jsiAsSVhBCJOA/2PPMymQ6R2k1WCR2jzARAnikFbj1wTMh2KTiLcaijG/GiOLvhoWIdBQ+NRx27Rfh0WPHxWONShUFh9BP8LnxfvX8wxON5R6WJXxe6PJxKSMpxm+IyRtON3xxWP3xpWIwRR+KwR13DPxeCOUQRSE7A55iq6yHkWEdSN8kWZB2Gf6JoRLSMwCQGMoJIGOb6N1Qyc

woDSghKzlxfqAy0a/1mwkcFwhMRL5Qrn21QqyASJlW2ymyRMPGTXiNxcQBNxSyIIR5uIRBRlmtxKTHox6dSmcTGIdxLGKdxxaJTxaeIzxiQCzxRgBzxeeILxPACLxZIOxGS8ViJGRI+Q2RNaOuRJrgKRPAB7yJUUlI12siQPjx7fUTxO6ALA7qCQyMIECoIgFWQ8wGuyygAoAUwGYA2AD0BzBNLx+AIHi7BP/Q5PnMsw4Orh6MHvqi2hbUhuBH8V

fAgQY4No4I6IKBVTU7xOiP8x12m1cveLHRA+LCxQgK8RIgLpRUWLHxU+InxKXVxxbKPxxa6PnxG6NSxxhNJxZhLXxFhI3xeWMlR56KKxT8xKx6CKKR9KUpwHg3AcYJXyQrJC/8POOqUYUKwaPJARmafXaxwRJNRdCO4MUAA+AqyHoAbQB02NqLFgI2KXMa2IyEm2O2xu2P2xh2LURQgBOxB5QQJ7dGACyBNQJmgHQJmBOwJuBPwJhBOIJp2NIJya

LLBs5ErB1YKTR6uRzR/C3CJV2Klx9wLmJimJ+RmczZArJPZJnJO7BsKPMw8DAKBfrFZmyMyKqcuAx4TzFrykuG2ApCJcxqwQn6DSI2AgIGWEPpPna/WkcRGZFkJCOIehwWO6qShP6BKOOBJdsNwKfiK36WhLixaUJnxTjjhJBhMhERhO3RphKFRh6PRJ4qO3xWJJlRjkwkAB+McJP3Upw5cNfBWwMzA2TVzs1s25xmmV5xkYh3CSwDTBL+IzBb+I

7hTULJ0l2M6RRpm6RMEP4U7hzC22qE/WhakqmKWQnJkW3acpPGIxRRMWRmgVKJvOAtxwz33SNGP4ayIOqJQ1mmmdRIxBjuPmmyxJJgqxI88GxK2JkgB2JexIOJfRJuRS8XnJEK0XJFkkmJUeNeMMeM+RCmNrkCeOUxbGPGxLqLdRKQA9Ri0LmxPqOshJxJ2KnJAw8s9n4K27lU8vkJFiQGG1cQmlBmxfBfUa9XUwzC1MSoZKPscQEiIyBNshhAgC

IihPHRgJKdBmM0VG6hPBJkgICRC6KhJS6LxxWo2zJiTUMJiJPzJu6MLJ6+OPRJZMxJhWPLJhOWUBVZPxJqQLGKRJI26lHRjBUfV7kRw3Cy+wJ8axRjFoLiMBAEsWNRWYIvmMkwocVQFQM8QAoAiYRTCbdCiBF9GoI5QP2qVBNNanUMaaD1XFmvTW9YYM0vouRghiTEMOku7h8aWwEyopwJVwgWWcA4RFSA9czFGlNjzArFUoIswE8h3YGIp18Gws

Icy9cGs2+hWsxbG6AD+hzAABhHGKBR3GLBRfGK9m+WWJq7vgbwJYhMEOiWjJRzQRMjkIuAxhneAtAM+hrrXmhO6FUx6mM0x9QHdxc9U9xxmOypF0NRhRzXiQh0grMaFQTo7YEqoEPWHRJMKWS4czFqk2QlqpbRmyLYMHhoIBphGqRIA9MMZhkgGZhSmKRaO6F0p+lJ+i/GIPKmiM/QBAOL4yoN/Ua2gbitmOfgM/jF8HkVzsmnh3hdHAZsfnndK0

MzUU4ZLhxLiPkJxVNvclsPIpyhPCxw+Oopo+KPBhpTTJk+K/huhNCR+hLYpuZI4py+K4pWWKLJvFK3x/FLpxe+IZxDhNEpx+IpwpSN8cb4MzyaMGkRvaOfxlUKKi9+LRgj8FbAchjbhn/XfxncLaR3cMlxXSOlxY5PQABiDgGveWZprNMNxUJGNxq5LNxG5PKJ9BEqJR8VtxOyNIG6IN4hi0QApTqKAp02JAps2Pmx7blWmQ1BZpLyI60QGSmJ0e

JmJ9+ULRFpPQAoBLDRRyAgJMaLjRzgATR6Rn/yEwX2pCYxMsU4LqwNwGJpW8OvGZQOvgxhgSkoM2rR5VPAY5/C6Bz5mwIfYKGwLaMswc7T7xIWO+p8ZJUJiZLRxNFMBpyUOBpjFKnxzFIyhENIZi7FJ5RnFMyx5hJFRlhIxJZ6IEp9OIkk16OrJdpQxpyqPXm/vi9oUlOQqu4HIIHmOIRRln5muqLZoKDDzALkUppnM2ppmlPEcaQx3QjiBSAsUH

0ADQD2y8iXOxRiVMpACAPAFlKkKVlPNaMHVaagYzwyCIizEGzDJY7zV3cJSFcU8uAZYg2ECyuMn9Uxhl20PcmsCnZFCpm1TQqAdMpklHRipjhVo6cdno6yVNSpgKK4xIKJ4x4KPapKMNypJVOtBz1jmAlgPzAh0l8hTJE3Ul9HsYVVP46rSXiptVKqAyeNTx6eMzx2eNzx+eMLxJMBfBSbRk65Y3fpPlW6p8swSA6KOZKg1Mhxa7BGp4418o4tTJ

hU1JjmM1IemKYHmpdMKFsy1NWp5pJ5BUbV7p/dMHpr2MtpFAl5wCKOUyOgjOp67gqUOBGwodALJa1qkEoq7EsBg2Guiz1NhxziLkJlVI+pwdNjJodIfh4dJpRIJPth4gNGqsdN360JLBpiWMUBxrEXxJOIyxq+Oyx5QFyxfFJzpyNLsJqNLxJCqOKRFOAfRd7Xcm19RO0ugT7RDdMdIOzD3YuBFbplwJdGtNNuBERM/m5DQuMopjZpTVDCZnNNLw

K5LIxyyLKJLELfgO5KIGk0xqJh5NyCx5IaJ80z1p4BKjRRtOgJJtNgJD5IPybRkiZ3AzVpH5K6Cd0zjxZpPuxvJLbg62IFJhAB2xe2J/CIpOOxkFIrRBAMeYsjkaM9JAMRHJAQ8KtizAGeET62KLoIvOAVI2wB8agAgzwtHHgW53S3AOuHkYgAmzAG8KRxu4ITJqjKTJ48w0JEJK0Z0w1ZRujNhJSdPHCKdKXxJhNhpGdJyxWdIsZNhOxJeSMrJa

NLsZBJM+SElPLpJJO2YUaWxEGFWzAt+gWAACH/QalI6xIRLG68XlHp98HppI5MZpHUMACAYwta4Y0zsCSFEoCPFMBRwCzA9tOBw8ygzIyyONq6SFpCdlLAAEzPFiNwDehHfEoInCy6k96gqUKuBB8G8PVm6NWdmCVNXw9VNdxTVIrAHuNLoXuJMxKDLLGuzUuhaMN4KBghIE61QrcMfSmhZzSdmvrg6SSxLWAKxJnAaxKvJ2xN2J+xMOJ7WVQZfL

M6pPlVEo5VPIIDzDQQ6qKwZmVF0E+RnaBHkQ+hoDLGyRbQnGFMImCVMILRu9TmpRyAWpVSQZhXKHoZtTN4sMpLQJMAAwJWBMIAOBLwJBBKIJHTK0RpGBMszih4BRolsxgAiGZ8CF0yTLS1h6g0JMLkVRRquCkJVLKlI4uApYA1P6GijIBJP1KBJWzMjpANNxmx4P2ZZ4MOZCWOOZ+jLOZRjILJcNJ4pVOOsJO+PuZsqJEpzzLEpp+OxpG8x/IFdO

K6nHnLCM3AwqNLBJpnOPKpWHl8ZAGNCJZPHBZ0CAnpErkg6os19G6hUJCs9Pcq0wH9Uf6C2A6SFoBdJK6AWLKeUsGGNq7inBwCLI4ERLOTZOoOzwh0gawSzMlMMzL+AdkXpZNVJvp2sx7IzRJgZbRLgZXRMQZyDOTYybWyKhoQpUF5UFZj0MtYIrO848GHFZSoS+h+Y1fZiVIgAZ5IvJ6xNIAmxKVZd5NVZAKgA5Zs3QZO7CFwtMxuGzMwAEhrPM

wvSBNZ4Xm2AhDIqKxDImppDKnGHbnLaRkQdZVDKdZNDOlYdDLMYokx1pEACYi94H0ATQDiQ4pMvmA/RyBmMLjGReQBA1yj4mWzHeA3wFmA8GBWAXLnEJjqlk8d6hUcTNCXBgtFqwCpGcU+4C7AQumvM6zOthquAuyEWJHxYJOjpc6Pop2OMJm54JXRWZJOZiFjRJCNObZZZLzpwlKeZzOMpwLhO7Z5SOFIGk03seeTB6WjDdKaSE5STSOBZoELFx

zUMNJkRJCZKCkwgHjGKgjpFs2X6UBGWkMJGoIyEu2yFwhiXIHgH4FqAqXIBGeIwy5wf100/kBy5xGK5I3wCpCbegRE62n5phA1XE4zxIGWTC9QbPRG8GskVpCXO54+XJS5zh3S5e70y5tDwq56yAjx50Siq0xKqZwk1/JsAJEGRaN1pbQHoiGIDbg6qhDZ+1LgQrkR8aTBG2GhwW3cwGAlKHlPp8//GBxsuDhiQZMw8RwxNsUhJoCJSBUczOVtpF

sO3Bpgw2ZKjO4yntXUZYwPRygSJBpwSKOZLFMc5YrRgq+SM855WJVoaTRVRPnnLAaCH4mpZCbSIZPqxrC3BKCnm/GEXIZJouMAxM7ObUY9OaBRpIZpJpPKAi7LhZM9N7G53MfarBVk5P3juUt3NR0kpn3wpZGfZ19LVCyWRnAqMn7AtcApwToEkA/YGwAw8AaAtcGPwgQDUxOOCkhWHJfQp0NTYGrNw5VblWYemUJhTsiFZ7HBfKhwD/Q9WHsKo4

yiKTPKySb7LmKH9yEA5wBgA8wEIA29HvAMAH0AV6EjAUwEIAbcDWAibX/Z4vKRhaDOeaGDNwIAsVOBUtnmZWrJm4MCF5ozJEfgUlQ15Jdmo5slhIZY1JHUILR581DMWptDLdZnHOUM2tMYZ2TB4AjiFrgbcCEAvWHW5OQLgQjzFZCVVBIIuPLmCNXT5wkGHMRXjWgWYzP0wCpBzyHOgVhYuAx0LQKzAJNCOYz1jrYvgyM5FFLM5/1Is5pbKBp1nO

0Jv7iCsidP0ZDzPQA7bK85HXUh5SDUiocGD3C8PJYW9/Brhs9mfxFUXUp1NIHJHfGx598Euq12NAxKIRFmxPNsp1mRZk1fMyorYDr5rFRV5TfNzsANWz5lYEZ5c0Pg5q+BxwT0XrAVkEjohSHaWjiH7AbcCdAM4HGAzgHmAHsXxqobkRhZ0Kd5Ps310O4CnByLkDJYozmaR0lbAERD8yL5W9Up7MD5k0klZPIUt8s8V0Q9yFwA4wDbgLQHGADMKd

AeOEIAKQDYAtDjua9vN5ZPrU1ZO7BgQmw1WZ69jWhm8KOadHHXsq2k25SpmWAVHKtZNHIBaEejIZ041jmErij5LrI45DZGoJiiI1qViFWQw3XvATQDfYQgCmAGQyWOqyHwA8QDmxk2D9RxxM6ZfcjQELAmbUu4DYS27nSQrfAR4DLH9U4uGpkIlGEoLiXHaZqk8U74gFiIC0jiag0Aw/kWe5g81e5v1NUJB4KuCjsM0ZffPTJOhKrZAPJrZkIhaA

YRBnAKMiMANcDaAMACMQMADYAkgCMQPAFigPAG5ZVvhfIchyMQToDWAeJw/CW8HsCM2EjAJMCJ2glJtKlDlB5ThLvR+c0n5yFQw8FBBKMTaV+mjcPpYm1Q2YAoknZ5TWi5g5Ni57JWNJFDK5BQwRwFeAoIFRApIFZAooFVAqlhp43fg47TiA0GCWEVyiSsgyhcockyW4Z/Deh11OqBfON4JLagawamAb4mnO7gFoN1EpgMjZubNZacZOUZfgojpa

hJLZQQrxmIQt+58WIvB1bKyhBjOiFFYFiFTQHiF8bySFKQrSFGQqyFSbFrguQuUA+QsKFiZXoAJQuq85QsqF7nJyhhSI7Zx+J5hbOLJ4L5Ww8uw1bRGVhFwkcXNGPZOFxpEw0pTJO7IkgGhhBiHXggVHmAE/NrBQBLtRS5iEA/YHCgGICKQ94H7AKCQ88mgHrAqyGym8wCgAuiEGxapMlJK2O4M+gGT5qfPT5RSl4Rw9INJdNPnZA8PXGQwSpFaX

FpF9IrYZvYMb59cVTZRqg/RxQJPmMwEfUdGSys49P2FbNGNUVHF7ktNChxkjJ2sK4NW0a4M6BJox6BX1PzZYdIeFRbKeF3fJeFZbLeFcdNBp4QqH53wv8wvwrWA/wsBFiQuSFqQvSFmQuyFkIvoAeQoKFRQvhFpQuYASIsIAVQvFajzNsZ4/KxpXnhxpGTW8UJZEbYgRJvxv8D+ZgAlUpECCf0r+LJFa/P6FFVCHJQwvx5URKGodyI/AUF3UgcFw

94CkBzesvEGWrAA3iaoCsgYyP2IbsB7Fub3gudQUHF6IGHFc8THFKtKGeVPUhBdEJhBjEKVwqJiox25MFpKINSZ3EKPJ4tIOR62EIAuAubykwuIFLQFIFW8HIFlAtqG03mKZEAC7FUN0bWfYsoOu0HnFQyEHEo4qxA44vfJk3I1p03NNJs3OSBixMgZw8AxARAvuAjiDS4qyCdA5qIXcRgH0AwoD6xKoihRnAG3k+1LwI4Un5YXjQL5rpKY4PHHY

46SDzCtCVn6UlFnBEMVqwcYMxhZwszA1Evr0ttN3A9Evb5BbMopMXXM5h4J75MdMDF2jKYpMJIiFYYqiFMQriFCQuBFcYrBFiYqhFMIrTFCIrKFFQuzFKIpqF+YrB5PAHrAQAvkylcNxpUAoGpdWLSs3ZKOBYULkJbJF6FhdQpFO6CsQ2AG8O5wEkABOC5J4uUQJwAVZF7Is5F3IrQQgVD5FAopHswotFFEpPompqKqAmABaAmqh4AhGwL6MgGaC

9AFUA94AMQ+4H8l8BMCllkqKCKQFClRyFrgqyDGxqyHiAGIDaJiEUjAHAFIAgJRIJkpOMpYRKVFQTPA69rJkFC3I1CNkrYAdkocltpKVBmFAvG43FEoaLI2FSoAPcj1ntF3pJ9UTihuJudjbR6nNU85oJmAACFZKU4MlwqOie5/eJe5g+O9F73NpRn3JTJEEyscNQP75TwU9hwksJxPwrElAIoklsYtBFCYohFsktTFcIoUlmYqUlOYuB5eYrRF4

/JLpt7WLFWEyIE2gS0wGFVWRHQtpstcI+AIlHrFvZMbF/ZObFl9FbFQymGF8XMaowHGxWzAHcO+XnJe0ZxUhBACkxdTgJ6VQBhlhUDhlWXJIhyMvwAqMrNQEIOLIG4sfaW4uYhayOox+4v3JXEMYx6TJPFrGMgl0Eoa4cEoMQCEqQlM4BQlaEuzFT4sExEgExlG0GxltD1xlTy3xl43Il6smPZB35OqZYEqHh/5MdQ8wGD6pADaAg3XoA/5EwARi

FigLQHhF9YE/g6iJLxi8LLxywD2YijAE4LaljoKk34QDcVSAyAqYhWwGBclou9olYCW4JYmXhrWOcFoNAuFXAMZoi4PYlXosLZK0rUZyZIZRqZP4lBzJ0ZIYtnxkQurAEYqjFx0pBF8YvBFU7CTFKYthFxQozFWYruluJMel6kvrAjjNelSklL4cdHMBoThIqxRiNEzMz+AQLPR57dJSlEgEkAWUoMQQgFrg5wDCBMkx5JvFhClYUoilW8Cil+AB

ilhADilCUt1JUpLlisdHKFgVH7AkYBgAM4F0QknRnl0bWFAjiCMQl3nlFj83X5YMsGFEMvbFNUtVFGtXrlUAEblzcrkyWlNYJflJm4MfWeh32S2YCGDnsOdRWFR+EOKo0P1ZIuBIkDEpiQnqiYBHQK8I3QN9l9wv9lcOR4ya0uDlG0oSUNnJe6dnMzJXDFYpydNElfwvElQIpOlCcpklyYuhFl0rTliItulKkpB5akrqFKtHrARiCxFWElNkBxS+

l3hKR58lDUG+4FXa9JO7iUXMx5ElnBlTfWCZtgQ/iWPyK0yL0RedQUigs7CbWdr0wGqRLYVkmmk0XgU4VCkG4VpCjQGQ7w5plPWa82uGhBpMqUY24v5pSTI4hEz1FpeyI65K+UxICsvwASspVlaso1lWssG6usqKZvMrhkgirs0IiqdOYiuKEvCuU0hkCkVK4p0hEAKm58mOllw2iGC+gBJgQO1ncToAoARiCsQGIESF2AF0QV7CEAhUNMxBsvwB

7iksxU4P4mV9GvlVstW0TJG5oBSANBFyhrFVwDhmQuA9KCzMzEOiMuF1oJ9lZFM9Ff8s4lIwyAVuzLopTKO2lNnns5UCsB5lnHDFh0ujFkktOlicv8wyctQVqcvTFGCuRFKNPzpY/JzlOhLUCbhPyQreIhChNJLlhVUR52kmpCN+B1RNCoryjJK6x/DnvAkYESABiEjA9wGvCgBNtRGpNr8aUsEA9AEyl2Utyl+UsdRRUpKlYouSlqyu4MgVCCA8

wEjCqAP0AjiB4AYgGWhW8At582Gm0SUrpK5UuLkjCo/m1UukFu8rql6ys2V2yvGAuyuYJe1JyBUzJAW3FDmZ8GEChiSriQOYSE00DBFcjqm7AnqmfUiwnlCCPKaqTos/lyoO/lm4P+Ji0o75f1J8RfosR8fEpqVoQoH5HxVDF+0uaVcCqOlCCvjl0kvOlKCrklV0vTlmCoGVHnJwVNZPrAXbKLFDZJiQAuhcSFUP5iuSsYW5CtUGNXKWCncWAhTX

SbF9CvFxlUrx5ULIJ5hRApB692ruhkHnijIP3ugv2wO3EB1Wa72Ugghxiss5Nh+LA3h+z4AUhXL0tVwGxtVZB3SMBRK5pUIJcRCirhBPNgple4sPSWyOFpDGPUVx4v2RDMtS03irnw68D8VASqCVMABCVYSoiVvuP6JCAzZ+S+1/iCPzNVbKDdVx9ytVnqrtVYspkxN+VnKUAPcVuejqlrPIIJHPK55PPL55AvM0AQvIaAIvPmFdpOwkrEsGwu4E

Jh/TN24E3B8SXk1MR1CqEJLYAo43soLC4oxLI5oKYSloKuFNoIR5lKp8FS0v/lQwOLZdKoESezNDlFbPDlnwr2l4SIOlHKtaViCp5VScoulPSuulGcqwVD0qZxOcp85kqrLpJ+iMBtcTNGeLOqRJcqMl7ZNUGUDDLcCqpJFHMz8ZH+KXMV6AoAFOAvQXNAAMapKZFByv4cDyvwATyoAFZvLeVHyqaAXysjAPyuHlEou7IY8vQik8unls8rbg88op

wi8uXl4YL+VE9WclcsXZJy3NW5UrUzRNqQBVDCs3lTCpBV8fJoJdUrA1EGsjAUGu1FMsIAwGFMCczM3+CXwBk5z8B44LkS7AKuCWE7aL5GyQGVBVmDQq3HCDpxKo/lprPXBbot/lxIE2ZAcu2Z6OMs5mON3VLKP3V9St9I0CtOZsCsjF8CpjF3KrOlF6r5VaCt6Vikv6V1jMGVtQprJz0orhj6P7ZpclMBUUIUpAGqf6+qJScirWoRtCox507JY1

OquHJfNlHJBqsXS/YmrgH4GPefU1CAK4t+B4GKS12qFS1ul2Gmciv9VDEMUV5MsJlW5KtxoathG2yIjV9uIyZQ3glpVQDrV7PM553PN55/PMF5CAGF5ovLuIDAwCYByGS1sxGiOeWsAlcc0/JmtK+RNTL/J61IJIbIo5F5wC5FPIq8l/IsFFfksz5MsJxap2g8hP6kAhmwtxkNwzQQHFB/UCPItEt1Kn60Ar/Qg2HkZTVUeYyBMGwKYMW0LpIUZt

wqUZOmre5ACo+5QcqqVb8MgmrsPeFGZN2lrKqPV7Kus1nKts1Ukvs1nSsvV8ksFVrmpxJ9hNFVRdJLh5iDeZvbI+ZVagswrcLxF4QhJplwDyM4VPMldCqi1a6lnZlAmVF0fCJ5s9PhZyY2NCTYgsMvclPcDLGI6GFK4F+YTtpfmXNZVOqOahwFdFFbn05zHGvxYOGu1+UXRR/g3biF9OmhT81mh4DMf5O6HGFl4sIF14tvF94rmFJsxFCOHOd5DA

tA57vkwECnLCGoBWqpWvOlZjMpgl4wBZlbMvCgyEtQl6EpV1+oXAFulSOkg/glGCwE48IlCtY7lX2UDNlR0BAOgYHIQtZYcwj0kc0mp9HLtZoKq5BjrNph0fPY5sfKkFa1MW6ncpJg4UqbqPcqgA0Util8UvmA/kvCB0c06ZwCzPwgTn3AinLD4LlGRcINV+AmwDjB/2Sr4sGE+mlNnO1meDflD/AVIrengwW7FEZD2pXVaCw4lnfNpVPEv9FvfM

ZVv2rCFB6oB1nKN9hMcps1bSqQVvKpTlUOr6VykuFVqIvvVuCoyFOCNLpFORR1W8zQAEuHVRVJMx1DMwzqqMCYh8Im84+OvJFdypPlwASmAQgBgQ2ACmAw8BEsa8tBlxOp1yfcN35ZOv35FOpJ5eyir1+YThRsqrjodykCSUCENB2w388DkTMKVeu+yW7C1cderuUZwEb1lBGb18GFb1YurSSLrQN1lvgMQUEuN1pusQl5uo5lluu5lx0NV1tuuA

5ezA2AApGvg+yizw3TU+mWVhQc/Oh8I+uof5zPPo6iGsVlysovUBis1l2spMV1usJqOVPV19us11vWT6pT6lo4KFNUS3wD4FZMID1dHKz1DHNEFKotD1LHPD1Egqj1CWC45ifMv11+tv1Bo1hVInMvg7wFU5rJDLYQBqlwZgro0CpHW0AuibEH5QQW/uGL4KKqRchAnG4ZoJaBJKo01rop/lJSqpVneppVoJJ719Kqs5/eqDFf3IjlDnKjl5QDH1

IOon156oh1jmqvV0Orn1bmpFV2cqX1sUELFoytVRlohB8VakKiVgP31LYD5omMNVKK/Mi5kWtBZATNkRuqri10LNVEEgEbAuEMaNxGL9V9ENhBLlJ3FluMSZVMqq1h4tpl2TGYxdWtPFEgDj1Cesilyer7lqeqHlPMqeozRukxukNcV2jWrV6tTqlViCOVGUqylbcByleUt/5lyuKlq2sWFEUlFIY9Okoik351hiMdIxevNUCBr3YFiLsMfsTdY9

PngcQGDehUhLgNT/D7kWrEfabAs+p3go71fsvKVgCo+1tFK+1m0p+1oRo+FZmtgYjSoXx0RtPVdmo6VkIi6V/KvQVLmuSNsOpsZaRs81XmvrJz6rbIfbMUShSBrpPhDzye+rQ8XpTFot2rR5EWprlZ+s7peYKqAPdAQA8rPXgFAFYMCorBZm/IoIpOqsS7+toqyHVXZvYxfKmJieNfmXupABqhB/8DNkpqn1MPlOFNfBQUYxthh5sBsnVIriJoJw

3paaAqo6sVIZZUrIwNWBuZl8EtwNFuq5lr9JyKdusvhdBqqou3K51xHSQpdBpskEUl3ATBql1LBrfZXip8VCav8VgSuCVoSpCA4SrNNQHKLcIHOksmdlEN5LPjo5LEtq0hrD5joUD18huD1HGtmpKhudZS1PUNTGBj1+iiZNLJrZN/GsWFIzWOF5Pjcan8GsUqzJ4463EVIdjGgYp3UjSDXGvqj1KFGjovU1LovJV7or+N/AIBNXeoCNgQqCNRmp

CNAkvjpQkuH1yWIiRcJrjlYOsRN1YGRNTmuvVQqpSNC+sPxnmrzlUqqbUojJh5tdMdI8lJ+lkTiuUhSABsJ+s1VhOpi5MWrbFeqo7FKCmVpuEMvNLRpJlRWsDVnRrK13Roq1dGN6NB5KPFdMujVjRPQAaxvSlJys2N2xouVhUv2NMxqVp0iteRE3JG1lTLcVM3I8VGtQQ1SGpeVqGs6Y6Gu+V3IAONlaIuAjzC8ZlAjWhrYHE1xfKo4CY3FiAnCc

UjfKXszOQU8OBA8a74mkcU3APcehXbi9spjJT2tKVL2uWlb2tWlwJsM1mhOM1OOMEl/3OHN8JNH1LSvHN7SuQV0+oFVs+szlcOqxNCOrvRsUAIV+gKjB8lA+ZiDHEovwCmV1Sj/gXBXJNbNFRRTJAA1ZRurlHcI7pXsS7pBxgxAqQrWA/YBgA+wA5NJlK5NhEq3lZ5p585Ov5NYYw51eRTJYJZGtmVwEpkCwAxZYOBaqUpAKQnHnwIlBDMKZFqR0

zOWicxEx3ItFoBq5/D8hIQnv5rpu15CHI9N8asTVPppTVfpqrgESp5ZpsxINwZsgwoZq11riX+ZFND11oDMbGjLIgZqPTZ5Dapa1zava1nWsDNrlUKyK7HsiXpN8kGFA0wlbm5qRNBQc1VFQcyphSSZRS06sZvJh8ZsphEVUUNCiMoZAKlUNaZqZhcfIYZEEoL0llpQSNlsPG5+vwB7HHgY0aTh4uYCU89kWwIDVUoEnUqciDspIIM/k482tiJVa

ig8NLZo3BbZoWlq6upV/gufhzwt7NPFv7NYcv4t4RoaVkRsgAY5q5VE5vEt3Spn1aJuktmJsX1nmpGVxUKh5fIgAwLuV7xsphQcxRif4iHi3NQuKA1U7MqNFUsCZNRs4c+qvqN6AH7AQgBuQ6G100n6zGRVNrZQNNqGJ+WtaNm4uK1QatK1bXnK10+Uq14ar6Nkao/NmiqoG8FueVKGveVyFow1WGpAtKCkpt1NvK8dNuG1bIMrVseJgtNau45eG

onlU8pnlc8t0QC8qXlK8uYJ9HM/QDBAU1UwkeNzovwtPnUlKQBprRp3NWCZFschdYvMwknN/GNFqYSANUKQDfGYEyMR8NH1r8NX1sixgRu3V1Su+1P3IhNf2r/ch6pH1o5pEt4NrEtU+qhtklphtt6tH5HmrktKtHNyyOvxNHzMYSgUK+A9o0R5+mHaFiqo/8R8y/8aqobFDUMPNhNqx5s0qLyRrRf1cXPqaU9J9GlOsFNiLI0wHFBoSxtQaR7zR

HadbH4mG9nCtYuoJZ5Am6ZjtrdM2rHr5nZAStdhUhiT6j0sqVrg5bpoQ5bBt0VHBtVlFAHVl3BuMV7gPatbHTgEpVr/p8DAqtpLDXcaSBdNy9vStq+Ea1TVqbVbWtbVHWvbVXWsKtxBql5ghsNcs9jpoM/SGpJHKGtP3h95KDmmA41sCqk1v911rJmttrLmtIwvmJGJHEFK1pWpa1o9Z/DkIA8YXOAToCsQ94Gkm9JqVBBgprFOgnG4pgqNFrekO

t15hOGw6M088pBYEwVNflUhIU1RJrh4/0oQQb1pDprFuHmpnP8NlSpBNjKNDtDFIHNwYqH1kcpElU5sh1SdpulMOpH5BdPRpiOsfVWRuRtiApuNWqPkohou3N81G5iRwGoEB5pBlWquPNxNqbtLRiGoSXO/ANm36iHUU2eU0H8g04pguuEKMdGsDQAGzwVglUEsdHAGzebAHOIUTJhxNXOzwdXMuADXISZ40QNVWTBa5duNXE7XLmmnXIUk3XMao

tjtw+DjskWzjtcd7jrKZkeKAlo2pAlfQVgdM5TpGGtXmAM4FgMmAHGARiBnA8wEjA4UCFhiQBilygEBh7AE7VSoJmZkwiKab7W4ElcyjixfBPmTAILCmwAnkTxKBAv6EVwNoM3wv6gQKbYGON2Y2OGFbhuFdvWRxr2o3VvoqDtTsJ4dYJrDt/DrCNgjoiNwjpWwx+AQITQCKlMAFYm25XwAM4AQAzgEcQq4A6AU7EwA+AF0QgVFZNbyCmATQGFAB

TtWQkYAMQSEVIAuXHn1qktktuXVSBsUCgAmRqRtU/KwkUAtWEG5tNEZFjbA19FxtgGtX52jqPNAwpPNzltqNZNoT5G1pSYmoEI2BvKN5JvLN5FvKt5NvOwdOND0FWiO0topBMFikz9YWOuKBWSq5I2wmUyRAnQqDsrxZpGIswzANoBc6oKVXsuuF2mupRems3V8zuCF/1r3VgNrWdwNo2dd9C2dMAB2dkcH2dZMCOdJzrOdSbEud1ztudfKHudjz

vgiLzredHzvnNXzvht6doyFdHkIV8cV25AEKbSQrBJpAun5wdGi0d2Dlrl6AAxAM4B7lTfnyujkr4R/Dn7IKQCV65wBOybQF0QvWNrgyKHvmcgvNW2GqClEgFo1MABW5a3NXlZBKfmDYNY1wKpKGrfTBV3HMddzrsCorrpalS8INwOEg8JXNFRtzmNdJrBQo4A0oKBwPlwp9AJ0m9wA5oFctbR40vcNzZq/lr1p5dumo4tgcp2Z3DpDlQrpM1Irq

hNCeHFdmJEld0rr2dzQDldxztOdcAHOd/mGVdNzooAdzoedTzq1d8wHedsNvc18Op+dx+JtJq+rGVjpBV5YuApJtajYEoIW5c/0rqxRlppNcLprt0Wr0dp5uRd55tuRk4pWgHOySgH4pcCObzB+gvRHFhkD2ybb2Ko4TNfFL7t7FFB3fdbjsJWn7t/FP7sou7b0SwN5vkVd5o6Nyip6NfNrfN/RvrKQxpjV6Lr15WLuN5j1FxdlvOt5tvNMVT1EA

9yWuA9t9znFYHtvEX7q6ov7qousHvmNLiuAl0FtAlsFrqlPAFIA68CsQvOHhFygCsQM7AaAFOA0hh2SMQ/YAh5RxKiVnTLbAz5WY4gIRuG09sL5t+JrdiMS51baLhqDsufUswE5IG6hiEmVA5dnAKtB3sttBzFqmdvgvXVzoO4lPZuDtoJtAVtSuxy/2qEdbKshE+AGHduztldhzondiroudVzrndC7o1dzztedK7p1dGJvXd3zp0BOm2XNfnJNA

9ei0CnOibSiypLtWjELlknLaxeNthddrruVqXEkA1DhgAbcHjKbrvblHrpnAXrqvQPrviAfroDdQbr5BWRO9Qsbrg13Blrg9AHvAzB3CgPAFMhuAB/xLUQxAjEX0pygCuRAUv+V+pK7ht7qRdpNpgdE2oWJcst642XqEAuXvy92bpshqYK09iMWb1FCRad2Yjk86zBMBeLJgKRxorCVkn1wBYHcZeSu0YTbrJVLbt9t/xrKVXZq4d3Fp3VPbr4tg

5oEtjnsB1zntc9MrrHdHnoVdU7qVdPntVdcAHVdS7sC9q7pTtUjvRFiOrHqO7uyNHFHENuGXpyZJuq6qg0eUchmhdF7uWVFRtr6w3uqNsWrG9UMoxl7Nzo9MHusgUyxNglEHyczMAg44TPK+UADQAhPoHwyL2FApPu/AyMApglPo8dtEPg97RqUV/joqJz5r3Jr5pplAtoGN9RIw9X5ogAHHq49PHq3gfHoE9QnuFAInrE9xHpimBPug99PpJ93U

FNgLTgp9PuOcV6tLSdLHoydE3vAlU3vQADQCMASDzuAmVR4AOIPs2UyGUAhEy61R40wlMKKVBQGEcRXjUzw6VFOtbvsOtdsrkJqDjk1XHC/g2E18kkpmF05oOD9XTtD9zEtHRvQLuFbFvM9VFO71VnoWd3bt4dYCogsECoc96zqc9ORHe9o7oOd8rsnd07shEs7v+9gPs1dwPuC9kjqGV6RrTxxrr8GdikPdxFkCct+lmE+duX5kQxAhp+olSndG

BhzAHuAMSIK9wBIfCjXua9uiFa97Xs69mIB69woD69YbvtddRkGKzAECoRBi8ViGnwAViDgAv4TwAgVDWAFGqWxVGpHlS5jrQ6qias6svfCjUpYmtcGIAZ2yglC/sy9O6GUAdcFIApvPaAGko+AtcEPQM4AXqbABxAMKtKltyt79O6CQILQHXgzAjS4M2GRQkgE5hHVGUAFOEh9gAcG95BNzRibsbtzCqTNqbsT5bAH79g/pX1u1IMNhxpuJh3XI

N61W1cMnP50DpPPtdgIA1ZLTEqpsnNc1yh5weTTjiw8nzIouElIN+CHi7eo7N13s4dXFt4lwRvT9dnrnmkdsEtOZLz9mgG2dbns+9Rfq89M7r+987rVdi7sr92rrXdqRv1dm7sR17blcJ0Pu/tTQKUdnjIR9BgX0w5cqoVgMtJFVdqvdmPqqNghNG911Tx9xRGlSITDDxrw1uMwPxqACWApOpAEwgdPuaQ4TIgxbju/AQ3KyJoaE8DqKCxWfgYY9

MiqNxrNoDViHp59AtL59NuJSZqHqF96HrXE9Wuvi5vuYAlvugo1vuHgtvtig9votUSvvAxzgeCDDgVCDb6C8DkQdV9/gcY9evqgtSxtVtKxu45woFrgN/paAwoCMQ5TiMAMAC3gzAApw4UAaAUwEkAhTsUtEnpWKCwsrRlBHXcumVNBFLErdiTJh5xxoQ8MtgcwjqmkcOYAvMNAKMN8/XOF86sKVRnuXVcfue1vLvbd+mqjpggb7NwgaZVO0rEDL

3ujtBjJc9UgaldMgcL9nnp+93npVdSgYB9KgYC9agdB9tfs81qgONdejC8m+pEMDUUixtzlK21truJ04brhkToHiAdmyuWBVo0R+yuo1LIuX9q/vCg6/uaCW/p39uAD39B/sz1y2KRDa4hSAqBlqA3UHXgtvOwAygD6EzBkjAh6GYAK7uHlzGu1VI3rY1ybuWNmhrRdKWRRDaIYQA6ar2tnTLVhpwErA/wG6Qn8Bk5WVj2Y/pSWYZ+FoDUlFPMEV

NL1iuGM9J3taBzoubdWmsu9vAYT9gJve1nbru9IdqWdfDoBtT3qBt5mphNXKNeD0gY+9nwe+9Jfo7kigb89QPqBDnzuwVYXrWBsUH692kp81iiT9UWFBOt64UrdRwPEN8EiJNCId1aOjoRdPIaTd8WvJtmTgMA9EBXSHcHXwTgAy5TKCiDGWtnJ/RgSwmYYQA2YZmgQ3LzD9QeiDnNtkVcQYQ93PuDV3NvGmYatSDgvpq19MrF9HQa6DPQb6DAwa

GDIwbGDEwbKDDTnTDW0F00WYYzY5YYcClYb/dDQeSdEFqVtX5PAy/IczNS5nvAV+voAIjhJgbAApwNRxxwpzucAw8AqFRBLlFUwZPGsKO/pdLQtUGZGb18ofOp6oJWZ2eHQojqmeJPFHiQMQj/gnPnYBRwa5dS6smdgE2NDN3oEDveoZVdwYH1zKriaUdpHNLwfz97nrkD3wYUDvwc9DqgaC96gYXNhdK0D8lswAkXvPxIyDNkdwCd10Id+ZJNKz

wwzIAwFgfxtnWOADVQApwDQGe2tQFWQkgGxcfqNg12Id4sp/vVSIgAv9zgCv9bQBv9d/sTah/r7qlIY4A94DGA9QBiRuACFF8AcgoA9GeS2AGtRdXr1JKAcVFSYfQD7GposqLpN9EAFoj9EcYjRPnFDWiL8tvHE4ZuYH9pJOv25CoYsMcwdCtqoYYBMwEW0MDl/pUOKkJz1v1D3hpM9AEYuDszoCFDsN+t93rAj4dsH1/bu9hzwf8wjofeDzofHd

rod+9SEeUD/nuXdIPp9Dd6sXNBrtigh410DyNrLww0iC1oTm1srcSgYtfEFxMLvKN1dpsDRNux9d7tx9LCsaoZq100IivXAdHqbWjUHrgdICnEjKG4g+YdwhdUY4VjUcouzUaq8bUfvEZyE6jVYZXFPqvXFnPrJlHNrwGj5sRByQaqJAvt2o75uF9tWsyDwxvQA64dTxW4Z3De4YPDR4dWQJ4eHDOlPXA9UcJeTUeHgLUbim7UZ/WXUcVtEsuVtU

staDAoe0jbAA5lkYAE54UHmA02AF5bcHilK/uEsmktqdS8NOkvvrmANAItUSsP6p1qhNG+vk2DDsuhSZBqJN9JFo42wnr1nssM93LsNDHiLbdPke+tW6tT9IComB9wbqVkCrtDINqHdbwZHdcEa+DboeGAHofijXodQjwIbTtmEYzt3jnBDUmr5oxIrSsxEY8Z+nO2E8jCrll7oy91EevSkgHrANOFZ5L9sxD3JJH9wAWf9EkTf9bQA/9zBm/9v/

v/9D/rFj6ACKuqyFIAUFH/5WXH15CADaAXIq8VGIGHgDIqQDR/q5Dujsqj9gcFm43pllQwUIAEsaljTQEd9hkY25NxJ4qqzCNh1ynlDRsusjyoYpY3ToYBLMgWAeuFYI5BsetTZtXB7kYpVZwbYduMYs9XfIFdrwoe9tnMrZorvJjg7oij1MdkDtMdijvnsZjKEaSjurt9DmgfC9LLiDDTjKrh0Xq5wTASoRiYMjDP6qzw/qp/aaPv/aGPufmtgc

hZ97scDOsaEAky1uQ8wFd4IbGlSz/vghNXsje4cBnD9HoLD6MokAdPBHjmxPHj6gDrQnABuQM8a6o88aJ9LNtvNXPpK1s0a5tT5p5tL5pQ9bYbPSIvvWjmHt3Q70c+j30abliQD+jiQABj94CBj0toacw8e4gXgTXj8UA3jU8e3j5q1njhkD3j/7saDFTOAS6TvASWAcFDsqQmKzgH7AFOFwAM4CiAiQAxAMEV0QPAGiA9AEmDC8OmDaoiJNO8Jw

qrTvSslkfvDsMY2Dz4aZdbmMBAX00rCEo0ZY+noXVRSu1DvxvetV3sAj/AbNDNwb+tgUZWdkJrJj0Jopj+cY+D0UeL9xcfL9AIcSj1frbZrMerjALp0lJYsjEMQkjjZCoLwOlsR9IsSmEXkwoj6XsRDi/swAPACvQz/t2hLvRYjWIeP9vFlAD4AZ+AkAckeCABgDXMKugCAa1jgaOzKh6BgAKQFsgc9FqAtcC559AApwXeXGAHmiZOnIaG9fcZ5N

KbtGFtBJMTZiezAeZptYojNOA8jiIEeBFOtVkaVDiwY50L4eL4QuG7AJgKO9FwHr1uodJVmmo8jKM3bNOMZmdqceT9fkes9izts9JMfs9jwZz9r3skDToYL9EifkDpfoZj/wYSjVfrQjertSjbMYyFRgBwju7q7ARqh/UmlqPdrccKNvmKOGHkQrtQMqsDbNlBlbHDQDO/P0d9w07FLF1k0UQYBBqTCGJCKDqubbE9+LQD62E4oHecZyrDxydRQE

F0SgQBEuT1ybg9hWqPjM0dXFtPRUVLYc4hy0bQ9gxtvjYvoQTZS2QTqCfQTmCaOwOCaZD+CeuRz4tPWhyfuTg4H2Jjye2uzyYuTP6yuTRxzLVCxuY9LQdY9atsT5ygDZFKQEPQjiA0A8QFigoSf0A2qV6DL4QogwMcW9OxU5cSwkp5YmssjGJhcimFprMVoKcUDxv1RuRjC4ZbldtHsp/DmMb/DrbtqTSfu7NDScJj4wJBxIgY9hbSbFdufs2dVM

fETX3skTPwZLjAyaZj5cZC9GgdGT1cYlVYfVOxRXUUS9Yh/U4XACGtaih6xRlTBeoLXC4WvR9tJu1jEAC8lZKx/xmgDJDbcvljZfWpDkMLpDDIaZDxwF2ybIY5DSkesT/DlEj4kaMAkkekjnyTSFUwHkjikcY1FIcX9usf1jWwGcARsfOAJsbNjJMAtjVsZuVGacf9VQAFy3id8TToH8TgSeCTpAFCTGIHCTUaZw1O6AERQiJERYiKjTtscTD9sd

5DKYa0jU2okAnqY69xAB9TSSbqiPkgu1Y8jwk8odxkbFGJZRwGVwQ0t8h1AmtqUcSwojZuXBZ3oqTicY9Fvhs7NPCYM1fCYCjloYz9hC2e97SbCjb3o1TUUa1TvSfdDcUb1TZcbkTFZNTtG7p0BDGpelK5uLmfVObjN+Kp5JNPGdUPQx1QRJFjsXgTDLYu2TkMpqjVQAgu2KaCe6uO2uCGfU+B8amj7NofNp8fmj58f59l8YBT6QaBTfEMsqpKfJ

TlKepT83jpTOOAZThBukhmaqjayGbeTkCdSdzQarVz0dXDvFk9d3rt9d/rvOAgboQAwbpq96FqzIq6ZMFkOP8G3UqMsPnFFItWN1EquF5GdBBXY+drWhnDMf4rJAZyPmJsUqQHrEkRHzdRAnmlrDoPTfAYDtlnrlTgroET1oYEdIUYJxHSfVTXSZpjMUZ1T0icGT3oYrjKUYwjn6ZSASidjqYBgJN9carmtjF8k0IZmVwWsykF+lR9Xfo1V1gd7j

1jCysMaUjjgyn7TdRrct3UIFN/ozXZimaKQymacSeKIawN7O6Z2mc8IUHL0zS9qbG0uuRBGLv15hvNw9pvPN5BHoJd+9v5ZXVOENPlW11lVvPt0HJTctVr1N6oQl93HpSAvHv49mAEE9wnpJgonvE9arNoF3Y3oFQhrKtIhvRRYhsjNkhpQNoDtJhU1tkNU1uEFChqdjw2jD1qZpj5q1uj161u0jY/pa9bXqyJ0/u69rJrn9gYfNpWCSz5EzLQQ2

gTwkj2Zk536DOJ0GBWRRTWpkt1KyseRn504cQMwUhLwyVHBZKPJDrF+mbzZhme4TxmbTjKfrMzZ6aVT0+Oz9qqZszErtvT3SfvTCEb6TT6Yr9gIeZjyUffTfoafB68EpmSltOxvmdxpthqIBQ7LxFCXtmVwsRLIy8MT6cYcA6kGf2YddsVI0SeFmLdqXZbdrSzvY1hmq2i9U+9IC8ymR186muwoZEvNcRwF6h4lW3ZR3u1cMQL256UjGh5HU6BBC

L7kJWbqtZWYkAvWal9MvqGzcvoV942bF5k2e9mFpqPtQrNPtuuovtNVswF7SUt8Zvot9awCt9NvvrAdvod9DWemzIZoRMtUN3CPLkRZq2ga4MfX50+ymip4us06q2fAdAgsnGCZugdO8uUNS1r2zkeoOzGhvYz/DhXMb8bxDBIc392/tWQu/v39Qmf5IjJAREJSAJM1ijYcjHHQEEpEJh6Sp3hRokRifrGVBrkbnsdtKE0pwKYhUqfYteMcDtcOY

zj5meFdNoZzjIibzjsEcLjDmcQjuqdxzsieGTlceNTawJJzpqfJyBgN4AqluIB6MCNhGiatFwXJ4KP8EU53ZK7jTozdTVHhwdD4Wr21S0mKCACcI9lr5Ys7J2qOPocDzdthZH+sP5Po2cAs0oSADeaO98CkFxXUmeJWTW6QcrUYtPlI/zauFb5plnyMF/JrdEwHDiz6ifD4edQNeY1KzK9s6SOQbyD68AKDRQZKDlBC9z0vJ3hdinpo3YEchlgOP

tyoNolCCH9KTmUvtyBevtcuk6DxAG6DvQdIA/QcGDwwdGD4weQCuBY/tlubDN6KPzA9EPbAeBAD5DsxkqRDJD5tHI2zQevjzIesydu2bY5i4EkFaeaOzQ6fQ4ep0vzWkq9jOQKqotbrtlMpWcUMnPb4qsNIylVELw7oxutK8No0rAOhMXTtcjO6a8Ne6eqTVKJTjMqdu9J6YtDzSfAjDwcH5Twegj4UbHzLoe1Tk+acz+qdfTQlPQj0jrvR68CJ8

mUaBdQtEhxYUNtTxFnbiGVmGZpqmpNrqaizCbsRdiWbJtDw37EX7qSJ4xOgg/kDc2mHMYan6UnECYEKLBIxKLqyDKLq4trDh8emjmGZ+TyHtbD+GfbDn5vmmmeZX9a/pJgG/qJD+eZJDhea/jiWsqL1kDGJNRaH2dRdxTTHv19BKcN9zsY1qHEfP9RiEv95wGv9t/tIA9/oxaABRwl7wAdJbrHv0tEq2KRljrFJCRQcGMKKBvpLws38DSQj6mzEo

rhu52BEhipeq1Yxhi7zifq4lsOdMz/eYRzLSdED3havTvhZvTdmfHzgRexzU+ZkTQyZZjH6YXz8QC8zkYPJzqlrmDU3AXs8XuMDSqsUYL6JMFLOZa6jIp4s/DhnAwoGYABiCpT2EaMpkSdvzjlv7j1Ucspz+fctPTWsyH8HYoZwHuLltX3ATxaBqLMjiQ6LO0t7ODqwcpuL5SjCh6G7NIyRRi/1Lxeehg7S8a6vO1NV9OYNtBc6EaBZdz+QbdzHu

dKDfBseaAhogFXAkyk72NF1puPeavkP1LuYHehrOWWznWftzFlR3QW0c3DGIG3Du4Zsl+0ePDkgFPDE2aKt79t1LPBej8fVP4LfpUELB7pjN0efELggqBaUhc7cTHOTNSefkLeQEULGZuULi3WJLpJfJLZtNPzNkKd1cY0EL0wmoEEmfoIO4VVhySvYDD8H5T5ZtAKVHGfRgEM8ak0oKzM0oBqdgZ4DNSe7zdSdlTGjL+LHhaCjEEZPaA7rVTaOb

BLARYfT9MZxz0JZczhqfCL4PsiL+eIb93NACthqIAzXyaf6EMV8GeYTxLVwIqjdgZyLD7qqAjYHm8BACTgZKwog1gDEA78Ewgl0cGjTRvS8e5acgB5acAx5f8gZ5dajaGY+TzRaQ9C0aFp7Rc2MK0YyDRGeRo8Ac4jizzWLPEY2LfEa2LOxYExsxsvL7eSNe3IFvLH4HvLV0Yz1uvqgTcmIWLsCdiTdUsVjr/pgA7/vrAn/vVjtcD/95yCEzfpTA

YlYGVweYAOYMnPOLECDZTZsI8JTikIBkcVpZKvKVMN3JOAbFDpobaVL1wcU8jBkyMzjwt8jbZYDFmcfAV2caszFmqc5oJcijGOfgjdMZvU/SenzMJYJzYPq85URaXzN/mUtq+Y31ZmAbi3QJ5jJcsSoo7OvGRTVxLLqe7jx+Zz6uYO0pEgDgAcxUa9gQHxYN+drtZlL3ZDsfaht1QZLKWY8t7dqLYhAOYyvFBFGGKPhqFHAp0A1JQcnJDMKjFcji

zAuw63mMfwuzA4rJZG0tTLTlLl9JkqL7JQLk1hVLrucKD7ueKDnua1LKbTfp3BccyHOkAQAmkiIBggHkUHLz4cGAAw1Be1zmVbTYD8amAX0Z+jL8f+jE8o/jQAtftNuq9LFucwZvBcFY9NDLmLQuELIc0jzo1JDLjszDLNRQjLjHKUNshZTNsZddZqeYTLyDu4MtlZgA9lYQAX6csT2QJlhALIcy5bg0w6mCuJddOWY0ob8yxZfkzyiCUKe7Hsie

hYdF3TCr1U0p9UdZbmlnxZNDnFt4TIEaED/xc8LpMeRzucd7LlMf7LPSaxzj6ahLzmfxzrmcJzVcYXzjvpiLyFSF0vauXh64SDpwWsUdoGaWV5lcyLFBOyLyYbqNGTgATk8a3jUFZPLkdCneNcBcABTg0AcgkzKS8dPCE8c3jD1CTg/kGao87s4AGkI4wDNZiDvqqaLGGdfLOGZSD/yc/LgKZvjP5aqAmFeVjqsa/9P/oIrmsdGLEgFJrrNavLcF

beBXNdprvNZrjSFeYz0CYN9aFcydQwVsTEAcbljiecTcAbcTuxYtpOQLoyIC2ehkwD5oxUcSZypi09B2uY4BYiZdp5l5LGeDlaJUVcjK4JuGcSCeh3pPONjZacL0qe+L9SaErfeoHzvbqHz4lftDvsLETd6dkrUib+DildHLNfoUTiNcRLaExFKFOZUTpNL8UXqi3z3tDoBi5Yb4KbP0TpUZMtTJPFD/CLQUbcFwAPACs2lJZUjnJo5zTFofzjsd

ctfJq8rTJZ9GgcVFI0fUjjCnOjSlbn6QNc0yzNZnI6m3MCyI9d9rO4H9rgmruUTsteJjDoKB0NS1z3WeSyTudyDqpYwL6pfyrmpaINfVboFeBa+yACDr447RFw/Op3Y2eXr0EIT0KOYAare9fo6oKaQTKCbQTuAAwTWCZhTeCa4L3pcGrvpb4LI1cfZQhfZ1IhaD5/AtDLsedmtkZcWrRvqBo8Dv2ziDsOzG1e7IHAGbrrdfbrC3vMabDnYr3AOV

BeRjqwBheeJlYUVw1knjS46vyQLjQLdgdHNlDGlsL8cfO9Bod4r9oMPTMOZjrX3KS6VocHzlmeETPZdRzYNekr9mYhLUNeCLL6dnzbmYiLKtAwLkyeyNmFFUpgCD3mkOKUpm3KqoY6pKjxlo2TbOa2ThNfUjfIYeB1TE7EMUA5hb+2POGUdnJI5Qsbciw/A1jafLbRpfLiQd+TvNo/LtRMFt4Tq0VptfsT5tegDsAdcTiAfhTZiogAdjYKZVjc9e

2kOumyFclly4bYziZf0U2AEDTtIbgA9IYxAjIeZD4afZDg1luzsKPIIioa6BfNCIRLTuISGVF0ypgmw61MgZso9cO9pfH1RtDd6GWnL7apsjXY1KnMFRuCTjUOe8jLZdcLf1duDANc7LXhZZVPhaEtESNTrMlaLjjmczrI5dhrY5ZGT7mcRr6le8zklNUtnHgda5dbPwDqeLN1alrrejYgz8Lo353dffmxjZTDyWZspK7P5ziLLZI9xfRh/aUmV4

uYOkuOmaUjkK3pZ7OBwtTd5o4IXqBPhD10fsQp57TcQYnTd3rWAvVCXYYYLPYeYLfYbYLg4c4LhVcA5HVsPtoDZqSZGFVBdkSLyIDqtLsHJoLhuokAJKfCgZKYpTQgCpTNKcoz1GeAbduu5qPhCh6UHO2G4IWNLVfONE6LferOzGDLKyXWzQgvmr81tuxKDbkLEeoUL6Zv8EWDbbTYkbgQ8abWAUkagAMkeTTqaaLzu7nyMgVKfgTlpWDE3AqbEU

mVwNkn5TJoqRcKiTYoI7I0zH6mBm0nt3mUAtRMEdemdzZZcLwEf8j7heJjgNdaTQJZRz16c6T4jfBLg5fkrw5ZhrBqZzrcJeJzGaO/TeJvmoqlt84H1TQctObIVvpQGpz6kAhh+e79ZUeizzlZx5iISJrZNoubGISubEs2LcALPJoP8DIrMsxLNTzbXYLzetNxSHANJovIk+4GtBmIitYRrYXsJrf/gZrdBbDufVCdpZ2jTpf3DQgEPDrpfdLpuc

9Ll9e4LKLa101zBZbsvKxbplWtLP0PxbJGeJbpLYozOOHpT9YEZTCLbV1EAupb2tidra0Lb0j7QMERqloBLMxcit2sFLvurAdHLYgdchsQbC1YWtiefxqy1vQb7rMm1i3SzTBsdzTTqPzTpsf7A5sctj6FsqpR8OuAa7nvMPdeLd5TYZ1rJBV5MBXLxxwslwT8C4BBrZO9bmOgQnLhrRRykRiX1aAjv1dtbNnvtbwzaBrKqZBrojcmbEjY9bPBgU

rczZ9b8ib9bxSJQB+dZ7Z2du0r/aVUSejAxL1YpmZqmVXL/jOpL3de35MGfpL4qRfzmbdHtsM1ml7caRR0HYsjoUk9UOYGmE5sPxZzJcg75YSd1FFk6BeugQ7HlISkiXkIm47Z1NGVaVL47BarbVefjr8ffjn8fPr/Bo6pV9aHbelRHbqResaf8HfrYLeSyBLaJbZGbJbC7aozS7ZozfbbftA7YgFxbB8SGlozIzamO9PlQ50iVlISyiRFG7LYjm

57ckLceaQb17aWrMZYFbcZaFb3cBFbFaa8TPifwAfiYCTxJHrTjaebThtvkNxtt5ilHCbEZrJezlkbVboHaqbWrYdl4MZAW/zK2A+VKIdJ3r9iV9ArwpoLd9HKc4bMUOhzAlfxj6ceEr8dce9QjeBrI+dBrhHfdbkNaHL0NZCLsjfhr8+f9bOEZXzRdagcTQMWUIlHi9kbeFiRwDSTlcvY73MxHpjlu4728qfzfHcZLPlNhmSUjMjviRtBqDHwEk

nYh6UVD8kZbY+b5Zga7A8kswoecch55Ha7T/E6G5HUkNzbZtL+SOkgYKZ/rkKYAbuCbhTwAvVZPnYGrzWas7aLZs7Y7fs7Lbcc7M7Zc787cXby7dM72pfM7ghr87Papaxc3AQNBgmLyHFDsYTLQFS+uCi741Nmrbbmz80hcwDN7fuad7ZTzGDaUL6XdgSGBYxAl2WFAPuM0LMsPqdQKSKaXlOLtFxslMUILehosSXsYcZxRVDqOphKtKT9DvlaId

f7SQuB5dJnMd9PeZMzsddAjQzcETEdqdb+HZdbs3ekbeOfI7b6ZUr6kpQBKzbrjlOZWRNaMSLyHnITHjLLY/aoC1uNaPz+NdQD2RZTDGThid8wHZ2IHrqC/kCA9xtySdIxiZrPHL65IfZnF/Yt2gEfbI9Ufdq97PtgKCyNq5B7l8dR7kSDTXPSCwTpFpbXOj7ovvZ6kTp61TeXj7ofYo9CkBT7aTDT7sxaaDBtdQrD+US7vdaGCmHD/9guRxwgbv

gwCSPJTViAaAz/qvQK4vuyhCdwdUCE1YBSf9KmmC2YRAPZ0JFRzqPOFurNoDshbGmyjLkR4rJ3qwoOnKyaxwF0LXTf3Tftu4bA3d7zvxeG7RvYszqzqTrFMcPQuiFwJzACIgiwLvScDUCoBgFrglAn6xkCN2JjPopwJkE0AW8DO2CGjbgwoGom8AHpwsJaJzVHbrJtcfzldaUmAo/WLlWluut/MbVwbsRbpZld97+jaObG8qMbOyYwDmkc413HJn

AvRlWQKAJxwbQCgA5uWEgToF1tfdJnSaaYIT54aVBNHF7g/BYQwj8HuA8/f+lZLqgFTALHpgfrDoRRK7JA0K+AXpJYTxwaxjvXfvh/XZ9Fglb4blk3BNxveCjwjdCjIJerA9/cf7z/YoAr/eHqH/a/7pXBSRv/aEA//agAgA+AHL8bAHGIAgHC3dt7S+vpD4IfFwF/DmTLfrMLHjMFSGjvSLeNdFjHiYJ8jiGFAFOGVlxACvQw/uZFHEQxAsUFig

PEUPQbcGEgHcFigSqN6cHAESAmcUo1wkcX9/gMCBwQNCBESc7rUSaqlJjcJTbQcT5UgcCHwQ9CHBDak9ovlnrUMxFG51e9oCBrINLiN20vjq+TFom2EUSU5IEmt6Qsce3TbDd3TLDshzJ/f4r8g8G7fecv7HZZUHXZemqEleyU/mC0Hb8Z0Heg/f7+gE/7z2J/7UwD/7AA6AHpABAH1g9sHUA4RrxOZo7UXqFoXFAvMldbyj2/cS9tNm6QslO97a

XrrrOA+vd3Ib7Tqba3LEgFfFqBl80hmhJ6Q3NigmgATe8EFWQsawWQ3IDKErRzr2TrPUgLmyZQFOCleE4v6RbUX00fmn+HDgUBHwI4+QYI5/AcxCCg3EGhHxYFuQVWwRHpK2cbbNvvNwtebDHjbFrXjdWjHYfmmpA5gA5A/mAlA+oHwvDoHjiAYHHACYHoTZI9T7pRHvw854II4xHQI5C0II5xHEI/xHTawggRI7hHFyFJH6Rj1rkFpb7rGeKHL0

ZUL07AMQ9QHHSJMCQZb0X0AGICMAsUC2NgVBmLkKKsA0KOwlOQPJk0mf3w18AZbPA8B84NSJoDGkolIONII0mr+ATQOfrfQ4YSno4yoLiLJoJSbQ7R6euDAzf4TV/cEbN/bUH1mfN7kAEWHT/ZNjug8jAb/YMHGw7jhJg7MHFg72HVg/AHbyTsHIIYNd68BxNcA5XN5KJbRxc3NdbZMWTGvFshDkU796qszBFlclylsccQg9QxAcBNljTkujT3Bg

MQkQ+iHRgFiH8Q42hSQ7ggKQ7SHQkfdd3BiDhFSyaA3WHGAtcBzx+AAyGToAMQsUDgiPVanHhXu4M9AH0ALQDGDW8CneJuvIH/ZGUAXIoxAUkd7bA3ptjVJcBV0GbO7rPeNrGtVTH+Vw7HaZbMtsKI4obfBV5Gg3LC18rYJ0HauYdWF7tpFt8hZrG9HEjPRjNZemlumdYloY54brZcUH+7S2lAJeVTpvYm7ojcTHyw9TH+g7WHhg82H2w/MHuw/2

H+Y8gHylaLHYydpF4IflwvJfex9OQKNultgK03F3C4WabHfZJeH5UaTbbJAbtBA40jYGJxGFQcQ+Yo4LWjAEwgQ/04ajNYvEQk9d4Ik+9WEk4YaDRdiDgtcpHbjbaLtI7SZ9I66LnXK1HOo68V+o5QlRo5NHEg3NH4FdcYMk8xH4o5S1yx0kn84fFlFaqXDVI3VH6ee4MJMF0QtcBkA+YBaA4UB6xygFMTW8FcWbQEjAOsqZT+AKIRkKlUSpLBx1

18szGo2DjoxZtX7jpD+xkpUsFALINhL1fFTi6uKVMg/j9vTetbGHcaTafqjHCdbG7eHcwn8Y4MUD/aWHyY5WH6Y+/7mY62Hpg52Hlg9AHZE8LHudeJzsPbLHZw8f44pRxriqv0w7wFv0YRECz/U90b4GefzPOUPQ6YBQJtcEkARg5IJrEd7H3ZFnH/YHnH6KKXHc4FXH6483H7iZ5yW8EAiTQH7Ap1iY8v/PCgkgC0BFOCRy+AGfgeQ/jdBNbUjf

E6KHixbY93HOmnTWE4i804nT61VFIRyh6tdkVLNOYir55EdwZ0nIRjBYHk5JYmrU9WGerIfDcj7DcqTHCYMzIw7kHfLrmdEw7jrxU9G7MY/G7IjYqn2E5qnuE9WH6w/qnxg8an2Y5IneY5sHBY6OHS3ao7iNuUTUDgBsAsXwI9OR3zSDjCI/tLdYh3Zpp65dpLj+YMdaz1LDk4e4gEFw92X+3Ugoit2gk72neLmxwgKO1jWGIB2wehrRlT1AnDOY

bFnTawlnQqGsV0s90Q/F22wyyFFuis+Vn5I/iDDYc5trRbfLB4rSDnRaFtqI3cnnk8SA3k98n/k8CnwU50F3WtWePUWFnGs+2u4s8nuks91n3EBlnHKyNnCs9/Wps/ujDk7G1P5NenifOYAFAC3gXeRSAHi1wr8QB8nBiDaAw8GcARiESAjiCyiyxRYHIMdb4/Bd7V+RhUGq4VFGcU6JazWardKhCn7/njFGqKMBZkg9/D2U6qTnCaNDeU+jrSE/

WlCqZxRiOYTpYzYkD5QAJnL/aJndU4WnOWKzHzU9zHrU+pn5E7hr9g5rJ68Ad78A48IXZLU7WzaGno7O840CB0bcbcizvg55yhAA0BEkRaAMABxN+1Z7HraaDR+48PHx4+c27MNIHF46vHe04fCM6goAToAxAH0f7AfXuUA5wGcA9YCaABvMwAToAOnd0/XlhjcenPHaIHtUu45Z8+vacMKvnE6a9Un0w/VTiW/G18qBnFwBBnYVYr1b40cNfavW

FIY8bdAw/sLQw5YtPTecLvc/6bmHaaT2HemHIzcgj4gchpmg6qnSY4nnaY/wnGY7JnRE5zHpE8Xn7U8o7BJPXgsjsBdsrS6Z9NFcHPKQMlP6sT6d8AlwPM+gXZKNgXj472TMtoOT56y8gXgURTsR0fWU7zDnTyAGgToCEuOqwxASs8cWOEB1W9ACsXNydYu9Fz0XByYMXoc8NnJi+nS5i8sXys6Nnti/sX7yZcbQtbUn1s+plHRevja0alrEoCTn

Kc7TnHwEzn2c9zn+c8LnZk60XtyakVyL30XMqEMXss/zQpi68XVi98Xdi6jnTGZVHKFbVHL06JTgoef5IoLf59YA/52tW/5v/P/5gAtCnnTOGZDmQJM8ChvrSnkjjPHE3suokO6VyhupjiM9tRANu0jbDbnEqY7nSM+GHXCZ7nFSptbhU6JjiqbQnSObKneM40HY884XOE54XJM+nnZjNnnxE5anBw5pnFE46nxSKYJgbbX1HMVfVxZHZwACBice

Is959OdpslVHRZ8riwH8bfrr5abrlNODWA9AGFB4pJvn04+7IB04pQx04wMmgDOnF0+IAV08SAN0+SX1sYyHPy/QAX85/nf84AXQC5AXYC4gXvI5vHyK/dTUopT5afIz53abvHN7veHZzbqNg6cW6hYNWQ/y8BXE6ZjSWtiOY/A4b4OC8DSypnxpMfQwk5hb7alcsfgjAobdGmbKTnhtbNCE7P7+veQnqo2UH1/aETuM/UH4zYMZ485THuy4InDU

4EXlM4Xnhw7OXoi9SBF4XBDyBMQHXkwYnWNveh/leFjGRc4nibYpXG5Y+Hg8at84QF5Q4cAZB8ZVUA147kws5IhIzq/AGxhzdX5gDNn9YePj3yfWR6k7UVds58bVA2qXr/OYA7/POAn/MaXf/IAFWkqidBxidXwvBdXfq7rQAa+jnt00NrbfZQbQwX7HUQ5iHcQ+t5o49w4449SHQmeFNNHHr0zdOw6lc0NwOfOoIttIF003G+z0maVwQOL8hleP

r1L1S21NMznZ2McjrVrboXiy/lT33IEbJU5xn6y8VXo84TH2y8Jnaq74XIqMOXgi6pnOq+XnlE50BW8HwD3mqRLhdY+ZH1QCzDcIGnjdMxLTcMCrXhEtXPg8Obrw4E0s7MA8m5f7rPOYP5AneZLRoO7Xpllx0qDh501rC5Ib7XI4bkUIm0Deub0fn3n2SpVMswhU7qQESroG5MBA1JB7U7fQATI5ZHbI5oHhAE5H3I7xXvVbM7xVZAbSPefwduZx

bjVd07pvuN5ek71HvWMMnxo9NHpk49L3namzFnYSQa5LOrZLCtGLzXvgKFN7VfqimE9PZ06sXcvbPLZiT7ffZ7yecFba1eFbj7f0Uq0/WnEwE2nK44aAa443H4wA0LOBltrAmvvGA8koEgGHbAKjqIl9hnCkMNRLNcPCsseQJNGfOo8huOjeNS2lol1BGZmsGBLLI68tbXxYWXBU8nX/DfPTbxVtD5U82Xi6+0Hy67wney8InTU6OX885OXS84Wb

c+aWbT4K3gpw+uXwbe0rDLBrpEIXNdO3cbU36E25Nrs+Xx88MTdJs/H1lYJ82Q3CgbcCBHBCqcrMCifXwAntX53eFsg9blNEzIfDVm6U1VrA50WffIjOYge54edHtik3k5qMbeXOFov5D8BbmT0PJRp+DOryG6ZZk1ko3RgF1HBk8NHdG5MnZRbw3BPYI3FufVadhUB6BSDF8ctjchdhWW40HbB8iQHR7oPdbGjs6gAXk58n/87dn9YCCnIU5Xbx

Vs6tPpbmzcrQjNEhqwoAm7jNF7agd8Xd5bMsv5bahqk3aXZk3S5j3wpTrK3jBgnT4XE5wdNHWqrrhinJGTF8snIIBCvdWCkSQFIQIFgw3SD3NE0q0zsE6Kz8E5c3Znu+rHbuPTEY9PTUw7lXJvdGbwJaVXCw6XX3C+C36q/4XYW43X2q9OX26/OXBJK3gpY+RrxXRWFGwBOtrvcpgNw1hD8HkbHldvbh1q6yL6i5ctsGa+HrkGcAsvGEiQEHJ9eM

BgrsAFPLRKFMZnq9j7lRBigKu5qONUGRgGu9Km0EDr2CyF13E0eJl6GdUnjYbPj1I4vjnjc0n35ayDDrrMQa04XHim+2nqm5TXlfduRSu6N3au9N3goE13Fu513Tfbibj0YSbzk6SbS5j3HB48YJT89PHr84Ta785trd2cOrtuVtp0yZ5ojsmvlRm+Uk0wG+Ab7SLd9c5NQO8JiB0fSehSXgb5Q/RUc3FCg5U3Fj9x/bmXtC/c35O4YXRU6p30Y/

lXc67jH/m8qngW6Z3xM5Z3a6/Jnc86EXW6+i3cjYnLKtC3gK3c0ra3djB0thtT5rsvXwsSDJQmnJsuW+bH3y5SG6ZZo1ToCldO8AxAPY57TxzbMpPxrcrN2Koqb6/47zTU8tf+duprBB/UDVW7AU9eL5DSKIRqjn9UPW+syfW4FjNe6VMCqq6kI26AETe4NLACCm39Voo32o7m3+k5o3i2+MnZo5W3NAv7bzG+4LMPJIalmBsRhVUfr9NAnBqDi/

8e7FO3KG9TA0S9IAqc90Q6c/iXOc7znBc8pbpBss7xbnDNjCQ+3SwC+301p+3dRRZ78C8Wtt7Yk3KXeB3Go8W69ABP36GrsXd2SP3FaLY067nQouEhiE7g8U9fEwvKyO7hBdkb5Gu9hhqbJAiIwq7a7ME9ZbhO4bL3TZRn8y6BNHm/hzve5nX/e4wnGy/p3kIhVXtU94XpM4n3mq+OXbU9pnsW4uXXU/53lqb27jpLnL568dIhwLbjT4ZwI+zYmn

rOdwHMC8pXT08D7Q1AfL10eGj3EBnAf5HUgw8EwgCyBMWJi1WQWmn8g9AFyPO2CRrs5OSPQ0ZSQQ+wyPMo5yPeR4KP9KGKPjvpt3HPufLQS4d32Gad3uGZd3X5cIz7u4YAD8+T3FABPHL8/PH6e++jx0ezKCFZo9u0HSP6IEyPRKFyP+R6EuRR5MWJR6j3+tbKXKtrj3PPfQAYK6OnJ06hXM4HOnl0+unt08z3sKJIqkzIeXcO4L3Zgoswq8Kfa0

fTRc9htWCVesBZTmLcaQqWnkCuFFi+DsSsBCIlXYw/P7Bvf+rNh+xndh9p3zraH3zh8nnrh/2XkAEcQ6661XkW5EX0A553DM9Wb7zPo7Uwh/U4DHS3rcVo0141S9406tX9664nVW65NqpRfXdW/58lzaf3Pla43+2urpEpEjj7vZF8EuZZ1lJrVm73a6kbx91wCKMykjNErc941Rt0TnqBOYlgwsB51z0BAu3V29dnygACnd249nzB5KtrB81c1u

aqttufQFAnR07eLdVUL/NqX9S6/5P/KTXLS8e3/Va5qsM2XsXjPaBchMLbuMI3JJbbb0rePCI3B85b4Zbi7V7f+3O2eWryXdWrXPfWroO94saK9/nR08xXwC9AXDEVxXP7Ziocnh8S6nlL1gM+wkZpcChTx6EHJoDePv8GIB+pG4HBgxFPosTXB70KgFgJ7RnCg/7nU6+83R7V83Dh4XXw++qno+6nnoW4pnnh+EX3h/kbPAC3g689o7SW9uXNoF

gwUGBo4+J5Jp5Pkut9Fb33HE7JPNq6J1lJ9RM1J9479W7pPPUJ5P2bemThMJ7mArFgQRbbIrnJ+XLI9rk7mZ/03vnAMw/6/zPOdUfq4XCkN0lTtsup8t8ic+Tn1B9iXGc7S4CS8YPiK687F9awPhG9mzLWY1P7WfIP026qA0a8NP8a4aXJp+aXPVYwPTG/Nz+zWY4UPVEJeElZmBgj9KsfSiozp/JkpRRWzU1bPbMeZtZfB7+3om75bvp6B3AZ+k

3k3s1H6oHiAObCaWqpO7HsKIgQpbo+zU4KMKSni8acMQ6BBzDNYNw4r3jdK8SiMTm4tDpaBavZvlTDq17xO+M5glA4diE/oXSy4HnqE4dbgJchPZvaH3iJ8n34W+n3nO9n3i3Z8PPO4kXjM9KUeuARED3f2BLxtBCnDNoBh84iz++5l3D0/iPcC4EnVQBidhS15+EUHqQU+E5gbKB+Q3mnvLfCp+Bs5McvaAB7WLj1Oj9EBuQnl/K5disgGOi/BB

O6U8dRw3oWpoh8aLRcnyBfcPiRfeq1oTtL7wKfL7wolTXG8D65Tl8Cvrl4SwoV5rg4V4ZBUivWPpS/ibTk4qXJQ8FDWQ6CBIQOPlGm6z3iwsZouwX5w0yaZaeZeLy8wahmGHkysdttAS9+g0wkUlL4gmq3TIfGL518DYchExuGcHZmX1C/MPHe8sPXe5kvFZ6HnQ5pHnDkzCLizfbPesv8Pfmdhi2eH3Nuw0B61JPhmlXbAzpJ/jDuA+J1vE7sve

/If3l3eXPsUhGvP3gFStwF03ABoIp03C5XBMmYEUp6ar18UQBOzrxBaAIwBM4CwBGIEuX759AFkvIR7LB65sE4PENuEgNZYHLLm9F6L4eMLA3EeZmrN5/VCaG4oHVA8w32G/0AjA5VPz283szAt9UFrntG/NVtpq2iskOknbAbp5i7XLc9PIm8B3CDofbCXcLXGtXbTwiNERnnanHSoN1wnOD9U6zFNxMnJdyj1lXr9JHUzNxbZouwW/QdVXd5LA

fdUoLnJY4uGYytCVb3jhdc3pO6uDP1vWvXm82vl6ahPSq99baJ9SBF/Sh9yNshdGVA+XiYLCPtY7LwSDHikKi82Tai9svGi4XZA9cXPqWazbAApVvbYDVvvltDGG6jjG8PCfUJ1JgPV55o6ipb1P1QCx7JLfIztKbc7FLet18N+Rh5ptIND9UPMF/DW0QIDtNDpLI5B7n037fHHbDY0nbAF4kARyPHhJyM2hZyNnhlyIRhEvNzvQZqpvDkU/3kLr

KiUVCQvP3lpolcqrb4CzZvOF8gdeF69PqDdY5fp/jLpF+9PlS+0j5YO1JNF/JDmm7av8pWUSODUyzmoOkccGDeqrE40kdDZ7gAAkYFJEn/gzOSZk0LiDJNaJx1buTlDYl8+tkq5+LIJ8GbYJ6zjpmtjHcw5P6MluOHxSJVnB643nLYFL4crTBd9dNUd7hLALjWOuvd69uvD697Tdq6pXabYDvGbfpP4G6XYMnpmZ8Uh6QHfvPIN9+VMtjFh5LuSB

v5G8Q5srPPJ8rMvJqHOvJt5JVZ7d8d5Fp9VPRgU9tMQNu158K11da4OYEPWuUdYwmr+N/QN6oQEhmgEFBwoNFByETEhkoOlBsoMpvh9sO6UKVzsMBdoC/65Ds0MW0tTARiyuN4mtUeewv8DdwvzPfwv3N/vbSDuQbSxbqllE+zo2/FhRMGHsxm3LoryucU9hzEnVolArcZkdYIz9TgNJsoa4Odneh08hzyINV4EZeboBFrZJ36HbWvnm6UHyzup3

qg4VXg+6tvy8zP6qQJQmVy93dxxe1scqq0tVw7dveoO9U+m69vbOfBZl1q5zKYDMOJ8EjQfICs6FxBmwpV/mwUQF9c2/DEIwFDUIRICaA+/pnA/YDrJxlCJAiQH7AJMBblMsYgApT7UoPAmaUHdeUj7Qa3g4wCEAiwBc9KomZwMwegW99Vz4XTrC5SsKR0Byg+zMdB8IXQwdIz7Xvqt95IDmNoMG6oMm4wzPexgGBUPi19M9wJ7Cf4Y+73yy8Hnq

y+HndO4QmCT6UCBJKUbWUeTq5Sj3mWnmx1ntrNYw0J97Xy+svTJQhj5kdO78u+UM4h3hwNlbbYGZVYkygIToGQwQA4xWvYVwEAgiUHg0tQD6wJICF0Y4H2IIoxzhuAHOAuAHiAOCwEA9+A/0T+C1N9tClBbMCSq6Fe45C5DaAB5A4AUwDpjR43mfpHEEoR8MgY/JFJYTuqQkNxOxLlebX3aO+UQMyqaqjw8e11z6lXYY5NvET5Qnsq773NO9YX21

5gV1YGgGlfXwAkERgiTQCdAuAHWA5gGt9OOAYRC3cSfx+MConz9iLpGWzqWZDaFWiZMDKPABqmWbsDR86svk554m4L5FikL4Hj7ShhfABCAICL+XwygNqAxAEawUSHUwowcAg3/if4yKHOAY4AaAG+AyGGQymAiUBGwgIAaA5L7vwbTk6kNL8DY9L+9QjL+fHdUr1H0Q6kiUwCE52dG5fCzF5f/sW4B9dtRvhfEqoiodLrMPOhi6Z6rme5kwEhE1

OpBgy1YF43+l8PCzG5rbMPV3tcLevdfv0q8mGUT9VfMT4H3P94Xx2r58Aer+aAhr+NfF2UkAZr4JAKdstfJcJ2pQD5XNE2C/8iVkMDUcVBCz6iZIQdI9fE58mnfgIDkawGFAF6nE8SK7Gf6/IjK5Pl9fxT7PY/+ARw8L9HyMhGUBV4Saw0GA3wRynzT60IawvWAQAsnImACADGwhwAjfERAAQf9dzfWoGNYBb7tSRb9Vq/N7qlYwdUFDQCsQJMAM

jjFFrfYJj6h8oTXcHk2JkfOA2fqlLxZxiVBm1osDJxthaxSYOOfJYRzqYmeRqbevHfvAcnffTYnX1h6YX0T5mHvoOH5bz8rSBJNffR77OHa9IFETTdlMOCTb9BmE8hgz1vfwMpPnD4XpX0MPlAdfigXzYs/fN+DLCP78SEf77hfDtmBYygNbxPAHTAKTZV5uYDJfHkHNcNWCuYqgojfYgAyGD8AQApL5qw6H8BwWiCw/DJRw/Jb7w/3HLYAJMCmA

sUGNi+AEqHzBPI/HfnrfLOVgQ59P0L27jq6Z5kKTMi8PpSt6FoGJhQpL9dEKuX7wpODFvZgIVLz4uF6tv8sE/+U/CfIn5WX8l/Qnil7838T7fT+77vReK+6nuEejo+wQ7AED5CPLDZJpCMx9HvK9gf2A/y37qd0/RgH0/8X7fflW75Exn4hfZn6ukFn9RXAH4z10SmUBmgClIxAFGDOL7QQIB2IAOYA+A2AEKFXwDg06b9xZtQFLD2wBzhVcRRAV

L7RCwX6fmoX8baxA8T5039m/Bxsfa2oPwP4p4LtW2kgYTzDo/dH8uAFVW4vVcziA/0rvgv493vBgzshgNjmlXtPL3IT7XVRt/5dGM8N7H99ErX99ifS7/mBSEyfBfh985PX4SYZkctqD2oxt8i9rHFBaYIrXaeHBzfgf5J8W/Pr9M/hQ/ObqD7oqn+t8r0P+oCj/ChS8P87IiP9IwrEpR/GF5mhaBqTvlvgI/GQ2I/zEcgvH5+gvJVqvopGV7mdH

/ZdA0lV/PwHV/0TjOA/57gPu6Ci/MX+HgcX9kfA0mVwsjhIWnlN5fx9oaB92lUKT6kuA4970fk94Mf096MfnPd5vi97qv2keJwcGmff9AFk/ot8z4NaNVhBYXLwykmKQxMlNEcG+HR0MXpItgsOpTBAY00aXhEUhPK/WN4DJFhj+J/H6bLbm9Wvdz9NvkT+nX4J7Vf3ZfnXO1+qFTk1SBw1UOvuNMoExAP88Iu6VAVP5/VtjDmlzGnHPWn69fPMz

5oy345/SWa5/Ysw/XPozqwZLrFPXOEwo/67GAmf+7XymRz/Wj7tSkupsE/zQJvyWXLf7bEwAVb/N/eVLVhoLqVmEMX05BgjLc4sW6FlMlEZqVbxvoheD5M1YQbv249/RF55vJj75vZj+459AFt5GIHzAkUDzNyX/5fvFCQNCH8ttAorUes3qnp8VBobqVvZJH90WQmwAw9SvwLwZ5c0f2fvIE95X2AVWS8VX1sPcv9Zh2TrbKEif2KRD1d6/2Lrc

UpH4CnkXYZNuU0bUZkYqHyfI5slvwBqVJxEjx65XvZu9kYgDeN7DkSgev5eUF0QSiFdECLDDMN9AB4An+MeAPmAUP5X7mRAWScsR1wFCFAogHMgZSA9ICmIW1UP7lggCFA5AGCYDgBlIAaAHfZwrhIgbQCIAHCufsBiSyaAAJN14CNOezZkAHCuH740lnCueB4qkBsnBSAaUC/4bFY14yl+cnpSAAv+FogBoBATIgAStgmINLkSuSG5cK4yuUquY

UA3sB6Mck50HmcApPsOACzgSxYAgLYVCIDceluWDH5CXn0AN7B9iGRQUSd4TlbQeCBZNBIgUxB8QBigU24mtBtgNrAq4G/AcK5N1iJ9M5M/Vm2mcH4RZRIeUeN39hzYDQ5XwE0AaCApQRCANKY4jgwgTEhrAHOuG2AmUGM0MwCkVnn2EmBugIRuJtZegOm2AuBgdl4AscM3sGVge/5qiAK+Gs59sGz+EKA9IHqgEqZL1nCuJw5RgNgOG8Rh4EmAm

2A7lhvEPd55gOqgH8BlADajAYRD7gqA+n0YR3hQd/5ugIZ2ZiBnnkOwJ5FoIA0Az8B9iHtgLVB0oC0ApFYe1n6RG5A1PhqgLrYNHlBAvOA9AH0ADNhR9gUgJlApwGeQaw4QvlWA6VIQ2AxOebxJjiRWQQ5mABvEA/55vkxA1VAiOFLAElYXIF3LKCt1gOggTmsaax5remsjAH0OOdYFIHQecK4CgDjwdLJWzA9AHIBjYCVgDaA9jjf2P8AsgCjeb

oDCNkCAabZ8gLJrNmsiIGIAE7BWQIAgeSggyWUgEUYeAA9AOw5LFgsA8JYtAN0ArUDyUEsWPO4Z0nkgK8shjHCuPO4rk02gA0CKa0KgEiAEbkQOUcNgIC+GHKVgTn2AlRYt7ltAldJCdh4AYE47VRgrI8tu3kCoeYCwoFx6NgBVQIsWHKVlIFWQPgBSViJQMQDowPMWKwDpIDPWaNB4wOYOFIAdQIsWPO4JMQzAzMCswOzAnMDcwLzA/MCCwMLAu

ZBjQKbWezY6ljs2VZAirhncOh4NoEF7f8gFAEj7GC5NAKRWPO5ZQP6AXRAOQOsAvEAW1kCAJE5FwGxWEiArdlkOYZFInl4VJnhmICZQQqBtkDbAhAB5QIToFUCSwJYeII4Y/guQQIBqQE6A5KZqdnm2bDBPwHHSQlYJ/jBOEJhrIBH2V0A8AEQAZSBPiGd4NlASwKqcKQ4sVlk0KaxXthIgF4D+gIuQAlZblnYAkSBKQO00HT5l/m72BoBu9n9An

FZ+xBbwaIC0wOnSAQ4gIH62G35BwPRObKB5vC0hCcCLkEKgeICmADQgHHBsznHSfEdDIDuA/sCHgJLA2TQngLM0dgBiAGUgNQAcVi9WECAbfgRAOwAbkEcAYkCzkGQgwy4w+1LAMiCKYAIgcOASwM+GSVhXdmggFyBKIGDA8xZ0wKLAkSDRILEg8SCJMXCuLTRkMXCuS/4PwC7yQGg0ADzuIcDIHhv+V840mBcCbsC4AGeeDSA/FjzudUCNQNu+V

ABlILLAvD5KwNcWRxYTgPHEIblP1mbAvSD3QDZAjsCypA9ADuApoHfYXNYmAEv2AcCIAB+HBrRvVj3eZiAutgrOAWUbxCvAmcC5wLWABcCjIJNAkqArgN4gXtBa9jr2XCDPsEfeDaAgHl8eJm4PYFqILCCXAilgYiBooOeAs/5YMRtgBYDPiDBWK8DdkGhA4no4YF0gmxY87kbAfoA0ABnSX+5+1hqABQBL9n4gC8CBZRXSWhAagDI2HQg7IEKgZ

axUAH/A7vZwVjquGrYdIP0ggyDQlh0g42B+AOSg6yAFkHmg/bBFoN0QajZdEGWsXRAGdjewPO4SYDigp2AFDgABIqDuqEWglD4/Fh0gmcCnIPPYD0BwwI5WRqAcIDkA0IACgGVA+84viHHSEUUxo0SWPO4ILjrA3sQhuQ8Xd/4MQOK+E6DwoN4AehMPQFTA6xZpoJmg4JYpoNLAg04zIKrAyyDqQO5rOmsgwHpAncsXtkiAuyC6oIcggCBroJDYD

0BrAJrOaEDqiFSgj5Af43IONtYmADBgs2EQQHjiX4AVQNqg6GCFFlAgNcDvFnpeYsNdNFQuQdZbkEagUIB4UH7WPKYuqHcgqpw2IGZAtcQlNF2OOABfIBtgeGDUYO1rOkCZNG4gACB/0nggFdZpUhCgdB4QE3RARqZULk4gX5YS3iHWGkEbANceViD4YLSAqyc7IHFAtWt28mnWTQ5jYO6oftYy4GAg3wAZrAiAdchJYDDAIAh6IG2AgqDrAIHEa

3AYIIgAeiD79mYgdB49IHBWQrxFYFbybM4RHj0gGRYSoDymKCAuqDUAQSCrFhhg2GCDFkugxyCOQMyFIlBFYK4AnWt3QOUgd8C5kHvAfy56oMgrJOA/oIy5dB4wUBxWaWCiQPv2V3hGoDpgoXBIYPsOeGCJIN7gvuDxIPhg3KtywNigcyDqwND+CKA/iAUAKx0wPVxg1mCuwKo9XsDann7Ay0CIABO2YcCPgLHAoIAJwPUgLGU2FXZAUMAuqHhgq

6COQK0gjuD3gGZgho4AaCegUaC3wB2cQV51IAK+XnY1YJB+WGVQoLA9DODdQJUOB7YrICog7FY/llasV7Zr2C9WayAZlnMADEBBoLCgY/5/jiqQFTAjSBBOQp54YKxlN+CW1mlSfABXQG8goGDTbhqsBNAbYA5gLNZM4B7g/uCiEOIQnMCdIIrOTI5eoIQAMPZo1guQHCBTQG6oDEAsIEewGhDZ4P8WHSDLFmPg5yCqnSb+ZKC3AjknNrRJAN5+K

IAcNjzuMH5+tRFeNiBkoO6oKBDe0FyeUjYO4MEoLuD2EPAg7OC9FmUQoSCEYOHg0eDLIPGAobkAADJSVm9A9ERWEPsgzhCboOsA18AjQDqA6CBd4PC2MZZTo0S2V0DdNFCA7AAwYNPweYBmYPUQ4yDbkHs+aYCaoFmAu0C3sDPA9bwbfjyA9EDTbjRANtgGLnR6Uu5YzhphLqhlUHIAZPYP4LxgwKhuqF/YDmAQoACQ8dIgkMogwXpvIPzOG4x+g

PUgQYxDyzmWdB59iSmRIaDjDixQFJDWYNUQ3RYvELMQomCcpQ5WXnZHoKYOZgACgBSAE5ZY1m4QvZYfoO2uXRCnEPSQtECCgIW+YzQ3sAUQ5UCmkLzg5yC0kKJQBZCOkKmIAoB4gF6Q06D2VjWOD0DYlkGQzpwbyx9A01Z3XnKvXtBKkOngZQApkLZA+UDvgCUQoyCOELmQm6DNoULg6mtOAGLgukDCdnoQ8uDK4J2QmI4a4KcgYZDuYJBgRuCXi

BCAbiAw4L/OV3hedmmQm5DvkIaQnRYvEJMgxGCKwORgmsCfAJhAr8ChiRMQvGCLEJDgpY4UkGYgAlY0IFNA67AOAAAAchqgNoBqnwpORB4vfhC+MFC6gjcCR7A6kMzgtmCQdnXWbTR1wIUgfbBVflwAN7BJwJCg/8hlIEwQhb46UM5QzIV/YO+Q6wD1wOPAw/YVUBIgPiAzoRUgQUBqAGYgLEA6rgdgy94WIJGjIQ5VIBZg/xY87kcAakhgYFaA7

FYhUIQgyJDGQBJWOSCIUNbQRkBOBhagv45e0DSYI5wmUM/gntZEoBcgfEcNwCFeWog2FTqjZwBUQFMoZOByQMiAl1CVENhQrRZZkIJgjkCRUN2gBZBHkJwgblC3oILgnJY87lxQlLUUQM2hV/ZKvDrgtwJtkJjQp6AoUMjQ9sCOQIJWDsCk4AWQJg5kXiV6ENh9sDSQnCAJoNUAkNZREIIAabBVsBKgd14azmfEQ5DcYH9Q1hALkLlA8GDrkK8Qo

tD2QOcgn5YEwKEQ2TR/IFLQrtDY1nzQ1mCjpmggLrZ0HlBA6yBC0PsOPxYtNCwgBZBedjzufox4IHQeQ0AuxBeAjgAmAPJQXLlT0N72FgDpUjYA/YhbkE4A7gDskP4AleMOACEAkQDkwOUgSycMgMEQpg4ZAO+A+QCrfg4OZQDWAAaedQDWEJ0A7QCkVn0AsAcjAJMA+sAhgLVA8NC4UMBAy34prHNg32ADkAcAwqAnAIoOJgA3APMADwCU4Mm2b

FYA/gy5AICJyV82YICinndXEGB4gKGMMCDYwKRWOj4c1lQg3/YD/hlQ5IDUgPVQDIC6oDbQHIDUwDGQ4GCszmYgEoC0zl1QxaCqgOQgGoDYkLjgtCA142/YZoDrIGNQ9oCjoLfADTRugJH2PoCqtkGA8K4RgLGAkL5DgMNAKYCwYH8QpxDzgPAgPY5lgLFebqg1gO+AzYD8QHFQixZdgO6AuuDDMNEgY4C64LOA6aABDgOgm4DqiAkwh4DCIITKZ

4CmbleA2753gN/Aq44vgMTg34DbMH+ApFY4wI/AYEC2UFBAxYD7NEhA5o4DAFhAl+DEQIGgZEDgdlRA/IDgYKxAyxYcQLxA01CUgJbgv85SQN+QvOBjUMVg2kCMYIZA/9JeDjCgFkD7kKJgrkDKoCfeCt5+QOkgcw444OFAkCAxQJZrIBMKQJlAy5DwYKFYcGDuwCigxDCkMIjQhLDtQN0AjdDwIP1AtCET8k94EsDTQIPgjbCk4BXg60CXQIBQ9

5DHQJSyHsQbQOOw8MDPQMq8fZC5llrQoCDAwIzg0MD+YKleKMDlIBjA3VDx0Nk0RMCmDl0QFMDVsI0QkhCgcOBwjMCSwKHgpGCLIJRQ/JwexAbA1PsmwIQw8CDmkPA2eeCewLquJeDPsBXglSDYtg3gtqhxwNfAkjD1kDPgyKCM4L1AwI5H2Cq2NcCC1jwuTcDw3m/dLyA6GgOQTI4hoKPApqALULPAluAaiGPAsXhdULzuW8CUoKFeB8C54BCw7

z4kIPGguQBuqE/Aw0BvwLUgkaCAIKAgqqDQIJ5wiCCfwCggvTRvIM92eCDA/mtgKrYUINww0gB0IMwg/QBsIM5eL6D8IJbAx4DgsOIglNgyIJqgYJDf4JnWPEAqQDZQedC+UI1Q2vtOADYgskDD4PNw7iD8QG5APiCpWDCAEnCkMRBw0PD+4KkgqMDZINBOM/JFIO8QrHCZcOfguoItIJ0g+GCFsOQw+yDwcKRQyHCrIP+ghwJbIIRw1mCkcJcg/

H53ILM0LyCV4N8gtEcRRyqCQKDtrmCgj8BcQPHEMKDJsOicYnD4YNNA6IBrgISg42ITcNnDFKC6tB1+Zl5MzgZ2LKCxiByguoI8oN1Qz+DnwKKgiOCLgLKghwIKoNfAKqCaPRqghWDXIFnAqG4WoLfQdqD0vE6g2GUeoPhAGSAXdgGgmxCNoGGgm+D3wKZQrOC08PUWOaCPoIkw5aDx0lWgsaN1oJ00TaC/iG2gpm5doKFQXzDVMLkQ06Cxo3Ogm

xZc4KjQ5yC7oO2wB6D/0Oeg16DY1nmgz6C+8Osgb5DfoNOAhwJAYIJAkGDzG3xgxqCpsLWQqGDmUNvwxbCM8NMgrPCx4Iaw9GDMaB+Q4NDPxQvOAvDmUKLwkmDrMLJgzFYB8I2gF9DqYJx6WmCW8IC8RUC8jE8QgqDTQMiQm54uYL4A3CAnYLugwWDZNGFg0BNetkeQawBvFjawqWCQUO7QOWCp8PAg8gidaxVg5rDhR1+WGVAtYJBgXWC2AH1gx

1DHYLQuebZXgTQwv85lUIKgq2CeMOggW2CxsMIgdVCxCLMI/bAXYM6eXEBx0isgRaAkHk2gDFMwwFyARzC54Mt+IODGMBDg/NCI4LCgKOCZQGN3EQBBsMEADI4YsKmgTwDl9nTg1PDCCI0WUAji0OcgguCFkCLgigijAFLgsXDmAArgquCqCOxgpyBPMIcCBuCsl2BQmaB50ILgjuD1MBuQwhCw8LaIosDB4JIIkeDkUPHghG4p4JcdaC4Z4LoI1

1DLfi0g7SA+wIxw+u5V4P6gdeDIsIt3MXht4NhlPeDz8jUIjRCi8NPglvCaxQvgmqAr4OsgG+CfFnvg9z4n4I0gsfYmIIbw5BDZYPhg6wCusPyQwqB/4OEgQBCBVhAQ7aAaQAgQl8AjcIQ+GBD0wDgQq1DEEP5Q3sQxiNQQ9BCV4Iqw3NYR9mYgPBDLIAIQgqD2iNhIgsCyEKFeGqBWjkoQ6hDaEK9IBhCmEJOwFhDhiJAI25CLFiLw/pCFkF4Qr

9DBVkEQr7CRENvEcRCRAC7QKRD9sBkQ0/5zG37QnAidfzwIgHC9UPfgW/D4UM0QiHCx4N0QhwIDENuwsQBMUMLwjrDkcMt+SxDitlFQQbDbENjeOqNHEIBQlxC3EIvMfgjvkNaQtDYTMPQGbmDckNZ4e3CBZUEwiJCeQBCgQ9YYkIh+DbD2IFf+H8BiwDfQIIj2SLSQu5ZAICwlTUi+AO1IkJCCkP9QIpDLkHpQIxDjywqQwpxqkPsVPtBQ0I0Qw

giR0MJg8DZWkO2wdpDoCK6QnpC3oP6Q3ZZdkN7Qf5DRCLuWfUiJkIC0JkjN8J1/GZC8SMOWUUiPQAWQhZAlkOjI1ZD1kNWgzZDY1m2QmJZEyO1QQUju3kNeCK9JFROQ9wADIEzIq5CcyNDI/ODedjyI55DX0IKI95Cy4LFeEoivkOrI8oj1awngmYCRkJqI23Dm4IaIyFDNiKHQtkj7IJDI3Mi48K6I7RCocIn2WEC84HzwrkjsUO8g3FD/kBtgA

lCWUOJQslDUAApQ4HYsYGpQ/LCaoHnQhlCbSPsgjvDjqHhQSfBwUK5QxQCeUJ1w/4jBUIwIqrD6ULFQoMjvEMlQ1XCkgP4w+VDEoEVQgWAVUKiQGQjdcPdwjqNtUOeQLkiDUJfJb8DmcMaeBb5zUNdAfDCvIEeQriBcmBt+ekjQICYAZ1C9yI2gd1CDAGuQcYldkFswv1CA0K8gMkCKiPowrkiVyNiWIvD50LjQqMjE0NjWZNCkllTQsTDxgIfIs

g4c0LFQ/8iSQOwIrMie5C7g9ij8yJnQ8tC6IDPWLwJq0KgAWtCjZwbQhp4m0J+IFtD+IG1QIBCQzk7QpOBPVn0AXtDTKDbIwdCcyNiWTsix0KTAolAvsKEueSinIDnQqKBW4OZQxdC0sJXQva510J0grdCd0O8Q/dDQIDCgI9DbcNCwy9D/vnsOAZ5DMF3FcspBaTSvfm0S+3T7E8kInRyvAPcqgD++a9DOAFOOO9DGnGLgtpweAKcQgQCXkM2Jd

9C/sM/Q/hCIwmHgKQDcAD/Qp6CSVm5Q4DDVALAwugiIMJWwyxZoMMMArPE4MLoIjIi78JQw18BLCInwzDCiREcAseNWMPwwqFBPAOIwqcDfAKoeKdJyMKy5SjCQgOzXVohwgM1QqIDdUNiAuxCOCJcAxICOMLqjLjD0gMFWXjDsgO6AsJDxkIQgooDvgLwAMTDygK+gxKBqgKwAWoCpSKFAWw4GgIUwznDPwDaAjmDp1nUwkiBNMKm2fHCdMOGAt

CA9gMfCAzCjgISODUin0PMwsECgbi3AlYDbMI2AuCAtgIzg5zCnQN7ENzDptiqIqoIYaMuArvDbgNNwokcgsM4gtcRQsPlg8LCZcOiwn4CpoD+AuGAAQMsWIED8IVSw8EDSjgyw4CC0ULhAxiDPwFcgPLCNoDHAArCzqOKw3VCysPHEfEDMKMJA/NCasOoIurCqQN7IxrDKCMTwpkC2sKRWIvCbiMNgxYD+timgAUCBsJeoobDRQOOAhwjyaxRga

UCmiLEApUC5sIsWHqjnAE1AiDC2SNJw80DIgO2wmSBOqD2wpyADsL+IC7CUyIdA1g4zsOdA9iBLsI9A21UbsO9I30CHsKYAIMDwrmew8MDXsOQxd7D3sMYwhmjbKJ+w0QD8COEguEj06LzAsHD1yJ6IntY/oNhwhvt4cJLAhgjRiIXgtHDwgHp9THCY9EgeEcDl/lxwreD8cKnAwnDNiPnA4PClwPJwplBKcI3A9z46cK/WPcCmcPPwlnCTwMqQ8

8CPqIqgm8CuYH5w9SBBcKfA0miRcPxw98CJcIFHaXCN4NGg+XCQIOrIBjDvEIaOKVC1cMro3MpNcMQghujmIJpg/XC1bkNw43CAsKJHAiCinnDgK3DSIP0OCiCdSNuI2t5HcLoglyjwUNdw7ajIgM9wjiDDIC4grIAeIP9w5OABIJLAjOiwGNIQpFZpIMloKPDCngUgzfDlIKrojf4ynkVoytAwPRTwgqCraOtogqDM8O6I7PDsaPAuc+hhSO8Qo

vDXII/AUvDPIPK8CvDURz+HavC3AxtgIKDESP+Iow4meCJwi2jWYI7wv/DtUESg3vCF4200bzRB8OBWYB4R8K/g96CjcNygmCCCoJnw8xs58OEI18ByoO5w5fD8i0g9TejP4IagzfDmoOpQVqCqIA6gpCAuoIbww/CroGPwniBT8JNQkL5L8KHI6/COSJ6o+/CFoK+gp/D9ABfwxAi38IMAD/DUQC/w7z4f8P2g/GiPCKwIxxiF42AI6xYsiNHQm

6CICP5go2daqJeg9ZD4CIkw5AjtrnwYlNZ0CPFozAjRxCaI1kj0iOsY7Bjs6OzwjQjlYKxgw0Dg1hxItYj8yMYIuq52aPJg1gjKYLOQPXC6YJ4IxmCekJUY8CDBCI5gv+CRkN5g0t4JCNKOaQjRYLIY+QiQYGfA5uDVwFUIhWC5aIKIrQjFaI1gvQiU2AMIvKY9YNfQbVA7iKdg02CBqItgmwjuMKOo+wjRsKNoywAa3iNg1wj3COJOTwiPYJ8I7

2D/CPdQ+VZLGMDg3sCwiO8giIiSoKiIhvDy/iPyOyAEiMq8JIjk4J8AVIjoSOXIq2igmLDIj0BciM1rGmtXkIxgoojPkLKIvJiKa3iYmxC8zhnI5QiGiPbgzYjmiPJQVojwGPTozojEUNwYseDAr0ng6eDzQCIYvO4UcMJWReDy6OXgqYi14OronHCFiOKQpYitqP3gtAYj4PzIjYiB0LFPbYieIAZAPYiAINvg7IBDiMfg7QjTiNfgpvD34KuIy

341aJt+e4jmEFC+VnhniLAQt4jiKK+IsdMyEHgQryA/iPOIwViUENfWEODQSOwQiEiblihIyxjUWLAYhEid4IoQo/DUSKNnehCw9kxI7Ejh0NXIgkj9VmJI8qj0skqoydCKSLEQnJ5qSNRQWki5WLkQ8yiWSOhQ0ci2KNHInBiNyLQ2EL59EMMQspChSMKY+gjimPFIh7ZJSI2wwaCBZV9QhxCn0Oow8wAlSMWAFUjRyLVIvxCnSLmAx+jXSKxlN

MizUMNI6JCnqLNI+JDw4ESQ60igKLzuO0iMkMdI6GjC2N1IzqBCkO1woV5SkNgrEGBTkPVow/5AyNYozkjbWPzIiMifEPCYzpDukPWQ+MidlhrI9NDJyOOw4UAS2J5gjMjJKPbImSiYliLwwsjIwPHYlZC1kLeg8siY1krI8HZZ2IjY7tjDzm9WY5DtUFOQ1sjV2Iso/1joliLwx5CeyK1rYFjMaAHI4ojSiO+QiFik4GTIscNAUNqI2cj36LqCR

5DvKNXIm/Dw0K5I4Nic6I2gLcj0UN3IsDiRGMnwq0DGNkyo48ixXkJQj8AzyPJQylDryJvEW8jxKN2gB8i62JZQ69g2ULfI+lDuUN5Qs4iviB7EX8ikmII4/f5AKPIokrRQKI4w8CjtoEgoipxoKJtgVVC4KOPo6X54QO8ePu4dUJQo8wA0KM+ok1C/yOwoy1Do8PwozLw7UM0Yh1D5mNIov1BiOLdQnIAqKNH2b1CxiBTYntCGKI/AJij8mNLAY

jjA2IfY/MjOKOtQhNDPyKTQxqAU0Jcvb8AhKMzQkSi8QLEoyWjb2OzI9dizOLAIm6DHKI/ACtClKK+IK9Aa0LrQuiAVAM0o+yCGiBXHXSj20KJeeCBDKKcgYyjTKOHedzjpKJtY2SjvOKJg+yjk6KnQsXCy0KcohjiF0JTgpdDtrk8oo44UuMXInyjlkD8ovdCnWRBgYKivPhhgP75z0NzXD5FY91qvWkY0cA1qIxADEHafI18MQDayYFdsZFmET

6YiEQ8pLDwDNwuNDR0c+XizUvM32hqbaAsnw0ezD+QnqQB8Rfou53z/DH90Zwv7TGccf0z9MStv7xwA/3ocuh0BDE9He2LrVsBVmUHPXYY7AyOBOJUaxWCPEk84HwXGWSweJkZoIXBbwzv3AAZMnE2wNAA/lhueLliWqG0g0zQ19jewRwAZQBUaUB4KvGggWhBrsF00LtjavFwhTlYafVt+fa4JTm5YsV5mtBB41VBweI4aA34oeJUgRkBvNHh47

6BIqMa5WKj9iGu4K+N0gjCdTEFsr18oXK8dYx+4lHj/uIOIjHjgeK+QsHjlGlx4kI4OAGh4zLwieO9AkniWuMWNcpcja3C/RPk2gCFyRIAEAGSFYP9hOQOrd+BjDDPMM6tjbGk9Z5dYGE/DdSYWZhr1Cvl30S5IbVhD/x8SMhcNM0O6Es9Lg0x/bbjsf1E/ed9xPz0JST92v3efVIEYdEIAqBwKlHr4c41ZTCL4Nv1yDT5oCy92Jx7/atojPydkb

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=
```
%%