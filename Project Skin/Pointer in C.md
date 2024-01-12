## Dereferencing pointer (con trỏ hội thảo) 
+ ? Dereferencing a pointer means getting the value that is stored in the memory location pointed by the pointer. The dereference operator `*` is used to do this in C.
	+  `*p = 99;` - Here, `p` is a pointer to `x`. `*p` dereferences the pointer, meaning it accesses the value stored at the memory location `p` is pointing to (which is `x`). So `*p = 99;` changes the value of `x` to 99.
 
	+ `**r` - Here, `r` is a pointer to a pointer `p`. So `*r` would give you the pointer `p`, and `**r` dereferences `p` to give you the value that `p` is pointing to (which is `x`). So `**r` gives you the value of `x`.
    
	+ `***h` - Here, `h` is a pointer to a pointer to a pointer. So `*h` gives you `r`, `**h` gives you `p`, and `***h` gives you the value that `p` is pointing to (which is `x`). So `***h` gives you the value of `x`.
	
+ !  Remember, **each** `*` **in front of a pointer variable in C is a level of dereferencing**, accessing the value that the pointer (or chain of pointers) points to.
(dereference -> lấy giá trị ở địa chỉ của con trỏ)

## referencing pointer (con trỏ tham chiếu)
+ ? a reference to a pointer is essentially another pointer that points to an existing pointer. This is often called a "pointer to a pointer".
	+ `int *p = &x;` - Here, `p` is a pointer that holds the address of `x`, so `p` is a reference to `x`.
    
	+ `int **r = &p;` - Here, `r` is a pointer that holds the address of `p`, so `r` is a reference to `p`, or a pointer to a pointer. When you dereference `r` once with `*r`, you get `p`. When you dereference `r` twice with `**r`, you get the value that `p` points to, which is `x`.
    
	+ `int ***h =&r;` - Here, `h` is a pointer that holds the address of `r`, so `h` is a reference to `r`, or a pointer to a pointer to a pointer. When you dereference `h` once with `*h`, you get `r`. When you dereference `h` twice with `**h`, you get `p`. When you dereference `h` three times with `***h`, you get the value that `p` points to, which is `x`
	  
+ ! In each case, the variable on the left side of the `=` is a reference to the variable on the right side of the `&`. The `&` operator is used to get the address of a variable, and the `*` operator is used to declare a pointer and to dereference a pointer. The number of `*`s indicates the level of indirection or the "depth" of the reference.
(reference -> 1 con trỏ trỏ tới trỏ khác)
a -> b (a reference b)

float, int - 4 bytes
short - 2 bytes

![[Pasted image 20240110175703.png]]

Changing value of a with pointer p
![[Pasted image 20240110180516.png]]
p = &a mean pointer p hold the address of a
> * p = 20  will also change the value of a with the address remain the same


Reason to have more than 1 type of pointer:
(Pointer type, void pointer, pointer arithmetic)
> for Dereference and to access and modify value.

p -> pointer
&p -> pointer address 
and * p -> pointer value

value with the same name (a) with difference memory address
![[Pasted image 20240112084641.png]]
![[Pasted image 20240112084811.png]]
+ what happened?  
 ![[Pasted image 20240112085139.png]]
> When a function is called, it goes into a stack frame. Therefor it memory address is also difference from the one in main. 

![[Pasted image 20240112085807.png]]
when a argument get passed to the function. Increment(a) mean the value a will be copied to the variable x or in other word: int x = a
+ pointer as function argument: if the **argument is * p instead of x**
	 with the same principle but with **&a as input** we get `int *p = &a`
Using this, result at a address will be 11. (no need to return value in function)

Pointer to Array
![[Pasted image 20240112092927.png]]

## Character arrays and pointers
![[Pasted image 20240112102626.png]]
+ ! The last variable of the string is null (n**ull use as end-of-the-array identifier** to **prevent the pointer to read all char on the array and return garbage value for unidentify momory block**. Ex: 5, 6, 7 is unidentify memory block)
The actual size of the String always 1 more than its total size, **bc the last element is null**
+ that why JOHN take 4 char but C total char is 5.
![[Pasted image 20240112103350.png]]
+ c2 can = to c1 because c2 is a pointer, but c1 cannot = to c2 bc it is an array thus c1 = c2 is Invalid.
+ `c[2] = *(c + 2) = l` and `c[0] = *c = H`
+ if `c[0] = *c = A` then c1 array will be "Aello"
+ ! The pointer c2 is not copying the `c1[]` array. But taking it 1st memory address `200` . So to access all of the array element I just need to point the pointer to each of c1 element. `c[n]`  with max n as the length of the array 



+ ! Array always be view as a pointer in a function argument.

> Printf each char of C array until reach the null variable. 
```c
while(C[i] != '\0'){
	// code
}
```

```c
char C[20] = "Hello" // string gets stored in the space for array
char *C = "Hello"; // string gets store as compile time constant (String literal)  
C[0] = "A"; // this make the program crash
print(C);
```
+ `char *C = "Hello";`   this in Read-Only Memory. So cannot be modify, else the program will crash 


### [[Pointer types]]


## Pointers and multi-dimensional arrays
+ ? (D as Dimension)
+ ? MA as memory address
1 D Array 
![[Pasted image 20240112120750.png]]

2D Array
![[Pasted image 20240112200833.png]]
+ ! remember array alway start from 0. 
`B[2][3]` is see as two 1D array. With the first array as `B[0]` and the second as `B[1]` 
+ ! Therefor `int p* = B;` will not return `B[2][3]` but just `B[0]` since the pointer always pointed to the 1st memory address of the array.
+ ? Each int take 4 bytes. So 1 array take 12 bytes. Thus if B[0] MA is 400 -> B[1]  MA will be 412
+ !  `int (p*)[3] = B;`  will return `B[2][3]`