**2.1 Cho lược đồ cơ sở dữ liệu quan hệ như hình dưới đây. Hãy xác định các khóa
và khóa ngoài của các quan hệ cùng với mô tả thông tin theo giả định của bạn.**
![[Pasted image 20231113232628.png]]

**STUDENT**
Student_number: Primary, Candidate Key
	student number can be unique for each student


**COURSE**
Course_number, {Course_name, Credit_hours, Department}: Candidate Key, Super Key
Course_number:  Primary key
	course number can be unique for each course
Course_number, Credit_hours, Department: Alternate Key

**PREREQUISITE**
Prerequisite_number: Primary key
	prequisite number can be unique 
Course_number: foreign key that reference relation in COURSE 


**SECTION**
Section_identifier: candidate key
	It identify section so it unique  
Course_number: foreign key that reference relation in COURSE

**GRADE_REPORT**
Student_number, Section_identifier: Super Key
Student_number: foreign key that reference relation in STUDENT
Section_identifier: foreign key (refer from SECTION )



**2.2  Xem xét các quan hệ sau đây đối với cơ sở dữ liệu theo dõi việc đăng ký của sinh viên vào các khóa học và các cuốn sách được sử dụng cho mỗi khóa học:**
![[Pasted image 20231114000224.png]]
Chỉ định các khóa ngoài cho lược đồ trên, và mô tả thông tin mà bạn giả định.

The schema of this question has the following 4 foreign key
+ the attribute Course# of relation ENROLL that reference relation in COURSE
+ the attribute Ssn of relation ENROLL that reference relation in STUDENT
+ the attribute Quater of relation BOOK_ADOPTION that reference relation in ENROLL
+ the attribute Book_isbn of relation TEXT that reference relation in BOOK_ADOPTION 

**2.3 Cho các quan hệ sau đây trong cơ sở dữ liệu theo dõi doanh số bán ô tô tại một đại lý ô tô (OPTION đề cập đến một số thiết bị tùy chọn lắp đặt trên ô tô):** 
![[Pasted image 20231114071228.png]]
**Hãy thực hiện các công việc sau:**
- **Xác định các khóa ngoài cho lược đồ trên cùng với mô tả thông tin mà bạn giả
định.**
- **Điền vào các quan hệ một vài bộ dữ liệu mẫu, sau đó đưa ra ví dụ về phép chèn
vào các quan hệ SALE và SALESPERSON vi phạm các ràng buộc toàn vẹn tham
chiếu và một phép chèn khác không vi phạm các ràng buộc.**

**Foreign Key:**
+ Serial_no is a foreign key of OPTION and SALE referencing the CAR relation 
+ Price is a foreign key of OPTION referencing the CAR relation 
+ Salesperson_id is a foreign key of SALESPERSON referencing the SALE relation

```sql
-- Inserting rows into the SALE table
INSERT INTO SALE (Salesperson_id, Serial_no, Date, Sale_price)
VALUES
    (1, 'SN123', '2023-11-13', 1000.00),
    (2, 'SN456', '2023-11-14', 1500.50),
    (3, 'SN789', '2023-11-15', 800.75),
    (1, 'SN101', '2023-11-16', 1200.25);

-- Inserting rows into the SALESPERSON table
INSERT INTO SALESPERSON (Salesperson_id, Name, Phone)
VALUES
    (1, 'John Doe', '123-456-7890'),
    (2, 'Jane Smith', '987-654-3210'),
    (3, 'Bob Johnson', '555-123-4567');
```
Example of a violation of **Referential Integrity Constraint** 
```sql
-- Inserting rows into the SALESPERSON table
INSERT INTO SALESPERSON (Salesperson_id, Name, Phone)
VALUES (4, 'Manny', '573-q23-7990'),
```

Example of non-violation **Referential Integrity Constraint**
```sql
-- Then Inserting rows into the SALE table
INSERT INTO SALE (Salesperson_id, Name, Phone)
VALUES (4, 'SN991', '2024-11-22', 1222.00),
-- Inserting rows into the SALESPERSON table
INSERT INTO SALESPERSON (Salesperson_id, Name, Phone)
VALUES (4, 'Manny', '573-q23-7990'),
```

