## Introduction to Entity Relationship Diagram
**Derived Attribute**: attribute that can be calculated using other attributes.
![[Pasted image 20250612202242.png]]

**Composite Attributes** (attribute contain multiple sub-attribute) - a attribute have a value type Object.
**Multivalue attribute** (attribute that contain/received multiple values) - a list in programming

**Relationships**
![[Pasted image 20250612202454.png]]


### Participation Constraints
**Partial participation:** 1 phần (có hay ko, ko có cũg đc) 
**Total participation:** toàn phần (bắt buộc phải có)
-> Các sinh viên có thể không có giảng viên hướng dẫn. 
-> Nhưng 1 giảng viên khi hướng dẫn chắn chắn sẽ hướng dẫn ít nhất 1 sinh viên.
![[Pasted image 20250612203019.png]] 


### Crow's Foot Notation
![[Pasted image 20250612203325.png| 300]]
**crow foot** mean many
**single line** instead of crow's foot mean 1 
**circle before** the foot mean optional (like partial participation) 
**line before** the foot mean mandatory (total participation) 
+ ? 1 - a course must have 1 and only 1 lecturer, and 1 lecturer can have 0 or many course. 
+ ? 2 - a student can enroll 0 to many course, and a course can have 0 to many enrolled student.
![[Pasted image 20250612211125.png]]

Line instead of foot mean one. One + Madatory mean One and only One.
![[Pasted image 20250612210904.png|350]]

Line instead of foot mean One. One + Optional mean Zero or One (One or Nothing because optional mean yes or no, either yes 1 or no 1)
![[Pasted image 20250612211034.png| 350]]

+ ? e.g. Student have only 1 seat. 1 seat have only 1 student
![[Pasted image 20250612211102.png]]

## Introduction to Database Normalization
