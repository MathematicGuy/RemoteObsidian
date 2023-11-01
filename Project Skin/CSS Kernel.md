# Week 1 
note: (become link when completed)

## CSS Basics
+ [[Tag and Class]]
+ [[Class Selector]] 



## CSS Rules Conflict Resolution and Text Styling 

+ ### Conflict Resolution
	+ [[DOM Tree & Score for Priority tag]] 

+ ### Styling Text
	+ [[CSS Units]]
	UTF-7 cannot express all type of text so we use UTF-8 



## CSS Box Model and Layout

### Box Model
+ [[Box-sizing]] (not inherited)
	+ [CSS Box Sizing](https://www.w3schools.com/css/css3_box-sizing.asp)
+ [[Cumulative Margin and Overflow]] (have margin collapse)

### Styling
+ background: url() no-repeat cross-axis main-axis color; 
+ [[Element Positioning]] 



## Introduction to Responsive Design

### Media Query 
note: 1px between 767px to 768px called the "breakpoint".
![[Pasted image 20231030233246.png]]
+ [[Reponsive Design]]



## [Introduction to Twitter Bootstrap](https://getbootstrap.com/docs/5.3/layout/grid/#example)
> Do the **12-Column Grid Reponsive Layout** in CSS automatically for me

**Intro to Twitter Bootstrap** (apparently most popular PJ in github)
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