
**DB_HW5 SUMMARY**

*instructor & course*
![[Pasted image 20231206100611.png]]
*prereq, department & teaches*
![[Pasted image 20231206100621.png]]
*section, student*
![[Pasted image 20231206100634.png]]
*takes*
![[Pasted image 20231206100645.png]]


---

**5.1 Với CSDL về trường đại học (university) đã cho ở chương 4, hãy viết các truy vấn
sau trong SQL:**

**a) Liệt kê danh sách tất cả giảng viên gồm ID, tên và số lượng lớp học phần họ đã dạy.
Với những giảng viên chưa dạy bất kỳ lớp học phần nào thì hiển thị số lớp học phần của
họ là 0.**

```sql
select instructor.ID , instructor.name, COUNT(course_id) as teaches_courses
from instructor LEFT OUTER JOIN teaches ON instructor.ID = teaches.ID
GROUP BY instructor.ID, instructor.name
```


**b) Viết truy vấn tương tự câu a), nhưng sử dụng truy vấn con vô hướng, không có liên kết
ngoài.**


```sql
select instructor.ID, count(course_id) AS teaches from teaches, instructor 
where instructor.ID = teaches.ID
GROUP BY instructor.ID  
```

**c) Hiển thị danh sách tất cả các lớp học phần vào mùa xuân 2010, cùng với tên của giảng
viên giảng dạy lớp đó. Nếu một lớp học phần có nhiều giảng viên thì lớp đó sẽ xuất hiện
trong kết quả với số lần tương ứng với số lượng giảng viên. Nếu lớp không có giảng viên
nào, nó vẫn xuất hiện trong kết quả với tên người hướng dẫn được đặt thành “—”.
(Gợi ý: SQL cung cấp một câu lệnh n-ary gọi là COALESCE, được định nghĩa như sau:
COALESCE (A1, A2, ..., An) trả về Ai khác


```sql
SELECT instructor.name, COALESCE(tid.course_id, '_') 
FROM instructor 
LEFT OUTER JOIN (
    SELECT teaches.ID, section.course_id 
    FROM teaches
    LEFT OUTER JOIN section ON teaches.course_id = section.course_id 
    WHERE section.year = 2010 AND section.semester = 'Spring'
) AS tid ON instructor.ID = tid.ID;
```


**d) Hiển thị danh sách tất cả các khoa, với tổng số giảng viên trong mỗi khoa mà không sử
dụng truy vấn con vô hướng. Với các khoa không có giảng viên thì hiển thị số giảng viên
là 0.**

```sql
SELECT COALESCE(instructor.dept_name, '0') AS dept_name, COUNT(instructor.name) AS instr_name
FROM department
LEFT OUTER JOIN instructor ON department.dept_name = instructor.dept_name
GROUP BY instructor.dept_name;
```

+ ! 5.2. Giả sử cho một quan hệ grade_points(grade, point), cung cấp sự chuyển đổi từ điểm chữ (grade) trong quan hệ takes thành điểm số (point); ví dụ: điểm “A” có thể được chỉ định tương ứng với 4 điểm, điểm “A−” tương ứng với 3,7 điểm, điểm “B+” tương ứng với 3,3 điểm, điểm “B” tương ứng với 3 điểm, v.v. Điểm số mà một sinh viên đạt được khi tham gia một lớp học phần (section) được xác định bằng số tín chỉ của khóa học nhân với số điểm mà sinh viên đạt được.

+ ! Với quan hệ grade_points và lược đồ CSDL university, hãy viết từng truy vấn sau bằng SQL. Để đơn giản, có thể giả sử rằng không có bộ nào trong takes mà có điểm grade nhận giá trị null

Tạo quan hệ grade_points(grade, point)
```sql
CREATE TABLE grade_points (
    grade VARCHAR(5) PRIMARY KEY,
    point DECIMAL(3, 2) NOT NULL
);

-- Inserting grade points data
INSERT INTO grade_points (grade, point) VALUES
    ('A', 4.0),
    ('A-', 3.7),
    ('B+', 3.3),
    ('B', 3.0),
    ('B-', 2.7),
    ('C+', 2.3),
    ('C', 2.0),
    ('C-', 1.7),
    ('D+', 1.3),
    ('D', 1.0),
    ('D-', 0.7),
    ('F', 0.0);

-- Verify the data
SELECT * FROM grade_points;

```

**a) Tìm tổng điểm mà sinh viên có ID là 12345 đạt được trong tất cả các lớp học phần mà
sinh viên đó đã học.**

