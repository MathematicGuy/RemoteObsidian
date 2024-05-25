![[Pasted image 20231026214601.png]]


Data Types
![[Pasted image 20231026220353.png]]

Common Strings method 
![[Pasted image 20231026220506.png]] 

**Array**
```js
let fruits = ['banana', 'apple', 'orange', 'pineapple'];
fruits = new Array('banana', 'apple', 'orange', 'pineapple');

// Split by comma & a space. literally split string that follow rule inside this ('')
let strArray = fruits.toString().split(', '); 

console.log(fruits.toString()); // turn Array to only string. no []
console.log(fruits.join('-')); // join each string in list with *
console.log(fruits.pop(), fruits); // pop() remove the last element from array
console.log(fruits.push('*')); // append element to array
console.log(fruits[fruits.length - 1] = "Kiwi",">>", fruits); // same as push
console.log(strArray, "remove first element:", fruits.shift(), fruits); //remove the first item from array
console.log(strArray, "add to first element:", fruits.unshift("strawberry"), fruits); //remove the first item from array

let Groceries = fruits.concat(fruits);
console.log("Groceries =", Groceries);
console.log("Groceries =", Groceries.slice(0, 4)); // slice 4 elements (0 1,2,3) from Groceries 
console.log("Groceries =", Groceries.reverse()); // reverse Array

let someNumber = [1,5,10,20,32,22,24,55,2,4];
console.log(someNumber.sort((a,b) => {return a-b})); // increase sort 
console.log(someNumber.sort((a,b) => {return b-a})); // decrease sort

let  emptyArray = new Array();
for (let i = 0; i <= 10; i++){
    emptyArray.push(i);
}
console.log(emptyArray);
```

Object (Dictionary in Python)
```js
// Object in JavaScript
// Dictionary in Python

let student = {
    "first":"Dinh",
     last:"Thanh",
    age:25,
};
console.log(student["first"]);
console.log(student.last);
student.age++;
console.log(student.age  );
```

```js
switch(0){
	case 0:
		// do sth
		break;
	case 1:
		// do sth
		break;
	default:
		// do sth
}
```


