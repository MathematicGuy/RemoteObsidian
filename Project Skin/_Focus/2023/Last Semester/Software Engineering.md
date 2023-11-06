[ONIX Solution Company ](https://onix-systems.com/contact-us?salesChannel=7+basic+software+development+models+which+one+to+choose) 

# Lecture 1: Software Engineering Overview
SDLC ( software developement lifecycle)
(vòng tuần hoàn thiết kế phần mềm)

Bản chất phần mềm là thay đổi. (do nhu cầu con )

Cấu trúc phầm mềm
+ Có chuẩn hóa (1 quy tắc chung, định nghĩa chung) -> quan trọng
"Không thể áp dụng các quy tắc của dự án nhỏ cho dự án lớn"

Kĩ năng xây dựng hệ thống, giao tiếp chiếm phần lớp trong các dự án. Lập trình chỉ chiếm 1 phần nhỏ.

Các cách tiếp cận dự án:
+ Cẩn thận
	Phân tích thiết kế rồi mới tiến hành code, kiểm thử. Viết tài liệu cẩn thận

[7 Mô hình](https://onix-systems.com/blog/7-basic-software-development-models-which-one-to-choose)
[10 Software Design Pattern Video](https://youtu.be/WnMQ8HlmeXc?si=F1NlKaYwZ6Y4FUaE) 
+ thác nước 
	- ưu điểm: làm từng bước 1, tuần tự 
	- điểm yếu: chỉ làm theo mẫu, kiến trúc thấp. (khách hàng không góp ý)
+ chữ V -( cứ 1 bước kiểm thử 1 lần (phân tích/kiểm thử, code/kiểm thử, v..v.. )
mô hình bản mẫu ( xây dựng dựa theo bản mẫu, làm từng bước cùng vs khách hàng, làm demo)
	+ demo giao diện trên photoshop
	+ xây dựng tương đối, các chức năng chưa hoàn hảo
	- không có phân tích bản mẫu, kiến trúc không cao (Vì góp ý mới sửa)
+ xoắn ốc = thác nước + chữ V
	+ Xác định nhu cầu
	+ Lập kế hoạch
	+ Làm mẫu
	+ Khích lệ (làm ra mô hình đó)
	+ làm bài bản nhưng có làm mẫu trước từng bước rồi đưa khách hàng.


[Kiểm thử](https://www.indeed.com/career-advice/career-development/phases-of-testing)
[Kiểm thử Trắng và Đen](https://www.practitest.com/resource-center/article/black-box-vs-white-box-testing/#:~:text=The%20Black%20Box%20Test%20is,into%20consideration%20its%20internal%20functioning.)
Kiểm thử hộp trắng 
	+ Phát hiện đầu đủ
	- Khó biết hết dữ liệu
Kiểm thử Hộp đen (Chương trình)
	Nhập dữ liệu vào -> kq ra
	chạy mô phỏng thật

Mô hình tăng triển và lặp lại có tính chu 
	Tăng triển -> phát triển ở các thời điểm/tốc độ khác nhau và đc gán vào khi hoàn thiện.  
	Lặp -> thường đc quay lại để phát triển.

Nên chọn mô hình nào?

UML - Unified Modeling Language (Ngôn ngữ mô hình kí hiệu thống nhất) 
	Như là dấu ngoặc thì làm gì, dấu * thì làm gì đối vs mọi dự án.

[UML Diagram Types](https://creately.com/blog/diagrams/uml-diagram-types-examples/)
[Types of UML:](https://www.google.com/search?q=uml+diagram+types&rlz=1C1YTUH_viVN1071VN1072&oq=UML+diagram+types&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyDAgBEAAYFBiHAhiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhgeqAIAsAIA&sourceid=chrome&ie=UTF-8) 9 Diagrams
	![[Pasted image 20231024144200.png]]
**Structure Diagrams**
+ Composite Structure Diagrams
+ Deployment Diagrams
+ Component Diagrams
+ Class diagrams
+ Object diagrams
+ Package diagrams


**Behavioral Diagrams**
+ State Machine Diagrams
+ Communication Diagrams
+ [Use Case Diagrams](https://thinhnotes.com/chuyen-nghe-ba/use-case-diagram-va-5-sai-lam-thuong-gap/)
+ Activity Diagrams
+ Sequence Diagrams
+ Timing Diagrams
+ Interaction overview Diagrams

**CASE technology**`

[UML Turtorial](https://thinhnotes.com/chuyen-nghe-ba/use-case-diagram-va-5-sai-lam-thuong-gap/)
	có thể viết hộ code sau khi Thiết Kế.
Quan tâm tới sự giao tiếp hơn quy trình

# Lecture 2: Project Managment Basics

**KISS Principle** (keep it simple, stupid) -> Key to Design
+ Keep it short and simple
+ keep it simple and straightforward 

**Quản lý dự án**
>Organizing and managing resource so that project complete within a define scope, budget, time and on constraints.
	**Managements**
	+ Scope
	+ Time
	+ Cost
	+ Quality
	+ Human Resource
	+ Communication
	+ Risk
	+ Procurement (trang thiết bị)

FAIL, WHY?
+ unrealistic goals and objective management.
+ over expectation
+ chaging requirement (on development)

Client & Project Reviews
**Reviews**
+ Client -> access progress of development to comfirm or change requirement
+ Project -> proj manageer to assess status, teams to exchange info/knowedge
+ Peer Reviews -> document / code inspection and walkthrough from your colleges
+ Status -> regular team meeting

**Project Scheduling**
	Slit task into smallest/simplest task.
	WBS (Work Breakdown Structure)
1) Create WBS
2) Task List
3) Sequence Task
4) Estimate Duration
5) Project Network DIagram
6) Develop Schedule

Gantt -> show project schedule of WBS elements along time axis

**Critical Path and Slack Time**
+ Critical path:
	+ A sequence of activities that take the longest time to complete.
	+ It’s called the critical path, because it has **no slack**.
	+ defines how long your project will take to complete
+ Non-Critical Path
	+ Can be Slack/Late
+ Slack Path ( or float )
	+ Refers to the amount of days or hours that various related tasks can be delayed without pushing the project back.

Definitions: Start and Finish Dates
+ Forward pass: determine the critical path(s)
	+ Compute the earliest date start & finish dates for each activities,
+ Backward pass: determine slack times
	 + Compute latest start & finish dates for each activities,
[How to Calculate Early Start, Late Start, Early Finish, Late Finish and Slack (Float)](https://www.pmcalculators.com/how-to-calculate-the-critical-path/)
Slack time ST of A: -ST(a) = LS(a) - ES(a)
![[Pasted image 20231031142000.png]]

##### 4) Estimate Duration
+ Key to any project plan and is especially prone in software engineering (times to write and test code)
**Use
Historical Data** 
	from experiance, history with inside and outside company.
**Expert Judgement**
	Get advice from experiance/senior programmer or use a software PJ Manager to provide estimates. 
**Whide band Delphi**
	*Each members give their estimations and discuss*
1) Each team members to make an estmation
2) Discusses the reasons for each estimations
3) Each member revises their estimation
4) Team discusses the reason for each estimation
5) Repair (3) and (4) until there is acceptable.
**Story Point**
	Evaluate each task base on amount of dififculty or effort (not time) then scale them from 1 to 10
**COCOMO**
	the COnstruction COst MOdel based on teams experience, estimates size of the programe in 1000s lines of code, cost drivers and product attributes. 
	 **Formalize method (function)** based on History Data and Expert Judgement. 
		Fomalize method -> *mathematical approaches to solving software (and hardware) problems at the requirements, specification, and design levels*

**Discussion Topics**
+ Requirement Elicitation
+ Requirements Analysis
+ Requirements Validation
+ Data Dictionary
+ Software Requirement Specifications
+ User Unterface Prototype

**Requirement Elicitation** (thu thập nhu cầu)
+ Interview (phỏng vấn)
+ Observation
+ Workshop
+ Legacy Product Study
+ Competitive Product Study
+ Prototype

**Type of Requirement** (note: e.g. mean for example) 
+ Functional requirements (YC Chức năng) > **Specifications of what the system must do**.
	+ **The information tobe displayed**
		e.g the system must display the current time in 24hr format 
	+ **Interface with other systems**
		e.g. The system must be able to use wifi to communicate all transactions with a client secure database.
+ [Non-Functional requirements](https://www.geeksforgeeks.org/non-functional-requirements-in-software-engineering/) (YC Phi Chức Năng) >  **are the constraints or the requirements imposed on the system**


Chú thích thuật ngũ

usecase -> báo cáo thực tế


