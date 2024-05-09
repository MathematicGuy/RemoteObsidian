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
        public string Status { get; set; }0


        // Many to 1 Teacher & Student User
        public TeacherAssignment? TeacherAssignments { get; set; }
        public StudentAssignment? StudentAssignments { get; set; }

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


        // 1 to 1 relationship with StudentQuestionResponse
        public StudentQuestionResponse StudentQuestionResponse { get; set; }
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
    
    public class StudentQuestionResponse : IValidatableObject
    {
        [Required]
        public int QuestionId { get; set; }

        [Required]
        public string StudentAssignmentId { get; set; }

        public int Points { get; set; } 

        public string? ResponseText { get; set; }

        [Required]
        public string? Status { get; set; } // verify question state

        // Many to 1
        public Question Questions { get; set; }
        public ApplicationUser Student { get; set; }

        // 1 to many to FeedBack
        public ICollection<FeedBack>? FeedBacks { get; set; }


        // Validate Question Score is not negative
        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            if (Points < 0)
            {
                yield return new ValidationResult("Points cannot be negative.", new[] { nameof(Points) });
            }
        }
    }


    public class FeedBack
    {
        public int Id { get; set; }

        [Required]
        public int QuestionResponseId { get; set; }

        [Required]
        public DateTime CreatedDate { get; set; }

        public string? Context { get; set; }

        // 1 to Many Relationship
        public StudentQuestionResponse? QuestionResponse { get; set; }
    }
    
    public class StudentAssignment
    {
        [Required]
        public string StudentId { get; set; }

        [Required]
        public int AssignmentId { get; set; }

        // prevent when an User is deleted and the Assignment also get deleted
        public ApplicationUser Student { get; set; }
        public Assignment Assignments { get; set; }
    }
    
    public class TeacherAssignment
    {

        [Required]
        public string TeacherId { get; set; }

        [Required]
        public int AssignmentId { get; set; }

        public ApplicationUser Teacher { get; set; }
        public Assignment Assignment { get; set; }
    }
```


