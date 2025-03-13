## Object Detection Performance
![[Pasted image 20250310093745.png]]

## Prior Development Model 
### DPM 
+ $ Uses **HOG features (Histogram of Oriented Gradients) + SVM classifiers** to detect objects with part-based models.
+ ? HOG features analyzing the distribution of gradient orientations (hướng gradient) within localized regions -> Good at pedestrian detection where detailed shape information is crucial -> Negative side: It slow.
![[Pasted image 20250310093906.png]]
### R-CNN 
+ $ Uses **Selective Search** for region proposals to generate approximately 2,000 region proposals from an input image. Each proposed region is then resized and fed into a **Convolutional Neural Network (CNN)** to extract features. These features are then classified (usually) with SVM. 
![[Pasted image 20250310094012.png]]

## Problems and Solutions

### **1. Complexity of Traditional Object Detection Pipelines**

### Problem: Multi-stage Pipelines (R-CNN, Fast R-CNN)
- Traditional object detection (like **R-CNN** and **Fast R-CNN**) involves **multiple separate steps**, such as:
    1. **Region Proposal** (Selective Search, Edge Boxes, etc.).
    2. **Feature Extraction** (CNN on each region proposal).
    3. **Classification** (SVM or softmax classifiers).
    4. **Bounding Box Refinement** (Post-processing adjustments).
    5. **Non-Maximum Suppression (NMS)** to remove duplicate detections.
    
- Each step is **trained separately**, making it **slow and hard to optimize**.

### YOLOv1 Solution: Unified Detection

- YOLO **frames detection as a single regression problem**.
- A **single neural network predicts**:
    - **Bounding boxes**.
    - **Class probabilities**.
    - **Confidence scores**.
	
- Eliminates region proposals and complex pipelines, making it **faster and more efficient**.


## **2. Speed and Real-time Object Detection**

### Problem: Traditional Methods are Slow

- **R-CNN takes ~40 seconds per image** (not real-time).
- **Fast R-CNN is faster but still not real-time** (~0.5 FPS).
- Object detection is critical for real-time applications like:
    - **Autonomous driving**.
    - **Robotics**.
    - **Video surveillance**.

### YOLOv1 Solution: Speed Optimization
- Instead of classifying multiple proposals, **YOLO looks at the entire image once**.
	- YOLO **processes images at 45 FPS** on a Titan X GPU.
	- A smaller version, **Fast YOLO**, runs at **155 FPS**.

## **3. Background Errors and False Positives**

### Problem: Contextual Understanding in Detection

- **R-CNN and Fast R-CNN detect objects without considering the whole image**.
- They may misclassify **background patches** as objects because they don’t consider **global context**.
- Example: **Fast R-CNN often detects background textures as objects**.

### YOLOv1 Solution: Global Reasoning

- Since **YOLO sees the entire image at once**, it **understands context** better.
- **Reduces background false positives** significantly compared to Fast R-CNN.
- Uses **spatial constraints (grid system)** to prevent excessive duplicate detections.

---

## **4. Generalization to Unseen Domains**

### Problem: Poor Generalization in Traditional Methods

- **Region proposal methods** (e.g., Selective Search in R-CNN) are **optimized for natural images**.
- They **fail to generalize** when applied to:
    - **Artwork**.
    - **Other non-standard datasets** (e.g., medical images, aerial images).

### YOLOv1 Solution: Strong Generalization

- **Trains on full images instead of patches**.
- Learns **general features** that work across domains.
- **Outperforms Fast R-CNN, DPM, and R-CNN** on **artwork datasets** like the **Picasso and People-Art datasets**.

---

## **5. Localization Issues in Traditional Methods**

### Problem: Poor Bounding Box Prediction in Sliding Window Approaches

- **DPM and R-CNN use sliding windows or region proposals**, leading to:
    - **Multiple overlapping detections**.
    - **Imprecise localization** (bounding boxes are not refined end-to-end).
- Bounding box refinement is **separate** from classification, making it **less accurate**.

### YOLOv1 Solution: Direct Bounding Box Regression

- Uses **a single CNN to predict bounding boxes directly**.
- Each **grid cell** predicts **bounding boxes and class scores simultaneously**.
- Improves localization consistency across the image.


![[Pasted image 20250310093658.png]]


## Summary of Problems Solved by YOLOv1

|**Problem**|**Traditional Method Limitation**|**YOLOv1 Solution**|
|---|---|---|
|**Complexity of Pipelines**|R-CNN and Fast R-CNN require multiple stages (region proposals, classification, refinement).|YOLO is **end-to-end**, combining all steps into **one neural network**.|
|**Slow Speed**|R-CNN takes ~40s/image, Fast R-CNN ~0.5 FPS.|YOLO runs **45 FPS**, Fast YOLO at **155 FPS**.|
|**Background False Positives**|Fast R-CNN mistakes background textures for objects.|YOLO sees the **entire image**, reducing false positives.|
|**Poor Generalization**|Traditional methods overfit to natural images, failing on artwork and new domains.|YOLO generalizes well, **outperforming R-CNN on artwork datasets**.|
|**Localization Issues**|Sliding window approaches struggle with accurate bounding boxes.|YOLO predicts **bounding boxes directly** via **single regression**.|

