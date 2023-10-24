#### Animation
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

