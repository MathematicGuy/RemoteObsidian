---
tags: Database
---
![[Pasted image 20231111082006.png]]
**3 Levels**
+ *INTERNAL LEVEL: physical storage*  
	Decribe complete detail how the data is stored and its physical path.
+ *CONCEPTUAL LEVEL(decribe by codes)*
	**Hides** the **details of the physical storage structure** 
		Concentrates on describing entities, data types, relationships, constraints, etc
+ EXTERNAL LEVEL - represent each user
	user level , the users basically

**Data Independence**
	The changed of data on the Internal schema doesn't effect other level
**Logical Data Independence**
	Modify the conceptual schema doesn't effect the external schemas or application programs
**Physical Data Independence**
	+ Ability to **modify the internal schema** without chhange the conceptual schema.
	+ Changes may be needed to improve performance.

f