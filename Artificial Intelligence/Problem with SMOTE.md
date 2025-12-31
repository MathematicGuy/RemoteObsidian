## Why SMOTE shoudn't be use in Action Recognition
Basically, SMOTE add synthetic data by adding MINIMAL NOISE to the dataset while keeping the dataset balace. 
### Main Problem with SMOTE
The main problem with **SMOTE** (Synthetic Minority Over-sampling Technique) is that it creates synthetic examples by **linearly interpolating** *between existing data points*. In high-dimensional spaces (like images or video features), this often generates **noisy, unrealistic, or semantically invalid samples** because the "path" between two valid data points usually passes through invalid space (the data manifold assumption).
+ ? **linearly interpolating** simply means **drawing a straight line** between two existing data points and picking a new point somewhere along that line.
+ @ Basically, SMOTE synthetic data by *adding Value to the original data. This make the action recognition dataset un-realistic.* e.g. for a random Weight $\lambda$:
![[Pasted image 20251231171433.png | 555]]

### Problem with SMOTE in HMDB51 (Action Recognition)
Applying SMOTE to the **HMDB51** dataset is particularly problematic for two reasons:
+ ? Imagine adding a average value between 2 most similar/consecutive frames. This is unrealistic even for synthetic data. 
	
1. **Temporal Destruction:** Action recognition relies on temporal sequences (motion over time). Linear interpolation between two video feature vectors destroys the temporal coherence, creating "actions" that are physically impossible or lack valid motion patterns.
	   
2. **High-Dimensionality:** HMDB51 videos are complex spatio-temporal data. Interpolating between two "fencing" clips might create a feature vector that looks like noise rather than a valid intermediate fencing motion, confusing the model rather than helping it learn the minority class.
