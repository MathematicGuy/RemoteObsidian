Why Normalization? to avoid DB vurnerbility.  

**First Normal Form (1NF)**  
1) Using row order to convey infomation is not permitted
2) Mixing data types within the same column is not permitted
3) Having a table without a primary key is not permitted
4) Repeating groups are not permitted

**Second normal form (2NF)** 
> Each **none-key attribute** in the table must be **dependent on the entire primary key**
> (meaning if the primary key change, non-key attributes change)
![[Pasted image 20231129164040.png]]

**Third normal form (3NF)** (depend on 1 key ?)
các thuộc tính không khóa phụ thuộc hết và 1 khóa.
> Problem **Player_Rating depend on Player_Skill_Level** (non-key attribute depend on a non-key attribute)
![[Pasted image 20231129160127.png]]
Sol: Seperate each one. Use a Foreign Key to conenct Player_Skill_Levels
> Player_rating and Player_Skill_Levels are 3rd normal form because the attributes depend on the key: "Player_ID", "Player_Skill_Level" (and nothing but the key)
![[Pasted image 20231129160249.png]]
**Dạng Chuẩn 3 NF:**
+ 3NF đảm bảo rằng một bảng không có sự dư thừa và bất thường bằng cách **loại bỏ các phụ thuộc bắc cầu.
+ Một mối quan hệ ở dạng 3NF nếu nó ở dạng chuẩn thứ hai (2NF) và không có thuộc tính không chính phụ thuộc bắc cầu vào khóa chính 1


**Boyce-Codd Normal Form (BCNF - 3.5NF)**
> Each attribute in the table must depend on the key, the whole key and nothing but the key.
+ Multivalued dependencies in a table must be multivalued dependencies on the key.



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

