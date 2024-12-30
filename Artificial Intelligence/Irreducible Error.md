### What is Irreducible Error in Machine Learning ?
(Lỗi không thể tránh)
The **irreducible error** is the error that **cannot be reduced or eliminated**, even with the best possible model. This type of error arises due to the **intrinsic randomness or noise** in the data that no model can predict or capture.


### Sources of Irreducible Error:
1. **Measurement Noise:**
   - Errors in how data is collected or measured.
   - Example: Sensor inaccuracies, rounding errors, or human error in labeling.

2. **Unmeasured Variables:**
   - Variables affecting the target output but not included in the model.
   - Example: Predicting house prices without considering neighborhood crime rates.

3. **Intrinsic Variability:**
   - Randomness inherent in the system being modeled.
   - Example: Predicting stock market prices, where external, unpredictable events can affect outcomes.

4. **Complex Systems:**
   - Systems where the behavior cannot be completely captured by mathematical models.
   - Example: Weather systems, where minor environmental changes can lead to vastly different outcomes.

---

### **Why Is It Important?**
- Irreducible error sets the **upper bound for model performance**.
- Even with perfect bias-variance tradeoff, this error remains.
- Overfitting to irreducible noise increases variance unnecessarily, worsening generalization.

---

### **Example in Context:**
- Suppose you're building a model to predict students' exam scores based on study hours. If a student has a bad day (e.g., feeling unwell or distracted during the exam), their score may deviate unpredictably. This variability is irreducible and cannot be captured by your model.

Would you like an illustration or example code to demonstrate irreducible error?