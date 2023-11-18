Class Structure
+ Class Name
+ Attributes : type
+ Methods : return type 
![[Pasted image 20231114165142.png]]

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






**Aggregation** *(line with **void diamond**)* - Ex: "the baby can survived without its mother"
	A child can exist beside the whole. Able to exist on its own 
	![[Pasted image 20231108095959.png]]
Ex:
> A turtoise can leave a creep and exist on it own.
![[Pasted image 20231108084256.png]]

**Composition** *(line with **solid diamond**)* - Ex: "the baby survival depend on its mother"
	A child couldn't exist without its parent.
Ex: Vtuber Sim couldn't exist without Vtuber
![[Pasted image 20231108083555.png]]
> Lobby and Bathroom cannot exist without Visitor center
> If the Visitor was destroyed, Lobby and Bathroom will be destroy also.
![[Pasted image 20231108083606.png]]

#### Association
**Mulplicity**
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

**Realization** (solid arrow)
	relationship between an Interface and Obj
![[Pasted image 20231108095808.png]]

**Dependency** (phụ thuộc)
	An object of one class might use an object of another class in the code of a method.
	And the Obj changed may also inflict changes to the Class 
> Ex: Student info change -> RegistrationManager also change it info relate to the student
![[Pasted image 20231108100931.png]]


**Constraint**
	Condition or restriction expressed as a text (like note)
![[Pasted image 20231108100435.png]]

**Inheritance**
+ void arrow
	![[Pasted image 20231108101059.png]]
	Example: Customer is a Child of User. Thus Customer inherit all attribute of User
	![[Pasted image 20231118152313.png]]