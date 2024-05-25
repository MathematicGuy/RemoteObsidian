Viết chương trình bằng ngôn ngữ C thực hiện các yêu cầu sau:

Câu 1 (2 điểm): Viết hàm nhập vào từ bàn phím số nguyên 1 byte n trong khoảng [1,20]. Nhập sai thì yêu cầu nhập lại. Gọi hàm này trong hàm main() để nhận được giá trị của biến nguyên n. Hiển thị n trong dạng hexa.

Câu 2 (1 điểm): Trong hàm main(), viết 1 lệnh để lấy giá trị số tạo thành từ 4 bit thấp của biến n.  Hiển thị kết quả.

Câu 3 (3 điểm):

+Định nghĩa cấu trúc quyển sách Book gồm các trường: mã sách bookID, tên sách bookTitle, số trang pageCount, năm xuất bản year  và trường next địa chỉ vùng nhớ của phần tử tiếp theo (con trỏ liên kết next).

+Viết hàm nhập vào từ bàn phím danh sách "không quá n quyển sách" (không yêu cầu nhập trường next từ bàn phím) thỏa mãn:

Khi nhập nếu sai (trường bookID, tên sách bookTitle là xâu rỗng...)  thì bỏ qua không lưu.

Nếu nhập trường pageCount là <=0 thì kết thúc việc nhập và trả về vùng nhớ lưu địa chỉ phần tử đầu danh sách.

Câu 4 (3 điểm):

+Trong hàm main(), khai báo con trỏ head trỏ tới quyển sách đầu tiên của danh sách.

+Cấp phát động n vùng nhớ cho các quyển sách, mỗi phần tử Book được lưu trữ ở các vùng nhớ không có thể rời nhau.

+Gọi hàm nhập danh sách ở câu 3 để nhập giá trị cho các trường của n quyển sách. Sau đó, hiển thị thông tin của không quá n quyển sách vừa được nhập.

+ Duyệt từ phần tử đầu danh sách của các phần tử Book, trượt theo trường next cho đến khi không có phần tử tiếp theo, hiển thị thông tin tất cả cuốn sách xuất bản năm 2020.

Câu 5 (1 điểm):

+Viết hàm ghi danh sách liên kết đơn các quyển sách từ con trỏ head ra 1 file text, mỗi dòng lưu thông tin của 1 quyển sách.

+Gọi hàm này trong main() để ghi danh sách từ head ra file "danhsach_sach.txt" (không lưu trường next), sau đó giải phóng vùng nhớ cấp phát cho danh sách và gán lại giá trị cho head.



