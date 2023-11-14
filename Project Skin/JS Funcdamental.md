### JS Basics
define var
- let
- vat

function
```js
let a = () => {...};
// or
function a () {...};
// or
a();
// example
let comapre = (x,y) => {...};
compare(4, "a");
// this is legal
compare() 
```

**Scope**
+ Global 
	Define here and available everyewhere
- Function
	Define here and available only within this function
**Scope Chain**
+ Everything is executed in an Execution Context
+ Function invocation creates a new Execution Context
+ Each Execution Context has:
	• Its own Variable Environment
	• Special 'this' object (*explain later*)
	• Reference to its Outer Environment
+ Global scope does not have an Outer Environment as it's the most outer there is
> Function first execute within the current scope. If not found
> 	Search it reference Outer Scope. If not found
> 		The Outer Scope of this Outer Scope will be search.
> 			Repeat until go to the Global scope. If still not found
> 				var undefined
Example: 
![[Pasted image 20231114132026.png]]
> Basically var x = 5 is called first, then var x = 2 is called later thus chagin x = 5 to x = 2. Hence why x = 2 in the console. 

**Detail Example**

> B() scan within itself but find no a. So B() scan outside and found a from Global scope. Therefor a = "Global Scope"
```js
var a = "Global scope";
console.log("global: message = " + a);

let A = () => {
  var a = "Inner Scope";
  console.log("a: message = " + a);

  B();
}

let B = () => {
    console.log("b: message = " + a);
}

A();
```
> global: message = Global scope
a: message = Inner Scope
b: message = Global scope

> > B() scan within itself but find no a, so B() goes outside it scope and found a in its reference Outer Scope which is A(). There for a = "Inner Scope"
```js
var a = "Global scope";
console.log("global: message = " + a);

let A = () => {
  var a = "Inner Scope";
  console.log("a: message = " + a);
  
  let B = () => {
    console.log("b: message = " + a);
  }

  B();
}

A();
```
> global: message = Global scope
a: message = Inner Scope
b: message = Inner Scope

**Summary**
+ Defining variables — dynamically typed
+ Defining functions — creates its own scope (lexical)
+ JS code runs within an Execution Context
+ Scope chain is used to retrieve variables from Outer Variable Environments
