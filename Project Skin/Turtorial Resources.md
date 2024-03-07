## [[Why Web APIs are Essential]] 
![[Pasted image 20240307150331.png]]


- **Tách biệt mối quan tâm:** API Web tách biệt giao diện người dùng của bạn (Ứng dụng web mà người dùng nhìn thấy) khỏi phần phụ trợ của bạn (cơ sở dữ liệu và logic). Điều này mang lại lợi ích:
    
     - **Phát triển độc lập:** Nhóm frontend và backend có thể làm việc song song.
     - **Khả năng mở rộng:** Mỗi phần có thể được điều chỉnh tỷ lệ độc lập tùy theo nhu cầu.
     - **Khả năng sử dụng lại:** API của bạn có thể phân phối dữ liệu đến các ứng dụng khác, không chỉ ứng dụng web của riêng bạn.
	 
- **Giao tiếp có cấu trúc:** API xác định "hợp đồng". Frontend và backend thống nhất về định dạng của yêu cầu và dữ liệu, đảm bảo tương tác suôn sẻ.
    
- **Bảo mật:** Ứng dụng web của bạn không truy cập trực tiếp vào cơ sở dữ liệu. API cho phép bạn kiểm soát dữ liệu nào được hiển thị và cách truy cập dữ liệu đó.


**API: Cầu dữ liệu của bạn**

1. **Ứng dụng web:** Ứng dụng web là những gì người dùng tương tác. Nó có các biểu mẫu để thu thập dữ liệu đầu vào.
    
2. **Web API:** Đây là "người trung gian":
    
     - **Nhận yêu cầu:** Ứng dụng web gửi dữ liệu tới API ở định dạng có cấu trúc (thường là JSON).
     - **Giao tiếp với cơ sở dữ liệu:** API biết cách tương tác với cơ sở dữ liệu của bạn (ví dụ: truy vấn SQL). Nó có thể thêm dữ liệu mới, truy xuất dữ liệu hiện có hoặc cập nhật bản ghi.
     - **Gửi phản hồi:** Sau khi vận hành cơ sở dữ liệu, API sẽ gửi phản hồi trở lại ứng dụng web (ví dụ: xác nhận thành công hoặc dữ liệu đã được truy xuất).

**Ví dụ:**

1. **Người dùng nhập dữ liệu:** Người dùng điền vào biểu mẫu trên ứng dụng web của bạn để đăng ký tài khoản.
2. **API cuộc gọi ứng dụng web:** Ứng dụng web của bạn gửi dữ liệu biểu mẫu (tên người dùng, email, v.v.) dưới dạng đối tượng JSON đến điểm cuối API của bạn.
3. **API lưu trữ dữ liệu:** API lấy dữ liệu này, tạo truy vấn SQL và chèn thông tin người dùng mới vào cơ sở dữ liệu của bạn.
4. **API gửi thành công:** API gửi phản hồi trở lại ứng dụng web xác nhận việc tạo tài khoản.
5. **Thông báo hiển thị ứng dụng web:** Ứng dụng web hiển thị "Cảm ơn bạn đã đăng ký!" thông báo tới người dùng.

**Không có API Web**

Về mặt kỹ thuật, bạn có thể xây dựng một ứng dụng web mà không cần API, nhưng điều đó tạo ra các vấn đề:

- **Kết nối chặt chẽ:** Ứng dụng web của bạn sẽ phải tương tác trực tiếp với logic cơ sở dữ liệu. Cập nhật một trong hai sẽ trở nên phức tạp.
- **Rủi ro bảo mật:** Việc tiết lộ chi tiết cơ sở dữ liệu trực tiếp cho phía máy khách (ứng dụng web) là một lỗ hổng bảo mật.
- **Khả năng sử dụng lại có giới hạn:** Dữ liệu bị khóa đối với ứng dụng web cụ thể đó. Một ứng dụng di động hoặc hệ thống khác sẽ khó tích hợp.

---
## Turtorial

###  (Xuân + Quang Huy)
**FE + DB:** https://youtube.com/playlist?list=PLIY8eNdw5tW_ZQawyxK0Dd1cZXwcNFWn8&si=hNos2vT9IVm7uaI8
	Bao gồm các Function Add/Delete/Update/View cho phần quản lý Assignment.

### (Quang Huy + Minh Nhật)
**Learn ASAP.NET CORE (FE + BE + DB) by building a Joke App:** https://youtu.be/BfEjDD8mWYg?si=cJKpDGxVh5RbVj1L
+ ? Nội dung video:	

### Minh Nhật
**Practice DB and Web API by making Pokemon Review WebApp**: https://youtube.com/playlist?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0&si=WAW5hB7W7g3uBX22


### Thành
**Login Page:** https://youtu.be/wzaoQiS_9dI?si=s-sUDK9qJWi6_CtP

**Scoring Section** 
+ [[Intergrate ChatGPT with WebApp]]
	search youtube for "How to intergrate ChatGPT to ASAP.NET Core" (chatGPT to evaluating code)
+ [Unit test to scoring code](https://youtube.com/playlist?list=PL82C6-O4XrHeyeJcI5xrywgpfbrqdkQd4&si=NRktX-ZqPMc6CGIH) 
	[[What is Unit & How can it help]]
