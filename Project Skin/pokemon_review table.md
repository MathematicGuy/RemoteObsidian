```sql
use pokemonreview

-- note: comission = salary - min_salary > 0
-- SELECT e.first_name + ' ' + e.last_name AS 'FULL Name', e.salary
-- CASE    
--     WHEN (e.salary - j.min_salary) < 0 THEN "no_comission"
-- FROM employees AS e
-- JOIN jobs AS j ON e.job_id = j.job_id;


CREATE TABLE Country
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    Name varchar(50) NOT NULL,    
);

CREATE TABLE Owner
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    Name varchar(50) NOT NULL,
    Gym varchar(50) NOT NULL,
    Country varchar(50) NOT NULL,
    
);


CREATE TABLE Category
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    Name varchar(50) NOT NULL,
    -- specify more columns here
);


CREATE TABLE Reviewer
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL,
    -- specify more columns here
);

CREATE TABLE Review
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    Title varchar(50) NOT NULL,
    Text varchar(50) NOT NULL,
    -- specify more columns here
);

CREATE TABLE pokemon
(
    id INT NOT NULL PRIMARY KEY, -- primary key column
    Name varchar(50) NOT NULL,
    BirthDate DATE NOT NULL,
    -- specify more columns here
);


```