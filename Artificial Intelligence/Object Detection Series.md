**Goals of this Series**
![[Pasted image 20241122110558.png]]

**Object Localization** is finding **what** a (single) object exists in and **where** an image
**Object Detection:** Multiple Object Localization (same as above but for multiple object)
>Use x and y points to detect box.
![[Pasted image 20241122110337.png]]
### Localization
+ sliding window
+ ...
### Potential Problems ?
1. A LOT of computation !
2. Many bounding boxes for same object

**Regional based networks**
![[Pasted image 20241122151947.png]]
>warped region: 224x224
+ Problems with this: slow and computationally expensive.

**YOLO Simple Overview:**
>**Yolo**: split image into $S \times S$ grid. Each grid's cell represonsible for predict a label.
+ ? Ex: yellow cell predict bycicle, blue predict dog.
![[Pasted image 20241122152250.png]]

**Step 1: Divide the Image into a Grid** 
	The image is divided into $S \times S$ grid cells
	![[Pasted image 20241120112354.png]]
	
**Step 2: Prediction for Each Cell**
- Each cell predicts a fixed number of **bounding boxes**, along with:
	+ **Bounding Box Confidence**: A score indicating the accuracy of the box and whether it contains an object.
	- **Class Probabilities**: The probabilities for each possible class (e.g., bicycle, dog).
	
**Step 3:** **Clean and Finalize Bounding Boxes**:
+ Use **Non-Maximum Suppression (NMS)** to remove overlapping boxes and keep the best predictions for each object. 
	![[Pasted image 20241120113757.png]]


---
# IoU (Intersection over Union)
>How do we measure how good a bounding box is?

$$IoU=\frac{\text{Area of Intersection}}{\text{Area Union}}$$
+ loU > 0.5: "decent"
+ IoU > 0.7: "pretty good"
+ loU > 0.9: "almost perfect"

**How to get the Intersection ?**
In computer vision, you go from the top left (0, 0). The righter a point is, the larger its coordinates are -> With this infor, we now know how to get the corner point of each Bouding Box.
![[Pasted image 20241122153807.png]]

### Intersection area coordinate (yellow region)
>The intersection area top-left and top-right are easily find by mapping top-left and top-right points of the 2 boxes.
- `max` ensures that the intersection **starts inside both boxes** by taking the larger (inner) top-left coordinate.
- `min` ensures that the intersection **ends inside both boxes** by taking the smaller (inner) bottom-right coordinate.
>Box 1 is Blue & Box 2 is Red 
   Top Left Points 
	X1 is `max(box1[0], box2[0])`
	Y1 is `max(box1[1], box2[1])` 
  Bottom Right Points
	X2 is `min(box1[2], box2[2])`
	Y2 is `min(box1[3], box2[3])`
![[Pasted image 20241122171350.png]]
![[Pasted image 20241122171412.png]]


# Non Max Suppression (NMS) 
+ $ Cleaning up Bounding Boxes (from n boxes to 1 box) by take out the most precision box.

Retrieve all boxes IoU $\to$ remove boxes box_IoU < IoU_threshold
![[Pasted image 20241125085937.png]]

What if multiple classes ?
![[Pasted image 20241125090130.png]]
NMS (bboxes: bounding boxes; box: box inside bboxes)
1) for all box in bboxes, remove all box with `IoU` < `threshold` 
	`IoU = IoU(predicted bbox, true bbox)` 