**2.4 Giả sử rằng mỗi thao tác Cập nhật sau đây được áp dụng trực tiếp vào trạng
thái cơ sở dữ liệu được cho trong hình dưới đây** 
Thảo luận về các ràng buộc toàn vẹn bị vi phạm bởi mỗi thao tác (nếu có), và
các cách khác nhau để thực thi các ràng buộc này

**a. Insert <'Robert', 'F', 'Scott', '943775543', '1972-06-21', '2365 Newcastle
Rd, Bellaire, TX', M, 58000, '888665555', 1> into EMPLOYEE.**
> M is not String data type -> Violate Domain Integrity

**b. Insert <'ProductA', 4, 'Bellaire', 2> into PROJECT.**
> Violate Referential Integrity Constraint because Dnum are foreign key of PROJECT referencing the DEPT_LOCATION relation 
Solve: 
1) Rejecting the insertion
2) Insert <2, 'Turos'> into DEPT_LOCATION 
3) Insert <'ProductA', 4, 'Bellaire', 2> into PROJECT

**c. Insert <'Production', 4, '943775543', '2007-10-01> into DEPARTMENT.**
Duplicate error Dnumber value is primary key = 4
Bug fix: fix Dnumber to a value different from the values that exist in the column

**d. Insert <'677678989', NULL, '40.0'> into WORKS ON.**
Causes an error related to the key constraint Pno to NULL
Bug fix: fix Pno to the value that appears in the PROJECT table Pnumber column

**e. Insert <'453453453', 'John', 'M', '1990-12-12', 'spouse'> into DEPENDENT.**
**Delete the WORKS_ON tuples with Essn = '333445555'.**
> No Constraint Violation

**g. Delete the EMPLOYEE tuple with Ssn = '987654321'.**
> No Constraint Violation

**h. Delete the PROJECT tuple with Pname = 'ProductX'.**
> Causing a key constraint error → Deleting the data set → losing the key value Pnumber → causing an error in the WORKS_ON table
Bug fix: delete all data with Pno = 1 in WORKS_ON table

**i. Modify the Mgr_ssn and Mgr_start_date of the DEPARTMENT tuple with
Dnumber = 5 to '123456789' and '2007-10-01 respectively.**
> No Constraint Violation

**j. Modify the Super_ssn attribute of the EMPLOYEE tuple with Ssn = '999887777' to '943775543'.**
>Causing errors related to key constraints → causing data errors in the DEPENDENT table
Add a data with Mgr_ssn = 943775543 in the DEPARTMENT table

**k. Modify the Hours attribute of the WORKS_ON tuple with Essn = '999887777' and Pno = 10 to '5.0'.**
> Causes a referential integrity error because the value 5.0 does not exist in the Pnumber column of the PROJECT table
Bug fix: Add 1 data with Pnumber = 5.0 in PROJECT table

![[Pasted image 20231114115150.png]]

**3.1, 3.2, 3.3**
![[3.1.jpg]]![[3.1.2.jpg]]
![[3.1.3.jpg]]

![[3.1.4.jpg]]
![[3.1.5.jpg]]

![[3.1.6.jpg]]

![[z4878989684293_02977e1b9c58840ea701b2d433c8f8a6 1.jpg]]

![[z4878989927567_196d38410f988c3c20ffefb6634fbf36 1.jpg]]

![[z4878990141543_0d8b99675beeea37d41b815865b5a796 1.jpg]]


![[z4878988381998_7c8b72a0f4b35245ce6c61d8fd2a30e9 1.jpg]]

![[z4878988110229_aca0de58d57eb463269544c9e953f97c 1.jpg]]

![[z4878988381998_7c8b72a0f4b35245ce6c61d8fd2a30e9 2.jpg]]

![[z4878988871714_c439cfdce9c7dab4e081ad582893aef8 1.jpg]]

![[z4878989368110_42a31dc3a456895795a6b79baa0ac080 1.jpg]]

![[z4878989684293_02977e1b9c58840ea701b2d433c8f8a6 2.jpg]]

![[z4878989927567_196d38410f988c3c20ffefb6634fbf36 2.jpg]]

![[z4878990141543_0d8b99675beeea37d41b815865b5a796 2.jpg]]
**3.3**
![[3.3.jpg]]
![[3.3.2.jpg]]