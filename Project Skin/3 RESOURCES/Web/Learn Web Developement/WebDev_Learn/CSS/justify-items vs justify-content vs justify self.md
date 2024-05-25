**Conclusion:** 
+ Explaination-1:  justify-item directly modify the items while justify-content modify the item position.
+ Explaination-2: if there 1 box containt 5 items, 
	using **justify-items: flex-end *=would equal to using=*  justify-self: flex-end for each items**. Since both of them will modify the items base on the items Axis, not the Container Axis like justify-content.    

Original
![[Screenshot 2023-10-21 140928.png]]
Struture: 5 items inside a container
	container > 5 * items 

**Justify-Items**
> Justify THE ITEMS base on the ITEMS AXIS
```css
justify-items:flex-start;
```
![[Pasted image 20231021140344 1.png]]
```css
justify-items:flex-end;
```
![[Pasted image 20231021140722.png]]


**justify-content:** 
> Justify the THE POTISION OF ITEMS base on CURRENT BOX AXIS  
```css
justify-content:space-between;
```
![[between.png]]

```css
justify-content:space-around;
```
![[around.png]]

```css
justify-itemcontents:space-evenly;
```
![[evenly.png]]


**justify-self**
> justify it-self. Modify itself on it own Axis


