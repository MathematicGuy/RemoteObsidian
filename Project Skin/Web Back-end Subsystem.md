1.2.1 User Management Subsystem
Models
User (id, name, email, password hash, role)
UserController
All Users: Login, logout, password reset, basic profile editing
Admin Actions: Create, delete, modify user accounts, and assign roles.
Views
Login UI
Logout (functionality more than a specific UI)
Registration UI (if applicable)
Password Reset UI
Profile Editing UI
Admin:
Admin Dashboard UI
User Management UI (Teacher List, Student List)



1.2.2 Question Subsystem
Models
Question (name, description, total_points)
QuestionController
Teacher Actions:
Create a new question (add to Question Bank)
Edit an existing question
Delete a question (with checks to ensure it's not currently in use by any assignments)
Views (Teacher Only)
Question Bank UI:
List view of questions with search/filtering
Individual question editing forms
Create Assignment UI:
Mechanism to select questions from the bank and add them to an assignment.


1.2.3 Assignment Subsystem
Model
Assignment: (title, description, publish_time, close_time, status [draft, published, closed, finalized], created_by_teacher_id)
Question: (name, description, total_points)
AssignmentQuestion: (assignment_id, question_id) – For the many-to-one relationship
Controllers
AssignmentController:
Teacher Actions: Create, edit, delete, publish, close, finalize assignments.
Student Interaction: Handles the creation of StudentAssignment records when a student selects an assignment to attempt.
Views
Teacher:
Create Assignment UI
Question Bank UI (if separate)
Opened Assignment UI
Closed Assignment UI
Finalized Assignment UI
Student:
Published Assignment UI
Dashboard UI (potentially showing assignments with their own statuses – started, in-progress, etc.)


1.2.4 Submission Subsystem
Model
StudentAssignment: (id, student_id, assignment_id, status [in_progress, submitted, graded], created_date, total_point)
QuestionResponse: (id, student_assignment_id, question_id, question_name, question_description, point, response)
Feedback: (feedback_id, question_response_id, created_date, text)
Controllers (SubmissionController)
Student:
submitQuestionAnswer()
Create a new QuestionResponse record.
Embed relevant question details from the active question the student is working on.
Potentially update the StudentAssignment status if needed.
submitAssignment()
Might update the StudentAssignment status to "submitted."
Could trigger score calculation logic (more on this below).
Teacher:
viewClosedAssignment()
Fetch submitted Student’s Assignments 
GradeQuestion()
Teacher submit scored and feedback of the Question
Update the StudentAssignment total_score.
SubmitAssignment()
Submit to update Student’s Assignment to the Database..
Views
Student's "Finalized Assignment UI":
Present questions, responses, and any feedback alongside for easy review.
Teacher's "Grading UI":
Provide access to the same information as the student.
Include input fields for teacher-specific scores and feedback.


