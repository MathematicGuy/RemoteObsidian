Define as the cosine of the angle between the vectors that **means this measure is scaling variant** or other words **uneffected by the length of vectors being compred.**
![[Pasted image 20250216165611.png]]
= *dot product of the vector* / *vector magnitude*
![[Pasted image 20250216165559.png]]

Range of value from $[-1, 1]$
> Similar if the value is 1. and unsimiliar if the value -1 
> If the value is 0, the vectors is ogthonal (vuông góc) or independent. 

---

### **Why Use Cosine Similarity and Not Sine?**

Cosine similarity is widely used in **vector comparison**, **machine learning**, and **information retrieval** because it effectively **measures the angle between two vectors**. However, you might wonder **why cosine similarity is preferred over sine similarity**.

Let’s break it down **step-by-step** with visualizations.

---

### **1️⃣ Cosine and Sine in Vector Comparison**

#### **Cosine Similarity Formula**

cos⁡(θ)=A⋅B∣∣A∣∣⋅∣∣B∣∣\cos(\theta) = \frac{A \cdot B}{||A|| \cdot ||B||}

where:

- A⋅BA \cdot B is the **dot product** of vectors AA and BB.
- ∣∣A∣∣||A|| and ∣∣B∣∣||B|| are the **magnitudes** (lengths) of the vectors.
- θ\theta is the **angle between the vectors**.

✅ **Cosine similarity** measures **how aligned two vectors are**.

#### **Sine Similarity Formula**

sin⁡(θ)=∣∣A×B∣∣∣∣A∣∣⋅∣∣B∣∣\sin(\theta) = \frac{||A \times B||}{||A|| \cdot ||B||}

where:

- ∣∣A×B∣∣||A \times B|| is the **magnitude of the cross product**.
- ∣∣A∣∣⋅∣∣B∣∣||A|| \cdot ||B|| normalizes the result.

❌ **Sine measures the perpendicularity** between vectors, **not alignment**.

---

### **2️⃣ Why Use Cosine Instead of Sine?**

#### **Cosine captures similarity (Alignment)**

- When **θ=0∘\theta = 0^\circ (vectors are identical)** → **cos⁡(0)=1\cos(0) = 1** (Max Similarity ✅).
- When **θ=90∘\theta = 90^\circ (vectors are perpendicular)** → **cos⁡(90)=0\cos(90) = 0** (No Similarity ❌).
- When **θ=180∘\theta = 180^\circ (opposite direction)** → **cos⁡(180)=−1\cos(180) = -1** (Completely Opposite ❌).

#### **Sine captures dissimilarity (Perpendicularity)**

- When **θ=0∘\theta = 0^\circ (vectors are identical)** → **sin⁡(0)=0\sin(0) = 0** (Not useful ❌).
- When **θ=90∘\theta = 90^\circ (vectors are perpendicular)** → **sin⁡(90)=1\sin(90) = 1** (Highest Value ✅).
- When **θ=180∘\theta = 180^\circ (opposite direction)** → **sin⁡(180)=0\sin(180) = 0** (Not useful ❌).

✅ **Cosine similarity focuses on alignment (useful for similarity measurements).**  
❌ **Sine similarity focuses on perpendicularity (useful in physics, but not for similarity).**

---

### **3️⃣ Visualization: Cosine vs. Sine**

Let's **visualize this** in Python to see how cosine and sine change with different angles.

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate angles from 0 to 180 degrees
angles = np.linspace(0, 180, 100)
cos_values = np.cos(np.radians(angles))
sin_values = np.sin(np.radians(angles))

# Plot the Cosine and Sine values
plt.figure(figsize=(8,5))
plt.plot(angles, cos_values, label='Cosine Similarity', color='b')
plt.plot(angles, sin_values, label='Sine Function', color='r', linestyle='dashed')

# Labels and title
plt.xlabel('Angle (Degrees)')
plt.ylabel('Similarity Value')
plt.title('Cosine vs. Sine in Vector Similarity')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid()

# Show plot
plt.show()
```
![[Pasted image 20250216170607.png]]

---

### **4️⃣ Interpretation of the Graph**

- **Cosine starts at 1 (max similarity at 0°), gradually decreases to -1 (opposite direction at 180°).**
- **Sine starts at 0, peaks at 90° (perpendicularity), then returns to 0 at 180° (no useful pattern for similarity).**
- **Cosine gives a smooth measure of alignment, while sine does not.**

---

### **5️⃣ Conclusion**

✅ **Cosine similarity is used because it directly measures alignment, which is key for similarity measurements.**  
❌ **Sine similarity focuses on perpendicularity, which is less relevant for comparing vector directions.**

