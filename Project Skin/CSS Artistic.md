[CSS Button Design](https://stacksorted.com/buttons)

[CSS Animation](https://www.youtube.com/watch?v=SgmNxE9lWcY)
	[Arrow Animation ](https://youtu.be/UTHgr6NLeEw?si=wEEHs0pSssOHk-R1&t=192)
	![[Pasted image 20231024113201.png]]


[CSS Shadow](https://getcssscan.com/css-box-shadow-examples) 

[Font Awesome Icon](https://www.w3schools.com/icons/fontawesome_icons_directional.asp)
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

li no bullet
```css
list-style: none;
```

ease:
ease-in
ease-out
ease-in-out
```css
@keyframes slideInLeft {
    0%{
        transform: translateY(-200px);
    }
    90%{
        transform: translateY(7px);        
    }
    100%{
        transform: translateY(0px);        
    }   
}

.img-container{
    /* animation-name: slideInLeft;
    animation-duration: 1.5s; 
    animation-timing-function: ease-in-out;
    animation-delay: 0s;
    animation-iteration-count:  1;
    animation-direction: normal;
    animation-fill-mode: none; */
    
    animation: slideInLeft 2.2s ease-in-out both;
}
```




