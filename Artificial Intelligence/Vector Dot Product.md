Source: https://www.mathsisfun.com/algebra/vectors-dot-product.html
![[Pasted image 20260204165454.png]]
![[Pasted image 20260204170258.png# left | 444]]
	$\cos(\theta):$ capture *directional alignment*
	$|a| \space . |b|$ capture vector *scale / strength* 
	
+ @ RESULT of te Dot Product is a Number (not a vector), its the "SCALAR" that represent the magnitude of one vector projected onto another. 

multiply two vectors it makes sense to multiply their lengths together _**but only when they point in the same direction**_
![[Pasted image 20260204170948.png]]


**Dot Product of Orthogonal vector** is ZERO because **$\cos(90^{o})=0$**
![[Pasted image 20260204165650.png | 444]]
-> This make much sense bc, dot product represent *the magnitude of one vector projected onto another.* Like shining the light example, perpendicular vector *don't project anything to eachother* (when you shining the light directly at a for example). 
![[Pasted image 20260204171309.png | 233]]


**Same Direction** have dot product of itself because $\cos(0)=1$ so just $a \cdot b = |a| \times |b|$
![[Pasted image 20260204165843.png]]


**Opposite Direction** result in Negative Magnitude.
![[Pasted image 20260204172546.png]]
Note: Dot Product + Normalization = cosine similarity. 
-> dot production indicates the strenth between 2 vector 
+ $a.b < 0$ if opposite then 2 strength *diminish* each other (obsivously)
	-> 2 vector *moving always* from each other. *unsimilarity*
	
+ $a.b > 0$ if same direction then 2 vector *strengthen* each other
	-> 2 vector moving with eachother, represent *similarity*. 
	
+ $a.b = 0$ then they have *no directional overlap* -> *unrelated* to eachother. 

Another way to calc dots product is to multiply vector coordinate, for 3D, just mult x, y and z. And if you need the angle, just use the 1st dot product fomula and find $\cos(\theta)$.
![[Pasted image 20260204170136.png]]