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
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

P4MuT8AiclfNkCAop4PVxBgWIChjBAg6MCkVjo+HNZkIN/2A/5pUMSA5ID1UDSAuqA20CyA1MBRkKBgrM5mICKAtM4dUIWgioDkICqAmJDY4LQgNeNv2EaA6yAjUNaAw6C3wA00ToCR9h6AqrZ+gPCuIYCRgJC+fYDDQAmAsGA/EMcQ04DwID2ORYCxXm6oFYDPgPWA/EAxUIsWbYDOgNrggzDRIEOA2uCTgOmgAQ59oKuA6ohxMLuA/CCEykeAp

m5ngNu+V4DvwKuOD4CE4O+A2zBfgKRWGMCPwEBAtlBgQPmA+zRwQOaOAwBoQOfg+ECBoERA4HZkQNyAoGCMQMsWLECcQJNQpIDm4L/OYkCfkLzgI1CFYOpA9GC6QP/SXg4woCZAu5DCYI5AyqAn3greXkDpIHMOWODBQJAgEUCmayATMkCpQIuQsGChWDBg7sBIoIQwxDDw0PiwzUDtAPXQ0CDdQLQhE/JPeCLA40D94PWwpOBl4MtAp0D/kLeQ+

0CUsh7EK0CjsNDA90DKvD2QuZYa0IAg/0D04ODAvmCpXgjA5SAowJ1QsdDZNHjApg5dECTAlbD1EOIQwHCgcLTAosDB4MRgsyDkUPycHsQ6wPT7BsD4MNAgppDwNjngrsC6rkXgz7Bl4KUg2LZ14LaoUcDnwOIw9ZBT4Iig9OCdQMCOR9gqthXAgtY8LnXA8N5v3S8gOhoDkEyOQaCDwKagc1CTwJbgGohDwLF4HVC87mvA5KChXjvAueBgsO8+B

CCxoLkAbqh3wMNAT8CVIOGgv8CAIMqg4CDucLAgn8AIIL00TyDPdlggwP5rYCq2JCCcMNIAVCD0IP0ATCDOXk+g3CCmwPuAoLDCIJTYEiCaoCCQn+CZ1jxAKkA2UDnQ3lD1UPr7TgAWIJJAg+CzcM4g/EBuQB4gqVgwgGJwpDFgcJDwvuCJIIjA6SDQTjPyeSCvEMxw6XCn4LqCDSCtILhg+bCkMNsgsHDEUIhwiyC/oIcCayD4cJZgxHCnIPx+V

yCzNA8g5eDvIIa0b1Y93gCg7a4goI/AbEDxxFCgibDonCJwuGDjQOiAS4D4oONiY3DZw2SgurQdfmZeTM4GdkygsYhsoLqCXKCdUI/gx8DCoPDgs4DSoIcCcqDXwEqgmj1qoPlg1yBpwKhuZqC30Dag9LwOoNhlbqD4QBkgF3Z+oOsQjaAhoOvg18DGUMzg1PD1Flmg96DxMKWg8dIVoLGjNaCdNA2gv4gtoKZuHaChUB8wlTDZEJOgsaMzoJsWH

ODI0Mcg26DtsHugv9CnoJeg2NY5oI+g3vDrIC+Qn6DjgIcCAGC8QOBgixs8YIagybDVkMhgplCb8IWw9PDjIMzw0eD6sLRgzGhvkKDQz8ULznzwplDC8OJgqzDSYMxWfvCNoGfQqmCcehpg5vCAvHlAvIwPEPyg40CIkJueTmCeANwgR2DboIFg2TQhYNATXrZHkGsAbxZWsMlg4FDu0FlgyfDQILIIrWtlYKaw3yDflhlQTWCQYB1gtgA9YIdQh

2C0Lnm2V4FUML/OJVD8oMtg7jDoIBtg0bDCIDVQ0QjTCP2wZ2DOnlxAcdIrIEWgJB5NoAxTMMBcgAcw2eDLfkDgxjBg4LzQ8OCwoEjgmUBzdxEAAbDBAAyOaLCpoHcA5fY04JTwggiNFhAIotDHIPzghZBC4PIIowAS4NFw5gBy4MrgygisYKcgDzCHAnrg3JcgUJmgOdD84Pbg9TBrkIIQ0PDWiILAgeDiCOHgpFCx4IRuSeCXHWguaeDaCJdQy

