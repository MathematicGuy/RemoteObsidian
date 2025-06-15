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
**Database Normalization help** reduce data redundancy and data anomaly (e.g. missing data, un-synchonize data between 2 tables) 

**Data Normalization** is the act of divides larger tables into smaller tables and link them to create relationship between tables. 

### Problem with Un-Normalize Table
![[Pasted image 20250615144133.png]]
	**Redundant Data Update:** update of 1 person lead to updation of multiple row.
	**Inconsistent Data:** If only 1 professor name is update while other row with that professor name don't. 
	**Delete Anomalies:** delete student mean delete all columns of that rows, if course 101 within the deleted row, the course data also get deleted while we only want to delete the student.  

### Type of Data Anomalies (in un-normalized table)

![[Pasted image 20250614165917.png]]

#### Insertion Anomaly
+ ? Happened when attributes are missing or un-synchronize at insertion time. Insertion in unnormalize database can create these problem:
 
 **Redundant Data:** Insertion of a student lead to value repeation of 'CourseName' and 'Professor'. Thus you have to insert these value again although these value already exist.
  ![[Pasted image 20250614170410.png]]
**Partial Data Insertion:** Insertion of New Course with no enrolled Student will allow missing value for student ID and Name. (often NULL value)
![[Pasted image 20250614170701.png| 450]]
  
**Null Value Issues:** Like partial data insertion, insertion of student who haven't enroll to any course will create null value for Courses and Professor columns.
![[Pasted image 20250614171111.png]]

#### Updation anomalies 
+ ? This occur when multiple data are repeated in the same table lead to inefficiency. 
	   ![[Pasted image 20250614172047.png]]
	**Redundant Data Update:** Update of 1 row mean the update of multiple rows because. e.g. when a Professor change his name to Dr.Brown, all row with Dr.Smith would also have to updated for data consistancy.
	![[Pasted image 20250614172305.png]]
	**Inconsistant Data:** when you update 1 row but forget to update other rows. LIke when you update 1 Professor name but not synchronized the rest.
	![[Pasted image 20250614172316.png]]
	
3. **Delete Anomalies:** Delete of 1 data lead to the unwanted deletion of other data.
	![[Pasted image 20250614173016.png]]
	**Unwanted Data Loss:** Delete Student Data also delete Course & Professor data. 
	This can create *Orphan Records* if Course Name are depend on CourseID.
	 ![[Pasted image 20250614173027.png]] 

## Terminology
![[Pasted image 20250615144249.png]]
**Primary Key** - **A column or combination of columns that uniquely identify each rows in a table**. (only 1 per table) 
	e.g. StudentCode or StudentID (must be Unique and not NULL)
	
**Candidate Key** -  is a **set of possible keys from which the primary key is chosen**.
	e.g. StudentID and Email are candidate key but only 1 are chosen as Primary Key. 
	
**Alternate Key** - is a **candidate key that is not chosen as the primary key**.  
	e.g. With StudentID chosen as Primary Key, Email become the Alternate key. 
	
**Super Key** - **any combination of Candidate Keys** (and any subsets of Candidate Keys) that uniquely identify record within a tables. 
	Note: key within {} create a super key. 
	e.g. {StudentID}, {Email}, {StudentID, Email}, {Email, StudentName}, {StudentID, Email, StudentName}
	
**Composite Key** - like a **superkey with > 1 attribute**. Specifically a **minimal combination of keys that identify record uniquely**. This mean if 2 keys are enough to identify each rows in the tables, then only 2 keys are selected as Composite Key.
	While super key can be more than enough {StudentID, Email, StudentName} for example. 
![[Pasted image 20250615144314.png]]
	
**Prime Attribute:** attribute that is a part of Candidate Key (can be chosen as primary key) 
	e.g. StudentID, Email
	
**Non-Prime Attribute:** attribute that is not a part of Candidate Key (cannot be chosen as primary key due to its repeatability) 
	e.g. Name, Age, SchoolName
	
Note: Prime and Non-Prime are not like Candidate and Alternate Key. It's describe if a attribute can become a key while Candidate and Alternate Key describe if a attribute (could become a key) has been chosen to be a key,   
	
Note: $X \to Y$ indicate funtional dependency (FD), means if 2 rows have the same value of X, they must have the same value of Y.   
	e.g. if $StudentID \to Name$, then $StudentID$ uniquely determines Name. 
	
**Transitive Dependency** (Tính chất bắc cầu): $X \to Y$ and $Z \to Y$ thus $X \to Y \to Z$

## Normalization Form
Explain 1NF -> 3NF, at BCNF explain the different betwen BCNF and 3NF -> 4NF to 5NF. 


