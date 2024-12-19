## Text Classification
+ Tokenize: Chia các từ ra từng unique character
+ Processing: xóa bỏ những ký tự ko cần thiết/quan trọng
+ Embedding: Chuyển từng unique char thành số (số vector)
	Tạo từ điển riêng cho từng câu khác nhau. "key : value" cho "chữ : số"	![[Pasted image 20241218201726.png]]
Nhưng nếu vs 1 từ nhiều nghĩa thì thể hiện như thế nào?
different word are enormous, how to represent 'text' effectively. -> acronym. 

Normalize độ dài của chữ. dùng padding là số 0 để chèn vào ô trống. Vd: thấy có 4 từ, nhưng đi có 2 từ nên phải thêm 2 số 0 vào để cân bằng list. 

Đặt 1 ký tự làm ký tự 0.
chuỗi số:từ đc chứa trong 1 dict
![[Pasted image 20241218204738.png]] 


![[Pasted image 20241218220039.png]]