# YOLOv1 Architecture Break Down
![[Pasted image 20250310081138.png]]
1. **Input Layer**:
    - The input is a **448×448×3** image.
    - The network processes the entire image in a single pass.
    
2. **Convolutional Layers (Feature Extraction)**:
    - The first layer applies a **7×7** convolution with **64 filters** and a **stride of 2**, followed by a **2×2 max pooling** layer.
    - Next, **3×3 convolutions** are applied with increasing filter sizes (from **192 to 1024** filters).
    - Several **1×1 convolutions** are used for dimensionality reduction before **3×3 convolutions** (similar to GoogLeNet).
    - After every few convolutional layers, **max-pooling layers (2×2, stride 2)** are used to reduce spatial dimensions.
    
3. **Fully Connected Layers (Bounding Box & Class Prediction)**:
    - The final convolutional layers output a **7×7×1024** feature map.
    - This feature map is **flattened and passed through two fully connected layers** with **4096 neurons**.
    - The last layer produces a **7×7×30** output tensor.

## YOLOv1 Output Representation

- The **final output tensor (7×7×30)** represents predictions for **each grid cell** in the **7×7 grid**.
- Each grid cell predicts:
    - **B = 2 bounding boxes** → 5 values each: **(x, y, w, h, confidence)**.
    - **C = 20 class probabilities** for **PASCAL VOC dataset**.
- **Total output per cell:** 2×5+20=302 \times 5 + 20 = 30.
![[Pasted image 20250310101725.png]]

## Key Architectural Insights:
1. **End-to-End Learning:** The entire network is trained as a single system without separate region proposals.
2. **Fast Inference:** The CNN processes the full image in one forward pass.
3. **Downsampling via Strides & Pooling:** Reduces computation while maintaining relevant spatial information.

# Summary of Architecture Layers:

| **Layer Type**  | **Filter Size** | **Stride** | **Number of Filters** | **Output Size** |
| --------------- | --------------- | ---------- | --------------------- | --------------- |
| Input Image     | -               | -          | -                     | **448×448×3**   |
| Conv + MaxPool  | 7×7             | 2          | 64                    | **112×112×64**  |
| Conv + MaxPool  | 3×3             | 1          | 192                   | **56×56×192**   |
| Conv Layers     | 1×1, 3×3        | 1          | 256, 512              | **28×28×512**   |
| Conv Layers     | 1×1, 3×3        | 1          | 512, 1024             | **14×14×1024**  |
| Conv Layers     | 3×3             | 2          | 1024                  | **7×7×1024**    |
| Fully Connected | -               | -          | 4096                  | **1×1×4096**    |
| Output Layer    | -               | -          | 30                    | **7×7×30**      |


# PASCAL VOC Dataset

The **PASCAL VOC (Visual Object Classes)** dataset is a benchmark dataset used for object detection and image classification. It provides annotated images for evaluating object detection models.
### Key Features of PASCAL VOC:
- Contains 20 object classes across multiple categories (animals, vehicles, indoor objects, etc.).
- Provides **bounding box annotations** for object detection.
- Used for training and evaluating object detection models.
- Versions: **VOC 2007, VOC 2010, VOC 2012** (each having different dataset sizes and annotation improvements).

### What Does PASCAL VOC Dataset Look Like?**

The dataset contains **real-world images** with:
- **Objects of various categories** (animals, vehicles, household items, etc.).
- **Bounding box annotations** (for object detection).
- **Pixel-wise segmentation masks** (for segmentation tasks).
- **Class labels** (for classification tasks).

#### Example Image with Annotations
A typical image in **PASCAL VOC** comes with:
- A **RGB image**.
- **Bounding box annotations** indicating where objects are.
- **Class labels** assigned to objects.

+ ? **Example**:
	- An image showing a **dog and a person**.
	- Bounding boxes labeled **"dog"** and **"person"**.
	- If segmentation is included, pixel masks highlight the **object shape**.

The **evaluation metric** used is **Mean Average Precision (mAP)**, which calculates how well the model detects objects across all categories.

---
# YOLO Training Loss Function
The **loss function in YOLO** is a **multi-component sum-squared error function** that optimizes both classification and localization performance.

