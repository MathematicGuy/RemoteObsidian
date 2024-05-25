
![[hw1.jpg]]
![[DB_Schema.jpg]]

#### Part 1

1)
```sql
select * from employees, departments
```
2)
```sql
select hire_date, first_name, last_name from employees
```
3)
```sql
select CONCAT(first_name, ' ', last_name, ', ', job_id) as 'Employee and Title' from employees;
```
4)
```sql
select hire_date, first_name, last_name, department_id from employees
```
5) Can this be automation
```sql
SELECT CONCAT(employee_id, ', ', first_name, ', ', last_name, ', ', email, ', ', phone_number, ', ', hire_date, ', ', job_id, ', ', salary, ', ', manager_id, ', ', department_id) as 'THE_OUTPUT'

FROM employees;
```
6)
```sql
select * from employees where salary > 2000
```
7)
```sql
select CONCAT(first_name, ' ', last_name) as "Name", hire_date as "Start Date" from employees
```
8)
```sql
select CONCAT(first_name, ' ', last_name) as "Name", hire_date as "Start Date" from employees ORDER BY hire_date ASC
```
9)
```sql
select CONCAT(first_name, ' ', last_name) as "Name", salary from employees ORDER BY salary
```
10)
Employees earned commission mean they have a manager. (Manager_id != NULL)
```sql
select  CONCAT(first_name, ' ', last_name) as "ename", department_id as 'deptno' from employees where manager_id IS NOT NULL ORDER BY salary
```
11)
```sql
select last_name, job_title

from

    employees INNER JOIN jobs ON employees.job_id = jobs.job_id  

where manager_id IS NULL
```
12)
```sql
select last_name, job_title, salary from employees
INNER JOIN jobs ON employees.job_id = jobs.job_id
WHERE job_title IN ('Sales Representative', 'Stock Clerk') 
AND salary NOT IN (2500, 3500, 5000)
```

#### Part 2
![[hw2.jpg]]
![[DB_Schema.jpg]]

1) x
```sql
select MAX(salary) as 'maximum salary', MIN(salary) as 'minimum salary', AVG(salary) as 'average salary' from employees
```

2) x
```sql
```
3) x
```sql
select department_id as 'Department Number', COUNT(department_id) as 'Number of Employee' from employees GROUP BY department_id
```
4) x
```sql
```
5) x
```sql
```
6) x
```sql
```
7) x
```sql
select 3
```  
8) x
```sql
select CONCAT(first_name, ', ', last_name), department_id from employees 
WHERE first_name IN (
    -- find duplicate first name
    select first_name from employees GROUP BY first_name HAVING COUNT(first_name) > 1 
)
```

