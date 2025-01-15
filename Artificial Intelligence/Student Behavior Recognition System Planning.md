### 1. System Overview

1. **Skeleton Data Collection and Preprocessing**
    
2. **Feature Extraction**
    
3. **Behavior Classification**

### 2. Key Components of the System
#### 2.1. Skeleton Pose Estimation (OpenPose)

#### 2.2. Person Detection (YOLOv4)

#### 2.3. Error Correction Scheme

Algo1
Algo2

#### 2.4. Skeleton Data Preprocessing

### 3. Feature Extraction

- Normalized Joint Locations:
    
    
- Joint Distances:
    
    
- Bone Angles:
    
The final feature vector is created by concatenating the normalized joint locations, joint distances, and bone angles.


### 4. Behavior Classification

- A **Deep Neural Network (DNN)** is used to classify student behaviors based on the extracted features.
    
- The DNN consists of:
    
    - An input layer with 26 features (representing the human posture).
        
    - Three fully connected (FC) layers with 128, 64, and 16 neurons, respectively.
        
    - A final FC layer with 4 neurons (one for each behavior class) and a softmax activation function for classification.
        
- The system is trained to recognize four behaviors:
    
    1. **Asking:** The student raises their hand.
        
    2. **Looking:** The student looks at the teacher.
        
    3. **Bowing:** The student is writing or reading (head bowed).
        
    4. **Boring:** The student is bored (e.g., resting their head on their hands).


### 5. System Implementation

- The user interface displays:
    
    - A live camera view of the classroom.
        
    - Behavior statistics (e.g., number of students asking, looking, bowing, or bored).

### 6. Experimental Results
Examples:
- The system is evaluated on a dataset of 11,500 images, divided into training and validation sets.
    
- The system achieves high accuracy in behavior recognition, with an average precision of **91.2%** and an average recall of **99.1%**.
    
- The proposed system outperforms a skeleton-based scheme (without person detection) in complex classroom scenarios, especially in crowded environments.
    
- The system can process frames at a rate of **13.5 frames per second (fps)**, making it suitable for real-time applications.

