**Problems & Challenges**
+ Lack of public data (Docter too busy for labeling) -> Low Quality Data.
+ Ethical problems, Low Quality Data
+ Garbage in, Garbage out in Model training. 
+ Foreigner Body is diff from Vietnames body -> Bias in labeling 
+ Accountability -> Medical Model only used under supervision 
	
**Technical Solutions**
![[Pasted image 20250206202945.png]]
![[Pasted image 20250206202957.png]]
- [ ] **Prioritize:** Accuracy, rather to diasnoised patient have illness than none illness at all. ~~~~

### Digital Image Processing (DIP) 
![[Pasted image 20250206204206.png]]
+ 8-bit is enough for human eyes to recognite changes easily.
+ Except for medical Image stored in 12-bit `[0 to 4096]` for more detail + features extraction. e.g. recognize pixel values of a tumors.

**Pixel value transformation**
+ **Isolated transformations:** enhance contrast, histogram equalization.

**Brightness:** represent under a histogram (i.e. color frequency)
-> Histogram Equalization make color frequency uniform. 
![[Pasted image 20250206205234.png]]
+ $ Phân bố toàn bộ các pixel trên mọi dải màu. 
+ $ Distribute all pixel to be equaler across all color range -> Help human see better, make image more visible.

**Basically Histogram apply PDF + CDF + some calculate + ranking**
![[Pasted image 20250209151214.png]]


**Contrast Limited Adaptive Histogram Equalization (CLAHE)**
![[Pasted image 20250206205526.png]]
+ $ Apply HE only to areas with pixel -> Focus HE on pixel specific area.  
	![[Pasted image 20250206210016.png]]
	![[Pasted image 20250206205544.png]]


**Medical file:** DICOM file -> must be process to read image inside DICOM file.

**Loss function in Medical focus on penelizing false positive & false negative** and focus on emphasizing accuracy purity.
![[Pasted image 20250206211011.png]]

### Simple Research Project: Breast Ultrasound Cancer Diagnosis
**Resnet:** Classification
![[Pasted image 20250206211947.png]]
**U-Net:** Segmentation
![[Pasted image 20250206211850.png]]

**Classification + Segmentation**
note: Research Try -> Wrong -> Retry with another method. 
Professor can đưa ra nhận định và góc nhìn tốt về bài toán hơn -> save research time.
![[Pasted image 20250206212155.png]]

**Suggest Research Questions**
![[Pasted image 20250206213108.png]]
1) Why U-net, not U-Net++ and others? 
2) Good/Top-tier Conference -> Hard requirements, Detail Feedback
	Local Conference -> feedback but not too detail.
3) Quantitative results might be clear, what about qualitative results (Visualization) ?
4) Try diff technique for Loss Function, Model, Pre-processing, Post-pocessing or Data augmentation. 
5) Look inside the system as each individual part, can we re-desgin the architecture, loss or any specific part of framework.

### Metrics
2 Object overlap càng nhiều -> Dice càng lớn (Kinda like IoU but emphasized)
![[Pasted image 20250206213904.png]]

**Synthetic data:** does its actually correct, or just a fraud and look correct through human eyes. 

**Trending in Computer Vision:** 3D Image like Recontruction, etc...
note: 3D CNN (for traffic Forecasting)
Swin3DUnet -> like transformer
Cùng **1 bài toán dùng mô hình 2D sang 3D**: có thể dc chấp nhận như **1 bài báo mới.**

**Prequisites for Medical Computer Vision:** 3D Segmentation 
2D to 3D -> Have data + labels: you good. 

**Down Sampling:** not recommend, reduce unimportant data in majority -> leading to information loss  
**Class Weight:** Recommend
**FocalLoss:** penalize minority
**Model not Efficient Enough** -> Don't try to feed more data

