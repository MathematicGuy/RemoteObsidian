## HW 7
> 
> Có một thuộc tính là color được khai báo với phạm vi truy cập_ **_protected_**_, cho phép lớp con truy cập vào thuộc tính này. Lớp cũng có một_ **_hàm tạo (constructor)_** _nhận vào tham số color để khởi tạo thuộc tính._   
Ngoài ra, lớp còn có phương thức displayColor() để hiển thị thông tin về màu sắc lên màn hình.
  
**Lớp Circle:**  
	là một lớp con của lớp Shape, kế thừa thuộc tính và phương thức từ lớp cha.  
**Bổ sung thuộc tính và phương thức:**  
>Lớp Circle có thêm một thuộc tính là radius (bán kính) và một hàm tạo khác nhận thêm tham số color và radius. Hàm tạo này gọi hàm tạo của lớp cha để khởi tạo thuộc tính color.  

> Lớp Circle cũng có một phương thức riêng là_ **_displayCircleInfo()_** để hiển thị thông tin về hình tròn gồm màu sắc và bán kính. 
  
> Trong phần chạy chương trình (hàm main), **khai báo và cấp phát** một đối tượng Circle mới với màu sắc là "**Red**" và bán kính là 5.0. Sau đó, gọi phương thức **displayCircleInfo()** để hiển thị thông tin về hình tròn lên màn hình.

```java
class Shape {
    protected String color;

    // hàm Construre nhận biến color để khởi tạo func 
    public Shape(String color) {
        this.color = color;
    }

    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

// kế thừa thuộc tính và phương thức từ Shape
// chỉ class mới extend class
class Circle extends Shape {
	// radius là float nên chọn double.
    private double radius; 

	// hàm Circle cho thêm 2 thuộc tính là color và 
	// radius
    public Circle(String color, double radius) {
        // super() accept parameter but o          nly 1
        super(color); // use it's parrent method
        
        // return input as output
        this.radius = radius; 
    }

    public void displayCircleInfo() {
        displayColor(); // cal displayColor() function
        System.out.println("Radius: " + radius); 
    }
}

public class Main {
    public static void main(String[] args) { 
	    // assign properties to a class
	    // in other word, input 
        Circle circle = new Circle("Red", 5.0); 
        // display, output
        circle.displayCircleInfo(); 
    }
}
```




## HW 8
**Override method in sub class** 
```java
class parent_Vehical {
    public void start(){
        System.out.println("The vehical starts");
    }
}

// add @Override allow sub-class method to Overide duplicate   method like start()
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


## HW 9
**Check Inheritance with For Loop and @Override**
```java
class Shape{
    public void draw(){
        System.out.println("drawing");
    }
}

class Circle extends Shape{
    @Override
    public void draw(){
            System.out.println("Drawing this Circle");
    }
}

class Mainly{
    public static void main(String[] args){
        // assign name for Shape's array with element is Shape or Circle
        Shape[] rounddy = new Shape[6]; 
        rounddy[0] = new Circle();
        rounddy[1] = new Shape();
        rounddy[4] = new Circle();
        rounddy[5] = new Circle();
        
        for (int i = 0;i < rounddy.length;i++){
            if(rounddy[i] instanceof Shape){
                rounddy[i].draw();
            }
        }
    }
}
```


## HW11
> **Viết code Java xây dựng các lớp có sự kế thừa nhau: lớp tứ giác, hình bình hành, hình chữ nhât, hình thoi, hình vuông nếu biết độ dài các cạnh và đường chéo (nếu cần thiết)
và bổ sung các hàm constructer có đối, hàm tính diện tích, chu vi của các hình.**

> **11b**. Bổ sung lớp hình thoi vào code trên.
**11c**. Bổ sung 1 hàm **tinh_dien_tich_tam_giac** loại **static** để tính diện tích của tam giác biết độ dài 3 cạnh
Gọi hàm tính diện tích tam giác **tinh_dien_tich_tam_giac** để code hàm tinh_dien_tich của lớp tư giác và lớp hình bình hành, lớp hình thoi. Gọi kiểm tra kết quả trong hàm main.
**11d**. Bổ sung các hàm tinh_chu_vi vào tất cả các lớp lớp _tứ giác, hình bình hành, hình chữ nhât, hình thoi, hình vuông_ và gọi trong hàm main để hiển thị kết quả.
**11e**. Bỏ khai báo protected của các biến của lớp tứ giác, và cung cấp 5 hàm set/get để truy cập vào các biến **private** của lớp tứ giác
**11g**. Bổ sung hàm **kiem_tra_dieu_kien_tam giac** loại **static**, kiểm tra điều kiện 3 giá trị số thực a,b,c thỏa mãn điều kiện là độ dài 3 cạnh của 1 tác giác nào đó. Gọi hàm trong các hàm **constructer** của _lớp tứ giác, lớp hình bình hành, hình thoi_. Khi các tham số độ dài cạnh không thỏa mãn, tung ra 1 ngoại lệ để báo lỗi.

```java
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.text.DecimalFormat;

