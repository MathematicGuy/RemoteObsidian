Project Name
Goal
	Do what?
	Product Function?
Input: (Text , Number)
Output: 
+ Initiation
	+ Theory, Fomula
	+ Experiment
+ Conclusion 


**Application of AI**
Nhận dạng + Thống kê cảm xúc khuôn mặt
	Phân loại cảm xúc.
Input: video 2-4s
Output: 


**DBSCAN**
là dựa trên mật độ của dữ liệu. Các cụm là đc định nghĩa là các vùng dữ liệu có mật độ cao và kết nối vs nhau. Giữa các cụm là các vùng có mật độ thấp hoặc rất thấp.

Để xd đc các cụm. Thuật toán DBSCAN sử dụng 2 tham số. 
	MinPts
	Epsilon 
	Việc hình thành các cụm đc thực hiện như sau: Xuất phát từ 1 điểm bất kì của dữ liệu chúng ta sẽ có hình cầu bán kính epsilon.
	Đếm xem trong hình cầu đó có tổng số điểm dữ liệu. Nếu có thì kết nạp số điểm các hình cầu đó
	Lặp đi lặp lại qtrinh đó với các điểm ở trong cụm. Đến khi ko tìm đc điểm nào nữa thì thôi.


Các điểm còn lại ko thuọc 
Thuật toán DBSCAN có thể phát hiện các cụm có hình dạng bất kì.Phất hiện ra cả các bất thường trong dữ liệu. 
Nhược điểm: Độ phức tạp tính toán O(n^2)

Việc xd MinPts và Epsilon là ko dễ. 

Đếm xem trong số hình cầu đó >= MinPts
Ci = {x1, x2, x3, x4,..,xn}


Nêu các phương pháp đánh giá chất lượng của các thuật toán. Và đánh giá kết quả.

ADORABLE
