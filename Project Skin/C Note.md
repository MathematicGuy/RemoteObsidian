### data type
![[DatatypesInC.jpg]]
The different between unsigned and default data form is that unsigned has no negative values.
> meaning it start from 0 to its limit
> Ex: short int go from -32,768 to 32,768 unsigned short int will be 0 to (32,768 * 2 = 65,535).

|Data Type|Size (bytes)|Range|Format Specifier|
|---|---|---|---|
|short int|2|-32,768 to 32,767|%hd|
|unsigned short int |2|0 to 65,535|%hu|
|unsigned int|4|0 to 4,294,967,295|%u|
|int|4|-2,147,483,648 to 2,147,483,647|%d|
|long int|4|-2,147,483,648 to 2,147,483,647|%ld|
|unsigned long int|4|0 to 4,294,967,295|%lu|
|long long int|8|-(2^63) to (2^63)-1|%lld|
|unsigned long long int|8|0 to 18,446,744,073,709,551,615|%llu|
|signed char|1|-128 to 127|%c|
|unsigned char|1|0 to 255|%c|
|float|4|1.2E-38 to 3.4E+38|%f|
|double|8|1.7E-308 to 1.7E+308|%lf|
|long double|16|3.4E-4932 to 1.1E+4932|%Lf|



HW
**Câu 1 (2đ)**

          Viết hàm nhập vào từ bàn phím số nguyên n trong khoảng [1,50], nếu nhập sai thì nhập lại. Gọi hàm trong hàm main() để nhận được giá trị của biến nguyên n. Hiển thị n dưới dạng nhị phân.

**Câu 2 (1đ).**

Kiểm tra một số n nguyên, biết rằng nếu bit thứ 3 tính từ phải sang của n là bit 1 thì đặt bit này về 0 và nhận được biến nguyên m mới. Hiển thị m dưới dạng nhị phân. Yêu cầu: Trong hàm main() viết không quá 3 lệnh để kiểm tra.

**Câu 3 (2đ)**.

Viết hàm **_nhapmang_** nhập vào từ bàn phím mảng động với n số nguyên 2 byte. Khi nhập các phần tử của mảng, nếu nhập sai thì nhập lại.

**Câu 4 (2đ).**

Trong hàm main() khai báo một biến địa chỉ pa, là con trỏ đến các vùng nhớ lưu các số nguyên 2 byte xếp liền nhau. Cấp phát động một vùng nhớ lưu được n số nguyên 2 byte và gán địa chỉ cho pa. Gọi hàm **_nhapmang_** để nhập giá trị của n phần tử liền nhau này. Hiển thị n giá trị được nhập.

**Câu 5 (1đ).**

Viết hàm tính giá trị phần tử nhỏ nhất của mảng n số nguyên. Trong main() gọi hàm để lấy giá trị nhỏ nhất trong n phần tử nguyên 2 byte của vùng nhớ tại địa chỉ pa.

**Câu 6 (2đ).**

Viết hàm ghi một mảng n phần tử lưu các số nguyên 2 byte lên 1 file text với tên file là đối của hàm, mỗi dòng của file text lưu không quá 3 phần tử của mảng, giữa các phần tử trên một dòng cách nhau bởi khoảng trắng.

Gọi hàm trong hàm main() để ghi vùng nhớ tại địa chỉ pa lên file  “mang_nguyen.txt”.

Sau khi ghi xong thì giải phóng vùng nhớ tại địa chỉ pa và gán địa chỉ pa về giá trị phù hợp.