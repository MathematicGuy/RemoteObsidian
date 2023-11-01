## Arrays
> Số phần tử Cố Định
Array (Mảng) - 1 chuỗi các phần tử. 
	+ Tập hợp phần tử cùng kiểu dữ liệu
	+ Các phần tử khác biệt vs nhau.
	+ Tuyến tính -> Liên tiếp và khác nhau.
	> number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

##### **One-Dimensional Arrays:**
	![[Pasted image 20230704101258.png]]
##### **Multi-Dimensional Arrays:**
+ Two-Dimensional Arrays
![[Pasted image 20230704101435.png]]

+ Three-Dimensional Arrays
+ ![[Pasted image 20230704101443.png]]


## Lists
> Các phần tử không Cố Định -> Có thêm thêm/bớt các phần tử
>(Có thể rỗng)
>+ atomic data: phần tử cơ bản
>+ Tính chất Tuyến tính: Khi biết giá trị 1 phần tử thì có thể đoán được giá trị tiếp theo.
![[Pasted image 20230704102310.png]]

## The Basic concept

**There are some common operations:** 
	• Accessing Values (modified values)
	• Insert an element into lists
	• Delete an element from lists
	• Concatenate two or more lists
	• Split a list into multiple lists
	• Copy a list
	• Update a list T

> Mảng trong OOP
> + pải khai báo: 
> 	+ Kiểu dữ liệu **int aray**
> 	+ Độ dài  **[10]** 
> 	+ Dữ liệu cho trước: {1,2,3,4,5,,7,8,9,10}
> ![[Pasted image 20230704102633.png]] 


**The basic operations supported by an array are as stated below**
	• **Traverse** − print all the array elements one by one. (in lần lượt)
	• **Insertion** − Adds an element at the given index. (chèn theo vị trí/giá trị)
	• **Deletion** − Deletes an element at the given index. (xóa theo vị trí/giá trị)
	// *Search = Sort  + Find*
	• **Search** − Searches an element using the given index or by the value. 
	• **Update** − Updates an element at the given index. 

