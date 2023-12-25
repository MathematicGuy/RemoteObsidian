6.1 Hãy xem xét lược đồ E-R được hiển thị trong hình dưới đây cho một phần cơ sở dữ liệu BANK (ngân hàng). Mỗi ngân hàng có thể có nhiều chi nhánh và mỗi chi nhánh có thể có nhiều tài khoản và khoản vay.
![[Pasted image 20231221080331.png]]
A_C - Normal Account, L_C - Loan Account
M - N or N - M: Many Many relationship
Weak Entity have dash line underneth (Weak Entity PK = Partial Key + Strong Entity PK )

**CUSTOMER**(Ssn, Name, Phone, Addr)
	**PK: Ssn**
**BANK**(Code, Name, Addr)
	**PK: Code**
**BANK_BRANCH**(Code, Addr, Branch_no) 
	**PK: Code, Branch_no**

**ACCOUNT**(Code, Branch_no, Acct_no, Balance, Type)
	**PK**: Code, Branch_no, Acct_no
**LOAN**(Code, Branch_no, Loan_no, Amount, Type)
	**PK**:  Code, Branch_no, Loan_no 
**A_C**(Ssn, Acct_no)
	PK: Ssn, Acct_no
**L_C**(Ssn, Loan_no)
	PK: Ssn, Loan_no


**a) Liệt kê các kiểu thực thể mạnh trong lược đồ E-R.** 
note: (tt mạnh không phụ thuộc vào tt khác)

Strong Entity in E-R Diagram: CUSTOMER, BANK, ACCOUNT, LOAN

**b). Có kiểu thực thể yếu trong lược đồ này không? Nếu có, hãy đặt tên cho kiểu thực thể yếu này, xác định khóa thành phần và xác định liên kết.**

Thực Thể yếu trong lược đồ: 
BANK_BRANCH(Code, Addr, Branch_no)
	Partial Key: Branch_no
Indetifying relationship: Branches

**c) Khóa thành phần và liên kết xác định của kiểu thực thể yếu chỉ định những ràng buộc nào trong lược đồ này?**

Partial Key: Branch_no.
Constraint Relation between Bank and Bank_branch throught BRANCHES is One-to-Many 
+ BRANCHES: BANK 1-to-Many BANK_BRANCH 
reasons: 
1) The Weak Entity must have total participation in the identifying relationship set, Branches.
2) the identifying reationshop between Bank & Bank_Branches must be **one to many** (example above).

**d) Liệt kê tên của tất cả các kiểu liên kết và chỉ định ràng buộc (tối thiểu, tối đa) cho mỗi sự tham gia của một kiểu thực thể trong một kiểu liên kết. Hãy giải thích cho sự lựa chọn của bạn.**

note: M - N or N - M as Many Many relationship

1. **BANK - BANK_BRANCH:**
	Bank (1..n)-<>-(1..1) BANK_BRANCH
	
	 + Explain: 1 bank can have many branches, bank_branch is a weak entity with on-to-many relationship with bank, therefor 1 bankbranch can only belong to 1 bank.
1. **BANK_BRANCH - ACCOUNT:**
	BANK_BRANCH (0..n)-<>-(1..1) ACCOUNT
	
	+ Explain: BANK_BRANCH to ACCOUNT is a one-to-many relationship. So 1 BANK_BRANCH can have 0 to many accounts, and 1 account belong to 1 BANK_BRANCH 
1. **BANK_BRANCH - LOANS:**
	BANK_BRANCH (0..n)-<>-(1..1) LOANS
	
	+ Explain: BANK_BRANCH to LOANS is a one-to-many relationship. So 1 BANK_BRANCH can have 0 to many loans, and 1 account belong to 1 BANK_BRANCH.
1. **CUSTOMER - ACCOUNT:**
	CUSTOMER (0..n)-<>-(1..n) ACCOUNT 
	
	+ Explain: CUSTOMER to ACCOUNT is a one-to-many relationship. So 1 CUSTOMER can have 0 to many accounts, and 1 account belong to 1 CUSTOMER 
1. **CUSTOMER - LOANS:**
	CUSTOMER (0..n)-<>-(1..n) LOANS
	
	+ Explain:  CUSTOMER to LOANS is a one-to-many relationship. So 1 CUSTOMER can have 0 to many loans, and 1 account belong to 1 CUSTOMER 
**e) Liệt kê ngắn gọn các yêu cầu của người dùng dẫn đến thiết kế lược đồ ER này.**

