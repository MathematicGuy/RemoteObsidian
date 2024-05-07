[[My Web Back-end Note]]
[[Web Back-end WorkFlow]]
[[Web Back-end Subsystem]]

Part I: INTRODUCTION TO THE PROBLEM

Current Situation:

Describe the current methods used for exam management and code scoring. Highlight the pain points and limitations users face.
    Purpose: Clearly articulate the specific problems the system aims to solve and the value it will provide to students, examiners, and administrators.
    Requirements: Outline high-level requirements before diving into the detailed specifications in later sections.
    Scope of the Problem: Explicitly define what is included and what is excluded from the system's functionality. Consider these sub-sections:
        Functional Scope: List the core features the system will provide.
        Non-Functional Scope: Address performance, security, usability, maintainability, etc.
        Data Range: Specify the types and volume of data the system will handle.
        Technical Scope: Outline technology constraints or compatibility requirements.
        Scope of time and resources: Estimate project timelines and necessary resources (personnel, budget).
    WBS (Work Breakdown Structure): Visually break down the project into manageable work packages. A hierarchical structure is helpful here.
    Overview of Main Functions: Briefly describe the primary actions users will take within the system.
    General Use Case Diagram: A simple diagram visually representing the actors (users) and their interactions with the core system functions.
    Participating Members and Duties: Define the project team, stakeholders, and their specific roles and responsibilities.

Part II: SYSTEM ANALYSIS

Analyze Functional Requirements:
        Use Case Diagram:
            Describe the problem: Expand on each Use Case in detail, explaining the user's goals and the steps involved.
            Actor: Clearly define the types of users (e.g., student, examiner, administrator) and their roles within the system.
            Use Case: List and name specific actions users will be able to perform (e.g., create an exam, submit code, review code, generate scores).
            Diagram: Create a visual representation of the actors, use cases, and relationships between them.
            Description: Provide thorough written descriptions for each use case.
            Overall Functionalities
                Screens Flow: Outline typical navigation paths users will take through the system's interface.
                Screen Description: Detail the purpose and elements of each interface screen.
                Screen Authorization: Define access levels and permissions for different user roles.
        Activity Model: Use activity diagrams to illustrate the flow of processes and decisions within key use cases.

Analyze Non-Functional Requirements: Address performance requirements, security measures, usability standards, reliability, scalability, and maintainability considerations.

Part III: SYSTEM DESIGN

System Architecture Design:
        Describe the overall high-level structure of the system, including major components and their interactions. Consider using diagrams for clarity.
    Software System Subsystems: Break down the system into modules or subsystems, explaining their functions.
    Analyze Flows: Use data flow diagrams or sequence diagrams to model how information moves through the system.
    Database Design: Outline the database schema with entities, relationships, and attributes. Consider normalization principles.
    Interface Design: Focus on user-friendliness and provide mockups or wireframes of key screens.
    Test Case Design
        Develop comprehensive test cases to cover functionality, performance, security, and usability. Consider different testing scenarios.

Part IV: CONCLUSION

Summarize Completed Tasks: Provide an overview of what's been accomplished so far.
    Remaining Problems: Identify open issues and areas yet to be resolved.
    Development Direction: Outline the plan for tackling remaining challenges and completing the project.


Feedback to Thay Huy
Bọn em còn trẻ nên bọn em muốn tự quyết định việc bọn em muốn làm gì và phát triển theo hướng gì. Và cố gắng tránh việc đi theo 1 dự án của người khác những lúc mới bắt đầu để tránh việc tư duy bị đóng khung, làm bọn em mất dần khả năng tự đưa ra quyết định.


### Use Case

Actor: Guest, Student, Teacher, Admin
Guest:
**Relation between Actor and Use Cases** 
**Shared relation Student, Teacher and Admin**
+ Login
+ Logout
+ Forget Password
+ Manage Profile

**Both Student, Teacher** 
+ View Assignment
	*View Assignment include*
	+ View Public Assignment
	+ View Enrolled Assignment
	+ View On Going Assignment
	+ View Finalized Assignment

**Student**
+ Join Assignment
+ Attempt Assignment
+ Submit Assignment

