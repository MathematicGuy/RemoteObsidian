
### final keyword

```java
public class Final{
    // Không thể override method final
    final public void sayHello(){
        System.out.println("Hiii");
    }

    public static void main(String[] args){
        Final f = new Final();
        f.sayHello();
    }
} 

// Không thể extends method có final keyword
public class MoreClass extends Final{
    System.out.println("This method cannot run - Error")
}
```


### Implement interface method 

>Main
```java
public class Main{
    public static void main(String[] args){
        Vehicle car = new Car("Toyota Camry", 100);
        Vehicle bike = new Bike("Honda Wave", 20);

        //overloading
        car.makeSound(); // In ra "I am a vehicle."
        car.move();// In ra "I am a vehicle."
        System.out.println(car.maxSpeed);
        car.makeSound("Woof!"); // In ra "Woof!"
        car.makeSound("Vroom!"); // In ra "Vroom!"

        
        bike.makeSound(); // In ra "I am a vehicle."
        bike.makeSound("Meow!"); // In ra "Meow!"
        bike.makeSound("Ring-ding-ding!"); // In ra "Ring-ding-ding!"
    }
}
```

> Vehicle.java
```java
interface MakeSoundable {
    public void makeSound();
}

abstract class Vehicle{
    private final String name;
    protected final int maxSpeed;
    
    public Vehicle(String name, int maxSpeed){
        this.name = name;
        this.maxSpeed = maxSpeed;
    }
    
    public abstract void move();
    public static int getSpeed(Vehicle vehicle){
        return vehicle.maxSpeed;
    }
    
    public String getName(){
        return name;
    }
    
    public void makeSound(){
        System.out.println("Iam a vehicle");
    }
    
    // overloading
    public void makeSound(String sound){
        System.out.println(sound);
    }
}

// implement Vehicle class interface method: MakeSoundable
class Car extends Vehicle implements MakeSoundable{
    public Car(String name, int maxSpeed){
        super(name, maxSpeed);
    }
    
    @Override
    public void move(){
        System.out.println("The car is moving at" + maxSpeed + "km/h");
    }
    
    @Override
    public void makeSound(){
        System.out.println("Vroom");
    }
}

final class Bike extends Vehicle implements MakeSoundable{
    public Bike(String name, int maxSpeed){
        super(name, maxSpeed);
    }
    
    @Override
    public void move() {
        System.out.println("The bike is moving at " + maxSpeed + " km/h.");
    }

    @Override
    public void makeSound() {
        System.out.println("Ring-ding-ding!");
    }
}
```


