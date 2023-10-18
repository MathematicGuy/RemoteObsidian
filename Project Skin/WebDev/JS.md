let -> assigned value that **can be reassigned**
const -> assigned value **cannot be reassigned** 
var -> assign value

Input
```js
const prompt = require("prompt-sync")();
const an_input = prompt("Enter a anything: ");
```

Condition
```js
isNaN(value); // check if value is a number
```

Extract Key Value pair from an Array
```js
for (const [symbol, count] of Object.entries(SYMBOL_COUNT)){}
```


##### splice(indexToRemove, numberToRemove)
The JavaScript `splice()` method is used to add or remove elements from an array. The method takes two parameters: `indexToRemove` and `numberToRemove`.
- `indexToRemove` specifies the index position of the first element to remove.
- `numberToRemove` specifies the number of elements to remove starting from the index position specified by `indexToRemove`.
Here’s an example:
```javascript
const arr = [1, 2, 3, 4, 5];
arr.splice(2, 2);
console.log(arr); // Output: [1, 2, 5]
```

In this example, we have an array `arr` with five elements. We call the `splice()` method on the array and pass two arguments: `2` and `2`. This means that we want to remove two elements starting from index position `2`. The resulting array will be `[1, 2, 5]`.