**Teacher**
+ Manage Assignment
	*Manage Assignment include*
	+ Create Assignment
	+ View Draft Assignment
	+ Publish Assignment
	+ Finalized Assignment
	+ Edit Assignment
	+ Delete Assignment

+ Manage Question
	*Manage Assignment include*
	+ Create Question
	+ View Question
	+ Edit Question
	+ Delete Question

+ Grading (Grade Assignment)

**Admin**
Manage Bot
	*Manage Bot insclude*
	+ Modify Bot
	+ Fine-Tune Bot
Manage User Account
	+ View Account
	+ Disable Acocunt
	+ Verify 


Usecase Model
```js
@startuml
!theme plain
left to right direction
skinparam linetype ortho

actor Guest
actor Student
actor Teacher
actor Admin

rectangle "Assignment Management System" {
    usecase "Login"
    usecase "Logout"
    usecase "Forget Password"
    
    usecase "View Assignment" 
    usecase "Grade Assignment"
    usecase "View Public Assignment"
    usecase "View Enrolled Assignment"
    usecase "View OnGoing Assignment"
    usecase "View Finalized Assignment"

    usecase "Create Assignment"
    usecase "Publish Assignment"
    usecase "Edit Assignment"
    usecase "Delete Assignment"
    usecase "Finalized Assignment"
    
    usecase "Create Question"
    usecase "View Question"
    usecase "Edit Question"
    usecase "Delete Question"
    
    usecase "Modify Bot"
    usecase "Fine-Tune Bot"
    
    usecase "Verify User Account"
    usecase "Disable Account"
    usecase "View Account"

    usecase "Join Assignment" 
    usecase "Attempt Assignment" 
    usecase "Submit Assignment" 

    usecase "Export Score"
    usecase "Manage Assignment"
    usecase "Manage Question" 

    usecase "Manage Bot" 
    usecase "Manage User Account"  
    
    usecase "Manage Profile" 

    "View Assignment" --> (View Public Assignment) : <<include>>
    "View Assignment" --> (View Enrolled Assignment) : <<include>>
    "View Assignment" --> (View OnGoing Assignment) : <<include>>
    "View Assignment" --> (View Finalized Assignment) : <<include>>

    "Manage Assignment" --> (Create Assignment) : <<include>>
    "Manage Assignment" --> (Publish Assignment) : <<include>>
    "Manage Assignment" --> (Edit Assignment) : <<include>>
    "Manage Assignment" --> (Delete Assignment) : <<include>>
    "Manage Assignment" --> (Finalized Assignment) : <<include>>
    "Manage Assignment" --> (Grade Assignment) : <<include>>

    "Manage Question" --> (Create Question) : <<include>>
    "Manage Question" --> (View Question) : <<include>>
    "Manage Question" --> (Edit Question) : <<include>>
    "Manage Question" --> (Delete Question) : <<include>>

    "Manage Bot" --> (Modify Bot) : <<include>>
    "Manage Bot" --> (Fine-Tune Bot) : <<include>>

    "Manage User Account" --> (Verify User Account) : <<include>>
    "Manage User Account" --> (Disable Account) : <<include>>
    "Manage User Account" --> (View Account) : <<include>>

    "Manage Profile" --> (Change Password) : <<include>>
    "Manage Profile" --> (Edit Profile) : <<include>>

    Student --> "Join Assignment"
    Student --> "Attempt Assignment"
    Student --> "Submit Assignment"

    Guest --> "Login" 
    Student --> "Login" 
    Teacher --> "Login" 
    Admin <-- "Login"

    Guest --> "Logout"
    Student --> "Logout" 
    Teacher --> "Logout" 
    Admin <-- "Logout"

    Guest --> "Forget Password"
    Student --> "Forget Password"
    Teacher --> "Forget Password" 
    Admin <-- "Forget Password"

    Guest --> "Manage Profile"
    Student --> "Manage Profile"
    Teacher --> "Manage Profile"
    Admin <-- "Manage Profile"

    Guest --> "View Assignment"
    Student --> "View Assignment"
    Teacher --> "View Assignment"
    Admin <-- "View Assignment"

    Teacher --> "Create Assignment"
    Teacher --> "Edit Assignment"

    Admin <-- "Manage Bot"
    Admin <-- "Manage User Account" 
}
@enduml

```


