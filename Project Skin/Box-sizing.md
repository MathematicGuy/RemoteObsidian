set `box-sizing: border-box;` on an element, **padding and border are included in the width and height**:
```css
box-sizing: border-box
```

**None** (included width and height)
>**total_width = padding + border + width
>total_height = padding + border + height**
+ **everything** are **included with the width and height**
Example:  (1 + 20) x 2 + 300 = 342px of total width
![[Pasted image 20231026100033.png]]

**Border-box** (note that calc both side of the box) (Is width & height)
> **width side = padding + border**
> **height side = padding + border** 
+ **padding and border** are **included in the width and height**
Example:  (1 + 20) x 2 + 258 = 300px of total width
![[Pasted image 20231026100004.png]]




