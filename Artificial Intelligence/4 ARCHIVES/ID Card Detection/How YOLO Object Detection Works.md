![[Pasted image 20241120112308.png]]

Each Cell in the SxS Grid have a class probabilities and multiple Bouding Box vector for multiple object prediction.
![[Pasted image 20241120112354.png]]

In real world, Class and Bounding Box vector are put into 1 vector size $(B \times 5 + n)$ where
	B: Bounding Box
	n: Number of cell
	S: grid size
![[Pasted image 20241120112616.png]]

Turn input image into vector using CNN
![[Pasted image 20241120112830.png]]

**Ground truth**
>ground truth: blue
>prediction: green
![[Pasted image 20241120113020.png]]

Each class are mutually exclusive, so YOLO can predict multiple classes, but now let focus on dog class only. 
![[Pasted image 20241120113136.png]]
![[Pasted image 20241120113318.png]]

**Confidence:** does an object appear in this grid cell or not ?
For every grid cell except for those grid cell with the dog there. 
![[Pasted image 20241120113436.png]]

>The fomula show the degree of overlap
![[Pasted image 20241120113523.png]]

The ground true of the IoU is the IoU of the predicted and ground boxes.
![[Pasted image 20241120113700.png]]
+ ? But each grid cells can produce multiple boxes, how can we choose ?

![[Pasted image 20241120113757.png]]
Similarly during inference if we have two predictions P1 and P2 then if the IOU between them is greater than some threshold we only keep the one that is associated with the higher confidence (keep box with higher confidence)


![[Pasted image 20241120114112.png]]
![[Pasted image 20241120114159.png]]
>MSE

![[Pasted image 20241120114209.png]]

Localization Loss
> Confidence loss and Box coordinate loss 
![[Pasted image 20241120114241.png]]
+ ? The coord loss sum over all grid cells and all bounding boxes in each grid cell but it is only counted for those cases where cell i contain an object and box j.

![[Pasted image 20241120114754.png]]
**Limitations**:
+ Each grid cell can contain only one class
+ Each grid cell can contain only B bounding boxes



---

# How YOLO Object Detection Works

## Introduction  
Today, we’ll explore YOLO (You Only Look Once), a highly influential algorithm and framework for **real-time object detection**. YOLO offers a desirable mix of speed and accuracy, making it popular for applications like:  
- Video surveillance  
- Self-driving cars  
- Face detection (e.g., measuring temperatures during the pandemic).  

## Overview  
The main goal of YOLO is to:
1. Create **bounding boxes** around objects in an image.  
2. Label these objects based on their class.  

Compared to traditional object detection methods, YOLO stands out by processing the entire image in a single pass, unlike region-based approaches that analyze multiple regions.

---

## Traditional Models vs. YOLO  
### Deformable Parts Model (DPM):  
- Uses filters to detect objects and parts of objects.  
- Employs a sliding window technique.  
- Focuses on part configurations.  

### Region-Based CNN (R-CNN):  
- Consists of three separate components:  
  1. **Region proposal model**  
  2. **CNN** for feature extraction  
  3. **Support vector machine (SVM)** for classification  
- Models are trained separately, making the process slower.

### YOLO:  
- Processes the image **only once** with a unified architecture.  
- Balances speed and accuracy efficiently.  

---

## YOLO Framework  

### Grid Cell Approach:  
1. **Grid overlay**: An image is divided into $S \times S$ grid cells.  
2. **Outputs for each grid cell**:  
   - **Bounding boxes** with confidence scores indicating object presence.  
   - **Class probability map** for object classification.  

### Output Vector:  
- For each grid cell: A vector combining bounding box parameters, class probabilities, and confidence scores.  
- Length of the vector = $B \times 5 + N$, where:  
  - $B$: Number of bounding boxes per grid cell.  
  - $N$: Number of object classes.  

For example, with a $7 \times 7$ grid, $B = 2$ bounding boxes, and $N = 20$ classes, each grid cell outputs a vector of length 30.

---

### CNN Architecture:  
- A stack of **convolutional layers** extracts abstract image features.  
- **Fully connected layers** transform features into output vectors.  

---

