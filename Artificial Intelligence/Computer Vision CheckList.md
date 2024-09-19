# Beginner
```ad-info
You’ll be equipped to handle basic image manipulation and enhancement tasks, preparing images for further processing.
```

- [ ] **Image Processing**: *Basic image manipulation techniques such as resizing, cropping, and color conversion.
	
  - [ ] **Basic Image Operations**: How to read, write, resize, crop, and manipulate images.
    - [ ] Image reading and writing (formats like JPG, PNG, etc.)
    - [ ] Image resizing, cropping, and rotation
    - [ ] Color space conversions (RGB, grayscale, HSV)
    - [ ] Histogram equalization and normalization
  - [ ] **Filtering**
    - [ ] Smoothing filters (Gaussian, Median, Bilateral)
    - [ ] Sharpening filters (Laplacian, Unsharp Masking)
    - [ ] Edge detection (Sobel, Canny, Prewitt)
  - [ ] **Thresholding**
    - [ ] Global thresholding (Binary, Truncated)
    - [ ] Adaptive thresholding
    - [ ] Otsu’s method
  - [ ] **Morphological Operations**
    - [ ] Dilation, Erosion
    - [ ] Opening, Closing
    - [ ] Morphological gradients
	
- **Capabilities**: Perform essential image preprocessing tasks to prepare images for further analysis or enhancement.
	
- **Usage**: Apply basic image processing techniques used in beginner projects like Instagram-style photo filters, simple photo editors, and QR code detection. These foundational skills are also essential for preparing datasets for machine learning projects, such as converting images to grayscale for digit classification.


- [ ] **Deep Learning Frameworks and Tools:** *Tools and libraries for building and deploying computer vision models.*
	
  - [ ] **OpenCV**
    - [ ] Image processing, video analysis, object detection
  - [ ] **TensorFlow/Keras**
    - [ ] Building and training deep learning models
  - [ ] **PyTorch**
    - [ ] Implementing custom deep learning networks
  - [ ] **TensorFlow**
    - [ ] Object detection and segmentation with deep learning
- [ ] **EasyOCR**

+ **Usage**: Start building computer vision projects like real-time object detection with webcams, using OpenCV and pre-trained models. Students often use frameworks like TensorFlow and PyTorch to implement tutorials, such as recognizing handwritten digits (MNIST) or creating simple image classifiers using transfer learning.


---
# Intermediate Level
```ad-info
You’ll gain skills in classifying, detecting, and matching objects in images, handling more complex analysis tasks.
```

- [ ] **Image Classification**: *Fundamentals of traditional machine learning algorithms like SVM and k-NN.*
	
  - [ ] **Traditional Machine Learning Algorithms**
    - [ ] Support Vector Machines (SVM) for classification
    - [ ] k-Nearest Neighbors (k-NN)
    - [ ] Decision Trees and Random Forests
  - [ ] **Deep Learning Algorithms**
    - [ ] Fully connected neural networks (MLP)
    - [ ] Convolutional Neural Networks (CNNs)
      - [ ] CNN architecture design (LeNet, AlexNet, VGG, ResNet)
      - [ ] CNN layers (convolution, pooling, fully connected)
- [ ] Transfer learning using pre-trained models (VGG16, ResNet, Inception)
- [ ] Model evaluation: accuracy, confusion matrix, F1-score, AUC-ROC
	
- **Capabilities**: Identify and match key points between images for basic alignment or recognition tasks.
	
+ **Usage**: Develop projects like image classifiers to distinguish between different animals, fruits, or vehicles, commonly found in student projects. Intermediate projects also include building models that can identify plant diseases, recognize handwritten text, or sort images into categories using deep learning.


- [ ] **Object Detection:** *Basic object detection methods such as Sliding Window and HOG + SVM.*
	  
  - [ ] **Traditional Methods**
    - [ ] Sliding Window technique
    - [ ] Image Pyramids for multi-scale detection
    - [ ] Histogram of Oriented Gradients (HOG) + SVM
  - [ ] **Deep Learning-based Object Detection**
    - [ ] Region-based Convolutional Neural Networks (R-CNN)
    - [ ] Fast R-CNN, Faster R-CNN, and Mask R-CNN
    - [ ] Single Shot MultiBox Detector (SSD)
    - [ ] YOLO (You Only Look Once) family (v3, v4, v5, etc.)
    - [ ] Anchor boxes and bounding box regression
    - [ ] Non-Maximum Suppression (NMS)
	
- **Capabilities**: Improve feature matching accuracy and robustness, useful for complex image alignment and recognition tasks.
	
