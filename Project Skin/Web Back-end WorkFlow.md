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
}

class Question {
    - name : String
    - description : String
    - totalPoints : int 
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
class Submission {
    - studentId : int
    - assignmentId: int
    - responses: String  
    - score: int
    - status: String 
}

class Feedback {
    - feedbackId: int
    - submissionId: int
    - timestamp: Datetime
}

class FeedbackContent {
    - feedbackId: int
    - text: String
}

class SubmissionController {
    + submitQuestionAnswer() // Student
    + submitAssignment() // Student
    + viewSubmissions()  // Teacher
    + scoreAssignment()  // Teacher
    + provideFeedback()  // Teacher
}

Submission "1" -- "*" Feedback
Feedback "*" -- "1" FeedbackContent
@enduml
```

Activity Model of Function