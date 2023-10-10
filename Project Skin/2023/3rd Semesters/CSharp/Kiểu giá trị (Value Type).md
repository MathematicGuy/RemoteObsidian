**Số nguyên**: **int**, **long**, **short**, **byte**.  
**Số thực**: **float**, **double**, **decimal**.
**String, Bool, Char**

Byte range :[0-255]
Kiểu Unicode Character: 16-bit
	ushort -> **số nguyên** không dấu 16-bit.
	range [-65 536 tới 65 536]

![[Pasted image 20230710095738.png]]

**Kiểu Unicode character (16 bit)**  
##### char
U +0000 tới U +ffff  
'\0'  

##### decimal  
**Kiểu thập phân (128 bit)**  
(-7.9 x 1028 tới 7.9 x 1028) / 100 to 28  
0.0M  

##### float  (hold up tp 7 digits)
**Kiểu float (32 bit)**  
-3.4 x 1038 tới + 3.4 x 1038  
0.0F  

##### double (like float but hold up to 16 digits)  
**Kiểu double (64 bit)**  
(+/-)5.0 x 10-324 tới (+/-)1.7 x 10308  
0.0D  

##### int  
**Kiểu integer (32 bit)**  
-2,147,483,648 tới 2,147,483,647  
0  

##### long  
**Kiểu signed integer (64 bit)**  
-9,223,372,036,854,775,808 tới 9,223,372,036,854,775,807  
0L  

##### sbyte  
**Kiểu signed integer (8 bit)**  
-128 tới 127  
0

##### short  
**Kiểu signed integer (16 bit)**  
-32,768 tới 32,767  
0  

##### uint  
**Kiểu unsigned integer (32 bit)**  
0 tới 4,294,967,295  
0  

##### ulong  
**Kiểu unsigned integer (64 bit)**  
0 tới 18,446,744,073,709,551,615  
0  

##### ushort  (Unassigned Integer) 
**Kiểu unsigned integer (16 bit)**  
0 tới 65,535  
0

## Simple Calculation
```cs
int number1;
int number2;

Console.Write("Enter a Decimal Number: ");

// To use Int we need to Convert it to Int thus ReadLine is String by Default 
number1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(number1);

Console.Write("Enter a Decimal Number: ");
number2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(number2);

Console.WriteLine("Average number: " + (number1 + number2)/2);
Console.ReadKey();
```