#### Activity Description Template
Use case name: 
Summary: 
Actor:
Precondition: 
Main sequence:
1. 
2. 
3. 
Alternative sequence:
Postcondition: 


#### Activity Description and Code
Login
```js
@startuml
start
if (User logged in?) then (yes)
 :ActionsBasedOnRole;
else (no)
 :EnterCredentials;
 :VerifyCredentials;
-> login;
endif 
stop
@enduml
```

Manage Bot
```js
@startuml
start
:Admin selects Manage Bot;
:Display bot list;
if (Bot available?) then (yes)
    :Admin selects a bot;
    fork
        fork again
            :Modify Bot;
        fork again
            :Fine-tune Bot;
        end fork
    :Update Bot;
else (no)
    :Display "No Bots Found";
endif
stop
@enduml
```

Manage Question
-> fork in activity diagram allow parralel flow of activity
```js
@startuml
title Manage Question Use Case

start

:Select "Manage Questions";
:Display list of questions;
:Teacher selects a question;

if (Question exists?) then (yes)
    fork 
        fork again 
            :Create Question; 
        fork again
            :View Question Details (Read);
        fork again
            :Update Question;
        fork again 
            :Delete Question; 
        end fork 
else (no)
    :Display Error Message;
endif 

stop
@enduml 
```

Manage Assignment
```js
@startuml
title Manage Assignment Use Case

start

:Teacher selects "Manage Assignments";
:System Displays Assignment List;

if (Existing Assignments?) then (yes)
    fork
        fork again 
            :Create New Assignment; 
        fork again
            :View Assignment Details;
        fork again
            :Edit Assignment;
        fork again 
            :Delete Assignment;
        fork again 
            :Publish Assignment; 
        fork again 
            :Close Assignment;
        end fork
else (no)
    :System Displays: No Assignments; 
endif

stop
@enduml
```

Publish Assignment
```js
@startuml
title Publish Assignment Use Case

start

:Publish Assignment;
repeat :Provide Detail;
    backward:System Prompts: Missing Details;
     repeat while (All Details Provided?) is (no)
    -> yes;     
    
repeat: Add Question;
    backward: Prompt for missing detail;
    repeat while (Questions Added?) is (no)
     -> yes;
    :Publishes Assignment;
stop
@enduml
```

![[Pasted image 20240428232317.png]]

View Assignment
```js
@startuml
start
if (User logged in?) then (yes)
  :Select "View Assignments";
  :Display list of assignments;
  :User selects an assignment;
  if (Assignment exists?) then (yes)
    :Display assignment details;
  else (no)
    :Display Error Message;
  endif;
else (no)
  -> User not logged in;
endif;
stop
@enduml
```

![[Pasted image 20240428233357.png]]

Submit Assignment
```js
@startuml
title Submit Assignment Use Case

start
repeat :Assignment view;
:Student selects "Submit Assignmet";
:Comfirm Submition;
:Display confirmation dialog;
repeat while (assignment complete?) is (no)
-> yes;
    if (Confirm submission?) then (yes)
    fork
        :Record student responses;
        :Mark assignment as "submitted";
    fork again
        :Notify teacher;
    end fork
    else (no)
    endif
stop
@enduml
```


1.1. Introduction to the MVC model
1.1.1. Components in MVC
1.1.2. Processing flow in MVC
1.2 Facility management system subsystems
1.2.1.
1.2.2.
etc..

1.2 Facility management system subsystems
1.2.1. User Subsystem
● Model:
○ Users
○ Loan/return slip
● Controllers:
○ User Controller
○ Controller loan/return slip
● View:
	○ User interface

Knowing what your opponent know, is what help you give what your opponent need.



Work Flow Description

