
**TOTAL SUMMARY:** https://za.zalo.me/v3/verifyv2/pc?token=OsVpmDzwNmXX0VlAsXLMRcO1zxlP7KnoOGttlZG&continue=https%3A%2F%2Flearnsql.com%2Fblog%2Fsql-basics-cheat-sheet%2F

## [[SQL Code]]
## [[SQL tips and tool]]

## [[SQL Table Command]]

## [[SQL tips and tool]]


Strategy for implement SQL in project
	*Understand the basic and let the bot do the code for you*
Organize data in to Table
> **Each Row** represent individual record / Data point.
> Primary Key is its ID
> Save data point into Special column called : 
> 	Foreign Key -> TeamID
![[Pasted image 20230724101404.png]]
-> Goal: Structure data into its most Normolized Formed.


### Syntax
![[Pasted image 20230724101909.png]]

Select -> make a query for Column that you want.
![[Pasted image 20230724101956.png]]

![[Pasted image 20230724102029.png]]
> At a certain condition.

**In a Nutshell, SQL are**
![[Pasted image 20230724102503.png]]


SQL - Relational - can connect data through KEY.
No SQL - No Relational
![[Pasted image 20230814100346.png]]




#### Select a table then Join data from another table.
```sql
"Select element with student_id from score table "
SELECT `student_id`, firstName, lastName, label, student_score
FROM `score`
"join student_id column from student as stab"
INNER JOIN student as stab on stab.id = `student_id`
"join course_id column from course as ctab"
INNER JOIN course as ctab on ctab.id = `course_id`; a
```
![[Pasted image 20230817142405.png]]


