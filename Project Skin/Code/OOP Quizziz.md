###### _**CÂU HỎI**_

1. Thế nào là lập trình hướng đối tượng ?
    
2. Các tính chất của hướng đối tượng là gì ?
    
3. Thế nào là lớp?
    
4. Thế nào là đối tượng?
    
5. Thế nào là tính đóng gói?
    
6. Có mấy loại access modifier? Phân biệt sự khác nhau giữa chúng?
    
7. Thế nào là tính đa hình?
    
8. Phân biệt override và overload?
    
9. Có thể override 1 static method không?
    
10. Thế nào là tính trừu tượng?
    
11. Có thể sử dụng thuộc tính trong interface?
    
12. Interface có thể là final không?
    
13. Có thể cài đặt phương thức trong interface?
    
14. Có thể cài đặt phương thức trong abstract class?
    
15. Có thể cài đặt nhiều interface trong class không?
    
16. Thế nào là tính kế thừa?
    
17. Có thể sử dụng constructor của lớp cha để tạo đối tượng cho lớp con không?
    
18. Thế nào là static?
    
19. Thế nào là final?
    
20. Có bắt buộc phải khai báo constructor trong lớp?
    

###### _**CÂU TRẢ LỜI**_

###### 1. THẾ NÀO LÀ LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG ?

Lập trình hướng đối tượng là một phương pháp lập trình dựa trên khái niệm về lớp và đối tượng. Nó tập trung vào các đối tượng thao tác hơn là logic để thao tác chúng, giúp code dễ quản lý, tái sử dụng được và dễ bảo trì.

###### 2. CÁC TÍNH CHẤT CỦA HƯỚNG ĐỐI TƯỢNG LÀ GÌ ?

Lập trình hướng đối tượng bao gồm 4 tính chất

- Tính đóng gói
    
- TÍnh kế thừa
    
- Tính trừu tượng
    
- Tính đa hình
    

###### 3. THẾ NÀO LÀ LỚP?

Một class đại diện cho 1 loại đối tượng. Nó có thể được hiểu giống như 1 bản định nghĩa của đối tượng.

###### 4. THẾ NÀO LÀ ĐỐI TƯỢNG?

Đối tượng là một thể hiện của lớp. Nó bao gồm các thuộc tính và phương thức.

###### 5. THẾ NÀO LÀ TÍNH ĐÓNG GÓI?

Đóng gói là việc che giấu các thông tin quan trọng của 1 lớp. Nó được thể hiển thông qua các access modifier như private, public, default, protected

###### 6. CÓ MẤY LOẠI ACCESS MODIFIER? PHÂN BIỆT SỰ KHÁC NHAU GIỮA CHÚNG?

Có 4 loại access modifier là: private, protected, default, public. Trong đó:

- **Private**: Chỉ có thể truy cập trong cùng class.
    
- **Default**: Có thể truy cập trong cùng class và cùng package.
    
- **Protected**: Có thể truy cập trong cùng class, package và ngoài package bởi lớp con.
    
- **Public**: Có thể truy cập ở bất cứ đâu.
    

###### 7. THẾ NÀO LÀ TÍNH ĐA HÌNH?

Tính đa hình là khi một hành động có thể được thực hiện theo nhiều cách khác nhau. Nó được thể hiện thông qua override và overload.

###### 8. PHÂN BIỆT OVERRIDE VÀ OVERLOAD?

Overide là việc lớp con ghi đè phương thức của lớp cha. Overload là việc một class sử dụng được cùng một phương thức nhưng khác nhau biến truyền vào hàm

###### 9. CÓ THỂ OVERRIDE 1 STATIC METHOD KHÔNG?

Không.

###### 10. THẾ NÀO LÀ TÍNH TRỪU TƯỢNG?

Tính trừu tượng là ẩn các chi tiết triển khai và chỉ hiển thị các tính năng với người dùng. Tính chất này cho phép loại bỏ các tính chất phức tạp của đổi tượng, chỉ cần đưa ra các tính chất cần thiết trong lập trình giúp tập trung vào những cốt lõi của đối tượng. Nó được thể hiện thông qua interface và abstract class.

###### 11. CÓ THỂ SỬ DỤNG THUỘC TÍNH TRONG INTERFACE?

Có. Thuộc tính phải là hằng số và được khai báo với từ khóa final.

###### 12. INTERFACE CÓ THỂ LÀ FINAL KHÔNG?

Không. Vì cần phải có một lớp implement interface thì mới sử dụng được.

###### 13. CÓ THỂ CÀI ĐẶT PHƯƠNG THỨC TRONG INTERFACE?

Không thể

###### 14. CÓ THỂ CÀI ĐẶT PHƯƠNG THỨC TRONG ABSTRACT CLASS?

Có. Phương thức không phải là abstract method thì có thể cài đặt.

###### 15. CÓ THỂ CÀI ĐẶT NHIỀU INTERFACE TRONG CLASS KHÔNG?

Có

###### 16. THẾ NÀO LÀ TÍNH KẾ THỪA?

Là khả năng tái sử dụng lại thuộc tính và phương thức của một lớp. Thể hiện thông qua từ khóa extend.

###### 17. CÓ THỂ SỬ DỤNG CONSTRUCTOR CỦA LỚP CHA ĐỂ TẠO ĐỐI TƯỢNG CHO LỚP CON KHÔNG?

Không. Phải cài đặt lại constructor trên lớp con. Có thể sử dụng từ khóa super() để gọi lại đối tượng của lớp cha.

###### 18. THẾ NÀO LÀ STATIC?

Những hàm, phương thức có từ khóa static sẽ thuộc về lớp có thể được truy cập trực tiếp từ Class mà không cần phải tạo đối tượng.

###### 19. THẾ NÀO LÀ FINAL?

Những thuộc tính final sẽ không thể thay đổi giá trị của nó Những phương thức final sẽ không thể overide ở lớp con Những class final sẽ không thể kế thừa được

###### 20. CÓ BẮT BUỘC PHẢI KHAI BÁO CONSTRUCTOR TRONG LỚP?

Không. Nếu không khai báo constructor, class sẽ sử dụng default constructor