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
The Venn Diagram show **not all Primary Key are Candidate Key** *because only some candidate keys are chosen to be primary key*, **not all Super Key are Candidate Key** because *Super Key include combination of Key with non-prime attributes*. 

We know that all Super, Candidate build upon Primary Key. So let start from the bottom, by knowing what is a Primary Key, and what Primary Key made of. 

In a tables there're columns and rows, each column represent a attribute and each row represent a example with those attributes. Whereas a Primary Key is a attribute or combination of attributes that used to uniquely identify other attributes. 
+ ? For example in this table, StudentCode and ProjectID can be combine as a Primary Key because these attribute ensure each row to be unique. (using only Student would leave row 1 the same as row 2) 
![[Pasted image 20250615173325.png| 450]]
From the example above we know there are **attributes that can and cannot be a Primary Key**. 
+ ? For example, ProjectLeader attribute isn't prime-attribute because name is repeatable, if there're 2 guy name Andy, we would have 2 rows `{101, (P03, Andy)}` and `{102, (P03, Andy)}`, if 2 attributes `(ProjectID, Project_Leader)` cannot uniquely identify other attributes (i.e. `StudentCode`) its not a Primary Key.   

So **Primary Key** is **a column or combination of columns that uniquely identify each rows in a table**. (only 1 per table)
	 Futhermore, Primary Key is **minimal**, so if it **not nescessary to combine** `ProjectID` and `Project_leader` as Primary Keys, only 1 attribute (`ProjectID` or `Project_Leader`) is chosen as primary key. 
+ ? Note: Primary key doesn't restrict combination between prime and non-prime attribute as long as its required to uniquely define other attributes inside the table. 
	e.g. StudentID or Email (must be Unique and not NULL) or {StudentID, Email} if 2 attributes required to uniquely identify other attributes. 
	
	
+ **Prime Attribute (can be Primary Key):** attributes that is unique, can be use to uniquely identify other attributes. Like StudentID or Email.  
		Prime attribute also is **a part of Candidate Key** (key that can be chosen as primary key)
	
+ **Non-Prime Attribute (cannot be Primary Key):** attribute that isn't unique and is repeatable like Name or SchoolName. 
		attribute also is **not a part of Candidate Key** (cannot be chosen as primary key due to its repeatability)  e.g. Name, Age, SchoolName
	
**Candidate Key** -  is a **set of possible keys from which the primary key is chosen**. That why prime attribute is a part of Candidate Key. 
	e.g. StudentID and Email are candidate key but only 1 are chosen as Primary Key. 
	
**Alternate Key** - is a **candidate key that is not chosen as the primary key**.  
	e.g. With StudentID chosen as Primary Key, Email become the Alternate key. 
	
**Super Key** - **any combination of Candidate Keys** and any subsets of Candidate Keys (i.e. prime attribute) as long as it **uniquely identify record within a tables**. This include combination between Candidate Key and Non-Prime attribute other than just Key. 
	Note: attribute within {} represent a super key. 
	e.g. {StudentID}, {Email}, {StudentID, Email}, {Email, StudentName}, {StudentID, Email, StudentName} 
+ $ In summary, Super Key include all possible key combinations.

**Composite Key** - is **primary key with > 1 attribute**. Specifically a **minimal combination of keys that identify record uniquely**. This mean if 2 keys are enough to identify each rows in the tables, then only 2 keys are selected as Composite Key.
	While super key can be more than enough {StudentID, Email, StudentName} for example. 
![[Pasted image 20250615144314.png]]
	
	
**Transitive Dependency** (Tính chất bắc cầu thông qua non-prime attribute): non-prime attribute depend on another non-prime attribute instead of the primary key.
	Say that $Z$ and $Y$ are non-prime. $X$ is primary key.   
	Because of $X \to Y$ and $Z \to Y$ we can determine $X \to Y \to Z$ (determine X through Y and Y through Z) $\to$ redundancy. 

**Summary:** X $\to$ Y is trivial if $Y \in X$, and $X \to Y$ is non-trivial in reverse  
**Trivial Dependecy:** Dependency **provide new information**. Not Obvious
e.g.
+ $\{StudentID, Course\} \to Instructor$
+ $Course \to Department$

**Non-Trivial Dependecy:** Dependency **doesn't provide new information.** Obvious
e.g. 
	$\{StudentID, Course\} \to StudentID$
	$StudentID \to StudentID$

