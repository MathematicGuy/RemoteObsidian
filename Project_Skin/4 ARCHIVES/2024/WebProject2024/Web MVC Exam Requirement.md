**I. Viết  1 net core để setup database SQL server hoặc SQLExpress hoặc 1 hệ quản trị CSDL quan hệ khác theo phương pháp code first dựa trên Entity net core**
**a. Tạo net core project với khai báo code của các lớp: Model, context.**
ví dụ: "User", với các thuộc tính như tên, email, và mật khẩu...
**b. Chạy tool Package Manager console để tạo Migration, cập nhật CSDL gồm các bảng...**

**II. Xây dựng Web API sử dụng .NET Core** 
•	Tạo một dự án Web API sử dụng .NET Core:
+ model, context cùng với câu I
•	Tạo 1 controller web API, định nghĩa các action của controller để thực hiện các hoạt động CRUD trên model "User" (Create, Read, Update, Delete).
+ Tạo chuỗi kết nối CSDL ở I ở file appsettings.json
+ Lập trình file Progmam để thiết lập hỗ trợ:
+ Kết nối CSDL qua  chuỗi kết nối
+ Cho phép/không cho phép CORS
+ Hỗ trợ/không hỗ trợ https
+ Hỗ trợ Swagger UI.
•	Cấu hình API để trả về dữ liệu dưới dạng JSON.
•	Test thử Web API bằng Swagger UI, Postman, curl...

**III. Tạo một ứng dụng Web frontend:**
•	Sử dụng fetch API của JS để gọi các API endpoints từ Web API đã xây dựng.
•	Hiển thị dữ liệu từ Web API trên ứng dụng frontend và cho phép người dùng thực hiện các hoạt động CRUD (Create, Read, Update, Delete) thông qua giao diện người dùng.
Thêm cột vào bảng SCL bằng lệnh Entity, chỉnh sửa các Migrations.
+ Viết thêm 1 action để up dữ liệu cho các thực thể của bảng CSDL. 
•	Đảm bảo rằng ứng dụng frontend có tính bảo mật và phân quyền.

**IV. Tạo wab app MVC để hiển thi dữ liệu tương đương nội dung với mục III nhưng tất cả các thao tác gọi web API và hiển thị được thực hiện trên server (host cùng server domain với web API) và trả về client là trang HTML kết quả cuối cùng.**
+ Tạo Model tương tự II
+ Tạo View khi sửa index.cshtml
+ Tạo controller MVC:
điều hướng dữ liệu từ contrller sang View. Con

**V. Sử dụng dịch vụ miễn phí như  http://www.smarterasp.net hoặc https://freeasphosting.net ...để triển khai Web API lên một máy chủ.**
•	Triển khai ứng dụng frontend của bạn lên một máy chủ hoặc dịch vụ miễn phí khác (chẳng hạn như GLITCH).
•	Đảm bảo rằng ứng dụng hoạt động trên máy chủ miễn phí và có thể tương tác với Web API.