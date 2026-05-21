[Key in RDB](https://youtu.be/_UZLrD_R0T4?si=2bShIa5jkrtPB0FT)
**Primary Key**
A primary is a single column value used to identify a database record uniquely.
+ It has following attributes
	- A [primary key](https://www.guru99.com/dbms-keys.html) cannot be NULL
	- A primary key value must be unique
	- The primary key values should rarely be changed
	- The primary key must be given a value when a new record is inserted.

**Composite Key**
> A composite key is a primary key composed of multiple columns used to identify a record uniquely.
![[Pasted image 20231129162312.png]]

**Candidate key**
> Is a Minimal super key. That mean no repetition Domain in Candidate key
> Ex:
> + {ID}, {SSN}, {ID, Name} -> ID repeat, False 
> + {Name, Phone}, {ID, Email} -> Minimal super key
![[Pasted image 20231114225214.png]]
> Candidate key is s selection of keys that can become super key.
>  + It can be the combination of key that make the Super Key. 
> 	 {Name, Phone}, {Name, Email}, {ID, SSN, Phone}, etc..
>  + Or can be 1 single key.
> 	 ID, SSn, Email

![[Pasted image 20231114230810.png]]
**Primary Key**
+ No duplication value in Primary key Domain
+ UNIQUE + Not NULL.
![[Pasted image 20231114230046.png]]
+ Candidate key with NULL value is NOT the primary key.

**Alternate key** -> Candidate key that not primary key (the left over candidate key)
Ex: 
+ Candidate Keys
	{ID}, {Age}, {Name}, {Class}
+ Primary Key
	{ID}
+ Alternate Keys
	{Age}, {Name}, {Class}

**Unique key** -> 100% Unique value bit can support NULL value
+ Candidate Keys:
	{ID}, {SSN}, {Name, Phone}, {Email}
+ Primary Key: {ID}
+ Alternate Keys:
	{SSN}, {Name, Phone}, {Email}, etc...
+ Unique Key
	{Name, Phone}, {Email}
+ Composite Key -> contain more than 1 attribute
	{Name, Phone}

**Foreign Key**
> This Intigrity constraint -> The Insertion in one Table is depending on the values to be validated in the other table.
![[Pasted image 20231114231048.png]]


