YOLO (You Only Look Once) is a family of real-time object detection models that have evolved significantly since their inception. Below is an overview of YOLO from v1 to v8, focusing on the improvements and advantages of each version.

---

### **[[YOLOv1]] (2016)**  
- **Key Contributions**:  
  - Introduced the "You Only Look Once" paradigm: treating object detection as a single regression problem instead of a pipeline.  
  - Unified detection and classification tasks into a single neural network.  
  - Uses a single forward pass for real-time detection.  

- **Architecture**:  
  - Based on a custom CNN.  
  - Divided the image into an $S \times S$ grid; each cell predicts bounding boxes, confidence scores, and class probabilities.

- **Advantages**:  
  - Extremely fast and suitable for real-time applications.  
  - End-to-end training.

![[Pasted image 20250312062622.png]]
```ad-warning
**Limitations**:  
- **Generalization**: YOLOv1 struggles to detect new objects, not seen in training accurately.

- **Spatial constraints**: In YOLOv1, each grid cell predicts only two boxes and can only have one class, which makes it struggle with small objects that appear in groups, such as flocks of birds.

- **Loss Function Limitations**: The YOLOv1 loss function treats errors the same in small and large bounding boxes. A small error in a large box is generally okay, but a small one has a much greater effect on IOU.

- **Localization Errors**: One major issue with YOLOv1 was accuracy, it often mislocates where objects are in the image.
```


---

## Network Block
note: backbone ~ network architecture that extract features
![[1_Et7cTk2LwvzQfcnMVKQbEQ.png]]
+ **Backbone:** responsible for the initial feature extraction from the input data. (Before: Fully Connected Layer) ![[Pasted image 20250312060105.png]]
+ **Bottleneck:** The presence of such a layer let the network to compress feature representations to fit in the given space as best as possible. ![[Pasted image 20250312055650.png]]
+ **Detection Head**: Produce the final prediction or inference based on the information extracted by the Backbone and Neck.
	![[Structure-of-Fast-R-CNN-head-for-object-detection.png]]

## Residual Block (Khối Dư)
A residual block is a layer stack arranged so that the output of one layer is taken and added to another layer deeper in the block.
![[Pasted image 20250312054655.png]]

## Skip Connection 
>Skip connections are a form of shortcut that connects the output of one layer to the input of an adjacent layer.
![[Pasted image 20250312054729.png]]
- **Residual blocks** address vanishing gradient, **making deeper networks easier to train and more accurate**. 
	
- **Skip connections** in general help **preserve or reuse important features and ensure stable gradient flow**, whether in classification, detection, or segmentation architectures.
	
+ In NLP. LSTM/GRU, skip connections help reduce gradient exploding/vanishing and represent a pipe line to transfer long-term memory from layer to layer.

-
## Downsampling
+ ? After extracting features from first layer of CNN , if we directly give the output to second layer then the **process becomes computationally expensive**. To **reduce the size of output** we **extract the minimal effect features and give to the next layer**. 
+ $ **This process done to reduce the output size without loosing important information** is called **Downsampling**. **Most common approach** use for Downsampling **is Max pooling**.
+ @ This process **compressed representation of the input image** that can be efficiently processed, **allowing the network to extract key structural features and relationships** within the input.
![[Pasted image 20250312054848.png]]
+ ? For many image processing applications (such as segmentation, co-registration (so sánh ảnh), artifact removal (loại bỏ hiện vật trong ảnh, e.g. loại bỏ sương che mất cây), and image enhancement) it may be **desirable to reverse the process, gradually restoring the spatial dimensions of the feature maps** **while reducing the number of channels or features**. This process call Up-Sampling. (có thể đảo ngược quá trình Downsampling mà không tăng số kênh màu hoặc features)
![[down-and-upsampling-cnn_orig.png]]
- ? **Convolution layers** progressively transform the input into feature maps that capture important visual patterns (edges, corners, textures, etc.).
	
- ? **Downsampling** (via pooling or strided convolution) reduces the spatial resolution, condensing the feature maps into fewer (but deeper) pixels. This reduces computational cost and forces the model to learn higher-level features.
	
- ? **Upsampling** (e.g., transpose convolution, nearest-neighbor, etc.) brings those smaller feature maps back to a higher resolution, effectively decompress spatial information to high-resolution information.


## Max Pooling
>Pooling operation that calculates the maximum value for patches of a feature map, and uses it to create a downsampled feature map
![[Pasted image 20250312055046.png]]

## 1 x 1 Convolution
1X1 Convolution simply means the filter is of size 1X1. This 1X1 filter will convolve over the ENTIRE input image pixel by pixel. 
+ ? if input of 64X64X3 (height X width X channel) , if we choose a 1X1 filter (which would be 1X1X3), then the output will have the same height and width as input but only one channel 64X64X1.
+ ? Example if we using 2 filter to extract 2 color channels from 5 colors channels Input.  ![[Pasted image 20250312053914.png]]
+ ! Don't use pooling because it reduce feature map parameters.

