### Extracting Keypoint & Build Dataset
```python
import os
import glob
import cv2 as cv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.metrics import confusion_matrix, classification_report

# Classes: 3 subfolders within 'Single_person_violent' => Kicking, Punching, Non-violent
CLASSES = ["Kicking", "Punching", "Standing"]

# We will define a fixed sequence length to handle variable-length videos
MAX_SEQ_LEN = 30 # example: 30 frames per video

# Set how many frames to skip when reading a video (to reduce computational load)
SKIP_RATE = 1  # example: capture 1 frame out of every 5

NUM_KP = 17  # Number of keypoints per person (COCO format)
DIM    = 2   # We only keep (x, y) coordinates

#? Initialize keypoints then updaate these keypoints later 
COCO_PAIRS = [
    (0, 1),  # nose → left eye
    (0, 2),  # nose → right eye
    (1, 3),  # left eye → left ear
    (2, 4),  # right eye → right ear
    (5, 6),  # left shoulder → right shoulder
    (5, 7), (7, 9),  # left arm
    (6, 8), (8, 10), # right arm
    (11, 12),         # left hip → right hip
    (11, 13), (13, 15),  # left leg
    (12, 14), (14, 16)   # right leg
]

from ultralytics import YOLO
model = YOLO("yolo11s-pose.pt")  # load a pretrained model, weight download from yolo pose website

def resize_frame(frame, target_width=720, target_height=1280):
    """
    Resize the frame to a fixed size (target_width x target_height)
    preserving aspect ratio and padding with black borders.
    """
    original_h, original_w = frame.shape[:2]
    scale = min(target_width / original_w, target_height / original_h)
    new_w, new_h = int(original_w * scale), int(original_h * scale)
    resized = cv.resize(frame, (new_w, new_h))

    # compute padding to center the resized frame
    top    = (target_height - new_h) // 2
    bottom = target_height - new_h - top
    left   = (target_width  - new_w) // 2
    right  = target_width  - new_w - left

    padded = cv.copyMakeBorder(
        resized,
        top, bottom, left, right,
        borderType=cv.BORDER_CONSTANT,
        value=[0, 0, 0]
    )
    return padded

def visualize_keypoints(frame, flat_kp):
    """
    Draws keypoints and skeleton lines on `frame`.

    Args:
      frame (np.ndarray):      BGR image to draw on.
      flat_kp (list or array): length 34 list of [x1, y1, x2, y2, …, x17, y17],
                                in pixel coordinates.
    """
    pts = np.array(flat_kp, dtype=np.float32).reshape(NUM_KP, DIM)

    # Draw joints
    for (x, y) in pts:
        cv.circle(frame, (int(x), int(y)), 4, (0, 255, 0), -1)

    # Draw bones
    for i, j in COCO_PAIRS:
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        # Only draw if both keypoints are non-zero
        if (x1 or y1) and (x2 or y2):
            cv.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)

def get_pose_sequence_from_video_yolov11(video_path, skip_rate=5, visualize=False, target_width=720, target_height=1280):
    """
    Extracts a fixed-length sequence of flattened (x, y) keypoints from a video using YOLOv11-Pose.

    Args:
      video_path (str):           Path to the input video file.
      skip_rate (int):            Process every `skip_rate`-th frame to reduce computation.
      visualize (bool):           If True, draw keypoints on each frame and display.

    Returns:
      np.ndarray of shape (T, NUM_KP * DIM):
        - T = number of frames processed (≈ total_frames / skip_rate)
        - Each row is a flattened list of 17 (x, y) pairs: [x1, y1, x2, y2, …, x17, y17].
    """

    # OpenCV video capture object for reading frames
    cap = cv.VideoCapture(video_path)

    # List to accumulate per-frame keypoint vectors
    sequence = []

    # Frame counter (to apply skip_rate)
    frame_index = 0

    while True:
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break  # No more frames → end of video
		
        # Fix orientation & size before inference
        frame = resize_frame(frame, target_width, target_height)

        # Only process every `skip_rate`-th frame
        if frame_index % skip_rate == 0:
            # Run your YOLOv11-Pose inference here:
            kp = run_yolov11_pose_on_frame(frame)
            # → `kp` might be:
            #     • None               (no person detected)
            #     • shape (1, N, D)    (batch & instances dims)
            #     • shape (N, D)       (already squeezed)
            #   where N = detected joints, D = coordinate dims (2 or 3)

            # If batched/instance dims present, take only the first person
            if kp is not None and kp.ndim == 3:
                kp = kp[0]  # now shape (N, D)

            # If confidence channel is present (D > DIM), drop it
            if kp is not None and kp.shape[1] > DIM:
                kp = kp[:, :DIM]  # keep only x,y

            # Prepare a fixed-size (NUM_KP × DIM) array:
            if kp is not None and kp.size:
                n_detected, d = kp.shape
                if n_detected >= NUM_KP:
                    # More joints than expected → truncate
                    kp = kp[:NUM_KP]
                else:
                    # Fewer joints → pad remaining rows with zeros
                    padding = np.zeros((NUM_KP - n_detected, DIM), dtype=kp.dtype)
                    kp = np.vstack([kp, padding])

                # Flatten to a 1D list: [x1, y1, x2, y2, …, x17, y17]
                flat_kp = kp.flatten().tolist()
            else:
                # No detection → all zeros
                flat_kp = [0.0] * (NUM_KP * DIM)

            # Add this frame’s keypoints to our sequence list
            sequence.append(flat_kp)


            if visualize:
                visualize_keypoints(frame, flat_kp)
                cv.imshow("YOLOv11 Pose Visualization", frame)
                if cv.waitKey(10) & 0xFF == ord('q'):
                    break

        frame_index += 1

    # Release resources
    cap.release()
    if visualize:
        cv.destroyAllWindows()

    # Convert list of lists to a NumPy array of shape (T, 34)
    return np.array(sequence)


def run_yolov11_pose_on_frame(frame):
    """
    Runs YOLOv11-Pose model on a single frame and returns the keypoints.
    """
    if frame is None:
        return None

    results = model.predict(frame, verbose=False)

    if results and results[0].keypoints:
        keypoints = results[0].keypoints.xy.cpu().numpy()
        return keypoints
    else:
        return None

```

