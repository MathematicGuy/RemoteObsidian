![[DB_Schema.jpg]]
![[1.jpg]]
![[2.jpg]]

![[Pasted image 20240301114752.png]]
```sql
select last_name, departments.department_id, departments.department_name
from  employees
    INNER JOIN departments ON employees.department_id = departments.department_id;
```
![[Pasted image 20240301114746.png]]
```sql
select Distinct(job_title), street_address from jobs
JOIN employees ON jobs.job_id = employees.job_id
JOIN departments ON employees.department_id = departments.department_id
JOIN locations ON departments.location_id =  locations.location_id  
where departments.department_id = 4

select * from locations
```
![[Pasted image 20240301114736.png]]
+ Using CASE WHEN `condition` THEN `something_happend_here` ELSE `something_happend_here` END AS `column_name`
+ ? *It can also be like this* Using CASE WHEN `condition` THEN `something_happend_here` END 
```sql
-- Select the last name, department name, location ID,
-- and commission status of employees from the "employees" table.
SELECT last_name, department_name, location_id,
    CASE WHEN (salary - min_salary) > 0 THEN 'commission' -- if true  
    ELSE 'no_commission' -- if false
    END AS commission -- column name

-- Join the "employees" table with the "jobs" table on the job_id column
-- and with the "departments" table on the department_id column.
FROM employees
    JOIN jobs ON employees.job_id = jobs.job_id
    JOIN departments ON employees.department_id = departments.department_id;
```
![[Pasted image 20240301114759.png]]
```sql
select last_name, department_name
from employees
JOIN departments ON employees.department_id = departments.department_id
where last_name LIKE '%a%';
```
![[Pasted image 20240301114804.png]]
ATLANTA -> SEATTLE
```sql
select last_name, departments.department_id, department_name from employees
    JOIN departments
        ON employees.department_id = departments.department_id
    JOIN locations
        ON departments.location_id = locations.location_id
    WHERE city LIKE '%Seattle';
```
![[Pasted image 20240301114815.png]]
```sql

```
![[Pasted image 20240301114821.png]]
```sql

```
![[Pasted image 20240301114830.png]]
```sql

```
![[Pasted image 20240301114837.png]]
```sql

```
![[Pasted image 20240301114848.png]]
```sql

```