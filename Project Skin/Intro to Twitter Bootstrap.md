(apparently most popular PJ in github)
+ mobile first
	+ Make you to think and force you to compress only what is important to ur website.
	+ Advantage
		+ Plan mobile fro the start
		+ CSS is mobile ready
	+ Disadvantage
		+ Too big, too bloated
			A lot of features you will probably never use
			+ Use selective download
		+ You can write your own that's more targeted/smaller
			+ Take longer time


![[Pasted image 20231101123048.png]]
+ script.js and style.css below for overwritting what bootstrap give us 
+ bootstrap depend on jquery library so it must import later

**Bootstrap Grid System Basics**
![[Pasted image 20231101124048.png]]

+ Structure Bootstrap expects for the grid-based layout
	• Needs to be include -container (or .container-fluid)
	• All columns must be inside .row
	![[Pasted image 20231101211509.png]]
+ SIZE identifier identifies at which breakpoint specified column spans will be ignored and all elements will collapse (i.e., stack)
+ If no other rules apply, specifying col-xs-... will keep that layout no matter what the size of the screen.

Homework: Make a website with Boostrap