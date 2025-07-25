# OOP
#### `__init__`
+ ? The `__init__()` function is called automatically every time the class is being used by a Object, it just empty when you don't initialize it. But if you do, `__init__()` can be used to initialize attribute of a class with specific value. 
	e.g. Dog class with `name` attribute. 
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
+ ? `self` is just a naming convention on how you declare a pointer. Its can be anything really, but you shouldn't.
```python
class Cat:
    def describe(age, name):
        age.__age = 9
        print(age.__age, name)

cat = Cat()
cat.describe(1) # 9 1
```



# Getting Started
## What is a Class in Python OOP
+ ?  A Class is like a **template for creating an Object in OOP**. Its **can contain multiple attributes and functions** (called methods). In simple terms, **OOP Class is way to organize and encapsulate both data and functionality together**.      

+ **instance: phiên bản/ví dụ** == **object: đối tượng**
	When printing out datatype of any variable, you can see each of them are instances/object of a class. 
		![[Untitled 3.jpg]]

Initialize a Class
```python
class Item:
    pass
```
Create a Object
```python
item1 = Item() # create instance of Item class
```
assign attributes for Object
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
+ $ You **can access Methods through its Class**. Help distinguish methods with identical name from different classes.
	e.g. **price attribute from item1** class: **item1.price**, **total_price function from item1** class: **item1.total_price()**
```python
class Car:
    @staticmethod
    def start():
        print("Car engine started.")

class Boat:
    @staticmethod
    def start():
        print("Boat engine started.")

# Creating instances of Car and Boat
car = Car()
boat = Boat()

# Calling start method through instances
car.start()  # Output: Car engine started.
boat.start()  # Output: Boat engine started.

# Accessing the start method through the class name
Car.start()  # Output: Car engine started.
Boat.start()  # Output: Boat engine started.
```

## Constructor: `__init__(self)`
> A special method used to **initialize the attribute of a newly created Object** by pre-define attribute the Object' class attribute.

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
        
item1 = Item("Phone", 2000, 3) # create instance of a class
item2 = Item("Phone", 1000, 22) # create instance of a class
print(f"total price of item1: {item1.total_price()}")
```
>An Instance/Oject created: Phone2 price $2000 with quantity of 3
>An Instance/Oject created: Phone price $1000 with quantity of 22
>Total price of item1: 6000

#### Validate Datatype
+ add expected class data type: str, float, int (quantity=0) auto define as int
+ ? **assert: [condition], [print_error_statement]**: assert is a keyword **for validation during debugging**, validate datatype, value and also can return error warning for those errors conditions.
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

item1 = Item("Phone", 1000, 22) # <- This is a Instance
item1.apply_discount()
item2 = Item("Phone2", 1000, 10) # create instance of a class
item2.apply_discount()

print('discount rate: ', item1.payrate) # can be accessible through class level
print('discount rate: ', item2.price) # STILL GET 80% DISCOUNT
```
>discount rate:  200.0
>discount rate:  200.0
+ ? E.g. **Modify attribute at instance level**  using `self.pay_rate`, `pay_rate` can be modify outside the class. Using `self.pay_rate` allow us to **modify only the instance not the whole class**, this mean `item1` and `item2` can have a different `pay_rate`
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

#repr_vs_str: like f string
```python
class ExampleClass:  
    def __init__(self, attribute1, attribute2):  
        self.attribute1 = attribute1  
        self.attribute2 = attribute2  
  
    def __repr__(self):  
        return "%s(%r)" % (self.__class__, self.__dict__)  
  
# Creating an instance of ExampleClass  
example = ExampleClass('value1', 'value2')  
  
# Printing the instance to see the output of __repr__  
print(example)
```
+ The `__repr__` method provides a string representation of the instance
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


`__call__(self)` -> return class information when calling the class a a function
	e.g. `deer = Animal()` -> calling `deer()` will trigger `__call__(self)` 

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
 
+ $ `@staticmethod`: is a method that belongs to the class , but it **does not receive any special first augment like** `self` or `cls` (like `@classmethod` ) while still **can be access like a normal function with parameter** 
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
print(result_multiply)  # Output: 12
```

## Inheritant
> Allow classes (children class) to have attributes and methods from another class (mother class)

**Item (Mother Class)**
```python
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        self.__name = name # private access modifier 
        self._price = price # protected access modifier
        self.quantity = quantity
        
        # Action to execute
        Item.all.append(self)

	 
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer() # return True if the float a integer
        elif isinstance(num, int):
            return True
        else:
            return False
```

**Phone (Child Class)**
> Inheritance allow Phone's class Objects to have all attributes and method from Item class.
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

+ ? **Question:** What if I **only want to calculate total Phone Price** of all Instances. should I remove super() function? Well you don't have to
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
phone3 = Phone('phonev3', 700, 4, 1) # 4-1 = 3 PHONE IN TOTAL
phone4 = Phone('phonev4', 800, 4, 2) # 4 - 2 = 2 PHONE IN TOTAL
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

### Inheritance Example using `super()`
```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def compute_salary(self):
        return self._salary + 1000

