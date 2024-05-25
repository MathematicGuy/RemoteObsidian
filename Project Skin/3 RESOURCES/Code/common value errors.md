#### Overflow
Overflow occurs when a value is computed that is outside the range of values that a type can represent.

In your code, `var` is a `short int`. In C, a `short int` is usually 16 bits, and it can represent values from -32768 to 32767. If you try to store a value outside this range in a `short int`, you get an overflow.

When an overflow occurs with signed integers, the C standard says that the result is undefined. This means that the language doesn't specify what should happen, and it can depend on the system or the compiler. However, in practice, many systems use two's complement representation for signed integers, where an overflow "wraps around".

In two's complement, if you try to store 32768 in a `short int`, it wraps around and becomes -32768. Similarly,**if you try to store -32769, it becomes 32767**. This is because in two's complement, the most significant bit is used to represent the sign of the number (0 for positive, 1 for negative), and the remaining bits represent the magnitude of the number. When an overflow occurs, the magnitude bits all become 1, and the sign bit flips.

### cannot catch out of range value
```c
int rows;
int cols;
// 2 Bytes integer
// Called a short. It can store values ranging from -32,768 to 32,767.
// In memory, a short takes up 2 bytes of
short var;

do {
  printf("Enter total rows: ");
  scanf("%d", &rows);
  if (rows < -2147483648 || rows > 2147483647){
		printf("Invalid value. Please enter a value between -2147483648 and 2147483647\n");
  };
}
while(rows < -2147483648 || rows > 2147483647);


do{
 scanf("%hd", &var);
 if (var > 32767 || var < -32768)
	  printf("Invalid value. Please enter a value between -32768 and 32767\n");
}
while(var > 32767 || var < -32768);
```
>  int cannot hold value more than 2147483647 and less than -2147483647 so checking if (rows < -2147483648 || rows > 2147483647) is useless. The same goes with short. 
>  
