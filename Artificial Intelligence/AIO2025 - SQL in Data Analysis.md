### Datatype in SQL 
VARCHAR

![[Pasted image 20250619150142.png]]


## SQL Queries:
### Join operation (INNER, OUTER, SELF, MUTIPLE TABLES, COMPOUND, IMPLICIT) JOINs
+ $ **Mục đích** chung của JOIN là **để tạo 1 bảng mới từ việc nối các bảng khác qua việc nối các cột có cùng Datatype với nhau chứ không nhất thiết phải là Khóa chính hay khóa phụ**, dựa nối dựa 1 hoặc nhiều điều kiện đặt ra.
	Dù có thể nối bất kì Cột nào vs nhau, ta vẫn nên nối các khóa để đảm bảo sự chặt chẽ giữa các dự liệu. 
	 
+ ? Note: you can name Attribute by write another Variable next to it. e.g. `FROM EMPLOYEE e` -> *now EMPLOYEE table can be access as e.*  

`Example table:`
![[Pasted image 20250622142640.png]]

**INNER JOIN (like INTERSECTION)** -> return only the rows where the join condition is met in both tables 
```sql
-- Ignore all rows with DepartmentID == NULL 
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

**OUTER JOIN (like RIGHT, LEFT, FULL intersection)** -> return all rows (include NULL) where join condition is met in both table. 

*LEFT OUTER JOIN* return all records from the LEFT table (i.e. Employees) and the matched records from the RIGHT table by key even if the SELECT attribute is NULL. 
+ ? Display NOT NULL Attribute on the LEFT and Allow SELECT NULL attributes from the RIGHT table. 
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```
![[Pasted image 20250622144223.png]]

*RIGHT OUTER JOIN* like the LEFT JOIN, it's return all records in the RIGHT table (i.e. DepertmentName) and the matched records from the LEFT table by key even if the SELECT attribute is NULL. 
+ ? Display NOT NULL Attribute on the RIGHT and Allow SELECT NULL attributes from the LEFT table. 
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
RIGHT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```
![[Pasted image 20250622144211.png]]

*FULL OUTER JOIN* COMBINATION of RIGHT and LEFT JOIN. What ever uniquely in RIGHT and LEFT Join is in FULL OUTER JOIN. 
+ ? Display both NULL attributes from LEFT and RIGHT. 
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```
![[Pasted image 20250622144434.png]]


**SELF JOIN**  (join using 1 attributes) -> Nối để truy vấn giá trị trong chính bảng đó. 
	e.g1. Trong *bảng company* có 2 cột là *employee_id và id manager_id. Biết rằng quản lý cũng là nhân viên của công ty đó, để biết ai quản lý của nhân viên có id 001* thì ta ghép bảng với chính nó dựa trên employee_id và manager_id. ![[Pasted image 20250622135921.png]]
**JOINNING MULTIPLE TABLES** (join using 1 attributes)
+ $ Joining multiple table by attributes of the current table, so you can joining as many table as you want as long they have the same attributes. (e.g. name, id, boolean, etc..) ![[Pasted image 20250622140445.png]]
	