source: [Python Array of Numeric Values (programiz.com)](https://www.programiz.com/python-programming/array)
#### using Arrays in Python
```python
from array import *
a = array('u', ['a','r','rouge','j','s','h'])

for x in a:
    print(x)
print(a[0]) 

// Operations
a.insert(1, "hehe")
a.remove(a)
a.index(r)
a[2] = "wholesome" // update wholesome word
```


## Linked List Operation.


#### [[What is are Pointers]]
>Quy Luật con Trỏ: Mọi Node đều phải Trỏ tới 1 điểm nào đó.
>VD:
	+ Đầu: Trỏ đến Node kế tiếp
	+ Giữ: Trỏ Đến Node kế tiếp và Node trước nó trỏ đến Nó. >
	+ Cuối: Trỏ đến None
Muốn gắn vào giữa 2 Nodes thì phải trỏ tới cả trỏ tr'c lẫn trỏ sau.

>
 + Nếu muốn truy cập thì chỉ cần chỉ thẳng tới là xong. Còn trong Danh sách thì phải duyệt từ đầu.

Tập trung vào Danh sách Nối Đơn
#### Singly Linked List:
![[Pasted image 20230704114630.png]]
> Cấu trúc con trỏ.

#### Insertion 


#### Search
> If the List contain the given character.
```python
iter() // 
``` 
? Tìm kiếm tuyến tính -> duyệt từ đầu đến cuối danh sách.

Đếm biến nhờ Search:
	current = head:
	while current: // current not == None
		curren = current.next
		count += 1

#### Delete
> Có thể xóa bằng cách ko nối nút nào với nó.

[Egg, Ham, Spam]
**First Node**
> Chuyển Head tới Node tiếp theo.
> self.head = current.next.
![[Pasted image 20230705111206.png]]

**Any Intermediate Node**
![[Pasted image 20230705111625.png]]
> cần biết 3 Node. Previous - Current - Next
> A,B,C để xóa Node B thì hướng con trỏ từ A -> C.
> current.data == data -> prev.next == current.next

![[Pasted image 20230705111725.png]]


**Last Node**
Node Hiện tại = None -> chứng tở nó là Node cuối.
> hướng Node tr'c đó = None nếu Node hiện tại = None. 
![[Pasted image 20230705110758.png]]

**Delete the Whole List**
> Xóa đầu + đuôi.
![[Pasted image 20230705112331.png]]


### Appilcation
> Dùng danh sách để tổ chức dữ liệu.
• **Dynamic memory allocation 
• **Implemented in stack and queue
• **In undo functionality of softwares
• **Hash tables, Graphs**



## STACKS
> Các phần tử được xếp chồng lên nhau.
> ![[Pasted image 20230705112730.png]]

Hoạt động Tuyến Tính (LIFO - last in first out)
=> this mean the Last Element in the stack is Removed First.

**Operation**
	**push** -> gán phần tử.
	**pop** -> lấy phần tử.
	**peek** -> chỉ đọc được phần tử cuối. 

=> Nếu muốn lấy đĩa ở cuối thì phải loại bỏ hết đĩa trên nó trước tiên.
![[Pasted image 20230705114227.png]]

#### 2 Important stack Operations (push & pop)
![[Pasted image 20230705114332.png]]

LIFO : Hiểu đơn giản là trong 1 Câu lệnh: Lệnh trên cùng chạy tr'c, lệnh thêm vào viết ở sau.
![[Pasted image 20230705114808.png]]

#### Basic Operations
• **Push**: Add an element to the top of a stack 
• **Pop**: Remove an element from the top of a stack 
	top == -1 means the top is Empty. 
• **IsEmpty**: Check if the stack is empty 
• **IsFull**: Check if the stack is full 
• **Peek**: Get the value of the top element without removing it


## Stack implemenation using arrays

#### Operation
+ ###### Push: 
	+ Check if Empty or Full yet.
	+ If Not:
		+ new.next = current.next 
		+ current.next = new.next
![[Pasted image 20230711120636.png]]


+ ###### Pop
+ Remove the top Element by pointing the Top element to another node thus removing it.

	+ Read & Remove Top element from Stack. Return None if Stack Empty.
	+ To implement:
		+ First, Checking Stack empty or not.
		+ If not, check wether the top node is pointing at another node.
			+ >> Change the Top Pointer. The next node should be at the top. 
			+ We do this by pointing **self.top** to **self.top.next**
![[Pasted image 20230711121444.png]]


`Code`
**Step1: Check whether the stack is Empty or not**
![[Pasted image 20230711121610.png]]
**Step2: Remove the top element**
![[Pasted image 20230711121719.png]]


## Applications of stack
#### Arithmetic expressions and Polish notation
> Các cách viết dấu và biể hiện phương trình khác.
+ **Prefix**: Tiền tố -> **dấu ở tr'c**
+ **Infix**: Trung tố -> **dấu ở giữa**
+ **Postfix**: Hậu tố -> **dấu ở sau**
![[Pasted image 20230711122159.png]]
Nghĩa đơn giản là sắp xếp theo thứ tự ưu tiên:
mũ, nhân chia tr'c, cộng trừ sau.
Ưu tiên phép tính kết hợp với ngoặc.   
	Tiền tố thì viết dấu tr'c -> Dấu nào Ưu tiên thì viết tr'c (Dấu trước số). 
	Hậu tố -> Cái nào ưu tiên sau thì viết trước (Dấu sau số).
	Trung tố: Viết như bth

>  
![[Pasted image 20230712103916.png]]
##### VD2: 
> **(1 + 5) * (8 - (4 + 1))**
==-> 1 5 + 8 4 1 + - *==

> **10 - 8 * 2 + (15 -9)/3**
10  8 2 * - 15 9 - 3 / +


**Recipe**
Lưu ý: FIFO (Vào tới đâu lấy tới đó)
>Độ ưu tiên của dấu: ^ * / + -
>**Cách sắp xếp**
>+ **Bước 1** - quét biểu thức từ Trái sang Phải Stack
>+ **Bước 2**  
>	 Nếu nó là một Toán Hạng (Dấu) đẩy nó vào.
>	 Nếu là Toán Tử thì cũng đẩy vào

>+ **Bước 4** -  Lấy từng phần tử. 
	> Cứ 2 Số thì tính với 1 Dấu
![[dauinstack.jpg]]


## Queues (FIFO rules)

