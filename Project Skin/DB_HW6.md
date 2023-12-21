6.1 Hãy xem xét lược đồ E-R được hiển thị trong hình dưới đây cho một phần cơ sở dữ liệu BANK (ngân hàng). Mỗi ngân hàng có thể có nhiều chi nhánh và mỗi chi nhánh có thể có nhiều tài khoản và khoản vay.
![[Pasted image 20231221080331.png]]
A_C - account Code, L_C - Loan Code
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


**a) Liệt kê các kiểu thực thể mạnh trong lược đồ E-R.** (tt không phụ thuộc vào tt khác)
Strong Entity in E-R Diagram: CUSTOMER, BANK, ACCOUNT, LOAN

**b). Có kiểu thực thể yếu trong lược đồ này không? Nếu có, hãy đặt tên cho kiểu thực thể yếu này, xác định khóa thành phần và xác định liên kết.**
Thực Thể yếu trong lược đồ: 
BANK_BRANCH(Code, Addr, Branch_no)
	PK: Code, Branch_no
Code: foreign key that reference relation in BANK 

**c) Khóa thành phần và liên kết xác định của kiểu thực thể yếu chỉ định những ràng buộc nào trong lược đồ này?**


**d) Liệt kê tên của tất cả các kiểu liên kết và chỉ định ràng buộc (tối thiểu, tối đa) cho mỗi sự tham gia của một kiểu thực thể trong một kiểu liên kết. Hãy giải thích cho sự lựa chọn của bạn.**


**e) Liệt kê ngắn gọn các yêu cầu của người dùng dẫn đến thiết kế lược đồ ER này.**


**f) Giả sử mỗi khách hàng phải có ít nhất một tài khoản nhưng bị hạn chế tối đa hai khoản vay cùng một lúc và một chi nhánh ngân hàng không thể có nhiều hơn 1.000 khoản vay. Điều này hiển thị như thế nào trên các ràng buộc (tối thiểu, tối đa)?**


**6.2 Xét lược đồ E-R trong hình sau. Giả sử một nhân viên có thể làm việc ở tối đa hai phòng ban hoặc có thể không được phân công vào bất kỳ phòng ban nào. Giả sử mỗi phòng ban phải có một và có thể có tối đa ba số điện thoại. 
Hãy chỉ ra các ràng buộc về tỷ số lực lượng (tối thiểu, tối đa) của các liên kết trên lược đồ này. Nêu rõ các giả định bổ sung nào bạn đưa ra (nếu có). Trong những điều kiện nào thì mối quan hệ HAS_PHONE sẽ dư thừa trong ví dụ này?**


**6.3 Hãy xem xét lược đồ E-R trong hình sau, biểu thị một lược đồ đơn giản hóa cho hệ thống đặt chỗ hàng không. Hãy nêu các yêu cầu và ràng buộc đã tạo ra lược đồ này. Cố gắng trình bày các yêu cầu và đặc tả ràng buộc của bạn càng chính xác càng tốt.**