+ (total_point = 48.)
```sql
-- total_point = (course) point * (course) credits
SELECT 
    --step0 get letter grade
	takes.ID,
    --step4 get total_point: result of all course's point   
	SUM(point * credits) AS total_point 
FROM
    takes
JOIN
    --step2 Conversion: convert letter grade to grade point
	grade_points ON takes.grade = grade_points.grade 
JOIN
    --step3 get Course Credits: connect to course to inherit credits field
	course ON course.course_id = takes.course_id 
WHERE
    --step1: get ID = 12345 from takes
	takes.ID = 12345
    --step5 Group by for aggregation: Group all course's points of students ID = 12345  
GROUP BY takes.ID
```

**b) Tìm điểm trung bình (GPA) của sinh viên trên, tức là lấy tổng điểm chia cho tổng số
tín chỉ của các môn học liên quan.**
```sql
SELECT 
    --step0 get letter grade
	takes.ID,
    --step4 get total_point: total_point / total course cred   
	(SUM(point*credits)/SUM(credits)) as avg_score
FROM
    takes
JOIN
    --step2 Conversion: convert letter grade to grade point
	grade_points ON takes.grade = grade_points.grade 
JOIN
    --step3 get Course Credits: connect to course to inherit credits field
	course ON course.course_id = takes.course_id 
JOIN 
    student ON student.ID = takes.ID
WHERE
    --step1: get ID = 12345 from takes
	takes.ID = 12345
    --step5 Group by for aggregation: Group all course's points of students ID = 12345  
GROUP BY takes.ID
```
**c) Tìm ID và điểm trung bình của mỗi sinh viên.**
```sql
SELECT 
    --step0 get letter grade
	takes.ID,
    --step4 get total_point: total_point / total course cred   
	(SUM(point*credits)/SUM(credits)) as avg_score
FROM
    takes
JOIN
    --step2 Conversion: convert letter grade to grade point
	grade_points ON takes.grade = grade_points.grade 
JOIN
    --step3 get Course Credits: connect to course to inherit credits field
	course ON course.course_id = takes.course_id 
JOIN 
    student ON student.ID = takes.ID
GROUP BY takes.ID
```
**d) Tăng lương 10% cho mỗi giảng viên trong khoa Comp.Sci.**
```sql
UPDATE
    instructor
SET
    salary = salary * 1.1
WHERE
    dept_name = 'Comp. Sci.';
```
**e) Xóa tất cả các môn học chưa bao giờ được đưa ra để xếp lớp (nghĩa là không xuất
hiện trong quan hệ section).**
```sql
--delete all distinct course_id from course that not exist in section
DELETE FROM
	course  
WHERE 
	course_id NOT IN (select distinct course_id from section); 
```
**f) Chèn mọi sinh viên có thuộc tính tot_cred lớn hơn 100 làm giảng viên hướng dẫn
trong cùng khoa với mức lương là 10.000 USD**
```sql
INSERT INTO instructor(ID, name, dept_name, salary)
select
    ID,
    name,
    dept_name,
    10000
from
    student
where
    student.tot_cred > 100
```

**5.3 Viết câu lệnh định nghĩa khung nhìn student_grades(ID, GPA) cho điểm trung bình
grade-point của mỗi sinh viên, dựa vào truy vấn trong bài tập 5.2 (nhắc lại rằng, ta sử
dụng quan hệ grade_points(grade, points) để lấy điểm số kết hợp với điểm chữ). Đảm
bảo rằng định nghĩa khung nhìn của bạn xử lý chính xác trường hợp thuộc tính grade của
quan hệ takes nhận giá trị null.**
(Gợi ý: SQL cung cấp câu lệnh CASE khi có nhiều điều kiện)
```sql
case
	when condition1 then result1
	when condition2 then result2
	...
	else default_result
end
```
Example:
```sql
update instructor
set salary = case
	when salary <= 100000 then salary * 1.05
	else salary * 1.03
end
```

```sql
CREATE VIEW student_grades AS
SELECT 
    takes.ID,
    --COUNT(field) = 0 mean there NULL value in field
    CASE
        WHEN COUNT(takes.grade) = 0 THEN NULL
        ELSE SUM(grade_points.point*course.credits)/SUM(course.credits)
    END AS GPA
FROM takes
LEFT OUTER JOIN
    grade_points ON takes.grade = grade_points.grade 
LEFT OUTER JOIN 
    course ON takes.course_id = course.course_id
GROUP BY 
    takes.ID;
```



