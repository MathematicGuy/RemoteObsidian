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

**Domain constraints**
+ Must be atomic value
+ Performs data type check

**Key Constraints** -> Represent by a underline of a attribute
![[Pasted image 20231113181645.png]]
+ Unique identify each tuples.
+ Superkey
	+ specify that no 2 tuples can have the same value
+ **Every relation has at least 1 superkey** -> set of all attributes.
Condition
1) Two tuples cannot have identical values for all attributes in the key.
![[Pasted image 20231113182137.png]]
2) It is a minimal superkey

**Candidate Keys** (More than 1 Key)
