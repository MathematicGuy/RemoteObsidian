
1) Create Main Screen
	import Screen, .tracer(0) -> smooth animation
2) Create Snake Body
	Class -> Create 1 Block -> Duplicate it up
3) Create Food
	random Coords Food block
	(Can use Snake Main Class to create new Food Class)
4) Detecting Food Collision
	Head Coords == Food Coords  
5) Detecting Wall Collison
	Head Coors ~ to Screen Width(x) /Height coordinate(y) 
6) Detecting Body Collision.
	Head Coords ~ Body Segment Coords.