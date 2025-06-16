## Giới thiệu về Entity Relationship Diagram

**Derived Attribute**: thuộc tính có thể được tính toán từ các thuộc tính khác.  
![[Pasted image 20250612202242.png]]

**Composite Attributes** (thuộc tính chứa nhiều sub-attribute) - một thuộc tính có kiểu giá trị là Object.  
**Multivalue attribute** (thuộc tính chứa/nhận nhiều giá trị) - một list trong lập trình

**Relationships**  
![[Pasted image 20250612202454.png]]

### Participation Constraints

**Partial participation:** 1 phần (có hay không, không có cũng được)  
**Total participation:** toàn phần (bắt buộc phải có)  
-> Các sinh viên có thể không có giảng viên hướng dẫn.  
-> Nhưng 1 giảng viên khi hướng dẫn chắc chắn sẽ hướng dẫn ít nhất 1 sinh viên.  
![[Pasted image 20250612203019.png]]

### Crow's Foot Notation

![[Pasted image 20250612203325.png| 300]]  
**crow foot** nghĩa là nhiều  
**single line** thay cho crow's foot nghĩa là 1  
**circle before** the foot nghĩa là optional (giống partial participation)  
**line before** the foot nghĩa là mandatory (total participation)

- ? 1 - một course phải có duy nhất 1 lecturer, và 1 lecturer có thể có 0 hoặc nhiều course.
    
- ? 2 - một student có thể đăng ký từ 0 đến nhiều course, và một course có thể có từ 0 đến nhiều student đã đăng ký.  
    ![[Pasted image 20250612211125.png]]
    

Line thay cho foot nghĩa là one. One + Mandatory nghĩa là One and only One.  
![[Pasted image 20250612210904.png|350]]

Line thay cho foot nghĩa là One. One + Optional nghĩa là Zero or One (Một hoặc Không có vì optional nghĩa là có hoặc không, hoặc có (1) hoặc không (1))  
![[Pasted image 20250612211034.png| 350]]

- ? ví dụ: Student có duy nhất 1 seat. 1 seat có duy nhất 1 student  
![[Pasted image 20250612211102.png]]    

## Giới thiệu về Database Normalization

**Database Normalization giúp** giảm dư thừa dữ liệu và lỗi bất thường dữ liệu (ví dụ: thiếu dữ liệu, dữ liệu không đồng bộ giữa 2 bảng)

**Data Normalization** là hành động chia nhỏ các bảng lớn thành các bảng nhỏ hơn và liên kết chúng để tạo mối quan hệ giữa các bảng.

### Vấn đề với bảng chưa được chuẩn hóa

![[Pasted image 20250615144133.png]]  
**Redundant Data Update:** cập nhật của 1 người dẫn đến việc cập nhật nhiều dòng.  
**Inconsistent Data:** nếu chỉ cập nhật tên 1 professor trong khi các dòng khác với cùng professor đó thì không.  
**Delete Anomalies:** xóa student đồng nghĩa với việc xóa tất cả các cột của dòng đó, nếu course 101 nằm trong dòng bị xóa thì dữ liệu course cũng bị xóa theo dù ta chỉ muốn xóa student.

### Các loại lỗi dữ liệu (trong bảng chưa được chuẩn hóa)

![[Pasted image 20250614165917.png]]

#### Insertion Anomaly

- ? Xảy ra khi thuộc tính bị thiếu hoặc không đồng bộ trong quá trình chèn dữ liệu. Việc chèn dữ liệu trong bảng chưa chuẩn hóa có thể tạo ra các vấn đề sau:
    

**Redundant Data:** Chèn một student dẫn đến việc lặp lại giá trị 'CourseName' và 'Professor'. Bạn phải chèn lại các giá trị này dù chúng đã tồn tại trước đó.  
![[Pasted image 20250614170410.png]]  
**Partial Data Insertion:** Chèn một Course mới mà chưa có student đăng ký sẽ tạo ra các giá trị bị thiếu cho Student ID và Name (thường là giá trị NULL).  
![[Pasted image 20250614170701.png| 450]]

**Null Value Issues:** Tương tự như Partial Data Insertion, chèn student chưa đăng ký course nào sẽ tạo ra giá trị null cho các cột Courses và Professor.  
![[Pasted image 20250614171111.png]]

#### Updation anomalies

