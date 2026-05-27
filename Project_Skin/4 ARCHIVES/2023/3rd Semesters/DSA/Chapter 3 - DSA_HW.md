



**Trình bày giải thuật thực hiện các phép sau đây đối với danh sách liên kết đơn mà nút s tiên được trỏ bởi L:**

**a) Tính số lượng các nút của danh sách**

**b) Tìm nút thứ k trong danh sách, nếu có nút thứ k thì đưa ra địa chỉ nút đó, nếu không thì đưa ra địa chỉ None**

**c) Bổ sung một nút vào sau nút thứ k**

**d) Loại bỏ nút đứng trước nút thứ k**

**e) Thêm con trỏ M trỏ tới một nút có trong danh sách và một danh sách liên kết đơn khác có nút đầu tiên trỏ bởi P. Hãy chèn danh sách P vào sau nút trỏ bởi M.**

**f) Tách thành 2 danh sách mà danh sách sau trỏ bởi M (như ở câu e)**

**g) Đảo ngược danh sách đã cho, tức là tạo một danh sách L’ mà các nút móc nối theo thứ tự ngược lại so với L.**

```python
class Node:
	# Truyền tham số
	def __init__(self, data = None):
		self.data = data
		self.next = None

# Khởi tạo 1 danh sách liên kết
class LinkedList:
	def __init__(self):
		self.head = None;

	# a. Tính số lượng các node trong danh sách
	def count_nodes(self):
		# Khởi tạo current = None
		count = 0;
		# Lặp cho tới khi nào current != head có nghĩa là đến cuối danh
		# sách thì curent = curent.next = None
		while current:
			count += 1
			current = current.next
		return count
		
	# b) Tìm nút thứ k trong danh sách,
	# nếu có nút thứ k thì đưa ra địa chỉ nút đó, nếu không thì đưa ra địa chỉ None
	def find_kth_node(self, k):
		current = self.head
		# Set count = 1 dùng vs đk count < k thì sẽ tính đc cả 1 giá trị ngoài k
		count = 1
		# tương tự như bước tính số lg các node trong danh sách
		while current and count < k:
			current = current.next
			count += 1
		return current

	# c) Bổ sung một nút vào sau nút thứ k
	def insert_after_kth_node(self, k, new_node):
		# Tìm node thứ k trong danh sách
		kth_node = self.find_kth_node(k)
		# Nguyên tắc khi bổ sung 1 node mới thì phải tạo 1 node mới
		if kth_node:
			new_node.next = kth_node.next
			kth_node.next = new_node


	# d) Loại bỏ nút đứng trước nút thứ k
	def remove_node_before_kth_node(self, k):
		# Nếu k = 1 hoặc k = 0 thì không có node nào trước node 
		if k > 1:
			# Duyệt tìm đến node thứ k - 1 trong danh sách
			k_minus_one_node = self.find_kth_node(k - 1)
		# Vì k_minus_one_node là node đứng trước k
		# Kiểm tra xem k có phải là node đầu tiên trong danh sách không hoặc k có phải là           node cuối cùng trong danh sách không
		if k_minus_one_node and k_minus_one_node.next:
			k_minus_one_node.next = k_minus_one_node.next.next

	#  e) Thêm con trỏ M trỏ tới một nút có trong danh sách
	#  và một danh sách liên kết đơn khác có nút đầu tiên trỏ bởi P.
	#  Hãy chèn danh sách P vào sau nút trỏ bởi M.
	def insert_list_after_m_node(self, m, other_linked_list):
		m_node = self.find_kth_node(m)

		# Kiểm tra xem m_node có nhận giá trị none hay k
		# -> câu lệnh đảm bảo node m thực sự tồn tại
		if m_node:
			last_node_of_other_list = other_linked_list.head
		while last_node_of_other_list.next:
			last_node_of_other_list = last_node_of_other_list.next
			last_node_of_other_list.next = m_node.next
			m_node.next = other_linked_list.head

	# f) Tách thành 2 danh sách mà danh sách sau trỏ bởi M (như ở câu e))
	def split_list_after_m_node(self, m):
		m_node = self.find_kth_node(m)

		if m_node:
			new_linked_list = LinkedList()
			new_linked_list.head = m_node.next
			m_node.next = None
		return new_linked_list

	# g) Đảo ngược danh sách đã cho, tức là tạo một danh sách L’ mà các nút móc nối theo        thứ tự ngược lại so với L.
	def reverse_list(self):
		prev = None
		
		current = self.head
		while current:
			next_node = current.next
			current.next = prev
			
			prev = current
			current = next_node
		self.head = prev
```



