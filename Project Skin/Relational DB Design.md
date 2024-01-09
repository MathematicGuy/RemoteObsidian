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


### Testing for Lossless-join Decomposition
![[Pasted image 20231228143943.png]]

Lập ma trận 
Tách
+ R thành 2 lược đồ con (2 dòng) - S->A, SI -> P
+ 4 cột (do có 4 thuộc tính) - SAIP

Bằng nhau trên F thì bằng nhau trên thuộc tính A 


### Functional Dependency
![[Pasted image 20231228173418.png]]
	If I have value of X, I can determint Y
	![[Pasted image 20231228173853.png]]

