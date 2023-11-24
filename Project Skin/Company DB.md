EMPLOYEE
```sql
create table employee (
    Fname varchar(50),
    Minit varchar(1),
    Lname varchar(50),
    Ssn varchar(9) NOT NULL PRIMARY KEY,
    Bdate DATE,
    Address varchar(50),
    Sex char(1),
    Salary INT,
    Super_ssn varchar(9),
    Dno INT,
)

INSERT INTO employee (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno)
VALUES
  ('John', 'B', 'Smith', '129456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', 90000, '993445555', 5),
  ('Franklin', 'W', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5),
  ('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321 Castle, Spring, TX', 'F', 25000, '987654321', 4),
  ('Jennifer', 'S', 'Wallace', '987654921', '1941-06-20', '291 Berry, Bellaire, TX', 'F', 43000, '888665555', 4),
  ('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire oak, Humble, TX', 'M', 38000, '333445555', 5),
  ('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5),
  ('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', 25000, '987654321', 4),
  ('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone, Houston, TX', 'M', 55000, NULL, 1);

select * from employee
```


DEPARTMENT
```sql
create table DEPARTMENT (
    Dname varchar(50),
    Dnumber INT NOT NULL PRIMARY KEY,
    Mgr_ssn varchar(9),
    Mgr_start_date date,
)

-- Insert data into the DEPARTMENT table
INSERT INTO DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date)
VALUES
  ('Research', 5, '333445555', '1988-05-22'),
  ('Administration', 4, '987654321', '1995-01-01'),  -- Assuming Mgr_start_date is allowed to be NULL
  ('Headquarters', 1, '888665555', '1981-09-19');


select * from DEPARTMENT
```

DEPT_LOCATIONS
```sql
create table DEPT_LOCATIONS (
    Dnumber INT,
    Dlocation varchar(50),
    PRIMARY KEY (Dnumber, Dlocation),
)

-- Insert data into the DEPT_LOCATIONS table
INSERT INTO DEPT_LOCATIONS (Dnumber, Dlocation)
VALUES
  (1, 'Houston'),
  (4, 'Stafford'),
  (5, 'Bellaire'),
  (5, 'Sugarland'),
  (5, 'Houston');

select * from DEPT_LOCATIONS
```

WORKS_ON
```sql
create table WORKS_ON (
    Essn varchar(9),
    Pno INT,
    Hours FLOAT,
    PRIMARY KEY (Essn, Pno),
)

-- Insert data into the WORKS_ON table
INSERT INTO WORKS_ON (Essn, Pno, Hours)
VALUES
  (123456789, 1, 32.5),
  (123456789, 2, 7.5),
  (666884444, 3, 40.0),
  (453453459, 1, 20.0),
  (453453453, 2, 20.0),
  (333445555, 2, 10.0),
  (933445555, 3, 10.0),
  (333445555, 10, 10.0),
  (933445555, 20, 10.0),
  (999887777, 30, 30.0),
  (999887777, 10, 10.0),
  (987987987, 10, 35.0),
  (987987987, 30, 5.0), 
  (987654321, 30, 20.0),
  (987654321, 20, 15.0),
  (888665555, 20, NULL);

select * from WORKS_ON
```

PROJECT
```sql
create table PROJECT  (
    Pname varchar(20),
    Pnumber INT NOT NULL PRIMARY KEY,
    Plocation varchar(20),
    Dnum INT,
)

-- Insert data into the PROJECT table
INSERT INTO PROJECT (Pname, Pnumber, Plocation, Dnum)
VALUES
  ('ProductX', 1, 'Bellaire', 5),
  ('ProductY', 2, 'Sugarland', 5),
  ('ProductZ', 3, 'Houston', 5),
  ('Computerization', 10, 'Stafford', 4),
  ('Reorganization', 20, 'Houston', 1), 
  ('Newbenefits', 30, 'Stafford', 4);

select * from PROJECT
```

DEPENDENT
```sql
create table DEPENDENT  (
    Essn varchar(9),
    Dependent_name varchar(20),
    Sex char(1),
    Bdate date,
    Relationship varchar(20),
)

-- Insert data into the DEPENDENT table
INSERT INTO DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship)
VALUES
    (333445555, 'Alice', 'F', '1986-04-05', 'Daughter'),
    (333445555, 'Theodore', 'M', '1983-10-25', 'Son'),
    (333445555, 'Joy', 'F', '1958-05-03', 'Spouse'),
    (987654321, 'Abner', 'M', '1942-02-28', 'Spouse'),
    (123456789, 'Michael', 'M', '1988-01-04', 'Son'),
    (123456789, 'Alice', 'F', '1988-12-30', 'Daughter'),
    (123456789, 'Elizabeth', 'F', '1967-05-05', 'Spouse');

select * from DEPENDENT;
```
