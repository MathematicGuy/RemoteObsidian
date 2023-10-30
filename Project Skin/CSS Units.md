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
