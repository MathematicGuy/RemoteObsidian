
![[Pasted image 20240328134513.png]]

Image processing
	One point (left) * 3x3 matrix = one pixel (the image on the right) 
![[Pasted image 20240328135153.png]]
Blurred Image
![[Pasted image 20240328135251.png]]

![[Pasted image 20240328135451.png]]



Each value as a coordinate represent the relationship from person A to person B. Which is the Path number from Person A to B. 
If you multiply the Matrix by itself you will get the relationship of person n (n mean Matrix's total index)  
+ A^2 have the diagnol as the total relationship of each person.
-> n mean How many paths of this length exist between any 2 nodes
![[Pasted image 20240328140212.png]]

Sum of the number in the diagnol / by matrix size -> total number of triangle (3 person relationship)
![[Pasted image 20240328141835.png]]


