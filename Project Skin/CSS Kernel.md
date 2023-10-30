# Week 1 
note: (become link when completed)

## CSS Basics
+ [[Tag and Class]]
+ ### [[Class Selector]] 
	(organize later)

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
+ [[Cumulative Margin and Overflow]]


### Styling

#### Background
background: url() no-repeat cross-axis main-axis color;
	bg repeat by default

#### Positioning Elements by Floating
**float** & **clear** tag
	+ The margin never collapse
	+ **clear: left/right/both;** -> nothing on its left/ right/ left & right
Box with not enough space get push down.
**Summary**
+ Floating elements can produce very flexible layouts
+ Floats are taken out of normal document flow
+ Floats don't have vertical margin collapse
+ To resume normal document flow, use the **clear** property

#### Relative and Absolute Element Positioning
**position: relative;**
	make the next re-position relate to it current position or base on it current position.
		Make current boxes ancher to its current position
-> When we set position to be relative, we've set an anchor.
Example: **moving element 50px from top left.** 
![[Pasted image 20231030152914.png]]

> All offsets (top, bottom, left, right) are relative to the position of the nearest ancestor which has positioning set on it, other than static.
+ Meaning: offsets (top, bottom, left, right) relative to its last re-position.

**position: absolute ;**
	if a container offset all the container within it offset either.
![[Pasted image 20231030161136.png]]
