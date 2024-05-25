> Tốc độ chạy của Thuật Toán. 
	+ Thuật toán tìm kiếm.
	+ Phương pháp tốt nhất cả về Thời Gian và Không Gian.

#### Hai Yếu Tố Chính cần chú tâm khi thiết kế Thuật Toán Hiệu Quả.
1) **Thực hiện Phép so sánh**: 
	TH: Tốt Nhất - Tồi Nhất - Trung Bình. Để tìm ra, **đảm bảo Phương Pháp Tối ưu nhất**.
	Kết quả Đầu ra như Mong Muốn
2) **Đáp Ứng Thời gian xử lý và GIới Hạn bộ nhớ mong muốn**
	Hiệu năng: Tối ưu thời gian, bộ nhớ, xử lý đc nhiều TH khác nhau.
*Độ Phức Tạp Thuật Toán do Khả Năng của mình*
> Phụ Thuộc vào Kích Thước Đầu vào, thời gian, không gian bộ nhớ.
- **Time Complexity**
> *Tổng thời gian* thực hiện/chạy thuật toán. Mỗi Dòng lệnh có thể có thời gian xử lý khác nhau.
> + Được đo bởi các *phép toán chính*:
> 	VD: phép toán so sánh.
![[Pasted image 20230627121950.png]]
> Tổng Thời Gian Nhân với N lần
![[Pasted image 20230627122119.png]]
	Tính Theo Số có bậc Cao Nhất (vd: c5 )

#### Asymptotic notation (Ký Hiệu Tiệm Cận)
> Khi bỏ qua số hạng bậc thấp (vô cùng bé). Chỉ quan tâm đến Biến lớn nhất (c4 * n, c5 * n)
> - Biểu Thị TH Thời Gian: 
> 	**θ** : *Tồi nhất* 
> 	**O** : *Trung Bình*
> 	**Ω** : *Tốt nhất*
> 𝑇(𝑛) = 𝑐1 + 𝑐3 + 𝑐4 × [𝑛 + 𝑐5 × 𝑛] -> Lớn nhất. Đại diện cho F(n)
> **Trong Phương Trình chọn Số có Bậc Lớn Nhất**

>![[Pasted image 20230628105359.png]]
**c** -> 1 số cụ thể nào đó.
**F(n)** -> Hàm số biểu thị Thời gian.
> **c.F(n) -> Độ Phức Tạp Thời Gian.**

#Example4 
![[Pasted image 20230628105746.png]]
[ Thực Hành và Note Trong Annotation ]

#### Quy Tắc Tổng
![[Pasted image 20230628112138.png]]

