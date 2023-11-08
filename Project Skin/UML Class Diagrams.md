Sign meaning
	+ Public
	-  Private
	# Protected
	~ Package local 

**Aggregation** *(line with void diamond)*
	A child can exist beside the whole. Able to exist on its own 
	![[Pasted image 20231108095959.png]]
Ex:
> A turtoise can leave a creep and exist on it own.
![[Pasted image 20231108084256.png]]

**Composition** *(line with solid diamond)*
	A child couldn't exist without its parent.
Ex: Vtuber Sim couldn't exist without Vtuber
![[Pasted image 20231108083555.png]]
> Lobby and Bathroom cannot exist without Visitor center
> If the Visitor was destroyed, Lobby and Bathroom will be destroy also.
![[Pasted image 20231108083606.png]]

**Association**
Mulplicity
+ 1..* -> 1 to many 
+ 0..1 -> 0 to 1
+ m..n -> range from m to n
![[Pasted image 20231108095608.png]]
**One to One relationship**
![[Pasted image 20231108084126.png]]


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
> void arrow
![[Pasted image 20231108101059.png]]