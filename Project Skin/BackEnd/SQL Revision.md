### Key

foreign key = links 2 table by a primary key
```sql
 CourseID INT FOREIGN KEY REFERENCES Courses(CourseID),
```

primary key - can be create by 2 fields to make a unique set of data which indentify a records in the table 

candidate key  - a key that can become primary key, a table can exist many but only 1  chosen to becoming primary key  
```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    SSN VARCHAR(11) UNIQUE, -- Social Security Number as a candidate key
    Email VARCHAR(100) UNIQUE, -- Email address as another candidate key
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    CourseID INT,
    GPA DECIMAL(3,2),
    CONSTRAINT UQ_StudentID_Email UNIQUE (StudentID, Email) -- Combined candidate key
);
```

constraint 

minimal sp key -> 1 column as key only

**Entity Integrity Constraint** -> ràng buộc toàn vẹn thực thể 

**Referential Integrity** -> toàn vẹn tham chiếu (Xóa 1 primary key trước khi xóa foreign key khiến cho tham chiếu trở nên vô lý)

### Example with Relational Albgebra Below

SELECT
```sql
select col1, col2 from table where condition
```
- Relational Algebra: 
	σ_condition(π_column1, column2(table))

ORDER BY
```sql
select col1, col2 from table order by col1 asc/desc
```

WHERE
```sql
select * from student where courseID = 2  
```

select distinct
```sql
select distinct(col1) from students
```
- Relational Algebra: 
	**π_column(table)**

AND
```sql
select * from student where courseID = 2 and student_number > 0
```
OR
```sql
select * from student where courseID = 2 OR  student_number > 0
```
- Relational Algebra ( and first or later)
	**σ_condition1(table) ⋀/⋁ σ_condition2(table)**

IN (if a element exist in a list of elements)
```sql
select * from table where studentID IN (StdID_LIST) 
```
- Relational Algebra: **σ_column=value1 ⋁ σ_column=value2 ⋁ ... (repeatly)**

NOT IN (opposite of IN)
```sql
select * from table where studentID NOT IN (StdID_LIST) 
```
- Relational Algebra: **π_column(table) - σ_column=value1 ⋁ σ_column=value2 ⋁ ...**

between

like

LIMIT

is NULL

Table & Column Aliases

OUTER JOIN

INNER JOIN (just Join) 

LEFT JOIN

RIGHT JOIN

Self Join

CROSS JOIN 

GROUP BY

HAVING

UNION 

EXCEPT

**AVG** (Aggregate Function)
AVG_sum(col) (table)
![[Pasted image 20231205120719.png]]

![[Pasted image 20231205122759.png]]
Tính tổng số h theo Dname -> Sum (Hours) từ table (WORKS_ON where Pno = Pnumber) Group by Dname

Find the maximun value from a table
![[Pasted image 20231205120837.png]]


![[Pasted image 20231205121342.png]]
note: Using **Aggragation function automatically group** the answer
![[Pasted image 20231205121412.png]]

Using Count and Distinct at the same time. (Applied 2 aggragate function) 
![[Pasted image 20231205121504.png]]


## Trigger and Procedure Exam
+ ! NULL value or not using JOIN.
Becaful when using JOIN. Pay attention if the column require NULL value (LEFT/RIGHT JOIN) or Not (INNER JOIN).


+ ! Be Specific when using Count
COUNT( * ) -> Count by 1 for everyrow that exist in the table
COUNT(Student.id) -> COunt by 1 for every student id that exist in the table


