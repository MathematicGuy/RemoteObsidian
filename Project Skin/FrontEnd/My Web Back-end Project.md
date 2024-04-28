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


|     |                          |                           |                                                                                 |
| --- | ------------------------ | ------------------------- | ------------------------------------------------------------------------------- |
| ID  | Feature                  | Use Case                  | Use Case Description                                                            |
| 01  | User registration        | Register                  | Creates a new account on the system                                             |
| 02  | User authentication      | Log in                    | Log in to the system                                                            |
| 03  | User authentication      | Log out                   | Log out of the system                                                           |
| 04  | User authentication      | Forget password           | Set new password if user forgot old password                                    |
| 05  | User profile management  | Change password           | Set new password                                                                |
| 06  | User profile management  | Edit profile              | Modify user personal information                                                |
| 07  | Participation Management | Join Assignment           | Students participate in classes as authorized by the instructor                 |
| 08  | Assignment Management    | Attempt Assignment        | Students do the available exercises                                             |
| 09  | Submission  Management   | Submit Assignment         | Students do the exercise until it is confirmed to be correct, then click submit |
| 10  | Viewing Management       | View Public Assignment    | See what exercises are allowed                                                  |
| 11  | Viewing Management       | View Enrolled Assignment  | View registered exercises                                                       |
| 12  | Viewing Management       | View Ongoing Assignment   | See which exercises are currently available                                     |
| 13  | Viewing Management       | View Finalized Assignment | Students can view details of completed assignments                              |
| 14  | Manage Questions         | Create Question           | Create Question to put in Assignment                                            |
| 15  | Manage Questions         | View Question             | View all Question                                                               |
| 16  | Manage Questions         | Edit Question             | Edit available Question                                                         |
| 17  | Manage Questions         | Delete Question           | Delete available Question                                                       |
| 18  | Manage Assignments       | View Draft Assignments    | Display Draft Assignment before publish                                         |
| 19  | Manage Assignments       | Create Assignment         | Create Assignment with questions                                                |
| 20  | Manage Assignments       | Publish Assignments       | Publish Assignment for students                                                 |
| 21  | Manage Assignments       | View Assignments          | Display Published Assignments                                                   |
| 22  | Manage Assignments       | Finalized Assignments     | Ending Assignments that have been Scored                                        |
| 23  | Manage Assignments       | Edit Assignments          | Modify available Assignment                                                     |
| 24  | Manage Assignments       | Delete Assignments        | Delete available Assignment                                                     |
| 25  | Manage Score             | Export Score              | Export Score to pdf, csv, txt, etc..                                            |
| 26  | Manage Bot               | Modify Bot                | Modify Bot version, Type, etc…                                                  |
| 27  | Manage Users Account     | Fine-tune Bot             | Remove property from wishlist                                                   |
| 28  | Manage Users Account     | Verify User Account       | Verify teacher & student account                                                |
| 29  | Manage Users Account     | Disable Account           | Disable account usability                                                       |
| 30  | Manage Users Account     | View Account              | View user account                                                               |