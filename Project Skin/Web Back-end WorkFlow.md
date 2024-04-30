**Scenario 1: Teacher Publishes Assignment**

1. **Teacher Initiates Action:**
    
    - Teacher accesses the "Opened Assignment UI" (likely a list of their draft assignments).
    - Teacher selects the "Publish" button or similar action next to an assignment.
2. **Controller Handles Publishing:** (`AssignmentController`)
    
    - Controller locates the correct `Assignment` record.
    - Controller performs checks:
        - Does the assignment have at least one question associated with it?
        - Any other validation rules you might have.
    - Controller updates the assignment's `status` to "published."
    - Controller sets the `publish_time` to the current timestamp.
3. **Model Updates:**
    
    - The changes to the `Assignment` entity are persisted in the database.
4. **View Updates:**
    
    - The "Opened Assignments UI" might automatically refresh to remove the now-published assignment.
    - The "Published Assignments UI" would likely update to show the newly available assignment.

**Scenario 2: Student Submits Entire Assignment**

1. **Student Finalizes Submission:**
    
    - Student is on the "Submissions UI" or similar, viewing their in-progress assignment.
    - Student clicks a "Submit Assignment" button.
2. **Controller Orchestrates Submission** (`SubmissionController`)
    
    - Controller locates the student's in-progress `Submission`.
    - Controller updates the `Submission` status to "completed".
    - Controller packages student responses and initiates a call to the ChatGPT API (likely asynchronously).
3. **ChatGPT Analysis (Behind the Scenes)**
    
    - ChatGPT receives the student's code and test cases (if applicable).
    - ChatGPT generates a response including feedback and a potential score.
    - This response is sent back to your application.
4. **Controller Handles Feedback**
    
    - `SubmissionController` receives the ChatGPT response.
    - Controller updates the `Submission` record with the score and feedback.
    - Controller creates a new `Feedback` record and associated `FeedbackContent` (author = "ChatGPT").
5. **View Updates**
    
    - Student's "Submissions UI" likely updates to show the assignment as submitted, potentially displaying the ChatGPT-generated score.

**Scenario 3: Teacher Grades a Submission**

1. **Teacher Accesses Grading:**
    
    - Teacher views the "Closed Assignment UI" or "Finalized Assignment UI."
    - Teacher selects a specific student submission to grade.
2. **Controller Fetches Data** (`SubmissionController`)
    
    - Controller loads the `Submission` including associated questions and student responses.
    - Controller fetches existing `Feedback` (from ChatGPT or any prior teacher input).
3. **View Renders Grading UI**
    
    - Controller passes data to the teacher grading view.
    - The view displays student code, ChatGPT feedback, a place to enter a score, and a text area for teacher feedback.
4. **Teacher Provides Feedback**
    
    - Teacher reviews the work and ChatGPT's assessment.
    - Teacher may adjust the score.
    - Teacher enters their own feedback in the provided text area.
5. **Controller Saves Changes**
    
    - Teacher clicks "Save" or similar.
    - `SubmissionController` updates the `Submission` score.
    - Controller creates a new `Feedback` record (author = "Teacher") and associated `FeedbackContent`.



### Class Diagram
example command: Create Class Diagram using PlantUML for Question Subsystem

#### User
```js
class User {
    - id : int
    - name : String
    - email : String
    - passwordHash : String
    - role : String 

    + login()
    + logout()
    + resetPassword()
    + editProfile()
}

class AdminController {
    + createUser()
    + deleteUser()
    + modifyUser()
    + assignRole()
}
```

#### Question
```js
@startuml
!theme vibrant
class Question {
    -name : String
    -description : String
    -totalPoints : int
    -isGlobal : boolean
}

class QuestionController {
    + createQuestion()
    + editQuestion()
    + deleteQuestion() 
}
@enduml
```


#### Assignment 
```js
@startuml
!theme vibrant
class Assignment {
    - title : String
    - description : String
    - publishTime : Datetime
    - closeTime : Datetime
    - status : String 
    - totalPoints: int
}

class Question {
    - name : String
    - description : String
    - point: int 
}

class AssignmentQuestion {
    - assignmentId: int
    - questionId: int
}

class AssignmentController {
    + viewPublishedAssignments() //Student
    + createAssignment() //Teacher
    + editAssignment() //Teacher
    + deleteAssignment() //Teacher
    + publishAssignment() //Teacher 
    + closeAssignment() //Teacher
    + finalizeAssignment() //Teacher
} 

Assignment "1" -- "*" AssignmentQuestion
AssignmentQuestion "*" -- "1" Question
@enduml
```


