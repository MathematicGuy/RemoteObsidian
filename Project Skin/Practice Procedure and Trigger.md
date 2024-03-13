![[Pasted image 20240313170209.png]]

1. Find those employees whose salaries are higher than the average for all departments
```sql

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

```
Before
![[Pasted image 20240313223910.png]]


4. Design a stored procedure that updates department details (department id and department name) and, if necessary, reassigns employees to a new department in a single transaction. Ensure the procedure handles errors and rolls back the transaction if any step fails.
```sql

```


6. Write a trigger that checks for dependencies before allowing the deletion of a manager. In this case, ensure that all employees under their supervision are reassigned before allowing the deletion.
```sql

```


7. Create a trigger to reassign employees before department deletion: Write a trigger that automatically reassigns employees to another department when their current department is deleted. The trigger should ensure that all employees in the department being deleted are reassigned to a valid department
```sql

```

