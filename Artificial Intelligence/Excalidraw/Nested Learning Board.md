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


# Based on the **Nested Learning (NL)** paradigm and the architectures of **CMS (Continuum Memory Systems)** and **TreeLoRA** described in the sources, here is a visualization of a **Base-Transformer integrated with TreeLoRA and CMS**.

### **The Concept: "The Organized Memory"**
In this integrated architecture, we replace the standard static MLP block of a Transformer with a **CMS-TreeLoRA Hybrid Block**.
*   **CMS Role (Time):** Splits learning into "Fast" (immediate adaptation) and "Slow" (consolidation) frequencies,.
*   **TreeLoRA Role (Structure):** Organizes the "Slow" consolidation. Instead of overwriting long-term memory with a single average update (which causes forgetting), it dynamically routes the update to a specific branch of a LoRA tree based on gradient similarity,.

---

### **Architecture Visualization**

```text
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
*   **Source:**,,
*   **Operation:** As tokens flow in, the **Fast Memory** (Track A) updates its weights immediately using a standard optimizer (like the Muon component of M3).
*   **Goal:** To minimize the immediate prediction error for the current sentence.
*   **State:** This memory is volatile; it might be reset or decay quickly after the context window shifts,.

#### **2. The Slow Loop (TreeLoRA Layer)**
*   **Source:**,,
*   **Operation:**
    1.  **Accumulate:** The system accumulates gradients in the background for a specific **Chunk Size** (e.g., 1,000 steps). The Slow Memory is **frozen** during this time.
    2.  **Trigger:** Once the chunk ends, instead of a simple addition ($M^{(2)} + \sum g$), the **TreeLoRA Logic** activates.
    3.  **Route:** The **Bandit Algorithm** compares the chunk's gradient direction with the existing Tree Nodes (Root vs. Leaves). It finds the "Most Similar Task" in $O(1)$ time.
    4.  **Update:** It performs a **Sparse Update** only on the selected LoRA adapter (branch).
*   **Goal:** To store the knowledge from the last 1,000 steps permanently without overwriting (forgetting) the knowledge stored in other branches (e.g., overwriting "French grammar" with "Python syntax").

#### **3. The Aggregation**
*   **Source:**,
*   **Operation:** The final output of the MLP block is a weighted sum of the Fast MLP and the active TreeLoRA adapter.
    $$ y_t = \text{MLP}_{\text{Fast}}(x_t) + \alpha \cdot \text{TreeLoRA}_{\text{Selected}}(x_t) $$
*   **Result:** The model has the "reflexes" of the Fast Learner and the "wisdom" of the organized TreeLoRA structure.

### **Why this Integration Works (Synthesis)**
*   **CMS solves the "When":** It dictates that we shouldn't update long-term memory every second (which causes instability), but rather in consolidated chunks.
*   **TreeLoRA solves the "Where":** It dictates that when we *do* update long-term memory, we shouldn't just mash it into one matrix (which causes catastrophic forgetting), but route it to a specific semantic branch.
*   **Efficiency:** TreeLoRA's Bandit search avoids calculating gradients for all past tasks, making it fast enough to run during the "Online Consolidation" phase of Nested Learning.

Based on the **Nested Learning (NL)** paradigm and the architectures of **CMS (Continuum Memory Systems)** and **TreeLoRA** described in the sources, here is a visualization of a **Base-Transformer integrated with TreeLoRA and CMS**.

### **The Concept: "The Organized Memory"**
In this integrated architecture, we replace the standard static MLP block of a Transformer with a **CMS-TreeLoRA Hybrid Block**.
*   **CMS Role (Time):** Splits learning into "Fast" (immediate adaptation) and "Slow" (consolidation) frequencies,.
*   **TreeLoRA Role (Structure):** Organizes the "Slow" consolidation. Instead of overwriting long-term memory with a single average update (which causes forgetting), it dynamically routes the update to a specific branch of a LoRA tree based on gradient similarity,.

---

### **Architecture Visualization**

```text
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
*   **Source:**,,
*   **Operation:** As tokens flow in, the **Fast Memory** (Track A) updates its weights immediately using a standard optimizer (like the Muon component of M3).
*   **Goal:** To minimize the immediate prediction error for the current sentence.
*   **State:** This memory is volatile; it might be reset or decay quickly after the context window shifts,.

#### **2. The Slow Loop (TreeLoRA Layer)**
*   **Source:**,,
*   **Operation:**
    1.  **Accumulate:** The system accumulates gradients in the background for a specific **Chunk Size** (e.g., 1,000 steps). The Slow Memory is **frozen** during this time.
    2.  **Trigger:** Once the chunk ends, instead of a simple addition ($M^{(2)} + \sum g$), the **TreeLoRA Logic** activates.
    3.  **Route:** The **Bandit Algorithm** compares the chunk's gradient direction with the existing Tree Nodes (Root vs. Leaves). It finds the "Most Similar Task" in $O(1)$ time.
    4.  **Update:** It performs a **Sparse Update** only on the selected LoRA adapter (branch).
