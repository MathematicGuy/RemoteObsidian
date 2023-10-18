In JavaScript, `for...of` and `for...in` are two different types of loops that can be used to iterate over arrays and objects, respectively.

`for...of` is used to iterate over the values in an array. It assigns each value in the array to a variable declared in the loop header. Here’s an example:

```javascript
const arr = [1, 2, 3];

for (const num of arr) {
  console.log(num);
}
```

This will output:
```
1
2
3
```

`for...in`, on the other hand, is used to iterate over the properties of an object. It assigns each property name to a variable declared in the loop header. Here’s an example:

```javascript
const obj = { a: 1, b: 2, c: 3 };

for (const prop in obj) {
  console.log(prop);
}
```

This will output:
```
a
b
c
```

It’s important to note that `for...in` iterates over all enumerable properties of an object, including properties inherited from its prototype chain. If you only want to iterate over an object’s own properties, you can use `Object.keys()` or `Object.getOwnPropertyNames()` to get an array of property names and then iterate over that array using `for...of`.
