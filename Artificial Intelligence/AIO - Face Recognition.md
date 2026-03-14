
*Main Concept - what are the step of ?* where the Input is a Image contain a Face
0. Convert online Dataset format to your Dataset Format. 
	e.g. convert widerface dataset format to COCO dataset format to train YOLO.  
	
1. Face Detection - Extract face bouding box  ![[Pasted image 20260312165707.png]]
	
2. Face Alignment - *normalize face angle* (like id_card alignment)
	use WiderFACE or YOLO FACE (basically yolo pose with only face landmark 
	![[Pasted image 20260312170102.png]]
	![[Pasted image 20260312170702.png]]
3. Feature Extraction - extract feature within face bounding box (ArcFace - 98.36%)
	*Continual Learning Here* ![[Pasted image 20260312171011.png]]
	**ArcFace (Additive Angular Margin Loss for Deep Face Recognition)** 
	+ ? ArcFace đưa ra một hàm mất mát mới dựa trên khoảng cách góc trong không gian đặc trưng![[Pasted image 20260312171904.png]]
	-> Instead of compare using Cosine Similarity - it compare the current sample with the Center of a Feature's Group (stay close similar group, staying alway disimilar group) where the center are called sub-center created by the loss function to force the majority of clean, correct classes/faces to naturally group into 1 "dominant" sub-class. 
	+ $ Help to learn Classes from Multple-Domain.
	![[Pasted image 20260312190112.png]]
	$m$ params help to *amplified the distant between disimilar image features.*
	+ @ ArcFace is a Loss Function so only use it when Training. ![[Pasted image 20260312190255.png]]
	+ ? ArcFace use ViT so make sure you have at least thousand of data for finetuning.
	
	 
4. Feature Matching - Use cosine similarity to check if the face feature similarity to any face within the facetabase :)) 



*Challanges in Face Recognition*
`Illumination` (Brightness in diff angle), `Various Expression`, `Pose` (face direction)

*Methods*
*Computation Redistribution* - SCRFD 
	re-distribute computation between system module to increase performance without increase total computation. 

Each Input Image include:
	image size: width x height
	bouding box format $(x_{\text{center}}, y_{\text{center}}, w, h)$ 
	
Fomula to calc bounding box $x$ and $y$ coordinates in 4 corners. $$x_{1} = x_{\text{center}}- \frac{w}{2} \space, \space y_{1}=y_{\text{center}}-\frac{h}{2}$$the same for $x_{}2, y_{}2$

*Face bounding box Annotation format for each image:* 
```
# 1 Image could hav multiple bboxes 
# <image_path> image_width image_height
bbox_x1 bbox_y1 bbox_x2 bbox_y2 
...
# <image_path> image_width image_height
bbox_x1 bbox_y1 bbox_x2 bbox_y2 
...
```
[Face Recognition Notable Methods](https://viblo.asia/p/paper-explained-some-face-recognition-approaches-facenet-arcface-cosface-Do754zgLZM6) - the evolution to ArcFace 


**Different Systems in different Face Recognition scenario** 
*RetinaFace* - detecting faces in a cowd under difficult conditions (poor lighting, severe angles, varying scales)  
+ $ robust face detection and dense 2D/3D facial landmark localization.
+ ? *Scenario Application:* When a group of students walks toward the campus entrance, RetinaFace scans the crowd to detect every face. It successfully identifies students looking down at their phones or turning away from the camera, mapping the exact structural points of their eyes, nose, and lips despite the challenging angles.

*YOLO* - identifying and tracking multiple diff class of objects simultaneously with extremely low latency. 
+ $ High speed, general purpose object detection, classification and segmentation. 
+ ? Usecase: detecting multiple object orther than just faces.

*DeepFace* - Extract FACE FEATURE (*feature extraction and verification*)
+ $ embedded the extracted face and compare its feature within the facetabase to verify face identify.   
+ ? Usecase: Once model like RetinaFace isolates and crops a student's face from the crowd, DeepFace embed the cropped face and compares it to faces from the facetable to verify indentify and authorize entry.

*MTCNN (Multi-task Cascaded Convolution Networks)* - Isolating faces and basic landmarks using limited computation overhead. (*Efficient Facial Detection & Alignment*)
+ $ Joint face detection and alignment using a stepped, three-stage cascade architecture (P-Net, R-Net, and O-Net) 
+ ? Usecase: Act like a Efficient filter, MTCNN process the video feed in 3 quick stages. 1st it scans the whole image to find which likely to be a face, then filter out the false positive, and finally outputs the confirmed faces along with 5 landmarks (eyes, nose, mouth corners) to ensure the face is correctly *ALIGNED before sending the face to model like DeepFace.*
