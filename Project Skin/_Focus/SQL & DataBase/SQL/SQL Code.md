source: https://youtu.be/5OdVJbNCSso?si=d81elQsUp3hp_XQr

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

MODIFIED TABLE
```sql
ALTER TABLE employees
ADD phone_number VARCHAR(20);
RENAME COLUMN phone_number TO email;
```
![[Pasted image 20230814114906.png]]

```sql
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100);
```
![[Pasted image 20230814114948.png]]


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


 UPDATE DATA 
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
FOREIGN KEY -> Join, Link 2 Table prevent any action destroy 2 tables 
![[Pasted image 20231003135913.png]]

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

CONCAT -> Merge 2 Column together
 >  a.f_name -> select f_name from table a
 ```sql
CONCAT(b.f_name, " ", b.l_name) AS "referred_by"
```
![[Pasted image 20231003141638.png]]


INNER JOIN 
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


IN
> represent = sign
```sql
SELECT name, population FROM world WHERE name IN ('FRANCE', 'Germany', 'Italy');
```