*   **Goal:** To store the knowledge from the last 1,000 steps permanently without overwriting (forgetting) the knowledge stored in other branches (e.g., overwriting "French grammar" with "Python syntax").

#### **3. The Aggregation**
*   **Source:**,
*   **Operation:** The final output of the MLP block is a weighted sum of the Fast MLP and the active TreeLoRA adapter.
    $$ y_t = \text{MLP}_{\text{Fast}}(x_t) + \alpha \cdot \text{TreeLoRA}_{\text{Selected}}(x_t) $$
*   **Result:** The model has the "reflexes" of the Fast Learner and the "wisdom" of the organized TreeLoRA structure.

### **Why this Integration Works (Synthesis)**
*   **CMS solves the "When":** It dictates that we shouldn't update long-term memory every second (which causes instability), but rather in consolidated chunks.
*   **TreeLoRA solves the "Where":** It dictates that when we *do* update long-term memory, we shouldn't just mash it into one matrix (which causes catastrophic forgetting), but route it to a specific semantic branch.
*   **Efficiency:** TreeLoRA's Bandit search avoids calculating gradients for all past tasks, making it fast enough to run during the "Online Consolidation" phase of Nested Learning.

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

M_t: model at t timestep
p(T) distribute of any random variable ^ZYEDa0km

L1 (LASSO) and L2 (Ridge) regularization are techniques adding penalty terms to a model's loss function to prevent overfitting by shrinking coefficients, but they differ in how they penalize: L1 uses absolute values, forcing some weights to exactly zero (feature selection/sparsity), while L2 uses squared values, shrinking all weights towards zero but keeping them non-zero (smoother shrinkage, handling multicollinearity). L1 creates simpler, sparse models; L2 creates more stable, complex models with evenly distributed weights

multicollinearity - 2 feature highly correlated, 2 neuron learn the same thing.  ^jVH9eZyX

Is $t \pmod f = 0?$<br>(Chunk Complete?) ^sU0GTZRn

Phase C: Weight Update ^0OErN8hT

Compute M3 Update Term:<br>$\frac{O^{(1)} + \alpha O^{(2)}}{\sqrt{V_t} + \epsilon}$ ^61zaqTYP

Update Weights:<br>$\Theta_t \leftarrow \Theta_{t-1} - \eta \cdot \text{Term}$ ^3glHsaV4


Phase B: Fast Memory (Muon + Adam) ^0rskxriU

Input: Gradient $g_t$, Weights $\Theta_{t-1}$ ^6GSEt8HG

Fast Update ^fK5Elgey

Update Fast Momentum $M^{(1)}$<br>($M^{(1)} + \beta_1 g_t$) ^VSD84GlD

Newton-Schulz Iteration<br>(Orthogonalize) ^WXr43BwG

Output Fast Direction $O^{(1)}$ ^Kq2lebGe

Update Variance $V_t$<br>($V_{t-1} + \beta_2 g_t^2$) ^RqWnAP9i

Calculate Denominator<br>($\sqrt{V_t} + \epsilon$) ^5tlKT9In


Phase A: Slow Memory (CMS) ^8N2ogdrB

Aggregate Chunk Gradients<br>($\sum g_i$) ^J6YfuEpx

Update Slow Momentum $M^{(2)}$<br>($M^{(2)} + \beta_3 \sum g$) ^7IOhH6Oj

Newton-Schulz Iteration<br>(Orthogonalize) ^YIhrbkUj

Update Frozen Anchor $O^{(2)}$ ^QYonEUWG

Retrieve Existing Frozen $O^{(2)}$ ^0Fk38SLc

Yes ^GUGGvZXr

No ^SUdMribU

Start Step $t$ ^QU2F7cO1

Next Step $t+1$ ^mhgiL1LI

## Embedded Files
07c397817d2d4bec7cc511dce5b811a6825de140: $$y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$$

bf46dad39ed1192f7350db19dd20e5fae48ba639: $$t \pmod f = 0?$$

bb3399ca9760b7590722699b403515f7cf7a6611: [[Pasted image 20260107144114.png]]

58cfe8ead52ecde8f4ce51e393faef298b6a7a1b: [[Pasted Image 20260110180129_992.png]]

4d7dee62f6ec906199fe7fafb3cfcf6dea696f1b: [[Pasted Image 20260110181704_838.png]]

afd289b35667e0e17dce59715e25d12d776501a9: [[Pasted Image 20260110181802_009.png]]

0262edc012448a1ab479c38006cd7cecf21e7ac3: [[Pasted Image 20260110182043_514.png]]

b145df64c80cdd91491c8d07f86d48944eb56b67: [[Pasted Image 20260110182143_442.png]]

22bb89089c2f5a08a41c1c79338a12624df7a8de: [[NL_AdaptiveLayerout.svg]]

%%
## Drawing
```compressed-json
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

TxwCFxKlzhNIgXgIAA==
```
%%