class Manager(Employee):
    def __init__(self, salary, bonus):
        self._salary = salary
        self.bonus = bonus

    def compute_salary(self):
        #? Inheritance allow merging function together
        #? return self._salary + 1000 + self.bonus
        return super().compute_salary() + self.bonus

n = Employee(3,4)
print(n.compute_salary()) # output: 1004
m = Manager(2, 4)
m.compute_salary() # output: 1006
```

## Getters and Setters

**read-only-method**: 
+ **@property** is use to **make a method behave like a read-only attribute**. 
+ This called **Encapsulation** (i.e. **Encapsulation** means *hiding internal data and only exposing what's necessary*) In this case:
	- `_name` is _hidden_ (a private detail).
	    
	- `@property` exposes it safely—**only for reading**, not writing.
	  
+ Read-only method doesn't modify any constance's or class's attributes, it just read them. Used to read private attribute without allowing direct modification. 
```python
class Item:
	def __init__(self, name):
	    self._name = name # private attribute
	
@property
def read_only_name(self):
	return self._name # private attribute
```
**usage**
```python
p = Person("D")
print(p.name)   # ✅ Output: D
p.name = "New"  # ❌ Error: can't set attribute
```
to modify private `name` attribute, you have to add a `setter`:
```python
@name.setter
def name(self, value):
    self._name = value
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
> **Using double underscore, private sign will not be show**. 
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

#### Purpose of "Setter"/"Getter with property"
+ ? **Getter** for attributes need only to be read like the **total_price**   
```python
class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
		self.quantity = quantity
		
    # Compute total price based on price and quantity
    @property
    def total_price(self):
        return self.price * self.quantity

item = Item("Laptop", 1000, 3)
print(item.total_price)  # Computed as 1000 * 3 = 3000
```
+ ? **Setter** for validation purpose, like a `try_except` for input. Allow you to dictate input format and datatype.
```python
class Item:
	# Getter for price
    @property
    def price(self):
        return self._price
    
    # Setter for price with validation
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price must be greater than zero")
	...
	
# Using @property
item = Item("Laptop", 1000)
```


```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
	
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
	
    def stop_engine(self):
        print("Car engine stopped.")
	
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")
	
    def stop_engine(self):
        print("Motorcycle engine stopped.")

# vehicle = Vehicle()  # This will raise an error: Can't instantiate abstract class

car = Car()
motorcycle = Motorcycle()

car.start_engine()         # Output: Car engine started.
motorcycle.start_engine()  # Output: Motorcycle engine started.
```


## Polymorphism
+ $ **Polymorphishm** mean "many form" in greek, it refers to **ability of different classes** to be **treated as instances of the same class through a common interface**.
+ ? Example: each animal **sub-class can override the `sound()` method to provide its own implementation** like below
```python
from abc import abstractmethod
class Animal:
    @abstractmethod
    def sound():
        pass        
    
def animal_sound(animal):
    return f'{animal.__class__.__name__} make sound: {animal.sound()}'    

class Dog(Animal):
    def sound(self):
        return "Bark Bark"    

class Cat(Animal):
    def sound(self):
        return "Meow Meow"

zoo = [Dog(), Cat()]

for animal in zoo:
    print(animal_sound(animal))
```
> Dog make sound: Bark Bark
> Cat make sound: Meow Meow
+ ? **Polymorphic Approach**:
	+ **Extensibility:** you can add new animal type like "Hourse" with their own behaviours (methods) without affecting the `Animal` class.
	+ **Method Overriding:** each animale type (sub-class) can override the `sound` method to provided their own implementation. 
	+ **Lose Coupling:** `animal_sound()` function doesn't need to know which class are called, it just care it that class have `sound()` function.
	
-> easy to scale and manage because each class are tidy and unique (don't have duplicate method)

 **Advantages of Polymorphism** compare to **Non-Polymorphism** Approach
```python
class Animal:
    all = []
    
    def __init__(self, sound):
        self.sound = sound
        Animal.all.append(self)
        
    def make_sound(self):
        return f'{self.__class__.__name__} make sound: {self.sound}'
    
    
dog = Animal("Bark Bark")
cat = Animal("Meow Moew")

for ani in Animal.all:
    print(ani.make_sound())
```
> Dog make sound: Bark Bark
> Cat make sound: Meow Meow
+ ? **Non-Polymorphic Approach**: 
	+ **Dependence:** All instance are depend on 1 class, making it un-flexible, there're no different between types like dog, cat making **some methods become redundent for some class**. (**Ex: dog with fly() method**). 
		+ **The logic for all animal are confine into 1 class**, making it harder to extend in the future. Hard to add specific behaviour for each type of animal. 
		
		+ Lead to Scalability problem in the future, different types of animals with different behaviors in a single `Animal` class would quickly become unmanageable.
		
	+ **Tight Coupling:** all animal type must follow  `make_sound()` method print format, can't customize their own.    

## Additional Note
### Recursion
```python
i = 0.02 
m = 100

def im(m, i, loop):
    loop = loop
    m = m + m*i
    print(f"loop {loop}, total money: {m:.4f}")
    
    if loop > 0:
        loop -= 1    
        return im(m, i, loop)

im(m,i,100)
```

### Access Object Type
![[Pasted image 20250402141710.png]]