**Giả sử đường vào có 4 đầu tàu được đánh số 1, 2, 3, 4. Gọi I là phép đưa một đầu tàu vào kho sửa chữa, O là phép đưa một đầu tàu từ kho ra. Nếu ta thực hiện dãy I I O I I O O O thì thứ tự các đầu tàu lúc ra sẽ là 2 4 3 1 (kho sửa chữa có cơ cầu như một stack). Như vậy, có thể coi như ta đã làm một phép hoán vị thứ tự đầu tàu.**
**Xét trường hợp có 6 đầu tàu: 1, 2, 3, 4, 5, 6. Có thể thực hiện một dãy các phép I và O thế nào để đổi thứ tự đầu tàu ở đường ra là:**
**a) 3 2 5 6 4 1** 
**b) 1 5 4 6 2 3** 
**c) 2 4 5 3 1 6**


**Câu a:** 
Thứ tự để ra được như yêu cầu đề bài là : I I I O O I I O I O O O
**Câu b:**
Thứ tự để ra được như yêu cầu đề bài là:  I O I I I I O O I O O (ở đường vào) O (ở đường ra) I O (ở đường ra)
**Câu c:** 
Thứ tự để ra được như yêu cầu đề bài là: I I O I I O I O O O I O

**2. Hãy chuyển số thập phân 2004 sang dạng nhị phân. Minh họa tình trạng của stack được sử dụng để lưu trữ các số dư trong quá trình chuyển đổi này.**

```python
def decimal_to_binary(decimal):
  binary = ""
  while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
  return binary

print(decimal_to_binary(2004))
```


3. **Hãy chuyển các biểu thức sau sang dạng tiền tố, hậu tố:**

**a) (A + B ** C) * D/E – (F + G)** 
	**Tiền tố**        :   - * +A ** BC/DE+FG
	**Hậu tố**         :  ABC ** + DE / * FG +- 

**b) ((A + B) * D) ** (E – F)**
	**Tiền tố**         : *** + ABD - EF
	**Hậu tố**          : AB + D * EF - **


4. **Minh họa tình trạng của stack qua các bước tính giá trị của các biểu thức ở dạng hậu tố ở bài 3, ứng với A = 12, B = 7, C = 3, D = 2, E = 1, F = 5.**
	4.1 **Biểu thức hậu tố: ABC ** + DE /  * FG +- (Bổ sung thêm giá trị G = 1)**

Khởi tạo stack rỗng và điểm danh giá trị biến A = 12, B = 7, C = 3, D = 2, E = 1, F = 5, G = 1

Duyệt qua từng ký tự trong biểu thức hậu tố từ trái sang phải:

- Gặp A: Đưa giá trị A (12) vào stack: Stack: [12]
    
- Gặp B: Đưa giá trị B (7) vào stack: Stack: [12, 7]
    
- Gặp C: Đưa giá trị C (3) vào stack: Stack: [12, 7, 3]
    
- Gặp **: Lấy 2 giá trị đầu tiên trong stack (3 và 7), tính 7 ** 3 = 343 và đưa kết quả vào stack: Stack: [12, 343]
    
- Gặp +: Lấy 2 giá trị đầu tiên trong stack (343 và 12), tính 12 + 343 = 355 và đưa kết quả vào stack: Stack: [355]
    
- Gặp D: Đưa giá trị D (2) vào stack: Stack: [355, 2]
    
- Gặp E: Đưa giá trị E (1) vào stack: Stack: [355, 2, 1]
    
- Gặp /: Lấy 2 giá trị đầu tiên trong stack (1 và 2), tính 2 / 1 = 2 và đưa kết quả vào stack: Stacck [355, 2]
    
- Gặp *: Lấy 2 giá trị đầu tiên trong stack (355 và 2), tính 355 * 2 = 710 và đưa kết quả vào stack: Stack: [710]
    
- Gặp F: Đưa giá trị F (5) vào stack: Stack: [710, 5]
    
- Gặp G: Đưa giá trị G (1) vào stack: Stack: [710, 5, 1]
    
- Gặp +: Lấy 2 giá trị đầu tiên trong stack (5 và 1), tính 5 + 1 = 6 và đưa kết quả vào stack: Stack: [710, 6]
    
