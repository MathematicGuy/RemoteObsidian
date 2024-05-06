**PCA Overview**
Principal Component Analysis - allow to distribute each Cel seperatly
![[Pasted image 20240417103920.png]]
High collerate group together

**X axis > Y axis (show more different)** 
> If the distance between Red and Yellow in X-axis are equal to Red and Sky Blue in y axis. Then Red and Yellow are more different from each other.
![[Pasted image 20240417104010.png]]


![[Pasted image 20240505101343.png]]
![[Pasted image 20240505101354.png]]

![[Pasted image 20240505101446.png]]

What if we have 4 genes -> 4D mesurement -> ...

**Step-by-Step PCA**
step0:  Move all datas so the center is on top of origin (0,0)
![[Pasted image 20240505152500.png]]
step1: draw a line that goes through the origin
![[Pasted image 20240505101917.png]]
but how can we do that
![[Pasted image 20240505152705.png]]
step2: rotate the line to fit the data
1) project the datas to the line
![[Pasted image 20240505102007.png]]
![[Pasted image 20240505102042.png]]
To calc the distances, we use Pythagorism
![[Pasted image 20240505102228.png]]
![[Pasted image 20240505154347.png]]
b - distance between the line and the point (data).
c - distance from the projected point to the origin.
The distance between the root and the point: a doesn't change (constant). so if 
b get bigger -> c get shorter and in reverse.
![[Pasted image 20240505102257.png]]
Thus, PCA can either minimize the distance to the line (b) or maximize the distance from the projected point to the origin (c)
![[Pasted image 20240505102459.png]]

![[Pasted image 20240505102611.png]]

![[Pasted image 20240505102719.png]]
repeat for d1 to d6
![[Pasted image 20240505102746.png]]
Next we square all of them to that negative values don't cancel out positive values. 
![[Pasted image 20240505102843.png]]
this called SS (distances) for short
![[Pasted image 20240505102942.png]]
-> We repeat until the sum of every point's distance from the origin largest.  Ultimatly we end up with...
The line with the longest distance from the projected point called **Principal Component 1 (PC1 for short)**

![[Pasted image 20240505103323.png]]
using pythagorian we got 
$$
a = \sqrt{b^2 + c^2} = \sqrt{4^2 + 1^2} = 4.12
$$
![[Pasted image 20240505160116.png]]
+ a / 4.12 = 4.12 / 4.12
+ b / 4.12 = 4 / 4.12
+ c /4.12 = 1 / 4.12
use pythago to calc the distance
![[Pasted image 20240505103443.png]]
 ![[Pasted image 20240505103643.png]]
Divide 4.12 to each points (or all 3 sides of the triangle)
![[Pasted image 20240505103738.png]]
by dividing b and c to the a (PC1) we know that PC1 is the Mixed of 97% of Gene1 and 2.42% of Gene2 -> Gene1 is 4 times of Gene2. 
![[Pasted image 20240505212215.png]]
![[Pasted image 20240505160548.png]]

![[Pasted image 20240505161531.png]]

Now that we've have figure PC1 all out let's work on PC2
![[Pasted image 20240505212325.png]]
This mean the recipe for PC2 is (-1 Parts Gene 1) and (4 Parts Gene 2)
![[Pasted image 20240505212517.png]]
![[Pasted image 20240505212617.png]]
-> Just like PC1 but in Y axis. They tell us that, in terms of how the values are projected onto PC2, Gene 2 is 4 times as important as Gene 1.
> And just like PC1 we have the sum as the distance. 
	![[Pasted image 20240505212802.png]]SS / n-1 mean divide the average total distance of every points to the total numbers of point except for the origin (center point) because the fomular calc from the origin.
+ So what Eigenvalue mean and what does it do: Eigen value show us the average projected distant of every points on the plane to the origin (0,0) or the Genes Origin.
-> So if we have more than 1 PC, we can determine what PC take up most points or in other words have the most point closed to its. (further explaination and example below)


To draw the final PCA plot, we rotate everything so the PC1 is horizontal. Then we use the projected point to find where the samples go in the PCA plot
Example: We take the coordinate of 1 each from from PC1 and PC2, then we have the position of Sample 6. 
![[Pasted image 20240505213515.png]]
and Sample 1.
![[Pasted image 20240505213625.png]]

