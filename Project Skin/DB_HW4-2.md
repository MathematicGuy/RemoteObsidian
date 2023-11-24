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
    ID varchar(5), 
    course_id varchar(30),
    sec_id varchar(30),
    semester varchar(30),
    year INT,
    grade varchar(2),

    PRIMARY KEY (ID, course_id, sec_id, semester, year)
);
```

```sql
INSERT INTO takes (ID, course_id, sec_id, semester, year, grade)
VALUES
  ('00128', 'CS-101', 1, 'Fall', 2009, 'A'),
  ('00128', 'CS-347', 1, 'Fall', 2009, 'A-'),
  ('12345', 'CS-101', 1, 'Fall', 2010, 'C'),
  ('12345', 'CS-190', 2, 'Spring', 2009, 'A'),
  ('12345', 'CS-315', 1, 'Spring', 2010, 'A'),
  ('12345', 'CS-347', 1, 'Fall', 2010, 'A'),
  ('19991', 'HIS-351', 1, 'Spring', 2009, 'B'),
  ('23121', 'FIN-201', 1, 'Spring', 2009, 'C+'),
  ('44553', 'PHY-101', 1, 'Fall', 2010, 'B-'),
  ('45678', 'CS-101', 1, 'Fall', 2010, 'F'),
  ('45678', 'CS-101', 1, 'Spring', 2009, 'B+'),
  ('45678', 'CS-319', 1, 'Spring', 2009, 'B'),
  ('54321', 'CS-101', 1, 'Fall', 2010, 'A-'),
  ('54321', 'CS-190', 2, 'Spring', 2009, 'B+'),
  ('55739', 'MU-199', 1, 'Spring', 2010, 'A-'),
  ('76543', 'CS-101', 1, 'Fall', 2009, 'A'),
  ('76543', 'CS-319', 2, 'Fall', 2009, 'A'),
  ('76653', 'EE-181', 1, 'Spring', 2010, 'C'),
  ('98765', 'CS-101', 1, 'Fall', 2010, 'C-'),
  ('98765', 'CS-315', 1, 'Spring', 2009, 'B'),
  ('98988', 'BIO-101', 1, 'Summer', 2010, 'A'),
  ('98988', 'BIO-301', 1, 'Summer', 2010, NULL);

-- Verify the inserted data
SELECT * FROM takes;
```

**4.2 Viết các câu lệnh sau trong SQL, sử dụng lược đồ CSDL university**

**a) Tìm tên của các môn học trong khoa Comp. Sci. mà có 3 tín chỉ**
```sql
select title from course where dept_name = 'Comp. Sci.' and credits = 3
```
![[Pasted image 20231123233148.png]]

**b) Tìm ID của tất cả các sinh viên mà được dạy bởi giảng viên có tên Einstein; và không
có các bộ trùng nhau trong quan hệ kết quả.**
```sql
select distinct ID from student where dept_name IN (select dept_name from instructor where name = 'Einstein')
```
![[Pasted image 20231123233130.png]]

**c) Tìm lương cao nhất của giảng viên**
```sql
select MAX(salary) from instructor
```
![[Pasted image 20231123233115.png]]

**d) Tìm tất cả các giảng viên có lương cao nhất (có thể có nhiều giảng viên cùng có lương
cao nhất).**
```sql
select name from instructor ORDER BY salary DESC
```
![[Pasted image 20231123233100.png]]


**e) Tìm số lượng sinh viên đăng ký của mỗi lớp học phần vào học kỳ Thu 2017.**
```sql
select COUNT(sec_id) from section where semester = 'Fall' and year = 2017
```
![[Pasted image 20231123233043.png]]


**f) Tìm các lớp học phần có số lượng đăng ký cao nhất vào học kỳ Thu 2017.**
note: group by: phân loại. 
	VD: group by sec_id là phân loại dựa theo mỗi sec_id
	![[Pasted image 20231123232914.png]]

```sql
SELECT sec_id, COUNT(*) as enrollment_count
FROM TAKES
WHERE semester = 'Fall' AND year = 2017
GROUP BY sec_id
ORDER BY enrollment_count DESC;
```
![[Pasted image 20231123233005.png]]


**g) Tạo một môn học mới với mã “CS-001”, tiêu đề “Weekly Seminar”, và 0 credits.**
```sql
insert into course (course_id, title, dept_name, credits)
VALUES
    ('CS-001', 'Weekly Seminar', '', 0)
```


**h) Tạo một lớp học phần (section) cho môn học đã tạo ở câu g) vào học kỳ Thu năm
2009, với sec_id là 1.**
```sql
insert into section (course_id, sec_id, semester, year, building, room_number, time_slot_id)
VALUES
    ('CS-001', 1,'Fall', 2009, '', '', '')  
```


**i) Ghi danh mọi sinh viên khoa Comp.Sci. vào section ở câu h).**
note: Ghi danh nghĩa là ghi danh sinh viên tham gia khóa học đó. E.g. student take CS-101
	There for insert student course enrollment to takes table 
```sql
-- Insert each student that take CS-101 to takes table
insert into takes (ID, course_id, sec_id, semester, year, grade)
select
    s.ID, 'CS-101', 1, 'Fall', 2009, NULL
