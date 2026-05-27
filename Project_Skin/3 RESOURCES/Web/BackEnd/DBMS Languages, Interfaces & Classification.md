**DDL (Data Definition Language)**
	Define the internal and conceptual schemas
**VDL (View Definition Language) -**
	To specify user views and their mappings to the conceptual schema.
	Ex: like using SQL to view data (a form of DML - Data Manipulation Language)
**Type of DMLs** 
+ **High-level (or non-procedural DML)**
	Specify complex database operations in a concise manner
	Also called **set-at-a-time DMLs (can retrieve many data statement at a time)**
		Lấy 1 phát hết luôn.
+ **Low-level (or procedural DML)**
	Embedded in a genral purpose programming language
	Also called **record-at-a-time (bc it use looping to retrieve record from a set of record)**
		Lấy từng cái 1 cho đến hết.
**Several criteria used to classify DBMS:**
+ Data model
+ Number of users
+ Cost of DBMS
+ Number of sites
+ Types of access path
+ Generality

 **Data Models:**
 **Relational data model**
![[Pasted image 20231111083758.png]]
**Object-oriented database model** -> see data as Object base


These 2 are not commonly use due to it complexity
**Hierarchical model:** represents data as tree structures.
![[Pasted image 20231111083643.png]]

**Network model:** represents objects and their relationships in the form of graph.
![[Pasted image 20231111083910.png]]

Number of Users
+ Single-user systems: supports only one user at a time.
+ Multiuser systems: supports multiple users concurrently.

DB are distributed over many sites