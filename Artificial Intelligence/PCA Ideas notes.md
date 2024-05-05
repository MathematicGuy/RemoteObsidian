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
The distance between the root and the point: a doesn't change. so if 
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
-> We repeat until the sum of eary point's distance from the origin largest.  Ultimatly we end up with...
The line with the longest distance from the projected point called **Principal Component 1 (PC1 for short)**

![[Pasted image 20240505103323.png]]
![[Pasted image 20240505160116.png]]
use pythago to calc the distance
![[Pasted image 20240505103443.png]]
 ![[Pasted image 20240505103643.png]]
Divide 4.12 to each points
![[Pasted image 20240505103738.png]]
all 3 sides means -> 3 side of the triangle

![[Pasted image 20240505160548.png]]

![[Pasted image 20240505161531.png]]

Now that we've have figure PC1 all out let's work on PC2
