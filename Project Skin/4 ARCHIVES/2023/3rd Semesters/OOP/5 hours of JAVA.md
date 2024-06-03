`Java Home: [Java Tutorial (w3schools.com)](https://www.w3schools.com/java/default.asp)

note tư duy: Nếu muốn Cập Nhật thì lặp lại nó nhiều lần. VD đặt 1 timer và cứ mỗi ms sẽ update trạng thái của nút 1 lần. 
# Java Type Casting (Kiểu Biến)
![[Pasted image 20230903200623.png]]
(Data Type) DT lên tự động, DT xuống làm tay
#### Widening Casting (Auto-Convert to Higher)
##### Đưa biến lên giá trị cao hơn. Chỉ cần đặt biến vào trong kiểu giá trị mới là xog. Biến đổi tự động 
==Done Automatically when passing a smaller size type to a larger size type.==
```java
public class Main {
  public static void main(String[] args) {
    int myInt = 9;
    double myDouble = myInt; // Automatic casting: int to double

    System.out.println(myInt);      // Outputs 9
    System.out.println(myDouble);   // Outputs 9.0
  }
}
```

#### Narrowing Casting (Manually Convert to Lower)
##### Đưa biến về giá trị thấp hơn bằng cách đặt (kiểu giá trị) trước biến đó
>Done Manually by placing a parentheses in front of the value.
```java
public class Main {
  public static void main(String[] args) {
    double myDouble = 9.78d;
    int myInt = (int) myDouble; // Manual casting: double to int

    System.out.println(myDouble);   // Outputs 9.78
    System.out.println(myInt);      // Outputs 9
  }
}
```


# Data Type
Data types are divided into two groups:
- Primitive data types - includes `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` and `char`
- Non-primitive data types - such as [String](https://www.w3schools.com/java/java_strings.asp), [Arrays](https://www.w3schools.com/java/java_arrays.asp) and [Classes](https://www.w3schools.com/java/java_classes.asp) 
#### Non-Primitive Data Types (Biến tham chiếu, kiểu biến không nguyên thủy)
> Non-primitive data types are called **reference types** because they refer to objects.  
> Các kiểu không nguyên thủy có thể được sử dụng để gọi các phương thức nhằm thực hiện một số thao tác nhất định, trong khi các kiểu nguyên thủy thì không thể.

The main difference between **primitive** and **non-primitive** data types are:
- Biến nguyên thủy đc chỉ định tr'c. Biến tham chiếu phải tự chỉ định (ko tính String)
- Biến Nguyên Thủy Không Gọi Được nhưng biến Tham Chiếu thì CÓ

- Biến nguyên thủy luôn có giá trị, biến tham chiếu có thể là `null`
- **Biến nguyên thủy** `viết thường`, **Biến tham chiếu** `VIẾT HOA`


+ ? What the different between Float and Double
```java
public class Main {
    public static void main(String[] args) {
        // Declaring a float
        float myFloat = 3.14f;
        System.out.println("Float value: " + myFloat); // Outputs: Float value: 3.14

        // Declaring a double
        double myDouble = 3.14;
        System.out.println("Double value: " + myDouble); // Outputs: Double value: 3.14

        // Precision difference
        float floatPrecision = 1234567.1234567f;
        double doublePrecision = 1234567.1234567;
        System.out.println("Float precision: " + floatPrecision); // May lose precision: 1234567.1
        System.out.println("Double precision: " + doublePrecision); // Higher precision: 1234567.1234567
    }
}
```


# Strings (Chuỗi phần tử)
```java
// Concatenate string (string1 + string2)
.concat()

.indexOf("a") # get the letter index of a string
```


# Reading Input
```java
Scanner scanner = new Scanner(System.in);
System.out.println("Age: ");
int age = scanner.nextInt();
System.out.println("You are " + age);
```

# Java Short Hand If...Else (Ternary Operator)
##### Viết Tắt 1 Hàm bằng kí hiệu
```java
variable = (condition) ? expressionTrue :  expressionFalse;
```


# Java Switch Statements (Dùng thay if/else vs 1 TH)
```java
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}
```

## The Do/While Loop (Làm cái này, Khi {đk} )
```java
do {
  // code block to be executed
}
while (condition);
```


# For Each Loop (Lặp với từng phần tử trong {...} )
```java
for (type variableName : arrayName) {
  // code block to be executed
}

