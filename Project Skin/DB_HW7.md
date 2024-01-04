6.1 Cho lược đồ quan hệ R(U, F), với tập thuộc tính U = {A, B, C, D, E, G}, tập phụ thuộc hàm F = {B → C, AC → D, D → G, AG → E}
![[Pasted image 20240104142234.png]]




![[Pasted image 20240104144016.png]]


1. **B → D** (từ F: B→D)
2. **B → D → A** (từ F: D→A)
3. **B → D → A, B** (thêm B)
4. **B → D → A, B → BCD** (từ F: A→BCD)
5. **B → D → A, B → BCD → ACD** (loại bỏ B)
6. **B → D → A, B → BCD → ACD → BCDE** (từ F: BC→DE)
7. **B → D → A, B → BCD → ACD → BCDE → ACDE** (loại bỏ B)
 
Vậy nên, B+={ A,C,D,E }B+={A,C,D,E}. Điều này có nghĩa là từ thuộc tính B, chúng ta có thể suy ra các thuộc tính A, C, D, và E.
B+ (B bao đóng  = U) -> đây chính là khóa duy nhất
