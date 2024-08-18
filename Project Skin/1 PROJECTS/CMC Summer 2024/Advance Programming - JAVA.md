[springboot.io](https://start.spring.io/)

Create Spring Boot Project
+ Setup IntelliJ
+ Create Project from [Maven Spring Boot Template](https://start.spring.io/#!type=maven-project&language=java&platformVersion=3.3.0&packaging=jar&jvmVersion=22&groupId=com.example&artifactId=ProjectOne&name=ProjectOne&description=Learn%20Bakcend%20using%20Spring%20Boot&packageName=com.example.ProjectOne&dependencies=web,devtools) 
+ Open the Project from IntelliJ 

**Spring Folder Structure**
+ main/java - main code. your main project java file store in here
+ test
+ pom.xml - dependencies


	JSP (like Razor page in C#)

JDBC Bridge -> Turn many Database Language into 1 form so that it can work together as 1. 
![[300px-Network_Protocol_driver.png]]

# [[How to build a web application in Java]]
Controller: Servlet
Dal: Java
Model: Java Class
Web Pages: JSP, HTML (view)



[](https://stackoverflow.com/posts/7348934/timeline)

Try cleaning-up your local repository with:

```
git gc --prune=now
git remote prune origin
```


Spring Data -> automatically simple CRUD operation

[[Full Stack Java]]
MSSQL - https://hub.docker.com/r/microsoft/mssql-server
[[Docker MSSQL]]

---

Ưu Tiên Triển Khai Dự Án

### Thứ tự ưu tiên các tính năng:

#1. Đăng Ký (Register)
#2. Đăng Nhập (Login)
#3. Quên Mật Khẩu (Forgot Password)
#4. Thanh Toán (Payment)
#5. Tải Lên File Ảnh/Tài Liệu (Dashboard - Side Bar)
#6. Tải Về Ảnh/Tài Liệu (Dashboard - Header)
#7. PDF OCR (OCR)
#8. Chuyển File Ảnh Sang File Text, Docx, PDF, Excel (Dashboard - Side Bar)
#9. Nhận Dạng Chữ Viết Tay (OCR)
#10. Xem Và Chỉnh Sửa PDF (Edit PDF)
#11. Xoay Trang Trong File PDF (Organize)
#12. Xóa Trang Trong File PDF (Organize)
#13. Ghép Trang File PDF (Organize)
#14. Tách Trang Trong File PDF (Organize)
#15. Nhân Bản Trang Trong File PDF (Organize)
#16. Tóm Tắt PDF (AI)
#17. Trò Chuyện Với File PDF Sử Dụng Chatbot (AI)
#18. Dịch Trang PDF (AI)
#19. Cung Cấp Dịch Vụ API OCR (Subscriptions)
#20. Đăng Ký Gói Dịch Vụ Cá Nhân (Subscriptions)
#21. Cung Cấp Gói Dịch Vụ Mặc Định Cho Doanh Nghiệp (Subscriptions)
#22. Cung Cấp Gói Dịch Vụ Theo Nhu Cầu Doanh Nghiệp (Subscriptions)
#23. Theo Dõi Lịch Sử Sử Dụng (Manage Subscriptions)
#24. Theo Dõi Lịch Sử Thanh Toán (Manage Subscriptions)
#25. Quản Lý Tài Khoản (Xóa Tài Khoản, Chỉnh Sửa Thông Tin Cá Nhân
#26. Feedback, Hỗ Trợ Riêng (Customer Support)
#27. Hỗ Trợ Tài Khoản Cá Nhân (Customer Support)
#28. Gửi Thông Báo Đến Người Dùng Về Trạng Thái Giao Dịch (Manage Users Account
#29. Xem Tài Khoản Người Dùng (Manage Users Account)
#30. Kích Hoạt/Vô Hiệu Hóa Tài Khoản (Manage Users Account)
#31. Xem Mọi Tài Khoản Người Dùng (View Account Detail)
#32. Xác Nhận Tài Khoản (View Account Detail)
#33. Phân Quyền Người Dùng (View Account Detail)
#34. Cập Nhật Trạng Thái Giao Dịch (View Account Detail)
#35. Truy Cập Danh Sách Các Giao Dịch Mua Dịch Vụ Của Người Dùng (Subscriptions
#36. Truy Cập Mọi Danh Sách Hợp Đồng của Từng Doanh Nghiệp (Subscriptions Overview)
#37. Xem Chi Tiết Thông Tin Dịch Vụ Của Từng Người Dùng (Admin Dashboard)
#38. Xem Mọi Tài Khoản Doanh Nghiệp (Manage Enterprise Account)
#39. Kích Hoạt/Vô Hiệu Hóa Doanh Nghiệp (Manage Enterprise Account)
#40. Gửi Thông Báo Đến Doanh Nghiệp Về Trạng Thái Hợp Đồng (View Enterprise Detail
#41. Xem Chi Tiết Thông Tin Hợp Đồng Của Doanh Nghiệp (View Enterprise Detail)
#42. Cập Nhật Trạng Thái Hợp Đồng (View Enterprise Detail)
#43. Tải Xuống Bản Sao Hợp Đồng Dưới Dạng File PDF (View Enterprise Detail)
#44. Kích Hoạt/Hủy Dịch Vụ Api OCR (View Enterprise Detail)
#45. Thống Kê Dịch Vụ (View Enterprise Detail)
#46. FAQs (Home Page)

### Hướng phát triển:

1. **Tạo các API cơ bản cho Đăng ký, Đăng nhập, và Quên mật khẩu**: Đây là các tính năng cơ bản cần hoàn thiện đầu tiên vì chúng là cửa ngõ để người dùng sử dụng hệ thống.
    
2. **Tích hợp thanh toán**: Phát triển các API liên quan đến thanh toán là bước quan trọng tiếp theo để đảm bảo rằng người dùng có thể thực hiện các giao dịch tài chính một cách an toàn và hiệu quả.
    
3. **Xử lý file OCR và các chức năng liên quan**: Tập trung vào xây dựng các API để tải lên, xử lý, và tải về file tài liệu, PDF OCR là phần cốt lõi của hệ thống.
    
4. **Phát triển chức năng chỉnh sửa PDF**: Sau khi hoàn thiện OCR, phát triển các tính năng liên quan đến chỉnh sửa PDF để đáp ứng nhu cầu của người dùng về thao tác với tài liệu.
    
5. **Xây dựng và triển khai các tính năng AI**: Các tính năng AI như tóm tắt, dịch trang PDF, và chatbot nên được xây dựng sau khi các chức năng cơ bản hoạt động ổn định.
    
6. **Quản lý tài khoản và dịch vụ**: Sau khi hoàn thành các tính năng cốt lõi, tiến hành phát triển các tính năng quản lý tài khoản, dịch vụ, và theo dõi lịch sử sử dụng, thanh toán.
    
7. **Tính năng nâng cao cho doanh nghiệp**: Cuối cùng, triển khai các tính năng nâng cao dành cho tài khoản doanh nghiệp, như quản lý hợp đồng, dịch vụ API, và thống kê dịch vụ.\

---

Embedding PDF
![[Pasted image 20240818144708.png]]

Query Format
![[Pasted image 20240818144902.png]]

