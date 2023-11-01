	
(Tuyến tính vì nằm liên tiếp, liền kề nhau)
(Mỗi Node chỉ tới 1 Node khác, trừ Node cuối)
> 	Is a **linear data structure**. **Each element contain in** a Seperate Obj called **a Node**
 
+ Head: First element.
+ Tail: Point to nowhere
+ Node: Being pointed and pointed to another node.
	A Node Include a Link to another Node
![[Pasted image 20230801121913.png]]

**There're 2 Form**  
+ **Single Linked List** (Chỉ tới Node sau nó)
	Each node store a **reference to the next node** in the List
+ **Double Linked List** (Chỉ tới cả Node trước lẫn sau)
	Each node store a **reference to the node Before & After** its.




**Delete, Sort, Append like List**
Khi Xóa, Thêm, các Nodes thay Trỏ hướng tới và Dịch List sang trái để duy trì thứ tự (index start from 0, 1, 2, etc...)



Pre-pend: add to head
append: add to tail
insert: add to anywhere in the list 

## Lợi Thế
> Chỉ cần thay Đầu và Đuôi
![[Pasted image 20230913151058.png]]

LinkedList nhận các node nối đuôi nhau. Miễn là còn Node thì mỗi node sẽ tự nối đuôi node còn lại. 

> **Xóa Nút cuối**
![[Pasted image 20230913164514.png]]

> **Xóa Nút bất kì**
![[Pasted image 20230913165105.png]]

Để 1 Node tồn tại, Node đó bắt buộc phải có 1 Node trỏ tới.
	Nếu không Node nào trỏ tới Node đó, nó đc coi như bị Xóa.
*Conclusion: Every node that not been linked get Deleted.*