$$\lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{obj}}_{ij} \left[ (x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2 \right] 
$$
$$+ \lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{obj}}_{ij} \left[ (\sqrt{w_i} - \sqrt{\hat{w}_i})^2 + (\sqrt{h_i} - \sqrt{\hat{h}_i})^2 \right]$$$$+ \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{obj}}_{ij} (C_i - \hat{C}_i)^2 $$$$+\lambda_{\text{noobj}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{noobj}}_{ij} (C_i - \hat{C}_i)^2$$ $$ + \sum_{i=0}^{S^2} \mathbf{1}^{\text{obj}}_{i} \sum_{c \in \text{classes}} (p_i(c) - \hat{p}_i(c))^2$$

### Each Term Explanation :
#### 0. Double Sum Meaning
$$\sum^{S^2}_{i=0}\sum^{B^2}_{j=0}$$
**where**
- **i** indexes the grid cells in the **$S \times S$** grid (total **$S^2$** cells).
- **$j$** indexes the **$B$** bounding boxes **per grid cell**.
+ n number of cell
Each grid cell predicts **$B$** bounding boxes, so the loss function iterates through all combinations of:
- **Grid cells ($S^2$)** (1 cell ~ literally 1 square / group of pixels)
- **Bounding boxes ($B$) per cell**. (1 Object can have many Bounding Box)
- ![[Pasted image 20250310102527.png]]
![[Pasted image 20250310093221.png]]
#### 1. Localization Loss (Bounding Box Coordinates)

$$\lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{obj}}_{ij} \left[ (x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2 \right]$$

- **Purpose:** Measures the error in the predicted center coordinates **x, y** of the bounding box.
- **Variables:**
    - $x_i, y_i$ → Ground truth center coordinates.
    - $\hat{x}_i, \hat{y}_i$ → Predicted center coordinates.
    - $\mathbf{1}^{\text{obj}}_{ij}$ → Indicator function (=1 if object exists in the cell, else =0).
    - **$\lambda_{\text{coord}} = 5$** → Increases weight for coordinate errors.

#### 2. Localization Loss (Bounding Box Size)

$$\lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{obj}}_{ij} \left[ (\sqrt{w_i} - \sqrt{\hat{w}_i})^2 + (\sqrt{h_i} - \sqrt{\hat{h}_i})^2 \right]$$

- **Purpose:** Penalizes the difference in width and height predictions **w,hw, h**.
- **Why use the square root?**
    - Small objects should be penalized more.
    - Large objects should have lower sensitivity.
- **Variables:**
    - $w_i, h_i$ → Ground truth width and height.
    - $\hat{w}_i, \hat{h}_i$ → Predicted width and height.

#### 3. Object Confidence Loss (When an Object is Present)

$$\sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{obj}}_{ij} (C_i - \hat{C}_i)^2$$

- **Purpose:** Measures the confidence score error.
- **Variables:**
    - $C_i$ → Ground truth confidence (calc using IOU between prediction and actual box).
    - $\hat{C}_i$ → Predicted confidence score.
    - **$C = Pr(Object) \times IOU_{\text{truth}, \text{pred}}$**.

#### 4. No Object Confidence Loss (Background Regions)

$$\lambda_{\text{noobj}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbf{1}^{\text{noobj}}_{ij} (C_i - \hat{C}_i)^2$$

- **Purpose:** Prevents false positives in empty grid cells.
- **$\lambda_{\text{noobj}} = 0.5$** reduces the penalty for background regions.

#### 5. Classification Loss

$$\sum_{i=0}^{S^2} \mathbf{1}^{\text{obj}}_{i} \sum_{c \in \text{classes}} (p_i(c) - \hat{p}_i(c))^2$$

- **Purpose:** Measures how well YOLO predicts the correct object class.
- **Variables:**
    - $p_i(c)$ → True probability of class cc.
    - $\hat{p}_i(c)$ → Predicted probability of class cc.

## Summary of Loss Function Components

| **Loss Component**                  | **Purpose**                                                | **Weight**                     |
| ----------------------------------- | ---------------------------------------------------------- | ------------------------------ |
| **Bounding Box Center (x, y) Loss** | Ensures accurate position of detected objects.             | $\lambda_{\text{coord}} = 5$   |
| **Bounding Box Size (w, h) Loss**   | Penalizes incorrect bounding box dimensions.               | $\lambda_{\text{coord}} = 5$   |
| **Confidence Loss (Object Exists)** | Encourages accurate confidence score for detected objects. | 1                              |
| **Confidence Loss (No Object)**     | Reduces false positives in empty grid cells.               | $\lambda_{\text{noobj}} = 0.5$ |
| **Classification Loss**             | Ensures correct object class is predicted.                 | 1                              |


- The **higher weight on localization $\lambda_{\text{coord}}$** forces the model to focus on precise bounding boxes.
- **Lower weight on no-object confidence $\lambda_{\text{noobj}}$** prevents over-penalization for detecting background.
- **Square root for width/height** balances error impact on small vs. large objects.

