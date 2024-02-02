
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
