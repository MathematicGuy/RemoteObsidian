### Prerequisite
+ PCB Board (2 versions for each Model: Defecs and Non-Defects PCB)
	PCB Board Models must match with the training Dataset Model
+ Training Dataset 
+ Need a Bright Light for Visual (Scanning) Enhanment
+ Understand [How to find defects on a PCB](https://www.proto-electronics.com/blog/how-to-find-defects-on-a-pcb)



### Algorithm
+ **[[Anomaly detection in ML]]** for Anomaly Detection ([example](https://youtu.be/Q7YGBwKVpds?si=9FEmW0fZ2KUY7-v4))
+ [[Anomaly Detection]]
+ [[PCB Anomaly Detection RoadMap]]

### Reference Project
+ [PCB Anomaly Detection Preference Project](https://github.com/OpenAOI/anodet)
	+ [PathCore_anomaluy_detection](https://github.com/hcw-00/PatchCore_anomaly_detection?tab=readme-ov-file)
	+ [Code in directory sampling_methods](https://github.com/google/active-learning)
	+ [concatenate_two_layers function in feature_extraction.py](https://github.com/xiahaifeng1995/PaDiM-Anomaly-Detection-Localization-master)
	+ [pytorch_cov function in utils.py](https://github.com/pytorch/pytorch/issues/19037)
### My Learning Project
+ [[PCB defects detection using YOLOv5]]



---

DRC Design errors
Defect Types:
+ Unique Detection for each PCB Models
+ Detect of solder bridge (thép hàn ở chân cpu bị hàn lỗi hoặc nối với nhau, etc...)
+ Scratch Detection

Note:
> Nhận diện xử lý ảnh : ảnh 3D, ảnh Depth, các bài toán xác định dị vật, lệch chân, ...trên PCB... OpenCV, Halcon/ C++

+ Tài Liệu giới thiệu dự 
+ Làm Slide trình bày dự án

---
### How it work ?
![[Pasted image 20240901140425.png]]

#### Traditional machine vision systems use a two step process to make decisions (use Probability)
![[Pasted image 20240901140517.png]]
Flaws
![[Pasted image 20240901140903.png]]

#### New machine vision system (use deep learning)
![[Pasted image 20240901141138.png]]
**Top 5 MSE**
![[Pasted image 20240901141149.png]]

**Myth and Challenges**
![[Pasted image 20240901141400.png]]

#### Reference Deployment
![[Pasted image 20240901141919.png]]
driff (performance decay)
![[Pasted image 20240901141825.png]]


![[Pasted image 20240901142312.png]]
**Compare goal result (real) and prediction result (test)** -> total accuracy
![[Pasted image 20240901142041.png]]



![[Pasted image 20240901142235.png]]
> Skill people monitor results and label them for furhter model training.
