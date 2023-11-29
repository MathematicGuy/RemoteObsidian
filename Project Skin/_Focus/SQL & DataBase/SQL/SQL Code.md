source: https://youtu.be/5OdVJbNCSso?si=d81elQsUp3hp_XQr
SQL Learning Tools
	[SQL Zoo](https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial)
		SQL quizziz
	[SQL Bolt](https://sqlbolt.com/)
		Interactive Lesson | All within Browser
	[Mode](https://mode.com/sql-tutorial/) 
		Learn Answer Question using SQL
		Level: Beginner - Intermediate - Advance
	[MySQLTUTORIAL](https://www.mysqltutorial.org/) 
		Make SQL Easy & Fun
		SQL Notes | With Practical Example 
	[SQL Murder Mystery](https://mystery.knightlab.com/)
		Hones SQL Problems solving 

---
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

RENAME Table or DROP the TABLE 
```sql
RENAME TABLE employees TO workers;
DROP TABLE employees;
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


 UPDATE DATA (Change Field and Record Value)
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
> + If cannot connect foreign key, re-check if you are connec to a primary key (caution for duplicate value, it not a primary key)
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
or you can add foreign key later with this
```sql
ALTER TABLE transactions
ADD CONSTRAINT fk_customer_id
FOREIGN KEY(trans_customer_id) REFERENCES customers(customer_id)
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
 >  a.f_name -> select f_name from table a
```sql
CONCAT(b.f_name, " ", b.l_name) AS "referred_by"
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

**INNER JOIN** 
-- SELF JOIN
-- join another copy of a tbale to itself
-- used to compare rows of the same table
-- helps to display a heirarchy of data
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


GROUP BY
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

**sth%** 
-> % represent 0, 1 or all the rest of the string. or something
-> %a% mean sth contain a. 
> use this when you try to search a word start with ...
```sql
SELECT name FROM world WHERE name LIKE 'United%'
```
> **select all word contain United in it.**

+ select the first name seperate by a space ' '
```sql
SELECT name FROM world WHERE name LIKE '% %';
SELECT SUBSTRING_INDEX(name, ' ', 1) AS first_name FROM world WHERE name LIKE '% %';
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
> Inside a table, a column often contains **many duplicate values;** and sometimes you **only want to list the different (distinct) values.**
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
        SELECT column_name
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
    where population <= 25000000)
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