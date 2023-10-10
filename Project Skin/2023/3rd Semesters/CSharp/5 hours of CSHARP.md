note: VS will run the previous code if the current code have bug.
> Supply & Demand (First you want to Need its. Then You will want it)
    Bí Quyết học code: Học và thực hành luôn. Thí nghiệm những code chưa hiểu sâu. Làm các Project nhỏ vs kiến thức vừa học đc. (very simple)


 ```cs
Console.WriteLine("Hey"); // no breakline
Console.WriteLine("Hello World"); // create a breakline

// prevent program stop running until pressing a key
Console.ReadKey(); 
        
```


#### Type Casting
GetType()
```cs
// constants = make the value to not able to change

const double pi = 3.14159;

Console.WriteLine(pi);


// type casting = Converting a data type
// to other data type

// convert a to int
double a = 3.14;
int b = Convert.ToInt32(a);

// get a data type
Console.WriteLine(a.GetType());

int c = 123;
double d = Convert.ToInt32(c) + 0.02;
Console.WriteLine(d.GetType());

int e = 34234;
string f = Convert.ToString(e);

string g = "$";
// char mean only 1 character
char h = Convert.ToChar(g);

String i = "true";
bool j = Convert.ToBoolean(i);


Console.WriteLine(j.GetType());
Console.WriteLine(f.GetType());
Console.WriteLine(h);
Console.WriteLine(h.GetType());


Console.ReadKey();
```

### User Input
```cs
Console.WriteLine("WHat your name bro");
string name = Console.ReadLine();

Console.WriteLine("Hello " + name);

Console.WriteLine("What your age: ");

// because ReadLine only read & write string.
// So we need to convert the output to Int
Console.WriteLine("How old are you?");
int age =  Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Your age is: " + age);
```

### Arithmetic
![[Pasted image 20230721075105.png]]


### Math Class
```cs
Math.someMathfunction()
```
![[Pasted image 20230721075605.png]]


### Random Numbers (Pseudo random numbers)
```cs
Random random = new Random();

// random between 1 and 7 range
int a1 = random.Next(0, 100);
int a2 = random.Next(0, 100);
int a3 = random.Next(0, 100);

// return numbers between 0 and 1
double b = random.NextDouble()*a1;

Console.WriteLine(a1);
Console.WriteLine(a2);
Console.WriteLine(a3);

Console.WriteLine(b);
```

**Pratice (Triangle Hypotenuse)  **
```cs
Random randomInt = new Random();
Random randomDouble = new Random();

int y = randomInt.Next(0, 100);
double x1 = randomDouble.NextDouble()*y;
double x2 = randomDouble.NextDouble() * y;


// find triangle hypotenuse c = a^2 + b^2
Console.WriteLine("Enter side A: ");
Console.WriteLine(x1);
double a = Convert.ToDouble(x1);


Console.WriteLine("Enter side B: ");
Console.WriteLine(x2);
double b = Convert.ToDouble(x2);
double hy = Math.Sqrt(a * a + b * b);

Console.WriteLine("\nThe hypotenuse of the triagle is: ");
Console.WriteLine(hy);

```

### String Method

```cs
static void Main(String[] args){
string FullName = "Major Heval1st";
string upperName = FullName.ToUpper();
string lowerName = FullName.ToLower();

string phoneNum = "123-345-4666";
phoneNum = phoneNum.Replace("-", " ");

// insert (index, string) just insert string at n index.
string userName = FullName.Insert(0, "@");

// .Length only for string
int nameLength = FullName.Length; 

// Sub String (start, end).
// Get the sub string from list_index( index a to index b )

Console.WriteLine("SubString have its own range");
Console.WriteLine("Cautions - SubString Length/Indexes are not relate to Main String Length/Idexes");

Console.WriteLine("Therefor Heval1st in FullName will have indexes from 5 to 9");

Console.WriteLine("Heval1st start from 5");
Console.WriteLine("New list [Heval1st]");
Console.WriteLine(" 'Heval1st' string length is 9");
Console.WriteLine("So that why SubString(5,9) is Heval1st");


string firstName = FullName.Substring(0, 5);
string lastName = FullName.Substring(5, 9);


Console.WriteLine("name length = " + nameLength);
Console.WriteLine(FullName);
Console.WriteLine(upperName);
Console.WriteLine(phoneNum);
Console.WriteLine("First Name: " + firstName);
Console.WriteLine("Last Name: " + lastName);
```



