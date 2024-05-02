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



#### Web Design

**Quản lý tag, role**
trang1:  input nhập để nhập tên , description
trang2: trang để xem tag. 1 Bảng tag sẽ hiện thị lên, bên phải có 2 action là Edit và Delete
trang3: trang edit. Sẽ hiện thị đầy đủ thông tin tag, có 1 nút Edit và Delete phía dứới 

**Quản lý dự án**
trang 1: Cho phép người dùng điền đầy đủ thông tin dự án
trang 2: Hiện thị 1 bảng bao gồm 1 số cột c thấy quan trọng. Bên phải có nút Edit và Delete
trang3: Trang edit. Sẽ hiện thị đầy đủ thông tin của dự án, có 1 nút Edit và Delete phía dứới 

**Trang Nhân viên**
trang 1: Điền thông tin của nhân viên và sẽ có thêm lựa chọn thêm Skills từ 1 cái bảng lọc tag (vd như hình dưới kia). 
trang 2: 1 Bảng hiện thị thông tin cơ bản của nhân viên. Bảng đó có tầm 5 cột để hiện thị Tên, Email, Dự án đang tham gia, Team đang tham gia, và Kĩ năng. (cột nào ko có dữ liệu thì hiện thị là "Not Join". Bên phải có 3 nút, Detail, Edit, Delete
trang 3: Như các trang trên. Trang edit sẽ có thêm cột lựa chọn Skills như trang 1 
trang4: (Detail -> trang 4) Do bảng nhân viên có quá nhiều thông tin để hiện thị hết. Nên trang 4 sẽ lo phần hiện thị toàn bộ thông tin của nhân viên.  

**Trang Team**
trang 1: có feature điền tên team và thêm thành viên vào team: 
1) Phần thứ nhất ở trên là 1 Thanh Lọc thông tin. 
> **Featurs**: gắn Tag cho nhân viên

Cơ bản thì lọc theo kĩ năng nhé. Ở trên có 1 input cho phép cậu tra các tag skills 
VD: sau khi tra đc tag skill JS thì bảng phía dưới sẽ hiện thông tin cơ bản của nhân viên đó. Bao gồm cả kĩ năng của nhân viên. 
(VD Thiết kế: cột chứa tag kĩ năng của nhân viên nhìn như hình màu xám ở dưới)  

2) 1 Bảng thông tin ở dưới thiết kế giống hệt bảng ở trang 2 của nhân viên. 
> **Feature**: hiện thị thông tin

note trang 2 của nhân viên: 1 Bảng hiện thị thông tin cơ bản của nhân viên. Bảng đó có tầm 5 cột để hiện thị Tên, Email, Dự án đang tham gia, Team đang tham gia, và Kĩ năng. (Cột nào ko có dữ liệu thì hiện thị là "Not Join". Bên phải có 3 nút, Detail, Edit, Delete 
*Ko phải giao diện nhưng mà t vẫn nói cho chi tiết: Các nút khi bấm vào thì cũng sẽ hướng tới các trang của nhân viên như bth.*

Trang 2: có 1 bảng hiện thị thông tin. Bảng đó có tầm 5 cột để hiện thị Team_name, Team_Skills (cột này có thể hiện thị 1 tag thể thiện kĩ năng team đó chuyên môn.), Participant(nghĩa là số lượng nhân viên trong team hay còn gọi là number_of_employee), project_name (dự án mà team đó tham gia),

Trang 3: Giao diện và quy trình edit giống như phần Tạo nhân viên ở trang 1. (vì nó cũng chỉ là tạo lại và thay thông tin)

**Feature Team cho Project** (thiết kế gần như tương tự Trang Team)
trang 1: Điền thông tin cơ bản của Project (mọi thông tin trong bảng project)
Phía dưới cùng có nút xác nhận. Bấm nút xác nhận sẽ chuyển tới Trang Chọn Team:

Giao diện gồm 2 phần. 
1) Phần thứ nhất ở trên là 1 Thanh Lọc thông tin. 
Cơ bản thì lọc theo kĩ năng nhé. Ở trên có 1 input cho phép cậu tra các tag skills 
VD: sau khi tra đc tag skill JS thì bảng phía dưới sẽ hiện thông tin cơ bản của Team. Bao gồm cả kĩ năng của nhân viên. 
(VD Thiết kế: cột chứa tag kĩ năng của nhân viên nhìn như hình màu xám ở dưới)  