- ? Điều này xảy ra khi có nhiều dữ liệu bị lặp lại trong cùng một bảng dẫn đến việc xử lý không hiệu quả.  
    ![[Pasted image 20250614172047.png]]  
    **Redundant Data Update:** cập nhật 1 dòng đồng nghĩa với việc phải cập nhật nhiều dòng khác. Ví dụ: khi một Professor đổi tên thành Dr.Brown, tất cả các dòng có Dr.Smith cũng cần được cập nhật để đảm bảo tính nhất quán dữ liệu.  
    ![[Pasted image 20250614172305.png]]  
    **Inconsistant Data:** khi bạn cập nhật 1 dòng nhưng quên cập nhật các dòng khác. Ví dụ: khi cập nhật tên 1 Professor nhưng không đồng bộ phần còn lại.  
    ![[Pasted image 20250614172316.png]]
    

3. **Delete Anomalies:** Xóa một dữ liệu dẫn đến việc xóa ngoài ý muốn các dữ liệu khác.  
    ![[Pasted image 20250614173016.png]]  
    **Unwanted Data Loss:** Xóa dữ liệu Student cũng xóa dữ liệu Course & Professor.  
    Điều này có thể tạo ra _Orphan Records_ nếu Course Name phụ thuộc vào CourseID.  
    ![[Pasted image 20250614173027.png]]

## Thuật ngữ

![[Pasted image 20250615144249.png]]  
Sơ đồ Venn cho thấy **không phải tất cả Primary Key đều là Candidate Key** _vì chỉ một số Candidate Key được chọn làm Primary Key_, **không phải tất cả Super Key đều là Candidate Key** vì _Super Key bao gồm tổ hợp của Key với các thuộc tính không phải là prime_.

Chúng ta biết rằng tất cả Super, Candidate đều xây dựng dựa trên Primary Key. Vậy hãy bắt đầu từ cơ bản, bằng cách hiểu Primary Key là gì, và nó được tạo nên từ gì.

Trong một bảng có các cột và hàng, mỗi cột đại diện cho một attribute và mỗi hàng là một ví dụ cụ thể với các attribute đó. Primary Key là một attribute hoặc tổ hợp attribute được sử dụng để xác định duy nhất các attribute khác.

- ? Ví dụ trong bảng này, StudentCode và ProjectID có thể được kết hợp làm Primary Key vì các thuộc tính này đảm bảo mỗi hàng là duy nhất. (chỉ dùng Student thì dòng 1 và dòng 2 sẽ trùng nhau)  
    ![[Pasted image 20250615173325.png| 450]]  
    Từ ví dụ trên, ta biết rằng **có những attribute có thể và không thể trở thành Primary Key**.
    
- ? Ví dụ, thuộc tính ProjectLeader không phải là prime-attribute vì tên là lặp lại, nếu có 2 người tên Andy, ta sẽ có 2 dòng `{101, (P03, Andy)}` và `{102, (P03, Andy)}`, nếu 2 thuộc tính `(ProjectID, Project_Leader)` không thể xác định duy nhất các attribute khác (ví dụ `StudentCode`) thì nó không phải là Primary Key.
    

Vậy nên **Primary Key** là **một cột hoặc tổ hợp cột dùng để xác định duy nhất mỗi hàng trong bảng**. (chỉ có 1 trong mỗi bảng)  
Hơn nữa, Primary Key là **tối thiểu**, nên nếu **không cần thiết kết hợp** `ProjectID` và `Project_leader` làm Primary Key thì chỉ cần chọn 1 attribute (`ProjectID` hoặc `Project_Leader`) làm Primary Key.

- ? Lưu ý: Primary Key không giới hạn phải là tổ hợp giữa prime và non-prime attribute, miễn là nó cần thiết để xác định duy nhất các attribute khác trong bảng.  
    ví dụ: StudentID hoặc Email (phải Unique và không NULL) hoặc {StudentID, Email} nếu cần cả 2 để xác định duy nhất các attribute khác.
    
- **Prime Attribute (có thể là Primary Key):** thuộc tính là duy nhất, có thể dùng để xác định duy nhất các attribute khác. Ví dụ: StudentID hoặc Email.  
    Prime attribute cũng là **một phần của Candidate Key** (key có thể được chọn làm primary key)
    
- **Non-Prime Attribute (không thể là Primary Key):** thuộc tính không duy nhất và lặp lại như Name hoặc SchoolName.  
    Attribute này cũng **không là một phần của Candidate Key** (không thể được chọn làm primary key vì tính lặp lại). Ví dụ: Name, Age, SchoolName
    

