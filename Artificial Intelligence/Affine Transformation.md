## Image Transformation
+ ? How to do all of these Transformation using JUST 1 MATRIX.
![[Pasted image 20250216162053.png]]

**Identity Matrix:** this do nothing at all $A \times I = I \times A$ 
![[Pasted image 20250216162130.png]]

**Changing in the upper left element:** perform horizontal scale. 
![[Pasted image 20250216162812.png]]

**Changing the bottom right element:** perform verticle  scale.
![[Pasted image 20250216163028.png]]
 
**When we make either elements negative** it produces a reflection
![[Pasted image 20250216163155.png]]
![[Pasted image 20250216163259.png]]

The **Upper right element corresponds to a horizontal sheer (X-Axis Sheer)** 
![[Pasted image 20250216163415.png]]
And the **Lower left is a vertical sheer (Y-Axis Sheer)**
![[Pasted image 20250216163458.png]]

+ ? **So where do rotation come from**
We start by sheer horizontally,
![[Pasted image 20250216163632.png]]
 then apply verticlally by the same amount
![[Pasted image 20250216163642.png]]

+ $ This is infact a popular way to implement image rotations, because all you do is translate each row by a different amount and then translate each collumn
+ ? note: divide the image by half then translate the 1st half left, 2nd half right. 
![[Pasted image 20250216163747.png]]
+ ? note: divide the image by half, 1st half down, 2nd half up
![[Pasted image 20250216163806.png]]

+ ? So this matrix create a rotation by 2 sheers. But how can we specify the **angle of rotation** ?
+ $ The $\sin(\theta)$ and $\cos(\theta)$ funciton could convert value into angle, it converts from an angles to the right shear amount.  
![[Pasted image 20250216164759.png]]
**Change the angle results**: image size change a bit as it rotate.
![[Pasted image 20250216164627.png]]
So we need to correct this size change, and it turns out scaling by the cosine function exactly counteracts this size change.
![[Pasted image 20250216170831.png]]
When combine together sine and cosine produce a perfect rotation. 
![[Pasted image 20250216170940.png]]


## 3D Matrix Transformation
Along the **diagnol entries are corresponding to x, y and z**
And **all the rest are Sheer**. (because each dimension have 2 others dimension so 1 * 2 = 2 ways to Sheer each dimension)
**The X-Axis**: 
+ ? sheer **toward the X-Axis and around the Z-axis** ![[Pasted image 20250216172012.png]]
+ ? sheer **toward the X-Axis and around the Y-axis** ![[Pasted image 20250216171252.png]]


**The Y-Axis:**
+ ? sheer **toward the Y-Axis and along the X-axis** ![[Pasted image 20250216173102.png]]
+ ? sheer **toward the Y-Axis and along the Z-axis**  ![[Pasted image 20250216173043.png]]


**The Z-Axis**
+ ? sheer **toward the Z-Axis and along the Y-axis** ![[Pasted image 20250216172329.png]]
+ ? sheer **toward the Z-Axis and along the X-axis** ![[Pasted image 20250216172321.png]]

Using all the value above, we can Rotate the image around the 
+ **Z-Axis** (Yawn) by
	**Rotate X around trục Z-axis**![[Pasted image 20250216174124.png]]
	**Rotate Y around Z-axis** ![[Pasted image 20250216174116.png]]
	The rest are of X, Y and Z value. As you can see **Z value remain, just X and Y changes to perform rotation**. ![[Pasted image 20250216173407.png]]

+ **Y-Axis** (Pitch) ![[Pasted image 20250216173418.png]]
+ **X-Axis** (Roll) ![[Pasted image 20250216173435.png]]

This should move the x origin to the right by 1, 
![[Pasted image 20250216175036.png]]
**If X and Y equal 0**, this is impossible **because all matrixes map the zero vector to itself**, this mean 2 by 2 matrix can't do translation. 
(ma trận nhân với ma trận đơn vị không thay đổi)
![[Pasted image 20250216175727.png]]