34NIO0gHsD0cPruFeD+oDXgiLCbdzF4LeDYZV3g8/JVCPUQwvCT4ObwmsVz4JqgS+DrIGvgnxY74Pc+R+C1ILH2BiD68KQQmWC4YMsAzrC8kMKgP+DhIAAQgVZgEO2gGkBwEJfAQ3CEPmgQ9MBYEMtQhBC+UN7EUYiUELQQ5eDysNzWEfZmIFwQyyB8EPygtoiYSLzA0hChXhqgVo4KEKoQmhCvSHoQxhCTsGYQoYjgCJuQixZC8L6QhZAeEM/Qt

ICBEM+w4RDbxDEQkQAu0EkQ/bBpENP+Cxs+0OwI/X9cCP+w3VD34BvwuFCNEPBw0eCdEIcCfRCbsLEADFCC8PawpHDLfgsQ4rZRUAGwmxDY3jqjBxD/kOcQ1xCLzD4Ir5CWkLQ2YzD0Bi5gnJDWeDtwgWUBMPCQnkAQoEPWaJCIfnWw9iBX/h/AYsA30ECItkjUkLuWQCAsJQ1IngCtSOCQ/JD/UEKQy5B6UEMQo8tykMKcKpD7FT7QEND1EIII4

dCCYPA2FpDtsDaQqAjOkO6Q16C+kN2WHZDe0D+QkQi7lj1I8ZCAtEZIjfD9f2mQ3EjDlhFIj0B5kIWQRZCoyJWQtZCVoI2Q2NYtkJiWBMjtUAFI7t5DXmivSRVjkPcAAyAMyMuQ7MiQyLzg3nZciKeQl9D8iLeQ0uCxXmKIz5CqyLKI1Wtx4KmA4ZDqiJtwpuD6iIhQjYjB0NZI2yDgyJzI2PDOiK0QyHCJ9mhAvOA88M5IrFDPIJxQ/5AbYHxQ5

lCiUNJQ1AByUOB2LGAqULywmqA50PpQ60jbIPbw46h4UEnwMFDOUPkA7lDtcL+IgVD0CMqwulDRUMDIrxCJUJVwhIC+MLlQxKAFUIFgZVCokGkInXC3cI6jLVDnkE5I/VCXyU/ApnDGngW+M1DXQDwwryAHkK4gXJgbfjpI0CAmACdQ3ciNoDdQgwBrkHGJXZAbMN9Q/1CvIBJA8oi6MM5I5cjYlkLwudDY0MjIhNDY1iTQpJYU0NEw0YD7yLIOb

NDRUL/IokCsCMzInuRO4LYovMjp0LLQuiAz1i8CKtCoABrQw2d60IaeRtCfiGbQ/iBtUEAQkM4O0KTgT1Z9AB7Q0yhWyIHQ7MjYlg7I0dCEwKJQT7ChLjkopyBZ0KigFuCmUIXQ1LDl0L2uNdCtIM3Q7dCvEL3Q0CAwoEPQm3CQsIvQ/757DgGeQzBdxXLKQWlMr35tMvtM+xPJCJ18ryD3KoA/vivQzgBTjlvQxpwi4LacLgDHEL4A55DNiTfQ3

7CP0L4QiMJh4AkA3ABf0MegklYuUKAw5QDQMNoI8DDlsMsWKDD9AKzxWDDaCPSI2/DkMNfACwjx8IwwokR7ALHjFjC8MKhQdwCiMInA7wCqHinSMjCsuQowoICc11aIUICNUIiAnVDogNsQ9ginAPiA9jC6o04w1IDBVh4wzIDOgNCQsZC4IIKAz4C8AFEw0oDPoMSgSoCsAGqAyUihQFsOOoD5MI5wz8AWgPZg6dY1MJIgDTCptjxw7TDBgLQgH

YDHwn0wg4CEjnVIx9CzMJBAoG4NwKWAmzC1gLggDYD04Kcwh0DexFcw6bZKiKqCaGjzgM7w64CTcMJHQLD2ILXEELC5YLCw6XCosK+AqaAfgLhgP4DLFgBA/CEUsNBA0o50sMAg1FCYQPogz8BXIFywjaAxwHyw06iisJ1Q0rDxxFxAjCj8QLzQ6rCqCNqwikCeyIawigiE8IZA1rCkVkLw64iDYPmA/rYpoD5A/rDnqMGw4UDDgPsI0msUYElAx

