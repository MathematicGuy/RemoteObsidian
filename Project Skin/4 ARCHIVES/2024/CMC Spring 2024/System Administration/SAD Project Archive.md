### SAD Project Document ver 1.0 

#### Table
**Employees**
id (PK)
first_name
last_name
email
phone_number
address
birth date
hire_date
job_title
salary 
department_id
manager_id 

**Leave Requests**
id (PK)
employee_id
start date
end date
reason
status

**Attendance**
id (PK)
employee_id
date
check_in_time
check_out_time

**Salary**
id (PK)
employee_id
salary_date
salary_amount

**Departments**
id (PK)
department_name
location
head_of_department
department_goal
performance_metrics

**Skills**
id (PK)
skill_name
skill_description
skill_category_id (FK)

**Skills Category**
id (PK)
skill_category_name

**Experience**
employee_id (key)
company_name
previous_role
year
skills

**Project**
id (PK)
project_name
description
start_date
end_date
project_manager_id
status
budget
client 
project_goal

**Team**
id (PK)
team_name
team_lead_id
description

**User Roles**
id (PK)
role_name

**Permissions**
id (PK)
permission_name 


#### Connection Table

**Employee Skills**
employee_id (PK, FK1)
skill_id (PK, FK2)

**Team Allocation**
project_id (PK, FK1)
team_id (PK, FK2)
employee_id (PK, FK3)
start_date
end_date
role
reason_for_allocation

**Project Skills**
project_id (PK, FK1)
skill_category_id (PK, FK2)
required_skill_level

**Role Permissions**
permission_id (PK, FK1)
role_id (PK, FK2)
employees_id

#### Connection 
Liệt kê các kết nối của các bảng -> Ghi chú PK, 

**Employee Table** 
Employees(id) to Employees(manager_id) - one to many (SELF-REFERENCING FOREIGN KEY)
Employees(id) to Leave_Requests(id) - one to one
Employees(id) to Attendance(id) - one to many
Employees(id) to Salary(id) - one to one
Employees(department_) to Departments(id) - one to many
Employees(id) to Employee Skills(employee_id) - one to many
Employees(id) to Role Permissions(employee_id) - many to one
 
Employees(id) to Experience(employee_id) - one to many
Employees(id) to Team allocation(employee_id) - many to one
 
**Skills Table**
Skills(id) to Employee Skills(skill_id) - one to many
Skills(skill_category_id) to Skills Category(id) - one to many

**Skills Category Table**
Skills Category(id) to Project skills(project_id) - one to many

**Team allocation**

#### [Crow foot Notation](https://www.freecodecamp.org/news/crows-foot-notation-relationship-symbols-and-how-to-read-diagrams/)
**Zero**
![[Pasted image 20240413114453.png]]

**One**
![[Pasted image 20240413114500.png]]

**Many**
![[Pasted image 20240413114511.png]]

**Zero or Many**
![[Pasted image 20240413114351.png]]

**One or Many**
![[Pasted image 20240413114521.png]]

**One and only One**
![[Pasted image 20240413114528.png]]

#### Example
![[Pasted image 20240413114623.png]]
> Teach can have 1 to many Course. But Course can have 1 and only 1 teacher


![[Pasted image 20240413114649.png]]
> 1 Customer can have 0 to many Pizza and 1 Pizza can have 0 to many customer


### Features