Customer Request:
+ Choose Type of Account (Normal Account or Loans Account)

A_C (Normal Account)
+ Withdraw money from a BRANK_BRANCH
L_C (Loan Account)
+ Take a Loans from a Bank from a BRANK_BRANCH

+ Withdraw Money or Take Loans from a BANK_BRANCH from many differents address 

**f) Giả sử mỗi khách hàng phải có ít nhất một tài khoản nhưng bị hạn chế tối đa hai khoản vay cùng một lúc và một chi nhánh ngân hàng không thể có nhiều hơn 1.000 khoản vay. Điều này hiển thị như thế nào trên các ràng buộc (tối thiểu, tối đa)?**

"Suppose **each customer** must have **at least one account** but is **limited to a maximum of two loan accounts at a time**, and a **bank branch cannot have more than 1,000 loan accounts**" this express as
note: only modify what the contents given.  

+ CUSTOMER (1..N)-< A_C >-(1..N) ACCOUNT
	"1 Customer can have 1 to many account and reverse"
 + ACCOUNT (1..2)-< L_C >-(1..n) LOANS 
	 1 account can take loans 2 times -< L_C >- 1 Loans 
+ LOAN (1..1)-< LOANS >-(0..1000) BANK_BRANCH
	can only Loan "0 to 1000 maximum Loans" at a time from an Bank Branch
 
**6.2 Xét lược đồ E-R trong hình sau. Giả sử một nhân viên có thể làm việc ở tối đa hai phòng ban hoặc có thể không được phân công vào bất kỳ phòng ban nào. Giả sử mỗi phòng ban phải có một và có thể có tối đa ba số điện thoại.**

**Hãy chỉ ra các ràng buộc về tỷ số lực lượng (tối thiểu, tối đa) của các liên kết trên lược đồ này. Nêu rõ các giả định bổ sung nào bạn đưa ra (nếu có). Trong những điều kiện nào thì mối quan hệ HAS_PHONE sẽ dư thừa trong ví dụ này?**
![[Pasted image 20231221111309.png]]

Assuming: 
1) 1 EMPLOYEE can WORKS_IN 0..2 DEPARTMENT
2) 1 DEPARTMENT can have 1..20 EMPLOYEEs

3) 1 EMPLOYEE can HAS 0..2 PHONE, 1 PHONE can be use by at least 1..5 persons
5) 1 DEPARTMENT can CONTAINS 1..10 PHONE, and 1 PHONE only belong 1 only 1 DEPARTMENT

**Relationship**
+ EMPLOYEE (0..2)-< WORKS_IN >-(1..20) DEPARTMENT
+ EMPLOYEE (1..2)-< HAS_PHONE >-(1..5) PHONE
+ DEPARTMENT (1..2)-< CONTAINS >-(1..1) PHONE


Case that HAS_PHONE will be redundant 
EMPLOYEE (0..2)-< WORKS_IN >-(1..20) DEPARTMENT
	assume that there're 2 employees work in the department 
EMPLOYEE (1..2)-< HAS_PHONE >-(1..5) PHONE
	1 employee can has 2 phone maximum. Making 4 phone being uses 
DEPARTMENT (5..10)-< CONTAINS >-(1..1) PHONE
	DEPARTMENT have 5 to 10 phone while there 4 phones can be uses maximum making 1 phone redundant.

**6.3 Hãy xem xét lược đồ E-R trong hình sau, biểu thị một lược đồ đơn giản hóa cho hệ thống đặt chỗ hàng không. Hãy nêu các yêu cầu và ràng buộc đã tạo ra lược đồ này. Cố gắng trình bày các yêu cầu và đặc tả ràng buộc của bạn càng chính xác càng tốt.**

![[Pasted image 20231221113341.png]]

**AIRPORT**(Airport_code, City, State, Name)
	PK: Airport_code
**CAN_LAND**(Airport_code, Type_name)
	PK: Airport_code, Type_name

**AIRPLANE_TYPE**(Type_name, Max_seats, Company)
	PK: Type_name
**AIRPLANE**(Airplane_id, Type, Total_no_of_seats)
	PK: Airplane_id, Type
	FK: Type reference to Type_name in AIRPLANE_TYPE

**FLIGHT_LEG**(Ariport_code, Leg_no, Number)
	PK: Ariport_code, Leg_no, Number

**DEPARTURE_AIRPORT**(Scheduled_dep_time, Airport_code, Leg_no, Number)
	PK: Airport_code, Leg_no, Number
