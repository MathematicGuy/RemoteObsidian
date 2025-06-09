
### Road Map for Learning Data Science 
Nguyễn Thái Hà - Ph.D
![[Pasted image 20250609165200.png]]
**Project in this Module** 
![[Pasted image 20250609165225.png]]
**Excel is very important (even nowaday)** for Data Analysis. 
**Databricks** - an organized platform for Data Analysis and Data Engineer working together. (platform tiềm năng)
Explainable AI -> Debug for Model, Identify the True Flaws (e.g. sometime its the Model fault, not your solution fault)

### Today Learning Objectives
+ Understand Clean Code and PEP-8 in python coding principle. 
+ Building "Pythonic" Thinking
+ Apply some of programming principles for better coding (DRY, KISS, YADNI)
+ Learn how to structure your source code (SOLID rule for Senior), Design Patterns. 

----
### Clean Code and PEP-8
#### Clean Code (TREM)
T - Testable 
R - Readable
E - Extensable 
M - Maintainable
+ ? You don't have to be CLEAN right away, 5%, 10% cleaner everydays is enough.

**When to skip Clean Code:** 
+ Small Testing Code
+ Temporary Code
+ Code to debug 

#### PEP-8 Rule (Python Enhancement Proposal)
**Clean Code:** better **codes that are easy to understand at the first glance** (Readable), easier to modify (Maintainable), easy for testing (Testable) and easy to expand and upgrade (Extensible). 
Note: tool for checking PEP-8 -> flake8
![[Pasted image 20250609171526.png]]
+ ? Strive for Consistent and Unified code with comment.

**Naming Convention:** snake_case, PascalCase, UPPER_CASE. 


**PEP-8** Basically a proposal for Python standard coding style, **so your code has the right look for anyone else reading or modifying it.** 
+ Indent 4 Space
+ Single space between items
+ Space after Comma/Colon
+ **Consistent Quote Mark,** single-quote `'` or double-quote `"`. Recommend `'` before `"`
+ DO NOT WRITE `if var == TRUE:` in a in/while test but `if var:` 
```python

def print_greeting(words, shout_mode):
    if shout_mode:           # YES like this
        print(words.upper())
    else
        print(words)

# To invert the logic do not use == False. Use not like this:

def print_greeting(words, shout_mode):
    if not shout_mode:
        print('Not shouting')
    else
        print(words)
```
+ *add* Inline *Comments*
+ **Do not use Python Keywords as function name:** some *built in function* so you *cannot name your function like python*.
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
+ ! DO NOT use Builtin Function as Variable Name. Such as `len abs min max int float list str dict range map filter format`
```python
>>> len('hello')   # len function works
5
>>> len = 7        # redefine "len" to be 7, bad idea
>>> len('hello')   # oh noes!
TypeError: 'int' object is not callable
```

**Open-Closed Principle**: Update the code without changing the original function. 
*Unexpandable Code* -> Have to modify the original function for changes.
```python
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'substract':
        return a - b
    elif operation == 'multiply':
        return a * b
    else:
        raise ValueError("Invalid operation")
```

*Expandable Code* -> Have to modify the original function for changes.
```python
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = {
    'add': add,
    'substract': substract,
    'multiply': multiply,
}

def calculation(a, b, operation):
    func = operations.get(operation)
    if func:
        return func(a, b)
    else:
        raise ValueError("Invalid operation")
```
- You can **extend** the dictionary with new operations (e.g., `'divide': divide`) **without changing existing code**.
    
- Existing logic in `calculation()` stays untouched.

| Principle        | Open-Closed (OCP)                                            |
| ---------------- | ------------------------------------------------------------ |
| **Bad Code**     | Hardcoded logic, requires editing function for new features  |
| **Good Code**    | Uses **functions as values** in a dictionary, easy to extend |
| **Real Benefit** | Scales better and avoids breaking old code                   |

### Pythonic Code
**What is PYTHONIC?** writing Python in way that is both readable and efficient. Simple and Efficient Code.  
#### Permutation
**Bad**
```python
temp = a
a = b
b = temp
```
**Pythonic**
```python
a, b = b, a # replace a at position b, replace b at position a 
```

#### List
**Bad**
```python
my_list = []
for i in range(10):
	my_list.append(i * 2)
```
**Pythonic**
```python
my_list = [i*2 for i in range(10)]
```

#### Check Empty List 
**Bad**
```python
a = []
if a is []: print('a')

if len(a) == 0: print('a')
```
**Pythonic**
```python
a = []
if not a: print('a')
```

#### Traverse Indexed Array 
**Bad**
```python
for i in range(len(my_list)):
    print(i, "-->", my_list[i])
```
**Pythonic**
```python
for key, value in enumerate(my_list):
    print(key, "-->", value)
```

#### Unpacking
**Pythonic**
```python
a, *rest = [1, 2, 3, 4, 5, 6, 7, 8]
print(*rest) # 2, 3, 4, 5, 6, 7, 8

a, *middle, b = [1, 2, 3, 4, 5, 6, 7, 8]
print(*middle) # 2, 3, 4, 5, 6, 7 
```

