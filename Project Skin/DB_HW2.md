**2.1 Cho lược đồ cơ sở dữ liệu quan hệ như hình dưới đây. Hãy xác định các khóa
và khóa ngoài của các quan hệ cùng với mô tả thông tin theo giả định của bạn.**
![[Pasted image 20231113232628.png]]
**STUDENT**
Student_number: candidate key 
	student number can be unique for each student

**COURSE**
Course_number:  candidate key
	course number can be unique for each course

**PREREQUISITE**
Prerequisite_number: candidate key
	prequisite number can be unique 
Course_number: foreign key

**SECTION**
Section_identifier: candidate key
	It identify section so it unique  
Course_number: foreign key (refer from COURSE)

**GRADE_REPORT**
Student_number: foreign key (refer from STUDENT)
Section_identifier: foreign key (refer from SECTION )

**2.2  Xem xét các quan hệ sau đây đối với cơ sở dữ liệu theo dõi việc đăng ký của sinh viên vào các khóa học và các cuốn sách được sử dụng cho mỗi khóa học:**
![[Pasted image 20231114000224.png]]
Chỉ định các khóa ngoài cho lược đồ trên, và mô tả thông tin mà bạn giả định.

The schema of this question has the following 4 foreign key
+ Course# from relation ENROLL refer relation in COURSE
+ Ssn from relation ENROLL refer relation in STUDENT
+ Quater from relation BOOK_ADOPTION refer relation in ENROLL
+ Book_isbn from relation TEXT refer relation in BOOK_ADOPTION 





2.3
3.3