**Testing**
```python
# print(get_pose_sequence_from_video_yolov11_yolov11("Single_person_violent\Kicking\kicking24.mp4", skip_rate=SKIP_RATE, visualize=True).shape)
# print(get_pose_sequence_from_video_yolov11_yolov11("Single_person_violent\Punching\Punching14.mp4", skip_rate=SKIP_RATE, visualize=True).shape)
print(get_pose_sequence_from_video_yolov11_yolov11("Single_person_violent\Standing\\video_12.avi", skip_rate=SKIP_RATE, visualize=True).shape)
```

**Build Dataset**
```python
import glob # for file path matching

BASE_DIR = "Single_person_violent"  # your main dataset folder
X_sequences = []
y_labels = []

#? Loop through each class directory (e.g. "Kicking", "Punching", "Non-violent")
for cls in CLASSES:  # e.g. "Kick", "Punching", "Non-violent"
    class_dir = os.path.join(BASE_DIR, cls)
    
    #? Use glob to list all .mp4 or .avi files
    video_paths = glob.glob(os.path.join(class_dir, "*.mp4")) + glob.glob(os.path.join(class_dir, "*.avi"))
    
    print(video_paths)
    print(cls)
	
    #? For each video file in the class directory
    for vid_path in video_paths:
        seq = get_pose_sequence_from_video_yolov11_yolov11(vid_path, skip_rate=SKIP_RATE)
        
        # If the video has at least 1 frame successfully processed, append
        if seq.shape[0] > 0:
            X_sequences.append(seq)
            y_labels.append(cls)
        else:
            print(f"No frames extracted from {vid_path} (possibly empty or skip too high).")
```

