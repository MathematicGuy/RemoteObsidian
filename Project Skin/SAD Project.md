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
id (key)
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
id (key)
employee_id
start date
end date
reason
status

**Attendance**
id (key)
employee_id
date
check_in_time
check_out_time

**Salary**
id (key)
employee_id
salary_date
salary_amount

**Departments**
id (key)
department_name
location
head_of_department
department_goal
performance_metrics

**Skills**
id (key)
skill_name
skill_description
skill_category_id

**Skills Category**
id (key)
skill_category_name

**Experience**
employee_id (key)
company_name
previous_role
year
skills

**Project**
id (key)
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
id (key)
team_name
team_lead_id
description

**User Roles**
id (key)
role_name

**Permissions**
id (key)
permission_name 


#### Connection Table

**Employee Skills**
employee_id; PK, FK1
skill id ; PK, FK2

**Team Allocation**


**Project Skills**


**Role Permissions**


#### Connection ()
Employees(id) to Employees(manager_id) - one to many