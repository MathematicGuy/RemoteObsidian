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
CREATE TABLE Project (
    project_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing ID
    name NVARCHAR(30) NOT NULL, 
    goal NVARCHAR(50) NOT NULL,
    number_of_employees INT, -- More flexibility than restricting beforehand
    prefer_skills NVARCHAR(255), -- Allow for more descriptive skills listing
    project_priority VARCHAR(10) CHECK (project_priority IN ('Low', 'Medium', 'High')), -- Enforce valid priorities
    project_status NVARCHAR(20) CHECK (project_status IN ('Pending', 'In Progress', 'Completed')),  -- Predefined statuses
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    project_manager_id int, 
    FOREIGN KEY (project_manager_id) REFERENCES Employee(employee_id) 
); 
```


**Project Assignment**
```sql
CREATE TABLE project_assignment (
    employee_id INT NOT NULL, 
    project_id INT NOT NULL,
    PRIMARY KEY (employee_id, project_id), 
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (project_id) REFERENCES Project(project_id) 
); 
```

**Employee**
```sql
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing ID
    first_name NVARCHAR(30) NOT NULL,
    last_name NVARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,  -- Enforce unique emails
    phone_number VARCHAR(15), -- More flexible format than CHAR
    address NVARCHAR(75),
    birth_date DATE,  -- DATE might be sufficient if you don't need time
    hire_date DATE  NOT NULL,
);
```

**Task**
```sql
CREATE TABLE Task (
    task_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing ID
    task_name NVARCHAR(30) NOT NULL,
    task_description NVARCHAR(100), 
    task_priority VARCHAR(10) CHECK (task_priority IN ('Low', 'Medium', 'High')), -- Enforce priorities
    status NVARCHAR(20) CHECK (status IN ('Pending', 'In Progress', 'Completed')), -- Predefined statuses
    due_date DATETIME, 
); 
```

**Team**
```sql
CREATE TABLE Team (
    team_id INT PRIMARY KEY IDENTITY(1,1), 
    team_name NVARCHAR(30) UNIQUE NOT NULL, 
	team_skill_id INT,  -- Could be NULL initially
	team_lead_id INT,  -- Could be NULL initially
    FOREIGN KEY (team_lead_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (team_skill_id) REFERENCES Skills(skill_id)
); 
```

**team_task**
```sql
CREATE TABLE team_task (
    team_id INT NOT NULL, 
    task_id INT NOT NULL,
    assigned_employee_id INT NULL, -- Allow for unassigned tasks initially
    PRIMARY KEY (team_id, task_id), -- Composite key 
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (task_id) REFERENCES Task(task_id),
    FOREIGN KEY (assigned_employee_id) REFERENCES Employee(employee_id),
); 
```

**team_project**
```sql
CREATE TABLE team_project(
    team_id INT NOT NULL, 
    project_id INT NOT NULL,
    PRIMARY KEY (team_id, project_id), 
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (project_id) REFERENCES Project(project_id) 
); 
```

**team_member**
```sql
CREATE TABLE team_member(
    role_id INT NOT NULL, 
    member_id INT NOT NULL,
	team_id INT NOT NULL,

    PRIMARY KEY (role_id, member_id, team_id), 
    FOREIGN KEY (role_id) REFERENCES Role(role_id),
    FOREIGN KEY (member_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id) 
); 
```


**Skills**
```sql
CREATE TABLE Skills(
    skill_id INT PRIMARY KEY IDENTITY(1,1), 
    skill_name NVARCHAR(50) UNIQUE NOT NULL,  -- Enforce unique skill names
    skill_description NVARCHAR(100) 
); 
```


**employee_skills**
```sql
CREATE TABLE employee_skills (
    employee_id INT NOT NULL, 
    skill_id INT NOT NULL,
    PRIMARY KEY (employee_id, skill_id), -- Composite key 
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id),
); 
```


**Roles**
```sql
CREATE TABLE Role (
    role_id INT PRIMARY KEY IDENTITY(1,1), 
    role_name NVARCHAR(50) UNIQUE NOT NULL,  -- Enforce unique role names
    role_description NVARCHAR(200) 
); 
```