However there a trick , let add a 1 to the bottom to make the vector into a 3D vector.  
![[Pasted image 20250216175515.png]]

And as you can guess, translation in 2D is basically sheer along the X-Axis in 3D. 
![[Pasted image 20250216180742.png]]

We saw a connect between 2D and 3D, the sheer translate the rows. In 3D, If we slice the cube into planes, each slices is translate by a different amount by the sheer. 
![[Pasted image 20250216180500.png]]
So if we think of our 2D image as the face of the z equal 1 planes. We can do any 2D matrix transformation and any translation using these elements of the 3 by 3 matrix. 
![[Pasted image 20250216181042.png]]

The 2D vector represent in 3D are called homogeneous coordinates.
![[Pasted image 20250216181125.png]]
The same thing work for higher dimensions. (i.e. 3D represent 4D)
![[Pasted image 20250216181157.png]]

---

1) Extract Point from Feature
2) Find x', y' (desired transformation coordinate) using parameters *a* 
![[Pasted image 20250216182528.png]]
![[Pasted image 20250216182601.png]]



---
## Affine Transformation: A Fundamental Image Registration Technique

### **1. What is Affine Transformation?**
Affine transformation is a **linear mapping technique** that preserves **points, straight lines, and planes** while allowing transformations like **scaling, rotation, translation, and shearing**. It is commonly used in **image processing, computer vision, and medical image registration** to align images.

Mathematically, an **affine transformation** can be represented as:

$$
T(x) = A x + t
$$

where:
- $x$ is the original coordinate vector **(x, y)**,
- $T(x)$ is the transformed coordinate vector **(x', y')**,
- $A$ is a **2×2 transformation matrix** (controls scaling, rotation, shearing),
- $t$ is a **translation vector** (shifts the image in x and y directions).

---

### **2. Types of Affine Transformations**
Affine transformation consists of multiple operations:

3. **Translation (Shifting)**  
   Moves an image without changing its shape.
   $$
   x' = x + t_x, \quad y' = y + t_y
   $$
   - Example: Moving an image **5 pixels right and 3 pixels down**.

4. **Scaling (Resizing)**  
   Stretches or compresses an image.
   $$
   x' = S_x \cdot x, \quad y' = S_y \cdot y
   $$
   - Example: Scaling **by 2x in width and 1.5x in height**.

5. **Rotation**  
   Rotates the image by an angle $\theta$.
   $$
   \begin{bmatrix} x' \\ y' \end{bmatrix} =
   \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
   \begin{bmatrix} x \\ y \end{bmatrix}
   $$
   - Example: Rotating an image **by 45 degrees**.

6. **Shearing (Skewing)**  
   Slants the image along the x- or y-axis.
   $$
   \begin{bmatrix} x' \\ y' \end{bmatrix} =
   \begin{bmatrix} 1 & sh_x \\ sh_y & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \end{bmatrix}
   $$
   - Example: A **shear factor of 0.5** skews the image diagonally.

---

### **3. General Affine Transformation Matrix**
A **2D affine transformation matrix** is:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & t_x \\
a_{21} & a_{22} & t_y
\end{bmatrix}
$$

which transforms a point $(x, y)$ into $(x', y')$ as:

$$
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
\begin{bmatrix}
a_{11} & a_{12} & t_x \\
a_{21} & a_{22} & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

- **$a_{11}, a_{22}$** control **scaling**.
- **$a_{12}, a_{21}$** control **rotation and shearing**.
- **$t_x, t_y$** control **translation**.

---

### **4. Affine Transformation in Medical Image Registration**
In **medical imaging**, affine transformations are used to:
- **Align multi-modal images (CT, MRI, PET)** before analysis.
- **Track tumor progression** in follow-up scans.
- **Correct distortions** from patient movement.

Example: A **brain MRI scan** might be **affinely registered** to a reference scan to correct slight head movements.
![[Pasted image 20250216160143.png]]