**Candidate Key** - là **tập hợp các key có thể được chọn làm Primary Key**. Do đó, prime attribute là một phần của Candidate Key.  
Ví dụ: StudentID và Email là Candidate Key nhưng chỉ một được chọn làm Primary Key.

**Alternate Key** - là **Candidate Key không được chọn làm Primary Key**.  
Ví dụ: Nếu StudentID được chọn làm Primary Key, thì Email trở thành Alternate Key.

**Super Key** - **bất kỳ tổ hợp nào của Candidate Key** và bất kỳ tập con nào của Candidate Key (tức prime attribute) miễn là **xác định duy nhất bản ghi trong bảng**. Bao gồm cả tổ hợp giữa Candidate Key và Non-Prime attribute.  
Lưu ý: thuộc tính trong {} biểu diễn một Super Key.  
Ví dụ: {StudentID}, {Email}, {StudentID, Email}, {Email, StudentName}, {StudentID, Email, StudentName}
- $ Tóm lại, Super Key bao gồm tất cả tổ hợp khóa có thể tổ hợp được. 


**Composite Key** - là **Primary Key gồm > 1 thuộc tính**. Cụ thể là **tổ hợp tối thiểu của các khóa để xác định bản ghi một cách duy nhất**.  
Điều này có nghĩa nếu 2 khóa là đủ để xác định mỗi hàng trong bảng, thì chỉ 2 khóa đó được chọn làm Composite Key.  
Trong khi Super Key có thể dư thừa, ví dụ {StudentID, Email, StudentName}.  
![[Pasted image 20250615144314.png]]

Lưu ý: Prime và Non-Prime không giống với Candidate và Alternate Key. Nó mô tả xem một thuộc tính **có thể trở thành key** hay không, trong khi Candidate và Alternate Key mô tả xem một thuộc tính (có thể là key) **đã được chọn làm key hay chưa**.

Lưu ý: $X \to Y$ biểu thị sự phụ thuộc hàm (functional dependency - FD), nghĩa là nếu 2 hàng có cùng giá trị X, thì chúng phải có cùng giá trị Y.  
Ví dụ: nếu $StudentID \to Name$, thì $StudentID$ xác định duy nhất Name.

**Transitive Dependency** (Tính chất bắc cầu thông qua non-prime attribute): non-prime attribute phụ thuộc vào một non-prime attribute khác thay vì phụ thuộc vào Primary Key.  
Giả sử $Z$ và $Y$ là non-prime. $X$ là primary key.  
Vì $X \to Y$ và $Z \to Y$ nên ta có thể xác định $X \to Y \to Z$ (xác định X thông qua Y và Y thông qua Z) $\to$ dẫn đến dư thừa dữ liệu.

**Tóm tắt:** X $\to$ Y là trivial nếu $Y \in X$, còn $X \to Y$ là non-trivial ngược lại.  
**Trivial Dependency:** Phụ thuộc **cung cấp thông tin mới**. Không rõ ràng  
Ví dụ:  
+ ${StudentID, Course} \to Instructor$  
+ $Course \to Department$

**Non-Trivial Dependency:** Phụ thuộc **không cung cấp thông tin mới**. Hiển nhiên  
Ví dụ:  
+ ${StudentID, Course} \to StudentID$  
+ $StudentID \to StudentID$

## Normalization Form

Giải thích 1NF → 3NF, tại BCNF giải thích sự khác biệt giữa BCNF và 3NF → 4NF đến 5NF.

**1NF: thêm sự phụ thuộc giữa các Attributes** điều này nghĩa là mỗi bản ghi (row) trong bảng được xác định duy nhất. Không có hàng nào trùng lặp.

**2NF: loại bỏ partial dependency** tức là không còn phụ thuộc một phần trong bảng, nghĩa là mọi attribute (bao gồm cả alternate key, prime-attribute) đều phụ thuộc hoàn toàn vào 1 primary key.

- ! Hạn chế phụ thuộc của attributes vào nhiều primary key nhưng không hạn chế phụ thuộc giữa Attribute và Attribute.
    

> Ví dụ: nếu {Player_ID, Item_Type} → Item_Quantity, Player_Rating - thì là 2NF  
> ![[Pasted image 20250615153211.png]]

**3NF loại bỏ transitive dependency** nghĩa là **không có sự phụ thuộc bắc cầu giữa các attributes không phải là primary key**. Nghĩa là mọi attribute trong bảng chỉ phụ thuộc hoàn toàn vào primary key và không phụ thuộc vào bất kỳ prime-attribute hay non-prime attribute nào khác.  
Ví dụ:

