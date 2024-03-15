what is a Scope
+ 'data = { } is a scope'
```js
data = { "I'm inside a Scope" }
console.log("I'm outside data's Scope")
```
> Everything within { } of sth is inside the Scope and outside it in reverse. 

```js
var url = `https://catfact.ninja/breeds?limit=1`;
fetch(url)
	// if not correct throw error else
	.then(res => {
		 if (!res.ok) {
			  throw new Error('Network response was not ok');
		 }
		 return res.json();
	})
	
	.then(data => { 
		// Everything within data {} can be access in here  
		 console.log(data);
		 console.log('\nThis is COOL: ', data.current_page);
	}) 
	// 
```


1.641

1.7777777778