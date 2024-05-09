**Project 1.** **Quản lý quan hệ khách hàng (6.6)**  
**Project 2. Quản lý kho (6.1)**  
https://youtu.be/1UbssR3pjL8?si=JjGWDzUv4QgUoRVA
https://youtu.be/KoGJsjnKmj0?si=kO-K_uTh25UcPRnO
**Project 3. Quản lý nhân sự**  
**Project 4. Quản lý công việc.**  
**Project 5. Quản lý thu chi tài chính (6.4)**  
**Project 6.** **Xây dựng hệ thống thi code hỗ trợ chấm điểm tự động bằng chatGPT có kết hợp với người đánh giá.**

14 - CDDL
16 - AI
21 - Web BE
22 - PM
24 - ATTT

```cs
    public class Assignment
    {
        public int Id { get; set; }

        [Required]
        [MaxLength(100)] // Example max length constraint
        public string Title { get; set; }

        public string? Description { get; set; }

        [Required]
        public DateTime PublishTime { get; set; }

        public DateTime? CloseTime { get; set; } // CloseTime is optional 

        [Required]
        public string Status { get; set; }

        // Many to 1 Teacher & Student User
        public ICollection<TeacherAssignment>? TeacherAssignments { get; set; } // Change to
        public ICollection<StudentAssignment>? StudentAssignments { get; set; } // Change to ICollection

        // 1 to many to QuestionResponse
        public ICollection<AssignmentQuestion>? AssignmentQuestions { get; set; }
    }
    
    public class Question : IValidatableObject
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        public string? Description { get; set; }

        public int? TotalPoints { get; set; }

        public string AnswerFileURL { get; set; }

        public string Status { get; set; }


        // 1 to 1 relationship with StudentQuestionResponse
        public FeedBack? QuestionFeedback { get; set; }
        // 1 to many relationship with AssignmentQuestion
        public ICollection<AssignmentQuestion> AssignmentQuestion { get; set; }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            if (TotalPoints < 0)
            {
                yield return new ValidationResult("Total points cannot be negative.", new[] { nameof(TotalPoints) });
            }
        }
    }
	    
    public class AssignmentQuestion
    {
        [Required]
        public int AssignmentId { get; set; }
        [Required]
        public int QuestionId { get; set; }

        // Many to Many relationship between Assignment and Question
        public Assignment Assignment { get; set; }
        public Question Question { get; set; }
    }
    
    public class StudentAssignment
    {
        [Required]
        public string StudentId { get; set; }

        [Required]
        public int AssignmentId { get; set; }

        // Many to Many relation. "Student" M-1 + 1-M "Assignment" = M-M
        public Student Student { get; set; }
        public Assignment Assignments { get; set; }    
    }
    
    public class TeacherAssignment
    {

        [Required]
        public string TeacherId { get; set; }

        [Required]
        public int AssignmentId { get; set; }

        // TeacherAssignment` is a join table between `ApplicationUser` and `Assignment`
        // Many to 1
        public Teacher Teacher { get; set; }
        public Assignment Assignment { get; set; }
    }

    
    public class FeedBack
    {
        public int Id { get; set; }

        [Required]
        public DateTime CreatedDate { get; set; }

        public string? Context { get; set; }

        // 1 to Many Relationship
        public Question? QuestionResponse { get; set; }
    }
    
```

Why StudentAssignment and TeacherAssignment Table?
1. To Manage.

**What They Enable**
These joining tables, in conjunction with your models, enable the following functionalities:

- **Enrollment/Management:** You can:
    
    - Easily enroll a student in an assignment.
    - Add or remove an assignment from a teacher's responsibility.
    
- **Data Retrieval:** You can fetch:
    
    - All the assignments a particular student is enrolled in.
    - All the students enrolled in a specific assignment.
    - All assignments managed by a specific teacher.
    
- **Flexibility:** You can add extra data to these joining tables if needed. For example, you could add a grade, a completion date, or other information specific to a particular Student-Assignment association.

- The `StudentAssignment` and `TeacherAssignment` tables are essential for modeling the many-to-many relationships between students/teachers and assignments.
- They provide a clean and normalized way to store and manage these associations.