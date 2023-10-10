### For Loop
> For Loop **(initiate value i, condition for i, action of i)**
![[Pasted image 20230703170101.png]]


```cs
for (int i = 0; i < 10; i++){
	Console.Write(i + 1);
} 
```


### Working with variable
```cs
static ushort[] nhapmang1chieusonguyen2byteskhongdau(int phantu)
{
    ushort[] a; // innitiate array
    a = new ushort[phantu]; // assign elements to array
	
    if (a == null) return null;

    for (int i = 0; i < phantu; i++)
    {
        Console.Write("array[" + i.ToString()+"]=");
        a[i] = nhapsonguyen2byteskhongdau();
    }
	
    return a;
}

static void hienthimang1chieu(ushort[] array)
{
    int sophantu = array.Length;
	
    Console.WriteLine("Straight");
    for (int i = 0; i < sophantu; i++)
    {
        Console.WriteLine("array[" + i.ToString() + "]= "
            + array[i].ToString());
    }

    Console.WriteLine("Reverse");
    for (int i = (sophantu - 1); i >= 0; i--)
    {
        Console.WriteLine("array[" + i.ToString() + "]= "
            + array[i].ToString());
    }
}

static float trungbinhcong(ushort[] a)
{
    float sum = 0.0f;
    int sophantu = a.Length;
    for (int i = 0; i < sophantu; i++)
    {   
        sum += a[i];
    }
            
    return sum/sophantu;
}

static ushort smallest(ushort[] a)
{
    ushort value = 0;
    value = a[0];
    for (int i = 0; i < a.Length; i++)
    {
        if (value < a[i])
        {
            value = a[i]; 
        }
    }
	
    return value;
}

static ushort biggest(ushort[] a)
{
    ushort value = 0;
    value = a[0];
    for (int i = 0; i < a.Length; i++)
    {
        if (value > a[i])
        {
            value = a[i];
        }
    }
	
    return value;
}
```


### While Loop

```cs
 while (conditional) {
	// code
 }
```

Application: Random number generator
```cs
// Initialize values

Random numberGen = new Random();

int roll = 0;
int attempt = 0;

while (roll != 6) {
    Console.WriteLine("Press Enter to roll the Dice !");
    Console.ReadKey();

    // Random number between a to (b-1). 0 -> 9
    roll = numberGen.Next(0,14);dd
    Console.WriteLine("A rolled: " + roll);
    
    roll = numberGen.Next(0,14);
    Console.WriteLine("B rolled: " + roll);

    attempt ++;

}
Console.WriteLine("Its took you " + attempt + " To roll a 6");
```

