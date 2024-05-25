> note: The reason why we use `list.Count` instead of `list.Length` is because `Length` is a **property of arrays** while `Count` is a **property of collections**.


```cs
List<string> shoppingList = new List<string>();

shoppingList.Add("Dream");
shoppingList.Add("Magic");
shoppingList.Add("Unicorn");
shoppingList.Add("Dragon");

for (int i = 0; i < shoppingList.Count, i++){
	Console.WriteLine(shoppingList[i]);
} 
``` 


#### Remove Element in List
```cs
shoppingList.Remove("Dream");
shoppingList.RemoveAt(1);

Console.WriteLine("-------------");

>> ------------- 
>> Magic
>> Dragon
```

## Application
> Student Name Sort in Alphabets.
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