> Special Function & Like Function
> What the point:
> 	Made to be pass to a Higher order function.
> 	(Meanning taking other funcs as output and input) 
```python
def my_map(my_func, my_iter):
	result = []
	for item in my_iter:
		new_item = my_func(item)
		result.append(new_item)
	return(result)

nums = [2,4,5,73,7,9]

# Traditional function usages
def to_cube(x):
	return x**3
cubed_trad = my_map(to_cube(num), nums)

# Lambda for clean code
cubed_lambda = mymap(lambda x: x**3, nums)

print(cubed_lambda)
```

> **Simple Example**
```python
def add(x,y):
	return x+y
print(add(4,5))

lambda x,y : x + y
```

