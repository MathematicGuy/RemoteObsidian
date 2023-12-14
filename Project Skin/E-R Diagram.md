
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