### Training
```python
Please continue to check if my code are compatible with the new YOLO-POSE model. 
import glob # for file path matching

BASE_DIR = "Single_person_violent"  # your main dataset folder
X_sequences = []
y_labels = []

#? Loop through each class directory (e.g. "Kicking", "Punching", "Non-violent")
for cls in CLASSES:  # e.g. "Kick", "Punching", "Non-violent"
    class_dir = os.path.join(BASE_DIR, cls)
    
    #? Use glob to list all .mp4 or .avi files
    video_paths = glob.glob(os.path.join(class_dir, "*.mp4")) + glob.glob(os.path.join(class_dir, "*.avi"))
    
    print(video_paths)
    print(cls)
	
    #? For each video file in the class directory
    for vid_path in video_paths:
        seq = get_pose_sequence_from_video_yolov11_yolov11(vid_path, skip_rate=SKIP_RATE)
        
        # If the video has at least 1 frame successfully processed, append
        if seq.shape[0] > 0:
            X_sequences.append(seq)
            y_labels.append(cls)
        else:
            print(f"No frames extracted from {vid_path} (possibly empty or skip too high).")

# Create output folder if it doesn't exist
SAVE_DIR = "extracted_data"
os.makedirs(SAVE_DIR, exist_ok=True)

# Convert to NumPy arrays and save
np.savez_compressed(
    os.path.join(SAVE_DIR, "pose_dataset_final.npz"),
    X=np.array(X_sequences, dtype=object),
    y=np.array(y_labels)
)

print(f"✅ Saved {len(X_sequences)} sequences to {SAVE_DIR}/pose_dataset_final.npz")

data = np.load("extracted_data/pose_dataset_final.npz", allow_pickle=True)
X_sequences = list(data["X"])
y_labels = list(data["y"])

print(f"✅ Loaded {len(X_sequences)} sequences.")

import numpy as np

def segment_sequence_with_tail(seq, max_seq_len=5, stride=2):
    """
    Breaks a long pose sequence into fixed‑length segments:
      1) All full windows of length max_seq_len, stepping by stride
      2) One final 'leftover' segment (the tail), padded to max_seq_len
    If seq is shorter than max_seq_len, returns one padded segment.
    Returns an array of shape (n_segments, max_seq_len, n_features).
    """
    segments = []
    L = len(seq) 

    # 1) Full windows
    for i in range(0, L - max_seq_len + 1, stride):
        segments.append(seq[i : i + max_seq_len])

    # 2) Tail leftover
    if L > max_seq_len:
        # compute where the next window would start
        last_full_start = ((L - max_seq_len) // stride) * stride
        next_start = last_full_start + stride
        if next_start < L:
            tail = seq[next_start:]
            # pad tail up to max_seq_len
            pad_amt = max_seq_len - tail.shape[0]
            tail_padded = np.vstack([
                tail,
                np.zeros((pad_amt, seq.shape[1]), dtype=seq.dtype)
            ])
            segments.append(tail_padded)
    else:
        # seq is shorter than max_seq_len: pad entire seq once
        pad_amt = max_seq_len - L
        padded = np.vstack([
            seq,
            np.zeros((pad_amt, seq.shape[1]), dtype=seq.dtype)
        ])
        segments = [padded]

    return np.array(segments)

def pad_or_truncate_sequence(seq, max_len=MAX_SEQ_LEN):
    """
    seq: (T, 132) array for T frames
    Returns an array of shape (max_len, 132).
    """
    
    length = seq.shape[0]
    num_features = seq.shape[1]
    
    # print(length, num_features)
    
    if length > max_len:
        # Truncate
        return seq[:max_len, :]
    else:
        # Pad with zeros
        padded = np.zeros((max_len, num_features))
        padded[:length, :] = seq
        return padded

X_seq_padded = []
y_seq_labels = []

for seq, label in zip(X_sequences, y_labels):
    # get _all_ segments including the leftover tail
    segs = segment_sequence_with_tail(
        seq,
        max_seq_len=MAX_SEQ_LEN,
        stride=1
    )
    for s in segs:
        X_seq_padded.append(s)
        y_seq_labels.append(label)

# X_seq_padded = np.array(X_seq_padded)    # shape (total_segments, MAX_SEQ_LEN, n_features)
# y_seq_labels = np.array(y_seq_labels)    # shape (total_segments,)

X_seq_padded = np.array(X_seq_padded, dtype=np.float32)
y_seq_labels = np.array(LabelEncoder().fit_transform(y_seq_labels), dtype=np.int32)

print("Final X shape:", X_seq_padded.shape)      # (n_segments, MAX_SEQ_LEN, 132)
print("Final y shape:", y_seq_labels.shape)      # (n_segments,)

label_encoder = LabelEncoder()
y_int = label_encoder.fit_transform(y_seq_labels)  
# e.g. "Kick"->0, "Punching"->2, "Standing"->1 (the mapping depends on alphabetical order)

# Convert to NumPy
y_int = np.array(y_int)
print(y_int.shape)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_seq_padded, 
    y_int, 
    test_size=0.2, 
    stratify=y_int,  # keep classes balanced
    random_state=42
)

print("Train shape:", X_train.shape, "Test shape:", X_test.shape)
print("Train labels shape:", y_train.shape, "Test labels shape:", y_test.shape)
```