class TuGiac{
    private float ab;
    private float bc;
    private float cd;
    private float da;
    private float db;
    private float ac;
    
    protected float S1;
    protected float S2;
    
        
    public float getAb(){
        return ab;
    }
    
    public void setAb(float ab){
        this.ab = ab;
    }
    
    public float getBc(){
        return bc;
    }
    
    public void setBc(float bc){
        this.bc = bc;
    }
    
    public float getCd(){
        return cd;
    }
    
    public void setCd(float cd){
        this.cd = cd;
    }
    
    public float getDa(){
        return da;
    }
    
    public void setDa(float da){
        this.da = da;
    }
    
    public float getAc(){
        return ac;
    }
    
    public void setAc(float ac){
        this.ac = ac;
    }
    
    public TuGiac(float ab, float bc, float cd, float da, float ac){
    //|ab-bc| < ac < ab+bc, |cd-da| < ac < cd + da
        kiem_tra_dk_tamgiac(ab, bc, ac);
        kiem_tra_dk_tamgiac(cd, da, ac);
    
        this.ab = ab; // 7
        this.bc = bc; // 4
        this.cd = cd; // 5
        this.da = da; // 4
        this.ac = ac; // 4.5
    };
    
    public static float tinh_dien_tich_tam_giac(float a, float b, float c)
    {
        // công thức Heron
        float s = (a + b + c) / 2;
        float area = (float) Math.sqrt(s * (s - a) * (s - b) * (s - c));
        return area;
    }
    
    public static void kiem_tra_dk_tamgiac(float a, float b, float c){
        if (Math.abs(a - b) > c || c > a +b ){
            System.out.println("Giá trị đường chéo sai/ vô lý");
        }
    }
    
    public float tinhdientich(){
        S1 = tinh_dien_tich_tam_giac(ab, bc, ac);
        S2 = tinh_dien_tich_tam_giac(cd, da, ac);
        
        return S1 +  S2;
    }
    
    public float tinhchuvi(){
        return ab + bc + cd + da;
    }
}


class hinhbinhhanh extends TuGiac{
    public hinhbinhhanh(float ab, float bc, float ac){
        super(ab, bc, ab, bc, ac);
    }
    
    public float tinh_dien_tich(){
        return super.getAb() * super.getAc();
    }
    
    public float tinhchuvi(){
        return 2 * (super.getAb() + super.getBc());
    }
    
    public static void kiem_tra_dk_tamgiac(float a, float b, float c){
        if (Math.abs(a - b) > c || c > a +b ){
            System.out.println("Giá trị đường chéo sai/ vô lý");
        }
    }
    
    public float tinhdientich_nho_tamgiac(){
        S1 = tinh_dien_tich_tam_giac(super.getAb(), super.getBc(), super.getAc());
        
        return S1*2;
    }
    
}


class hinhchunhat extends hinhbinhhanh{
    public hinhchunhat(float ab, float bc){
        super(ab, bc, (float) Math.sqrt((ab + bc)*2));
    }
    
    public float tinh_dien_tich(){
        return super.getAb() * super.getBc();
    }
    
    public float tinhchuvi(){
        return 2 * (super.getAb() + super.getBc());
    }

    public static void kiem_tra_dk_tamgiac(float a, float b, float c){
        if (Math.abs(a - b) > c || c > a +b ){
            System.out.println("Giá trị đường chéo sai/ vô lý");
        }
    }
    