oiRAIVA2bCLFm6o5wB1QPAw1kiScNNA8ICtsJkgTqhdsKcgfbC/iHOw5Mi7QNYOU7DHQPYgC7C3QNtVa7CvSO9A+7CmAADA8K4nsNDAl7DkMTewt7CGMPpomyjvsOEAvAjBINhItOicwNBwtcjuiJ7WX6CYcKb7OHCiwPoIkYj54NRw8IB6fQxwmPRIHiHA5f4ccM3gvHCJwIJwjYjZwKDwhcCycKZQCnC1wPc+WnCv1h3AxnCz8OZwo8CKkNPA9

6jyoKvArmA+cPUgAXCHwJJo4XC8cNfA8XCvhylw9eCRoLlwoCDqyHowrxCGjklQ1XCK6NzKDXD4IProxiDqYL1wtW4DcKNw/zDCRzwgop5w4Etw4iD9DjIg7UibiNreB3CaIOcosFCXcK2o8ICPcLYgwyAOIKyALiC/cOTgPiCiwPTo0BiSEKRWSSDJaEjwwp45II3wxSDK6I3+Mp4FaMrQMD1k8Pygy2iraPygjPCuiKzwrGjwLnPoIUivEMLw5

yCPwBLw9yDyvHLwwUdtCIPo1LC68K+IEKCxeEJw82iWYPbw3/DtUASgnvCF4200bzQB8OBWYB5h8M/gt6DDcJygqCD8oOnwixtZ8KEI18AyoK5wpfC8i0g9DeiP4PqgjfCmoOpQFqCqIHagpCBOoPrwg/CroCPwniAT8ONQkL4L8MHIq/D2SO6ou/D5oM+gx/D9AGfwhAjX8IMAd/DUQE/w7z5v8L2gvGj3CMwIuxiF4yAI6xZMiJHQ66DwCL5gw

2caqOegtZC4CPEwpAjtrjwYlNY0CLFojAjRxEaIlki0iIsYrBis6Kzw9QilYMxg/UDg1mxI1Yi8yIYIuq42aLJglgiKYLOQXXDaYO4IhmDukMUY0CCBCPZg3+DhkJ5g0t5xCNKOKQiRYNIYuQiQYEfApuDVwBUI+WDZaPyIzQiFaPVg3QiU2H0IvKZdYNfQbVBbiMdgk2D+qPNg6wiuMMOouwiRsMNoywAa3kNglwi3COJODwj3YO8Ir2C/CLdQ+

VYzGIDg7sDQiM8g8IjioMiI+vDy/iPyOyB4iMq8RIik4J8AFIioSKXIy2j/GNDIj0AciPVrKmsXkPRgwoiPkNKI7JiyaxiY6xC8zmnIpQj6iLbgjYimiPJQFoiwGLTojoiEUJwY0eCQrwngqeDzQEIYvO5kcMJWBeCy6KXgyYjV4Kro7HD5iKKQxYjNqL3gtAZD4LzI9Yj+0PFPLYieIAZAXYi/wJvg7IADiIfgrQiTiJfgxvC34MuIy35VaJt+O

4jmEFC+VngniNAQ14iiKM+IsdMyEDgQryBfiLOIvljkENfWYOCQSKwQ8EiblkhIsxikWNAY+Ejt4PIQw/CUSMNnOhCw9gxIrEih0JXI/Ej9ViJIsqj0sgqoidDySNEQnJ4qSNRQGkjpWNkQsyjmSKhQkcjWKJHI7Bj1yLQ2EL49EIMQ0pDBSLyYugiCmLFIh7YJSPWwgaCBZR9Q+xDH0Kow8wBFSMWAZUiRyNVI3xDHSJmAh+iXSKxlVMjTUINIq

JDHqNNIuJDw4ASQq0jAKLzuW0j0kIdIqGi82J1IzqACkK1woV4SkJgrEGATkLVow/4AyJYojkirWLzI8MjvEJCYjpCukLWQuMidlmrItNCJyKOw4UBC2O5g9MiJKLbI6SiYlkLwgsjwwJHY5ZDVkNegssiY1grI8HYp2NDYjtjDzm9WI5DtUBOQlsil2PMon1jolkLwh5DuyI1rAFjMaH7IooiSiK+Q0Fik4CTIscMAUJqImci36LqCB5CvKJXI6

