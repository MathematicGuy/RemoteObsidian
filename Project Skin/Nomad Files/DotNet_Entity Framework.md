note: 
+ EF - Entity Framwork
+ EDMX (Entity Data Model XML)
+ CRUD (Create, Read, Update, Delete)
+ ORM (Object-Relational Mapping)

---
Entity Framework Core là một **framework ORM cho .NET.**






```cs
var blog = mycontext.Blogs.FirstOrDefault(b => b.BlogId == 1); 
```
**Result**
- If a blog with `BlogId` of 1 exists, the `blog` variable will hold a `Blog` object representing that database entry.
- If no blog exists with that ID, the `blog` variable will be null.


### **Công cụ "Update Model from Database":**
- Cập nhật file EDMX tự động dựa trên thay đổi trong cơ sở dữ liệu.
- Giữ nguyên dữ liệu và cấu hình hiện có.
- Cách đơn giản và hiệu quả nhất để cập nhật EDMX.
	
**Cách sử dụng:**
1. Mở file EDMX trong Visual Studio.
2. Nhấp chuột phải vào file EDMX và chọn "Update Model from Database".
3. Chọn các thay đổi muốn cập nhật và nhấp chuột vào "Finish".
**Lưu ý:**
- Luôn sao lưu file EDMX trước khi cập nhật.
- Giải quyết xung đột (nếu có) sau khi cập nhật.


**EF không tự động xử lý** các mô hình kế thừa phức tạp khi tạo migration.
- Cần **cấu hình** cách thức EF tạo bảng và cột cho các loại kế thừa.
- Hai phương pháp phổ biến:
    - **Table-Per-Type (TPT):** Tạo bảng riêng cho mỗi loại kế thừa.
    - **Table-Per-Hierarchy (TPH):** Tạo bảng chung cho tất cả các loại kế thừa.

DbSet đóng vai trò như một tập hợp các thực thể (entity) trong mô hình dữ liệu cho phép thực hiẹn thao tác CRUD.


Entity Framework Core, migrations được sử dụng để: **Quản lý thay đổi cấu trúc cơ sở dữ liệu.**
	Bằng migrations, có thể thực hiện CRUD vs bảng, cột và ràng buộc trong cơ sở dữ liệu một cách dễ dàng.


EF don't support MongolDB


```cs
<connectionStrings>
	<add name="StudentDBConnectionString"
		 connectionString="Server=macbookM5\SQLEXPRESS;Database=StudentDB;User Id=sa;Password=cmcuni;"
		 providerName="System.Data.SqlClient" />
</connectionStrings>
	
```