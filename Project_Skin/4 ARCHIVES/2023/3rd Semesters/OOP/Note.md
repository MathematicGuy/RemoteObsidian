
## OOPs Constructor
> Basically Function inside of Class.
> Function that modified Class contents/datas.

```java
class car {
	String make;
	String type;
	int construct_date;
	boolean available;

	// this is a Constructor, Its construct the data 
	// inside car (make, type, construct_date, available,etc..)
	public car(String make, String type, int construct_date,
	boolean available) {
            this.make = make;
            this.type = type;
            this.construct_date = construct_date;
            this.available = available;
        }
        
        public void data() {
            System.out.println(make + " " + type + 
            "from " + construct_date + " is available? " + available);
        }  
}

public class Main{
    public static void main(String[] args) {
        car new_Car = new car("Nissan", "GTA Skyline", 1998, true);
        new_Car.data();
    }
}
```

## OOPs Static Modifier
> **static** thuộc về chính lớp (**belong to the Class**) đó 
> chứ không phải đối tượng cụ thể (**not belong to object**).
> -> Ko khai biến dưới dạng obj được. Chỉ dưới dạng lớp (Class)

> Để dùng hàm chứa static mình phải gọi tên Lớp thì mới dùng đc nó.  
```java
Math math1 = new Math()
math1.round() // not work for static

// Must call the class to use .round() method 
Math.round() // work for static
```

```java
using System;

namespace MyFirstProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            // static = modifier to declare a static member, which belongs               to the class itself rather than to any specific object

            Car car1 = new Car("Mustang");
            Car car2 = new Car("Corvette");
            Car car3 = new Car("Lambo");

            // with static its goes with Car class
            Console.WriteLine(Car.numberOfCars);
	        
	        // without static its goes with object (car1, car2)
            Console.WriteLine(car1.numberOfCars);
            Console.WriteLine(car2.numberOfCars);
            
            
            Car.StartRace();

            Console.ReadKey();
        }
    }
    class Car
    {
        String model;
        public static int numberOfCars;

        public Car(String model)
        {
            this.model = model;
            numberOfCars++;
        }

		// 
        public static void StartRace()
        {
            Console.WriteLine("The race has begun!");
        }
    }
}
```