## Normalization Form
Explain 1NF -> 3NF, at BCNF explain the different betwen BCNF and 3NF -> 4NF to 5NF. 

**1NF: add dependency between Attributes** this mean every records (rows) within a tables is uniquely defined. No duplicate between rows. 

**2NF: remove partial dependency** mean there is no partial dependent existed within a table, this mean every attribute (include alternate key, prime-attribute) depend entirely on 1 primary key. 
+ ! Restrict dependecy of attributes to multiple primary key but not restrict dependency between Attribute to Attribute.
> Ex: if {Player_ID, Item_Type} -> Item_Quantity, Player_Rating - then it 2NF
![[Pasted image 20250615153211.png]]

**3NF remove transitive dependecy** mean there is **no transitive dependency between attributes that is not primary key**. This mean every attribute within a table only depend entirely on the primary key and not any other prime-attribute or non-prime attribute. 
e.g. 
+ *StudentCity depend on StudentZipcode* because a City city can be determine through ZipCode. (note that StudentZipcode is a part of Candidate key)
+ *StudentZipcode depend on StudentCode*. So we can use StudentCode to determind StudentCity through StudentZipCode -> transitive dependecy. 
+ ! Transitive Dependecy can **cause Update Redundency** because if there are 2 rows with the same StudentCity, you would have to update StudentCity twice, right ?   
![[Pasted image 20250615154948.png]]
+ $ Instead, if we seperate Student Zipcode and StudentCity apart and use Student Zipcode to refer Student table from Student_Location we only need to update StudentCity once, because each record in Student_Location are uniquely define, not repeatable like in the first one.    
![[Pasted image 20250615160425.png]]


**3NF vs BCNF Key Difference:** In **3NF**, a **non-prime attribute can depend on a prime attribute or a superkey. Not strictly require to be depend entirely on the PrimaryKey alone,** attributes **can depend on candidate  within the superkey**
	e.g.
		`Instructor` depend on `PrimaryKey(StudentCode, Course)` 
		`Instructor` also depend on `Course`  -> **not depend entirely on the PrimaryKey.** ![[Pasted image 20250615203105.png]]
	
	
- In **BCNF**, is *3NF but no attribute (prime and non-prime) can depend on anything other than the PrimaryKey*
	e.g.
		`Instructor` depend on `PrimaryKey(StudentCode, Course)` 
		`Instructor` also depend on `Course`  -> **violate BCNF**
	
	**Basically:** Every attribute only depend on the entire super key (e.g. depend on both Student_Code and ProjectID) and not a single prime attribute. (i.e. depend ProjectID or StudentCode alone)
	
Decompose table into $R_{1}$ and $R_2$ to satisfied BCNF.
$R_{1}(Course, Instructor)$
![[Pasted image 20250615201944.png]]
$R_{2}(StudentCode, Course)$
![[Pasted image 20250615201949.png]]

**4NF: remove multi-value dependency** (in table with at least 3 columns)
	Table satisfied **4NF also satisfied BCNF and should not have any Multi-valued Dependency.** 
	Note: A and B is attribute, so its could contain either 1 or multiple values. 
	
**Multi-valued Dependecy** ($\to \to$) mean 
![[Pasted image 20250615183556.png]]
1. For dependecy $A \to B$, if for single value of A `e.g. Course=CS101`, multiple values of B exist `e.g. Teacher={Smith, Jones}`. (i.e. A determint a set of B values)
2. A table need to have at least 3 columns to be Multi-valued Dependency `e.g. R(Course, Teacher, Book)`. (*create to proved condition 3.*)  
3. For relational `R(Course, Teacher, Book)`, if there are multi-valued dependecy between Course and Teacher, then Book should be independent. 
	
**Multi-value Dependecy table (i.e. 4NF) can also be decompose into** $R_1(Course, Teacher)$ and $R_2(Course, Book)$ which required the at least 3 attributes in the original relation.
![[Pasted image 20250615190538.png]]
**Where:** 
+ B `Teacher` is not dependent on C  `Book`
- Primary key $R_1(A, B)$ but `Course` is the linking attribute.
- Primary key $R_2(A, C)$ but `Course` is the linking attribute. Course simply a shared attribute. 
+ $A \to \to B$  and $A \to \to C$  ($\to \to$ mean multi-valued dependency)
+ Note: A could be the primary key in its own table (e.g. `Course` table) and both $R1$ and $R_{2}$ could reference it as a foreign key.   

**TODO:** 
Example of 5NF
Compare 4NF to 5NF 
Case Study