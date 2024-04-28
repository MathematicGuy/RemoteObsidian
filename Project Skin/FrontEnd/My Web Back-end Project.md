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
```js
@startuml
start
:Select "Manage Questions";
:Display list of questions;
:Admin selects a question;
if (Question exists?) then (yes)
    switch (Manage Question Actions?)
    case (Create)
      :Create Question;
    case (Update) 
      :Update Question;
    case (Read) 
      :Read Question;
    case (Delete) 
      :Delete Question;
    endswitch
else (no)
    :Display Error Message;
endif 
stop
@enduml
```

Publish Assignment
```js
@startuml
!pragma useVerticalIf on 
start 
if (Teacher logged in?) then (yes)
    :Select "Publish Assignment";
    repeat :Teacher provides details;
    backward: Prompt for missing details;
    repeat while (All details provided?) is (no)
    -> yes;
    :Publish Assignment;
else (no) 
    stop 
endif
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