1. **Quản lý Dự án (Manager):**  
- Xem, sửa, thêm, xóa thông tin dự án: Cho phép quản lý dự án thực hiện các thao tác quản lý thông tin về dự án.  
- Quản lý nhân viên trong dự án: Cung cấp tính năng quản lý thành viên dự án, bao gồm xem, thêm, xóa, sửa thông tin nhân viên.  
- Quản lý team và team allocation: Cho phép quản lý gán nhân viên vào các nhóm công việc và quản lý phân bổ nhân sự cho các dự án.  
- Quản lý các kỹ năng cần có trong dự án: Cho phép quản lý thêm, sửa, xóa các kỹ năng cần thiết cho dự án.  
- Xem nhân viên phù hợp với dự án dựa trên kỹ năng: Cung cấp khả năng tìm kiếm và xem nhân viên có kỹ năng phù hợp với dự án.  
2. **Quản lý Thông tin Cá nhân của nhân viên (Manager và Head of department):**  
- Xem thông tin nhân viên: Hiển thị thông tin cá nhân của nhân viên.  
- Lọc thông tin nhân viên theo thuộc tính: Cho phép lọc thông tin nhân viên theo các thuộc tính như vị trí công việc, phòng ban, kỹ năng, ...  
3. **Quản lý Ban (Head of department):**  
- Xem, thêm, sửa thông tin ban: Cho phép quản lý thực hiện các thao tác quản lý thông tin của ban.  
- Xem nhân viên trong một ban: Hiển thị danh sách nhân viên thuộc về một ban cụ thể.  
- Đánh giá hiệu suất của nhân viên và phòng ban: Cung cấp tính năng đánh giá hiệu suất làm việc của nhân viên và tổng hợp hiệu suất của cả phòng ban.  
- Quản lý chấm công và nghỉ phép: Đánh giá và quản lý việc chấm công và đăng ký nghỉ phép của nhân viên trong phòng ban.  
4. **Chấm công (Employees):**  
- Chấm công bằng máy: Cho phép nhân viên sử dụng máy để chấm công và lưu trữ dữ liệu.  
5. **Quản trị hệ thống (Admin):**  
- Quản lý quyền các tài khoản: Cho phép quản trị viên thực hiện các thao tác quản lý về quyền truy cập của người dùng.  
- Tạo, đọc, cập nhật, xóa tài khoản người dùng: Cho phép quản trị viên thực hiện các thao tác quản lý về tài khoản người dùng trong hệ thống.  
Phân quyền cụ thể cho từng người dùng:  
- Employees: Chỉ có quyền điểm danh và xem số công.  
- Manager: Có quyền truy cập đầy đủ vào các tính năng quản lý dự án và quản lý thông tin cá nhân.  
- Head of department: Có quyền truy cập vào các tính năng quản lý phòng ban và thông tin cá nhân.  
- Admin: Có quyền quản lý hệ thống và tài khoản người dùng.

```sql
CREATE TABLE Employees (
  id int PRIMARY KEY,
  first_name nvarchar(200),
  last_name nvarchar(200),
  email varchar(30),
  phone_number varchar(10),
  address varchar(100),
  birth_date date,
  hire_date date,
  job_title nvarchar(50),
  salary int,
  department_id int,
  manager_id int, 
  CONSTRAINT FK_Employees_Manager FOREIGN KEY (manager_id)
    REFERENCES Employees(id) 
);
```

```sql
CREATE TABLE [Leave_Requests] (
  [id] int,
  [employee_id ] int,
  [start_date] date,
  [end_date] date,
  [reason] nvarchar(200),
  [status] varchar(10),
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE [Attendance] (
  [id] int,
  [employee_id ] int,
  [date] date,
  [check_in_time] time,
  [check_out_time] time,
  PRIMARY KEY ([id])
);

```

```sql
CREATE TABLE [Salary] (
  [id] int,
  [employee_id] int,
  [salary_date] date,
  [salary_amount] int,
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE [Departments] (
  [id] int,
  [department_name] nvarchar(50),
  [location] string,
  [head_of_department_id] int,
  [department_goal] nvarchar(200),
  [performance_metrics] int,
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE [Experience] (
  [employee_id] int,
  [company_name] nvarchar(200),
  [previous_role] varchar(50),
  [year] int,
  [skills] varchar(100),
  PRIMARY KEY ([employee_ id])
);


```

```sql
CREATE TABLE [Team] (
  [id] int,
  [team_name] nvarchar(30),
  [team_lead_id] int,
  [description] nvarchar(200),
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE Team_Allocation (
 project_id int,
 employee_id int,
 team_id int,
 start_date date,
 end_date date,
 role nchar(30),
 reason_for_allocation nvarchar(200),
 PRIMARY KEY (project_id, employee_id, team_id),
  CONSTRAINT FK_TeamAllocation_Project FOREIGN KEY (project_id) REFERENCES Project(id),
  CONSTRAINT FK_TeamAllocation_Employee FOREIGN KEY (employee_id) REFERENCES Employees(id),
  CONSTRAINT FK_TeamAllocation_Team FOREIGN KEY (team_id) REFERENCES Team(id) 
);
```

```sql
CREATE TABLE [Project] (
  [id] int,
  [project_name] nvarchar(200),
  [description] nvarchar(200),
  [start_date] date,
  [end_date] date,
  [project_manager_id] int,
  [status] varchar(10),
  [budget] int,
  [client ] nvarchar(50),
  [project_goal] nvarchar(200),
  PRIMARY KEY ([id])
);
```


