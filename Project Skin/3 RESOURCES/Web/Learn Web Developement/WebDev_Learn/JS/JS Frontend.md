**JS HTML**
	[[3 RESOURCES/Web/FrontEnd/FrontEnd]]

+ **Concept**
	HTML DOM (Document Object Model)
		When a web page is loaded, the browser creates a **D**ocument **O**bject **M**odel of the page.


**Knowledge**
document -> connect to HTML document
.getElementbyId("id") -> get ID of an Element/Tag
.querySelector("class") -> select a class in HTML. Access method similiar to CSS. 
	Ex1: class="container" -> ("container")
	Ex2: class="container part2" -> (".part2")
-> by this we can set an HTML element as an JS Element
```js
const btn = document.getElementById("btn");
const panel = document.getElementById("panel");
const color = document.querySelector(".color");

// catch mouse click event & do sth
btn.addEventListener("click", () => {
	// code
});
```

code run after DOM all loaded
```js
window.addEventListener("DOMContentLoaded", () => {
	// code run after JS File all loaded
});
```

[replace class name](https://stackoverflow.com/questions/195951/how-can-i-change-an-elements-class-with-javascript)
```javascript
document.getElementById("MyElement").className = "MyClass";
```

[CSS hover effect in JS](https://stackoverflow.com/questions/8318591/javascript-addeventlistener-using-to-create-a-mouseover-effect)

[Change HTML Element's class in JS](https://stackoverflow.com/questions/195951/how-can-i-change-an-elements-class-with-javascript) 

## jQuery
+ JS library
