2:10:52
### Basic Concept
> **Tree** is a non-linear data structure. thus tree have Parent-Child relationship. (Quan hệ phân cấp - cha con)
+ **Top Node** called **Root Node**.
	**Also a Node**. Thus **it is connected** to other node
+ **Last Nodes** called **Leaf.**
	These are **Nodes**. Thus **they be connected** to 
+  **All Nodes** in the **Middle called Branch**
	Can be **both parent & child** (thus it is and be connected to others node)
![[Pasted image 20230801111104.png]]
+ If **more than 1 Node shared a Parent**. They called **Sibling**. 
+ **Sub Tree** is the Tree that **held inside other Trees**.
> n là số cạnh
#### Height & Depth
**Level (Tầng)
	Bắt đầu từ 0 tầng 1 ở nhánh gốc và tăng lên dần.**
![[Pasted image 20230801111726.png]]
#### Degree (Mức ĐỘ)
**Số Con mà phần tử có (chỉ tính 1 tầng dưới nó)**
![[Pasted image 20230807214947.png]]


Áp dụng trong toán tử và toán hạng.
![[Pasted image 20230801114430.png]]


Node cha 
+ = vị trí Node con / 2
	VD: 3 / 2 = 1.5 = 1 (làm tròn xuống)
Nút con
+ = 2 * index_node cha 
+ =  2 * index node cha + 1 
![[Pasted image 20230802112158.png]]


Với Tree bị Lệch Trái hoặc Phải
	Thì sẽ cần thêm 1 phần tử rỗng cho mỗi Nodes bị lệch
-> (Gây Lãng phí bộ nhớ)
Các phần tử con có phần tử cha là (vị trí Node con * 2)
![[Pasted image 20230802112438.png]]
**Giải pháp**
	Dùng các con trỏ móc nối
	![[Pasted image 20230802112803.png]]

Thăm tất cả các nút trong cây -> Duyệt cây

## Tree traversal (Duyệt cây Nhị Phân)
+  Ưu tiên Duyệt Trái trước

**Quét Tree từ Giữa **
(Triagle scan from bottom up) 
+ G -> D -> H 
+ B -> E -> A 
+ C -> F
	Muốn túm lấy cây thì túm lấy gốc của nó.
![[Pasted image 20230802115945.png]]


**Duyệt Tree từ Trên Xuống (trái) rồi từ dưới lên (phải)**
	Duyệt xuống tầng cuối rồi mới duyệt lại các tầng trước nó/
+ A -> B -> D -> G
+ H -> E -> C -> F
	Muốn túm lấy cây thì túm lấy gốc của nó.
![[Pasted image 20230802115945.png]]


**Duyệt Tree từ Trên Xuống**
Duyệt hết lớp con rồi mới lên lớp cha
VD: có **2 Node con thì quét 2 Node con tr'c rồi mới quét Node cha.** (nclncl Quét hết lá trước khi quét cành)
Nói 1 cách khác, với mỗi Nodes cha thì phải quét hết Node con tr'c.
+ G -> H -> D -> E
+ B -> F -> C -> A (quét node hiện tại rồi xuống node của tầng thấp nhất)
	Muốn túm lấy cây thì túm lấy gốc của nó.
![[Pasted image 20230802115945.png]]


### Breadth-first traversal
+ **Duyệt theo chiều Ngang or chiều Rộng**
	Tại mỗi lớp thì duyệt hết các Nodes theo chiều ngang rồi mới Dịch xuống Tầng Dưới.
![[Pasted image 20230802121146.png]]


![[Pasted image 20230926115331.png]]
![[Pasted image 20230926115347.png]]

### Dept-First Search

![[Pasted image 20230926123340.png]]


## Balance Tree


Cách nhau 1 lớp vẫn là cây Cân Bằng
=> Cách nhau, Chênh nhau nhiều nhất về độ cao là 1. 

## Binary Search Tree
Chia đôi đến khi tìm thấy kết quả.
	 Mỗi nút có tối đa 2 Nút con.
**Nút Trái < Nút gốc < Nút Phải**

Key - số cần tìm
+ Bắt đầu quét từ trên xuống: Nếu Bé Hơn thì quét Trái. Lớn hơn thì quét Phải.

## [[AVL Trees]]




# Algorithm Design Strategy

## Devide and Conquer
*Break an Problem into sub-problem*
+ *Sub-problem remain the same type of problem as Main Problem*.
	Ex: Sort cannot convert to Search.
+ Can be Recursive
+ Have a *Method to combine sub-problem*
![[Pasted image 20230926140312.png]]

**Algorithm**
![[Pasted image 20230926140648.png]]

**Problem Type for this**
![[Pasted image 20230926140714.png]]
## Dynamic Programming 

1. Greedy Method
2. Dynamic Programming

**recursion**
> Algorithm that run it self and return a result.

> Fibonacci 
![[Pasted image 20230926141532.png]]


**memoization**
> Improve run time by save result for recursing event.  

**Reducing Function call**
	Save the Calculated result then use for later
Restore for the next function.
![[Pasted image 20230926141639.png]]