    public float tinhdientich_nho_tamgiac(){
        S1 = tinh_dien_tich_tam_giac(super.getAb(), super.getBc(), (float) Math.sqrt( Math.pow(super.getAb(), 2) + Math.pow(super.getBc(), 2) ));
        
        return S1*2;
    }
}


class hinhvuong extends hinhchunhat{
    public hinhvuong(float ab){
        super(ab, ab);
    }
    
    public float tinh_dien_tich()
    {
        return super.getAb()*super.getAb();
    }
    
    public float tinhchuvi()
    {
        return (4*super.getAb());
    }
    
    public static void kiem_tra_dk_tamgiac(float a, float b, float c){
        if (Math.abs(a - b) > c || c > a +b ){
            System.out.println("Giá trị đường chéo sai/ vô lý");
        }
    }
    
    public float tinhdientich_nho_tamgiac(){
        S1 = tinh_dien_tich_tam_giac(super.getAb(), super.getAb(), (float) Math.sqrt( Math.pow(super.getAb(), 2) + Math.pow(super.getAb(), 2) ));
        
        return S1*2;
    }
}

class hinhthoi extends hinhbinhhanh{
    public hinhthoi(float ab, float bc, float ac){
        super(ab, bc, ac);
    }
    

    public float tinh_dien_tich(){
        return (float) 1/2 * (super.getBc() * super.getAc()); 
    }
    
    public float tinhchuvi()
    {
        return (4*super.getAb());
    }
    
    public static void kiem_tra_dk_tamgiac(float a, float b, float c){
        if (Math.abs(a - b) > c || c > a +b ){
            System.out.println("Giá trị đường chéo sai/ vô lý");
        }
    }
}

public class Mainly {
    public static void main(String[] args) throws UnsupportedEncodingException{
        System.setOut(new PrintStream(System.out, true, "UTF-8"));
        DecimalFormat numberFormat = new DecimalFormat("#.00");
        
        TuGiac obj_tg = new TuGiac(5, 4, 6, 3, 7);
       
        hinhbinhhanh obj_hbh = new hinhbinhhanh(13, 18, 12);
        hinhchunhat obj_hcn = new hinhchunhat(6, 3.5f);
        hinhvuong obj_vg = new hinhvuong(5);
        hinhthoi obj_thoi = new hinhthoi(8, 6, 12);
        
        System.out.println("S tứ giác là: " + numberFormat.format(obj_tg.tinhdientich()));
        System.out.println("S hình bình hành là: " + numberFormat.format(obj_hbh.tinh_dien_tich()));
        System.out.println("S hình chữ nhật là: " + numberFormat.format(obj_hcn.tinh_dien_tich()));
        System.out.println("S hình vuông là: " + numberFormat.format(obj_vg.tinh_dien_tich()));
        System.out.println("S hình thoi là: " + obj_thoi.tinh_dien_tich());
        
        System.out.println("");
        System.out.println("Tính S tứ giác nhờ S tam giác là: " + numberFormat.format(obj_tg.tinhdientich()));
        System.out.println("Tính S hình bình hành nhờ S tam giác là: " + numberFormat.format(obj_hbh.tinhdientich_nho_tamgiac()));
        System.out.println("Tính S hình chữ nhật nhờ S tam giác  là: " + numberFormat.format(obj_hcn.tinhdientich_nho_tamgiac()));
        System.out.println("Tính S vuông nhờ S tam giác là: " + numberFormat.format(obj_vg.tinhdientich_nho_tamgiac()));
        System.out.println("Công thức Heron không áp dụng được cho hình thoi");
        
        System.out.println("");
        System.out.println("Chu vi tứ giác là: " + numberFormat.format(obj_tg.tinhchuvi()));
        System.out.println("Chu vi hình bình hành là: " + numberFormat.format(obj_hbh.tinhchuvi()));
        System.out.println("Chu vi hình chữ nhật là: " + numberFormat.format(obj_hcn.tinhchuvi()));
        System.out.println("Chu vi hình vuông là: " + numberFormat.format(obj_vg.tinhchuvi()));
        System.out.println("Chu vi hình thoi là: " + numberFormat.format(obj_thoi.tinhchuvi()));
    }
}

```