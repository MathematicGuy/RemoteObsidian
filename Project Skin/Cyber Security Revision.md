DDA - MAC dựa trên mã khối
hàng băm sd chứng thực bản tin - SHA235, ..., ... (tất cả loại bảng băm)
Mac - ko cung cap chữ kí số
	- sd hàng băm
	- dựa trên ã Khối
	xác minh -> khóa bí mật
	- không cung cấp chữ kí 	


Criticality Flag trong Extension -> cho bik có qutrong hay 

Mã hóa khóa đối xứng
Mac
X.509 - lưu trữ và chứng thực 
	Unique Id and ... -> Version 
X.800 (có  loại) - thực hiện chính sách an toàn
+ Authentication exchange (trao đổi xác thực) 
+ Traffic padding (đệm giao thông)
+ Routing control (điều khiển định tuyến)
+ Notarization (công chứng)


Để đạt được tính bảo mật trong việc truyền dữ liệu giữa ng A và B, cần có điều gì? -> thỏa thuận về cơ chế mã hóa. (2 ways handshake for)

Dịch vụ an nh đảm bảo thông tin không bị thay đổi or chỉ đc phép chỉnh sửa bởi ng có thẩm quyền? -> Tính toàn vẹn.
1
An Ninh mạng - phát hiện phòng ngừa, đối 


Bảng Băm
	T/c 1 chiều: khó tạo ra mã hóa từ dữ liệu khối??
	nghịch ảnh: khối dữ liệu giá trị bảng băm (not cùng giá trị bảng băm)  
Hàng Băm -> dùng verify bản tin

Mã khóa bí mật và công khai để chứng thực bản tin 
- nhược điểm: tăng độ phức tạp chi phí

Giao thức Needham/Schroeder - 
	tấn công phản lại
	phân phối khóa phiên sd: KDC (trung tâm phân đối khóa)
	sử dụng PK để mã hóa Khóa 

chứng thực vs toàn phần ?


CBC-MAC (sd ASE)
	Bộ đếm CBC -> sử dụg mã hóa nhận thực

CCM - xáct hực và bảo mậttcao hơn. 

pp cung cấp mã hóa và mật mã cho bản tin -> 4 pp


Chứng thực bản tin - cả ngăn chặn sửa đổi và bảo 

Bảng băm -> xác định tính toàn vẹn bản 
	xung đột khi cùng giá trị vs 2 khối dữ liệu.

CMAC - Mac dựa trên mật mã khối
Denning - Noun và thời gian

Mã khóa công khai -> người gửi là người tạo bản  
Mã hóa đối xứng -> chỉ người nhận giải đc mã
	được dùng để tạo mã chứng thực bản tin.

HMAC (bảng băm, mã bí mật) > MAC (better than MAC)
	giả mạo bằng cách tạo ra 1 bản tin giống và hợp lệ

mã hóa bảng băm và mã hóa đối xứng không được ưu tiên sử dụng -> chi phí đắt, cần nhiều năng 
tạo - bí mật
xác minh - công khai



Lỗ hổng bảo mật khó đánh giá nhất -> lỗ hổng kết nối liên mạng
## Chap 2
Khóa con Ki vòng thứ i: dịch vòng trái, hoán vị, nén khóa K

ECB mode: 

DES (Data Encryption Standard - mã hóa tiêu chuẩn dữ )
+ Key size
+ Bock size
+ Block code and Feitel code
+ Create 16 sub-key from 56-bit primary-key
+ have 16 password round 
+ S-Boxes: tranform 6 bit to 4 bit
+ F function in DES round can both Expand and Compress
+ F function substitute A and B (thay thế A và )
+ 64 bits in length

ECB - encrypt block seperatly (mã khóa các khối 1 cách riêng )

One-time-pad: 
+ Save to only use once

BBS (Blum Blum Shub) use 2 prime number to ensure the safety of the numbers array

COde table of Feistel system
	output code of the last cycle permuted

Tại sao cần có các giả thiết chính xác trong mật mã hiện đại?
	Chứng minh độ an toàn vô điều kiện và so sánh các giả định.

Vigenere
	thuật toán dịch chuyển đa chữ 4
	Use matrix to encrypt planintext
	![[Pasted image 20240510151515.png]]
	Ex: The letter corresponse to the coordinate 
	A - L is L; T - E is X, T - M is F. Therefor the Cipher of the first 3 letters are LXF

How to attack Vigenere if know the key length
	alphabet frequent
	pp vét cạn
	tấn công 

LCG 
	prone to attacker if know the length a certain part
	m,a,c,X0

PRF vs PRNG 
	PRF can create fixed bit length and can add additional infomation
Improve PRNG (Pseudorandom number generator) safety
+ synchronize system
+ combine many PRNG group
+ change seed frequently


SPN - replace-substitution (thay thế) and permutation (hoán vị) (trộn khóa, thay thế hoán vị)

Hiệu ứng lan truyền trong mật mã là gì?
	1 bit change in key can lead to a big differences in  

Bỏ Phiếu điện tử ko sử dụng mã hóa khóa bí mật

Code Block is a password schema symetric in plaintext M {0 ,1}^n and key space K  = {0,1}^r



**AES:** (Advanced Encryption Standard)
128 bit synmetric block cyper
128 bit -> 128 of cyber text
from 128 to 256 bits

[Feistel](https://www.youtube.com/results?search_query=Feistel+)
Feistel Network
Split the block in two
Put it in a function (hash, round, etc..)
last round -> flip the output
![[Pasted image 20240510154121.png]]
to decrypt it -> (Run the algoorithm again with the encrypt as the input) put it in the top -> decrypt it.
two side (L and R)
put a key to each F (2 F -> K1 and K2)
**F function Substitue L and R  (Hàm F thay thế L và R)**
![[Pasted image 20240510154253.png]]
![[Pasted image 20240510154242.png]]
next step
![[Pasted image 20240510154316.png]]
next step
![[Pasted image 20240510154347.png]]




[DES](https://www.youtube.com/results?search_query=DES)
	(Data Encyption ALgorithm) Symemetric block Cipher
	don't use often nowaday. but use AES instead
	input: 64bits (64 bits plain text) -> 64 bits cyber text (kích thước khối)
	main key: 64 bits. subkey: 56 bits  (kích thước )
	Round key: 48 bits (using subkey, 16 x 48 bits round key)
	No. of Round: 16 rounds
	Feistel type
![[Pasted image 20240510152009.png]]
64 bits input to each round, after 16 round. 64 bits get inot 32 bits swap function to Inverse initial permutation
key is 64 bits which is 8 bytes but for each bytes there a parity bit (bit ngang bằng) (64 - 64/8 = 56) -> 56 bits in total. 


[AES](https://www.youtube.com/results?search_query=AES)
Plain text -> XOR -> Subbytes -> Shift Rows -> Mix -> Add Round Key -> Repeat ![[Pasted image 20240510153513.png]]
