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


### Document Form

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