**Overview**

#### User Description
**user: guest**
+ Register (Create instructor/student Account)
(Add later: acocunt register to be instructor need to be verify by admin)

+ ! notice: Assignment contain 1 to many exercise.
**user: instructor** (Thành, Minh Nhật, Minh Hải, Quang Huy)
+ Login

	+ ! Assignment contain many Questions. Like a Folder contain many Files. 
+ Manage Question
	+ Create Question
	+ View Question (from Question Bank)
	+ Edit Question
	+ Delete Question
(Questions can be added to a Assignments later)

+ Manage Assignments
	+ Create Assignment
	+ Publish Assignments (to Draft)
	+ View Assignment
		+ View Draft Assignments (View assignments waiting to be Publish)
		+ View Opened Assignments
		+ View Closed Assignments
		+ View Finalized Assignment
		
	+ Score Assignment along with ChatGPT
	+ Finalized Assignments (Finalize Scored Assignment)


**user: student** (Xuân)
+ Login
+ View Assignment 
	+ View Public Assignments
	+ View Enrolled Assignment
	+ View Ongoing Assignment
	+ View Finalized Assignment


	+ Join Assignment (from Public Assignments)
+ Atempt Assigment (from Ongoing Assignments)
+ Submit Assignment 


**user: admin** (Thành)
+ Manage User
	+ View Account
	+ Disable/Enable Account
	+ Delete Account
	+ Save Account




### Screen Flow: 

Welcome Screen
	![[Pasted image 20240224095216.png]]

user: Guest
+ Sign up as Instructor
	![[Pasted image 20240224095413.png]]
	+ press SIGN UP
		![[Pasted image 20240224095551.png]]
		Verifycation send to Gmail
		![[Pasted image 20240224095523.png]]

user: Instructor
+ Login
	![[Pasted image 20240224095802.png]]


### Main Page

Navbar
+ Create Question
	![[Pasted image 20240224100114.png]]
	+ press ADD NEW
		![[Pasted image 20240224100133.png]]
	+ press Submit (comfirm screen pop-up)
		![[Pasted image 20240224100232.png]]
		+ Yes -> go back to Create Question Screen
		+ No -> Pop-up Disappear

+ Question Bank
+ ---------------
+ Create Assignment
	![[Pasted image 20240224100455.png]]
	select time
	+ EVENT
		![[Pasted image 20240224100527.png]]
	+ ACCESS_TIME
		![[Pasted image 20240224100536.png]]
	+ press NEXT
		![[Pasted image 20240224100603.png]]
	+ press Submit (comfirm screen pop-up)
		![[Pasted image 20240224100232.png]]

+ Draft Assignments
	![[Pasted image 20240224100719.png]]
	+ press PUBLISH -> Success Notification
		![[Pasted image 20240224101016.png]]

+ Publish Assignments
	![[Pasted image 20240224101031.png]]
	+ press OPEN -> Success Notification
		![[Pasted image 20240224101016.png]]
		Transfer Assignment 
+ Opened Assignments
	![[Pasted image 20240225140653.png]]
+ Closed Assignments (same Design)
	![[Pasted image 20240225140653.png]]
+ Finalized  Assignments
	![[Pasted image 20240225140745.png]]

**Summary:** This use case enables students to answer questions within a selected assignment.

**Actor:** Student

**Precondition:**

- The student is logged into the system.
- The student has selected a published assignment.

**Main Sequence:**

1. **Initiate Attempt:** The student selects the "Attempt Assignment" option.
2. **Question Display:** The system presents a list of questions from the assignment.
3. **Question Selection:** The student selects a specific question to answer.
4. **Question Details:** The system displays the question details (name, description, available points).
5. **Provide Response:** The student provides their answer within the designated input area.
6. **Submission (Implicit):** The student's response is recorded (this might trigger further actions like saving progress or submitting the entire assignment, which could be separate use cases).

**Alternative Sequence:**

- **Invalid Question:** If the selected question cannot be found (possible data issue), the system displays an error message.

**Postcondition:** The student has attempted to answer the selected question, and their response has been recorded by the system.