**Teacher**
**Question CRUD feature:**
+ Create Question: Teacher fills basic input (name, description).
+ Question Bank: Display Question Table with Edit Question Action and Delete Question Action for each Question.
**Assignment CRUD features:**  
+ Create Assignment: Teacher fill basic input (Name, Description, Start date, Due Date), add wanted Questions (at least 1 to many)
+ Publish Assignment: Teacher choose a Assignment from the Assignment List Table to publish
+ Opened Assignment: Display published Assignment with Edit Assignment Action and Delete Assignment Action
+ Closed Assignment: Display closed Assignment. cannot edit (assignment that pass due date)
+ Finalized Assignment: Display Scored Assignment of each Student in the Table with Edit Submission Action and a circle (green (done)/red (not done)) to show the status of each student to for each Assignment


**Student**  
**Assignment CRUD Features** 
+ Publish Assignment: Student choose a Assignment from the Assignment List Table to Enroll 
+ Enrolled Assignment: Display enrolled Assignment, student can attempt assignment 
+ Closed Assignment: Display Closed Assignment. student cannot attempt anymore (assignment that pass due date) 
+ Finalized Assignment: Display every Student's Assignment Scored. 
+ Submissions: Display student's attempted assignment and coding IDE on the Dashboard. Student can Submit Assignment after Finished. Submitted Assignment show Assignment finished time, State and Point in Dashboard. (note: Student will submit the whole Assignment, not per Question)


#### ER Diagram & Database 
ER
```js
@startuml
entity User {
  id : INT <<PK>>
  name : STRING
  email : STRING
  password_hash : STRING
  role : STRING
}

entity Question {
  id : INT <<PK>>
  name : STRING
  description : STRING
  total_points : INT
}

entity Assignment {
  id : INT <<PK>>
  title : STRING
  description : STRING
  publish_time : DATE
  close_time : DATE
  status : STRING
  created_by_teacher_id : INT <<FK>>
}

entity AssignmentQuestion {
  assignment_id : INT <<PK, FK1>>
  question_id : INT <<PK, FK2>>
}

entity StudentAssignment {
  id : INT <<PK>>
  student_id : INT <<FK>>
  assignment_id : INT <<FK>>
  status : STRING
  created_date : DATE
  total_points : INT
}

entity QuestionResponse {
  id : INT <<PK>>
  student_assignment_id : INT <<FK>>
  question_id : INT <<FK>>
  points : INT
  response : STRING
  status: String
}

entity Feedback {
  id : INT <<PK>>
  question_response_id : INT <<FK>>
  created_date : DATE
  text : STRING
}

User ||--o{ Assignment : created 
User ||--o{ StudentAssignment : created  
Assignment ||--|{ AssignmentQuestion: have
Question }|--|| AssignmentQuestion: contain
StudentAssignment }--o| QuestionResponse: contain
QuestionResponse ||--o{ Feedback: have
@enduml
```


DB
```js
@startuml
!theme vibrant

class User {
  id : INT <<PK>>
  name : STRING
  email : STRING
  password_hash : STRING
  role : STRING
}

class Question {
  id : INT <<PK>>
  name : STRING
  description : STRING
  total_points : INT
}

class Assignment {
  id : INT <<PK>>
  title : STRING
  description : STRING
  publish_time : DATE
  close_time : DATE
  status : STRING
  created_by_teacher_id : INT <<FK>>
} 

class AssignmentQuestion {
  assignment_id : INT <<PK, FK1>>
  question_id : INT <<PK, FK2>>
}

class StudentAssignment {
  id : INT <<PK>>
  student_id : INT <<FK>>
  assignment_id : INT <<FK>>
  status : STRING
  created_date : DATE
  total_points : INT
}

class QuestionResponse {
  id : INT <<PK>>
  student_assignment_id : INT <<FK>>
  question_id : INT <<FK>>
  points : INT
  response : STRING
  status: String
}

class Feedback {
  id : INT <<PK>>
  question_response_id : INT <<FK>>
  created_date : DATE
  text : STRING
}

User <|-- Assignment 
User <|-- StudentAssignment 
Assignment <|-- StudentAssignment 
Assignment <|-- AssignmentQuestion 
AssignmentQuestion --|> Question 
Question <|-- QuestionResponse 
User <|-- QuestionResponse 
StudentAssignment <|-- QuestionResponse 
QuestionResponse <|-- Feedback
@enduml
```
	![[Pasted image 20240503151618.png]]

