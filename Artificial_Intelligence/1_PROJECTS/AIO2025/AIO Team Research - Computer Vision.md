**dataset:** Conser-vision Practice Area: Image Classification - [src](https://www.drivendata.org/competitions/87/competition-image-classification-wildlife-conservation/page/483/#features_list)

**Bag of Visual Words** (K-Mean + SIFT) 
For each feature apply a circle then extracting features of the image within those circle. (A Image can have many SIFT features) 
	All extracted features are encoded as a id which can be used to group into clusters later. ![[Pasted image 20250525073954.png]]
	By group different features into cluster, we can measure the Feature Histogram of the image and determind what kind of image it is. 
+ ? e.g. the upper image is contain a person because there are more features represent human than a bike, the same go for the lower image, its contain more bike's feature than human's feature.   ![[Pasted image 20250525074350.png]]

![[Pasted image 20250525075226.png]]
Sliding window in HOG extract features linearly, only slide in 1 direction -> Fail to detect if there are 2 similar group of features close to each other (i.e red & yellow).   
![[Pasted image 20250525075512.png]]


**Object Extraction Pipeline**
![[Pasted image 20250525075725.png]]

Note: new field of study created to understand how Deep Learning Model understand -> Explainable AI 
+ ? There once a research team trying to combine dataset of tank and tank hiding inside a bush, the result give high accuracy, it is too good to be true. After analyse it, the research figure out the ML Model actually classified the sky is cloudy or sunny, not the tank itself. ![[Pasted image 20250525080346.png]]
+ $ **What you think your model learn** can be different **what your model actually learn.** This is why you should understand what your model are doing. 

[[Xplainable AI (xAI)]]