### **YOLO v2 (2017)** *(YOLO 9000)*  
+ ? 9000 in detect 9000 different object categories

+ $ Researchers behind YOLO9000 proposed a unique **joint training** algorithm that **trains object detectors on both detection and classification data**. This method **leverages labeled detection images** to learn to **precisely localize objects and uses classification images to increase its vocabulary and robustness.**
	![[Pasted image 20250312050903.png]]

**Key Improvement**:
1. **Batch Normalization everywhere**: Greatly improved convergence (hội tụ) and stability.
	
2. **Anchor boxes (predefined bounding boxes) + Dimension Clusters**: Adopted “**anchor bounding box**” priors (inspired by Faster R-CNN) and used k-means clustering on training dataset bounding box sizes to pick better priors.
	+ ? Anchor boxes are **used as templates for prediction** during model training and inference. The **model predicts adjustments to anchor boxes** to match objects’ actual locations. ![[Pasted image 20250312064007.png]]
	
3. **Multi-scale training**: Randomly changed the input resolution during training to make the network more robust to different input sizes.
	
4. **Improved backbone (Darknet-19)**: A more efficient classification backbone with fewer layers than VGG, but better performance.
	![[DarkNet-19-Architecture.jpg]]
+ - **Predict One**:  
    Uses deeper but lower-resolution feature maps.  
    Good for detecting larger objects (e.g. 13×13 output).
- **Predict Two**:  
    An intermediate scale (e.g. 26×26 ).  
    Helps detect medium-sized objects.
- **Predict Three**:  
    An even higher-resolution feature map (e.g. 52×52),  
    Better at detecting small objects

![[Pasted image 20250312064950.png]]
note:  **Convolution Layers** allow us to **extract key informations** and **Downsampling (pooling, stride) help reduce spatial information dimensions** while **Up Sampling decompress those information to high-resolution information**


---

### **YOLO v3 (2018)**  
+ @ The improvements start with the bounding boxes, while it still uses the sliding window approach, YOLOv3 had some enhancements. YOLOv3 introduced multi-scale predictions where it predicts bounding boxes at three different scales. This means more effectiveness in detecting objects of different size

**Improvements**:  
+ **Backbone:** YOLOv3 uses a better and bigger CNN backbone which is Darknet-53 which consists of 53 layers and is a hybrid approach between Darknet-19 and deep learning residual networks (Resnets), but more efficient than ResNet-101 or ResNet-152.
    
+ **Predictions Across Scales:** YOLOv3 predicts bounding boxes at three different scales, similar to feature pyramid networks. This allows the model to detect objects of various sizes more effectively.
	
+ **Classifier:** Independent logistic classifiers are used instead of a softmax function, allowing for multiple labels per box.
	
+ **Dataset:** The researchers train YOLOv3 on the COCO dataset only.
+ Also YOLOv3 fixed a little data-loading bug in YOLOv2, which helped by like 2 mAP points
![[Pasted image 20250312065007.png]]

---

### **YOLO v4 (2020)**  
+ ? The most notable change is the 3 part architecture, while YOLOv4 is still a one-stage object detection network, the architecture involves 3 main components, backbone, head, and neck
+ $ The backbone is the feature extraction part, usually a CNN that learns features across layers. Then the neck refines and combines the extracted features from different levels of the backbone, creating a rich and informative feature representation. Finally, the head does the actual prediction, and outputs bounding boxes, class probabilities, and objectness scores.
![[Pasted image 20250312065506.png]]
For YOLOv4 the researchers used the following components for the backbone, neck, and head.

- **Backbone**: CSPDarknet53 is a convolutional neural network and backbone for object detection that uses DarkNet-53 which uses a Cross Stage Partial Network (CSPNet) strategy.
- **Neck**: Modified Spatial Pyramid Pooling (SPP) and Path aggregation network (PAN) were used for YOLOv4, which produced more granular feature extraction, better training, and better performance.
- **Head**: YOLOv4 employs the (anchor-based) architecture of YOLOv3 as the head of YOLOv4.

This was not all that YOLOv4 introduced, there was a lot of work on optimization and picking the right methods and techniques, let’s explore those next.

##### Optimization

The YOLOv4 model came with two bags of methods, as the researchers introduced in the paper: Bag of Freebies (BoF) and Bag of Specials (BoS). Those methods were instrumental in the performance of YOLOv4, in this section, we will explore the important methods the researchers used.

