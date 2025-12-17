
![[Pasted image 20250119101113.png]]


## Pose Estimation (PE) Flavors
**Single/Multi Object**
+ **Top-Down:** First get the Proposals of the Object then you extract  Object's keypoints.
+ **Bottom Up:** Find the Object's Keypoints (i.e. Skeletons of a Person, Bee, etc...) and use them predict Object. 
**Single/Multi Class:** Detect many Class (e.g. Detect both Fish and Bee at the same time)
![[Pasted image 20250119103307.png]]

## PE Challenges
+ Many unknown Subjects in an Images. 
+ **Occlusions:** multi-person and non-visible object in the same image.
![[Pasted image 20250119103908.png]]

## Datasets
Most Common 2D Dataset -> COCO dataset from YOLO
Human3.6M -> 17 Basic Human Interactions with 3.6mil 3D human poses.
![[Pasted image 20250119104201.png]]

## Evaluation Metrics
Comaparing Points of  each Line (i.e. Skeleton's Segment). 
![[Pasted image 20250119104449.png]]
h & L is a constant properties (e.g. head to neck length) 
0.5 mean *half-the-distant*.  
![[Pasted image 20250119104509.png]]
(find out more about Eva metrics)

Note: Single-Object PE (Shouldn't do this)

**DeepPose (DNN-based regressor)**
![[Pasted image 20250119104857.png]]
DNN came into 2 different stages: 
1) **Initiate Stage:** use to pre-predict key-points. 
	+ Receive the Image 
	+ Propose 14 diff positions
2) **Refinement Stage**: use to **predict refinement positions** ![[Pasted image 20250119105047.png]]

## How to represent keypoint outputs ?
![[Pasted image 20250119105757.png]]
Heat map for each of those keypoints (i.e. classes) - prob of a certain pixels to beyond that keypoint is encoded. 
+ $ **Encode each keypoints** and assign a confidence score. 
+ ? Ex: Green corresponding to the right shoulder, Blue to the left, etc.
note: kps mean keypoints
Each color channel in the tensors represent the elbows, shoulders, knees and diff types of kps.    
+ Output will then be post-process because we would have many positions (kp) using NMS or LMS (Local Maximum Search). 

+ ? **How good is OpenPose:** Yes ![[Pasted image 20250119110109.png]]
 
## Part-Affinity-Field (PAF)
+ ? Is a proposed solution for Ambiguties (mơ hồ) problems. e.g. **2 shoulder and 2 elbows**, how can we know **which belong to the left and right hand**.  
+ $ PAF **Encode Connections Between 2 Parts**. Example Elbow to Wirst or to Hand). 
+ ?  PAF is a *vector field* which come from 2 components x and y for each pixels. (**Each pixel assign as a Vectors**)  
**Example:** **Encode person's behaviour by Vectors Orientation** and assign each orientation range with diff colors. So hand/limb point down is yellow, horizontal is red and raise up is green. 
![[Pasted image 20250119110156.png]]
	
## OpenPose Overview
+ ? Open Pose seperate the inputs into 2 parts: 
	+ **Part Confidence Maps (PCM):** Heat map showing the confidence of each parts (elbows and the shoulders in example below).
	  
	+ **Part Affinity Fields (PAF):** Encode each parts orientation with colors. (use to predict parts movements)   
	
The **post-processing** of those 2 kind of Maps (i.e. PCM and PAF) -> Lead to the first **matching of those parts** if we have 2 shoulders and 2 elbows.   
![[Pasted image 20250119110734.png]]
+ ? **Problems:** **which elbows to we connect that shoulder to.** One we make up this part, we then merge it (i.e. elbow to shoulder) into the skeletons of the corresponding human. 



## OpenPose: Network
![[Pasted image 20250119115319.png]]
$L^{t}$  (PA): Part-Affinity (Field)
$S^t:$ Confident Heat Map

Each States output 18 vectors represent 18 parts of the skeletons.
![[Pasted image 20250119120115.png]]


## Merging parts to persons
```ad-abstract
Merging parts to persons by choosing the highest PAF scores between each keypoints where Score are the sum of vectors between in the line connect keypoint 1 and keypoint 2. 
```
> Using PAF scores. But first let see how do we do the Scoring parts.  
![[Pasted image 20250119123432.png]]


### Scoring pairs of parts
Note:
+ Each vector represent a pixel. 

We would expect each vector from p1 to p2 (i.e. point 1 and 2) having the same direction are postive value. (oppsite are negative)   
+ $ We **Scoring each parts** by taking the **Sum of Vectors that are On The Line Between Keypoint 1 and Keypoint 2** . Because vectors in opposite direction would be negative, vectors pair with highest score would always correct.   
+ ? Perform dot product between $V^T$ and $W_{i}$ 
![[Pasted image 20250119123904.png]]

## Assigning Parts in a Bipartite Graph
**n:** shoulders
**m:** elbows
**Emn:** shoulders to elbows scores (calculate above)
>Assigning Parts using Greedy Assignment. 
>1) **Collecting** Scores (Each Elbow to Each Shoulder).
>2) **Sorting** Scores in Ascending order.
>3) **Retrieve the Highest elbow to shoulder Scores** for each *elbow-shoulder pair.*
![[Pasted image 20250119125330.png]]
+ ! Not always correct & best for Global solution, but good & fast in generals. 

## Merging pairs to persons: merge by parts
![[Pasted image 20250119130343.png]]
