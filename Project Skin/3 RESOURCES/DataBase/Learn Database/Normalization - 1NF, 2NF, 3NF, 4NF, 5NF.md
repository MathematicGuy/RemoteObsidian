Why Normalization? to avoid DB vurnerbility causes by data anomaly. 
+ Easier to understand
+ Easier to enhance and extend
+ Protected from:
	 insertion anomalies
	 these shortly...)
	 update anomalies
	 deletion anomalies
	
+ Normalization to **Reduces data redundancy**

+ $ **Normalization rules divide larger tables into smallar tables and links them using relationship.** (Chia bé để đảm bảo dữ liệu trong 1 bảng là dữ liệu độc nhất, ko bị lặp lại) 

## Problem with Un-Normalize Table
![[Pasted image 20250612213441.png]]
	**Redundant Data Update:** update of 1 person lead to updation of multiple row.
	**Inconsistent Data:** If only 1 professor name is update while other row with that professor name don't. 
	**Delete Anomalies:** delete student mean delete all columns of that rows, if course 101 within the deleted row, the course data also get deleted while we only want to delete the student.  

## Terminology
![[Pasted image 20250614223855.png]]
**Primary Key** - The only key used to identify a database record uniquely.  
**Candidate Key** -  
**Super Key** - a group of keys (multiple keys combine create a super key)
**Composite Key** - 
**Alternate Key** - 


## Normalization Form
### 1NF
+ ? All it attributes have an atomic value. This mean doesn't contain multi-valued attributes like Phone Numer (2 values in 1 attribute) ![[Pasted image 20250612214230.png]]
**Convert to correct form**
![[Pasted image 20250612214259.png]]

**First Normal Form (1NF)**  - Have at least 1 PK And No repeating {Key, attributes} group - 2 or more row with the same data.
1) Using row order to convey infomation is not permitted
2) Mixing data types within the same column is not permitted (unclear date like saying  A value is from 2 to 5)
3) Having a table without a primary key is not permitted
4) Repeating groups are not permitted

### 2NF
1) 1NF is satisfied 
2) **Eliminate all partial dependencies** (1 bảng chỉ phụ thuộc vào 1 khóa chính)
e.g. The table above violate 2NF because Student Name depend on Student Code while Project Name also depend on Project ID. Thus 2 attributes depend on 2 keys. 
![[Pasted image 20250612215011.png]]
Solution: divide table to only have 1 key
![[Pasted image 20250612215118.png]]

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


## 3NF
Không cho phép phụ thuộc bắc cầu. 
e.g. `Student City` có thể đc xác định qua `Student Zipcode` -> có tính phụ thuộc. 

Mà dựa vào Student Code mình cũng có thể xác định Student City. Ta thấy có tính chất bắc cầu từ Student Code -> Student Zipcode -> Student city, nói cách khác ta có thể sử dụng Student Code để xác định Student Zipcode và từ Student Zipcode ta lại có thể xác định Student City. 
![[Pasted image 20250612215421.png]]
+ ? Những **thuộc tính không phải khóa chính** (e.g. thuộc tính bình thường như zipcode, sđt) thì phải phụ thuộc hoàn toàn vào khóa chính. Chứ không phải bất kì thuộc tính nào khác. 

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

**[Boyce-Codd Normal Form (BCNF - 3.5NF)](https://youtu.be/NNjUhvvwOrk?si=34Vtp5BJWbqzBaFd)**
> Each attribute in the table must depend on the key, the whole key and nothing but the key.
+ ? **Objective:** Remove dependencies on non-prime attributes.
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

### BCNF Examples
The Ex below is not in BCNF
![[Pasted image 20240117094614.png]]
+ Professor depend on std_id and subj 
+ This is where we have a problem bc: **prime attr depend on a non-prime attr**

**How to make the table satisfy BCNF?** We have to break the table
![[Pasted image 20240117095146.png]]
![[Pasted image 20240117095155.png]]



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

