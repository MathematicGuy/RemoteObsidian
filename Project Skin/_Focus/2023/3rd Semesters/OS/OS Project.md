
Nộp trên: https://cmcuni-my.sharepoint.com/:f:/g/personal/nhanh_cmc-u_edu_vn/EjmI1FnrbY5HiGgFV4XQpe4Bk2hvgSxtjMKvpx1IM62NlA?e=myl26U
Điều kiện: Mỗi bạn chọn ít nhất 02 bài, điểm tối đa là 9, nếu được 10 thì các em phải có so sánh giữa hai thuật toán, tiêu chí so sánh có thể là thời gian, hiệu quả...

---
**10, 22, 20, 2, 40, 6, and 38**
## Bài 11. Viết chương trình cài đặt thuật toán Elevator tính thời gian tổng số cylinders và thời gian tìm kiếm (seek time). Tham khảo bài 5.22 phần c)


**Elevator algorithm (initially moving upward)**  
sắp xếp lại
Sort max
Sort 
_Giống như khi đi thang máy, Đi lên hết rồi mới xuống đón lần lượt các tầng ở dưới. (Trạng thái đang đi lên)_  
Thang máy đi lên: 20 -> 22 -> 38 -> 40 -> 10 -> 6 -> 2  
Tổng số cylinder = 2 + 16 + 2 + 30 + 4 + 4 = 58  
ĐS: 58 * 6 = 348 (ms)
##### Pseudo code (theo tư duy của người nhìn)
Sort the list from min to max  
	Start from the Current floor
		Sort Right_half  (traverse all upper floor)
		Sort Left_half (then trarverse all lower floor)



## Bài 12. Viết chương trình cài đặt thuật toán Modified-Elevator tính thời gian tổng số cylinders và thời gian tìm kiếm (seek time). Tham khảo bài 5.22 phần d)
**Modified Elevator algorithm  (upward)***
_Chỉ đón khách khi đi lên, thang máy đi xuống dưới cùng rồi mới đi lên đón khách_  
20 -> 20 -> 22 -> 38 -> 40 -> 2 -> 6 -> 10  
Tổng số Cylinder = 0 + 2 + 16 + 2 + 38 + 4 + 4 = 66  
ĐS: 66 * 6 = 396 (ms)




