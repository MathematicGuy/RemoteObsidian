**4.1 Giả sử các thông tin về một trường đại học được mô tả (bằng tiếng Anh) như sau:**

- The university is organized into departments. **Each department is identified by a unique name
(dept name), is located in a particular building**, and has a budget.

- Each department has a list of courses it offers. Each **course has associated with it a course id,
title, dept name, and credits**, and may also have have associated prerequisites.

- Instructors are **identified by their unique ID**. Each instructor has name, associated department
(dept_name), and salary.

- Students are **identified by their unique ID**. Each student has a name, an associated major
department (dept_name), and tot_cred (total credit hours the student earned thus far).

- The university maintains a list of classrooms, specifying the name of the **building, room_number**, and room capacity.

- The university maintains a list of all classes (**sections**) taught. Each **section is identified by a
course id, sec_id, year, and semester**, and has **associated with it a semester, year, building,
room_number, and time_slot_id** (the time slot when the class meets).

- The **department** has a list of teaching assignments specifying, for **each instructor, the sections** the instructor is teaching.

- The university has a list of all student **course registrations**, specifying, for each student, the
**courses and the associated sections** that the student has taken (registered for).

**a) Cơ sở dữ liệu quan hệ về trường đại học được thiết kế gồm các lược đồ quan hệ sau. Hãy xác
định khóa chính của mỗi lược đồ**

**Bold Word** represent **Primary Key** 
>classroom(**building, room_number**, capacity)
	->  Building can have the same room_number. 

> department(**dept_name, building**, budget)
	-> Building can have smae department 

>course(**course_id**, title, dept_name, credits)

>instructor(**ID**, name, dept_name, salary)

>section(**course_id, sec_id, semester, year**, building, room_number, time_slot_id)
	-> The combination of course_id, sec_id, semester, and year uniquely identifies each section.

>teaches(**ID, course_id, sec_id, semester, year**)
	-> A sub-class of Instructor

>student(**ID**, name, dept_name, tot_cred)

>takes(**ID, course_id, sec_id, semester, year**, grade)
	-> Course enrollment each year in a semester in a section of a student 

>advisor(**s_ID, i_ID**)
	-> A Teacher can advise each Student

>time_slot(**time_slot_id**, day, start_time, end_time)

>prereq(**course_id, prereq_id**)
	-> The combination of course_id and prereq_id uniquely identifies each prerequisite relationship.

**b) Viết câu lệnh SQL tạo các bảng và nhập dữ liệu cho các bảng như sau**


```sql
-- Create the table in the specified schema
CREATE TABLE instructor
(
    ID INT NOT NULL PRIMARY KEY, -- primary key column
    name varchar(50),
    dept_name varchar(50),
    salary INT,
);
GO
```

```sql
INSERT INTO instructor (ID, name, dept_name, salary)
VALUES
  (10101, 'Srinivasan', 'Comp. Sci.', 65000),
  (12121, 'wu', 'Finance', 90000),
  (15151, 'Mozart', 'Music', 40000),
  (22222, 'Einstein', 'Physics', 95000),
  (33436, 'El Said', 'History', 60000),
  (76343, 'Gold', 'Physics', 87000),
  (76766, 'Katz', 'Comp. Sci.', 75000),
  (98345, 'Califieri', 'History', 62000);

-- Verify the data
SELECT * FROM instructor;
```


course
```sql
CREATE TABLE course
(
    course_id varchar(20) NOT NULL PRIMARY KEY, -- primary key column
    title varchar(50),
    dept_name varchar(50),
    credits INT,
);

Select * FROM course
```

```sql
INSERT INTO course (course_id, title, dept_name, credits)
VALUES
  ('BIO-1O1', 'Intro. to Biology', 'Biology', 4),
  ('BIO-301', 'Genetics', 'Biology', 4),
  ('BIO-399', 'Computational Biology', 'Biology', 3),
  ('CS-101', 'Intro. to Computer Science', 'Comp. Sci.', 4),
  ('CS-190', 'Game Design', 'Comp. Sci.', 4),
  ('CS-315', 'Robotics', 'Comp. Sci.', 3),
  ('CS-319', 'Image Processing', 'Comp. Sci.', 3),
  ('CS-347', 'Database System Concepts', 'Comp. Sci.', 3),
  ('EE-181', 'Intro. to Digital Systems', 'Elec. Eng.', 3),
  ('FIN-201', 'Investment Banking', 'Finance', 3),
  ('HIS-351', 'World History', 'History', 3),
  ('MU-199', 'Music Video Production', 'Music', 3),
  ('PHY-1O1', 'Physical Principles', 'Physics', 4);

-- Verify the data
SELECT * FROM course;
```

prereq
```sql
INSERT INTO prereq (course_id, prereq_id)  
VALUES 
(
    'BIO-301', 'BIO-101'
); 
```


```sql
-- Insert data into the prereq table
INSERT INTO prereq (course_id, prereq_id)
VALUES
  ('BIO-399', 'BIO-101'),
  ('CS-190', 'CS-101'),
  ('CS-315', 'CS-101'),
  ('CS-319', 'CS-101'),
  ('CS-347', 'CS-101'),
  ('EE-181', 'PHY-101');

-- Verify the inserted data
SELECT * FROM prereq;
```

