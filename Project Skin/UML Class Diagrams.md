**Purpose**
> Represents a blueprint for objects, defining attributes and behaviours 
```java
// UML representation of a class
+---------------------+
|      Car            |
+---------------------+
| - make: String      |
| - model: String     |
| - year: int         |
|---------------------|
| + start()           |
| + accelerate()      |
| + brake()           |
+---------------------+
```
+ Class Name : CAR
+ Attributes : type
```java
// UML representation of attributes in the Car class
+---------------------+
|      Car            |
+---------------------+
| - make: String      |
| - model: String     |
| - year: int         |
+---------------------+
```
+ Methods : return type 
```java
// UML representation of methods in the Car class
+---------------------+
|      Car            |
+---------------------+
| + start()           |
| + accelerate()      |
| + brake()           |
+---------------------+
```

Sign meaning
	+ Public
	-  Private
	# Protected
	~ Package local 
	underline : " __ " -> static method  
		![[Pasted image 20231118143859.png]]

> Employee take attribute String and double
> ![[Pasted image 20231118144018.png]]
> getName() method return String 
> changeName() method take String value and return nothing
> ![[Pasted image 20231118143953.png]]


#### **Association**
>Represents relationships between classes.
![[Pasted image 20231118164553.png]]
> ClassA knows about ClassB
> ClassB knows nothing about ClassA

![[Pasted image 20231118164428.png]]


#### **Aggregation** *(line with **void diamond**)* - Ex: "the baby can survived without its mother"
> Represents a "whole-part" relationship, where a part can exist independently of the whole.
	![[Pasted image 20231108095959.png]]
Ex:
> A turtoise can leave a creep and exist on it own.
![[Pasted image 20231108084256.png]]


#### **Composition** *(line with **solid diamond**)* - Ex: "the baby survival depend on its mother"
+ **A child couldn't exist without its parent.** 
> Represents a stronger form of the "whole-part" relationship, where the part cannot exist without the whole.
Ex: Vtuber Sim couldn't exist without Vtuber
![[Pasted image 20231108083555.png]]
> Lobby and Bathroom cannot exist without Visitor center
> If the Visitor was destroyed, Lobby and Bathroom will be destroy also.
![[Pasted image 20231108083606.png]]


#### **Mulplicity**
+ * -> zero or more instances
+ n -> exactly n instances
+ 1..* -> 1 to many 
+ 0..1 -> 0 to 1
+ m..n -> range from m to n
![[Pasted image 20231108095608.png]]
**One to One relationship**
![[Pasted image 20231108084126.png]]
+ More Example of Mulplicity
	+ (Course tbl) 1 - 0...* (Project tbl)
		 1 course 0 to many projects (or 1 course can have zero or many projects )
	+ (Course tbl) 1 - 0...* (Student tbl)
		1 course can have one to many Student attended

+ House Muplicity Example
	![[Pasted image 20231118151124.png]]
**Composition** 
 + Kitchen, Bath, Bedroom cannot exist without a House. (là 1 thành phần, ràng buộc) 
	 1 House have 1 Kitchen, 1 House have 1 Bath, 1 House have 1 to many Bedroom
**Aggragation** 
+ Mailbox a part of a house but can exist independent. (là 1 phần, ko ràng buộc, có thể tách ra)
**Association**
+ Mortgage -> Associate with a house. But not a part of a House. A house can have a mortgage or not. (liên quan)

#### **Realization** (solid arrow)
+ Relationship between an Interface and Obj
![[Pasted image 20231108095808.png]]

#### **Dependency** (phụ thuộc)
+ An object of one class might use an object of another class in the code of a method. And the Obj changed may also inflict changes to the Class 
> Ex: Student info change -> RegistrationManager also change it info relate to the student
![[Pasted image 20231108100931.png]]

#### Diagram Sign 
**Constraint**
	Condition or restriction expressed as a text (like note)
![[Pasted image 20231108100435.png]]

**Inheritance**
> **Represents an "is-a" relationship, where one class is a specialized version of another.**
> Ex: The Square is a Shape
+ void arrow
	![[Pasted image 20231108101059.png]]
```java
// UML representation of inheritance between Vehicle and Car classes
+---------------------+        +---------------------+
|      Vehicle        |        |         Car         |
+---------------------+        +---------------------+
| - make: String      |        | - model: String     |
| - model: String     |        | - year: int         |
| - year: int         |        |---------------------|
|---------------------|        | + start()           |
| + start()           |        | + accelerate()      |
| + accelerate()      |        | + brake()           |
| + brake()           |        +---------------------+
+---------------------+
```

**Summary**
![[Pasted image 20231119171726.png]]

