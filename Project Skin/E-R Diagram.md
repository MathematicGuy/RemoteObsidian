
**Symbols used in the E-R notation**
![[Pasted image 20231214142859.png]]



**Alternative E-R notations**
![[Pasted image 20231214142919.png]]



**Symbols used in the UML class diagram notationL** 
![[Pasted image 20231214142927.png]]

![[Pasted image 20231214145528.png]]

+ lấy dữ liệu từ trái sang phải.
+ Thực thể không có tên sẽ thành relation mới.
+ thực thể yếu (dấu hiệu là có discrimination) lấy mọi key từ các thực thể khác
	như là section lấy key của course, classroom, time_slot
+ 1 Thực thể hết yếu khi nó có Khóa Chính (có thể phân biệt độc nhất)
+ Thực thể phải có 2 cột trở lên để trở thành 1 quan hệ.

**Relationship**
student(ID, name, tot_cred, dept_name)
instructor(Id, name, salary, dept_name)
advisor(istr_ID, std_ID)

department(dept_name, building, budget)

section(course_id, sec_id, semester, year, time_slot_id, building, room_number)
course(course_id, title, credits, dept_name)
prereq(course_id, prereq_id)

takes(ID, sec_id, semester, year, grade)
teaches(ID, sec_id, semester, year, course_id)
	thuộc tính của teaches dựa trên key của section và instructor 

course(course_id, title, credits)
classroom(building, room_number, capacity)


**Cardinality Notation:**
	
- **One-to-One (1-1):** Indicates that each entity on one side is associated with exactly one entity on the other side.
    - Example: A person can have only one passport, and a passport can belong to only one person.
```plaintext
PERSON 1-1 PASSPORT
```
	
- **One-to-Many (1-N):** Indicates that each entity on one side can be associated with multiple entities on the other side.
    - Example: A department can have multiple employees, but each employee is associated with one department.
```plaintext
DEPARTMENT 1-N EMPLOYEE
```
- **Many-to-Many (N-M):** Indicates that each entity on both sides can be associated with multiple entities on the other side.
    - Example: A student can enroll in multiple courses, and a course can have multiple students.
```plaintext
STUDENT N-M COURSE
```

- **Participation Constraints:**
    
    - **Total Participation (Total):** Indicates that every entity in an entity set must participate in at least one relationship in the relationship set.
        - Example: Every student must be enrolled in at least one course.
```plaintext
STUDENT (Total Participation) N----1 ENROLLS_IN 1----N COURSE
```
	
+ **Partial Participation (Partial):** Indicates that not every entity in an entity set must participate in a relationship in the relationship set.
    - Example: A student may or may not be assigned to a project.
```plaintext
STUDENT (Partial Participation) N----0..1 ASSIGNED_TO 0..1----N PROJECT
```

- **Key Constraints:**
    
    - **Primary Key (PK):** Indicates the attribute(s) that uniquely identify each entity in an entity set.
        - Example: In the entity set "Person," the primary key might be "SSN."
```plaintext
PERSON
PK: SSN
```


- **Foreign Key (FK):** Indicates an attribute in an entity set that refers to the primary key of another entity set, establishing a relationship.
	
    - Example: In the entity set "Order," the foreign key might be "CustomerID" referring to the primary key "CustomerID" in the "Customer" entity set.
```plaintext
ORDER
FK: CustomerID
```