+ **Usage**: Implement popular object detection projects such as detecting faces in live video feeds, identifying objects in video games, or building smart home applications like intruder detection using a Raspberry Pi and a webcam. These methods are also used in student projects like counting objects (e.g., cars, people) in a video stream for data analysis.


---
# Advanced Level
```ad-info
You’ll be able to track objects, segment images in detail, recognize faces, estimate poses, and extract text, allowing for sophisticated and comprehensive computer vision applications.
```


- [ ] **Object Tracking:** *Traditional tracking algorithms like Optical Flow and Kalman Filter.*
	
  - [ ] **Traditional Tracking Algorithms**
    - [ ] Optical Flow (Lucas-Kanade, Farneback)
    - [ ] Kalman Filter
    - [ ] Mean-Shift and CAMShift (Continuously Adaptive Mean-Shift)
  - [ ] **Modern Tracking Techniques**
    - [ ] Multi-Object Tracking (MOT)
    - [ ] SORT (Simple Online and Realtime Tracking)
    - [ ] DeepSORT (Deep Learning + SORT)
    - [ ] Correlation Filter-based Trackers (CSRT, KCF)
	
+ **Capabilities**: Perform detailed image segmentation tasks, including instance and semantic segmentation for advanced image analysis.
	
+ **Usage**: Build advanced projects like AI-based tracking systems for sports analysis, drone tracking, or automated surveillance systems. Projects often include following a ball during a soccer match or tracking hands for gesture recognition in real-time using webcams.


- [ ] **Image Segmentation:** *Divide images into segments to isolate or analyze specific regions, useful for tasks like separating text from the background in ID cards.*
	
  - [ ] **Traditional Segmentation**
    - [ ] Threshold-based segmentation
    - [ ] Region growing and merging techniques
    - [ ] Watershed algorithm
    - [ ] K-means clustering for segmentation
  - [ ] **Deep Learning-based Segmentation**
    - [ ] Fully Convolutional Networks (FCN)
    - [ ] U-Net (Medical Image Segmentation)
    - [ ] Mask R-CNN for instance segmentation
    - [ ] Semantic segmentation (pixel-wise classification)
    - [ ] Instance segmentation vs semantic segmentation
	
- **Capabilities**: Perform detailed image segmentation tasks, including instance and semantic segmentation for advanced image analysis.
	
+ **Usage**: Create projects that involve segmenting objects from backgrounds, such as real-time background removal for virtual meetings or extracting roads from aerial images for mapping. Medical image segmentation projects, like identifying tumors in MRI scans, are also popular among advanced students.


- [ ] **Face Detection and Recognition:** *Detect and recognize human faces using various techniques, including deep learning-based methods.*
	
  - [ ] **Face Detection**
    - [ ] Haar Cascades (Viola-Jones algorithm)
    - [ ] HOG + Linear SVM
    - [ ] Deep learning-based face detection (MTCNN, RetinaFace)
  - [ ] **Face Recognition**
    - [ ] Eigenfaces and Fisherfaces
    - [ ] Face embedding techniques (FaceNet, DeepFace)
    - [ ] Triplet Loss and Contrastive Loss
    - [ ] Real-time face recognition using OpenCV and deep learning
	
- **Capabilities**: Detect and recognize faces in images with high accuracy, applicable to various face-related tasks.
	
+ **Usage**: Implement face recognition systems for building security or attendance tracking. Students often create projects like smart doorbells with face recognition, automatic photo tagging, and facial expression analysis for emotion detection using deep learning models.


- [ ] **Keypoint Detection and Feature Matching:** *Detecting specific interest points in images (like corners) and matching them between images.*
	
  - [ ] **Feature Detection**
    - [ ] Harris Corner Detection
    - [ ] SIFT (Scale-Invariant Feature Transform)
    - [ ] SURF (Speeded-Up Robust Features)
    - [ ] ORB (Oriented FAST and Rotated BRIEF)
  - [ ] **Feature Matching**
    - [ ] Brute-Force Matching
    - [ ] FLANN (Fast Library for Approximate Nearest Neighbors)
    - [ ] Homography estimation (RANSAC)
	
- **Capabilities**: Handle complex feature matching and alignment tasks, including homography estimation for accurate image transformations.
	
+ **Usage**: Develop projects such as augmented reality (AR) applications where virtual objects are placed in the real world by matching features from a camera feed. Other popular projects include creating panorama stitching software that merges multiple images into a single wide-angle photo.


- [ ] **Pose Estimation:** *Analyze and track the pose of objects or people, useful for applications in robotics and augmented reality.*
	
  - [ ] **2D Pose Estimation**
    - [ ] OpenPose for human body keypoint detection
  - [ ] **3D Pose Estimation**
    - [ ] Estimating 3D pose from 2D images
  - [ ] **PnP (Perspective-n-Point) Algorithm**
    - [ ] Estimating camera pose from a set of 3D points
	
