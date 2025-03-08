**Main Different between Supervised & Unsupervised & Reinforcement Learning:**
+ **Supervised Learning** learn then predict data based on the given labeled input dataset. (e.g. Classification, Time Series, Prediction, etc...)
+ **Unsupervised Learning** learn a unlabeled dataset in order to find patterns of the given dataset. (e.g. Segmentation, Categorizing, Identifying Pattern, etc...)
+ **Reinforcement Learning** is a ML technique that teach ML Model learns base on some set-of-polices that is reward-and-punishment. 

**CNN vs MLP**
	**CNN extract spatial features** (đặc trưng không gian) like **edges, textures and patterns** while **MLP is less efficient at capturing spatial features** compared to CNNs even with features engineering.


### What the different between Keras, Tensorflow and Pytorch
+ **Keras** is a **high-level network API specialize in Deep Leraning** that integrated in TensorFlow. 

+ **TensorFlow** was developd for a **range of rask include math, machine learning** with **comprehensive ecosystem** of community resources, lib and **tools that facilitate building and deploying ML applications**. 

+ **PyTorch** is a **Deep Learning framework specialize in NLP.**

![[Pasted image 20250108112844.png]]

---

MLP take 1D input -> cannot differentiate features at diff position, its only recognized object but not where the object, hence why MLP is bad for recognized spatial features.  

**What is Spatial Features ?**


**Why kernel help highlight certain features of the image ?**

---

### Penalized
Add $\lambda$ to penalized multiple weights. larger $\lambda$ is smallar $W_i$ is 
![[Pasted image 20250205120006.png]]

### Drop Out
Each training dataset, we randomly remove a subset of neurons.
![[Pasted image 20250205120119.png]]

## [One-Hot Encoding vs Label Encoding]((https://www.analyticsvidhya.com/blog/2020/03/one-hot-encoding-vs-label-encoding-using-scikit-learn/#:~:text=Label%20encoding%20assigns%20integers%20to,nominal%20and%20number%20of%20categories)
![[Pasted image 20250207111442.png]]
+ **One-Hot Encoder:** Encode features into a array where each value is either 0: False or 1. Each feature have their own array fill with 0 (array length == number of feature) but value 1 at feature_index.     
+ **Label Encoding:** assign id to each features 


### Cross-Validation
**K-fold Cross-Validation:** divide to each part for test, validate, 


# RNN
Độ quan trọng của từ trong mẫu $\times$ độ quan trọng của từ trong văn bản 
BT: lấy ví dụ đơn giản cho TF-IDF 

---

[[CMC Deep Learning Midterm Test]]

## [[Autoencoder and Variational Autoencoder]]