1. **Mosaic [Data Augmentation](https://viso.ai/computer-vision/image-data-augmentation-for-computer-vision/)**: This data augmentation method combines 4 training images into one, enabling the model to learn to detect objects in a wider variety of contexts and reducing the need for large mini-batch sizes. The researchers used it as a part of the BoF for the backbone training.
	
2. **Self-Adversarial Training (SAT)**: A two-stage data augmentation technique where the network tricks itself and modifies the input image to think there’s no object. Then, it trains on this modified image to improve robustness and generalization. Researchers used it as a part of the BoF for the detector or head of the network.
	
3. **Cross mini-batch Normalization (CmBN)**: A modification of Cross-Iteration Batch Normalization (CBN) that makes training more suitable for a single GPU. Used by researchers as part of the BoF for the detector.
	
4. **Modified [Spatial Attention Module](https://viso.ai/deep-learning/grounded-sam/) (SAM)**: The researchers modify the original SAM from spatial-wise attention to point-wise attention, enhancing the model’s ability to focus on important features without increasing computational costs. Used as part of the BoS as an additional block for the detector of the network.

![[Pasted image 20250312065654.png]]

---

### **YOLO v5 (2020)** *(Unofficial)*  
![[Pasted image 20250312065849.png]]
### Issues from YOLOv4

1. **Less Accessible Codebase**: Official YOLOv4 was primarily in C/darknet framework, less flexible for many practitioners.
2. **Deployment & Scaling Complexity**: Harder to scale or export YOLOv4 models quickly to mobile devices, TensorRT, etc.

### Key Improvements

1. **Pure PyTorch Implementation**: Easy for the community to read, modify, and integrate with other PyTorch projects.
2. **Focus Layer & AutoAnchor**: Streamlined early feature extraction and automatically computed optimal anchor boxes.
3. **Mosaic & MixUp**: Extended data augmentation strategies for more robust training.
4. **Model Scaling**: Simple s/m/l/x variants for different speed/accuracy trade-offs.
5. **Seamless Deployment**: Provided built-in export to ONNX, TensorRT, CoreML, etc.

---

### **YOLO v6 Industrial Quality (2022)**  
+ ? This version for industrial focus offered deployment-ready networks and better consideration of the constraints of real-world environments.
#### Issues from YOLOv5 (and earlier YOLOs)
1. **Anchor Management**: Anchor-based approaches can be tedious to tune and can become less efficient on edge devices.
2. **Label Assignment Complexity**: Hard to find an optimal way to assign ground-truth objects to anchors (or grid cells).
#### Key Improvements
1. **Anchor-Free by Default**: Simplified model configuration and improved speed.
2. **Advanced Label Assignment**: Introduced new assignment mechanisms for better training stability and performance.
3. **Lightweight/Edge Variants**: Specialized optimizations for mobile/edge applications.

![[Pasted image 20250312065909.png]]
- **Backbone**: The researchers build the backbone using EfficientRep which is a hardware-aware CNN featuring RepBlock for small models (N and S) and CSPStackRep Block for larger models (M and L).
	
- **Neck**: Uses Rep-PAN topology (cấu trúc), enhancing the modified PAN topology from YOLOv4 and YOLOv5 with RepBlocks or CSPStackRep Blocks. Which gives a **more efficient feature aggregation (tổng hợp) from different levels of the backbone**.
	
- **Head**: YOLOv6 introduced the **Efficient Decoupled Head simplifying the design for improved efficiency**. It utilizes a hybrid-channel strategy, reducing the number of middle 3×3 convolutional layers and scaling the width jointly with the backbone and neck.

YOLOv6 also incorporates several other techniques to enhance performance.
	
- **Label Assignment**: Utilizes Task Alignment Learning (TAL) to address the misalignment between classification and box regression tasks.
	
- **Self-Distillation**: It applies self-distillation to both classification and regression tasks, improving the accuracy even more.
	
- **Loss Function**: It employs VariFocal Loss for classification and a combination of SIoU and GIoU Loss for regression.
![[Pasted image 20250312070156.png]]

---

### **YOLO v7 (2022)**  
### Issues from YOLOv6 & Earlier
1. **Limited Use of Re-Parameterization**: E.g., other architectures used re-param to fuse multiple layers at inference.
2. **Inefficient Feature Aggregation**: Standard skip connections or feature pyramids could still be improved.

### Key Improvements
1. **E-ELAN (Extended Efficient Layer Aggregation Networks)**: More refined way to aggregate features across layers, enabling deeper networks without huge computation overhead.
	
2. **Re-parameterization**: Train with certain structural layers (e.g., batch norms, multiple convs) and fuse them into simpler layers for faster inference.
	
3. **Scaled Variants**: Different versions (tiny, base, large) to fit different speed/accuracy needs.
	
4. **State-of-the-Art Real-Time Accuracy**: Claimed top real-time performance on popular detection benchmarks at release.

![[Pasted image 20250312070424.png]]

### **Key Trends Across YOLO Versions**:  
1. **Speed vs. Accuracy**: Early versions (v1-v3) prioritized speed; later versions (v4-v8) improved accuracy without compromising much on speed.  
2. **Anchor-based to Anchor-free**: Transitioned to anchor-free methods for simplicity and efficiency.  
3. **Backbone Evolution**: Progressed from custom CNNs to sophisticated architectures like CSPDarknet.  
4. **Small Object Detection**: Improved handling of smaller objects with multi-scale prediction and better feature pyramids.  
5. **Integration with Modern Techniques**: Incorporated advancements like attention mechanisms, loss functions, and data augmentation.