**ARRIVES_AIRPORT**(Scheduled_arr_time, Airport_code, Leg_no, Number)
	PK: Airport_code, Leg_no, Number

**LEG_INSTANCE**(Airport_code, Leg_no, Number, Date, Airplane_id)
	PK: Airport_code, Leg_no, Number, Date, Airplane_id 

**DEPARTS**(Airport_code, Leg_no, Dept_time)
	PK: Airport_code, Dept_time
**ARRIVES**(Airport_code, Leg_no, Arr_time)
	PK: Airport_code, Arr_time
**RESERVATION**(Customer_name, Cphone, Airport_code, Leg_no, Number, Date, Airplane_id)
	PK: Airport_code, Leg_no, Number, Date, Airplane_id 
**SEAT**(Seat_no, Airport_code, Leg_no, Number, Date, Airplane_id )
	PK: Seat_no, Airport_code, Leg_no, Number, Date, Airplane_id) 

**FLIGHT**(Number, Airline, Weekdays)
	PK: Number
**FARE**(Number, Restriction, Amount, Code)
	PK: Number, Code

**Requirements and Constraints created in the ER diagram**

**Many-to-1** Relationship
+ FLIGHT_LEG N-< DEPARTURE_AIRPORT >-1 AIRPORT
+ FLIGHT_LEG N-< ARRIVAL_AIRPORT >-1 AIRPORT
	Weak Entity, depend on AIRPORT and FLIGHT primary key
	+ Airport_code, Number 

+ AIRPLANE N-< TYPE >-1 AIRPLANE_TYPE

+ FLIGHT_LEG N-< LEGS >-1 FLIGHT

+ LEG_INSTANCE N-< INSTANCE_OF >-1 FLIGHT_LEG

+ LEG_INSTANCE N-< ASSIGNED >-1 AIRPLANE

+ LEG_INSTANCE N-< DEPARTS >-1 AIRPORT

+ LEG_INSTANCE N-< ARRIVES >-1 AIRPORT

 + SEAT N-< RESERVATION >-1 LEG_INSTANCE
	Weak Entity, depend on LEG_INSTANCE primary_key: 
	+ Airport_code, Leg_no, Number, Date, Airplane_id

+ FARE N-< FARES >-1 FLIGHT
	Weak Entity, depend on FLIGHT primary_key:
	+ Number

**Many-to-Many** Relationship
+ AIRPORT m-< CAN_LAND  >-n AIRPLANE_TYPE
+ AIRPLANE m-< CAN_LAND  >-n AIRPLANE_TYPE


## Movie DB

Một hoặc Nhiều: Total participation
Có hoặc Không: Partial participation

Movie(company_id, emp_id, title, yr, length, name, plot), 

Firm(studio, genre)
	studio (the company)
Quotes(actor, movie_name, quote)
	quote - 0-to-Many
Actor(id, name, birth, role)
	birth(mm/dd/yyyy)
	Appear in 1 or many movie
Director(id, name, birth, direct_movie) kế thừa atttibute của 
	Can also be a Actor
	Appear in 1 or many movie
FirmStudio(studio, address) 

![[Pasted image 20231225123729.png]]
+ **Mỗi bộ phim có một hoặc nhiều đạo diễn và một hoặc nhiều diễn viên xuất hiện trong đó.**
	employee: Mỗi diễn viên đều có một vai trong phim. Đạo diễn có thể là diễn viên trong bộ phim của họ. 
-> employee vs film có mqh one-to-many qua Work_In
	Mỗi câu trích dẫn **có thể không có hoặc có nhiều** câu trích dẫn và câu trích dẫn **được nói bởi 1 diễn viên** cụ thể trong film. 
-> Mỗi nhân viên có thể có 1 câu trích dẫn hoặc không.  Và mỗi câu trích dẫn phải đi vs 1 emp_id
Quote (1..1)-< Actor_Quote >-(0..n) employee.
Quote(emp_id, quote_id, content)
	Do Quote là thực thể yếu nên quote_id và content có thể NULL.
![[Pasted image 20231225125439.png]]

Một công ty sản xuất sản xuất một hoặc nhiều bộ phim.
![[Pasted image 20231225113619.png]]

Mỗi Hãng được phân theo 1 hoặc nhiều thể loại (Genre không phải weak entity vì thuộc tính của weak entity có thể null -> tạo ra vấn đề hãng phân ko có thể loại )
-> total participation
![[Pasted image 20231225131824.png]]

