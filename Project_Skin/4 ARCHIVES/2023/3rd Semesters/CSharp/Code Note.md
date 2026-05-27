#### [[MessageBox]]

#### Vietnamese in Console
```cs
Console.OutputEncoding = System.Text.Encoding.UTF8
```


#### Math in Code
![[Pasted image 20230704112520.png]]


#### While Error -> try catch 
```cs
class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.WriteLine("Nhập số phần tử trong mảng: ");
        int n = 0;
        while (true)
        {
            // Không lỗi nên rơi vào try 
            try
            {
                n = Convert.ToInt32(Console.ReadLine());
                break;
            }
            catch (Exception e)
            {
                Console.WriteLine("Nhập lại do: " + e.ToString());
            }

        }


        ushort[] numbers = new ushort[n];

        for (int i = 0; i < n; i++)
        {
        while (true)
            {
                Console.WriteLine("Nhập số thứ " + (i + 1) + ": ");
                try
                {
                    numbers[i] = Convert.ToUInt16(Console.ReadLine());
                    break;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Nhập lại do " + e.ToString());
                }
            }
        }

        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            sum += numbers[i];
        }

        Console.WriteLine("Tổng các số trong mảng là: " + sum);
    }
}
```




#### Running Class from other file

`Declaration`
```cs
using System;

namespace HelloWorld
{
    public class Declaration
    {
        public void Show()
        {
            Console.WriteLine("I'm a simple Class");
        }
    }	
}
```


`Program.cs`
```cs
using HelloWorld;
using System.ComponentModel.DataAnnotations;
using System.Runtime.InteropServices;

class Program
{
	// input_value can only be used inside the              function
	public program(input_value1, input_value2){
		// code
	}
    static void Main(string[] args)
    {
	    // assign name for class
        Declaration ob = new Declaration(); 
        ob.Show(); // activate function in 
    }
}
```






**Format** 
```java
Console.WriteLine("What is your name?");
var name = Console.ReadLine();
var currentDate = DateTime.Now;

Console.WriteLine($"{Environment.NewLine}Hello, {name}, on {currentDate:d} at {currentDate:t}!");
Console.Write($"{Environment.NewLine}Press any key to exit...");

Console.ReadKey(true);
```

### [[Export to Excel CSharp]]