String[] cars = {"Volvo", "BMW", "Ford"};
for (String i : cars) {
	// print i for each i in cars
  System.out.println(i); 
}
```


# Continue (bỏ qua TH hiện tại và tiếp tục )
```java
// Skip the value of 4. Go to the next iteration
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    continue;
  }
  System.out.println(i);
}
```

# Multi-Dimensional Arrays (Dãy đa chiều)
> An Array of Array (Like a table with Row & Column )
```java
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
```


# Method (Hàm, lấy tham số và cho ra kết quả)
##### static: belongs to the Main class and not the Obj itself
(**Class's Obj inherit Main class value**)
	Example: A Car_Team own 3 race cars [car1, car2, car3].  When a Car_Team class is static, each time a car win a race the Score belong to the whole car team, not the car itself.
##### Multiple methods can have the same name with different parameters
```java
int myMethod(int x)
float myMethod(float x)
double myMethod(double x, double y)
```

```java
static int plusMethodInt(int x, int y) {
  return x + y;
}

static double plusMethodDouble(double x, double y) {
  return x + y;
}

public static void main(String[] args) {
  int myNum1 = plusMethodInt(8, 5);
  double myNum2 = plusMethodDouble(4.3, 6.26);
  System.out.println("int: " + myNum1);
  System.out.println("double: " + myNum2);
}
```


# Scope
##### Area that code can be used. Local & Global for example
```java

