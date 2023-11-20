**Create Object**
```js
// create new obj 
let anny = new Object();
anny.name = "Mary"; // set obj name
anny.isekai = new Object(); // create child obj
// set key var pair to child obj
anny.isekai.firstName = "Hack"; 
anny.isekai.lastName = "er";

console.log(anny["age"] = 13); // this also add "age: 13" to anny obj 
console.log(anny);
```
> 13
{
		  name: 'Mary',
		  isekai: { firstName: 'Hack', lastName: 'er' },
		  age: 13
	  }

**Better way to Create Object**
```js
// Better way: Obj literal
var facebook = {
    name: "Facebook",
    ceo: {
        firstName: "John",
        age: 16,
        favFood: "Apple Cream Pie"
    },
    "stock of company": 110,
};

console.log(facebook.ceo.favFood);
```

**Function are Object**
```js
let multiply = (x,y) => {
    return x + y;
}

multiply.version = "v.1.0.0";
console.log(multiply.version);

// function factory
let makeMultiplier = (multiplier) => {
    var myFunct = (x) => {
        return multiplier * x;
    };
    return myFunct;
}

// set multiplier value to 3. output [Function: myFunct]
var multiplyBy3 = makeMultiplier(3); 
console.log(multiplyBy3); 
// set x value to 10 & calc 3 * 10 = 30
console.log(multiplyBy3(10)); // output: 30

var doubleAll = makeMultiplier(2);
console.log(doubleAll(100)); // output: 200

// Passing functions as arguments
doOperationOn = (x, operation) => {
    return operation(x);
}

var result = doOperationOn(5, multiplyBy3);
console.log(result); // output: 15
result = doOperationOn(100, doubleAll);
console.log(result); // output: 200
```


#### **Passing Variables by Value vs by Reference**
> In Javascript, primitives are passed by value, objects are passed by reference.
> 	But "Under the hood", everything is actually passed by value
> 	![[Pasted image 20231120100956.png]]

**Passing Variables by Value (truyền theo giá trị)**
> passing/coping by value means changing copied value in b **does not affect value stored in a** and vice versa. 
![[Pasted image 20231120100003.png]]


**Pass by Reference (truyền theo tham chiếu)**
> passing/coping by value means changing copied value in b **does affect value stored in a** and vice versa.
![[Pasted image 20231120100206.png]]


![[Pasted image 20231120100337.png]]
> when we **update b = a**, what **really happening is b pointing to 0x003 (ô nhớ)** so the **direct value of b stay the same** 

**Summary**
+ Everytime there a new value, a new memory address is born -> Changing the new var won't affect the old var.
	Khi khai báo 1 giá trị, 1 ô nhớ mới sẽ đc sinh ra. 
```js
var x= 5; // tạo 1 giá trị x = 5 trong 1 ô nhớ mới
var y = a; // tạo 1 giá trị y = a = 5 trong 1 ô nhớ mới. Chú ý là b ko liên quan tới a
x = 10;
console.log(y); // y = 5, vì b chỉ copy giá trị của a và đc đặt trog ô nhớ mới.
```
+ **Primitives** are passed/coppied by value. var **a = 5**
+ **Object** are passed/copied by reference. var a : **{x: 5}**

**Function Constructor, prototype and 'this' keyword**
```js
// this refer to the current Obj
function Square(width) {
    this.width = width; // this width of the Obj
    // cannot return value

    this.getArea = 
    function(){
        return Math.pow(width, 2);
    };
}

// prototype must be put outside 
Square.prototype.DoubleWidth = 
    function () {
        return this.width * 2;
    }

var disSquare = new Square(5);
console.log(disSquare.getArea());
console.log(disSquare.DoubleWidth());
```

