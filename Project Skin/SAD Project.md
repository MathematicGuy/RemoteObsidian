teamname: WeDoneWhatWeWant
pass: WDWWW

Hệ thống quản lý nhân viên (EMS) được thiết kế chủ yếu hướng tới
quản lý bộ phận và dự án được thiết kế để tối ưu hóa điều phối và quản lý các phòng ban và dự án khác nhau
trong một tổ chức.

Các **tính năng chính có thể bao gồm:**

• Quản lý thông tin cá nhân: Lưu trữ chi tiết nhân viên
hồ sơ.

• Phòng Quản lý: Tổ chức và quản lý thông tin cụ thể của bộ phận, bao gồm cả bộ phận mục tiêu, nhân sự và các thước đo hiệu suất.

• Phân bổ dự án: Phân công nhân viên vào các dự án dựa trên
kỹ năng, kinh nghiệm và mục tiêu của bộ phận, đảm bảo tối ưu
Trang 3 trên 4 thành phần nhóm dự án.

Các tính năng bổ sung có thể được bao gồm là:
• Quản lý chấm công và nghỉ phép: Theo dõi giờ làm việc,
vắng mặt và yêu cầu nghỉ phé


### Planning
1) **Project Initiation**
**Do it from Scratch**
+ Choose Main Topic -> Business Problem 
+ Use Case
+ Make Database Schema
**Alternative** 
+ Choose an Database Schema from Internet
+ State the Business Problems
+ Use Case
**both**
+ Sketch out project plan


2) **Data Modelling**
+ Design ER -> Implemented in SQL
+ Migrate SQL -> NoSQL (An)
+ Use ER to explain 
	MongoDB collections and their relationships, demonstrating an
	understanding of both SQL and NoSQL data modeling


3) **Querying and Data Manipulation** (An + Thành)
+ Construct wireframes for the system's
	Basic System Functionalities (Hệ thống làm gì)


(Triển khai bằng SQL query)
**Demonstrate functionalities with SQL:**
+ Basic SQL: CRUD Operation 
+ Advance SQL: Trigger, Store Procedures and Transactions. 
	+ Give example with Relevant use cases
		+ Explain its effectiveness


4) **Critical Analysis**
Analyze and Articulate 
+ **Pros and Cons of SQL (MSSQL) and NoSQl (MongoDB)** 
	+ then give realife Example (đưa ra vd thực tế) 
+ **Evaluate the work (on ours system)**
	+ **Evaluation Criteria**
		+ Data Consistensy 
		+ Data Model 
		+ Querying Needs
	+ **Evaluation Process**
		+ Which factors important the most (Yếu tố quan trọng nhất)
		+ Trade off (Better This but Worsten That) (Đánh Đổi - có thể đánh đổi cái gì để tối ưu hệ thống) - Như viết nhanh hơn, chấp nhận đọc chậm hơn 
5) **Presentation, Questions and Answer**
+ Present on Canvas 
+ Do some Prep (May Have) Questions to prepare for the real Presentation

[[SAD Project Archive]]

### SAD Project Document 

**Project**
```sql
CREATE TABLE project (
    project_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing ID
    name NVARCHAR(30) NOT NULL, 
    goal NVARCHAR(50) NOT NULL,
    number_of_employees INT, -- More flexibility than restricting beforehand
    prefer_skills NVARCHAR(255), -- Allow for more descriptive skills listing
    priority VARCHAR(10) CHECK (priority IN ('Low', 'Medium', 'High')), -- Enforce valid priorities
    status NVARCHAR(20) CHECK (status IN ('Open', 'In Progress', 'Completed', 'On Hold')),  -- Predefined statuses
    start_date DATETIME NOT NULL,
    end_date DATETIME 
); 
```


![[Pasted image 20240421225908.png]]

**Employee**
```sql
CREATE TABLE employee (
    employee_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing ID
    first_name NVARCHAR(30) NOT NULL,
    last_name NVARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,  -- Enforce unique emails
    phone_number VARCHAR(15), -- More flexible format than CHAR
    address NVARCHAR(75),
    birth_date DATE,  -- DATE might be sufficient if you don't need time
    hire_date DATE  NOT NULL,
    manager_id INT NULL, 
    FOREIGN KEY (manager_id) REFERENCES employee(employee_id) -- Self-referential foreign key
);
```


Query for employee manager
```sql
SELECT p.project_id, p.name, 
       m.first_name AS 'Manager First Name', m.last_name AS 'Manager Last Name' 
FROM project p 
JOIN employee m ON p.project_manager_id = m.employee_id
WHERE p.project_id = 123; -- Example project ID
```

**Task**
```sql
CREATE TABLE task (
    task_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing ID
    task_name NVARCHAR(30) NOT NULL,
    task_description NVARCHAR(100), 
    task_priority VARCHAR(10) CHECK (task_priority IN ('Low', 'Medium', 'High', 'Urgent')), -- Enforce priorities
    status NVARCHAR(20) CHECK (status IN ('Open', 'In Progress', 'Completed', 'On Hold')), -- Predefined statuses
    due_date DATETIME, 
    assigned_employee_id INT NULL, -- Allow for unassigned tasks initially
    FOREIGN KEY (assigned_employee_id) REFERENCES employee(employee_id) 
); 
```

**Team**
```sql
CREATE TABLE team (
    team_id INT PRIMARY KEY IDENTITY(1,1), 
    team_name NVARCHAR(30) UNIQUE NOT NULL, 
    team_lead_id INT,  -- Could be NULL initially
    FOREIGN KEY (team_lead_id) REFERENCES employee(employee_id) 
); 
```


Team_Task
```sql
CREATE TABLE team_task_assignment (
    team_id INT NOT NULL, 
    task_id INT NOT NULL,
    PRIMARY KEY (team_id, task_id), -- Composite key 
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (task_id) REFERENCES task(task_id),
); 
```

select task assignment

**Skills**
```sql
CREATE TABLE skill (
    skill_id INT PRIMARY KEY IDENTITY(1,1), 
    skill_name NVARCHAR(50) UNIQUE NOT NULL,  -- Enforce unique skill names
    skill_description NVARCHAR(100) 
); 
```


**Roles**
```sql
CREATE TABLE role (
    role_id INT PRIMARY KEY IDENTITY(1,1), 
    role_name NVARCHAR(50) UNIQUE NOT NULL,  -- Enforce unique role names
    role_description NVARCHAR(200) 
); 
```
