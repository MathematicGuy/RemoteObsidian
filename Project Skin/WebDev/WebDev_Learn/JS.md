[[Frontend]]

**Value**
declare value:
	+ const
	+ let
value  
	" " + 2 -> "2"



**function**
let a_function = (parameter) => {
	// code
}


**java front end**
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


