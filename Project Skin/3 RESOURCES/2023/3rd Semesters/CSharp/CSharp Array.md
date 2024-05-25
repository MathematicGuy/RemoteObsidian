```cs
// index like Python. Start from 0 
string[] favourites = {
	"varys", 
	"Cersei",
	"Tyrion",
	"Bronn",
}

Console.Write(favourites[1]);
>> "Cersei"
```
![[Pasted image 20230710100320.png]]
 
  ##### Run Array with For Loop
```python
for (int i = 0;i < movies.Length;i++){
    int rank = i + 1;
    
    Console.WriteLine(rank + ". " + movies[i]);
}

>> 1. varys 
>> 2. Cersei
>> 3. Tyrion
>> 4. Bronn
```
  

```python
from array import *

#? Create an integer array with the number of elements entered by the user.

size = int(input("Enter the size of the Array: "))
my_arrays = array('i')

for i in range(size):    
    numbers = int(input("Pls enter a number for the element {}: ".format(i))) my_arrays.append(numbers)

print(my_arrays)
  
#? Inserts an element with a specified value and position into the array.
my_arrays[3] = 100 #! catch out range (IndexError), string (TypeError) error
print("\nInserts 100: {} ".format(my_arrays))
# Remove an element at the specified position from the array
my_arrays.pop(2)
print("\nRemove number at pos 2: {} ".format(my_arrays))

# Remove an element with a specified value from the array
my_arrays.remove(100)
print("\nRemove 100: {} ".format(my_arrays))

# Specifies the position of the element with the specified value in the array
for pos, num in enumerate(my_arrays):
    print(pos,'.',num)

for num in my_arrays:
    print(num)
```

## Application
#### Game Inventory
```cs
int size;

Console.WriteLine("How many slot in your inventory: ");  
// Convert ReadLine() String type to Int32 type
size = Convert.ToInt32(Console.ReadLine());

// Create a Box with n Slots
string[] game = new string[size];  

Console.WriteLine("Type in 4 Game: ");

// Assigns elements to each slot
for (int i = 0;i < size;i++){
    game[i] = Console.ReadLine();
}

Console.WriteLine("\nGame Inventory: ");
for (int i = 0;i < size;i++){
    int rank = i + 1;
    Console.WriteLine(rank +". "+ game[i]);
}
```

#### Student Printer

```cs
int size;

Console.WriteLine("How many creature are in the class: ");

size = Convert.ToInt32(Console.ReadLine());
List<string> student = new List<string>();

for (int i=0;i<size;i++){

    Console.WriteLine("Enter Student name: ");
    student.Add(Console.ReadLine());
}

Console.WriteLine("----------------");

for (int i=0;i<size;i++){
    student.Sort();
    Console.WriteLine(student[i]);
}
```