department
```sql
CREATE TABLE department (
    dept_name varchar(30),
    building varchar(30),
    budget INT,
    PRIMARY KEY (dept_name, building)
)
```

```sql
INSERT INTO department (dept_name, building, budget)
VALUES
  ('Biology', 'Watson', 90000),
  ('Comp. Sci.', 'Taylor', 100000),
  ('Elec. Eng.', 'Taylor', 85000),
  ('Finance', 'Painter', 120000),
  ('History', 'Painter', 50000),
  ('Music', 'Packard', 80000),
  ('Physics', 'Watson', 70000);


Select * FROM department;
```

teaches
```sql
CREATE TABLE teaches (
    ID INT,
    course_id varchar(30),
    sec_id INT,
    semester varchar(30),
    year INT,
    
    PRIMARY KEY (ID, course_id, sec_id, semester, year),
);
```

```sql
INSERT INTO teaches (ID, course_id, sec_id, semester, year)
VALUES
  (10101, 'CS-101', 1, 'Fall', 2009),
  (10101, 'CS-315', 1, 'Spring', 2010),
  (10101, 'CS-347', 1, 'Fall', 2009),
  (12121, 'FIN-201', 1, 'Spring', 2010),
  (15151, 'MU-199', 1, 'Spring', 2010),
  (22222, 'PHY-101', 1, 'Fall', 2009),
  (32343, 'HIS-351', 1, 'Spring', 2010),
  (45565, 'CS-101', 1, 'Spring', 2010),
  (45565, 'CS-319', 1, 'Spring', 2010),
  (76766, 'BIO-101', 1, 'Summer', 2009),
  (76766, 'BIO-301', 1, 'Summer', 2010),
  (83821, 'CS-190', 1, 'Spring', 2009),
  (83821, 'CS-190', 2, 'Spring', 2009),
  (83821, 'CS-319', 1, 'Spring', 2010),
  (98345, 'EE-181', 1, 'Spring', 2009);

-- Verify the inserted data
SELECT * FROM teaches;
```


section
```sql
CREATE TABLE section (
    course_id varchar(30),
    sec_id INT,
    semester varchar(30),
    year INT,
    building varchar(30),
    room_number INT,
    time_slot_id varchar(1),
    
    PRIMARY KEY (course_id, sec_id, semester, year),
);
```

```sql
-- Insert data into the section table
INSERT INTO section (course_id, sec_id, semester, year, building, room_number, time_slot_id)
VALUES
  ('BIO-101', 1, 'Summer', 2009, 'Painter', 514, 'B'),
  ('BIO-301', 1, 'Summer', 2010, 'Painter', 514, 'A'),
  ('CS-101', 1, 'Fall', 2009, 'Packard', 101, 'H'),
  ('CS-101', 1, 'Spring', 2010, 'Packard', 101, 'F'),
  ('CS-190', 1, 'Spring', 2009, 'Taylor', 3128, 'E'),
  ('CS-190', 2, 'Spring', 2009, 'Taylor', 3128, 'A'),
  ('CS-315', 1, 'Spring', 2010, 'Watson', 120, 'D'),
  ('CS-319', 1, 'Spring', 2010, 'Watson', 100, 'B'),
  ('CS-319', 2, 'Spring', 2010, 'Taylor', 3128, 'C'),
  ('CS-347', 1, 'Fall', 2009, 'Taylor', 3128, 'A'),
  ('EE-181', 1, 'Spring', 2010, 'Taylor', 101, 'C'),
  ('FIN-201', 1, 'Spring', 2010, 'Packard', 514, 'B'),
  ('HIS-351', 1, 'Spring', 2010, 'Painter', 101, 'C'),
  ('MU-199', 1, 'Spring', 2010, 'Packard', 100, 'D'),
  ('PHY-101', 1, 'Fall', 2009, 'Watson', 101, 'A');


-- Verify the inserted data
SELECT * FROM section;
```

student
```sql
CREATE TABLE student (
    ID INT NOT NULL PRIMARY KEY,
    name varchar(30),
    dept_name varchar(30),
    tot_cred INT,
);
```

```sql
-- Insert data into the student table
INSERT INTO student (ID, name, dept_name, tot_cred)
VALUES
  ('00128', 'Zhang', 'Comp. Sci.', 102),
  ('12345', 'Shankar', 'Comp. Sci.', 32),
  ('19991', 'Brandt', 'History', 80),
  ('23121', 'Chavez', 'Finance', 110),
  ('44553', 'Peltier', 'Physics', 56),
  ('45678', 'Levy', 'Physics', 46),
  ('54321', 'Williams', 'Comp. Sci.', 54),
  ('55739', 'Sanchez', 'Music', 38),
  ('70557', 'Snow', 'Physics', 0),
  ('76543', 'Brown', 'Comp. Sci.', 58),
  ('76653', 'Aoi', 'Elec. Eng.', 60),
  ('98765', 'Bourikas', 'Elec. Eng.', 98),
  ('98988', 'Tanaka', 'Biology', 120);

-- Verify the inserted data
SELECT * FROM student;
```


takes
```sql
CREATE TABLE takes (
    ID INT, 
    course_id varchar(30),
    sec_id varchar(30),
    semester varchar(30),
    year INT,
    grade varchar(2),

    PRIMARY KEY (ID, course_id, sec_id, semester, year)
);
```