2) Thiết kế Bảng giống kêt trang Team. Nhưng mà thay vì hiện thị thông tin nhân viên thì sẽ hiện thị thông tin Team
Giao diện bảng: Bảng hiện thị thông tin cơ bản của Team. Bảng đó có tầm 5 cột để hiện thị Team_name, Team_Skills (cột này có thể hiện thị 1 tag thể thiện kĩ năng team đó chuyên môn.), Participant (nghĩa là số lượng nhân viên trong team hay còn gọi là number_of_employee), project_name (dự án mà team đó tham gia), Bên phải có 3 nút, Detail, Edit, Delete 
*Các nút khi bấm vào thì cũng sẽ hướng tới các features của team như bth.*

trang2: Hiện thị 1 bảng để xem tổng quan các dự án. Bảng bao gồm tên name, number_of_employee, project_priority, start_data, end_date, project manager. Bên phải có 3 nút, Detail, Edit, Delete 

trang 3: Giao diện và quy trình edit giống như phần tạo dự án. (vì nó cũng chỉ là tạo lại và thay thông tin)

trang 4: khi bấm vào Detail sẽ hiện thị toàn bộ thông tin chi tiết của dự án đó. Bao gồm mọi thông tin của dự án và team tham gia dự án đó.



### Insertion
note: 
```sql
SET IDENTITY_INSERT Employee ON;
SET IDENTITY_INSERT Employee OFF;
```

```sql
INSERT INTO Employee (first_name, last_name, email, phone_number, address, birth_date, hire_date)
VALUES 
    ('Michael', 'Johnson', 'michael.johnson@example.com', '555-123-4567', '789 Oak St, City, Country', '1985-07-10', '2019-06-01'),
    ('Emily', 'Davis', 'emily.davis@example.com', '555-987-6543', '321 Pine St, City, Country', '1992-03-25', '2021-02-15'),
    ('David', 'Wilson', 'david.wilson@example.com', '555-456-7890', '456 Maple St, City, Country', '1988-11-18', '2018-09-01'),
    ('Sarah', 'Anderson', 'sarah.anderson@example.com', '555-789-1234', '987 Cedar St, City, Country', '1991-09-03', '2020-12-01'),
    ('Christopher', 'Brown', 'christopher.brown@example.com', '555-234-5678', '654 Walnut St, City, Country', '1987-12-07', '2017-03-15')
    ('Sarah', 'Smith', 'sarah.smith@example.com', '555-987-6543', '123 Maple Ave, City, Country', '1990-03-15', '2020-02-15');
```


```sql

INSERT INTO Project (name, goal, number_of_employees, prefer_team, project_priority, project_status, start_date, end_date, project_manager_id)
VALUES  
    ('Project A', 'Caffee Shop Website', 0, '["Web Development", "Tester", "Marketing"]', 'High', 'In Progress', '2023-01-01', NULL, 1),
    ('Project F', 'Integration of AI into Existing Systems', 0, '["Artificial Intelligence", "Machine Learning", "Software Engineering"]', 'High', 'In Progress', '2023-06-15', NULL, 5),
    ('Project C', 'Mobile Application Development', 0, '["Mobile Development", "QA", "Backend Development"]', 'High', 'In Progress', '2023-02-28', NULL, 3),
    ('Project B', 'E-commerce Platform Development', 0, '["Web Development", "Database Administration", "UI/UX Design"]', 'Medium', 'Pending', '2023-04-15', NULL, 2),
    ('Project D', 'Data Analysis Platform Development', 0, '["Data Science", "Database Administration", "Business Analysis"]', 'Medium', 'Pending', '2023-03-10', NULL, 4),
    ('Project E', 'Internet of Things (IoT) Solution Development', 0, '["Embedded Systems", "Cloud Computing", "Data Engineering"]', 'High', 'In Progress', '2023-05-01', NULL, 6);

select * from Project
```


![[Pasted image 20240502160108.png]]