**M-M**
```sql
CREATE TABLE [Employees] (
  [id] int,
  [first_name] nvarchar(200),
  [last_name] nvarchar(200),
  [email] varchar(30),
  [phone_number ] varchar(10),
  [address] varchar(100),
  [birth_date] date,
  [hire_date] date,
  [job_title ] nvarchar(50),
  [salary] int,
  [department_id] int,
  [manager_id] int,
  PRIMARY KEY ([id]),
  CONSTRAINT [FK_Employees.id]
    FOREIGN KEY ([id])
      REFERENCES [Employees]([manager_id])
);
```

```sql
CREATE TABLE Employee_Skills (
 [employee_id] int,
 [skill_id] int,
 PRIMARY KEY ([employee_id], [skill_id]),
  CONSTRAINT FK_EmployeeSkills_Employee FOREIGN KEY (employee_id) REFERENCES Employees(id), 
  CONSTRAINT FK_EmployeeSkills_Skill FOREIGN KEY (skill_id) REFERENCES Skills(id)
);

CREATE INDEX [FK1] ON [Employee Skills] ([employee_id]);
CREATE INDEX [FK2] ON [Employee Skills] ([skill_id]);

```

```sql
CREATE TABLE [Skills] (
  [id] int,
  [skill_name] nvarchar(30),
  [skill_description] nvarchar(200),
  [skill_category_id] int,
  PRIMARY KEY ([id])
);
```


M-M
```sql
CREATE TABLE [Permissions] (
  [id] int,
  [permission_name] nvarchar(50),
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE UserRole_Permissions (
  user_role_id int,
  permission_id int,
  PRIMARY KEY (user_role_id, permission_id),
  CONSTRAINT FK_UserRolePermissions_UserRole FOREIGN KEY (user_role_id) REFERENCES User_Roles(id),
  CONSTRAINT FK_UserRolePermissions_Permission FOREIGN KEY (permission_id) REFERENCES Permissions(id)
);


CREATE INDEX [FK1] ON  [Role Permissions] ([permission_id]);
CREATE INDEX [FK2] ON  [Role Permissions] ([role_id]);
```

```sql
CREATE TABLE [User Roles] (
  [id] int,
  [role_name] nvarchar(50),
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE [Accounts Role] (
  [name] int,
  [role_id] int,
  PRIMARY KEY ([name], [role_id])
);

CREATE INDEX [FK1] ON  [Accounts Role] ([name]);
CREATE INDEX [FK2] ON  [Accounts Role] ([role_id]);
```

	```sql
CREATE TABLE [Account ] (
  [name] nvarchar(200),
  [register_date] datetime,
  [password] nchar(100),
  PRIMARY KEY ([name])
);
```

M-M
```sql
CREATE TABLE [Skills] (
  [id] int,
  [skill_name] nvarchar(30),
  [skill_description] nvarchar(200),
  [skill_category_id] int,
  PRIMARY KEY ([id])
);
```

```sql
CREATE TABLE `Project skills` (
  `project_id` int,
  `skill_category_id` int,
  `required_skill_level` int,
  PRIMARY KEY (`project_id`, `skill_category_id`),
  KEY `FK1` (`project_id`),
  KEY `FK2` (`skill_category_id`)
);
```

```sql
CREATE TABLE [Project] (
  [id] int,
  [project_name] nvarchar(200),
  [description] nvarchar(200),
  [start_date] date,
  [end_date] date,
  [project_manager_id] int,
  [status] varchar(10),
  [budget] int,
  [client ] nvarchar(50),
  [project_goal] nvarchar(200),
  PRIMARY KEY ([id])
);
```


Check SQL Index

Constraint
```sql
ALTER TABLE Team 
ADD CONSTRAINT FK_Team_EmployeeTeamLead FOREIGN KEY (team_lead_id) 
    REFERENCES Employees(id); 

ALTER TABLE Experience 
ADD CONSTRAINT FK_Experience_Employee FOREIGN KEY (employee_id) 
    REFERENCES Employees(id); 

ALTER TABLE Project 
ADD CONSTRAINT FK_Project_EmployeeProjectManager FOREIGN KEY (project_manager_id) 
    REFERENCES Employees(id); 
```

