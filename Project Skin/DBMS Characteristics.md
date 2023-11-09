**File System Approach** 
![[Pasted image 20231109091539.png]]
> Have to maintain different file because they have different interests + they have duplicated data (Roll_No + Name)
*one to one*

**BDSM Approach**
![[Pasted image 20231109091651.png]]
> Everything save in the responsitory and everybody use the data for their interest
*one to many*

**Chracteristics of DBMS Approach**
1) Self-Decribing Nature of a Database System
2) Insulation (cách biệt) between Programs and Data, and Data Abstraction
3) Support of Multiple Views of the Data
4) Sharing of Data and Multiuser Transaction Processing

**Self-Decribing Nature of a Database System**
	1) **Database system** -> Database + Meta-data (DB Definition)
		2) **Stored in:** DBMS catalog
			3) **Used by:** DBMS Software & Database Users
DBSM can work well with any number of database application

+ In constract file processing, data definition can only work with only one specific DB. Cannot connect parralel with many DB at the same time.

**Insulation between Programs and Data, and
Data Abstraction**
+ If any changed made in file -> bc the structure of data file is embedded in the application so the program also changed.
+ Structure of data files is store in DBSM catalog -> seperate from access program -> changes does not affect the program
	program-data independence

+ The chracteristoc that allow program-data independence is called data abstraction

**Support of Multiple Views of the Data**