### Inference
```python
import cv2 as cv
import numpy as np
import collections
import tensorflow as tf

# 1) Define constants (must match your training setup)
MAX_SEQ_LEN   = 30
NUM_FEATURES  = 33 * 4   # 33 landmarks × (x,y,z,visibility)
CLASSES = ["Kicking", "Punching", "Standing"]
VIS_THRESH     = 0.3      # visibility threshold
PUNCH_SPEED_T  = 0.02     # normalized‐coords/frame threshold for punching
KICK_SPEED_T   = 0.05    # normalized‐coords/frame threshold for kicking

# 2) Load your trained models
lstm_model = tf.keras.models.load_model("model_weights/lstm_dr30.keras")
gru_model  = tf.keras.models.load_model("model_weights/gru_dr30.keras")
dnn_model  = tf.keras.models.load_model("model_weights/dnn_dr40.keras")

# Pick which to use:
infer_model = dnn_model  # or gru_model, or dnn_model

# Landmark indices
WRISTS = [
    mp.solutions.pose.PoseLandmark.LEFT_WRIST.value,
    mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value
]
KNEES  = [
    mp.solutions.pose.PoseLandmark.LEFT_KNEE.value,
    mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value
]
ANKLES = [
    mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value,
    mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value
]

# Helper to compute max 2D speed in a buffer for given landmark indices
def max_landmark_speed(buffer, landmark_idxs):
    """
    buffer: deque of length MAX_SEQ_LEN, each element is flat [x1,y1,z1,vis1,...]
    
    xi, yi: is in the range [0 … 1], where 1.0 means “100% of the frame width” (for x) 
			or “100% of the frame height” (for y).
    
    landmark_idxs: list of landmark indices to check (0-based 0–32)
    returns: max Euclidean speed (in normalized coords per frame)
    """
    seq = np.array(buffer, dtype=np.float32)  # shape (T, 132)
    # extract only x,y coords for our landmarks
    speeds = []
    for lm in landmark_idxs:
        #? xi, yi is the normalized‐coordinate units per frame, 
        #? 
        xi = seq[:, lm*4 + 0]  # x
        yi = seq[:, lm*4 + 1]  # y
        # compute displacements between successive frames
        dx = np.diff(xi)
        dy = np.diff(yi)
        dist = np.sqrt(dx*dx + dy*dy)  # length T-1
        speeds.append(dist)
    # stack all speeds and return the overall max
    if speeds:
        return float(np.max(np.stack(speeds)))
    else:
        return 0.0
        
# Helper to compute max 2D speed in a buffer for given landmark indices
def max_landmark_speed(buffer, landmark_idxs):
    """
    buffer: deque of length MAX_SEQ_LEN, each element is flat [x1,y1,z1,vis1,...]
    landmark_idxs: list of landmark indices to check (0-based 0–32)
    returns: max Euclidean speed (in normalized coords per frame)
    """
    seq = np.array(buffer, dtype=np.float32)  # shape (T, 132)
    # extract only x,y coords for our landmarks
    speeds = []
    for lm in landmark_idxs:
        xi = seq[:, lm*4 + 0]  # x
        yi = seq[:, lm*4 + 1]  # y
        # compute displacements between successive frames
        dx = np.diff(xi)
        dy = np.diff(yi)
        dist = np.sqrt(dx*dx + dy*dy)  # length T-1
        speeds.append(dist)
    # stack all speeds and return the overall max
    if speeds:
        return float(np.max(np.stack(speeds)))
    else:
        return 0.0
        
# === MediaPipe setup ===
mp_pose = mp.solutions.pose
pose    = mp_pose.Pose(min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# === Rolling buffer ===
buffer = collections.deque(maxlen=MAX_SEQ_LEN)

# === Webcam ===
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,  960)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.resize(frame, (960, 720))
    rgb     = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = pose.process(rgb)

    # 1) Extract keypoints or zeros
    if results.pose_landmarks:
        keypoints = []
        for lm in results.pose_landmarks.landmark:
            keypoints.extend([lm.x, lm.y, lm.z, lm.visibility])
    else:
        keypoints = [0.0] * NUM_FEATURES

    buffer.append(keypoints)

    # Default label
    label = "Warming up..."

    # 2) When we have enough frames, do conditional + model inference
    if len(buffer) == MAX_SEQ_LEN:
        # Check visibility of WRISTS/ANKLES first
        has_limbs = False
        if results.pose_landmarks:
            for idx in WRISTS + ANKLES:
                if results.pose_landmarks.landmark[idx].visibility >= VIS_THRESH:
                    has_limbs = True
                    break

        if not has_limbs:
            # No hands/feet visible → Non‑violent
            class_name, confidence = "Non violent", 100.0
        else:
            # Run your model
            seq = np.array(buffer, dtype=np.float32)
            if infer_model.input_shape[-1] == seq.size:
                seq_input = seq.reshape(1, -1)
            else:
                seq_input = seq[np.newaxis, ...]
            preds      = infer_model.predict(seq_input, verbose=0)[0]
            class_id   = int(np.argmax(preds))
            confidence = float(preds[class_id] * 100)
            class_name = CLASSES[class_id]

            # 3) Motion‐speed check override
            if class_name == "Punching":
                speed = max_landmark_speed(buffer, WRISTS)
                if speed < PUNCH_SPEED_T:
                    class_name, confidence = "Non Violent", 100.0
            elif class_name == "Kicking":
                # check both knees and ankles
                speed_knee  = max_landmark_speed(buffer, KNEES)
                speed_ankle = max_landmark_speed(buffer, ANKLES)
                if max(speed_knee, speed_ankle) < KICK_SPEED_T:
                    class_name, confidence = "Non Violent", 100.0

        label = f"{class_name} ({confidence:.1f}%)"

    # 4) Draw
    cv.putText(frame, label, (30, 50),	
               cv.FONT_HERSHEY_SIMPLEX, 1.5, (255,58,58), 5)
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp.solutions.drawing_utils.DrawingSpec((245,117,66),2,2),
            connection_drawing_spec=mp.solutions.drawing_utils.DrawingSpec((245,66,230),2,2)
        )

    cv.imshow("Live Action Detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
pose.close()
```