Let get a deeper understand before we go any further.
![[Pasted image 20240505213650.png]]
For example: the **Variation of PC1 is 15 and PC2 is 3 -> total PCs = 18**
that mean **PC1 = 15 / 18 = 0.83  = 83% of the total variation around the PCs**. And PC2 take up 17% 

![[Pasted image 20240505213905.png]]

**What if we have 3 Genes**, well then we just have 3 Ingerdients. 
+ With PC1 have Gene3 as the most importance ingredient.
![[Pasted image 20240505214057.png]]
For PC2, the next best fitting line given that it goes through the origin and it is perpendicular to PC1. 
Just like before, we calculate the distance between each point to the line. And get the final result if the sum from the projected distance to the origin of each point is largest.  
-> we have Gene2 the most importance ingre for PC2.
![[Pasted image 20240505214246.png]]
Lastly we find PC3, the best fitting line that foes throught the origin and is perpendicular to PC1 and PC2
![[Pasted image 20240505221428.png]]
If we had more Genes, we'd just keep on finding more and more principal component by adding perpendicular lines and rotating them...
	In theory there is one per gene (or variable) but in practice, the number of PCs is either number of variables or the number samples, whichever is smaller.
![[Pasted image 20240505221750.png]]
In this case
![[Pasted image 20240505221811.png]]
![[Pasted image 20240505223503.png]]
Once I have all the principal components figured out, I can use the eigenvalues (SS - distance) to determine the proportion of variation  that each PC accounts for (% of each PC account for)
![[Pasted image 20240505223943.png]]
+ In this case we have PC1 and PC2 account for 90% of the variation so we can just use those to draw a 2-D PCA graph
![[Pasted image 20240505225524.png]]

**PCA - Practical Tips**
1) **Scaling your data**
	Make sure the data is on the same scale
	Ex: Math score in 100 scale. Reading in 10 scale -> scale them all up to 100 or 10. If not it shall lead to misinformation.
	![[Pasted image 20240505230356.png]]
	![[Pasted image 20240505230224.png]]
	Correct scaling help us to read the right data.
	![[Pasted image 20240505230314.png]]
	![[Pasted image 20240505230334.png]]

2) **Centering your data**
	![[Pasted image 20240505230609.png]]
	So make sure that I'm using centers PCA data or center the data myself. 

3) **How many principal components you should expect to find**
	If we try to find the 3rd PC in a 2D graph -> impossible
	![[Pasted image 20240505230806.png]]
	However let try to understand why it cannot be like that, we could add the 3rd line and rotate it until it perpendicular to PC1 and PC2, but is that possible (pss, no it not bruh) 
	![[Pasted image 20240505231217.png]]
	![[Pasted image 20240505231225.png]]
	So the answer is we can only have the 3rd line perpendicular to the 1st and 2nd line is to have the graph in 3-Dimension or more.
	![[Pasted image 20240505231240.png]]
Scenario: Math and Reading score are 100% correlated
	![[Pasted image 20240505231523.png]]
	As we can see, If we can have the 2nd line perpendicular to the 1st line
	![[Pasted image 20240505231651.png]]
	...This mean that the eigenvalue for the new line (the sum of sqr of the distance between the points projected onto the line and the origin), would be 0. (each distance projected to the line between the origin would be 0, because all of them are align with eachothers. (straighline across the origin)
	![[Pasted image 20240505231741.png]]
	![[Pasted image 20240505233457.png]]
	Likewise if we have 2 student
	![[Pasted image 20240505233524.png]]
	and then we center the data to find PC1, we could find a line that is perpendicular to PC1 but the eigenvalue would be 0
	![[Pasted image 20240505233620.png]]
	A simple way to understand this is that, 2 points define a line. So 2 point can only have a PC. 
	![[Pasted image 20240505233729.png]]
	
	![[Pasted image 20240505233750.png]]
	And just like before, 2 Students give us only 2 Point -> 1line -> So we only have 1 PC
		(note that all the subject represent the value scale and coordinate the point (student))
	But if we have 3 student, we can define a plane then we would predict that there'd only be 2 principal components...
	![[Pasted image 20240505234030.png]]
	...so we can again center the data, find the line through the origin that fits best (PC1)
	![[Pasted image 20240505234259.png]]
	![[Pasted image 20240505234323.png]]
	![[Pasted image 20240505234344.png]]
