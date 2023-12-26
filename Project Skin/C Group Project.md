**Sản phẩm nộp**: 
+ Báo cáo bằng Word + Code+ Clip.
+ Báo cáo bằng word có từ 5-10 trang. 
+ Trang bìa làm bằng Canva report template, bên trong sơ đồ vẽ bằng Figma. Clip quay demo chương trình sinh viên chạy.

---
**Đề tài 7. Danh sách liên kết và quản lý bộ nhớ trong C.**
(Linked Lsit and Memory management)
> Remember, understanding pointers and memory allocation is crucial in C. T


Quản lý bộ nhớ: cung cấp đủ bộ nhớ và dọn bộ nhớ sau khi sử dụng.

Code documentation
```c
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
```
+ `struct Node* newNode`: This declares a pointer variable named `newNode` of type `struct Node*`, which means it is a pointer to a structure of type `Node`. This structure likely represents a node in a linked list.

+ `malloc(sizeof(struct Node))`: This is a function call to `malloc`, which stands for "memory allocation". It dynamically allocates memory on the heap for the size of the structure `Node`. The `sizeof` operator is used to determine the size of the structure in bytes.

+ `(struct Node*)`: The return value of `malloc` is a void pointer (`void*`), so it needs to be cast to the appropriate pointer type, which is `struct Node*` in this case. This allows the allocated memory to be treated as a `Node` structure.