### Data Visualization
- **Normalized keypoints** (34 features = 17 joints × 2D)
    
- **Joint distances** (let’s say 16 distances for example)
    
- **Bone angles** (say 10 angles)

- MAX_SEQ_LEN = 5 frames
    
- Feature vector per frame = 34 (normalized joints) + 16 (distances) + 10 (angles) = **60 features**
    
- Each sequence is padded or truncated to exactly 5 frames
    
- Final model input shape = `(num_samples, 5, 60)`

**Abstract Example**
```json
X_final[0] = [
  [ 0.01, 0.03, ..., 0.89 ],  # frame 1 (60 features)
  [ 0.02, 0.04, ..., 0.91 ],  # frame 2
  [ 0.01, 0.05, ..., 0.90 ],  # frame 3
  [ 0.00, 0.00, ..., 0.00 ],  # frame 4 (padding)
  [ 0.00, 0.00, ..., 0.00 ]   # frame 5 (padding)
]
```
	Each row = one frame of the person  
	Each value = a feature (joint xy / distance / angle)

Detail Breakdown (`X_final[0][0]`: frame 1 feature vector)

| Feature Type            | Description                                  | Count | Example (first few values)      |
| ----------------------- | -------------------------------------------- | ----- | ------------------------------- |
| Normalized<br>Keypoints | `[x0,y0, x1,y1, ..., x16,y16] / W,H`         | 34    | `[0.12, 0.55, 0.14, 0.56, ...]` |
| Distances               | Distances between adjacent joints (16 pairs) | 16    | `[0.04, 0.03, ...]`             |
| Angles                  | Angles (in radians) between joint triples    | 10    | `[1.57, 2.01, ...]`             |
```python

X_final[0][0] = [ 
  # --- 34 normalized joints ---
  0.12, 0.55, 0.14, 0.56, 0.15, 0.57, ..., 0.31, 0.68,  # shape (34,)

  # --- 16 distances between connected joints ---
  0.04, 0.03, 0.05, ..., 0.07,                         # shape (16,)

  # --- 10 angles in radians (e.g., elbow, knee, etc.) ---
  1.57, 2.01, 0.87, ..., 2.45                          # shape (10,)
]
```

- **Shape of one sample**: `X_final[i].shape == (5, 60)`
    
- **Shape of dataset**: `X_final.shape == (num_samples, 5, 60)`
    
- **Labels**: `y_final.shape == (num_samples,)`, with values like `0`, `1`, `2` corresponding to `"Kicking"`, `"Punching"`, `"Non-violent"`.

**Note:** 
1) Test Features **Engineering** (distanct + joint)
2) Add dataset
	1 variant
	Punching (30s - 50s)
	Kicking (30s - 50s) 
3) Algorithm (predict hidden limbs)
$\theta$
