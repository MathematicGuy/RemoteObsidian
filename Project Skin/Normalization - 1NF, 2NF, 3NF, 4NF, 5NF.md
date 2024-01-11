Why Normalization? to avoid DB vurnerbility.  
+ Easier to understand
+ Easier to enhance and extend
+ Protected from:
	 insertion anomalies
	 these shortly...)
	 update anomalies
	 deletion anomalies


**First Normal Form (1NF)**  - Have at least 1 PK And No repeating {Key, attributes} group - 2 or more row with the same data.
1) Using row order to convey infomation is not permitted
2) Mixing data types within the same column is not permitted (unclear date like saying  A value is from 2 to 5)
3) Having a table without a primary key is not permitted
4) Repeating groups are not permitted

**Second normal form (2NF)** 
+ ? Objective: Loại bỏ sự phụ thuộc một phần.
+ ? **Example:** Consider a table with columns (Student_ID, Course, Instructor). If a student can take multiple courses, and the instructor depends on the whole primary key (Student_ID, Course), it's not in 2NF. To address this, you'd split the table into two: one for student information and another for course details.

> Each **none-key attribute** in the table must be **dependent on the entire primary key** (As long as it depend on a PK it 2NF?)
> Ex: if {Player_ID, Item_Type} -> Item_Quantity, Player_Rating - then it 2NF
![[Pasted image 20231129164040.png]]

> {Player_ID, Item_Type} -> Item_Quantity -> 2NF
> {Player_ID, Item_Type} -> Player_Rating -> 2NF
>  **Each none-key attribute** in the table  **depend on the entire primary key**
![[Pasted image 20240110082954.png]]

**Third normal form (3NF)** (depend on 1 key ?)
+ ! **3NF Forbid:** a on_key attribute on another non-key attribute. Because Player_Rating depends on Player_Skill
+ ? **Objective:** Remove transitive dependencies.
+ ? **Example:** Building on the previous example, if Instructor depends on Student_ID (a non-prime attribute), it indicates a transitive dependency. To achieve 3NF, you'd further normalize the table by creating a separate table for instructors and their details, linked by the instructor's ID. 
các thuộc tính không khóa phụ thuộc hết và 1 khóa
> Problem **Player_Rating depend on Player_Skill_Level** (non-key attribute depend on a non-key attribute)
![[Pasted image 20231129160127.png]]
Sol: Seperate each one. Use a Foreign Key to conenct Player_Skill_Levels> Player_rating and Player_Skill_Levels are 3rd normal form because the attributes depend on the key: "Player_ID", "Player_Skill_Level" (and nothing but the key)
![[Pasted image 20240110083421.png]]
**Dạng Chuẩn 3 NF:**
+ 3NF đảm bảo rằng một bảng không có sự dư thừa và bất thường bằng cách **loại bỏ các phụ thuộc bắc cầu.
+ Một mối quan hệ ở dạng 3NF nếu nó ở dạng chuẩn thứ hai (2NF) và không có thuộc tính không chính phụ thuộc bắc cầu vào khóa chính 1

**Boyce-Codd Normal Form (BCNF - 3.5NF)**
> Each attribute in the table must depend on the key, the whole key and nothing but the key.
+ ? - **Objective:** Remove dependencies on non-prime attributes.
+ ? **Example:** Let's say you have a table with columns (Employee_ID, Project_ID, Task). If the combination of Employee_ID and Project_ID determines the Task and there are no other dependencies, it's in BCNF. However, if there's another non-prime attribute dependent on a subset of the primary key, further normalization may be needed.
+ Multivalued dependencies in a table must be multivalued dependencies on the key.
+ review def: 2NF
![[Pasted image 20240110084552.png]]

+ review def: 3NF
![[Pasted image 20240110084517.png]]
+ BCNF
![[Pasted image 20240110085105.png]]
+ Overcome a loop hole in 3NF: 
![[Pasted image 20240110085643.png]]
note that: the key mean "every candidate key"
![[Pasted image 20240110094449.png]]


### [Review: 2NF vs 3NF vs BCNF](https://chat.openai.com/share/442b423f-e413-4ef1-bde5-fb77773c45cc)


**Fourth Normal Form (4NF)**  
![[Pasted image 20231129160902.png]]

**Fifth Form** (5th form)
> A table is in 5th Normal Form only if it is in 4NF and it cannot be decomposed into any number of smaller tables without loss of data
![[Pasted image 20231129161614.png]]


Phụ thuộc hàm dư thừa
	Từ phụ thuộc hàm này -> phụ thuộc hàm khác

F(c) -> F tối thiểu 
	Course depends only on the Student ID and not on any other attribute, it exhibits minimal dependency**.**
**Course**

| Student ID | Name  | Course           |
| ---------- | ----- | ---------------- |
| 001        | John  | Data Science     |
| 002        | Jane  | Computer Science |
| 003        | Alice | Data Science     |

