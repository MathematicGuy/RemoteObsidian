
## Single inherit

Khai báo a, hàm của b
-> hàm của b không truy cập đc bằng a

VD:
```java
A ob1;
ob1 = new A();

// khai báo A, hàm của B -> A ko truy cập đc
A ob2;
ob2 - new B();

// Phải ép kiểu thì ms truy cập đc. ínstanceof() -> (True/False) kiểm tra đối tượng animal có phải 1 hàm của lớp khác hay ko.
 ```


```java
class A  
{  
  public int f();  
}  

// ép kiểu B với A
class B extends A{  
    public int f()  
    {  
           // **Viết lại hàm f của lớp super**  
     }  
}

A ob;
ob = new b(); // -> ép kiểu (khai báo biến của A nhưng ép kiểu thành biến của b)
ob.f() // ưu tiên gọi hàm của b). Khi lớp A hoặc B có cùng hàm thì sẽ ko bị lỗi mà sẽ gọi hàm của lớp B.
```

