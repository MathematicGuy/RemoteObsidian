**Structure Overview**
![[Pasted image 20240801130027.png]]

## Create Project
Create a Spring Boot Project from [Spring Initializr](https://start.spring.io/)  with these dependencie
![[Pasted image 20240801132239.png]]

# Create Class and Run

**StudentClass**
```java
package com.example.fun2.student;

import java.time.LocalDate;


public class Student {
	// Object Attributes
	private Long id;
    private String name;
    private String email;

    private LocalDate dob; // Data of Birth
    private Integer age;
```
2) Add Object Component. So you can call it as a Function
```java
// Student Component. Simplelize Object into a function
    public Student(Long id, String name, String email, LocalDate dob, Integer age) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.dob = dob;
        this.age = age;
    }
```
3) Add Getter and Setter Class. Use to get and set Object's data 
```java


	// Getter and Setter. Use to get and set Object's data
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public LocalDate getDob() {
        return dob;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
```
4) View your Object in json 
```java
	// toString() Function. This use to view the Object
    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", dob=" + dob +
                ", age=" + age +
                '}';
    }
}
```


Now let test your API using the code in your **Application.java** inside src/main/java 
> This should return a json string of the Student Object
```java
package com.example.fun2;  
  
import com.example.fun2.student.Student;  
import org.springframework.boot.SpringApplication;  
import org.springframework.boot.autoconfigure.SpringBootApplication;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
import java.time.LocalDate;  
import java.time.Month;  
import java.util.List;  
  
@SpringBootApplication  
@RestController  
public class Fun2Application {  
  
    public static void main(String[] args) {  
        SpringApplication.run(Fun2Application.class, args);  
    }  
    @GetMapping ("/hello")  
    public List<Student> hello() {  
        return List.of(  
            new Student(  
                    1L,  
                    "Mariam",  
                    "thanh@gmail.com",  
                    LocalDate.of(200, Month.JANUARY, 5),  
                    21  
            )  
        );    }}
```


# API Layer
**StudentController**
The Controller will be where we control the API. it often called the **API Layer**  
```java
@RestController  
@RequestMapping(path = "api/v1/student")  
public class StudentController {  
	// This is a API Action
    @GetMapping  
    public List<Student> getStudents() {  
        return List.of(  
            new Student(  
                    1L,  
                    "Mariam",  
                    "thanh@gmail.com",  
                    LocalDate.of(2004, Month.JANUARY, 5),  
                    21  
            )  
        );   
	}
}	
```
> Thus we would need another file called StudentRepository or StudentService working a function library holding all the API Action like getStudent(). Then we just need to call it in StudentController. (Cleaner right)


# Business Layer
(your code is not going to work in this step)

**StudentService**
>The Service call Business Layer because it take care of all the functions.

1) Moving the function to StudentService 
```java
public class StudentService {  
    public List<Student> getStudents() {  
        return List.of(  
            new Student(  
                    1L,  
                    "Mariam",  
                    "thanh@gmail.com",  
                    LocalDate.of(2004, Month.JANUARY, 5),  
                    21  
            )  
        );    
	}
}
```
2) Call it on the StudentController
	Remember to call the StudentService Class before using StudentService getStudent() actions. 
```java
@RestController
@RequestMapping(path = "api/v1/student")
public class StudentController {

    private final StudentService studentService;

    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    @GetMapping
    public List<Student> getStudents() {
        return studentService.getStudents();
    }
}
```

# Dependency Injection
> Inject StudentSevice into StudentController

Autowire (connect) the Controller with the Service by default 
```java
@Autowired // Inject StudentService into StudentController
public StudentController(StudentService studentService) {  
    this.studentService = studentService;  
}
```

Then we annotate the StudentService class with @Service to tell the StudentController StudentService Class is a Service Layer.
```java
@Service // Service Component. This is a Annotation  
public class StudentService { 
```

Now you have achieve the API Layer with the Service Layer. In Which the API Layer give command to the Service Layer and the Service Layer return data to the API Layers.  
![[Pasted image 20240801140414.png]]


```txt
# host    all             all             127.0.0.1/32            scram-sha-256
# host    all             all             ::1/128                 scram-sha-256

```
# Properties File
> Let connect to the Database

