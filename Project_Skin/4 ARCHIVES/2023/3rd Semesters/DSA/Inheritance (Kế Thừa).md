Intro Write-Later

-----

## Object-Oriented Relationship

![[Pasted image 20230711072433.png]]



## Inheritance
> **Extend** is a simple word for the **idea of Subclass**

Parent class -> Need to Innitiate.
Sub-Class -> just called Parent class. Can re-use all of its parent characristic. 
> **A Class can be directly derived from Only One Class** <-> Cannot have more than 1 Parent Class. ( Java is a single-inherited OOP language).
> 
> A Class that **don't have any superclass**, then it **is implicitly derived from Object class.** (được dẫn hoàn toàn từ lớp đối tượng)

+ Unlike other members, **Constructor cannot be inherited** (constructor of super class can not initialize sub-class objects.

###### `Code`
```cs
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

class Parrent {
    public void print() {
        System.out.prinln("This is da Parent class");
    }
}

class Child extends Parrent{
    public void printChild(){
        System.out.println("This is da Child class");
    }
}

class Baby extends Child{
    public void printBaby(){
        for (int i = 5;i > 0; i--){
            System.out.println("Baby count: " + i);
        }
    }       
}

public class simpleLove {
    public static void main(String[] args){
        Child new_child = new Child();
        new_child.printChild();

        Baby littleChild = new Baby();
        littleChild.printBaby();
        
        String text = "\n" + new_child.toString();
        System.out.println(text);
        System.out.println(new_child.getClass());
    } // main
}
```






## Inheritance Class Access Limitations

```cs
class Superclass {
	public void publicMethod() {
		System.out.println("This is a public method of the                    superclass");           
	}

	private void privateMethod() 
	{ 
		System.out.println("This is a private method of the"
		+ "superclass");
	
}

public class Main {
	public static void main(String[] args) {
	Superclass obj = new Superclass();
	obj.publicMethod(); // OK, accessible from superclass instance
	}
}
```

obj.privateMethod(); 
	// `Error: privateMethod() has private access in Superclass