#### Submission
```js
@startuml
!theme vibrant

class StudentAssignment {
    - id : int
    - student_id : int
    - assignment_id : int
    - status : String 
    - created_date : Datetime
    - total_points: int
}

class QuestionResponse {
    - id : int 
    - student_assignment_id : int
    - question_id : int
    - question_name : String
    - question_description : String
    - points : int
    - response : String 
}

class Feedback {
    - feedback_id : int
    - question_response_id : int 
    - created_date : Datetime 
    - text : String
}

class SubmissionController {
    + submitQuestionAnswer() // Student
    + submitAssignment() // Student
    + viewClosedAssignment()  // Teacher
    + GradeQuestion()  // Teacher
    + SubmitAssignment()  // Teacher
}

StudentAssignment "1" -- "*" QuestionResponse
QuestionResponse "1" -- "*" Feedback
@enduml
```




### Backend subsystem Design

![[Pasted image 20240430175915.png]]
Submission Controller Code
```cs
public class StudentAssignment 
{
    public int Id { get; set; }
    public int StudentId { get; set; }
    public int AssignmentId { get; set; }
    public string Status { get; set; } // Consider using an enum for better type safety
    public DateTime CreatedDate { get; set; }
    public int TotalPoints { get; set; }

    // Navigation Property
    public ICollection<QuestionResponse> QuestionResponses { get; set; } 
}

public class QuestionResponse
{
    public int Id { get; set; }
    public int StudentAssignmentId { get; set; } // Foreign key
    public int QuestionId { get; set; }
    public string QuestionName { get; set; }
    public string QuestionDescription { get; set; }
    public int Points { get; set; } 
    public string Response { get; set; }

    // Navigation Property
    public StudentAssignment StudentAssignment { get; set; }
}
```
WebAPI Controller
```cs
// Inside your Web API Controller
public async Task<ActionResult<StudentAssignment>> GetStudentAssignment(int id)
{
    var assignment = await _context.StudentAssignments
                                   .Include(a => a.QuestionResponses)
                                   .FirstOrDefaultAsync(a => a.Id == id);

    if (assignment == null) return NotFound();

    return assignment; 
}
```



#### Assignment 
![[Pasted image 20240430180805.png]]
```cs
public class Assignment 
{
    public int Id { get; set; }
    // ... other properties ...

    public ICollection<AssignmentQuestion> AssignmentQuestions { get; set; }
}

public class Question
{
    public int Id { get; set; }
    // ... other properties ...

    public ICollection<AssignmentQuestion> AssignmentQuestions { get; set; }
}

public class AssignmentQuestion
{
    public int AssignmentId { get; set; }
    public int QuestionId { get; set; }

    public Assignment Assignment { get; set; }
    public Question Question { get; set; }
}

```

example
```js
Can you express the Database Design into code Using PlantUML Entity Relationship Diagrams. Remember to use notation on this page: https://plantuml.com/er-diagram

@startuml
!theme vibrant

class User {
    - id : int
    - name : String
    - email : String
    - password_hash : String
    - role : String
}

class Question {
    - id : int 
    - name : String
    - description : String
    - total_points : int
}

class Assignment {
    - id : int
    - title : String
    - description : String
    - publish_time : Datetime
    - close_time : Datetime
    - status : String
    - created_by_teacher_id : int
} 

class AssignmentQuestion {
    ~ assignment_id : int
    ~ question_id : int
}

class StudentAssignment {
    - id : int
    - student_id : int
    - assignment_id : int
    - status : String
    - created_date : Datetime
    - total_points : int
}

class QuestionResponse {
    - id : int
    - student_assignment_id : int
    - question_id : int
    - question_name : String
    - question_description : String
    - points : int 
    - response : String
}

class Feedback {
    - id : int
    - question_response_id : int
    - created_date : Datetime
    - text : String
}

User "1" -- "*" Assignment : "created by"
User "1" -- "*" StudentAssignment : "created by"  
Assignment "1" -- "*" AssignmentQuestion 
AssignmentQuestion "*" -- "1" Question 
StudentAssignment "1" -- "*" QuestionResponse 
QuestionResponse "1" -- "*" Feedback
@enduml
```