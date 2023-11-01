pivot element -> phần tử trục

note: Có thể chia ngay trong List đó. Ko cần tạo thêm List
**Mục đích**





Lấy phần tử đầu tiên làm trục
	Quét DS nếu phần tử 
		nào lớn hơn thì để Bên phải (giữ nguyên)
		Bé hơn thì Sang bên trái (Lên đầu danh sách)
	" 2 bên đc chia bởi số trục gọi  là 2 sub-list (max sublist và min sublist) "
	Dừng quét khi vị trí 2 con trỏ trùng nhau.
	Thay vị trí của số trục cho số cuối cùng.

Nếu tìm min -> chia đôi lấy list bên trái
Nếu tìm max -> chia đôi lấy list bên phải

Lùi 2 con trọ ngược hướng (1 từ phải sang, 1 từ trái sang)
Phải - Max còn Trái - Min
( Nếu trỏ trái > trỏ Phải -> phạm quy tắc -> Hoán vị vị trí 2 của số đc trỏ vs nhau)

Vấn đề: Khi pivot là số bé nhất -> left ko tăng.


