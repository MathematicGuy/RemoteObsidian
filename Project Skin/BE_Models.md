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
{
  "email": "admin2@gmail.com",
  "password": "Admin2@123"
}
```
Data
```cs
   public class ApplicationUser : IdentityUser
   {
        // "email": "admin2@gmail.com", 
	     // "password": "Admin2@gmail.com"


	    public string Name { get; set; }
	    public string Email { get; set; }
	    public string Role { get; set; }
	
	    // 1 to 1 Relationship
	    public Student Student { get; set; } 
	    public Teacher Teacher { get; set; }
	}
```
Models/Domains
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
   
    public class Student 
    {
        public int StudentId { get; set; }
        public string UserId { get; set; } // Foreign key to ApplicationUser
        public int averageScore { get; set; }

        // 1 to 1 Relationship
        public ApplicationUser User { get; set; }
        // 1 to Many Relationship
        public ICollection<StudentAssignment>? StudentAssignments { get; set; }
   }

    public class Teacher 
    {
        public int TeacherId { get; set; }
        public string UserId { get; set; } // Foreign key to ApplicationUser
        public string Department { get; set; }

        // 1 to 1 Relationship
        public ApplicationUser User { get; set; }
        // 1 to Many Relationship
        public ICollection<TeacherAssignment>? TeacherAssignments { get; set; }
    }

    public class StudentAssignment
    {
        [Required]
        public int StudentId { get; set; }

        [Required]
        public int AssignmentId { get; set; }

        public int? AssignmentTotalPoints { get; set; }


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

Backend Features for Student User
![[Pasted image 20240512173635.png]]

Use 2 diff account to test data update Concurrentcy. (2 users update the same data at 1 moment) 
admin2@gmail.com 
```json
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6Ijg5ZTQ0ZTY1LWM4MTQtNGU1Mi05ZTFjLWQ0OWVlOTkwMmJmYyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJtYWluIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvZW1haWxhZGRyZXNzIjoiYWRtaW4yQGdtYWlsLmNvbSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFkbWluIiwiZXhwIjoxNzE1NTk3ODQ1LCJpc3MiOiJodHRwczovL2xvY2FsaG9zdDo3MjAyIiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NzIwMiJ9.l6mz077hC2kUg6zQjDx8_7NsNKhZm9wC9WW22FFCNEo
```

admin@gmail.com
```json
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6ImU1NWE1ZmU4LTFjNTQtNDEyOC05MThjLWNlZDllMGNjYjhlYiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJSYXZpbmRyYSIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2VtYWlsYWRkcmVzcyI6ImFkbWluQGdtYWlsLmNvbSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFkbWluIiwiZXhwIjoxNzE1NTk4OTc0LCJpc3MiOiJodHRwczovL2xvY2FsaG9zdDo3MjAyIiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NzIwMiJ9.66Nxnd5W19EfQp2ZpYcMVcjWf59nz0LgdNHN4LbPgc8
```


```cs
[HttpGet]
[Route("get-students-list")]
public async Task<IActionResult> GetAsync()
{
	 var students = await context.Student.ToListAsync();
	 return Ok(students);
}

// Lấy người dùng theo ID
[HttpGet]
[Route("get-user-by-id/{UserId}")]
public async Task<IActionResult> GetUserByIdAsync(int UserId)
{
	 var user = await context.Student.FindAsync(UserId);
	 if (user == null)
	 {
		  return NotFound(); // Trả về lỗi 404 nếu không tìm thấy người dùng
	 }
	 return Ok(user);
}

// Thêm người dùng mới
[HttpPost]
[Route("add-user")]
public async Task<IActionResult> PostAsync(Student user)
{
	 if (!ModelState.IsValid)
	 {
		  return BadRequest(ModelState); // Trả về lỗi 400 nếu dữ liệu không hợp lệ
	 }

	 context.Student.Add(user);
	 await context.SaveChangesAsync();
	 return Created($"/get-user-by-id/{user.StudentId}", user);
}

// Cập nhật thông tin người dùng
[HttpPut]
[Route("update-user/{UserId}")]
public async Task<IActionResult> PutAsync(int UserId, Student userToUpdate)
{
	 if (UserId != userToUpdate.StudentId || !context.Student.Any(u => u.StudentId == UserId))
	 {
		  return BadRequest("Invalid user ID"); // Trả về lỗi 400 nếu ID không hợp lệ hoặc không tìm thấy người dùng
	 }

	 context.Student.Update(userToUpdate);
	 await context.SaveChangesAsync();
	 return NoContent();
}

// Xóa người dùng
[HttpDelete]
[Route("delete-user/{UserId}")]
public async Task<IActionResult> DeleteAsync(int UserId)
{
	 var userToDelete = await context.Student.FindAsync(UserId);
	 if (userToDelete == null)
	 {
		  return NotFound(); // Trả về lỗi 404 nếu không tìm thấy người dùng
	 }

	 context.Student.Remove(userToDelete);
	 await context.SaveChangesAsync();
	 return NoContent();
}
```
