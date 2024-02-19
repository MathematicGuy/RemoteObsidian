```sql
CREATE TABLE employees(
    employee_id CHAR(4) NOT NULL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    phone_number INT,
    hire_date DATE,
    job_id VARCHAR(7),
    salary INT,
    manager_id CHAR(4) NOT NULL,
    department_id CHAR(4) NOT NULL
);
```

Update
```sql
update employees
set manager_id = 'M001'
WHERE employee_id = 'E001';

select * from employees
```

Insert
```sql
INSERT INTO employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
VALUES ('E001', 'John', 'Smith', 'john.smith@example.com', 5551234, '2022-10-01', 'IT_PROG', 60000, 'E001', 'D001');
```

