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
+ **Else Scenario:** new department_id = old department_id -> Change dep_name only
```sql
/*
? This script is used to modify department details in the jobDB database.
? It includes a stored procedure called modifyDep which 
?    takes three parameters: @oldDep_id, @newDep_id, and @dep_name. 

? The procedure works as follows:
*    1. It retrieves the location_id of the old department.
*    2. Checks if the new department id already exists in the departments table.
*    3. If the new department id does not exist, it inserts a new department with the new department id, department name, and the location id of the old department. It then transfers all employees from the old department to the new one and deletes the old department.
*    4. If the new department id already exists, it simply updates the department name of the existing department.

* In case of any errors during the transaction, it rolls back the transaction and raises an error.

? Finally, the script executes the modifyDep procedure with sample parameters and selects all records from the departments table.
*/
SET IDENTITY_INSERT departments ON;
GO

CREATE OR ALTER PROCEDURE modifyDep(@oldDep_id INT, @newDep_id INT, @dep_name nvarchar(30))
AS BEGIN 

    BEGIN TRANSACTION;
    -- Begin Try Catch. Any Errors within Try goes to Catch
    BEGIN TRY
        -- get location_id from the old department
        DECLARE @location_id INT;
        SELECT @location_id = departments.location_id from departments WHERE department_id = @oldDep_id;
        
        -- insert new dep if not inserted already
        IF @newDep_id NOT IN (SELECT department_id FROM departments)
            BEGIN
                -- Insert the new department
                INSERT INTO departments (department_id, department_name, location_id)
                VALUES (@newDep_id, @dep_name, @location_id);

                -- Transfer employees from the old department to the new one
                UPDATE employees 
                SET department_id = @newDep_id 
                WHERE department_id = @oldDep_id

                -- Delete the old department
                DELETE FROM departments 
                WHERE department_id = @oldDep_id
            END
        ELSE
            BEGIN
                -- If the new department already exists, rename it
                UPDATE departments 
                SET department_name = @dep_name 
                WHERE department_id = @newDep_id;
            END
    -- pernamently save progress. The opposite of ROLLBACK
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

EXEC modifyDep @oldDep_id = 1, @newDep_id = 1, @dep_name = 'Administration'
SELECT * from departments
SET IDENTITY_INSERT departments OFF; -- turn back On auto-increament
GO
```


5. Create a trigger to log deleted employee information: Write a trigger that logs information about the deleted employee into a separate table before the deletion occurs. Include details such as the employee's ID, name, department, and deletion timestamp
	+ create deletedEmployee 
	+ trigger before -> insert 'deleted employee' to deletedEmployee with timestamp
```sql
CREATE OR ALTER TRIGGER delete_empls 
ON employees
AFTER DELETE
AS BEGIN
    SET IDENTITY_INSERT deletedEmployee ON -- turn ON auto-increment for deletedEmployee table
    INSERT INTO deletedEmployee (employee_id, first_name, last_name, department_id)
        SELECT employee_id, first_name, last_name, department_id
        FROM deleted;
    SET IDENTITY_INSERT deletedEmployee OFF; -- turn OFF auto-increment for deletedEmployee table

    UPDATE deletedEmployee SET deletion_time = GETDATE() 
    -- where employee_id == deleted employee_id  
    WHERE employee_id IN (SELECT employee_id FROM deleted)
    
END;


delete from employees where employee_id = 302
select * from employees
select * from deletedEmployee;
```
![[Pasted image 20240319124346.png]]


6. Write a trigger that checks for dependencies before allowing the deletion of a manager. In this case, ensure that all employees under their supervision are reassigned before allowing the deletion.
+ Check Dependencies: Employee - Manager
	1) Employee depend on that SManager 
+ Reassigned 
```sql
--? Use INSTEAD OF DELETE (like BEFORE DELETE but easier to understand) (Instead of just delete we do this and that and finally delete)
CREATE OR ALTER TRIGGER smart_mgrs_deletion 
on employees
Instead OF DELETE
as BEGIN
    DECLARE @old_mgr_id INT;
    DECLARE @new_mgr_id INT;
    --? get @old_mgr_id & @new_mgr_id
    SELECT @old_mgr_id = employee_id from deleted; 

--? 1. Check the manager dependancies. If more than 0 employees depend on that 1 manager_id
    IF (SELECT COUNT(*) from employees where employee_id = @old_mgr_id) > 0
    BEGIN
    --? Reassign the emlpoyee's manager before deletion.
        --? UPDATE empls old manager -> @new_mgr_id. 
        --? Get @new_mgr_id
        SELECT TOP(1) @new_mgr_id = manager_id from employees WHERE manager_id <> @old_mgr_id  
        UPDATE employees SET manager_id = @new_mgr_id WHERE manager_id = @old_mgr_id
        --? employee's manager_id = @new_mgr_id
    END
    --? Delete. Left outside of If because if there're no problem then just delete 
    DELETE from employees WHERE employee_id = @old_mgr_id  
END
GO

delete from employees WHERE employee_id = 108
select * from employees
select * from deletedEmployee

--! Common errors might occurs? 
--? Delete the manager's manager: 
    -- when do this
        -- SELECT @old_mgr_id = manager_id from deleted; 
     
--? Delete manager's manager while still reassigning employees to another manager 
    -- DELETE from employees WHERE manager_id = @old_mgr_id  

```


7. Create a trigger to reassign employees before department deletion: Write a trigger that automatically reassigns employees to another department when their current department is deleted. The trigger should ensure that all employees in the department being deleted are reassigned to a valid department
```sql

```
**BEFORE**
![[Pasted image 20240320000910.png]]
EXAM -> **Trigger, Procedure**