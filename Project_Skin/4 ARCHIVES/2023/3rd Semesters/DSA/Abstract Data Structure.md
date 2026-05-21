
	Tốc đọ Giải Thuật <-> Độ Trừu Tượng Thuật Toán

#### Data Type
> Ex: String, Interger, Float, Bool

#### Abstrac Data Type
> Special kind of Data Type

**Some operation of Stack
+ **isFull()**        : kiểm tra Danh sách đã đầy hay chưa.
+ **isEmpty()**   : Ktra có trống không. 
+ **push(x)**       : Đẩy X vào Stack.
+ **pop()**           : Lấy giá trị đầu tiên trong ngăn xếp. 
+ **peek()**         : Lấy giá trị đầu tiên (trên cùng) của Stack
+ **size()**           : Trả lại độ lớn của Stack

| Operation         |                   Stack                    |             Queue              |           List            |
| ----------------- |:------------------------------------------:|:------------------------------:|:-------------------------:|
| **isFull()**      |     Kiểm tra Danh sách đã đầy hay chưa     |             -same-             |          -same-           |
| **isEmpty**       |            Ktra có trống không.            |             -same-             |          -same-           |
| **push(x)**       |              Đẩy x vào Stack.              |               x                |             x             |
| **pop()**         |    Lấy giá trị đầu tiên trong ngăn xếp.    |               x                |             x             |
| **peek()**        | Lấy giá trị đầu tiên (trên cùng) của Stack |               x                |             x             |
| **size()**        | Lấy giá trị đầu tiên (trên cùng) của Stack | Tổng số lượng giá trị sau cùng |             x             |
| **remove()**      |                     x                      |               x                | Loại bỏ 1 phần tử trong x |
| **get(i)**        |                     x                      |               x                |  Lấy phần tử ở vị trí x   |
| **replace(x, y)**   |                     x                      |               x                | Thay thế giá trị x với y  |
| **insert(x)**     |          Thêm X ở phía sau Queue           |               x                |             x             |
| **delete()**      |                     x                      |   delete xóa phần tử ở cuối    |             x             |

+ Insert -> Pointer
> Khi thêm phần tử hàng đợi thì thêm ở Đầu. Còn lấy thì ở Đuôi.

