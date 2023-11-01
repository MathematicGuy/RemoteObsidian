
![[Pasted image 20231101102755.png]]
**Design Ideology**
![[Pasted image 20231101102822.png]]
+ Site's layout adapts to the size of the device
+ Content verbosity or its visual delivery may change
	Design can be different on various devices.
	All device *can be or can not be* display the same. (Yes, it's like re-design with what you have)


**12-Column Grid Reponsive Layout**
+ Assigned Boxes with the right proportion to make a balance & responsive layout. 
+ **Manipulate Box size with class name.**
+ Re-size Boxes with CSS Media Query
> 1 column = 100% / 12 = 8.33%
![[Pasted image 20231101105506.png]]
> Using this we can achieve balance between Boxes
> e.g. 3 column as: 25%, 6 as 50% and 4 as 33%
> The leftover percent become the margin of the box (Perfectly calculated)
![[Pasted image 20231101105834.png]]
How to use this?
> we assigned class name for each box we desired e.g. col-lg-3 as 3 columns for large device, col-md-6 as 6 columns for medium device
```html
<div class="col-lg-3 col-md-6"> 
	  <p>Item1</p>
</div>
```
> Then we applied the 12-Column Grid % rules. Now we can modify how much a box take using class name for screen width at x(px)  
> note: -lg and -md are to manipulate boxes at large/medium screen distinctively.
```css
/* Large device only */
@media (min-width: 1200px){
    .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6,
      .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12{
        float: left;
        border: 1px solid green;
    }
	
    /* Calculate the percentage for each column */
    .col-lg-1 { width: 8.33%; }
    .col-lg-2 { width: 16.66%; }
    .col-lg-3 { width: 25%; }
    .col-lg-4 { width: 33.33%; }
    .col-lg-5 { width: 41.66%; }
    .col-lg-6 { width: 50%; }
    .col-lg-7 { width: 58.33%; }
    .col-lg-8 { width: 66.66%; }
    .col-lg-9 { width: 75%; }
    .col-lg-10 { width: 83.33%; }
    .col-lg-11 { width: 91.66%; }
    .col-lg-12 { width: 100%; }
}

/* Medium device only */
@media (min-width: 750px){ 
    .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6,
      .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12{
        float: left;
        border: 1px solid green;
    }
	
    /* Calculate the percentage for each column */
    .col-md-1 { width: 8.33%; }
    .col-md-2 { width: 16.66%; }
    .col-md-3 { width: 25%; }
    .col-md-4 { width: 33.33%; }
    .col-md-5 { width: 41.66%; }
    .col-md-6 { width: 50%; }
    .col-md-7 { width: 58.33%; }
    .col-md-8 { width: 66.66%; }
    .col-md-9 { width: 75%; }
    .col-md-10 { width: 83.33%; }
    .col-md-11 { width: 91.66%; }
    .col-md-12 { width: 100%; }
}
```

<meta name="viewport" content="width=device-width, initial-scale=1.0">
	make web site response to device viewport (eg. phone, tablet, ipad) not just 1 static viewport.
![[Pasted image 20231101120140.png]]

**SUMMARY**
+ Need and idea of responsive design
+ 12-column grid layout
	+ Use % to achieve fluid width (wrt browser width)
+ Viewport meta tag to turn off default mobile zooming 
	+ (Remain this layout even if the screen are smaller)
	![[Pasted image 20231101120459.png]]
