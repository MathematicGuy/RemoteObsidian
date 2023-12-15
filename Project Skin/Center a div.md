### [11 way to center a div](https://blog.hubspot.com/website/center-div-css#center-div-css)

#### Center a div to the middle of the screen 
> The div center by it self
![[Pasted image 20231023142625.png]]
**html**
```html
<html>
	<head></head>
	<body>
		<div class="center-screen">
			I'm in the center
		</div>
	</body>
</html>
```
**css**
```css
.center-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
}
```

#### Center a div independently 
>center div horizontally -> margin: auto;

>center div vertically 
```css
position: absolute;
top: 50%;
transform: translate(0, -50%);
```

>Center a Div Horizontally and Vertically
```css
position: absolute;
left: 50%;
top: 50%;
transform: translate(-50%, -50%);
```
this can also be applied
```css
body{
    display: flex;
    justify-content: center;
}

main{
    position: absolute;
    top:50%;
    transform: translateY(-50%);
}
```

#### Center a Div Within a Div
note: 
+ set child div position to relative
+ push child div 50% at the top and right (or bottom and left) so it stay in the middle

```css
.parent{
    background: gray;
    height: 300px;
    width: 300px;
    position: relative;
}

div{
    background: orange;
    padding:50px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```
![[Pasted image 20231023141949.png]]



[Center using CSS Grid](https://youtube.com/shorts/oy2iUDT0mf8?si=XDf7fjJzQe0cYFVM)
![[Pasted image 20231215145517.png]]