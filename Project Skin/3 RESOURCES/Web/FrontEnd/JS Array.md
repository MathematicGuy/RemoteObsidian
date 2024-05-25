## Array

Method 1: manualing
```js
// Create Array
var array = new Array();
// Add value to Array 
array[0] = "Ussopp";
```

Method 2: Shorthand 
```js
// Create Array
var names = ["luffy", "nami", "zoro", "sanji", "robin", "chopper", "brook", "franky", "jinbe"];
// loop through array
for (var i = 0; i < names.length; i++){
    console.log(names[i]);
}

// create Object
var StrawHatPirate = {
    members: names,
    ship: "going marry and sea lion",
    status: "Sea Emperor",
    bounty: "13.000.000.000 BL",
};

//? add property to Object 
StrawHatPirate.relationships = "Lmao Lmao"; 

for (var prop in StrawHatPirate){
    //? access Object like Python
    console.log(prop + ":" + StrawHatPirate[prop]); 
} 
```