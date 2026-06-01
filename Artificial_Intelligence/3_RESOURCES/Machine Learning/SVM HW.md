1. Tìm hiểu [[HoG]] của ảnh
+ Use Sliding window 


2. Áp dụng cho bài toán face/human detection trong đó input có thể là miếng vá của ảnh hoặc là đặc trưng HoG của miếng vá 
+ [HoG and SVM Visualization](https://youtu.be/SPXocFBjr70?si=uUKUo_xpX48Dxp0o)
	![[Pasted image 20240710111048.png]]
4x4 -> 16D vector

3.  Chạy và hiểu bài tập liên quan đến SVM (Classification) trong link github sau


[https://github.com/mantasu/cs231n (Links to an external site.)](https://github.com/mantasu/cs231n) 

4. Đọc trước thuật toán tối ưu từ slide số 34 đến hết của Lec06_Classification_SVM 

Chú ý: các em có thể follow các bài tập trên course ở link trên, trong assignment 1 nhé. Các assigment khác các em có thể tham khảo

---

Hội tụ sau 1 số vòng lặp
![[Pasted image 20240710132344.png]]
+ find the best $\alpha$
![[Pasted image 20240710132527.png]]
Sliding win  overlap / non-overlap

Classify if a window slide is facial or not (0 or 1)

Training data - pos/neg data (yes/not facial)

CVPR - Conference on Computer Vision and Pattern Recognition
+ Remember to update yearly. Free Course

y = -1 / 1
x = i, j vector


Let's walk through each step for implementing a face detection model using an SVM classifier:

### 1. Prepare Data

**Load and Normalize Images:**

- **Positive and Negative Training Images:** Load images that contain faces (positive samples) and images without faces (negative samples).
- **Visualization:** Display some examples of both positive and negative samples to understand the data.
- **Normalization:** Apply mean-variance normalization to ensure each pixel in the image has zero mean and unit variance.

**Format Data for SVM:**

- **Xtrain, ytrain:** Training data and labels. `Xtrain` contains the image data, and `ytrain` contains the corresponding labels (1 for face, 0 for non-face).
- **Xval, yval:** Validation data and labels, used to evaluate the model's performance during training.

### 2. SVM Classification

**Train Linear SVM Classifier:**

- Use `svmclass` function to train the SVM model on `Xtrain` and `ytrain`.
- Evaluate the trained model using `svmvalmod` on `Xval` and `yval`.

**Compute Hyper-plane W and Bias b:**

- Derive the hyper-plane WWW from support vectors and alpha-coefficients obtained from the SVM training.
- Recompute confidence values for training and validation sets using WWW and bias bbb to ensure they match the values returned by `svmvalmod`.

**Visualization of Hyper-plane W:**

- Visualize WWW as an image. It often resembles an average face because the SVM finds the optimal hyper-plane that best separates face and non-face images.
- For small CCC values, WWW looks more like a face because the regularization term dominates, allowing more margin violations (support vectors close to the decision boundary).

**Retrain for Various C Values:**

- Retrain the SVM model for different values of CCC to find the one that maximizes accuracy on the validation set.
- Visualize WWW for each CCC value to observe how it changes.

### 3. Face Detection

**Scanning-Window Technique:**

- Slide a window across the test image and classify each patch using the trained SVM model.
- Store the confidence scores for each patch.

**Non-Maxima Suppression (NMS):**

- Apply NMS to remove redundant detections. Only keep the detection with the highest confidence score in the neighborhood.
- Experiment with different confidence thresholds for pre-selecting windows and NMS.

**Testing with Different Images:**

- Test the face detector on multiple images (img1.jpg, img2.jpg, img3.jpg, img4.jpg).
- Adjust `confthresh` (pre-selection threshold) and `confthreshnms` (NMS threshold) to optimize detection performance.

**Using HOG Features:**

- Instead of raw pixel values, extract HOG features from each image patch.
- Train the SVM using HOG features, which often improves detection accuracy.

### Example Code Snippet

Here's an example code snippet to illustrate the steps:
```python
from sklearn import svm
import numpy as np
import cv2
from skimage.feature import hog

# Part 1: Prepare Data
# Load positive and negative images
# Normalize images
# Format images into SVM-acceptable input

# Example normalization
def normalize_images(images):
    return (images - np.mean(images, axis=0)) / np.std(images, axis=0)

# Part 2: SVM Classification
# Train linear SVM
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(Xtrain, ytrain)

# Compute hyper-plane W
W = clf.coef_
b = clf.intercept_

# Visualization of W
W_image = W.reshape(image_shape)
plt.imshow(W_image, cmap='gray')
plt.title('Visualization of W')
plt.show()

# Retrain SVM for different C values and visualize W
C_values = [0.1, 1, 10]
for C in C_values:
    clf = svm.SVC(kernel='linear', C=C)
    clf.fit(Xtrain, ytrain)
    W = clf.coef_
    W_image = W.reshape(image_shape)
    plt.imshow(W_image, cmap='gray')
    plt.title(f'W visualization for C={C}')
    plt.show()

# Part 3: Face Detection
# Implement scanning-window technique
# Apply non-maxima suppression

def sliding_window(image, step_size, window_size):
    for y in range(0, image.shape[0] - window_size[1], step_size):
        for x in range(0, image.shape[1] - window_size[0], step_size):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])

# Example detection with NMS
def detect_faces(image, clf, window_size, step_size, conf_thresh):
    detections = []
    for (x, y, window) in sliding_window(image, step_size, window_size):
        if window.shape[0] != window_size[1] or window.shape[1] != window_size[0]:
            continue
        window = window.reshape(1, -1)
        score = clf.decision_function(window)
        if score > conf_thresh:
            detections.append((x, y, score))
    return non_maxima_suppression(detections)

# Apply NMS
def non_maxima_suppression(detections, conf_thresh_nms=0.5):
    if len(detections) == 0:
        return []
    detections = sorted(detections, key=lambda x: x[2], reverse=True)
    final_detections = []
    while len(detections) > 0:
        best = detections.pop(0)
        final_detections.append(best)
        detections = [d for d in detections if iou(best, d) < conf_thresh_nms]
    return final_detections

# IOU computation for NMS
def iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[0] + window_size[0], boxB[0] + window_size[0])
    yB = min(boxA[1] + window_size[1], boxB[1] + window_size[1])
    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = window_size[0] * window_size[1]
    boxBArea = window_size[0] * window_size[1]
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

# Test with different images and thresholds
test_images = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
for img_path in test_images:
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    detections = detect_faces(image, clf, window_size=(64, 64), step_size=8, conf_thresh=0.5)
    final_detections = non_maxima_suppression(detections, conf_thresh_nms=0.3)
    # Visualize results
    for (x, y, score) in final_detections:
        cv2.rectangle(image, (x, y), (x + 64, y + 64), (255, 0, 0), 2)
    plt.imshow(image, cmap='gray')
    plt.show()
```
This code snippet demonstrates the key steps involved in data preparation, SVM classification, and face detection using a sliding-window technique with non-maxima suppression. Adjust the parameters and thresholds as needed to optimize detection performance.

