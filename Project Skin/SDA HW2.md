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
select e.last_name as 'e last_name', e.phone_number as 'e phone_number', me.last_name as 'me last_name', me.phone_number as 'me phone_number'
from employees as e
    JOIN employees as me ON e.manager_id = me.employee_id 
    JOIN jobs ON e.job_id = jobs.job_id
```
![[Pasted image 20240301114821.png]]
```sql
select e.last_name as 'Employees', e.phone_number as 'em_phone', me.last_name as 'Manager', me.phone_number as 'ma_phone'
from employees as e
    -- LEFT/RIGHT JOIN take NULL value. INNER JOIN only take value != NULL
    -- we 'e' with 'me' so I use Left JOIN to extract all value from employees 
    -- Get the last names of employees who do not have a manager.
    LEFT JOIN employees as me ON e.manager_id = me.employee_id 
    JOIN jobs ON e.job_id = jobs.job_id
```
![[Pasted image 20240301114830.png]]
+ ? something wrong but I don't know
```sql
select e1.last_name, e2.last_name, departments.department_id 
from employees as e1
LEFT JOIN departments  ON e1.department_id = departments.department_id
LEFT JOIN employees as e2 ON  e1.department_id = e2.department_id;

```
![[Pasted image 20240301114837.png]]
+ ! remove 1 zero for each grade.
```sql
select (employees.first_name + ' ' + employees.last_name) as 'name', jobs.job_title, departments.department_name, employees.salary,
--- if else statement
CASE 
    WHEN (employees.salary) >= 5000 THEN 'A'
    WHEN 5000 >= (employees.salary) and (employees.salary) >= 3000 THEN 'B'
    ELSE 'C'
END AS Grade
--- end of if else statement

--- connect fields from other table
FROM employees
    JOIN jobs on employees.job_id = jobs.job_id
    JOIN departments on employees.department_id =  departments.department_id ;
```
![[Pasted image 20240301114848.png]]
```sql
select (e.first_name + ' ' + e.last_name) as 'name', e.hire_date
from employees as e
    -- display the employee name along with their manager
    LEFT JOIN employees as me ON e.manager_id = me.employee_id 
    JOIN jobs ON e.job_id = jobs.job_id
where e.hire_date < me.hire_date;
```
