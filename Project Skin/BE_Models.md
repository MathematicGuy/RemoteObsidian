
```cs
    public class Assignment
    {
        public int Id { get; set; }

        [Required]
        [MaxLength(100)] // Example max length constraint
        public string? Title { get; set; }

        public string? Description { get; set; }

        [Required]
        public DateTime PublishTime { get; set; }

        public DateTime? CloseTime { get; set; } // CloseTime is optional 

        [Required]
        public string? Status { get; set; }

        [Required]
        public int CreatedByTeacherId { get; set; }

        // Navigation Property (Relationship to User)
        public ApplicationUser? CreatedByTeacher { get; set; }
        // 1 to many to AssignmentQuestion
        public ICollection<AssignmentQuestion>? AssignmentQuestions { get; set;
    }

    public class AssignmentQuestion
    {   
        public int AssignmentId { get; set; }
        public int QuestionId { get; set; }

        // Navigation Properties
        public Assignment? Assignment { get; set; }
        public Question? Question { get; set; }

        public ICollection<Assignment>? AssignmentsCreated { get; set; }
        public ICollection<StudentAssignment>? StudentAssignments { get; set; }
    }
    public class FeedBack
    {
        public int Id { get; set; }

        [Required]
        public int QuestionResponseId { get; set; }

        [Required]
        public DateTime CreatedDate { get; set; }

        public string? Context { get; set; }

        // Navigation Property
        public QuestionResponse? QuestionResponse { get; set; }
    }

  public class Question : IValidatableObject
  {
      public int Id { get; set; }

      [Required]
      public string Name { get; set; }

      public string? Description { get; set; }

      public int TotalPoints { get; set; }

      // 1 to many to AssignmentQuestion
      public ICollection<AssignmentQuestion>? AssignmentQuestions { get; set; }

      public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
      {
          if (TotalPoints < 0)
          {
              yield return new ValidationResult("Total points cannot be negative.", new[] { nameof(TotalPoints) });
          }
      }
  }


    public class QuestionResponse : IValidatableObject
    {
        public int Id { get; set; }

        [Required]
        public int StudentAssignmentId { get; set; }

        [Required]
        public int QuestionId { get; set; }

        public int Points { get; set; }

        public string? ResponseText { get; set; }

        [Required]
        public string? Status { get; set; }

        // Navigation Properties
        public StudentAssignment? StudentAssignment { get; set; }
        public Question? Question { get; set; }

        // 1 to many to FeedBack
        public ICollection<FeedBack>? FeedBacks { get; set; }
        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            if (Points < 0)
            {
                yield return new ValidationResult("Points cannot be negative.", new[] { nameof(Points) });
            }
        }
    }

	    public class StudentAssignment : IValidatableObject
    {
        public int Id { get; set; }

        [Required]
        public int StudentId { get; set; }

        [Required]
        public int AssignmentId { get; set; }

        [Required]
        public string? Status { get; set; }

        [Required]
        public DateTime CreatedDate { get; set; }

        public int TotalPoints { get; set; }

        public ApplicationUser? Student { get; set; }
        public Assignment? Assignment { get; set; }
        public ICollection<QuestionResponse>? QuestionResponses { get; set; }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            // Ensure TotalPoints is non-negative
            if (TotalPoints < 0)
            {
                yield return new ValidationResult("Total points cannot be negative.", new[] { nameof(TotalPoints) });
            }
        }
    }
	
```