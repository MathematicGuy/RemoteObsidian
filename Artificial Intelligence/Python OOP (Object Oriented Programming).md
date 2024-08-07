OOP help Optimized Procedure Programming

# What is OOPs
![[Pasted image 20240807102434.png]]
> Like Designning a Car. Each part of it was seperated as a Modules for research and production. Which made the car as a whole.  
> + ? In Programming, we seperate a module into many sub module so we use them again and again by calling them. 

+ $ OOP in a nutshell where you are the Manager (Main) give command to each Staffs (Module)
![[Pasted image 20240807102948.png]]


# Classes and Objects
a Module:
has: 
does:
![[Pasted image 20240807103105.png]]
> thinki that we want to model real life Object. An Object contain pieces of data and some functionality.

Object can be used as a Blueprint - which can be re-used as a Class (Same Core Attributes and Functions with little alternative)
![[Pasted image 20240807103411.png]]


# Constructing Object and Accessing their Attributes and Methods

![[Pasted image 20240807104022.png]]

# CODE
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
+ ? The `__init__` method initializes attribute1 and attribute2 when an instance of ExampleClass is created.
+ ? The `__repr__` method provides a string representation of the instance