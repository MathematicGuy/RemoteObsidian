
### Python Good Habit
> This will improve your coding readbility and performance.

+ ! Never thing your code is too obsivous, because there always people who misunderstand how your code work

1) **use `__name__ == '__main__'` for Module** 
	Let test out to see why !

module.py
```python
def connect():
    print('Connecting...')
    time.sleep(1)
    print('You are Connected!')

if __name__ == '__main__':
	connect()
    print('This is the main module')
```

main.py
```python
from module import connect # import connect function
from module import calc # import connect function

connect()
```
Output if not using `__name__ == '__main__'`![[Pasted image 20240601230835.png]]This is because all of the file was readed when module is imported in main.py. 
> When we use `__name__ == '__main__'`  the connect function only run if module.py was run and not being run by imported in other file (e.g. main).  

note: "entry point" where everything access through it (e.g. ngã tư, ngã ba, etc..)
Have **main() as Module entry point** (more readablity)
```python
def main() -> None:
    connect()
    calc(2, 4.4)
    
if __name__ == '__main__':
	main()
```


2) **Use Notation** (for big project)
```python
def calc(x:int, y:float) -> float: # this does not change the function. It just show as notation
    if type(y) != float: # warn the user if y not float
        return "y must be float"
    return x + y
```
Other can inspect your function notation (by overing over the function)   
![[Pasted image 20240601230122.png]]
Function without notation will look like this
![[Pasted image 20240601230235.png]]

`map(function, iterable)`: **appiles function** to **every item of iterable**
```python
def plus(num):
    if num % 2 == 1: # not divided by 2
        return num 
    else:
        return 'Nah'
    
x = [1, 2, 3, 4, 4]
y = list(map(plus, x)) # output: [1, 3]
print(y)
```
the same as
```python
y = [y = [plus(i) for i in x]  # output: [1, 3]]
```

---

#### Get path as a List 
+ If the list was empty
```python
list(path.glob('*'))
```
> `[ ]`
```python
list(path.iterdir())
```
> Traceback (most recent call last):
> [...]
> FileNotFoundError: [Errno 2] No such file or directory:

**glob()** takes a pattern as an argument. This patterns include wild card like `*`, `?`, `[]` to match file name:
- `*` matches any number of characters (including none).
- `?` matches any single character.
- `[]` matches any single character specified within the brackets.

**cv.imshow()**
	+ `imshow()` often interpret image data from `[0, 255]` as representing the intensity of RGB color channels. 
	+ `uint8` represents integers in the range `[0, 255]`
	-> Convert image datatype to `unit8`: `.astype('unit8)` to display image with `imshow()`