/Cw0M5IgNjs6I2gTci0UJ3I4DjBGInwi0DGNgyoo8ixXgJQj8BTyLJQilCryJvEG8ixKN2ge8jq2OZQ69hWUNfIulCuUJ5Q04j6GP5Q6+iP/iFQ/9iRULdAgjjgKM+wUCjOgPAozFAuYCgom2AVUNgoo+jpflhA7x4+7m1Q5CjzAFQoj6jjUN/IrCiLUKjwvCjMvFtQtRj7UJmYkii/UEY48iicgEoo0fYvULGIRNju0Pooj8BGKJyY0sACOL9Y2

9i8yI4oq1D40I/IxNDGoGTQ2SdvwEEojNDhKJxA0SiJaKvYrMiV2JM40AjroIcoj8By0MUor4gr0GrQ2tC6ICUAjSjbIIaIJccdKLbQol54IAMopyAjKJMo4d5XOKkoy1iZKM84wmC7KKToydDRcNLQxyjcONQ+XaDk4MXQ7a4PKKOOJLiFyO8o5ZBfKN3Qp1kQYCCorz4YYD++M9C81w+RePdGr3EPfRRYoBxwYeApgFZNQbhdVFDgY6havBwyZ

ewtPV84VZhiWmJkK2V0O0hxagQ32kO0NJAQFi8aU2RjChYDFwU58XgA2WgPWBx/NV8XSE9wTjA1l0cocv9h5za/VS88ALelbS0KbAWTJidzzGoCa8Z5uCoA+xhMLV6YNH13Qn/vHT8KTxAECAACgAKANHpmyM8ACgAFAGaoLR4GyK6obw5Rlm0AfQBiAEJAHEAIKO6uD0APQD5AV9dcxW+/KMtUyDe/LD8tyCZfOp9ZsH0ARp9FsH98SHjZeDkAM

Bxq8DCAAEcHACcAPpEq4CLQN0ABbC2ZLIkoAD/ABogOAEGMWnihmHp4jcA/wHoZTawi/xMcJFBF6CGBFng4LAtdCcgpwEhgVDlOeMovbuAeeIJ4cXjbigADSEQxeOLgIXinHHgEG7gcgCnwQKg+wHYaLUBpRGzRFNwdAR1kReBwAFaQBwg8pgXJR2xoAD6wk+ByYChAXYAGABIUCgAccGbLQkAxhj3EV1jsVE+GArx1rxUZNcQPeL5CT4ZneIa/G

ik/eLxWT3isgEigPH93eLD4gPisgG94wKNQ+IYQeAw4+Ja/MWRE+IcET4Z8KzBpdPjw+P0AFXi3Wxz42Pj9AEBIOaM94kL45Pji+KJlZR17ePEQovih4CCdfYgjKHL4r3i/dQIvYRhm+KyAGcBxC25va7wO+K8VUehTeRxoUxBuQASoobx/eIr4s7Yp8HwrLUAwqFTAFl8hQCwMLHRlmGjjX+kTBUWUe3j9iXRAIUBrURnsC5Q9tECcHfsauXt4l

uoDAFjsBgBpzlpaBSZDZBTIPvis+LUCeTIhgCA8EgAcBkSQJ/iShDFeLo83+KQhLvjavA7UN/jWnxTAbw5UEOGEZQAqQH2wb2leAALESAT6YIvKeIJWo34gC3A5iDAEtEteACIyVASBkEloWYBvsAooQvj4+I2hCXgblidobfR64DDAS6Atc1RUX/ioExeIPlAoE0qfKBMloF8CKBN+1g80JgB6wCnwJgTuQCxAUgAf+O+gLZJZZTuISycQOFDQc

QZGpB4E3E4PyQcINID7wDcdKVRMcGzoMIBggD/OdmB6nwMAQfjUYHW/ZQxqNnHie/ZvjD+IYUFBVmkEheg4aBwExwBlvGCAext7AkDAQTxwCHV4lzhNIgXgIAA==
```
%%