- Gặp -: Lấy 2 giá trị đầu tiên trong stack (710 và 6), tính 710 - 6 = 704 và đưa kết quả vào stack: Stack: [704]

Kết quả cuối cùng là giá trị còn lại trong stack, tức là 704

**Vậy, giá trị của biểu thức hậu tố là** 
ABC ** + DE / * FG +-
với A = 12, B = 7, C = 3, D = 2, E = 1 F = 5, và G = 1 là 704.


	4.2 Biểu thức hậu tố:  AB + D * EF - **

**Khởi tạo stack rỗng và điểm danh giá trị biến A = 12, B = 7, C = 3, D = 2, E = 1, F = 5**
Duyệt qua từng ký tự trong biểu thức hậu tố từ trái sang phải:

- Gặp A: Đưa giá trị A (12) vào stack: Stack: [12]
    
- Gặp B: Đưa giá trị B (7) vào stack: Stack: [12, 7]
    
- Gặp +: Lấy 2 giá trị đầu tiên trong stack (12 và 7), tính 12 + 7 = 19 và đưa kết quả vào stack: Stack: [19]
    
- Gặp D: Đưa giá trị D (2) vào stack: Stack: [19, 2]
    
- Gặp *: Lấy 2 giá trị đầu tiên trong stack (19 và 2), tính 19 * 2 = 38 và đưa kết quả vào stack: Stack: [38]
    
- Gặp E: Đưa giá trị E (1) vào stack: Stack: [38, 1]
    
- Gặp F: Đưa giá trị F (5) vào stack: Stack: [38, 1, 5]
    
- Gặp -: Lấy 2 giá trị đầu tiên trong stack (1 và 5), tính 1 - 5 = -4 và đưa kết quả vào stack: Stack: [38, - 4]
    
- Gặp **: Lấy 2 giá trị đầu tiên trong stack (38 và -4), tính 38 ** -4 = 1/2085136 và đưa kết quả vào stack: Stack: [0.0000004795850247]

Kết quả cuối cùng là giá trị còn lại trong stack, tức là 0.0000004795850247
Vậy, giá trị của biểu thức hậu tố ABC ** + DE / *FG +- với A = 12, B = 7, C = 3, D = 2, E = 1 và F = 5 là 0.0000004795850247.

**5. Trình bày thuật toán thực hiện đảo ngược một xâu ký tự (ví dụ, input là “abc” thì output là “cba”) sử dụng stack, và viết chương trình bằng ngôn ngữ Python.**

```python
def reverse_string(input_str):
	# Khởi tạo một stack rỗng
	stack = []
	
	# Duyệt qua từng ký tự trong xâu đầu vào và đưa vào stack
	for char in input_str:
		stack.append(char)
	
	# Khởi tạo một xâu rỗng để lưu kết quả
	reversed_str = ""
	
	# Lấy từng ký tự từ stack và ghép lại thành xâu mới
	while stack:
		reversed_str += stack.pop()
	return reversed_str
```


 **6. Cho một queue được lưu trữ trong bộ nhớ bởi vector Q có 6 ô nhớ, được hoạt động theo cấu trúc vòng tròn. Ban đầu queue có dạng**
![[hhaaa.jpg]]


7. **Nếu tổ chức stack theo kiểu danh sách nối đơn thì có thể duyệt stack bằng cách thăm lần lượt các phần tử của stack từ đỉnh tới đáy một cách dễ dàng. Nhưng nếu muốn duyệt theo chiều ngược lại thì người ta tổ chức stack theo kiểu danh sách nối kép (doubly linked list). Có 2 con trỏ trỏ tới đỉnh và đáy stack. Con trỏ T trỏ tới đỉnh stack đặt tại trường TOP của một nút của S, con trỏ BT trở tới đáy stack đặt tại trường BOTTOM của S như sau**


![[Pasted image 20230725224831.png]]
**Hãy trình bày giải thuật và viết chương trình bằng ngôn ngữ Python thực hiện:**
**a) Duyệt stack từ đáy lên**
**b) Bổ sung một phần tử vào stack**
**c) Loại bỏ một phần tử khỏi stack**

```python

# Định nghĩa lớp Node cho các nút của danh sách liên kết kép
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.p rev = None

# Định nghĩa lớp Stack cho stack được tổ chức theo kiểu danh sách nối kép

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
```


