DDA - MAC dựa trên mã khối
hàng băm sd chứng thực bản tin - SHA235, ..., ... (tất cả loại bảng băm)
Mac - ko cung cap chữ kí số
	- sd hàng băm
	- dựa trên mã khối
	xác minh -> khóa bí mật
	- không cung cấp chữ kí 


Criticality Flag trong Extension -> cho bik có qutrong hay 

Mã hóa khóa đối xứng
Mac
X.509 - lưu trữ và chứng thực 
	Unique Id and ... -> Version 

Bảng Băm
	T/c 1 chiều: khó tạo ra mã hóa từ dữ liệu khối??
	nghịch ảnh: khối dữ liệu chung vs  
Hàng Băm -> dùng trong verify bản 

Mã khóa bí mật và công khai để chứng thực bản tin 
- nhược điểm: tăng độ phức tạp chi phí

Giao thức Needham/Schroeder - 
	tấn công phản lại
	phân phối khóa phiên sd: KDC (trung tâm phân đối khóa)
	sử dụng PK để mã hóa Khóa 

CBC-MAC (sd ASE)
	Bộ đếm với CBC -> sử dụg mã hóa nhận thực

pp cung cấp mã hóa và mật mã cho bản tin -> 4 pp


Chứng thực bản tin - cả ngăn chặn sửa đổi và xác minh 

Bảng băm -> xác định tính toàn vẹn bản 
	xung đột khi cùng giá trị vs 2 khối dữ liệu.

CMAC - Mac dựa trên mật mã khối
Denning - Noun và thời gian

Mã khóa công khai -> người gửi là người tạo bản  
Mã hóa đối xứng -> chỉ người nhận giải đc mã
	được dùng để tạo mã chứng thực bản tin.

HMAC - bảng băm, mã bí 


mã hóa bảng băm và mã hóa đối xứng không được ưu tiên sử dụng -> chi phí đắt, cần nhiều năng 