- _StudentCity phụ thuộc vào StudentZipcode_ vì một City có thể xác định thông qua ZipCode (lưu ý rằng StudentZipcode là một phần của Candidate key)
    
- _StudentZipcode phụ thuộc vào StudentCode_. Vậy ta có thể dùng StudentCode để xác định StudentCity thông qua StudentZipCode → transitive dependency.
    
- ! Transitive Dependency có thể **gây ra sự dư thừa khi cập nhật** vì nếu có 2 dòng cùng StudentCity, bạn sẽ phải cập nhật StudentCity 2 lần, đúng không?  
    ![[Pasted image 20250615154948.png]]
    
- $ Thay vào đó, nếu ta tách StudentZipcode và StudentCity ra riêng và dùng StudentZipcode để tham chiếu tới bảng Student từ bảng Student_Location thì ta chỉ cần cập nhật StudentCity một lần, vì mỗi bản ghi trong Student_Location được xác định duy nhất, không lặp lại như ở ví dụ đầu tiên.  
    ![[Pasted image 20250615160425.png]]
    

**3NF vs BCNF Sự khác biệt chính:**

- Trong **3NF**, một **non-prime attribute** có thể phụ thuộc vào prime attribute trong candidate key hoặc superkey, miễn là không có tính chất bắc cầu. Điều này có nghĩa là attributes không cần phụ thuộc vào toàn bộ superkey mà chỉ cần phụ thuộc vào candidate key.
    
- Trong **BCNF, là 3NF nhưng không attribute nào (prime hay non-prime) được phép phụ thuộc vào bất kỳ tập hợp attribute nào không phải superkey**. Điều này loại bỏ cả functional dependency vào prime attribute không phải superkey. 
- **Giải thích rõ hơn:** 
	**Mọi attribute chỉ được phép phụ thuộc vào toàn bộ super key**. 
	VD: *Phụ thuộc và cả 2 khóa Student_Code và ProjectID chứ không phụ thuộc đơn lẻ vào 1 prime attribute* như ProjectID hoặc StudentCode.
    

![[Pasted image 20250615160717.png]]  

![[Pasted image 20250615160733.png]]

**4NF: loại bỏ multi-value dependency** (trong bảng có ít nhất 3 cột)  
Bảng thỏa mãn **4NF cũng thỏa mãn BCNF và không có bất kỳ Multi-valued Dependency nào.**  
Lưu ý: A và B là các attribute, nên có thể chứa 1 hoặc nhiều giá trị.

**Multi-valued Dependency** ($\to \to$) nghĩa là:  
![[Pasted image 20250615183556.png]]

1. Với phụ thuộc $A \to B$, nếu với một giá trị A duy nhất `ví dụ: Course=CS101`, tồn tại nhiều giá trị B `ví dụ: Teacher={Smith, Jones}`. (tức là A xác định một tập giá trị của B)
    
2. Một bảng phải có ít nhất 3 cột để xảy ra Multi-valued Dependency `ví dụ: R(Course, Teacher, Book)` (_để đảm bảo điều kiện thứ 3_)
    
3. Với quan hệ `R(Course, Teacher, Book)`, nếu tồn tại multi-valued dependency giữa Course và Teacher, thì Book phải độc lập.
    

**Bảng có Multi-valued Dependency (tức là vi phạm 4NF) có thể được tách thành** $R_1(Course, Teacher)$ và $R_2(Course, Book)$, với yêu cầu có ít nhất 3 thuộc tính trong quan hệ ban đầu.  
![[Pasted image 20250615190538.png]]  
**Trong đó:**

- B `Teacher` không phụ thuộc vào C `Book`
    

- Primary key $R_1(A, B)$ nhưng `Course` là attribute liên kết.
    
- Primary key $R_2(A, C)$ nhưng `Course` là attribute liên kết. Course chỉ đơn giản là thuộc tính chia sẻ.
    

- $A \to \to B$ và $A \to \to C$ ($\to \to$ nghĩa là multi-valued dependency)
    
- Lưu ý: A có thể là primary key trong bảng riêng (ví dụ bảng `Course`) và cả $R1$ và $R_2$ có thể tham chiếu đến nó qua foreign key.
    

---

**TODO:**

- Ví dụ về 5NF
    
- So sánh 4NF và 5NF
    
- Case Study
