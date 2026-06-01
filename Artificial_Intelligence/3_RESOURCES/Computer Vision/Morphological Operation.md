## Morphological (hình thái) Operation
The most [basic morphological operations](https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html) are: Erosion and Dilation. They have a wide array of uses, i.e. :
- Removing noise
- Isolation of individual elements and joining disparate elements in an image.
- Finding of intensity bumps or holes in an image

 **Original Image**
	![[Pasted image 20250207091354.png]]


## Morphological Operation Example

**Input Image (3x3):**

$$
I = \begin{bmatrix}
10 & 20 & 30 \\
40 & 50 & 60 \\
70 & 80 & 90
\end{bmatrix}
$$

**Kernel (Structuring Element - SE, 3x3)** *(Anchor at center)*:

$$
SE = \begin{bmatrix}
1 & 1 & 1 \\
1 & \textbf{1} & 1 \\
1 & 1 & 1
\end{bmatrix}
$$

> **Note:** Anchor point is at the bolded center position.

To keep things simple, we focus on calculating only at the central pixel $(1,1)$:


### 🔹 **1. Dilation Example** (phép giãn)
[visualize dilation](https://www.youtube.com/watch?v=xO3ED27rMHs)
![[Pasted image 20250207091443.png]]
>Dialation include **convolving an image (A) with some kernel (B)** which can have any shape and size, usually square or circle. Each **convolve pick the maximum value inside the kernel each pixel across the image**. (e.g. 1 out of `[0, 1]`)

Performing dilation at the center pixel position $(1,1)$:

- **Step-by-step:**
  - Place kernel aligned with the center pixel, covering:
  
$$
\begin{bmatrix}
10 & 20 & 30 \\
40 & \textbf{50} & 60 \\
70 & 80 & 90
\end{bmatrix}
$$

- Take the **maximum** value from this area:

$$
(I \oplus SE)(1,1) = \max\{10,20,30,40,50,60,70,80,90\} = 90
$$

**Where**:  
- $I$ is the input image.  
- $SE$ is the structuring element (kernel).  
- $\oplus$ represents dilation.


### 🔹 **2. Erosion Example** (phép co)
[visualize erosion](https://www.youtube.com/watch?v=fmyE7DiaIYQ)
![[Pasted image 20250207091514.png]]
>Erosion is the same as Dilation except for it picking Minimum value (e.g. 0 out of `[0, 1]`) 

Performing erosion at the center pixel position $(1,1)$:
- **Step-by-step:**
  - Again, the kernel covers the same central area:

  $$
  \begin{bmatrix}
  10 & 20 & 30 \\
  40 & 50 & 60 \\
  70 & 80 & 90
  \end{bmatrix}
  $$

  - Select **minimum** pixel value from this region:

  $$
  (I \ominus SE)(1,1) = \min\{10,20,30,40,50,60,70,80,90\} = 10
  $$

**Where**:  
- $I$, $SE$ as previously defined.

---
### 🔹 **Summary of Results:**

| Operation | Result at (1,1) | Explanation                         |
|-----------|-----------------|-------------------------------------|
| Dilation  | 90              | Maximum value within kernel region  |
| Erosion   | 10              | Minimum value within kernel region  |

- **Dilation** picks the brightest pixel under the kernel, enlarging brighter regions.
- **Erosion** picks the darkest pixel, shrinking bright regions or enlarging darker ones.

### Openning (Phép mở: co -> giãn)
### Closing (Phép đóng: giãn -> co)
![[Pasted image 20250317095557.png]]
