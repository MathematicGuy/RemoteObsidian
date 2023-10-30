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
+ [[position relative]]
+ [[position absolute]]
**Summary**
+ Static positioning is default for all elements, except html
+ Relative positioning offsets the element relative to its normal document flow position
+ Absolute positioning is relative to closest ancestor which has positioning set to non-static value
+ Offsetting the relative container element offsets its contents as well