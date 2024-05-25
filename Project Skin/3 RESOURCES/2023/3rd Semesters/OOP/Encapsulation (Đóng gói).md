##### Đóng gói vào trong 1 CLASS.
```python
// Cho phép a được dùng ở mọi nơi.
def f1():
	global a
	a = 1
def f2():
	print('a = ', a)
```


Nói tới Method -> Class nào 
+ Function: hàm trả lại 1 giá trị.
+ Method: phương pháp, hàm của Class. (Tính che giấu dữ liệu)
> Class = Data (Fields/Properties) + Methods
>-> Dữ liệu của Class đc giấu khỏi bên ngoài.
>-> Tất cả các hành vi chỉ nên được truy cập thông qua các phương thức.
>-> Method, chỉ quan tâm đến mục đích để gọi.

Class & Object
> (Class & Student)
> Ex: Student include: Code, Name, Year of Birth, Address.
![[Pasted image 20230704074009.png]]

Source: [OOP (Java-C++-Python-C#) (google.com)](https://classroom.google.com/c/NjA5Mjc4ODk1Nzkw)
Từ Khóa: Encapsulation, Circle trong Java.
>Tính **Che Giấu** được thể hiện qua **Private**.
```cs
public class Circle {
    private double radius;  
  
    public double getRadius() {  
        return radius;  
    }  
  
    public void setRadius(double radius) {  
        this.radius = radius;  
    }  
  
    public double calculateArea() {  
        return Math.PI * radius * radius;  
    }   
}
```

