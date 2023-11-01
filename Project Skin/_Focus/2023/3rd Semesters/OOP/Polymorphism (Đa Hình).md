==Đa hình là 1 dạng nhưng có nhiều kiểu==  


*( mã nguồn )*
+ **Overloading:** Cho phép có nhiều method cùng tên khác kiểu trong 1 hàm.
> **public int num(){}** and **public float num(){}**
- Cùng **1 Phương Pháp. Có nhiều cách nó chính là Overloadding.** 
> VD: Tính diện tích tam giác: (**1 phương pháp tính S, 2 cách tính khác nhau**)
> + S tam giac: 1/2 (a * h) 
> + S tam giac heron: căn(p*(p-a)*p(p-b)*p(p-c))


( *chạy mới biết* )
+ **Overriding**: lớp con ghi đề code của lớp mẹ. Lớp con ghi đè code  khi kế thừa 1 lớp.
> VD: lớp con và lớp cha có chung 1 method -> lớp con dùng Override nên.
```java
class parent_Vehical {
    public void start(){
        System.out.println("The vehical starts");
    }
}

// add @Override allow sub-class method to Overide duplicate method like start()
class child_Car extends parent_Vehical{
    @Override
    public void start() {
        System.err.println("The vehical starts with a key");
    }
}

public class Mainly{
    public static void main(String[]  args){
        System.out.println("Example of @Override annotation");
        
        parent_Vehical lambo = new child_Car();
        lambo.start();
    }
}
```

+ **Abtraction principle**
>code: 
 + **extends**
	 + **abstract** 
> Giúp tạo nên lớp chung. Kết nối, gán 2 lớp, lớp con kế thừa lớp cha.
> - Giúp che chi tiết không cần thiết.
```java

abstract class Shape {
 public abstract void draw(); // Abstract method
 public void displayInfo() {System.out.println("This is a shape.");}
}
class Circle extends Shape {
 @Override
 public void draw() {System.out.println("Drawing a circle.");}
}

```