2) Choose hpb (highest precision box) in bboxes
	For box in bboxes, if `box_i not hp_box` & `iou(hp_box, box_i) < iou_threshold`
	+ `box not hp_box`- not the highest precision box 
	+ `iou(hp_box, box_i) < iou_threshold` - retain others class boxes by retain all boxes that have iou with `hp_box` < iou_threshold (very low threshold) 
		saving all boxes that is far from the current box while eliminate all boxes close to the current box. (Basically **save others class boxes and remove all boxes of the current class except for class's highest precision box**)   
	Then save `hp_box` to nms_list


### Non-max suppresion algorithm
(Perhaps start with discarding all bounding boxes < probability threshold)
While BoundingBoxes:
- Take out the largest probability box
- Remove all other boxes with IOU > threshold
(And we do this for each class)

**parameters**
	predictions - should be boxes `[[box_id, box_iou, x1, y1, x2, y2]]` 
	iou_threshold
	prob_threhold 
	box_format="corners"

use `assert` to check if bboxes is a list
boxes_list = retrieve all boxes with IoU > IoU_threshold
retrieve highest IoU box out of all boxes in boxes_list

# Mean Average Precision (mAP) 
+ $ Evaluate and Compare object detection models

1. Get all bounding box predictions on our **test set**  ![[Pasted image 20241125143332.png]]
	 Bounding Box with IoU < Threshold is False Positive (FP mean predicted true but it actually false)
	 Bounding Box with IoU > Threshold is True Positive (TP mean predicted true and it is true) 
	**threshold** to be positive is 0.5 in this scenario  


2. Sort by **descending confidence** score 
	![[Pasted image 20241125143714.png]]
	**[[Precision and Recall]]** ![[Pasted image 20241125143905.png]]
	**Precision:** Of **all bounding boxes**, what **fraction** was **actually correct** ? (Trên tổng số kết quả dự đoán, bao nhiêu trong số đó là đúng)
	**Recall:** Of **all target bounding boxes**, what **fraction** did we **correctly detect** ? (Out of all positive, how many of them was correctly classified positive - trên tổng số TH đúng, bao nhiêu TH đc dự đoán là đúng và thực sự đúng)
	+ ? There's a battle between precision and recall! Different applications may prioritize recall and others precision. e.g. car auto driving prioritize recall bc it prefer not to crash any pedestrians.
 
 
3. **Calculate the Precision and Recall as we go through all out puts** (of dog class)
   note: only take account of a class highest confidence score![[Pasted image 20241125144719.png]]
	Precision = TP / total TP + total FP
	Recall = TP / Total  


4. **Plot the Precision-Recall graph** ![[Pasted image 20241125145333.png]]

5. **Calculate Area under PR curve** ![[Pasted image 20241125145315.png]]

6. This was only for dog class, we need to calculate for all classes. Let's say we do this for cats and dogs ![[Pasted image 20241125145412.png]]
 
7. Repeat for all class ? ![[Pasted image 20241125145510.png]]

---


~~**S1:** Already have bouding box for each class so let no care about that~~
**S2:** Retrieve Image Predicted and Ground Truth Confidence score using IoU and sort image by confidence score. Each Image only have 1 True Positive (1 bbox)

![[Pasted image 20241127093652.png]]
S2.1: check number of bboxes of each class
S2.1: retrieve confidence score of each class 
	2.1.1: Sorting class's confidence score
	2.1.2: retrieve highest confidence score bboxes of each class 

**S3:** Assign class TP and FP 
	Calc the IoU between predicted bboxes & ground truth bboxes of each class. 
	Save it to a list

**S4:** Calc Precision and Recall
![[Pasted image 20241127093633.png]]




def mean_average_precision(
	pred_boxes, # list: `[[train_index, class_pred, prob_score, x1, y1, x2, y2], ...]`
	true_boxes,
	iou_threshold=0.5,
	box_format="corners",
	num_classess = 20 # default for YOLO
)

1) retrieve prediction and groundtruth bboxes
2) keep track of image's total bboxes (using dictionary ofc)
	`img 0 has 3 bboxes, img 1 has 5 bboxes`
	`-> amount_bboxes={0:3, 1:5}`
	2.1) convert bboxes number into tensor 
	`amount_boxes = {0: torch.tensor([0,0,0])}`
3) sorting probability score
4) create data holder for TP, FP, Ground True (list) 
5) compare grounth truth with detect image
	take out the grouth truth with the same index with detection class
	Get the best IoU between the grounth true and detection clas 
	

we don't want multiple bboxes for 1 img, only the 1st one, bc the 1st one is correct, other one is false positive.

 

note: khi nào dùng list và dict