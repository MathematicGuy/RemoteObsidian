6.1 Cho lược đồ quan hệ R(U, F), với tập thuộc tính U = {A, B, C, D, E, G}, tập phụ thuộc hàm F = {B → C, AC → D, D → G, AG → E}
![[Pasted image 20240104142234.png]]



6.2 Cho lược đồ quan hệ R(U, F), với tập thuộc tính U = {A, B, C, D, E} và tập phụ thuộc hàm F = {AB → DE, E → AD, D → C}
![[Pasted image 20240107225756.png]]


6.3 Cho lược đồ quan hệ R(U, F), với tập thuộc tính U = {A, B, C, D, E} và tập phụ thuộc hàm F = {A → BC, CD → E, B → D, E → A}
![[Pasted image 20240107225813.png]]


6.4 Giả sử một cơ sở dữ liệu về đầu tư trái phiếu được cài đặt dựa trên lược đồ quan hệ R(U, F). Trong đó
U = {B, D, I, O, Q, S} (B: người môi giới, D: lãi suất của trái phiếu, I: người đầu tư (mua) trái phiếu, O: văn phòng người môi giới, Q: số trái phiếu được một người đầu tư sở hữu, S: loại trái phiếu), và F = {S → D, I → B, IS → Q, B → O}

![[Pasted image 20240107225854.png]]
![[Pasted image 20240107225902.png]]




6.5 Cho lược đồ quan hệ R (U, F), với tập thuộc tính U ={A, B, C, D, E, F} và tập phụ thuộc hàm F = {A→BCD, BC→DE, B→D, D→A}

![[Pasted image 20240107225708.png]]

a) 
1. **B → D** (từ F: B→D)
2. **B → D → A** (từ F: D→A)
3. **B → D → A, B** (thêm B)
4. **B → D → A, B → BCD** (từ F: A→BCD)
5. **B → D → A, B → BCD → ACD** (loại bỏ B)
6. **B → D → A, B → BCD → ACD → BCDE** (từ F: BC→DE)
7. **B → D → A, B → BCD → ACD → BCDE → ACDE** (loại bỏ B)
 
Vậy nên, B+={ A,C,D,E }B+={A,C,D,E}. Điều này có nghĩa là từ thuộc tính B, chúng ta có thể suy ra các thuộc tính A, C, D, và E.
B+ (B bao đóng  = U) -> đây chính là khóa duy nhất
