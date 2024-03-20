source: https://youtu.be/5OdVJbNCSso?si=d81elQsUp3hp_XQr

**SQL Learning Tools**
	[SQL Zoo](https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial)
		SQL quizizz
	[SQL Bolt](https://sqlbolt.com/)
		Interactive Lesson | All within Browser
	[Mode](https://mode.com/sql-tutorial/) 
		Learn to answer question with data using SQL
		Level: Beginner - Intermediate - Advance
	[MySQLTUTORIAL](https://www.mysqltutorial.org/) 
		Make SQL Easy & Fun
		SQL Notes with Practical Example 
	[SQL Murder Mystery](https://mystery.knightlab.com/)
		Hones your SQL Problems solving 
	[Data View - DB for Obsidian](https://youtu.be/i_q4cXhhaqg?si=LMJowSWcQ55Ea_rY) 
		Dynamic Data Query in Obsidian
	[DrawSQL - DB View and Design](https://drawsql.app/teams/3-bowls-of-rice/diagrams/student-score-management-db) 

**SQL tables:**
+ [[Company DB]]
+ [[DB Users]]
+ [[Std_ManagementDB]]
+ [[Movie_DB]]
+ [[jobDB]]

---

Priority single collin in SQL: '  ' not " "
Column - Field
Row - Recordw

### USEFUL SQL RULES
- **Order of Operations:** SQL follows an order of operations, similar to mathematical expressions:
    
    1. FROM and JOINS
    2. WHERE
    3. GROUP BY
    4. HAVING
    5. SELECT
    6. ORDER BY

+ **WHERE vs. HAVING: Key Differences**    
    - **WHERE:** Filters individual rows _before_ grouping takes place.
    - **HAVING:** Filters groups of rows _after_ grouping and aggregate functions have been applied.
+ Query are read from Bottom to Top
+ Number field group by another field are group by as sum.
+ To get number output we have to add a `.0`
```sql
Select (309 + 517 + 304 + 282) / 6366.0; --without .0 nothing will appear
```
+ ! Cannot use Aggregate functions in WHERE clause. (The example below will cause Error)
	Ex: select * from employees where salary > AVG(salary) GROUP BY employee_id


Create Data Base
```sql
-- 1) Create DB
create DATABASE myShop;
-- 2) Select DB
use myShop;
-- 3) Select a Table Name
select DB_NAME()
-- 4) Create the table in the specified schema
CREATE TABLE users
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    full_name varchar(50) NOT NULL,
    email varchar(50) NOT NULL
    -- specify more columns here
);
GO
-- 4) Insert
INSERT INTO users
(id, username, email)
VALUES
(   
    1, 'Elong Mask', 'maskElon12@gmail.com' 
),
(   
    2, 'Bill Stone', 'billmak122@gmail.com' 
),
(   
    3, 'Alternative Man', 'alterman@gmail.com' 
)
GO
-- 5)  
```


work for mySQL
```sql
CREATE TABLE employees (
	employee_id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	hourly_pay DECIMAL(10, 2), 
	hire_date date,
);
```
+ ? **DECIMAL(10, 2)**: means that you're declaring a decimal number that can have a **total of 8 digits**, with **2 of these digits after the decimal point**.


work for phpMyAdmin
> Need " reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP " to run.
```sql
CREATE TABLE employees (
	employee_id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	hourly_pay DECIMAL(10, 2), 
	hire_date date,
   reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
```

SELECT TABLE
```sql
SELECT * FROM employees
```
![[Pasted image 20230814105526.png]]

SELECT TOP(1)
```sql
select TOP(1) @new_mgr_id = manager_id from employees WHERE manager_id <> @mgr_id;
```


RENAME Table or DROP the TABLE 
```sql
RENAME TABLE employees TO workers;
DROP TABLE employees;
```
RENAME in 1 line
```sql
EXEC sp_rename 'deletedEmployee', 'delEmps';
```

DROP KEY
drop employees FK that reference to department PK
```sql
ALTER TABLE employees DROP CONSTRAINT fk_department_id;
```


ALTER TABLE (Modify Table) 
> All ALTER Command below must goes with ALTER TABLE command
```sql
ALTER TABLE DEPT_LOCATIONS
```

ALTER TABLE - Change Field Name
```sql
ADD phone_number VARCHAR(20);
RENAME COLUMN phone_number TO email;
```
![[Pasted image 20230814114906.png]]
```sql
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100);
```
![[Pasted image 20230814114948.png]]

ALTER TABLE - Set Primary Key 
```sql
-- Assume you have a table called DEPT_LOCATIONS
-- with columns Dnumber and Dlocation
ADD CONSTRAINT PK_DEPT_LOCATIONS PRIMARY KEY (Dnumber, Dlocation);
```
ALTER  TABLE  - Change Field Data Type
```sql

ALTER COLUMN Dlocation VARCHAR(255) NOT NULL;
```


MOVING COLUMN AROUND
	FIRST <-> AFTER  
```sql
ALTER TABLE employees
MODIFY email VARCHAR(100)
AFTER last_name;

SELECT * FROM employees;
```
![[Pasted image 20230814115226.png]]
```sql
ALTER TABLE employees
MODIFY COLUMN phone_number 
VARCHAR(20) FIRST;
```

ALTER TABLE ADD COLUMN (FIELD)
```sql
ALTER TABLE jobs
ADD hours_salary INT NULL;
```
COLUMN DATATYPE to NULL(able)
```sql
-- Alter the table to make deletion_timestamp nullable
ALTER TABLE deletedEmployee ALTER COLUMN deletion_timestamp datetime NULL;
```

DELETE ROW
```sql
DELETE FROM employees WHERE employee_id = 201;
```

DROP COLUMN ( *Delete Column* )
```sql
ALTER TABLE employees
DROP COLUMN email;

SELECT * FROM employees;
```

DELETE WHOLE TABLE
```sql
TRUNCATE TABLE table_name
```
+ Replace `table_name` with the name of your table. This statement will remove all records from the table.

![[Pasted image 20230814120418.png]]

To INSERT  Multiple Row at once.
```sql
INSERT INTO employees
VALUES (2, "Adam", "Smasher", 20000, "1998-04-26"),
	    (3, "Spinse", "SquareJean", 12.44, "2023-03-04"),
	    (4, "Sandy", "Cheek", 12.33, "2023-01-06");
SELECT * FROM employees
```
the table might look like this
![[Pasted image 20230814120741.png]]

So What happend if there're datas missing.  It's may cause error
But if input item are pre-defined. Blank block will just value as null.
(List the name of the column you want to insert)
![[Pasted image 20230814120948.png]]

SELECT (like info QUERY )
// select info at 1
```sql
SELECT first_name, last_name;
SELECT last_name, first_name;
FROM employees;

WHERE employee_id = 1; 
```

// return Obj (row) with hourly_pay >= 15
```sql
SELECT *
FROM employees
WHERE hourly_pay >= 15;
WHERE hoursly_pay != 15; 
```

```sql
WHERE hire_date IS NULL
```
![[Pasted image 20230814121723.png]]

**UPDATE DATA** (Change Field and Record Value)
 ```sql
UPDATE employees
SET hourly_pay = 10.25
WHERE employee_id = 6;

SELECT * FROM employees
```
![[Pasted image 20230814121959.png]]



Bug4: Không cộng hết số
![[Pasted image 20230830221531.png]]


SORT TABLE
![[Pasted image 20230911121716.png]]


KEY
PRIMARY KEY -> make sure only of that data exist. Unique
![[Pasted image 20231003135844.png]]
FOREIGN KEY -> Link 2 Table prevent any action destroy the link between them. 
> note: foreign key itself cannot have its own foreign key. 
> + A foreign key must connect to a primmary key
> + If cannot connect foreign key, re-check if you are connect to a primary key (caution for duplicate value, it not a primary key)
![[Pasted image 20231003135913.png]]
```sql
CREATE TABLE transaction (
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
	amount DECIMAL(5,2),
	trans_customer_id INT,
	-- add and connect foreign key to the primary key
	FOREIGN KEY (trans_customer_id) REFERENCES customers(customer_id),
)
```
or you can **add foreign key later with this**
```sql
ALTER TABLE transactions
ADD CONSTRAINT fk_customer_id
FOREIGN KEY(trans_customer_id) REFERENCES customers(customer_id)
```

SELF-REFERENCING FOREIGN KEY
	Foreign key that reference the Primary Key of it's Table
```sql
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    manager_id INT,  -- This references the employee_id of the employee's manager
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);
```

ORDER BY (kind of like SORT) - can sort Date
```sql
SELECT * FROM employees
ORDER BY last_name DESC;
ORDER BY last_name ASC;
```

```sql
SELECT * FROM transactions
ORDER BY amount;
```
![[Pasted image 20231003140555.png]]


UNION -> merge
	To Join **2 Table** together. They must **Have The Same Number Of Column**
```sql
SELECT f_name, l_name FROM employees;
UNION
SELECT f_name, l_name FROM customer;
```
notice:
+ UNION -> don't take Duplicates (just 1/1)
+ UNION ALL -> take all Duplicates

CONCAT -> Connect 2 String together
+ ! Use ' ' for space not " "
 >  a.f_name -> select f_name from table a
```sql
CONCAT(b.f_name, ' ', b.l_name) AS "referred_by"
```
![[Pasted image 20231003141638.png]]
+ CONCAT to merge elements together (connect string with number, etc...)
```sql
select name, 
CONCAT(
ROUND(
       (population/
           (select population 
                   from world 
                   where name = 'Germany'))*100
            ),'%')
as percentage
from world 
where continent = 'Europe' 
```
![[Pasted image 20231128153152.png]]

### **[[SQL JOIN]]**  
[[JOIN Tables]]
note: JOIN doesn't have to have condition, but RIGHT/LEFT JOIN must have condition 
+ ? Why using Join but not CASESIAN product
```sql
select * from jobs, regions
```



**JOIN** (INNER JOIN)
>-- join another table to itself
>-- used to compare rows of the same table
>-- helps to display a heirarchy of data
```sql
SELECT *
FROM customers AS a
INNER JOIN customers AS b /*basically copy and paste the horizontally*/
ON a.referral_id = b.customer_id
```
![[Pasted image 20231003142200.png]]
```sql
SELECT a.customer_id, a.first_name, a.last_name,
		CONCAT(b.f_name," ", b.l_name) AS "referred_by"
FROM customers AS a
INNER JOIN customers AS b
ON a.referral_id = b.customer_idff
```
![[Pasted image 20231003141924.png]]

Example Table
![[Pasted image 20240314090233.png]]
**LEFT JOIN**
> Get all matching valid value, 
> but left the unmatching valid only on the left and null on the right.
```sql
SELECT Employees.EmployeeID, Employees.Name, Departments.DepartmentName
FROM Employees
LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```
+------------+---------+--------------+
| EmployeeID | Name    | DepartmentName |
+------------+---------+--------------+
| 1          | Alice   | Sales         |
| 2          | Bob     | Marketing     |
| 3          | Charlie | Sales         |
| 4          | David   | NULL          |
+------------+---------+--------------+


**RIGHT JOIN**
> Same as left join but reverse
```sql
SELECT Employees.EmployeeID, Employees.Name, Departments.DepartmentName
FROM Employees
RIGHT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```
+------------+---------+--------------+
| EmployeeID | Name    | DepartmentName |
+------------+---------+--------------+
| 1          | Alice   | Sales         |
| 2          | Bob     | Marketing     |
| 3          | Charlie | Sales         |
| NULL       | NULL    | HR            |
+------------+---------+--------------+


**FULL JOIN**
> Left JOIN first
> the RIGHT JOIN

**UNION**
> **Merge Data** from 2 tables **without duplicate.**
> or
> **Combine date** from 2 table **into 1 field and ignore the duplicate.**
![[Pasted image 20231130143728.png]]
```sql
SELECT age
FROM teacher
UNION
SELECT age
FROM student;
```

**UNION ALL**
> Conbine all data into 1 field.
![[Pasted image 20231130143748.png]]
```sql
SELECT age
FROM teacher
UNION ALL
SELECT age
FROM student;
```

**CROSS** (CROSS JOIN) (Tổng đề các nhưng là 1 bên)
**A x (C, D)** và **B x (C, D)**
![[Pasted image 20231130144011.png]]


**GROUP BY**
*note: GROUP BY is unnescessary if already using WHERE*  

= aggregate all rows by a specific column
-- often used with aggregate functions
ex. SUM(), MAX(), MIN(), AVG(), COUNT()
```sql
SELECT SUM(amount), order_date
FROM transactions
GROUP BY order_date;
```
Tính SUM của amount tại giá trị order_date -> Tính tổng của amount vs  order_date giống nhau.
> Total amount of $ in that Date
![[Pasted image 20231003143259.png]]
 (Replace SUM by MAX we have)
 MAX amount of that Date  -> giá trị cao nhất tại amount, với order_date tương ứng
![[Pasted image 20231003143335.png]]
 (Replace SUM by COUNT we have total Event trigger on that Date -> đếm amount có cùng order_date
![[Pasted image 20231003143521.png]]


```sql
SELECT SUM(amount), customer_id
FROM transactions
GROUP BY order date;
```
> total $ those customer had spended
![[Pasted image 20231003143659.png]]

notice: **When using GROUP BY use HAVING for WHERE statement. (replace WHERE as HAVING)** 
![[Pasted image 20231003143811.png]]


GROUP BY with ORDER BY
```sql
select continent, name from world group by continent order by name asc
```
> group first then order


**[GROUP BY with SUM](https://learnsql.com/blog/case-when-with-sum/)**
```sql
SELECT 
  department,
  SUM (CASE
    WHEN number_of_lectures > 20 THEN 1
    ELSE 0
  END) AS mandatory_subjects,
  SUM (CASE
    WHEN number_of_lectures <= 20 THEN 1
    ELSE 0
  END) AS elective_subjects
FROM subject
GROUP BY department;
```


**IN**
> The `IN` operator **allows you to specify multiple values** in a `WHERE` clause. 
```sql
SELECT name, population FROM world WHERE name IN ('FRANCE', 'Germany', 'Italy');
```

The expression **subject IN ('chemistry','physics')** can be used as a value - it will be **0** or **1**. 
**Show the 1984 winners and subject ordered by subject and winner name; but list chemistry and physics last.**
```sql
SELECT winner, subject, subject IN ('physics','chemistry') 
  FROM nobel
 WHERE yr=1984 
 ORDER BY subject IN ('physics','chemistry') ASC
```
![[Pasted image 20231122103231.png]]

**sth%** - **%sth%**
+ ? % represent 0, 1 or all the rest of the string. Or something
**Select only a:**
+ ?  %a% mean sth contain a. 
> use this when you try to search a word start with ...
```sql
SELECT name FROM world WHERE name LIKE 'United%'
```

**SUBSTRING**
```sql
SUBSTRING(string, position, number_of_characters) = 'a'
```
+ The string from which to extract the substring.
+ The position to start extraction. The position of the first character is 1.
+ The number of characters to extract.
```sql
SELECT (me.last_name + ' ' + me.first_name) as 'Employee',
        (e.last_name + ' ' + e.first_name) as 'Employee',
        e.department_id, e.salary from employees as e 
JOIN employees as me ON e.manager_id = me.employee_id
WHERE SUBSTRING(e.last_name, 2, 1) = 'a'
COLLATE Latin1_General_100_BIN2;
```

+ select the first name seperate by a space ' '
```sql
SELECT name FROM world WHERE name LIKE '% %';
SELECT SUBSTRING_INDEX(name, ' ', 1) AS first_name FROM world WHERE name LIKE '% %';
```
+ select the employee last name that have second letter as a
```sql
SELECT  (me.last_name + ' ' + me.first_name) as 'Employee',
        (e.last_name + ' ' + e.first_name) as 'Employee',
        e.department_id, e.salary from employees as e 
JOIN employees as me ON e.manager_id = me.employee_id
WHERE SUBSTRING(e.last_name, 2, 1) = 'a'
COLLATE Latin1_General_100_BIN2;
```


**XOR**
> not >> or << but always ><
```sql
SELECT name, population, area FROM world WHERE (area > 3000000 AND population < 250000000) OR (area < 3000000 AND population > 250000000) 
```

[ROUND(f,p)](https://sqlzoo.net/wiki/ROUND)
>returns f rounded to p decimal places
```sql
SELECT name, ROUND(population/1000000, 2), ROUND(gdp/1000000000, 2) FROM world WHERE continent = 'South America'
```
> The number of decimal places *may be negative*, this will round to the **nearest 10 (when p is -1)** or **100 (when p is -2)** **or 1000 (when p is -3)** etc..

[LENGTH](https://sqlzoo.net/wiki/LENGTH)
```sql
SELECT name, capital
  FROM world
 WHERE LENGTH(name) = LENGTH(capital)
```

**<>** is just **=!**
> You an use `<>` as the **NOT EQUALS** operator.
> Ex: (name <> capital) 


LIKE (**Use To Find Pattern**)
> contain sth. Must goes along with % symbol '%sth', 'sth%', '%sth%'
> E.g. '%Smith' -> sth end with Smith, 
```sql
SELECT winner FROM nobel
 WHERE winner LIKE 'John%'
```
> Show the winners with first name John

NOT LIKE 
> exclude characters from your results. The ex above exclude a
```sql
SELECT name
FROM world
WHERE name LIKE '%a%' // name include a
    AND name LIKE '%e%' 
    AND name LIKE '%i%' 
    AND name LIKE '%o%' 
    AND name LIKE '%u%'
    AND name NOT LIKE '% %';
```
**ORDER BY**
Ex: List the winners, year and subject where the winner starts with *Sir*. Show the the most recent first, then by name order.
```sql
SELECT winner, yr, subject
FROM nobel 
WHERE winner LIKE 'Sir%' ORDER BY yr DESC, winner;
```
>  + date_column DESC sorts the records in descending order based on the date (most recent first)
> +  name_column is used for secondary sorting in ascending  order (alphabetical order).

**SELECT DISTINCT**
> Inside a table, a column often contains **many duplicate values;** and sometimes you **only want to list the "different" values.**
```sql
(SELECT DISTINCT yr FROM nobel WHERE subject = 'Medicine')
```
> Select all the distinct year of medicine subject

```sql
SELECT COUNT(yr)
FROM nobel
WHERE yr NOT IN (SELECT DISTINCT yr FROM nobel WHERE subject = 'Medicine');
```
```plaintext
+-------+
|  yr   |
+-------+
| 2000  |
| 2001  |
| 2001  |
| 2002  |
| 2002  |
| 2003  |
+-------+
```
> Count **all the year** but **Exclude all distinct year of medicine** subject 

```sql
SELECT COUNT(DISTINCT yr)
FROM nobel
WHERE yr NOT IN (SELECT DISTINCT yr FROM nobel WHERE subject = 'Medicine');
```
> Count **all distinct year** but **Exclude all distinct year of medicine** subject 
```plaintext
+-------+
|  yr   |
+-------+
| 2000  |
| 2001  |
| 2002  |
| 2003  |
+-------+
```

Select Only Year from Date data type
```sql
select distinct Year(birth_date)
from patients
order by birth_date asc;
```


**GROUP BY**
> **groups rows** that have the **same values into summary rows**, like "find the number of customers in each country".
+ The `GROUP BY` statement is **often used with aggregate functions** (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) to group the result-set by one or more columns.

Change Table Name
```sql
EXEC sp_rename 'employee_1stName', 'EMPLOYEE_2ndName';
select * from EMPLOYEE_2ndName
```

**ANY** (return **True** if any **subquery meet the condition**)
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
  (SELECT column_name
  FROM table_name
  WHERE condition); 
```


**ALL command** (act like **IF statement**)
```sql
SELECT ALL column_name(s)
FROM table_name
WHERE condition; 
```
**ALL with WHERE or HAVING**
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL (
        FROM table_name
        WHERE condition
);
```

> Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show **name**, **continent** and **population**.
+ Think of this like a for loop with if statement
```sql
-- select all the continent that satisfy the condition 
(select continent from world 
	 -- select if the contries have population <= 25000000
    where population = ALL (
    select population
    from world
    having population <= 25000000)
)
```

+ Quizz: Three tinme bigger
```sql
SELECT name, continent from world x
where (population/3) > ALL (
      select population 
      from world y where x.continent = y.continent
      and x.name != y.name
);
```
> "and x.name != y.name" because the
> **Biggest contry can only Large than 3, but not more than 3 compare to itself**  

**PROCEDURE**
> Stored Procedure = save SQL code to a Function (yea, like function in python) 
Advantaged:
	+ reduce network traffic
	+ secure, admin can grant permisson to use
	+ increase memory usage of every connection
```sql
DELIMITER $$
CREATE PROCEDURE find_customer (
	IN f_name VARCHAR(50),
	IN l_name VARCHAR(50)
)
BEGIN
	SELECT *
	FROM customers
	WHERE first name = f_name AND last_name = l_name;
END
```
Call the Procedure
```sql
CALL find_customer("Larry", "Lobster");
```


**PROCEDURE IN VSCode SQL**
Create a procedure output the avg employees salary from an department (department_id)
+ ! Prodecure Query have 2 Component
**main query**
```sql
SELECT AVG(salary) as avg_salary FROM employees WHERE department_id = @deparment_id;
```
**procedure template** (think this like a function) 
+ ? Procedure can be ALTER just like a table. (sometime ALTER can be use to run the query)
+ Or use both CREATE and ALTER
```sql
CREATE OR ALTER PROCEDURE get_customer_salary (@deparment_id INT)
AS BEGIN
	-- put your SQL query here
END
```
like python
```python
func hello(name):
	print('hello', name)
```

Final Result
+ ! The Procedure should be the 1st query. If there're any query above it add Go 
```sql
GO

CREATE PROCEDURE get_customer_salary (@deparment_id INT)
AS BEGIN
    SELECT AVG(salary) as avg_salary FROM employees WHERE department_id = @deparment_id;
END

get_customer_salary 8; -- OR EXEC get_customer_salary 8;
GO -- Remeber to add Go at the end to run the query
```

**PROCEDURE Example**
+ ? Create the Procedure to Update employee salary and department_id
```sql
CREATE OR ALTER PROCEDURE Gehalt_und_AbteulungsID_aktualisieren (@emp_id INT)
AS BEGIN
    DECLARE @emp_salary DECIMAL(8, 2);
    select @emp_salary = salary
    from employees
    where department_id = 2    
    
    IF (@emp_salary != 4800) 
    BEGIN
        UPDATE employees SET department_id = 6 WHERE employee_id = 107
        UPDATE employees SET salary = 4800 WHERE employee_id = 107
    END
END
```
+ ? Test the PROCEDURE
```sql
use jobDB; -- use jobDB database
-- Update salary from 4800 to 9000 to test the procedure
UPDATE employees SET salary = 9000 WHERE employee_id = 107; 
-- select table before the procedure was trigger 
select employee_id, salary, department_id as 'dep2 salary' from employees where employee_id = 107
-- Trigger the procedure
EXEC Gehalt_und_AbteulungsID_aktualisieren 107;
Go
```


**COALESCE** (Liên kết)
+ **Retrieve the first non-null expression among its arguments**.
	It is particularly handy when you have multiple columns or values and want to retrieve the first non-null one.
+ **and return NULL if all values are NULL.**

```sql
SELECT FirstName, COALESCE(MiddleName, '') AS MiddleName, LastName
FROM Employee;
```
>In this example, if `MiddleName` is null, the `COALESCE` function will return an empty string (`''`). **This ensures that you always get a non-null value for the middle name in your result set.**
| FirstName | MiddleName | LastName |
|-----------|------------|----------|
| John      |            | Doe      |
-> **COALESCE provides a Robust way to handle NULL values in more controlled manner.** 



**Create 1 table by joinning 2 tables**
> Đây là quy trình chung để thêm một bảng mới, vốn là kết quả từ hoạt động JOIN, vào cơ sở dữ liệu:

+ **1. Tạo bảng tạm thời (Temporary Table):**
	- Thực hiện câu query JOIN của bạn.
	- Dùng `SELECT ... INTO temp_table FROM ...` để lưu kết quả trực tiếp vào một bảng tạm thời. Bảng này chỉ tồn tại trong phiên làm việc hiện tại.
**Ví dụ:**
```sql
SELECT customers.customer_name, orders.order_date
INTO temp_customer_orders -- Tên bảng tạm thời
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```


+ **2. Chuyển bảng tạm thời thành bảng vĩnh viễn:**

	- Sử dụng `CREATE TABLE AS` để tạo một bảng mới dựa trên cấu trúc của bảng tạm thời.
	- Bảng mới này sẽ tồn tại kể cả sau khi bạn đóng phiên làm việc.
**Ví dụ:**
```sql
CREATE TABLE customer_orders AS
SELECT * FROM temp_customer_orders; -- Sao chép dữ liệu 
```

SAVE query as a temporary table and use it to calculate later
```sql
-- Find the scores of high-scoring titles
WITH high_scoring_titles AS (
    SELECT title, MAX(score) as max_score
    FROM hacker_news
    GROUP BY title
    HAVING MAX(score) > 200
)
-- Calculate the percentage
SELECT SUM(max_score) / (SELECT SUM(score) FROM hacker_news) * 100 as percentage
FROM high_scoring_titles;
```


**Extract Date and Time in SQL****
**For `strftime(__, timestamp)`:

- `%Y` returns the year (YYYY)
- `%m` returns the month (01-12)
- `%d` returns the day of the month (1-31)
- `%H` returns 24-hour clock (00-23)
- `%M` returns the minute (00-59)
- `%S` returns the seconds (00-59)

if `timestamp` format is `YYYY-MM-DD HH:MM:SS`.
```sql
select timestamp, strftime('%H:%M:%S', timestamp) 
from hacker_news 
group by 1 limit 10;
```


**Select only from letter** 
+ ? Select all letter both Uppercase and Lowercase
```sql
select * from employees
where last_name LIKE '%[a-z]%'
```

+ ? select only Lowercase or Uppercase 
```sql
select * from employees
where last_name LIKE '%[a-z]%'
COLLATE Latin1_General_100_BIN2;

-- uppercase only
select * from employees
where last_name LIKE '%[A-Z]%'
COLLATE Latin1_General_100_BIN2;

-- only uppercase 'G'
select * from employees
where last_name LIKE '%G%'
COLLATE Latin1_General_100_BIN2;
```


### Select field by number (Easier way to select collumn)
```sql
select strftime('%H', timestamp) as 'time_stamp',
  avg(score),
  count(*) as 'total story'
from hacker_news 
group by 1
order by 2 desc -- make the time_stamp column not group all together since they're number'
```
Line 1: GROUP BY 1
+ Purpose: This line groups the results of the query based on the value calculated in the first SELECT clause.
    
+ "1": In this context, the number '1' refers to the first column in the SELECT statement, which is the extracted hour from the timestamp (strftime('%H', timestamp) as 'time stamp').
	
+  Effect: The query will calculate average scores and total stories for each unique hour found within the timestamp column.

Line 2: ORDER BY 2 DESC
+ Purpose: This line sorts the results of the query.
	
+ "2": The '2' refers to the second column in the SELECT statement, which is the average score (avg(score)).
 DESC: This indicates the sorting will be in descending order (highest average scores first).
```sql
select strftime('%H', timestamp) as 'time_stamp',
  ROUND(AVG(score), 2) as 'avg score',
  count(*) as 'total story'
from hacker_news 
where 1 IS NOT NULL -- only take the un-NULL value
group by 1 
order by 2 desc -- make the time_stamp column not group all 
```

**TRIGGER**
+ ? Trigger function: Automatically Trigger a Query after an Event
	Example: increate salary automatically when hourly_pay was increase. (don't need to update salary manually anymore)
1) Name Trigger function 
2) BEFORE/AFTER (INSERT/UPDATE/DELETE)
3) FOR (What/How Many) Row ?
4) Trigger a Query 
-> Trigger applied changes into table before an operation (UPDATE/INSERT/DELETE) FOR N number of row.


+ SHOW TRIGGER



**TRIGGER Example**
+ **BEFORE**
	![[Pasted image 20240318094657.png]]

+ **AFTER**
	![[Pasted image 20240318094636.png]]\

### Update Column A value for each value in Column B
> Insert new Column hours_salary -> Update hours_salary alongside with employees salary.

+ ? Update hours_salary by salary of an Employee
**SQL on MS SQLServer**
```sql
CREATE TRIGGER update_hours_salary 
ON employees
AFTER UPDATE 
AS 
BEGIN
    UPDATE employees
    -- 70 hours work week for a year = 3360 hours
    SET hours_salary = salary / (12*4*70)
    WHERE employee_id IN (SELECT employee_id from inserted)
END;
```

Create Procedure
+ ? Update salary by @emp_id
```sql
--? update salary by @emp_id
CREATE OR ALTER PROCEDURE translate_salary(@emp_id INT)
AS BEGIN
    DECLARE @salary DECIMAL(8, 2)
    SELECT @salary = salary from employees WHERE employee_id = @emp_id;
    UPDATE employees SET salary = @salary WHERE employee_id = @emp_id
END
GO
```

+ ? Repeat a procedure n time for each element in table
+ ? For each @emp_id execute translate_salary procedure
1) For Loop
```sql
DECLARE @emp_id INT;
DECLARE emp_cursor CURSOR FOR 
SELECT employee_id FROM employees;

OPEN emp_cursor;
FETCH NEXT FROM emp_cursor INTO @emp_id;

WHILE @@FETCH_STATUS = 0
BEGIN
    --? Excecute 'translate_salary' Procedure for each @emp_id
    EXEC translate_salary @emp_id;
    FETCH NEXT FROM emp_cursor INTO @emp_id;
END;

CLOSE emp_cursor;
DEALLOCATE emp_cursor;
GO
SELECT * from employees
```
2) While Loop
```sql
DECLARE @emp_id INT;
DECLARE @max_emp_id INT;

SELECT @max_emp_id = MAX(employee_id) FROM employees;
SET @emp_id = 1;  -- Or the minimum employee_id

WHILE @emp_id <= @max_emp_id
BEGIN
    -- Call your procedure and pass in the current @emp_id
    EXECUTE translate_salary @emp_id;

    SET @emp_id = @emp_id + 1;
END

SELECT * from employees
```

