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
SET IDENTITY_INSERT departments ON;
GO

CREATE OR ALTER PROCEDURE modifyDep(@oldDep_id INT, @newDep_id INT, @dep_name nvarchar(30))
AS BEGIN 
    BEGIN TRANSACTION;
    BEGIN TRY
        -- get location_id from the old department
        DECLARE @location_id INT;
        select @location_id = departments.location_id from departments WHERE department_id = @oldDep_id;
        
        -- insert new dep if not inserted already
        IF @newDep_id NOT IN (SELECT department_id FROM departments)
            BEGIN
                -- Insert the new department
                INSERT INTO departments (department_id, department_name, location_id)
                VALUES (@newDep_id, @dep_name, @location_id);

                -- Transfer employees from the old department to the new one
                UPDATE employees 
                SET department_id = @newDep_id 
                WHERE department_id = @oldDep_id;

                -- Delete the old department
                DELETE FROM departments 
                WHERE department_id = @oldDep_id;
            END
        ELSE
            BEGIN
                -- If the new department already exists, rename it
                UPDATE departments 
                SET department_name = @dep_name 
                WHERE department_id = @newDep_id;
            END
    COMMIT TRANSACTION;
    END TRY

    BEGIN CATCH
        -- An error occurred, so rollback the transaction
        ROLLBACK TRANSACTION;

        -- Re-throw the error
        RAISERROR('Duplicate Department_id. Can not Execute', 16, 1)
    END CATCH
END
GO

EXEC modifyDep @oldDep_id = 1, @newDep_id = 66, @dep_name = 'Administration'
SELECT * from departments
SET IDENTITY_INSERT departments OFF; -- turn back On auto-increament 
GO
```


5. Write a trigger that checks for dependencies before allowing the deletion of a manager. In this case, ensure that all employees under their supervision are reassigned before allowing the deletion.
```sql

```


6. Create a trigger to reassign employees before department deletion: Write a trigger that automatically reassigns employees to another department when their current department is deleted. The trigger should ensure that all employees in the department being deleted are reassigned to a valid department
```sql

```