FROM student s
where s.dept_name = 'Comp. Sci.'
-- Check for duplicate PRIMARY KEY VALUES
AND NOT EXISTS (
    select 1
    from takes t
    where t.id = s.id 
    and t.course_id = 'CS-101'
    and t.semester = 'Fall'
    and t.year = 2009
);
```


**j) Xóa đăng ký vào section ở câu h) của sinh viên có tên là Chavez.**
```sql
DECLARE @id varchar(5);
select @id = ID from student where name = 'Chavez';
delete from takes where ID = (@id)

-- Verify the inserted data
SELECT * FROM takes;
```


**k) Xóa môn học CS-001. Điều gì sẽ xảy ra nếu bạn thực hiện câu lệnh xóa này mà không
xóa các section của môn học này trước.**
```sql
delete from course where course_id = 'CS-001'
-- correct way to delete shoud be 
delete from takes where course_id = 'CS-001'
delete from section where course_id = 'CS-001'
delete from teaches where course_id = 'CS-001'
delete from prereq where course_id = 'CS-001'

delete from course where course_id = 'CS-001'
```
+ If I proceed this command without deleting  course_id = 'CS-001' from section, I will violate key Referential Integrity Constraint (ràng buộc tham chiếu) 


**m) Xóa tất cả các bộ trong quan hệ takes tương ứng với bất kỳ một section nào của bất kỳ
môn học nào có tiêu đề chứa từ “cơ sở dữ liệu” (bỏ qua trường hợp từ này khớp với tiêu
đề)**
```sql
DECLARE @db_course_id varchar(20);
select @db_course_id = course_id from course where title = 'cơ sở dữ liệu'

delete from takes WHERE course_id = (@db_course_id) 

SELECT * FROM takes;
```

**4.3 Viết câu lệnh SQL biểu diễn các câu truy vấn ở bài 3.3 (Bài tập chương 3)**
[[Company DB]]

**a. Đưa ra tên và địa chỉ của tất cả các nhân viên của phòng 1**
```sql
select Fname, Lname from EMPLOYEE where Dno = 1
```


**b. Cho biết tên và mã nhân viên của những nhân viên làm việc ở phòng
Research.**
```sql
select Fname, Lname, Ssn from EMPLOYEE 
where Dno = 
(select Dnumber from DEPARTMENT where Dname = 'Research')
```


**c. Cho biết tên dự án, mã dự án của những dự án do phòng Administration quản lý.**
```sql
select Pname, Pnumber from PROJECT
where Dnum = (select Dnumber from DEPARTMENT where Dname = 'Administration');
```


**d. Đưa ra tên của tất cả nhân viên của phòng 5 làm việc hơn 10 giờ trong dự án ProductX.**
```sql
select Fname, Lname from EMPLOYEE 
where Dno = 5 
and Ssn in 
	(select Essn from WORKS_ON where Hours > 10)
```
> note: In nghĩa là thuộc. Dùng khi so sánh vs nhiều giá trị. = để so sánh 1 vs 1 giá 


**e. Liệt kê tên của tất cả nhân viên có người phụ thuộc có cùng tên với họ. **
```sql
select Dependent_name from DEPENDENT 
where Essn IN (select Ssn from EMPLOYEE) 
```


**f. Tìm tên của tất cả nhân viên được 'Franklin Wong' trực tiếp giám sát.**
```sql
select Fname, Lname from EMPLOYEE 
where Super_ssn = (select Ssn from EMPLOYEE where Fname = 'Franklin' and Lname = 'Wong')
```


**g. Đối với mỗi dự án, hãy liệt kê tên dự án và tổng số giờ (của tất cả nhân viên) dành cho dự án đó.**
```sql
select Pno, SUM(Hours) as total_hours
from WORKS_ON 
where Pno IN (select Pnumber from PROJECT) group by Pno
```


**h. Truy xuất tên của tất cả nhân viên làm việc trong mọi dự án.**
```sql
--! count total project a employee work on
select Essn, COUNT(Pno) as total_project 
from WORKS_ON GROUP BY Essn
--! If total project = 6 -> select
having COUNT(Pno) = 6
```


**i. Đưa ra tên của tất cả nhân viên không làm việc trong bất kỳ dự án nào.**
```sql
--! count total project a employee work on
select Essn, COUNT(Pno) as total_project 
from WORKS_ON GROUP BY Essn
--! If total project = 6 -> select
having COUNT(Pno) = 0
```


**j. Đối với mỗi phòng, đưa ra tên phòng và mức lương trung bình của tất cả nhân viên làm việc trong phòng đó.**
```sql
select t2.Dname, AVG(t1.Salary) 
from EMPLOYEE as t1
JOIN DEPARTMENT as t2 ON t1.Super_ssn = t2.Mgr_ssn GROUP BY t2.Dname;
```


**k. Cho biết mức lương trung bình của tất cả nhân viên nữ.**
```sql
select AVG(Salary) as avg_f_salary from EMPLOYEE WHERE Sex = 'F' GROUP BY Ssn
```