**COMPOUND JOIN CONDITION** (join using 1 attributes)
+ ? When ? When the **Table's Primary Key comprised of 2 prime attributes. Yeah, it a Composite Primary Key**, this mean we need both columns to iniquely identify a record. 
+ ! **Problem:** Need 2 tables with both ids. **Simply, JOIN tables by COMPOSITE KEY.** 
	e.g.  **Both table 1 and 2** need to have `order_id` and `product_id` 
	![[Pasted image 20250622141622.png# left| 300]]![[Pasted image 20250622141637.png# left| 250]]
```sql
USE sql_store;
SELECT *
FROM order_items o
JOIN order_item_notes n
	ON o.order_id = n.order_id
	AND o.product_id = n.product_id;
``` 
![[Pasted image 20250622144623.png# left]]
	
**IMPLICIT JOIN** (not recommend because it prone to error, consider its a legacy/old syntax)
+ ? IMPLICIT mean not directly, not clear, ambiguity. 


**USING Clause** -> Use to **simplify SQL** JOIN statement. **JOIN only happend between pair of tables.** This allow us to simplify SQL syntax with **USING clause where both column of the JOIN condition have the same name**.  
	Note: Multiple join is just joining 2 tables to create a new table, then continue to JOIN it with another table. 
```sql
...
FROM customer c
JOIN order o
	ON c.customer_id = o.customer_id -- both table join by customer_id
ORDER BY c.customer_id
```
simplify with `USING` clause
```sql
... 
FROM customer c
JOIN order o 
	USING (customer_id) 
ORDER BY c.customer_id
```
+ ? another example ![[Pasted image 20250622152706.png]]

**UNION** 
+ $ UNION **when you want to add new Attribute (i.e. column) by condition without DUPLICATE.** This help to consolidate your data when there're multiple duplicate. 
	+ Note: `UNION` remove duplicate *by default*, `UNION ALL` don't.  
+ ! The datatype of the corresponding (UNION) *column must be compatible* (e.g. you can union `VARCAR` with `CHAR` *or* an `INT` with an `DECIMAL`) 
+ ? *Example, to align each user Tier by points*. < 2000 point as Bronze or between 2000 to 3000 point as Silver and > 3000 as Gold.  ![[Pasted image 20250622153848.png]]
	Note: Apply **UNION after Query**, not before.  ![[Pasted image 20250622153340.png]]
	**Result after apply UNION:** ![[Pasted image 20250622153811.png# left]]

+ ? Example 2: *Consolidate Data by Removing Duplicate*
![[Pasted image 20250622155354.png# left | 600]]
+ ? *Preserve Duplicate*
![[Pasted image 20250622155416.png# left|600]]


### Common Table Expression (CTE)
**Application 0:** set query as a variable where you can retrieve that same table without re-write the whole query. 
+ $ The `WITH` clause defines a CTE name `AvgSalaryByDept`
```sql
WITH AvgSalaryByDept AS (
    SELECT Department, AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY Department
)
SELECT *
FROM AvgSalaryByDept; -- call query by name, much versatile
```

**Application 1:** set query as function with Input and Output
```sql
WITH
  cteReports (EmpID, FirstName, LastName, MgrID, EmpLevel)
  AS
  (
    SELECT EmployeeID, FirstName, LastName, ManagerID, 1
    FROM Employees
    WHERE ManagerID IS NULL
    UNION ALL
    SELECT e.EmployeeID, e.FirstName, e.LastName, e.ManagerID, 
      r.EmpLevel + 1
    FROM Employees e
      INNER JOIN cteReports r
        ON e.ManagerID = r.EmpID
  )

SELECT
  FirstName + ' ' + LastName AS FullName, 
  EmpLevel,
  (SELECT FirstName + ' ' + LastName FROM Employees 
    WHERE EmployeeID = cteReports.MgrID) AS Manager
FROM cteReports 
ORDER BY EmpLevel, MgrID 
```
+ ? Like every other programming language, function allow recursion to happend. To avoid infinite recursion SQL set recursion limit to 100 by default, but you can customize it using `MAXRECURSION` hint:
```sql

OPTION(MAXRECURSION 50)
```
+ ? Like Python, CTE exists only during the execution of the query. CTE is discarded once the query completes. 

### Subqueries
+ $ Subqueries **allow to use a query as a variable Inside another query**, hence the name Subqueries. ![[Pasted image 20250622162150.png]]This help save time when your Queries is small since you don't have to join 2 or some tables for a simple Query.  


```ad-warning
Both **CTE and Subqueries both have the same problem.** It **have to re-evaluate all of ours query every time we run it**. As we know, CTE only exist during the executin of a single query, this mean we can only call a CTE once per execution. 

What if we need that Subquery multiple time ? -> Performanace issue
```

### Temp Table
+ $ **A simple solution is to SAVE the query's result** using `TEMPORARY TABLE`. Basically its act like a Storage.

**Step 1:** Create the Storage to allow re-accessability. 
![[Pasted image 20250622163102.png| 400]]
**Step 2:** Insert Data into Temp Storage using Subquery and INSERT like you always do for table in SQL. 
![[Pasted image 20250622163227.png| 400]]

```ad-caution
Its is super useful when subquery involve heavy calculation, we only have to save it once for **unlimited use in 1 SESSION** (i.e. each time you connect to the database and make query). **Once the session is close, temp table will be delete.**
```

### QUESTION: using CTE's `WITH` clause for CREATING and INSERTING Data 
+ $ What about we create function using `WITH` that "create a new table with *no relationship* and inserting new data into it."   
+ ! The reason is, `WITH` is only compatible with a certain SQL function like `SELECT`, `INSERT`, `UPDATE` and `DELETE` statement, not `CREATE`. *However there a workaround* to  this by seperate INSERT and CREATE table query, *but*
```sql
-- Define a virtual table
WITH CTE_Sample AS (
    SELECT 1 AS ID, 'D' AS Name
    UNION ALL
    SELECT 2, 'Tina'
)

-- Use it to create a permanent table
CREATE TABLE MyPermanentTable AS (SELECT * FROM CTE_Sample);
```
1) SQL Server will return ERROR if we use `WITH` and `INSERT` as a subquery for `CREATE`. This only work in PostgreSQL.
2) `WITH` clause **LIMITED** the function capability. 
	+ You can't reuse this logic without copy-pasting the query. 
	+ You can't add control flow like `IF`, `LOOP` and `EXCEPTION`
		*Without control flow, you can't insert more data later from the CTE* (it disappears after the query)
	
### Stored Procedures
+ ? We know that each *CTEs can only be execute once as subquery* and *TempTable running at Session level.* 

[What the difference between Procedure and WITH clause CTE](https://www.google.com/search?client=firefox-b-d&channel=entpr&q=what+the+differenece+between+Prodedure+and+WITH+clause+CTE+)
[ChatGPT](https://chatgpt.com/c/6857e0a3-ab70-8007-b813-9de183167fe1)
[HW](https://docs.google.com/forms/d/e/1FAIpQLSd0NXDMFs9A8mO983dRHE6DFCE8QUFkuz8-xYjBatRTx4koDg/viewform)
[Zoom Video](https://zoom.us/rec/play/QmIM36G5miOEKrLzaqx-VuS-bEUv3NE1iNEPdf9rzRkQi4800BYKpAtwQBPzAX8yAZTA-sDdttYrti0E.RJsGf2VTrpRWG23r?eagerLoadZvaPages=&accessLevel=meeting&hasValidToken=false&canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2F7oBuN1J3iQwkp-SjKAl9kqoD4o6pMPsMIhtdirCwKIKTgUEkhpJd32zYpCeZ2Wi5.tnqJZzlW1p8Perjo)
[Slides](https://aivnlearning.edu.vn/api/files/68317ac3519c0e157fb5148a/Documents%2F2025-5%2FM01W03%20-%20Database%20-%20SQL%20(3)%2FAIO2025_SQL3_v3.pdf)


+ *Trigger (if this event happened -> trigger another event to happend), Trigger Validation* **(IMPORTANT)**
+ PRACTICE SECTION. 

Data Analyst SQL Queries
![[Pasted image 20250619150505.png]]

**Extra:** RECURSIVE in SQL, Data Mining. 

