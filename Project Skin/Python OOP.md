# OOP
![[Pasted image 20240923101844.png]]

the `__init__` method allow class attribute to be modified directly without adding any function like `speak()` below
```python
class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
```
>output: Rodger is a mammal
+ ? Add speak function after `def __init__(self, name)`
```python
def speak(self):
	print("My name is {}".format(self.name))

Tommy.speak() 
```
>output: My name is Tommy

### Getting Started
when printing out datatype of any variable, you can see each of them are instances/object of a class. 
+ **instance: phiên bản/ví dụ**  
![[Pasted image 20240923103507.png]]
+ ? instance == object

Initialize a Class
```python
class Item:
    pass
```
Create a Object
```python
item1 = Item() # create instance of Item class
```
Assign attributes for Object
```python
item1.name = "Phone"
item1.price = 10000
item1.quantity = 4

# Check attribute datatype
print(type(item1)) 
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
```
> <class '__main__.Item'>
> <class 'str'>
> <class 'int'>
> <class 'int'>

### Method (Function inside Class)
+ ? When function created inside a Class, it called Method.
+ When calling a method outside of the class remember to call the class as well. Because each **subvalue/object of a class can only be access though "."** 
	e.g. **price attribute from item1** class: **item1.price**, **total_price function from item1** class: **item1.total_price()**
	
```python
class Item:
    def total_price(self, x, y):
        return x * y

# "Create Instance"/"Add attributes" to Item class
item1 = Item() 
item1.price = 10000 
item1.quantity = 4
tot = item1.total_price(item1.price, item1.quantity)
print(tot)
```

## Constructor
> Method with a unique name that you need to call it in able to use it special features. e.g. `__init__(self)`

`__init__(self, attribute_1, attribute_1, etc..)`: define class attribute, making them accessible from both in and out side of the class.
+ ? Keyword **self** represent the class itself. when you calling **self** you calling **Item** class. 
	Like when you access attribute from outside Item class (example above), to **access attribute inside a class you use self** 
	Also, you can add attributes outside of Item class like normal, this doesn't affect anything.
```python
class Item:
    #? __init__ get call everytime the main class is called
    def __init__(self, name, price, quantity):
        print(f"An Instance/Oject created: {name} price ${price} with quantity of {quantity}")
        self.name = name
        self.price = price
        self.quantity = quantity

	# now you can calc total_price automatically when calling this func
    def total_price(self):
        return self.price * self.quantity
        
item1 = Item("Phone", 1000, 22) # create instance of a class
print(f"total price of item1: {item1.total_price()}")
```
>An Instance/Oject created: Phone price $1000 with quantity of 22
>An Instance/Oject created: Phone2 price $2000 with quantity of 3
>Total price of item1: 6000
#### Validate Datatype
+ add expected class data type: str, float, int (quantity=0) auto define as int
+ ? **assert: condition, print_error_statement**: assert keyword (not a function) use to validate datatype, value and can also return error warning for those errors conditions.
	in the example below, assert check if the price is larger or equal to 0, if not print out AssertionError statement.
```python
    def __init__(self, name: str, price: float, quantity=0):
		 # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
		...
		
item1 = Item("Phone", -22, 22) # create instance of a class
```
> AssertionError: Price -22 is not greater than or equal to zero

+ ? **attribute**: Python will first look for an instance-level (`__init__`) attribute; if it's not defined, it will fall back to the class-level attribute. 
	To access `pay_rate`, we can either called `Item.pay_rate` or `self.pay_rate` to determint if we want `pay_rate` can be access at Class or Instant level.
	
- **Class Attributes**:
	    - Defined at the class level (outside `__init__`).
	    - **Accessible** using both `ClassName.attribute_name` and `self.attribute_name`.
	    - **Shared** by all instances of the class.
	    - **Not private by default**—you can access or modify them from outside the class unless you deliberately restrict access.
	
- **Instance Attributes**:
    
    - Defined inside the `__init__` method or other instance methods.
    - **Accessible** using `self.attribute_name`.
    - **Specific to each instance**—each instance of the class has its own copy of the attribute.
    - **Public by default** but can be made private using name mangling (e.g., `__attribute`).
    
```python
class Item:
    #? Class Level
    pay_rate = 0.8 # discount 20%
     
    def __init__(self, name: str, price: float, quantity=0):
        #? Instance Level
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity
		
	def apply_discount(self):
        self.price = self.price * Item.pay_rate 
```
Check attribute each level can access, seem like at instance level, only attributes inside `__init__` can be access.
```python
print(Item.__dict__) # list all the attributes for Class level
print(item1.__dict__) # list all the attributes for instance level
```
> {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x00000155335DCFE0>, 'total_price': <function Item.total_price at 0x00000155335DD120>, 'apply_discount': <function Item.apply_discount at 0x00000155335DD260>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
> 
> {'name': 'Phone2', 'price': 2000, 'quantity': 3}

+ ? Notice that for `item2`, we must access `pay_rate` at Class level to modify `pay_rate` from 0.8 to 0.2. Remember Class attribute modify at Class level, Instance attribute modify at Instance level.    
```python
item1.apply_discount()
print('discount rate: ', item1.payrate) # can be accessible through class level

Item.pay_rate = 0.2
item2.apply_discount()
print('discount rate: ', item2.price) # STILL GET 80% DISCOUNT
```
>discount rate:  800.0
>discount rate:  400.0


```python

```

```python

```

```python

```

