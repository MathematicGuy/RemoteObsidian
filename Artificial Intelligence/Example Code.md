```python
# Example: Joint locations before and after normalization
# Assume two persons are detected in an image of size 1920x1080 (width x height)
image_width = 1920
image_height = 1080

# Joint locations for a closer person (closer to the camera)
closer_person_joints = np.array([
    [800, 400],  # Joint 1 (e.g., nose)
    [850, 600],  # Joint 2 (e.g., shoulder)
    [900, 750],  # Joint 3 (e.g., elbow)
    [920, 900]   # Joint 4 (e.g., wrist)
])

# Joint locations for a farther person (farther from the camera)
farther_person_joints = np.array([
    [400, 200],  # Joint 1 (e.g., nose)
    [425, 300],  # Joint 2 (e.g., shoulder)
    [450, 375],  # Joint 3 (e.g., elbow)
    [460, 450]   # Joint 4 (e.g., wrist)
])

# Normalize joint locations
normalized_closer_person_joints = closer_person_joints / [image_width, image_height]
normalized_farther_person_joints = farther_person_joints / [image_width, image_height]

# Create DataFrame for visualization
df = pd.DataFrame({
    'Joint': ['Nose', 'Shoulder', 'Elbow', 'Wrist'],
    'Closer Person (X, Y)': [tuple(x) for x in closer_person_joints],
    'Farther Person (X, Y)': [tuple(x) for x in farther_person_joints],
    'Normalized Closer (X, Y)': [tuple(x) for x in normalized_closer_person_joints],
    'Normalized Farther (X, Y)': [tuple(x) for x in normalized_farther_person_joints]
})

# Visualization
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Plot original joint positions
ax[0].scatter(closer_person_joints[:, 0], closer_person_joints[:, 1], color='red', label="Closer Person")
ax[0].scatter(farther_person_joints[:, 0], farther_person_joints[:, 1], color='blue', label="Farther Person")

# Annotate joints
for i, txt in enumerate(['Nose', 'Shoulder', 'Elbow', 'Wrist']):
    ax[0].annotate(txt, (closer_person_joints[i, 0], closer_person_joints[i, 1]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=12, color='red')
    ax[0].annotate(txt, (farther_person_joints[i, 0], farther_person_joints[i, 1]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=12, color='blue')

ax[0].set_xlim(0, image_width)
ax[0].set_ylim(image_height, 0)  # Invert Y-axis for correct visualization
ax[0].set_xlabel("X Coordinate")
ax[0].set_ylabel("Y Coordinate")
ax[0].set_title("Joint Locations Before Normalization")

# Plot normalized joint positions
ax[1].scatter(normalized_closer_person_joints[:, 0], normalized_closer_person_joints[:, 1], color='red', label="Closer Person")
ax[1].scatter(normalized_farther_person_joints[:, 0], normalized_farther_person_joints[:, 1], color='blue', label="Farther Person")

# Annotate joints
for i, txt in enumerate(['Nose', 'Shoulder', 'Elbow', 'Wrist']):
    ax[1].annotate(txt, (normalized_closer_person_joints[i, 0], normalized_closer_person_joints[i, 1]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=12, color='red')
    ax[1].annotate(txt, (normalized_farther_person_joints[i, 0], normalized_farther_person_joints[i, 1]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=12, color='blue')

ax[1].set_xlim(0, 1)
ax[1].set_ylim(1, 0)  # Invert Y-axis for correct visualization
ax[1].set_xlabel("X Coordinate")
ax[1].set_ylabel("Y Coordinate")
ax[1].set_title("Joint Locations After Normalization")

plt.legend()
plt.show()
```