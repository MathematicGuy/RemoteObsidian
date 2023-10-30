# Week 1 
note: (become link when completed)

## CSS Basics
+ ### [[Class Selector]]


## CSS Rules Conflict Resolution and Text Styling 

### Conflict Resolution
>Last Declaration Wins (If there 2 CSS style affect 1 element) in other word The Last overwritten the Previous.

**DOM Tree**
> **Inheritance** (sub-element inheritance)
body
	element
		element
		element
	element
	element

**Score for Priority tag** 
	(Tag with higher score can overwrite)
	Even it get specify later.
![[Pasted image 20231030083335.png]]
	Example:
		specify **id after div** can **overwrite class with 2 element after div**
	![[Pasted image 20231030083701.png]]

### Styling Text
2em -> 2 times the current font size
.5em -> 1/2 time the current font size

[**CSS Units**]([CSS Units (w3schools.com)](https://www.w3schools.com/cssref/css_units.php))
*relative: tương đương*
*viewport: kích thước màn hình của thiết*
*kt: kích thước

ex -> Relative to the x-height of the current font (rarely used) 
ch -> Relative to the width of the "0" (zero)
rem -> Relative to font-size of the root element

**Font auto adjust to screen size**
vw (v-width) -> Relative to 1% of the width of the viewport*
vh (v-height) -> Relative to 1% of the height of the viewport*
**vmin** -> Relative to 1% of viewport's* smaller dimension **(chỉ giảm, ko tăng)**
	+ **Kt chữ chỉ giảm với độ dài max/default là vmin**
	Ex: Kt lớn nhất là 15vmin, khi màn hình càng bé, kích cỡ chữ càng giảm.
**vmax** -> Relative to 1% of viewport's* larger dimension **(chỉ tăng, ko giảm)**
	 **Ngược lại với vmin.**
	Ex: Kt bé nhất là 15vmax, khi màn hình càng lớn kích cỡ chữ càng tăng.
% -> Relative to the parent element 

### CSS Box Model and Layout

#### Box Model
[[Box-sizing]] (not inherited)
+ [CSS Box Sizing](https://www.w3schools.com/css/css3_box-sizing.asp)

> Cumulative Margins
> + If there're 2 Boxes adjacent to eachother top to bottom. Only the bigger margin will be valid.
> + This does not happen on left and right margins! Only top and bottom margins !
![[Pasted image 20231030100828.png]]

There case that text overflow, we can use [overflow attributes]([CSS Overflow (w3schools.com)](https://www.w3schools.com/css/css_overflow.asp)).
![[Pasted image 20231030101552.png]]
- `visible` - Default. The overflow is not clipped. The content renders outside the element's box
- `hidden` - The overflow is clipped, and the rest of the content will be invisible
![[Pasted image 20231030101742.png]]
- `scroll` - The overflow is clipped, and a scrollbar is added to see the rest of the content
![[Pasted image 20231030101750.png]]
- `auto` - Similar to `scroll`, but it adds scrollbars only when necessary
![[Pasted image 20231030101801.png]]