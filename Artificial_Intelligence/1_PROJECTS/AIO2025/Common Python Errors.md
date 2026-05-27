**A. Common Errors**
1. **Zero Division Error (Lỗi chia cho 0 trong toán học)**
	**Defi:** Caused when a number divided by zero

2. **Name Error (Lỗi đặt sai tên)**
	**Defi:** Caused when unidentify variable get called. 
```python
a = b + 1 
print(a) # calculate a without define what value b is
``` 

3. **Syntax Error (Lỗi sai cú pháp, format code của ngôn ngữ)**
	**Defi:** Caused when we used incorrect python syntax format. e.g. using `' '` inside a `' '` or forget `;`  in javascript.
```js
console.log("Hello Word") // forgot semi-collon ;
```

4. **Type Error (Lỗi kiểu dữ liệu, Datatype Error)**
	**Defi:** Occur when we using wrong datatype type. e.g. sum of a number and  a string. 
```python
s = 'haha'
n = 4
sum = n + s # TypeError: can only concatenate str (not "int) to str 
```

5. **Indentation Error (Lỗi thụt lề)**
	**Defi:** Occur when any lines of code not in the right indent position. e.g. code inside function without indent.
```python
def sum(a, b):
return a + b # no indentation
```
   
6. **Module Not Found Error** (Lỗi gọi thư viện)
	**Defi:** ModuleNotFoundError occur when the language (i.e. python) cannot found a module (i.e. library) like numpy, pytorch, random, etc..
	**How to fix:** make sure all library correctly imported and downloaded to your python env. In some case, you add module path to your computer system environment path.
	![[Pasted image 20250105165823.png]]
 
7.  **Index Error** (Lỗi thứ tự)
	Often occur when you call a index out of list range. For instance, list nums have 5 number but you print nums value at index 6 `nums[6]`.
```python
nums = [1,2,3,4,5]
print(nums[6]) # IndexError: list index out of range
```

8. **Value Error** (Kiểu dữ liệu đúng nhưng phạm vi dữ liệu sai)
	Occur when a function or variable take in acceptable datatype but the value within that type is not valid for the operation. For instance `int()` expect a string represent a number like `'5'` but received `'abc'` :
```python
num = int('abc') # `ValueError: invalid literal for int() with base 10: 'abc'`
```

9. **Type Error**
	TypeError typically occur when you perform a operation on a data type that doesn't support it. e.g. `print('3' + 2)`
+ Or when you convert a unsupported value like 
```python
int('number') #  ValueError: could not convert string to float: 'number'
``` 
+ **Unpack TypeError  **: Occur when a **function return more values than we can retrieve**. For instance, math function return 3 values `a,b,c` while we only retrieve 2. 
```python
def math(a,b):
	sum_ab = a + b
	mul = a*b
	div = a/b
	
	return sum_ab, mul, div

# retrieve 2 values but return 3 values -> cannot unpack it all
sum_ab, mul = math(5, 6) # TypeError: too many values to unpack (expected 2)
``` 

10. **Recursion Error**
	Occur when your recursion is to deep or cannot stop, leading it surpass the recursion limit. Each time recursion function get called, a new *frame* added to program *stack*, when the *stack* overflow, RecursionError happend. 
```python
def a_func(n):
	return a_func(n) # no stop condition

a_func(5) # RecursionError: maximum recursion depth exceeded
```  

11. **AttributeError**
With every variable in python is a Object. AttributeError mean the object you attempt to access or assign an attribute (which can be a variable or a method of the Object).   
For example, calling mew() method with dog Class. 
```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()  # This works fine

try:
    my_dog.meow() # This will raise an AttributeError
except AttributeError as e:
    print(f"Caught an AttributeError: {e}")

# Example of NoneType error
my_cat = None
try:
    my_cat.sleep() #? Accessing a method that doesn't exist
except AttributeError as e:
    print(f"Caught an AttributeError for NoneType: {e}")
```


**B. Lý thuyết Assert**
**assert** basically **try-catch statement** but shorter, its **validate values by condition and return a message if the condition is False**. Assert often use to  **Customize Error Statement.**
```python
assert expression, message 
```
where 
+ **expression** is the condition.
+ **message**: notification if **condition** is False 
**Example:**
```python
x = 5
assert x==5, "The value is not 5"
print("hehe, value is 5")

>> Output: 'hehe, value is 5'
```

```python
x = 2
assert x==5, "The value is not 5"
print("hehe, value is 5")

>> AssertionError: 'The value is not 5'
```

---
# OOP Errors
### OOP Types Error -> Datatype is incorrect
+ ? Occurs due to incorrect method calls, attribute access or object instatiation. 

