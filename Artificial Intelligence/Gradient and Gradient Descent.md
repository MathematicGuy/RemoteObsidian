# Lesson 1: Gradient

### Intro: Tangent Plane
Tangent Plane: mặt phẳng tiếp tuyến
	contain the tanget lines of more than 2 tangent lines.
	![[Pasted image 20240805104205.png]]
### Partial Derivative - Part 1 (Đạo hàm riêng)
> Partial Derivative mean to calculate the derivative of each variable.
	![[Pasted image 20240805102659.png]]
	![[Pasted image 20240805102942.png]]
+ $ Treat the not derivative one as a Constant. Ex: Derivative of x, see y as a constant. 
	$f_{x} = 2x$ and $f_{y} = 2y$

### Partial Derivative - Part 2
$f(x, y) = 2x^2y^3$
$=> f(x,y) = 6xy^3$
	![[Pasted image 20240805103507.png]]

### Gradient
	![[Pasted image 20240805105716.png]]
	
	
### Gradients and maxima/minima
+ ? **Minimum is when slope = 0** <-> Both Slopes of x and y is  0
	![[Pasted image 20240805105858.png]]
To Calculate the the function minimum, we **calc the Derivative of 2 variables and set it equal to 0.**
	![[Pasted image 20240805110029.png]]
### Optimization with gradients: An example (in 3D)
+ $ $Motive: Find the **Coldest place in the Sauna Room**
+ ? The coldest place in the room is when every other direction you walk are hoter.
	![[Pasted image 20240805110428.png]]
	To get to that Coldest position we calc the Partial Dervative we see that it symmetric to the floor.
	![[Pasted image 20240805110505.png]]
	**Example:**
	1) **Calculate the Partial Derivative of f(x,y) which is the derivative of X and Y**![[Pasted image 20240805111430.png]]
	2) **Set the Partial Derivative = to 0**![[Pasted image 20240805111648.png]]
	We notice there are some point outside of the Sauna, so just remove those invalid values. 
	+ $ Insert x, y back to the function, we see that x=4 and y=4 it the Minimum of the function. ![[Pasted image 20240805111837.png]]

### Optimization using Gradients - Analytical Method