+ **Capabilities**: Estimate the orientation and position of objects or people, useful for applications in robotics and augmented reality.
	
+ **Usage**: Build interactive projects like fitness trainers that analyze body posture, dance step analysis, or human pose estimation for gaming. These projects often involve using body keypoint detection to provide real-time feedback on movements.


- [ ] **Optical Character Recognition (OCR):** *Convert images of text into machine-readable text, essential for extracting information from ID cards.*
	
  - [ ] Tesseract OCR
  - [ ] Preprocessing for OCR (denoising, binarization)
  - [ ] Deep learning-based OCR (CRNN, Attention models)
	
+ **Capabilities**: Extract and interpret text from images with high accuracy, essential for document processing and text extraction tasks.
	
+ **Usage**: Create OCR projects like digitizing handwritten notes, building number plate recognition systems for parking management, or extracting text from documents for data entry automation. OCR projects are widely used in applications like library management systems to scan and store book information.


- [ ] **Generative Models:** *Create synthetic data (dữ liệu tổng hợp) or perform advanced image transformations, useful for augmenting datasets or simulating data.*
	
  - [ ] **Autoencoders**
    - [ ] Vanilla autoencoder
    - [ ] Variational Autoencoder (VAE)
  - [ ] **Generative Adversarial Networks (GANs)**
    - [ ] Basic GAN architecture
    - [ ] DCGAN (Deep Convolutional GAN)
    - [ ] Conditional GANs
    - [ ] CycleGAN for image-to-image translation
	
+ **Capabilities**: Create new images, enhance existing ones, or perform advanced transformations like image inpainting and style transfer.
	
+ **Usage**: Experiment with creative projects like generating new faces using GANs, converting sketches into realistic images, or creating deepfake videos. Students also use generative models for data augmentation in machine learning projects to improve model performance with limited datasets.







---
## Not Need to Focus Right now
```ad-info
These areas are more specialized and may not be immediately relevant but provide a solid foundation for more advanced applications.
```


- [ ] **Video Analysis**
  - [ ] Background subtraction techniques (MOG2, KNN)
  - [ ] Motion detection
  - [ ] Action recognition (using RNNs, LSTMs, or 3D CNNs)
	
- **Purpose**: Analyzing and processing video streams.
	
- **Usage**: Explore projects like real-time motion detection for security cameras, creating smart video surveillance systems, or developing action recognition models for sports footage. These projects often involve processing video streams to identify and track movements.

- [ ] **3D Vision**
  - [ ] **Stereo Vision**
    - [ ] Disparity map computation
    - [ ] Depth estimation from stereo images
  - [ ] **Structure from Motion (SfM)**
    - [ ] Estimating 3D structure from 2D image sequences
  - [ ] **Point Cloud Processing**
    - [ ] Using Open3D or PCL (Point Cloud Library)
    - [ ] LIDAR and depth sensor data processing
	
- **Purpose**: Extracting 3D information from 2D images.
	
- **Usage**: Implement projects such as 3D reconstruction of objects using multiple camera angles, building 3D models from 2D images, or developing depth-sensing applications for robotics. Students often work on stereo vision for self-driving car simulations.

- [ ] **Augmented Reality (AR)**
  - [ ] **Camera Calibration**
    - [ ] Camera distortion and undistortion techniques
  - [ ] **Homography Estimation**
    - [ ] AR marker detection and tracking
  - [ ] **AR Development Frameworks**
    - [ ] ARCore (Google) for Android
    - [ ] ARKit (Apple) for iOS
	
- **Purpose**: Integrating virtual elements into real-world scenes.
	
- **Usage**: Create AR projects like placing virtual furniture in a room using your phone's camera, developing educational apps that overlay information on real-world objects, or making interactive AR games. These projects often involve detecting surfaces and tracking markers.

- [ ] **Image Generation**
  - [ ] **Image Inpainting**
    - [ ] Traditional inpainting algorithms
    - [ ] GAN-based inpainting
  - [ ] **Super-Resolution**
    - [ ] SRCNN (Super-Resolution CNN)
    - [ ] GAN-based super-resolution (ESRGAN)
  - [ ] **Style Transfer**
    - [ ] Neural style transfer using CNNs
	
- **Purpose**: Enhancing or creating new images.
	
- **Usage**: Work on creative projects like super-resolution to enhance low-resolution images, neural style transfer to apply artistic styles to photos, or image inpainting to restore damaged images. These projects are popular for learning about the generative capabilities of neural networks.