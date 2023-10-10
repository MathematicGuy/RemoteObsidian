
## Constructer

```java
package testing;

class Circle {
    // radius default value
    public Circle(){
        radius = 0;
    }
    
    // radius using constructor -> can take external input value 
    public Circle(double r){
        radius = r;
    }

    private double radius;

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    private double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    private double Perimeter(){
        return 2*Math.PI * radius;
    }
    // Kết thúc radius
    public static void main(String[] args) {
        Circle circle1 = new Circle();
        // Initiate new Circle() function
        Circle circle2 = new Circle(30);
        
        // set radius value
        circle1.setRadius(5.0);
        // present circle1.getRadius() value in r1 & r2
        double r1 = circle1.getRadius();
        double r2 = circle2.getRadius();
        
        System.out.println("Radius of circle1: " + r1); // result: 0.0
        System.out.println("Radius of circle2: " + r2); // result: 30.0

    }
}


```


