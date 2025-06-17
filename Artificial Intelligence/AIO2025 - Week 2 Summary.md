Khi khai báo giá trị của 1 biến X, biến X đó chỉ hoạt động như 1 con trỏ hướng tới Object chứa giá trị của biến X -> Lý do mọi biến trong python đều là Object.

![[Pasted image 20250616155558.png]]

*Giải thích cơ chế hoạt động của hàm swap*, cách `a, b = b, a` hoạt động. 
Do giá trị thực của 1 biến được lưu vào Object ở trong Heap. Khi 2 biến hoán đổi giá trị (re-binding) **thực chất là chúng liên kết lại con trỏ tới Object của đối tượng kia,** nghĩa *Trỏ a liên kết tới Object b từng trỏ tới, còn b thì trỏ lại tới Object ban đầu của a.* 

Vậy nên **thực chất giá trị của x và y không thay đổi,** chỉ là tên của 2 giá trị đc gán lại vào object thoi. 
![[Pasted image 20250616160249.png]]
Các tầng của biến
+ **Local:** Biến trong hàm hiện tại.
+ **Enclosing:** Biến trong hàm bao ngoài hàm hiện tại (closure) 
+ **Global:** Biến trong Module (file)
+ **Built-in:** biến được tạo tr'c của python (print, len, range, count, etc..)

Khi thực thi chương trình các NameSpace đều được coi là 1 dictionary, trong đó:
Tên hàm hay biến là key và giá trị Object mà nó chỉ tới là value. Lưu ý, mọi tên trong namespace kể cả tên hàm cũng đc coi là tên biến. 
```python
globals () = {
	’ swap ’: < function swap at 0 x ... > ,
	’ v1 ’: 2 ,
	’ v2 ’: 3 
}
```
+ ? Nói cách khác, khi thực thi chương trình ở mỗi tầng, python có thể xác định đc các biến hiện có qua NameSpace. Ví dụ như global() ở trên.
+ $ NameSpace là 1 cư xử như 1 dictionary, dùng để liên kết giữa tên biến là key `(swap, v1, v2)` và Object là value `(function đc trỏ tới, 2, 3)` trong 1 phạm vi cụ thể (scope có thể là global, enclosing, local, built-in). 


Khi gọi biến **Python gọi theo thứ tự: Local -> Enclosing -> Global -> Built Int** (nghĩa là *mỗi khi quét, tên biến không được tìm thấy trong namespace trong tầng hiện tại, python sẽ di chuyển tới tầng tiếp theo*) Nên khi hoán đổi giá trị các tầng của biến hoạt động như sau: 
![[Pasted image 20250616161246.png| 450]]
Trước Khi Swap, hàm `swap()` đc gọi -> Tiến vào trong hàm swap, các con trỏ thay đổi liên kết tới Object của nhau (e.g. v1-> 3, v2 -> 2) -> Trả về giá trị v1, v2 và Thoát khỏi hàm `swap()`. 

**Stackframe** là **bộ nhớ tạm thời** (cache) đc **tạo ra để lưu dữ liệu mỗi khi hàm đc gọi.**
	Các *key và value* trong namespace ở 1 hàm sẽ *bị xóa khỏi callstack bởi pop()* sau khi việc thực thi *Hàm kết thúc.*
	Nếu còn biến tham chiếu nào còn trỏ tới Object trong Stackframe thì sẽ đc đánh dấu để loại bỏ bởi *Garbage Collector*. 

---
Tubple - immutable
+ Can set as dictionary key because it immutable. 
**Set (work exactly like set in math)**
![[Python-Set-Operatioons.webp| 300]]
- each value is unique, every value is unorganized (ko có thứ tự)
-> Có thể dùng để lọc các phần tử trùng lặp sử dụng set.
```python
fruit = [(1, "apple"), (2, "banana"), (3, "apple")]
unique_fruit = set([item[1] for item in fruit])
print(unique_fruit) # {'banana', 'apple'}
```

+ ! Don't update a set using String because String will be read as list of letter. 
```python
mem = {"Linh", "Tung", "HJa"}
mem.update(['Phuong'])
print(mem) # {'g', 'HJa', 'o', 'Tung', 'u', 'n', 'Linh', 'P', 'h'}
```



Dictionary:
+ key: must be immutable.
+ value: any value








