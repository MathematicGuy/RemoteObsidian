**JavaScript Code Analysis**

**A variable must have 1 of these**
	**let** -> assigned value that **can be reassigned** (Value can be change)
	**const** -> assigned value **cannot be reassigned** (Only take Value Once)
	**var** -> assign value

Input using Node.js
```js
const prompt = require("prompt-sync")();
const an_input = prompt("Enter a anything: ");
```

Check if isNotANumber
```js
isNaN(value); 
```

Extract Key Value pair from an Array
```js
for (const [symbol, count] of Object.entries(SYMBOL_COUNT)){}
```

Function
```js
let function = ("parameters") = {"do sth"};
```

JS_Array
```js
anArray.push("Sth") // append to an Array in js
```

splice(a,b) -> *Delete b Element starting from index a*
```javascript
const arr = [1, 2, 3, 4, 5];
arr.splice(2, 3);
console.log(arr); // Output: [1, 2, 5]
```
 `splice()` method  pass two arguments: `2` and `3`. This means that we want to REMOVE `3` ELEMENTS starting FROM INDEX POSITION `2`. The resulting array will be `[1, 2]`.

String format
```js
const name = "Jenny";
const id = 1;
console.log (`Welcome ${name}, your ID is ${id}`);
```


#### [[for of vs for in]] 
> Giá trị của v/s Giá trị trong
> of -> List, Array
> in -> Dictionary
```js
for (const row of rows) {} -> output the key value from sth ("work with list")
for (const row in rows) {} -> output the value of a key ("work with arr, dict")
```