#### Join elements inside a Array
**Bad**
```python
letters = ['s', 'p', 'a', 'm']

s = ""
for i in letters:
	s += i # add chars 1 by 1
```
**Pythonic**
```python
letters = ['s', 'p', 'a', 'm']
word = ''.join(letters) # join all seperated letter all at once  
```

#### Checking Condition
**Bad**
```python
if attr == True:
    print 'True!'

if attr == None:
    print 'attr is None!'
```
**Pythonic**
```python
if attr:
	print 'attr is True'

if not attr:
	print 'attr is False'

if attr is None:
	print 'attr is True'
```

#### Array Actions
**Bad**
```python
a = [3, 4, 5]
b = []
for i in a:
    if i > 4:
        b.append(i)
```
**Pythonic**
```python
a = [3, 4, 5]
b = [i for i in a if i > 4]
# Or
b_lambda = filter(lambda x:x > 4, a) #? `filter()` will remove elements that evaluate to `False` in a boolean context (e.g., `0`, `None`, empty strings, empty lists). However this doesn't return a list
print(list(b_lambda))
```

**Bad**
```python
a = [3, 4, 5]
for i in range(len(a)):
    a[i] += 3
```
**Pythonic**
```python
a = [3, 4, 5]
a = [i + 3 for i in a]
# Or
a_lambda = map(lambda x:x + 3, a)
print(list(a_lambda))
```

#### Reverse List
**Bad**
```python
a = [3, 4, 5]
b = []
for num in reversed(a):
	b.append(num)
print(b)
```
**Pythonic**
```python
a = [3, 4, 5]
print(a[::-1])
```

**Prefix** under string (`_variable`) -> Indicate Private attribute, shouldn't be access directly from outside of the function. 

**Python Context Manager**
+ $ Manage resource, ensure file get open and close accordingly while resource are freeup when the operation end. 
+ ? Resource include
	+ File
	+ Database Connection
	+ Socket, Network
	+ Lock in Multi-Threaded  


**What `@property` does ?** Allow accessing method like they are attributes, make cleaner code and easy access.  

### General Law of Clean Code
**DRY (Don't Repeat Yourself) principle:** avoid repeated code, every function do exactly 1 job, transparent (straight forward,  easy to understand) and have purpose.
>This principle aimed at **reducing repetition of information which likely to change, replacing it with abstrations that are less likely to change**, or using data normalization which avoids redundancy in the first place. 

❌ **Bad Code (violates DRY):**
```python
def get_admin_discount(price):
    return price * 0.9

def get_student_discount(price):
    return price * 0.9

def get_senior_discount(price):
    return price * 0.9

```
✅ **Good Code (follows DRY):**
```python
def apply_discount(price, discount=0.1):
    return price * (1 - discount)
```
>💡 **DRY** avoids repeating the same logic. You **abstract the common part**.


**YAGNI (You Aren't Gonna Need It)** says devs should only build features only when they're needed, instead of trying to predict and adding future need.

### SOLID rule and Design Patterns (Advance)
+ $ These are coding principle, your code still run weather you you followed it or not.

#### Liskov Substitution Principle (LSP) -  Subclass must act like the base class
>LSP states that **if class `B` is a subclass of `A`, then object of type `A` should be replaceacle with objects of type `B` without breaking the program.** 
+ ? 🧬 **LSP**: "If `B` is a `A`, then using `B` should behave like `A`."


❌ **Bad Code (violates LSP):**
```python
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly!")  # Breaks parent contract

def make_it_fly(bird: Bird):
    bird.fly()

make_it_fly(Ostrich())  # 💥 Error!
```
+ You wrote your program expecting **any `Bird` to be movable**
- When a subclass (`Ostrich`) **breaks that assumption**, it **violates LSP**.
	
✅ **Good Code (follows LSP):**
```python
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")

def make_it_move(bird: Bird):
    bird.move()

make_it_move(Ostrich())  # ✅ Works fine
make_it_move(Sparrow())  # ✅ Also works
```

#### Dependency Inversion Principle (DIP)
>DIP state that **High-level modules should not depend on low-level modules**. Both should depend on abstractions (Interfaces/protocols) -> **Basically Interface in Java and C#.** 
+ ? 🔌 **DIP**: "Don’t depend on **concrete classes**, depend on **interfaces**."

❌ **Bad Code (violates DIP):**
```python
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class App:
    def __init__(self):
        self.db = MySQLDatabase()  # tightly coupled

    def run(self):
        self.db.connect()
```

✅ **Good Code (follows DIP):**
```python
class DatabaseInterface:
    def connect(self):
        pass

class MySQLDatabase(DatabaseInterface):
    def connect(self):
        print("Connected to MySQL")

class App:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def run(self):
        self.db.connect()

# Inject dependency
app = App(MySQLDatabase())
app.run()
```