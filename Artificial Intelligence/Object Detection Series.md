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


# IoU
>How do we measure how good a bounding box is?

$$IoU=\frac{\text{Area of Intersection}}{\text{Area Union}}$$
+ loU > 0.5: "decent"
+ IoU > 0.7: "pretty good"
+ loU > 0.9: "almost perfect"

**How to get the Intersection ?**
In computer vision, you go from the top left. Get the corner point of each Bouding Box.
![[Pasted image 20241122153807.png]]

### Intersection area coordinate (yellow region)
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




