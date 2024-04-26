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
