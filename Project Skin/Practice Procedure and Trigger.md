![[Pasted image 20240313170209.png]]

1. Find those employees whose salaries are higher than the average for all departments
```sql
select * from employees where 
    salary > (select AVG(salary) from employees)
```


2. Write a stored procedure that receives the department id as the input and displays the average salary of the employees working at that department.
```sql
CREATE PROCEDURE get_customer_salary (@deparment_id INT)
AS BEGIN
	 SELECT AVG(salary) as avg_salary FROM employees WHERE department_id = @deparment_id;
END

get_customer_salary 8; -- OR EXEC get_customer_salary 8;
```

   
3. Create a stored procedure that takes the department ID and the employee ID as parameters, enabling the transfer of employees from one department to another. If an employee's salary is lower than the minimum salary of the destination department, the procedure will adjust the employee's salary to match the minimum salary of that department
```sql
CREATE OR ALTER PROCEDURE tranfer_employee
 (
	-- input parameter
	@emp_id INT,
	@dep_id INT
)
AS
BEGIN
    DECLARE @min_salary DECIMAL(10, 2);
    DECLARE @emp_salary DECIMAL(10, 2);
    --? Get the Minimum Salary of the selected department
    select @min_salary = MIN(salary)
    from employees
    where department_id = 2
    --? Get the Selected Employee Salary 
    select @emp_salary = salary
    from employees
    WHERE employee_id = 107
    --? If the employee's salary is lower than 
    --? the minimum salary of the destination department, adjust the salary
    UPDATE employees
SET department_id = 2
WHERE 107 = employee_id
    IF (@min_salary > @emp_salary) BEGIN
        UPDATE employees
SET salary = @min_salary
WHERE 107 = employee_id
    END
END 
-- Go mean run all the Query before me
GO -- always add GO at the end of a procedure. Else it will not run/ 

EXEC tranfer_employee @emp_id = 107,
@dep_id = 2
```
+ ? BEFORE
![[Pasted image 20240318014550.png]]
+ ? AFTER
![[Pasted image 20240318014618.png]]


4. Design a stored procedure that updates department details (department id and department name) and, if necessary, reassigns employees to a new department in a single transaction. Ensure the procedure handles errors and rolls back the transaction if any step fails.
   
+ **Summary:** procedure update department id or name or both. And reassignment employees to a new department if needed
+ **Method:** 
	Create a temporaly department_id and transfer all the employee to that department then Update current department_id.
+ **Fail Scenario:** new department_id = old department_id
```sql

```
![[Pasted image 20240318030825.png]]

5. Write a trigger that checks for dependencies before allowing the deletion of a manager. In this case, ensure that all employees under their supervision are reassigned before allowing the deletion.
```sql

```


6. Create a trigger to reassign employees before department deletion: Write a trigger that automatically reassigns employees to another department when their current department is deleted. The trigger should ensure that all employees in the department being deleted are reassigned to a valid department
```sql

```

