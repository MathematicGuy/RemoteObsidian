**Building a Visual Vocabulary from CNN Patches & Encoding Images as BoF Histograms**

This guide shows how to:

1. **Extract intermediate CNN feature maps** as a source of local patch descriptors.
    
2. **Cluster these patch descriptors** to form a "visual vocabulary" (codebook).
    
3. **Quantize** each image’s patch descriptors against the codebook to build a Bag-of-Features histogram.
    

---

## 1. Overview of the Pipeline

1. **Pretrained CNN Backbone**
    
    - Use a network (e.g., ResNet-50) pretrained on ImageNet. Remove its final classification head, so you can access feature maps (e.g., output of `layer3`).
        
2. **Patch Descriptor Extraction**
    
    - For each image, forward‑pass through the CNN and extract the feature map tensor of shape `(C, H, W)`.
        
    - Treat each spatial location `(h, w)` as a descriptor of dimension `C`.
        
3. **Visual Vocabulary Construction**
    
    - Sample a subset of descriptors from many images.
        
    - Run **K-Means** clustering (e.g., `K=1000`) on these `C`‑dim vectors to obtain `K` cluster centers (the codebook).
        
4. **Encoding Images**
    
    - For each image, extract its full set of `C`‑dim descriptors.
        
    - Assign each descriptor to its nearest codebook center.
        
    - Build a length-`K` histogram of assignments and **L1-normalize** it.
        
    - This histogram is the Bag-of-Features representation.
        
5. **Classification**
    
    - Train a simple classifier (e.g., an MLP or SVM) on these histograms.
        

---

## 2. Detailed Steps & Code

Below is a self-contained Python example using PyTorch + scikit-learn.

```python
import torch
import torch.nn as nn
from torchvision import models, transformsrom PIL import Image
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import glob

# ---- CONFIGURATION ----
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
BACKBONE = 'resnet50'
LAYER_NAME = 'layer3'
N_CLUSTERS = 500  # size of vocabulary
DESCRIPTORS_PER_IMAGE = 200  # to sample for clustering

# ---- 1. Prepare CNN feature extractor ----
model = getattr(models, BACKBONE)(pretrained=True)
modules = list(model.children())
# Truncate after layer3
feature_extractor = nn.Sequential(*modules[:7]).to(DEVICE).eval()

# ---- 2. Image preprocessing ----
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

# ---- 3. Collect descriptors for clustering ----
all_descriptors = []
image_paths = glob.glob('/path/to/images/*.jpg')
for img_path in image_paths:
    img = Image.open(img_path).convert('RGB')
    x = preprocess(img).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        fmap = feature_extractor(x)  # shape: [1, C, H, W]
    C, H, W = fmap.shape[1:]
    descs = fmap.view(C, -1).cpu().T.numpy()  # shape: [H*W, C]

    # randomly sample
    idx = np.random.choice(descs.shape[0], DESCRIPTORS_PER_IMAGE, replace=False)
    all_descriptors.append(descs[idx])

all_descriptors = np.vstack(all_descriptors)
print(f"Collected descriptors: {all_descriptors.shape}")

# ---- 4. K-Means clustering to build codebook ----
kmeans = MiniBatchKMeans(n_clusters=N_CLUSTERS, batch_size=10000)
kmeans.fit(all_descriptors)
codebook = kmeans.cluster_centers_

# ---- 5. Encode each image as BoF histogram ----
def compute_bof_histogram(image_path, extractor, codebook):
    img = Image.open(image_path).convert('RGB')
    x = preprocess(img).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        fmap = extractor(x)
    C, H, W = fmap.shape[1:]
    descs = fmap.view(C, -1).cpu().T.numpy()

    # assign descriptors to nearest cluster
    assignments = kmeans.predict(descs)
    hist, _ = np.histogram(assignments, bins=np.arange(N_CLUSTERS+1))
    # L1 normalize
    hist = hist.astype(float)
    hist /= hist.sum()
    return hist

# Example: encode a single image
hist = compute_bof_histogram(image_paths[0], feature_extractor, codebook)
print(f"BoF histogram: {hist.shape} sums to {hist.sum():.3f}")
```

---

## 3. Next Steps

- Experiment with **different layers** (`layer2`, `layer3`, `layer4`) for more local vs. global descriptors.
    
- Tune **`N_CLUSTERS`** to balance discriminative power vs. overfitting.
    
- Try **spatial pyramids**: build separate codebooks in different image regions and concatenate their histograms.
    
- Replace k-means with **GMM** for Fisher Vector encoding, which often yields stronger performance.
    

Feel free to adapt paths, batch sizes, and classifier choices to your environment and dataset!