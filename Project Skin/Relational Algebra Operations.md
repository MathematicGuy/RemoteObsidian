### Unar
[Cartesian Product](https://www.youtube.com/watch?app=desktop&v=qvioqCvvMek)


### Binary
**JOIN Operation ( ⋈ )**
	Combines related tuples from 2 relations into a vgle relation.
![[Pasted image 20231117080302.png]]
> Goal: Combine data from multiple relation so that related infomation display in a single table.
![[Pasted image 20231117080524.png]]
*JOIN vs Casian Product*
JOIN
	Only take what satisfied the condition
Casian Product
	Combine all into a single table

**NATURAL JOIN ( * )** 
> Can be performed only if there is a common attribute in between the relations.
![[Pasted image 20231117080907.png]]

>In JOIN there is a duplicate of data. That are unecessary
![[Pasted image 20231117080741.png]]
> NATURAL JOIN like JOIN but remove the abundant column from it comparesor table: "SSN" 
![[Pasted image 20231117081150.png]]

**DIVISON Operation ( ÷ )**
Ex: To retrieve the Employee ID (EID) of the employees working on all
projects.
+ notice to use DIVISON op if there the keyword: "all" 
![[Pasted image 20231117081812.png]]
Res
![[Pasted image 20231117081824.png]]

**Explaine using other operation**
![[Pasted image 20231117082007.png]]

+ Step1: Get value (no duplicate) from column x in table R
	![[Pasted image 20231117083211.png]]
+ Step2: Multiply it with column x in table S. Called this new table T1   
	![[Pasted image 20231117083219.png]]
+ Step3: Minus table T1 with table R, delete all the similiar tuple in both table. 
> Call this table **T2** 
	![[Pasted image 20231117083157.png]]
+ Step4: Minus T2 with T1, get all tuples that are represent onluy in relation T1 not T2.
	![[Pasted image 20231117083629.png]]
We have this
![[Pasted image 20231117083524.png]]


