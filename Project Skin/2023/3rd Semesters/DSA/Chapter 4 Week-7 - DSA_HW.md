 ![[Pasted image 20230816093637.png]]

Thuật Toán tìm sinh viên có điểm trung bình học tập là 9:
1.  Bắt đầu từ Đầu của Linked List
2. Quét qua từng Node trong List
3. Với từng Node, Kiểm tra nếu Key (điểm trung bình) bằng 9 hay không. 
4.  Nếu có Tìm thấy Node bằng 9, quay về INFO (mã sinh viên) và trả lại mã sinh viên
5. Nếu không tìm thấy, quay về None.

```python
class Node:
    def __init__(self, key, info, link=None):
        self.key = key
        self.info = info
        self.link = link

def find_student(L, score):
    current_node = L
    while current_node is not None:
        if current_node.key == score:
            return current_node.info
        current_node = current_node.link
    return None

# create 3 nodes
node1 = Node(5, "BIT1")
node2 = Node(7, "BIT2")
node3 = Node(9, "BIT3")
# connect node to form a linked list
node1.link = node2
node2.link = node3
nodeList = [node1, node2, node3]

print(find_student(node1, 9))
# BIT3
```

![[Pasted image 20230816100852.png]]
### Tìm Kiếm Tuần Tự (so sánh từng phần đến (chết) khi thảo mãn)
 1. For each item in the list:
     **if** that item has the desired value,
          then stop the search and return the item's location.
 2. Return **Δ**

- Với phần tử cần tìm là 23, ta quét dãy mất O(2) thời gian -> 23 Tìm đc ở vị trí thứ 2
- Với phần tử cần tìm là 72, ta quét dãy mất O(n) thời gian -> 72 không tìm được trong Dãy

### Tìm Kiếm Nhị Phân (Chia đôi dãy và so sánh với số trung vị đến khi điều kiện thỏa mãn)
(Có Trung vị có dãy ở vị trí thứ 5: 58)
+ Với số cần tìm là 23
1)  23 > 58 -> Chia đôi dãy. Lấy dãy để so sánh  mới là mọi số bé hơn 58 {11,23,36,42}
2) Trung vị của dãy là 23, Ta tìm đc 23 == 23, Dừng Thuật toán.
+ Với số cần tìm là 72
1) 72 > 58, Gạc bỏ Mọi số bé hơn hoặc bằng 58. Lấy Các số còn lại làm 1 dãy để so sánh  mới {65,74,87,94,99}
2) Trug vị là 74, 74 > 72 nên lấy số bé hơn 74 làm dãy để so sánh mới {64}. 
3) Còn 1 số nên so sánh luôn, do 74 > 64. Nên không trả lại gì hết, Dừng Thuật toán.

![[Pasted image 20230816143054.png]]

Cây tìm kiếm Nhị phân là cây Cân Bằng (Balance Tree or Perfect Tree) có đặc điểm là:
bf - balance factor.
rh - right height
lh - left height
	**(bf <= 1) Chênh nhau nhiều nhất về độ cao là 1.** 
	+ **balance factor** (BF)= **left height** (LH) - **right height** (RH)
	+ **| BF | = |  LH - RH |** <= 1
Dựa vào tiêu chí trên **cây cân bằng trong hình là: A, C, D** 
VD:  Đây ko đc coi là cây cân bằng, vì bf > 1. 
![[Pasted image 20230816143731.png]]

![[Pasted image 20230816143822.png]]
a) 
So sánh số cần chèn bắt đầu từ Gốc
	Bé hơn thì làm con Trái | Lớn hơn làm con Phải
![[Pasted image 20230816200720.png]]
**Với 6**. Với mỗi lần sâu xuống 1 tầng
	6 < 10. Sang trái 
	6 > 5. Sang phải
	6 < 9. Sang trái
	6 < 7. Sang Trái.
	6 Trở thành Node con Trái với Node Cha là 7
**Với 14**
	14 lớn hơn 10. Sang Phải
	14 < 15. Sang Trái
	14 > 13. Sang Phải
	Vậy 14 trở thành Node Con phải với Node Cha là 13

b) Sau khi Xóa 1 Nút có Con. Nút con ở tầng dưới cùng sẽ là Nút Kế Thừa. (Ưu tiên nút trái)
Thuật toán Xóa.
![[Pasted image 20230816202014.png]]
Thuật toán tìm successor.

![[Pasted image 20230816200817.png]]
+ Delete 13, Ko có thay đổi gì hết vì 13 là Nút Lá
![[Pasted image 20230816201426.png]]

+ Delete 15. 18 Kế thừa nên sẽ nối vs 10. 13 nối vs 18 nên giữ nguyên
![[Pasted image 20230816200940.png]]

+ Delete 5. 7 Kế thừa nên sẽ nối vs 10, với 3 và 9 là nút 
![[Pasted image 20230816201411.png]]

+ Delete 10. 13 Kế thừa nên sẽ có Nút con là 7, 15.  Các nút lá của 7, 15 giữ nguyên.
![[Pasted image 20230816202145.png]]

![[Pasted image 20230816202125.png]]

**Cây Nhị Phân Hoàn Chỉnh**
	là một cây nhị phân có đều cân bằng ở mọi tầng, trừ tầng cuối cùng.
![[Pasted image 20230816202323.png]]
**Để đọc được Complete Binary Tree ta dùng thuật toán của Balance Binary Tree**
![[Pasted image 20230816203224.png]]

Đọc dãy số theo thứ tự sau: 42, 23, 74, 11, 65, 58, 94, 36, 99
Với mỗi Bước xuống 1 tầng
	+ Nếu Lớn Hơn thì Sang Phải
	+ Nếu Nhỏ Hơn thì Sang Trái
![[Pasted image 20230816204007.png]]

**Cây Nhị Phân Suy Biến**
![[Pasted image 20230816202636.png]]
 gốc và các cành, chỉ có 1 nút con.
	+ Cây Cây Nhị Phân Suy Biến có cấu trúc giống Dãy Tuyến Tính nên ta có thể sắp xếp theo cấu trúc Max -> Min hoặc Min -> Max.
=> Chọn phần tử bé nhất hoặc lớn nhất làm  rồi Insert tuyến tính theo thứ tự giảm hoặc tăng dần.
![[Pasted image 20230816204445.png]]

