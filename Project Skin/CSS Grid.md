> Flexbox vs Grid
![[Pasted image 20231020164755.png]]

![[Pasted image 20231021105449.png]]
>right-column: 200px and left is 200px


fr - fraction
px - pixel

grid-gap: gap-size 
	grid-column-gap
	grid-row-gap


> Allow box spanning manipulation
grid-column: span 2; // take up 2 column space
grid-row: span 3;  // take up 3 column space
```css
display: grid;
grid-template-columns: 200px 250px;
grid-auto-rows: minmax(150px, auto);
grid-gap:10px;
    
.item1{
    /* grid-area: header; */
    grid-column: span 3;
}
.item2{
    /* grid-area: menu; */
    grid-row: span 2;
}
.item3{
    /* grid-area: main; */
}
.item4{
    /* grid-area: right; */
}
.item5{
    /* grid-area: footer; */
    grid-column:span 2;
}
```
![[Pasted image 20231021133710.png]]


**grid-template-areas** (move box using abstract method)
```css
.grid-container{
	display: grid;
	grid-template-columns: 200px 250px;
	grid-auto-rows: minmax(150px, auto);
	grid-gap:10px;
    
	grid-template-areas:
	"header header header"
	"menu main right";  
}

.item1{
    grid-area: header; 
}
.item2{
	grid-area: menu; 
}
.item3{
	grid-area: main; 
}
.item4{
	grid-area: right;
}
.item5{
    grid-area: footer;
}
```
![[Pasted image 20231021145242.png]]
make the structure to be more accurate
```css
grid-template-areas:
'header header header header header'
'menu main main right right'
'menu footer footer footer footer';
```
