![[Language in OOP]]


## PROCEDURAL PROGRAMMING
> Code running inside a Function()
![[Pasted image 20230704080641.png]]
 A Car: Have Properties like color and type, Method like Start(), Move() and Stop().


  
# Foundation of OOP 
> Tính chất và Nền Tảng của Hướng Đối Tượng.

### [[Encapsulation (Đóng gói)]] 
> **Encapsule Code inside Function.**
>> Giảm độ phức tạp + Khả năng sử dụng lại
##### Example of Function & Class (Encapsulation)
![[Pasted image 20230704081308.png]]

Code Example:

```cs
class Circle {
    // Method Encapsulation
    private double radius;

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

	// Method
    public double Parameter(){
        return 2*Math.PI * radius;
    }
}

public static void FileName(String[] args) {
        Circle circle = new Circle();
        circle.setRadius(5.0);
        System.out.println("Radius: " + circle.getRadius());
        System.out.println("Parameter: " + circle.Parameter());
}
```


### [[Abstraction (Trừu tượng)]]
> **Code that are Function but not show** (source code) **For ease of uses** 
> !? Think of a Wifi Router -> You just use it without thinking of what machanic inside it.
> 1 Hàm có thể sử dụng lại trong các Hàm khác. Nhưng Không thể thay đổi chức năng của hàm (vì tính chất Riêng tư) 
> *Ex: ToString() function*
```cs
public double calculateArea() {
        return Math.PI * radius * radius;
    }
```  
> Help eliminate Redundance code.
![[Pasted image 20230704081916.png]]
=> TextBox, Select, CheckBox **reused code** from HTML Element.

 
### [[Inheritance (Kế Thừa)]]

>> Ghép Nối Dễ Dàng do mọi câu lệnh đều là 1 Hàm 
>> Mỗi Hàm là 1 Chức Năng
>> -> Khả năng làm các Project lớn phức tạp đơn giản hơn.
-> Updata Hệ Thống dễ dàng. (Sắp xếp theo Hệ Thống)
=> **Loại bỏ các Lệnh thừa thãi** 

 

### [[Polymorphism (Đa Hình)]] 
+ **Poly (Many)** 
>  polygon -> many sided, polygot -> can speak many language, etc..
+ **Morph-ism**   **(Form - transform)** 
> morphology -> study of biology form, Morpheus -> Greek god of dream able to take any form, etc.. 

> **About Modifying behaviour.** 
-> Polymorphism mean **Many Form Method** .
> A technique to eliminate of/else switch statement.
> => **Giống Class trong Python**
> => **Refactor ugly switch/case statement**
Instead of this:
![[Pasted image 20230704083657.png]]
Polymorphism like this:

###### **code-1**
> **extends** (class Name) -> **Inherited function from other Class**
> Concludesion: Now Robin() can use every functions that Bird() have.
```java
class Bird {
	public void sing() {
		System.out.println("chip chep chop");
	} 
}

// inherit Bird properies and methods
class Robin extends Bird {
	// code
}


public class Polymorphism {
	public static void main(String[] args){
		Bird b = new Bird();
		b.sing();
	}
}

```

###### **test-2**
> Concludesion: Robin can now sing "Twitch twitch" on it own beside sing "chip chop chep"  by using Bird() language.
```java
class Bird {
	public void sing() {
		System.out.println("chip chep chop");
	} 
}

// inherit Bird properies and methods
class Robin extends Bird {
	public void sing(){
		System.out.println("twitch twitch")
	}
}

public class Polymorphism {
	public static void main(String[] args){
		Bird b = new Bird();
		b.sing();
	}
}

```




### Complexity

**Có 2 Chiều Hướng quyết định các Tính năng chính  **
+ **Distinct Algorithm** (Thuật toán riêng biệt)
	Từng Thuật Toán tiếp cận 1 Vấn Đề.  
+ **Disinct Object** (Đối tượng riêng biệt)

Lấy Tĩnh chế Động
	>> Đóng gói các đối tượng.

## Phạm Vi Truy Cập
> **private, protected, public**

+ **Private**: Can *only* access *inside the class*, include its sub-class.
+ **Public**: *everything* can access it.
+ **Protected**: *Imported method and property* can only *access in the same layer*.  

```java 
public  class Parent {  
    // protected int pa1;  
    protected void pf1() {  
        System.out.println("This is a protected method");  
    }  
}  
  
public  class Child extends Parent {  
    public void pf2() {  
        System.out.println("Protected Variable: " + pa1);  
        pf1();  
    }  
}  
  
public class Main {  
    public static void main(String[] args) {  
        Child child = new Child();
        child.pf2();  
    }  
}
```


> **Biến static**
> +  **Thuộc về lớp** không phải đối tượng. **Tất cả đối tượng** của lớp cùng **chia sẻ 1 biến static**.
> +  **Có thể truy cập thông qua tên lớp** maaaaaà **không cần tạo đối tượng từ lớp đó**.
> => *Class 2 có thể dùng biến Class 1 mà không cần khai biến*.  
```java
class A{  
       public static int a=10;  
       public float b=0.0;  
}  

class Main{  
   public void main(..)  
	{  
			 A ob; // **ob=null**  
			 ob = new A();  
			 ob.a=9; //ok, thâm nhâp qua đối tượng  
			 ob.b=1.0;//ok  
			 A.a=8; // ok, thâm nhập  biến **static**= tên lớp  
			 A.b=2.0; // not ok, không thâm nhập được.
	}  
}
```



## [[Inheritance]]