#### String.Format()
> Link: [String.Format Method (System) | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/system.string.format?view=net-7.0#control-spacing)
> manipulate String "{rank, space}"
```cs
int[] years = { 2013, 2014, 2015 };
int[] population = { 1025632, 1105967, 1148203 };
var sb = new System.Text.StringBuilder();
sb.Append(String.Format("{0,6} {1,15}\n\n", "Year", "Population"));
for (int index = 0; index < years.Length; index++)
	sb.Append(String.Format(
	"{0,6} {1,15:N0}\n",years[index],population[index]
	));

Console.WriteLine(sb);

// Result:
//      Year      Population
//
//      2013       1,025,632
//      2014       1,105,967
//      2015       1,148,203
```

### If Else Statement

```cs
Console.WriteLine("Pls enter your age: ");
int age = Convert.ToInt32(Console.ReadLine());
if (age < 0)
{
	Console.WriteLine("You haven't been born yet !");
}
else if (age <= 18 )
{
	Console.WriteLine("You must be 18+");
}
else
{
	Console.WriteLine("You are now Sign Up");
	Console.WriteLine("Pls enter your Name: ");
	string name = Console.ReadLine();
	if (name ==  "")
	  {
		Console.WriteLine("You Haven't enter your name");
	}                
}
```

### Switch
> Like if else, but with 1 input and optional outputs. 
```cs
Console.WriteLine("What day is today? ");
string day = Console.ReadLine();
// examine day variable
switch (day)
{
	case "Monday":
		Console.WriteLine("It's Monday");
		break;
	// output goes here by default
	// if there're no matching cases
	default:
		Console.WriteLine(day + "Is not a day");
		break;
}
```


## Logical Operator

```cs
// logical operator = use to check if more than 1 conditions is True or False
/*
    && (And)
    || (OR
*/
Console.WriteLine("What's the temp outside: (C): ");
double temp = Convert.ToDouble(Console.ReadLine());

if (temp >= 15 && temp <= 25)
{
    Console.WriteLine("It's Warm outside");
}
else if(temp < -100 || temp > 100)
{
    Console.WriteLine();
    Console.WriteLine("Still Alive Son?");
}
```


### While Loop

```cs
double temp;

Console.WriteLine("What's the temp outside: (C): ");
while (true) {
	try
	{
		temp = Convert.ToDouble(Console.ReadLine());
		break;
	}
	catch (FormatException)
	{
		Console.WriteLine("Pls enter a number");
	}

}

if (temp >= 15 && temp <= 25)
{
	Console.WriteLine("It's Warm outside");
}
else if(temp < -100 || temp > 100)
{
	Console.WriteLine();
	Console.WriteLine("Still Alive Son?");
}
```


### Nested Loop

> Triangle Algorithm
```cs
using System.Diagnostics;
using System.Linq.Expressions;
using System.Net.Sockets;
using System.Xml.Schema;

Console.Write("Total row: ");
int row = Convert.ToInt32(Console.ReadLine());

Console.Write("Total Column: ");
int column = Convert.ToInt32(Console.ReadLine());

Console.Write("Enter a symbol: ");
string input_symbol = Console.ReadLine();

// Create Triangle with for loop


// column - vertical
// Step 1: Create total column. High to Low

int chars = 0;
int indent = column;
string seperator = "#";
string symbol = input_symbol;

for (int i = row; i > 0; i--)
{
    for (int j = 0; j < indent; j++)
    {
        Console.Write(seperator);
    }
    for (int k=0;  k < chars; k++)
    {
        Console.Write(symbol);
    }
    
    if (chars > 0){
        for (int k = 0; k < chars; k++)
        {
            Console.Write(symbol);
        }
        for (int j = 0; j < indent; j++)
        {
            Console.Write(seperator);
        }
    }
    else
    {
        Console.Write(symbol);
        for (int j = 0; j < (indent-1); j++)
        {
            Console.Write(seperator);
        }
    }
    chars += 1;
    indent -= 1;
    Console.WriteLine();
}

```

> **Guessing Number** 
```cs
// Number Guessing game
static void Main(String[] args)
{
	Random random = new Random();
	int theNum = random.Next(0, 101);
	// The 80% of theNum 
	double approximateHigher = Math.Round(theNum - (theNum * 0.2));
	double approximateLower = Math.Round(theNum + (theNum * 0.2));

	bool playAgain = true;

	while (playAgain) {
		Console.WriteLine("Guess the number: ");
		int userGuess = Convert.ToInt32(Console.ReadLine());

		if (userGuess == theNum)
		{
			Console.WriteLine("Your guess is right");
			playAgain = false;
		}

		// VD:  50 > userGuess > 40
		else if (theNum > userGuess && userGuess > approximateHigher)
		{
			Console.WriteLine("A litther Higher ");
		}

		// VD: 50 < userGuess < 60
		else if (theNum < userGuess && userGuess < approximateLower)
		{
			Console.WriteLine("A litther Lower ");
		}

		else if (userGuess < theNum)
		{
			Console.WriteLine("Too Low");
		}

		else if (userGuess > theNum)
		{
			Console.WriteLine("Too High");
		}

		else
		{
			Console.WriteLine("Better Luck this time ;))");
		}
	}
}
```


> **Rock - Paper - Scissors game**
```cs
Random random = new Random();
bool play_Again = true;
string bot;
string player;
string answer;

Console.WriteLine("ROCK - PAPER - SCISSORS GAME");

while (play_Again)
{
	player = " ";
	bot = " ";
	answer = " ";

	while (player != "rock" || player != "paper" || player != "scissors")
	{
		Console.Write("Enter Rock, Paper, Scissors: ");
		player = Console.ReadLine();
		player = player.ToLower();

		// (1, 4) mean 1 to 3
		int randomNum = random.Next(1, 4);
		switch (randomNum)
		{
			case 1:
				bot = "rock";
				break;
			case 2:
				bot = "paper";
				break;
			case 3:
				bot =  "scissors";
				break;
		}
		Console.WriteLine("Player choice: " + player);
		Console.WriteLine("Bot choise : " + bot);

		switch (player)
		{
			case "rock":
				if (bot == "rock")
				{
					Console.WriteLine("It's a Draw");
				}
				else if (bot == "paper")
				{
					Console.WriteLine("It's a Lose");
				}
				else if (bot == "scissors")
				{
					Console.WriteLine("It's a Win");
				}
				break;
			
			case "paper":
				if (bot == "rock")
				{
					Console.WriteLine("It's a Win");
				}
				else if (bot == "paper")
				{
					Console.WriteLine("It's a Draw");
				}
				else if (bot == "scissors")
				{
					Console.WriteLine("It's a Lose");
				}
				break;
			
			case "scissors":
				if (bot == "rock")
				{
					Console.WriteLine("It's a Lose");
				}
				else if (bot == "paper")
				{
					Console.WriteLine("It's a Win");
				}
				else if (bot == "scissors")
				{
					Console.WriteLine("It's a Draw");
				}
				break;
		}

		Console.Write("Do you want to play again (y/n): ");
		answer = Console.ReadLine();
		answer = answer.ToLower();

		if (answer == "n")
		{
			play_Again = false;
			Console.WriteLine("Thank for playing !");
			break;
		}
	}               
}
Console.WriteLine("ROCK - PAPER - SCISSORS GAME");

```

### Array (Need a Recheck)

> **Array recheck**
```cs
int[] listItems = new int[] { 2, 4, 8 ,7, 1, 6};
int length = listItems.Length;

Random random = new Random();
int random_number = listItems[random.Next(1, length)]; 

Console.Write("Random number from Array: " + random_number);

```

**2 ways to Declare an Array**

( Khai báo dãy với tập con cho trước)
 ```cs
// declare Array with given items
String[] car = { "Lamboghini", "Tesla", "Porche"};

for (int i=0; i < cars.Length; i++)
{
	Console.WriteLine(cars[i]);
}
Console.ReadKey();
```

(Khai báo dãy với độ dài cho trước)
```cs
// array - a variable that can store multiple values. fixed size
// array cannot be empty

// declare an empty list with a given range -> string[4]
String[] cars = new string[4];

cars[0] = "VinFast";
cars[1] = "Tesla";
cars[2] = "Porche";

for (int i=0; i < cars.Length; i++
{
	Console.WriteLine(cars[i]);
}

Console.ReadKey();
```

>**foreach() method**
>Simplier & more elegant way to print an array. less flexible though.
```cs
// for each items in array >> print(items)
foreach (String car in cars)
{
	Console.WriteLine(car);
}
```

### Methods

```cs
// method - like a function. perform a set of task.  
// Let us reused code for multiple times.

sing("Gubmorning Dog", 9);       
 
static void sing(string sentence, int time)
{
	for (int i = 0; i < time; i++)
	{
		Console.WriteLine(sentence);
		Console.WriteLine();
	}
}
```

>  using **void mean not returning anything**. 
```cs
double result;

Console.Write("Enter a number: ");
double num1 = Convert.ToDouble(Console.ReadLine());

Console.Write("Enter a number: ");
double num2 = Convert.ToDouble(Console.ReadLine());

double result;

result = Remainder(num1, num2);
Console.WriteLine(result);

static double Remainder(double x, double y)
{
	return x % y;
}
```

#### Method Overloading
> Method declare as static at local class. And public at foreign class.

###### Local Overloading 
> Put Method outside Main. 
```cs
// methods share the same name but different parameter (tham số)
//                name + parameter -> signature
//                method must have a unique signature.

// Summary: If a Method have the same name but different parameter -> They're different.

static void Main(String[] args){
	double total;
	double total2;
	
	total = Multiply(2, 3);
	total2 = Multiply(2, 3, 6);
	
	Console.WriteLine(total2);
}

static double Multiply(double a, double b)
{
	return a + b;
}

static double Multiply(double a, double b, double c)
{
	return a * b + c;
}
```

#### Class to Class Overloading
```cs 
public class Area
{
    public double area(double s)
    {
        double area = s * s;
        return area;
    }

    public double area(double l, double b)
    {
        double area = l * b;
        return area;
    }

    public double area(double l, double b, double p)
    {
        double area = l * b * p;
        return area;
    }
}

class Program
{
    public static void Main(string[] args)
    {
        Area a = new Area();
        double length = 3.3;
        double breadth = 4.9;

        double rect = a.area(length, breadth, 5.5);
        Console.WriteLine("Area of rectangle " + rect);

        double side = 3.3;
        double square = a.area(side);
        Console.WriteLine(square);
    }
}
```

#### Params keyword (need review)
> Overloading but better. Use for Loop that take in various of input. Like an Array, Dictionary, etc..
```cs
static void Main(String[] args)
{
	// params = single method that can take various        parameter.  
	double total;
	double total2;

	total = Multiply(2.5, 3);
	total2 = Multiply(2, 3.33, 6);

	Console.WriteLine("The total prices are: " + total);
	Console.WriteLine("The total prices are: " + total2);
}

static double Multiply(params double[] price)
{
	double sum = 0;
	foreach (double unit in price)
	{
		sum += unit;
	}
	return sum;
}   
```

### Exception Handling
> catch bug for you.
```cs
static void Main(String[] args)
{ 
	double total = 323;
	double total2;

	// try = dangerous potential code in here.
	try
	{
		Console.WriteLine("Write double num: ");
		total2 = Convert.ToDouble(Console.ReadLine());
	}
	// catch = if buged it goes in here
	catch (Exception ex)
	{
		Console.WriteLine(ex.Message);
	}
	// finaly = always excutes regardless if the           exception is caught or not,
	finally
	{
		Console.WriteLine("hahahahahaahh");
	}

	Console.WriteLine("The total prices are: " +           total);
}
```


#### Conditional Operator 
> shorten the if else operation.
```cs
// conditional operator = used in conditional assignment if a condition is true/false

// (condition) ? x : y -> this will return a value. So assign it
double temparature = 20.434f;
string message;

// Assign value for conditional operator.
message = 
(temparature < 20) ? "Cannot go out" : "Can goes out";
Console.WriteLine(message);
```

### String Interpolation (like f'string format in python )
> Like f" {variable} string " in python

```cs
// string interpolation = allow us to insert variables
// into a string literal (chuỗi chữ)

// precede the string literal with $. 
// The placeholders are {}

String firstName = "Dinh";
String lastName = "NhatThanh";
int age = 19;

Console.WriteLine($"Hello {firstName} {lastName}");
Console.WriteLine($"You are {age} years old");

// Adding 5 Space to the strings
Console.WriteLine($"You are {age, 5} years old");
```

### Multi-Dimensional Array
> Imagine the Matrix. Its just like that 
![[Pasted image 20230723152050.png]]

```cs
// Multi-dimensional Array = an Array for Array
// Ex: (row array for column array)

//String[] ford = {"Mustang", "F-150", "Explorer" };
//String[] tesla = {"Tesla-S", "Tesla-E", "Tesla-X"};
//String[] toyota = {"Corolla", "Camry", "Rav4"};

// Now parkingLot array have row and column
// Like in matrix we access it with x and y
String[,] parkingLot = {
	{"Mustang", "F-150", "Explorer"} ,
	{"Tesla-S", "Tesla-E", "Tesla-X"},
	{"Corolla", "Camry", "Rav4"},
};

// change "Explorer" at row[0] and column[2] to "Fusion"v
parkingLot[0, 2] = "Fusion";

// Use .GetLength(int dimension_rank) to get multiple-dimension Array Length. 
// .GetLength(0) - represent the first dimension
for (int i =0; i < parkingLot.GetLength(0); i++)
{
	// .GetLength(1) - represent the second dimension
	for (int j=0; j < parkingLot.GetLength(1); j++)
	{
		Console.WriteLine(parkingLot[i, j]);
	}
}
```


## OOPs Parto


To Add Class
 > Solution Explorer -> rightClick to FileName -> Add -> Class
note: Same namespace, both class and method have public static

>*Program.cs*
>**Use method in another file**
```cs
 namespace Study
{
    class Program
    {
        static void Main(String[] args)
        {
            Message.hello();
            Console.WriteLine(Message.thanks());
        }
    }
}
```

> *messages.cs*
```cs
namespace Study
{
    // class = A bundle of related code & method
    // Can be use as an Blueprint 
    // to create Object (OOP)

    static class Message
    {
	// void because method dont return anything.
        public static void hello()
        {
            Console.WriteLine("Helllooo");
        }
        
	// string because it return string.
        public static string thanks()
        {
            return "Thanks";
        }
    }
}
```

## Practice
**> Program**
```cs

namespace Study
{
    class Program
    {
        static void Main(String[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            
            float[] l_list = new float[3];
            l_list[0] = 3.5f;
            l_list[1] = 3.5f;
            l_list[2] = -5.9f;
            
            foreach (float f in l_list)
            {
                Console.WriteLine(f);
            }
            
            string[] l_string = new string[3];
            l_string[0] = "ABC";
            l_string[1] = "xyz";
            l_string[2] = "123";
            
            foreach (string s in l_string)
            {
                Console.WriteLine(s);
            }
            string inputString;
            int aIndex = 0;
            double[] nArray = new double[20];
            nArray[3] = 34324;
            while (true)
            {
                try
                {
                
                    Console.Write("Pls enter a number: ");
                    inputString = Console.ReadLine();
                    if (inputString == "#")
                    {
                        Console.WriteLine("Stop");
                        for (int i = 0; i < nArray.Length; i++)
                        {
                            if (nArray[i] != 0)
                            {
                                Console.Write($"[{nArray[i]}] ");
                            }
                            
                        }
                        break;
                    }
                    else 
                    {
                        double doubleInput = double.Parse(inputString);
                        nArray[aIndex] = doubleInput;
                        aIndex++;
                        Console.WriteLine($"{inputString} type is :                                  {doubleInput.GetType()}");
                    }
                    
                }
                catch (FormatException e) {
                    Console.WriteLine("This is bug: " + e);
                }
            }
            string ten_hs = hocSinh.ho_ten("Dinh Nhat Thanh");
            double diemtb_hs = hocSinh.diem_trung_binh(7.8, 8.9, 7.6);
            
            Console.WriteLine($"\nHọc sinh {ten_hs} có điểm trung bình là:                                {diemtb_hs}");
        }
    }
}
```

**> hocSinh.cs**
```cs
namespace Study
{
    static class hocSinh
    {
        public static string ho_ten(string name)
        {
            return name;
        }
        public static double diem_trung_binh(double a, double b, double c)
        {
            return (a + b + c) / 3; 
        }
    }
}
```

### Constructor
> **method but have input**

```cs
class Program
{
	// constuctor = method but can assign              argument/parameter
	static void Main(string[] args)
	{
		Car car1 = new Car("Tesla", "E", 2019,                                "Red");
		car1.Drive();
	}
}

class Car
{
	string make;
	string model;
	int year;
	string color;
	
	public Car(string make, string model, int          year, string color)
	{
		this.make = make;
		this.model = model;
		this.year = year;
		this.color = color;
	}
	
	public void Drive()
	{
		Console.WriteLine($"You drive the {make}           model {model}");
	}
}
```

### ToString method
> Return a String when a Class being called in Default

```cs
Player gamer1 = new Player();
Console.WriteLine(gamer1);

class Player
{
	public String username;
	
	public Player(String username)
	{
		this.username = username;
	}
	
	// Return a String when called in               default
	public override string ToString()
	{
		return username;
	}
}
>> 
```


### Static Main
> static làm giá trị trong class thuộc về Cả Class đó chứ không riêng gì Obj. Nghĩa là là giá trị static sẽ có thuộc tính global trong Class đó. 

**> Main line of code**
```cs
// numberOCar belong to whatever obj it in
public int numberOCar;

Car car1 = new Car("Tesla", "E");
Car car2 = new Car("Ford", "Mustang");
 // numberOCar belong to each of the Obj
Console.WriteLine(car1.numberOCar);
Console.WriteLine(car2.numberOCar);


// numberOCar belong to the whole class. Every change make an influence to it.
public static int numberOCar;

Car car1 = new Car("Tesla", "E");
Car car2 = new Car("Ford", "Mustang");
// numberOCar belong to the class
Console.WriteLine(Car.numberOCar);
```

**> Without static**
```cs
class Program
{
	// static = modifier to declear a static member which belongs to the class      itself rather than to any object.
	
	static void Main(string[] args)
	{
		Car car1 = new Car("Tesla", "E");
		Car car2 = new Car("Ford", "Mustang");
		 
		// numberOCar belong to each of the Obj
		Console.WriteLine(car1.numberOCar);
		Console.WriteLine(car2.numberOCar);
	}
}

class Car
{
	string make;
	public int numberOCar;
	
	public Car(string make, string model)
	{
		this.make = make;
		numberOCar++;
	}
}   
```


**> With static**
```cs
class Program
{
	// static = modifier to declear a static member, which belongs to the class itself rather than to any object.
	
	static void Main(string[] args)
	{
		Car car1 = new Car("Tesla", "E");
		Car car2 = new Car("Ford", "Mustang");
		 
		// numberOCar belong to each of the Obj
		Console.WriteLine(Car.numberOCar);
	}
}

class Car
{
	string make;
	public static int numberOCar;
	
	public Car(string make, string model)
	{
		this.make = make;
		numberOCar++;
	}
}   
```

> Conclusion: static allow for **each method in Class to influence the static value outcome**. Without static, class's value are inependent and Belong directedly to the Object.

### Inheritance
> Reuse code from other Class

```cs
static void Main(string[] args)
{
	// inheritance = 1 or more child                   classes receiving fields, methods,                 etc..
	
	Car car = new Car();
	plane jet = new plane();
	Console.WriteLine(car.speed);
	Console.WriteLine(jet.wheels);
	car.go(200);
}

class Vehicle
{
	public int speed = 0;
	
	public void go(double speed)
	{
		Console.WriteLine($"this vehicle is                moving at {speed} km/h");
	}
	
	
	class Car : Vehicle {
		public int wheels = 4;
	}
	
	class plane : Vehicle{
		public int wheels = 20;
	}
}
```



### Abstract classes
> **Dùng khi ko muốn class được gọi vì class đó chưa hoàn tất.**
![[Pasted image 20230724153812.png]]

### Array of Objects
> Dãy của Object. Mục tiêu -> Tạo 1 Dãy chứa các Obj các loại.

**> Innitiate given array. (Can be useful or appending items)**
```cs
Car[] garage = { 
	new Car("Mustang"),
	new Car("Corvet"),
	new Car("Lamdo") 
};

for (int i = 0; i < garage.Length; i++)
{
	Console.WriteLine(garage[i].model);
}
```

**> Innitiate array with given length**
```cs
class Program
{
	static void Main(string[] args)
	{
		// Garage Array with Car as obj.
		// Translate: create a Garage for [3] Car class Obj.
		
		// Obj[] arrayName = new obj[arrayLength]
		Car[] garage = new Car[3]; 
		
		Car car1 = new Car("Mustang");
		Car car2 = new Car("Corvet");
		Car car3 = new Car("Lamdo");
		
		garage[0] = car1;
		garage[1] = car2;
		garage[2] = car3;
		
		for (int i = 0; i < garage.Length; i++)
		{
			Console.WriteLine(garage[i].model);
		}
	}
}    

class Car
{
	public string model;
	public Car(string model)
	{
		this.model = model;
	}
} 
```

> **Checkmark**
![[Pasted image 20230724155940.png]]


### Object as arguments
>  A technique that take Obj as Input By accessing its variables.
>  Ex:
```cs
class Program
{
	// no method or class allow in main
	static void Main(string[] args)
	{
		Plane mk_12 = new Plane("Boing", 1655);
		Console.WriteLine(mk_12.speed);
		ChangeSpeed(mk_12, 100);
		Console.WriteLine(mk_12.speed);
	}
	public static void ChangeSpeed(Plane daplane, int speed)
	{
		daplane.speed = speed;
	}
}

class Plane
{
	public string make;
	public int speed;
	
	// đặt giá trị của Lớp ko cần static và void vì nó ko trả       lại giá trị.
	public Plane(string make, int speed)
	{
		this.make = make;
		this.speed = speed;
	}
}
```  

**> Using Obj as argument. (Need Check Later)**   
```cs
class Program
{
	// no method or class allow in main
	static void Main(string[] args)
	{
		Plane mk_12 = new Plane("Boing", 1655);
		
		// Make mk_33 = new Plane("Boing", 1655); using method
		Plane mk_33 =  Copy(mk_12);
		
		Console.WriteLine(mk_33.make + " speed is " +                  mk_33.speed);
	}
	
	// return a Class with function.
	// Pass Obj as Argument
	public static Plane Copy(Plane plane)
	{
		return new Plane(plane.make, plane.speed);
	}
}

class Plane
{
	public string make;
	public int speed;
	
	// đặt giá trị của Lớp ko cần static và void vì nó ko trả lại giá trị.
	public Plane(string make, int speed)
	{
		this.make = make;
		this.speed = speed;
	}
}
```


### Method Overriding


```cs
class Program
{
	// no method or class allow in main
	static void Main(string[] args)
	{
		// method overriding = provides a new version of a method inherited from a parent class inherited               method must be: abstract, virtual, or already overriden Used with ToString(), polymorphism.
		
		Dog dog = new Dog();
		Cat cat = new Cat();
		
		dog.Speak();
		cat.Speak();
		
	}
}

class Animal
{
	public virtual void Speak()
	{
		Console.WriteLine("The animal goes *brrrr*");
	}
}

class Dog : Animal
{
	// Attention: only override virtual or          abstract method only.
	public override void Speak()
	{
		Console.WriteLine("ahahahhahah");
	}
}
class Cat: Animal
{
	// Attention: only override virtual or          abstract method only.
	public override void Speak()
	{
		Console.WriteLine("mewemwmemwmewme ");
	}
}
```


### MAIN LIST

> Inside " static void Main(String[] args) { } "

 **> This is an Array**
```cs
String[] food = new string[3];

// Disadvantage - Max length of 3. Cannot be more or less
food[0] = "pizza";
food[1] = "apple";
food[2] = "croissan";

foreach (string item in food)
{
	Console.WriteLine(item);
}
```

> This is an List
> List = data structure that represents a list of **Obj that can be accessed by Index**. Similar to array, but can dynamically increase or decrease in size.
```cs
List<String> fastFood= new List<String>();

fastFood.Add("HotDog");
fastFood.Add("Hamburger");
fastFood.Add("fries");
string insert_item = "Pancake";

// note: Write down the usages of these List's functions
// count the length of fastFood list
Console.WriteLine(fastFood.Count);
fastFood.Remove("fries");
fastFood.Insert(1, insert_item);

Console.WriteLine(
$"Index of {insert_item} is " + fastFood.IndexOf(insert_item));

Console.WriteLine(
$"is fastFood contain HotDog? " + fastFood.Contains("HotDog"));

foreach (string item in fastFood)
{
	Console.WriteLine(item);
}
Console.WriteLine();

// List can be easily be Sort or Reverse
fastFood.Sort();

Console.WriteLine("[Sorted List]");
foreach (string item in fastFood)
{
	Console.WriteLine(item);
}
Console.WriteLine();

Console.WriteLine("[Reverse List order]");
fastFood.Reverse();
foreach (string item in fastFood)
{
	// testing String.Format()
	Console.WriteLine(String.Format("{0, 15}", item));
}
Console.WriteLine();

// List can also be converted to Array
Console.WriteLine("This is an Array Converted form an List");
String[] fastFood_Array = fastFood.ToArray();
foreach(string f in fastFood_Array)
{
	Console.WriteLine(f);
}
```
> Idea: Using List for creating a Hotal management Databases or a food Menu.


### List of Object

#problem: How to Add function that Add a List as Input

> **List of object = a list that store Obj as variable**
```cs
class Program
{
	static void Main(string[] args)
	{
		// Ex: List<Object> = new List<Object>;
// List that can Store player Object
		List<Player> player; 
		player = new List<Player>();
		
		Player player1 = new Player("Chad");
		Player player2= new Player("Kevin");
		Player player3 = new Player("Mousey");
		
		player.Add(player1);
		player.Add(player2 );
		player.Add(player3);
		
		// Get Obj Player as p in player
		foreach (Player p in player)
		{
			Console.WriteLine(p);
		}
	}
}

class Player
{
	public String username;
	
	public Player(String username)
	{
		this.username = username;
	}
	
	// Return a String when called in default
	public override string ToString()
	{
		return username;
	}
}
```
> **Conclusion**: Tóm gọn Khai báo Class -> cho nó 1 cái tên : Vehicle vehicle1 rồi 
> + Lấy giá trị ở bên trong nó 
> + Hoặc thay thế giá trị bằng method và dùng Class như 1 input (Class class_name và biến tự do) rồi thay giá trị của Class qua biến. "class_name.make = biến tự do".


### Dictionary

```cs
Dictionary<int, string> car = new Dictionary<int, string>();

car.Add(111, "JDM1")
car.Add(222, "JDM2")
car.Add(333, "JDM3")

// extract key value pair in C#
foreach (KeyValuePair<int, string> item in car){
	Console.WriteLine($"{e.Key} {e.Value}")
}

```


### Getters & Setters

> getter & setters  = tăng bảo mật hơn bằng phương pháp Đóng gói. Coder có thể quyền kiểm soát giá trị biến trong Class của bằng get và set.  
> +   get: return biến - set đặt giá trị cho biến
> + từ khóa value - dùng để định nghĩa cho giá trị chung mà set đặt. 
```cs
class Program
{
	static void Main(string[] args)
	{
		// getters and setter = add securities to fields               by encapsulation.
		// They're accessors found within properties.
		
		// properties = combine aspects of both fields and             methods (share name with a field).
		// get accessors = used to return the property                 value.
		// set accessors = used to assign a new value.
		// value keyword = defines the value being                     assigned by the set (parameter)     
		
		Car car = new Car(479);
		Console.WriteLine(car.speed);
		
	}
}

class Car
{
	// field là giá trị khai báo
	// this is a field
	public int speed;
	public Car(int speed)
	{
		// assign Speed not field (speed) but as a                     properties Speed
		Speed = speed;
	}
	
	// this is a property (Share name with a field)
	public int Speed 
	{
		//read 
		// get use to return prop value.
		get { return Speed; } 
		// write 
		// set use to assign prop value.
		set {
			// value is like a parameter
			speed = value;
			if (speed > 500)
			{
				speed = 500; 
			}
			else
			{
				speed = value;
			}
		} 
	}
}
```


### Auto Implemented Properties
> **{get; set;}**
Not detail, but very versatile. And short. 
> (rất tiện nếu chỉ cần đặt và lấy biến giá trị)

**> Callout the Class**
```cs
  static void Main(string[] args)
{
	// Auto-Implemented properties = shortcut when no                 additional logic is required in the property.
	// You + do not have to defined a field for a property.
	//     + only have to write get; and/or set;                            inside the property.
	
	// shortcut when no logical logic in a property.
	
	Car car = new Car("Tesla");
	Console.WriteLine(car.Model);
}
```

**> without auto implemented properties**
```cs
class Car
{
	string model;
	
	public string Model
	{
		get { return model; }
		set { model = value; }
	}
	public Car(string model)
	{
		this.Model = model;
	}
}
```

**> with auto implemented properties**
```cs
public String Model {get; set;}

public Car(string model)
{
	this.Model = model;
}
```


### enums
> Like ToString() method. 
> Class holding a set of integer that will not change. Name as string and set value as integer. 
> To access it int. use (int) before calling class string.
> Ex: (int) (int)Planets.Venues -> 4


```cs
class Program
{
    static void Main(string[] args)
    {
        // enum = special "class" that cotains a set of named          integer constants.
        // Use enums when you have "values that you know               will not changes".
        
        // To get the integer value from an item 
        // You must explicitly convert to an int 
        // name = integer -> (int) name = integer
		   
        Console.WriteLine(Planets.Venues + " is a planet               number # " + (int)Planets.Venues);
        String name = PlanetRadius.Earth.ToString();
        int radius = (int) PlanetRadius.Earth;
        
        Console.WriteLine("Planet " + name + "have the radius           of " + radius);
        Console.WriteLine("Planet " + name + "volume is " +            Volume(PlanetRadius.Earth) + " km cube");
    }
    
    public static double Volume(PlanetRadius radius)
    {
        double volume = (4.0/3.0) * Math.PI * Math.Pow((int)           radius, 3); 
        return volume;
    }
}

// Kind of like ToString() method
enum Planets
{
    Mercury = 2,
    Venues = 4,
    Earth,
    Mars, Jupiter, Saturn, Uranus, Neptune, Pluto,
}

enum PlanetRadius
{
    Mercury = 2439,
    Venues = 42121,
    Earth = 2323,
}
```

 
### generic !?

> It very tiredsome to write code this way. 
> -> Duplicate methods just for different kind of input (string, int, double, etc..) 
> I wonder if there any way to shorten this process.
> God: replace method data type with this (code down here) 
```cs
int -> <Thinggy>
	public static void displayElement<Thinggy>(Thinggy[] array)
// <Thinggy> act as 
```

```cs 
class Program
{
	static void Main(string[] args)
	{
	    int[] int_array = { 2, 3, 4 };
	    double[] double_array = { 2.2, 3.2, 4.6 };
	    string[] string_array = { "2", "3", "4" };
		
	    // run through all of array items
	    displayElement(int_array);
	    displayElement(double_array);
	    displayElement(string_array);
	}
	 
	public static void displayElement(int[] array)
	{
	    foreach (int item in array)
	    {
	        Console.WriteLine(item);
	    }
	}
	
	public static void displayElement(double[] array)
	{
	    foreach (double item in array)
	    {
	        Console.WriteLine(item);
	    }
	}
	
	public static void displayElement(string[] array)
	{
	    foreach (string item in array)
	    {
	        Console.WriteLine(item);
	    }
	}
}
```


>**This when generic come in** 
```cs
static void Main(string[] args)
{
	// generic = "not specific to a particular data type"
	//           add <T> to: classes, methods, fields, etc...
	//           allows for code reusability for different                      data types.
	int[] int_array = { 2, 3, 4 };
	double[] double_array = { 2.2, 3.2, 4.6 };
	string[] string_array = { "2", "3", "4" };
	
	// array can accept infinite overloading
	displayElement(int_array);
	displayElement(double_array);
	displayElement(string_array);
}

// Change datatype to <ThisIsAName> to accept every kind of input data type. 
// In other word -> Method receive data types as parameter.
// Therefor method parameter data types just need to be call out.
public static void displayElement<Thigh>(Thigh[] array)
{
	foreach (Thigh item in array)
	{
		Console.WriteLine(item);
	}
}
```

### Multi-Thread
> Basically run Method at the same time.
> **Run Simultanuously**


**> Without Thread**
```cs
static void Main(string[] args)
{
	// thread = like thread in computer.
	// Exucute many task of the program at the same time
	
	Thread mainThread = Thread.CurrentThread;
	mainThread.Name = "Main Thread";
	
	// Call function in sequence. Whatever called first, run       first
	CountDown();
	CountUp();
	
	Console.WriteLine(mainThread.Name + "is complete !");
}
```


**> With Thread**
```cs
static void Main(string[] args)
{
	// thread = like thread in computer.
	// Exucute many task of the program at the same time
	
	Thread mainThread = Thread.CurrentThread;
	mainThread.Name = "Main Thread";
	
	Thread thread1 = new Thread(CountDown);
	Thread thread2 = new Thread(CountUp);
	
	// with Thread both of the method at the same time.
	thread1.Start();
	thread2.Start();
	
	Console.WriteLine(mainThread.Name + "is complete !");
}
```


**> The Methods**
```cs
public static void CountDown()
{
	for (int i = 10;i > 0;  i--)
	{
		Console.WriteLine("Current time: "  + i + " second");
		// add a Delay of n millisecond
		Thread.Sleep(1000);
	}
	// When the loop is over -> run this
	Console.WriteLine("Timer #1: complete!");
}
public static void CountUp()
{
	for (int i = 0; i < 10; i++)
	{
		Console.WriteLine("Current time: " + i + " second");
		// add a delay of n millisecond
		Thread.Sleep(1000); 
	}
	// When the loop is over -> run this
	Console.WriteLine("Timer #2: complete!");
}
```




### [[Tips & Trick lỏd CSharp]]

#### CheckOut & Note
## NET array - difference between "Length", "Count()" and "Rank"]

Link: [c# - .NET array - difference between "Length", "Count()" and "Rank" - Stack Overflow](https://stackoverflow.com/questions/6646449/net-array-difference-between-length-count-and-rank)

+ **Length** is the property of an array object and using it is the most effective way to determine the count of elements in the array ([Array.Length in MSDN documentation](http://msdn.microsoft.com/en-us/library/system.array.length.aspx))

+ **Count()** is a [LINQ](https://en.wikipedia.org/wiki/Language_Integrated_Query) extension method that does effectively the same. It applies to arrays because arrays are enumerable objects. It's preferred to use **Length**, because **Count()** is likely to be more expensive (see [this question](https://stackoverflow.com/q/981254/501518) for further discussion and [MSDN documentation on Count](http://msdn.microsoft.com/en-us/library/system.linq.enumerable.count.aspx) for reference)

+ **Rank** is the property that returns the number of dimensions (a different thing entirely). When you declare an array **int[,] myArray = new int[5,10];**, the **Rank** of it will be 2, but it will hold a total of 50 elements.

note: chuỗi kết nối trong SQL thêm 1  sẹt " / "