## Training YOLO  
### Key Concepts:  
1. **Ground Truth Values**:  
   - **Class probabilities**:  
     $P(c) = 1 \text{ for the correct class, and } 0 \text{ for others.}$  
   - **Bounding box parameters**:  
     $x$, $y$, $w$, $h$ are normalized to fall between $[0, 1]$:  
     - $x = \frac{\text{distance from top-left corner of grid cell to center of bounding box in x-axis}}{\text{width of grid cell}}$  
     - $y = \frac{\text{distance from top-left corner of grid cell to center of bounding box in y-axis}}{\text{height of grid cell}}$  
     - $w$ and $h$ are expressed as a proportion of the total image dimensions.  

2. **Confidence Scores**:  
   - Reflect the likelihood of object presence in a grid cell:  
     $C = P(\text{object}) \times \text{IoU of predicted and ground truth boxes}$.  

   - **Intersection over Union (IoU)**:  
     $\text{IoU} = \frac{\text{Area of Overlap}}{\text{Area of Union}}$.  

3. **Non-Max Suppression**:  
   - Eliminates overlapping bounding boxes by keeping the one with the highest confidence score.

---
### Loss Function  
YOLO’s total loss is the sum of three components:  

1. **Localization Loss**: Penalizes errors in bounding box predictions for cells containing objects.  
   $$
   \text{Localization Loss} = \lambda_{\text{coord}} \sum_{i=0}^S \sum_{j=0}^B \mathbb{1}_{ij}^{\text{obj}} \left[ (x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2 + (\sqrt{w_i} - \sqrt{\hat{w}_i})^2 + (\sqrt{h_i} - \sqrt{\hat{h}_i})^2 \right]
   $$  

2. **Confidence Loss**: Penalizes errors in predicted confidence scores for both object and no-object cases.  
   $$
   \text{Confidence Loss} = \sum_{i=0}^S \sum_{j=0}^B \mathbb{1}_{ij}^{\text{obj}} (C_i - \hat{C}_i)^2 + \lambda_{\text{noobj}} \sum_{i=0}^S \sum_{j=0}^B \mathbb{1}_{ij}^{\text{noobj}} (C_i - \hat{C}_i)^2
   $$  

3. **Class Loss**: Penalizes errors in class probabilities for grid cells containing objects.  
   $$
   \text{Class Loss} = \sum_{i=0}^S \mathbb{1}_i^{\text{obj}} \sum_{c \in \text{classes}} \left( P_i(c) - \hat{P}_i(c) \right)^2
   $$  

Here:  
- $\mathbb{1}_{ij}^{\text{obj}}$ = 1 if object exists in grid cell $i$ and box $j$, otherwise 0.  
- $\mathbb{1}_{ij}^{\text{noobj}}$ = 1 if no object exists in grid cell $i$ and box $j$.  
- $\lambda_{\text{coord}}$ and $\lambda_{\text{noobj}}$ are scaling factors to balance the losses.  

---

### Scaling Factors:  
- $\lambda_{\text{coord}} = 5$: Prioritizes bounding box prediction.  
- $\lambda_{\text{noobj}} = 0.5$: Reduces the impact of confidence loss for empty grid cells.

---

## Limitations of YOLO v1  
1. **Single-class restriction**:  
   - Each grid cell predicts only one class. Overlapping objects (e.g., dog and bicycle in the same cell) cause issues.  

2. **Bounding box limits**:  
   - Fixed number of bounding boxes per cell struggles in crowded scenes (e.g., busy urban areas).  

3. **Aspect ratio and size scaling**:  
   - Errors in predicting large versus small boxes are not properly scaled.  

---

### Solutions:  
- Use $\sqrt{w}$ and $\sqrt{h}$ to scale box size differences sublinearly.  
- Adjust scaling factors ($\lambda_{\text{coord}} = 5$, $\lambda_{\text{noobj}} = 0.5$) for better training balance.

---

## Conclusion  
YOLO revolutionized object detection with its simplicity and speed, using a single CNN for bounding box regression and classification. While early versions like YOLO v1 had limitations, subsequent iterations introduced significant improvements.  

For further learning, explore newer YOLO versions and advancements.  


T