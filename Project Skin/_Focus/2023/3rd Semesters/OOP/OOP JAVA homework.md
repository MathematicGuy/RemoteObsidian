##### Bài tập nhập mảng 1 chiều, số nguyên, số thực

```java
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

public class Clara {

    private static float[] a;
    
    public static int nhapsonguyen4byte() throws UnsupportedEncodingException {
        System.setOut(new PrintStream(System.out, true, "UTF-8"));

        int value = 0;
        boolean validInput = false;
        Scanner scanner = new Scanner(System.in);

        while (!validInput) {
            try {
                value = scanner.nextInt();
                validInput = true;
            } catch (Exception e) {
                System.out.println("Giá trị nhập không hợp lệ. Vui lòng nhập lại.");
                scanner.nextLine();
            }
        }

        return value;
    }


    public static float nhapsothucfloat() throws UnsupportedEncodingException{
        float value = 0;
        boolean validInput = false;
        Scanner scanner = new Scanner(System.in);

        while (!validInput) {
            try {
                value = scanner.nextFloat();
                validInput = true;
            }
            catch (Exception e) {
                System.out.println("Giá trị nhập không hợp lệ. Vui lòng nhập lại.");
                scanner.nextLine();
            }
        }
        return value;
    }
    
    
    public static float[] nhapmang1chieufloat(float[] a)
    {
        
        a = new float[10];

        System.out.println("Giá trị của a: " + a);
        System.out.println("Giá trị của a: " + a);
        
        Scanner scanner = new Scanner(System.in);
                
        if (a == null) 
        { 
            System.out.println("nhapmang1chieufloat: Không cấp phát được bộ nhớ cho mảng"); 
            return null;
        }
        return a;
    }
    
    
    public static void main(String[] args) throws UnsupportedEncodingException {
	        System.setOut(new PrintStream(System.out, true, "UTF-8"));
        System.out.println("Giá trị của n: " + a);
        
        
        System.out.println("Nhập giá trị của n: ");
        int n = nhapsonguyen4byte();
        System.out.println("Nhập giá trị của x: ");
        float x = nhapsothucfloat();
        
        
        System.out.println("Giá trị của n: " + n);
        System.out.println("Giá trị của x: " + x);
    }
}


// public: 
// Khi khai báo một phương thức hoặc một biến là public,nghĩa là nó // có phạm vi truy cập ngoài lớp. Điều này có nghĩa là phương thức 
// hoặc biến có thể được truy cập từ bất kỳ nơi nào trong chương trình, bao gồm các lớp khác.

// static:
// Khi khai báo một phương thức hoặc một biến là static,
// nghĩa là nó thuộc về lớp chứ không phải một đối tượng cụ thể. 
// Điều này có nghĩa là chúng có thể được truy cập trực tiếp từ lớp
// mà không cần tạo một đối tượng của lớp đó.
```


#### [[HW 7 to 11]]


#### [[BT12]]
- Overloading
- Overriding
- Abstraction

[[Chapter 4 Week-6 - DSA_HW]]