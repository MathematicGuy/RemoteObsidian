#### Color
![[Pasted image 20240124135629.png]]
+ text-color
```html
<p class="text-primary">.text-primary</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-success">.text-success</p>
<p class="text-danger">.text-danger</p>
<p class="text-warning">.text-warning</p>
<p class="text-info">.text-info</p>
<p class="text-light bg-dark">.text-light</p>
<p class="text-dark">.text-dark</p>
<p class="text-body">.text-body</p>
<p class="text-muted">.text-muted</p
<p class="text-white bg-dark">.text-white</p>
<p class="text-black-50">.text-black-50</p>
<p class="text-white-50 bg-dark">.text-white-50</p>
```


#### Background - Color
+ p : padding
+ mb : margin border
```html
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
<div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
<div class="p-3 mb-2 bg-warning text-dark">.bg-warning</div>
<div class="p-3 mb-2 bg-info text-white">.bg-info</div>
<div class="p-3 mb-2 bg-light text-dark">.bg-light</div>
<div class="p-3 mb-2 bg-dark text-white">.bg-dark</div>
<div class="p-3 mb-2 bg-white text-dark">.bg-white</div>
<div class="p-3 mb-2 bg-transparent text-dark">.bg-transparent</div>
```


### Button 
![[Pasted image 20240124141822.png]]
```html
<h2>Button Colors</h2>
<button class="btn btn-primary p-2 mb-2">My Btn</button>
<button class="btn text-dark btn-info p-2 mb-2">a</button>

<h2>Button Sizes</h2>
<button class="btn btn-lg btn-danger">Dangerous</button>
<button class="btn btn-md btn-primary p-2 mb-2">My Btn</button>

<h2>Button Outline</h2>
<button class="btn btn-md btn-outline-danger">Dangerous</button>
<button class="btn btn-outline-primary btn-lg">My Btn</button>

<!-- btn group -->
<p class="h2">Button Group</p>
<div class="btn-group">
  <a href="#" class="btn btn-primary">btn 1</a>
  <a href="#" class="btn btn-info">btn 2</a>
  <a href="#" class="btn btn-warning">btn 3</a>
  <a href="#" class="btn btn-danger">btn 4</a>
</div>
```


### Modify block
Margin - Border - Box-Shadow - Font-weight
![[Pasted image 20240124153754.png]]
```html
<!-- margin and padding -->
<h2>Inline Margin and Padding</h2>
<div class="bg-primary my-5 px-2">margin in y direction, padding in x direction</div>
<div class="bg-primary my-1 px-5">margin in y direction, padding in x direction</div>

<h2>Direction Margin and Padding</h2>
<div class="bg-primary mt-3 pb-5">margin top and padding bottom</div>
<div class="bg-primary pt-5 m-3">padding top and margin 3</div>
<div class="bg-primary m-2 ps-5 me-5">margin, padding start and margin end - 5</div>

<!-- borders -->
<div class="m-3 p-3 border border-info">default border</div>
<div class="m-3 p-3 border-primary border-top border-start border-end">border at start (left), top, end (right)</div>
<div class="m-3 p-3 border-start border-success border-5">Thick</div>
<div class="m-3 p-3 rounded border border-danger border-5">rounded</div>
<div class="m-3 p-3 rounded-pill border border-danger border-5">rounded</div>


<!-- box shadow -->
<div class="m-3 p-3 border shadow-md">rounded</div>


<!-- font-weight -->
<section class="m-4">
  <p class="fw-bold">Bold Text</p>
  <p class="fw-bolder ms-5">Bolder Text</p>
  <p>normaltext</p>
  <div class="fst-italic ms-5">italic text</div>
  <div class="fst-italic fw-light">italic text</div>    
</section>
```


### Container

fluid : make div responsive
max-width of 100% (responsive)
+ container-lg :  until it reached large
+ container-md: until it reached medium
```html
<div class="container my-5">
  <h1>normal container</h1>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur consectetur quod hic cumque voluptas, fuga ab ratione ipsa totam cupiditate sunt ipsam voluptate necessitatibus mollitia dolorem sequi exercitationem minus laboriosam?</p>
</div>

<div class="container-fluid my-5">
  <h1>normal container</h1>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur consectetur quod hic cumque voluptas, fuga ab ratione ipsa totam cupiditate sunt ipsam voluptate necessitatibus mollitia dolorem sequi exercitationem minus laboriosam?</p>
</div>


<div class="container-lg my-5">
  <h1>100% width util lg screen, then container</h1>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias laborum et vitae ducimus consequatur! Dolorum harum natus ipsum quaerat, recusandae enim minima quam exercitationem tempora fugit animi molestias culpa saepe!</p>
</div>


<div class="container-md my-5">
  <h1>100% width util lg screen, then container</h1>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias laborum et vitae ducimus consequatur! Dolorum harum natus ipsum quaerat, recusandae enim minima quam exercitationem tempora fugit animi molestias culpa saepe!</p>
</div>

```

### Grid

