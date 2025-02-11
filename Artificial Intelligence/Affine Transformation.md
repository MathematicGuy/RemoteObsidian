## Affine Transformation: A Fundamental Image Registration Technique

### 1. What is Affine Transformation?

Affine transformation is a **linear mapping technique** that preserves **points, straight lines, and planes** while allowing transformations like **scaling, rotation, translation, and shearing**. It is commonly used in **image processing, computer vision, and medical image registration** to align images.

Mathematically, an **affine transformation** can be represented as:

T(x)=Ax+tT(x) = A x + t

where:

- xx is the original coordinate vector **(x, y)**,
- T(x)T(x) is the transformed coordinate vector **(x', y')**,
- AA is a **2×2 transformation matrix** (controls scaling, rotation, shearing),
- tt is a **translation vector** (shifts the image in x and y directions).

---

### **2. Types of Affine Transformations**

Affine transformation consists of multiple operations:

1. **Translation (Shifting)**  
    Moves an image without changing its shape.
    
    x′=x+tx,y′=y+tyx' = x + t_x, \quad y' = y + t_y
    - Example: Moving an image **5 pixels right and 3 pixels down**.
2. **Scaling (Resizing)**  
    Stretches or compresses an image.
    
    x′=Sx⋅x,y′=Sy⋅yx' = S_x \cdot x, \quad y' = S_y \cdot y
    - Example: Scaling **by 2x in width and 1.5x in height**.
3. **Rotation**  
    Rotates the image by an angle θ\theta.
    
    [x′y′]=[cos⁡θ−sin⁡θsin⁡θcos⁡θ][xy]\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
    - Example: Rotating an image **by 45 degrees**.
4. **Shearing (Skewing)**  
    Slants the image along the x- or y-axis.
    
    [x′y′]=[1shxshy1][xy]\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} 1 & sh_x \\ sh_y & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
    - Example: A **shear factor of 0.5** skews the image diagonally.

---

### **3. General Affine Transformation Matrix**

A **2D affine transformation matrix** is:

A=[a11a12txa21a22ty]A = \begin{bmatrix} a_{11} & a_{12} & t_x \\ a_{21} & a_{22} & t_y \end{bmatrix}

which transforms a point (x,y)(x, y) into (x′,y′)(x', y') as:

[x′y′1]=[a11a12txa21a22ty001][xy1]\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} a_{11} & a_{12} & t_x \\ a_{21} & a_{22} & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

- **a11,a22a_{11}, a_{22}** control **scaling**.
- **a12,a21a_{12}, a_{21}** control **rotation and shearing**.
- **tx,tyt_x, t_y** control **translation**.

---

### **4. Affine Transformation in Medical Image Registration**

In **medical imaging**, affine transformations are used to:

- **Align multi-modal images (CT, MRI, PET)** before analysis.
- **Track tumor progression** in follow-up scans.
- **Correct distortions** from patient movement.

Example: A **brain MRI scan** might be **affinely registered** to a reference scan to correct slight head movements.

---

### **5. Conclusion**

✅ **Affine transformation is a fundamental image registration method** that aligns images through **scaling, rotation, translation, and shearing**.  
✅ It is widely used in **medical imaging, robotics, and augmented reality**.  
✅ For **non-linear deformations (e.g., organ shifting, elastic tissues), deformable registration is needed**.

Would you like a **Python example using OpenCV or SimpleITK**? 🚀