public class Main {
  public static void main(String[] args) {
    // Code here CANNOT use x. Because x is not declared
    
    int x = 100;
    // Code here can use x
    System.out.println(x);
```


# OOP
## Constructor (Cấu trúc của Lớp)
##### It can be used to set initial values for object attributes
```java
// Create a Main class
public class Main {
  int x;  // Create a class attribute

  // Create a class constructor for the Main class
  public Main() {
    x = 5;  // Set the initial value for the class attribute x
  }

  public static void main(String[] args) {
    Main myObj = new Main(); // Create an object of class Main (This will call the constructor)
    System.out.println(myObj.x); // Print the value of x
  }
}

// Outputs 5
```


# Modifier

+ ##### public: *The class is accessible by ANY other class* 

+ ##### private: *The code only accessible within the DECLARED class* 
```java
// Data can only be access in the Main class
public class Main {
  private String fname = "John";
  private String lname = "Doe";
  private String email = "john@doe.com";
  private int age = 24;
	
	public static void main(String[] args) {
		Main myObj = new Main();
		System.out.println("Name: " + myObj.fname + " " + myObj.lname);
		System.out.println("Email: " + myObj.email);
		System.out.println("Age: " + myObj.age);
		}
}
```

+ ##### protected: *The code only accessible in the same package and SUBCLASSES*
```java
class Vehicle {
  protected String brand = "Ford";        // Vehicle attribute
  public void honk() {                    // Vehicle method
    System.out.println("Tuut, tuut!");
  }
}

class Car extends Vehicle {
  private String modelName = "Mustang";    // Car attribute
  public static void main(String[] args) {

    // Create a myCar object
    Car myCar = new Car();

    // Call the honk() method (from the Vehicle class) on the myCar object
    myCar.honk();

    // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
    System.out.println(myCar.brand + " " + myCar.modelName);
  }
}
```


+ ##### final: class that CANNOT be INHERITED by other class
	```java
	final class Exam{}
	```
	##### if try to modify final value or class. It'll cause an error
	```java
	public class Main {
	  final int x = 10;
	
	  public static void main(String[] args) {
	    Main myObj = new Main();
	    // will generate an error: cannot assign a value to a final variable
	    myObj.x = 25; 
	    System.out.println(myObj.x);
	  }
	}
	```

+ ##### abstract: The class cannot be used to create objects (To access an abstract class, it must be inherited from another class. 


## Encapsulation (Đóng gói)
##### Đóng gói các biến theo kiểu private (chủ truy cập đc ở trong lớp đó), public (có thể truy cập từ mọi nơi). 
The meaning of **Encapsulation**, is to make sure that "sensitive" data is hidden from users. To achieve this, you must:
- Declare class variables/attributes as `private`
- Provide public **get** and **set** methods to access and update the value of a `private` variable
> Example of Java's Encapsulation 
```java
public class Person {
  private String name; // private = restricted access

  // Getter
  public String getName() {
    return name;
  }

  // Setter
  public void setName(String newName) {
    this.name = newName;
  }
}

public class Main {
  public static void main(String[] args) {
    Person myObj = new Person();
    myObj.name = "John";  // error. bcs name is private. 
    System.out.println(myObj.name); // error 
  }
}
```


# Inheritance (Thừa Kế)
##### + Lớp con kế thừa method (thuộc tính) của lớp cha. 
##### + Thuộc tính protected chỉ cho phép truy cập trong phạm vi lớp con và gói (package), ko thể truy cập từ bên ngoài nên tính bảo mật vẫn cao như private.
**subclass** (child) - the class that inherits from another class
**superclass** (parent) - the class being inherited from
>To inherit from a class, use the `extends` keyword. 
```java
class Vehicle {
  protected String brand = "Ford";        // Vehicle attribute
  public void honk() {                    // Vehicle method
    System.out.println("Tuut, tuut!");
  }
}

class Car extends Vehicle {
  private String modelName = "Mustang";    // Car attribute
  public static void main(String[] args) {

    // Create a myCar object
    Car myCar = new Car();

    // Call the honk() method (from the Vehicle class) on the myCar object
    myCar.honk();

    // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
    System.out.println(myCar.brand + " " + myCar.modelName);
  }
}
```
> Use `protected` for brand in Vehicle so that sub-class can have access to it. If it was set to `private`, the Car class would not be able to access it.

# Polymorphism
##### Nhiều biến thể từ 1 Hàm. VD cùng là hàm động vật, nhưng đối tượng chó, mèo có tiếng kêu khác nhau.
```java
class Animal {
  public void animalSound() {
    System.out.println("The animal makes a sound");
  }
}

class Pig extends Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
}

class Dog extends Animal {
  public void animalSound() {
    System.out.println("The dog says: bow wow");
  }
}

class Main {
  public static void main(String[] args) {
    Animal myAnimal = new Animal();  // Create a Animal object
    Animal myPig = new Pig();  // Create a Pig object
    Animal myDog = new Dog();  // Create a Dog object
    myAnimal.animalSound();
    myPig.animalSound();
    myDog.animalSound();
  }
}
```


# Abstraction (Trừu Tượng)
##### + Abstract chỉ để khai báo Hàm trừu tượng. Các lớp con có thể dùng hàm đó để tạo ra nhiều biến thể khác nhau. ( Như khai báo bản vẽ tr'c, chi tiết để sau )
##### + Lớp trừu tượng chỉ có thể được truy cập qua lớp con.
###### VD: Lợn có hàm trừu tượng là màu sắc. Cùng 1 hàm màu sắc, nhưng 2 con Lợn có thể có 2 màu khác nhau.
> abstract class Animal {...}
> class Pig extends Animal {...}
```java
// Abstract class
abstract class Animal {
  // Abstract method (does not have a body)
  public abstract void animalSound();
  // Regular method
  public void sleep() {
    System.out.println("Zzz");
  }
}

// Subclass (inherit from Animal)
class Pig extends Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig(); // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```
> Công dụng: có thể để bảo mật thông tin của 1 hàm.

# Interface (Giao Diện)
##### Nhóm các phương thức vào 1 lớp. Dùng để nhóm các phương thức chung của các Object dưới 1 Lớp, chống việc khai báo lại 1 phương thức nhiều lần.
(United pre-declare method under 1 class.)
> interface Animal {...}
> class Pig implements Animal {...}
```java
// Interface
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void sleep(); // interface method (does not have a body)
}

// Pig "implements" the Animal interface
class Pig implements Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
  public void sleep() {
    // The body of sleep() is provided here
    System.out.println("Zzz");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();  // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```
> Công dụng: Khi muốn có các thành phần thiết yếu của 1 chiếc xe thì chỉ cần gọi. Mọi hàm trong đó đã được tạo sẵn.


# User Input
> The `Scanner` class is used to get user input, and it is found in the `java.util` package.
```java
import java.util.Scanner;  // Import the Scanner class

class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter username");

    String userName = myObj.nextLine();  // Read user input
    System.out.println("Username is: " + userName);  // Output user input
  }
}
```

# Dates
>Java does not have a built-in Date class, but we can import the `java.time` package to work with the date and time API.
+ ###### LocalDate : Represents a date (year, month, day (yyyy-MM-dd))
+ ###### LocalTime : Represents a time (hour, minute, second and nanoseconds (HH-mm-ss-ns))
+ ###### LocalDateTime : Represents both a date and a time (yyyy-MM-dd-HH-mm-ss-ns)
+ ###### DateTimeFormatter : Formatter for displaying and parsing date-time objects

> Get current Date example
```java
import java.time.LocalDate; // import the LocalDate class

public class Main {
  public static void main(String[] args) {
    LocalDate myObj = LocalDate.now(); // Create a date object
    System.out.println(myObj); // Display the current date
  }
}
```
Output: 2023-09-04
### Formatting Date and Time
> Use: 
> + **DateTimeFormatter** class
> + **ofPattern()** method
```java
import java.time.LocalDateTime; // Import the LocalDateTime class
import java.time.format.DateTimeFormatter; // Import the DateTimeFormatter class

public class Main {
  public static void main(String[] args) {
    LocalDateTime myDateObj = LocalDateTime.now();
    System.out.println("Before formatting: " + myDateObj);
    
    DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
    String formattedDate = myDateObj.format(myFormatObj);
    System.out.println("After formatting: " + formattedDate);
  }
}
```
The Output will be
	Before Formatting: 2023-09-04T14:37:46.662903  
	After Formatting: 04-09-2023 14:37:46

# ArrayList
> The `ArrayList` class is a resizable [array](https://www.w3schools.com/java/java_arrays.asp), which can be found in the `java.util` package.

Create an `ArrayList` object called **cars** that will store strings:
```java
import java.util.ArrayList; // import the ArrayList class

public class Main {
  public static void main(String[] args) {
	// Create an ArrayList object
	ArrayList<String> cars = new ArrayList<String>(); 
```
##### Add Items -> .add() 
```java

    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
  }
}
```
##### Access an Item -> .get(int)  refer to the index number
```java
	cars.get(0) // ouput Volvo
```
##### Change an Item
```java
cars.set(0, "Opel");
```
##### Remove an Item
```java
cars.remove(0); // remove Opel
```
##### Clear ( remove all the elements in the ArrayList)
```java
cars.clear();
```
##### Size
```java
cars.size();
```
##### Loop Through an ArrayList 
###### -> use get() method 
```java
  for (int i = 0; i < cars.size(); i++) {
      System.out.println(cars.get(i));
    }
```
###### -> use For-Each loop 
```java
    for (String i : cars) {
      System.out.println(i);
    }
```

##### Other Types
>  In the examples above, I created elements (objects) of type "String". (Remeber String is an Object in Java, not a primitive type).  To use other types, such as int, you must specify an equivalent [wrapper class](https://www.w3schools.com/java/java_wrapper_classes.asp): `Integer`. For other primitive types, use: `Boolean` for boolean, `Character` for char, `Double` for double, etc

##### Sort  
> Can Sort an ArrayList of Strings & Numbers:
```java
import java.util.Collections;  // Import the Collections class
// inside Main after Declare an cars ArrayList
Collections.sort(cars);  // Sort cars
```

# Linked List
Source: [Java LinkedList (w3schools.com)](https://www.w3schools.com/java/java_linkedlist.asp

> The `LinkedList` class is almost identical to the `ArrayList` (same interface)
```java
// Import the LinkedList class
import java.util.LinkedList;

public class Main {
  public static void main(String[] args) {
    LinkedList<String> cars = new LinkedList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
  }
}
```



# Note

### Biến đổi từ List lên ArrayList
```java
List<SinhVien> list_sv;
list_sv = new ArrayList<SinhVien> ();
```

