#### Positioning Elements by Floating (use for article positioning)
[float](https://www.w3schools.com/Css/css_float.asp) & [clear](https://www.w3schools.com/Css/css_float_clear.asp)
+ The float property is used for positioning and formatting content e.g. let an image float left to the text in a container. 
	+ The margin never collapse
+ **clear: left/right/both;** -> nothing on its left/ right/ left & right
**Summary**
+ Floating elements can produce very flexible layouts
+ Floats are taken out of normal document flow
+ Floats don't have vertical margin collapse
+ To resume normal document flow, use the **clear** property
> *When clearing floats, you should match the clear to the float: If an element is floated to the left, then you should clear to the left. Your floated element will continue to float, but the cleared element will appear below it on the web page.*

#### Relative and Absolute Element Positioning
+ [[position relative]]
	+ Set current Position as Original position.  
+ [[position absolute]]
	+ Offset element from all un-relative container.
	+ Absolute position element cannot stay inside position relative element. 

**Summary**
+ Static positioning is default for all elements, except html
+ Relative positioning offsets the element relative to its normal document flow position
+ Absolute positioning is relative to closest ancestor which has positioning set to non-static value
+ Offsetting the relative container element offsets its contents as well


