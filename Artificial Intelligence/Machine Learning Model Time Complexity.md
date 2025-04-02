Here’s a summary of the **time complexity** of **Linear Regression**, **Random Forest**, and **Gradient Boosting**, both for **training** and **inference**:

---

### 1. 🧮 Linear Regression

|Phase|Time Complexity|
|---|---|
|**Training**|$O(n \cdot d^2 + d^3)$ (Normal Equation) or $O(n \cdot d)$ per iteration (Gradient Descent)|
|**Inference**|$O(d)$ per sample|

- **n** = number of training samples
    
- **d** = number of features
    
- Super fast for small or medium-sized datasets.
    
- Scales poorly if **features (d)** are huge due to matrix inversion.
    

---

### 2. 🌲 Random Forest

| Phase         | Time Complexity                            |
| ------------- | ------------------------------------------ |
| **Training**  | $O(t \cdot m \cdot \log m \cdot d)$        |
| **Inference** | $O(t \cdot \text{tree\_depth})$ per sample |
|               |                                            |

- **t** = number of trees
    
- **m** = number of samples per tree (usually close to n)
    
- Grows trees in parallel → great for parallelization.
    
- **Slower inference** than linear models if there are many trees or deep trees.
    

---

### 3. 🔥 Gradient Boosting (e.g., XGBoost, LightGBM)

| Phase         | Time Complexity                            |
| ------------- | ------------------------------------------ |
| **Training**  | $O(t \cdot m \cdot \log m \cdot d)$        |
| **Inference** | $O(t \cdot \text{tree\_depth})$ per sample |

- Same **asymptotic** training time as Random Forest, but it runs **sequentially**, so it's **slower** in practice.
    
- Highly optimized versions like **LightGBM** and **XGBoost** use histogram-based or leaf-wise methods to improve performance.
    

---

### 🧠 Summary Table

| Model             | Training Time                          | Inference Time                     | Notes                                |
| ----------------- | -------------------------------------- | ---------------------------------- | ------------------------------------ |
| Linear Regression | Fast ($O(n \cdot d^2)$)                | Very fast ($O(d)$)                 | Best for large **d**, simple tasks   |
| Random Forest     | Medium ($O(t \cdot m \log m \cdot d)$) | Medium ($O(t \cdot \text{depth})$) | Trees can be trained in **parallel** |
| Gradient Boosting | Slower (sequential trees)              | Medium                             | High accuracy, more tuning needed    |

---

Let me know if you want memory complexity or runtime comparison in practice!