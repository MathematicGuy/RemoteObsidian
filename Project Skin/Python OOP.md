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
	To access `pay_rate`, we can either called `Item.pay_rate` or `self.pay_rate` to determint if we want `pay_rate` can be access at Class level or Instant level.
	
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
Check attribute each level can access, at instance level, only attributes inside `__init__` can be access.
```python
print(Item.__dict__) # list all the attributes for Class level
print(item1.__dict__) # list all the attributes for instance level
```
> {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x00000155335DCFE0>, 'total_price': <function Item.total_price at 0x00000155335DD120>, 'apply_discount': <function Item.apply_discount at 0x00000155335DD260>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
> 
> {'name': 'Phone2', 'price': 2000, 'quantity': 3}

+ ? Notice that for `item2`, we must access `pay_rate` at Class level to modify `pay_rate` from 0.8 to 0.2. Remember Class attribute modify at Class level, Instance attribute modify at Instance level. The results below show **pay_rate are modify throughout the whole class.**     
```python
Item.pay_rate = 0.2

item1 = Item("Phone", 1000, 22) # create instance of a class
item1.apply_discount()
item2 = Item("Phone2", 1000, 10) # create instance of a class
item2.apply_discount()

print('discount rate: ', item1.payrate) # can be accessible through class level
print('discount rate: ', item2.price) # STILL GET 80% DISCOUNT
```
>discount rate:  200.0
>discount rate:  200.0
+ ? Example of modify at instance level  using `self.pay_rate`, pay_rate can be modify outside the class. Using self.pay_rate allow us to modify only the instance not the whole class, this mean item1 and item2 can have a different pay_rate
```python
class Item:
	...
	def apply_discount(self):
        self.price = self.price * self.pay_rate 


item2 = Item("Phone2", 1000, 10) # create instance of a class
item2.pay_rate = 0.5
item2.apply_discount()
print('discount rate: ', item2.price) 
```
>discount rate:  500.0 


**Save all class instance and Accessing all instance name**
```python
class Item:
	all = []
	def __init__(self):
		# Action to Execute
		Item.all.append(self)
		...

for i in Item:
	print(i.name)
```

#repr_vs_str
![[Pasted image 20240923142039.png]]
+ use `__str__` to display information to user
+ use `__repr__` to debugging, allow dev to modify print output format 

**Example Usage**
```python
class Item:
	...
	# modify print format
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

print(Item.all)
```
> [Item(Phone, 100, 2), Item(Phone2, 200, 3), Item(Cable, 10, 5), Item(Mouse, 50, 5), Item(Keyboard, 75, 5)]
### Class & Static Methods
+ ? "Instantiate Method" (Class Method) can only be access through Class Level.
```python
class Item:
	...
	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			items = csv.DictReader(f)
			for item in items:
				print(Item(
					name = item.get('name'),
					price = float(item.get('price')),
					quantity = int(item.get('quantity')),
				))
	...
	
Item.instantiate_from_csv() # call classmethod
```
> Class reference must be pass as the first augument: cls for instant
![[Pasted image 20240923161111.png]]

####  When to use class methods and when to use static methods ?
+ $ `@classmethod`: used when yo **need to do sth** at the **class level** rather than the instance level, take `cls` as first argument. **e.g. modify class level attribute**. 
+ $ It can be called **on the class itself**, or **on instances** (gọi hàm trong class), but it **operates on the class data**.
+ ? Example: change class level pay_rate using @classmethod
```python
    @classmethod
    def change_pay_rate(cls, new_rate):
        # Modifies the class attribute `pay_rate`
        cls.pay_rate = new_rate

# Call classmethod from an instance
item1 = Item('Phone', 1000)
item1.change_pay_rate(0.7)
print(Item.pay_rate)  # Output: 0.7
```

+ $ `@staticmethod`: is a method that belongs to the class , but it **does not receive any special first augument like** `self` or `cls` (like `@classmethod` ) while still **can be access like a normal function with parameter** 
+ $ The method doesn’t need access to instance or class data.
	they could be standalone functions, but they are grouped within the class for organizational purporses.
```python
class MathUtility:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

# Call static methods directly on the class
result_add = MathUtility.add_numbers(5, 10)
result_multiply = MathUtility.multiply_numbers(3, 4)

print(result_add)  # Output: 15
print(result_multiply)  # Output: 12z
```


## Inheritant
**Basic Class Inheritant.** Phone inherit attribute from Item, this allow us to create new instance of class Phone with Item Class attributes like name, price, quantity. 
```python
class Phone(Item): # inherit Item class
	...

phone4 = Phone('phonev4', 800, 4)
```

**super function**: allow sub-class to have access to all attributes/methods from its mother class
+ ? with `super().__init__`, print out both Phone and Item Class 
```python
class Phone(Item): # inherit Item class
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        #? Instance Level
        # Call to super func to have access to all attributes/methods from Item class
        super().__init__(
            name, price, quantity
        )
		self.broken_phone = broken_phone


#? Initiate Class Instances 
phone1 = Item('phonev1', 500, 4)
phone2 = Item('phonev2', 600, 4)

# This is just fine
phone3 = Phone('phonev3', 700, 4, 1)
phone4 = Phone('phonev4', 800, 4, 2)
print(Phone.all)
```
>[Item(phonev1, 500, 4), Item(phonev2, 600, 4), Phone(phonev3, 700, 4), Phone(phonev4, 800, 4)]
	
+ ? without `super().__init__`, only print out Phone Class 
```python
class Phone(Item): # inherit Item class
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        #? Instance Level
        # Call to super func to have access to all attributes/methods from Item class
		self.broken_phone = broken_phone
	
#? Initiate Class Instances 
phone1 = Item('phonev1', 500, 4)
phone2 = Item('phonev2', 600, 4)

# This is just fine
phone3 = Phone('phonev3', 700, 4, 1)
phone4 = Phone('phonev4', 800, 4, 2)
print(Phone.all)
```
> [Item(phonev1, 500, 4), Item(phonev2, 600, 4)]

+ ? **Question:** What if I **only want to calculate total Phone Price**, not including Item. should I remove super() function? Well you don't have to
+ $ `@classmethod` are made for this, class method only access attributes and instance of that class. 
```python
class Phone(Item): # inherit Item class
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        #? Instance Level
        super().__init__(
            name, price, quantity
        )
        self.broken_phone = broken_phone
        
    @classmethod
    def total_assets(cls):
        total = 0
        for instance in cls.all:
            if isinstance(instance, cls):
                total += instance.price * (instance.quantity - instance.broken_phone)
                
        return total


#? Initiate Class Instances 
phone1 = Item('phonev1', 500, 4)

# This is just fine
phone3 = Phone('phonev3', 700, 4, 1)
phone4 = Phone('phonev4', 800, 4, 2)
print(Phone.total_assets())
```
> output: 3700 ($700*3 + 800*2 = 3700$)

**access to class attributes**: 
+ `self`: the class itself
+ `__class__`: access to class function
+ `__name__`: class function use to get class name
```python
print(f'{self.__class__.__name__}')
```

## Getters and Setters

**read-only-method**: use @property to make variables cannot be change, only readable. this called Encapsulation.
```python
@property
def read_only_name(self):
	self.name = name # private attribute
```

**private attribute**: in python **private attribute annotate with a underscore** `_name`, private attribute prevent access to the attribute from outside of the class. (`_` is **just a annotation, it doesn't affect the code**)
```python
class Item:
	def __init__(self, name):
	    self._name = name # private attribute
	
	@property
    def name(self):
        return self._name
```
However, it not authentic to show the underscore along with attribute, we could hide it using not underscore `__`, a double underscore. 
![[Pasted image 20240924112925.png]]
> Using double underscore, private sign will not be show. 
```python
class Item:
	def __init__(self, name):
	    self.__name = name # private attribute
	
	@property
    def name(self):
        return self.__name
```

**Modify private attribute** with **setter method**,  using setter, `@property` method's attribute can be replace and modify.
```python
class Item:
    def __init__(self, name: str, price: float, quantity=0):
	    self.__name = name # private attribute
	
	
	 @name.setter
    def name(self, value): # parameter set as value
        self.__name = value
```


```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

