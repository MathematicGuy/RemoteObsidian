
![[Pasted image 20230704151748.png]]

```cs
class Circle {
    // Hàm tính radius
    private double radius;

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    public double Perimeter(){
        return 2*Math.PI * radius;
    }
    // Kết thúc radius
    public static void main(String[] args) {
           Circle circle = new Circle();
           circle.setRadius(5.0);
           System.out.println("Radius: " + circle.getRadius());
           System.out.println("Area: " + circle.calculateArea());
           System.out.println("Perimeter: " + circle.Perimeter() + "\n");


           Circle circle2 = new Circle();
           circle.setRadius(2);
           System.out.println("Radius: " + circle.getRadius());
           System.out.println("Area: " + circle.calculateArea());
           System.out.println("Perimeter: " + circle.Perimeter());
    }
}
```


``?? Thay đổi biến private của lớp Circle thành public và truy cập trực tiếp biến radius mà không cần thông qua hàm set/getRadius để gán và hiển thị kết quả các hàm tính diện tích và chu vi của một đối tượng đường tròn`

Nếu thay **public** thành **private** thì sẽ có thông báo: Private is not allowd here, vì biến private ko thể đặt giá trị hay thay đổi.
![[Pasted image 20230704143513.png]]


`Thay đổi phạm vi các methods tính diện tích, chu vi của lớp Circle thành  private. Điều gì sẽ xảy ra?`
Không có chuyện gì xảy ra vì phạm vi tính diện tích và chu vi được gọi bên trong lớp Circle.

![[Pasted image 20230704151608.png]]