source: [Lec 1: Introduction to DBMS | Database Management System - YouTube](https://www.youtube.com/watch?v=T7AxM7Vqvaw&list=PLdo5W4Nhv31b33kF46f9aFjoJPOkdlsRc)

## **Amstrong Axiom**

1. Phản xạ: Nếu Y ⊂ X thì  X → Y
2. Tăng trưởng: Nếu Z ⊂ U và X → Y thì XZ → YZ

(Ký hiệu: XZ là X ∪ Z)

3. Bắc cầu: Nếu X → Y và Y → Z thì X → Z
4. Giả bắc cầu: Nếu X → Y và WY → Z thì XW → Z
5. **Luật hợp**: Nếu X → Y và X → Z thì X → YZ
6. **Luật phân rã**: Nếu X → Y và Z ⊂ Y thì X → Z (vì Z ⊂  U == Y -> Z)

[Bài tập tính bao đóng](https://tailieu.vn/docview/tailieu/2018/20180206/saobien_09/csdl_chuong_5_phu_thuoc_ham_5456.pdf?rand=828051)

![[Pasted image 20231228140354.png]]
Lý thuyết phụ thuộc hàm
+ bao đóng của tập thuộc tính
+ bao đóng của tập phụ thuộc hàm
+ khóa

Dependency preserving
A xác định B -> A xác định AB

mỗi dòng tương đương vs 1 quan hệ 
mỗi cột tương đương vs 1 thuộc tính


## Normalization
Chuẩn hóa là gì: 
> Đây là một kỹ thuật thiết kế bảng trong cơ sở dữ liệu, chia các bảng lớn thành các bảng nhỏ hơn và liên kết chúng bằng các mối quan hệ. 
+ Các dạng chuẩn hóa cao hơn sẽ có hết các tiêu chí của chuẩn hóa trước.

[Dạng chuẩn hóa 1NF, 2NF, 3NF](https://youtu.be/TKYd6gKF2Cc?si=xS5_Ztw9-xkAEUbq)

F = { AB -> C, B -> C }
B -> C: Phụ thuộc hàm nguyên tố: 
AB -> C: Không phải hàm nguyên tố

### 1NF (First Normal Form)


### 2NF
+ Trong bảng có thể có 2 khóa. Và có thể bắc cầu sang 1 bảng khác.
+ Cái nào phụ thuộc vào cái gì thì chia nó ra.

VD: DiemDA, TenDA chỉ phụ thuộc vào MaDA nên sẽ chia ra 2 bảng DUAN(MaDA, TenDA, DDiemDA) và NV_DA(MaNV, MaDA, Sogio) .
+ Tuy nhiên nó sẽ tạo ra việc MADA là thuộc tính có tính chất bắc cầi 
![[Pasted image 20240109113556.png]]


### 3NF 
+Trong bảng chỉ có 1 khóa