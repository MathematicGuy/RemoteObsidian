
## instance variable as Obj 
> **Trả lại 1 Biến như 1 Obj của Class**
> Mục đích: Tạo vô số Obj vs cùng 1 Class.


>Main.java
```java
public class Main{
    public static void main(String[] args){
        Logger ob1 = Logger.getInstance();
        
        ob1.log("Starting Application");
        
        Logger ob2 = Logger.getInstance();
        ob2. log("Logging from another instance");
        System.out.println(ob1==ob2);
    }   
}
```

> Logger.java
```java
public class Logger {
    // dùng instance như 1 giá trị thay thế
    private static final Logger instance = new Logger();
    
    // Vì instance là giá tị đc thay thế cho Obj Logger()
    // Khi instance đc return nó sẽ được coi là 1 Obj
    public static Logger getInstance(){
        return instance;
    }
    
    // method in từ của Obj 
    public void log(String message){
        System.out.println("LOG" + message);
    }
    
}
```

## count substring from mainstring

> if sub_str.length = 3. sub_strM = get 3 adjacent chars in main_Str, turn it into a string 
 >if (sub_StrM == sub_str) or not
```cs
string main_str = Console.ReadLine();
string sub_str = Console.ReadLine();
int sub_str_Length = sub_str.Length;

int count = 0;
int index = 0;

// loop through each index in the string
while (index < main_str.Length)
{
	 // Substring(start_index, sub_str length)
	 // this mean start from index x, scan for a string with the length of y, return sub_StrM.
	 // then Check if the sub_strM == sub_str (both in Lowercase).
	 // If Yes count+=1. Else increase the starting index from main_Str by 1
	 if (main_str.Substring(index, sub_str_Length).ToLower() == sub_str.ToLower()
	 {
		  count++;
	 }
	 index++;
}
Console.WriteLine(main_str);
Console.ReadKey();
```

