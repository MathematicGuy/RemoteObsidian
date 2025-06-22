**Steamlit -** require no Front End experiment. Streamlit already handle front-end aspect with predefined layout so you can focus on developing your AI app and testing model.  
	Additionally Streamlit allow:
1. **Automatic Update Script** (like Live Server for HTML)  
2. **Built-in Backend:** Streamlit handle all the BE work like API, adding widget is the same as declaring variable. 
3. **Deploy Instantly** Deploy app for free using Streamlit.. 

![[Pasted image 20250621074421.png]]
![[Pasted image 20250621074603.png]]


![[Pasted image 20250621075611.png]]

```text
	Câu hỏi: 
	Các mối đe dọa tầng cảm biến trong IoT
	
	Trả lời:
    * Khai thác thiết bị vật lý: Người tấn công có thể trích xuất dữ liệu từ bộ nhớ flash, trích xuất firmware, chiếm quyền shell root hoặc thậm chí cài đặt firmware có chứa mã độc.
    * Tấn công side-channel: Người tấn công có thể chiết xuất khóa bí mật dùng để mã hóa/giải mã hoặc trộm cắp dữ liệu nhạy cảm bên trong.
    * Chỉnh sửa firmware: Người tấn công có thể lợi dụng việc thiếu cơ chế xác thực chặt chẽ trong quá trình cập nhật firmware qua OTA.
```

![[Pasted image 20250621085948.png]]
```

		Question:
		Các mối đe dọa tầng cảm biến trong IoT

		Answer:

	{"main_ideas": [
		{"point": "Khai thác thiết bị vật lý", "source": "Nhiều nhà sản xuất thiết bị IoT thường để lộ chân UART/JTAG hoặc bật chế độ console gỡ lỗi ngay trên thiết bị thương mại. Khi có quyền truy cập vật lý, kẻ tấn công có thể trích xuất dữ liệu từ bộ nhớ flash, trích xuất firmware, chiếm quyền shell root hoặc thậm chí cài đặt firmware có chứa mã độc."},
		{"point": "Khai thác thiết bị vật lý", "source": "Nhiều nhà sản xuất thiết bị IoT thường để lộ chân UART/JTAG hoặc bật chế độ console gỡ lỗi ngay trên thiết bị thương mại. Khi có quyền truy cập vật lý, kẻ tấn công có thể trích xuất dữ liệu từ bộ nhớ flash, trích xuất firmware, chiếm quyền shell root hoặc thậm chí cài đặt firmware có chứa mã độc."},
		{"point": "Tấn công side-channel", "source": "Bằng cách theo dõi mức tiêu thụ điện năng hay bức xạ điện từ của thiết bị khi thực hiện các phép toán mã hóa và giải mã, người tấn công có thể chiết xuất khóa bí mật dùng để mã hóa/giải mã hoặc trộm cắp dữ liệu nhạy cảm bên trong."}
	]}
```