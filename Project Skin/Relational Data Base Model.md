### Intro to Relaitonal Data Model
###### Terminologies
**Domain** (Miền)
+ Set set of values in range that satisfied a condition
+ Ex:
	+ (a) Name : string of characters that represent name of persons. 
	+ (b) Employee-ages: Possible ages of employees of a	company (values between 20 & 70 years old).

**Relation Schema** (lược đồ quan hệ)
Atomic value: single value in a column
> Describe a relation
 STUDENT (Name, RollNo, Age, Address, Phone, Grade)
	STUDENT (Name: string, RollNo: integer, Age: integer, Address: strin Phone: string, Grade: real)

Ordering of Tuple within a Relation
+ A relation is a set of tuples

### Relational Model Constrains
**Constraints on databases**
+ Inherent model-based (Explicit constraint): inherent in the data model
	Ex: duplicate tuple or row.
+ Schema based (Explicit constaint): Define directly in the schemas of the data model 
	+ Ex: must be between 62 and 65
+ Application based: Must be expressed and enforced by the application program.
	+ Used mainly to testing how goo the design of the relational DB and normalize

**Domain constraints** (Data Type error like "int with string , etc..." )
+ Must be atomic value.
+ Performs data type check.
![[Pasted image 20231113193334.png]]

**Key Constraints** -> Represent by a underline of a attribute
![[Pasted image 20231113181645.png]]
+ Unique identify each tuples.
+ Superkey
	+ specify that no 2 tuples can have the same value
+ **Every relation has at least 1 superkey** -> set of all attributes.
#### Condition
1) Two tuples **cannot have identical values for all attributes in the key**.
![[Pasted image 20231113182137.png]]
2) It is a **minimal superkey**

**Candidate Keys** (More than 1 Key)
> Set of attributes that uniquely identify the tuples in  a relation.
+ A table may have multiple candidate keys, but one of them is chosen as the primary key.
+ The primary key is the selected candidate key that uniquely identifies each record in the table.

**Null Values**a
+ Specifies whether null values are permitted or not (NOT NULL).

**Entity Integrity Constraint** -> Primary Key is Null 
+ States that no primary key value can be null
![[Pasted image 20231113193507.png]]

**Referential Integrity Constraint:**
> When insert/update an item to a column making it unorder therefor violate
+ Specify between 2 ralations.
+ **States that a tuple in one relation that refers to another relation must refer to an existing tuple in that relation.**

**Dno called a foreign**
![[Pasted image 20231113192358.png]]

**Foreign key (FK):** (a key that connect outside of the table)
1) same domain (Exist in 2 or more tables)
2) Value of FK in a tuple either occurs as a value of PK
+ Table1[FK] = Table2[PK] or is null

### Operation/Dealing with Constraint Violations
![[Pasted image 20231113200044.png]]
> + Violate referential intergrity bc WORKS_ON tables connect to the primary table  EMPLOYEE.
> + In other word EMPLOYEE table (which created first) refer to WORKS_ON table. (created later)
> + Can delete EmplD = '1331' from WORKS_ON but not from EMPLOYEE.

### [[Relational Constraint Exercise]]