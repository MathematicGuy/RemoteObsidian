#### Array 
+ (Độ dài số phần tử tối đa ko thay đổi)

#### List:
+ Có thể lấy 1 phần tử ngay Lập tức. (Nằm rải rác)
+ Điểm Yếu: Chậm.

#### Array List:


#### Hash Table:
> Các phần tử đc lưu vào trong các bộ nhớ liền kề nhau. -> CÓ thể truy cập cực nhanh.

#### Maps:

> Dùng HashMap có thể lấy giá trị của Sophia ngay lập tưc
```java
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Iterator;

public class Main {

    public static void main(String[] args) throws UnsupportedEncodingException {
        System.setOut(new PrintStream(System.out, true, "UTF-8"));

        // Create a new HashMap
        HashMap<String, Integer> ageMap;
        ageMap = new HashMap<>();
        
        // Add key-value pairs to the HashMap
        ageMap.put("John", 25);
        ageMap.put("Emily", 29);
        ageMap.put("Michael", 22);
        ageMap.put("Sophia", 28);
        
        // Access and print the value for a specific key
        System.out.println ("John's age: " + ageMap.get ("John"));
        
        // Check if a key exists in the HashMap
        if (ageMap.containsKey ("Sophia"))
          System.out.println ("Sophia's age: " + ageMap.get ("Sophia"));
        else
          System.out.println ("Sophia's age not found.");
    }        
}
```


#### Iterator
> Duyệt từng phần tử.


```java
import java.util.ArrayList; 
import java.util.Iterator;
```

##### main iterator
> Interator có thể kết hợp vs Array, List, Linked List, HashSet, etc... 
```java
public class Main {
	public static void main(String[] args) {
		ArrayList<String> names;
		names= new ArrayList<>();
		names.add("Alice");
		names.add("Bob");
		names.add("Charlie");
		
		Iterator<String> iterator = names.iterator();
		while (iterator.hasNext()) {
			String name = iterator.next();
			System.out.println(name);
	}
}
```
> 		Alice
> 		Bob
> 		Charlie


##### Iterator with List

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;
public class Main {
    public static void main(String[] args) {
        // Create a list of strings
        List<String> list = new ArrayList<>();
        list.add("Hello");
        list.add("World");
        // Create an iterator for the list
        Iterator<String> iterator = list.iterator();
        // Iterate over the list
        while (iterator.hasNext()) {
            // Get the next element
            String element = iterator.next();
            // Print the element
            System.out.println(element);
        }
    }
}
```
##### Iterator with Hash Table
```java
import java.util.Hashtable;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        
        // Create a hashtable
        Hashtable<String, Integer> hashtable = new Hashtable<>();
        
        // Add some key-value pairs to the hashtable
        hashtable.put("Nguyen", 11);
		hashtable.put("Minh", 14);
        hashtable.put("Huy", 12);
       
		// Create an iterator for the hashtable
        Iterator<String> iterator = hashtable.keySet().iterator();
        
        // Iterate over the hashtable
        while (iterator.hasNext()) {
        
			// Get the next key
            String key = iterator.next();
            
            // Get the value for the key
            Integer value = hashtable.get(key);
            
            // Print the key and value
            System.out.println("Key: " + key + ", Value: " + value);
        }
    }
}
```
>Key: Huy, Value: 12
>Key: Minh, Value: 14
>Key: Nguyen, Value: 11
##### Iterator with Hash Map

```java
import java.util.HashMap;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {

		// Create a HashMap
        HashMap<String, String> map = new HashMap<>();
        
		// Add some key-value pairs to the HashMap
        map.put("Dan", "Nail");
        map.put("Pink", "Black");
        map.put("Hai", "Ly");
        
        // Create an iterator for the HashMap
        Iterator<String> iterator = map.keySet().iterator();
        
        // Iterate over the HashMap
        while (iterator.hasNext()) {
        
			// Get the next key
            String key = iterator.next();
            
            // Get the value for the key
            String value = map.get(key);
            
            // Print the key and value
            System.out.println("Key: " + key + ", Value: " + value);
        
        }
    }
}
```
>Key: Dan, Value: Nail
>Key: Hai, Value: Ly
>Key: Pink, Value: Black