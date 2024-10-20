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
+ Pointer as function argument: if the **argument is * p instead of x**
	 with the same principle but with **&a as input** we get `int *p = &a`
	 ![[Pasted image 20240114085354.png]]
Using this, result at a address will be 11. (no need to return value in function)
+ ! Take notice that a is not a pointer. So what the function doing is p pointer pointed to a address. Like scanf("%d", &a), p is modifying the value at &a.
+ ! Applied the same principle, if we want to modify `*p` pointer when calling `Increment(&p)` the argument would be `void Increment(int **p)`

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
+ ! Caution:  `int *p[3] = B;` **is not**     `int (*p)[3] = B;` 
	+ Because `p[3] = *(p + 3) thus *p[3] would be *(p + 3)[3] -> third element of the third array pointer pointed to` This would cause an error if that element isn't exist.  
	+  `int *(p)[3] = B;` mean select the 3rd element of the 1st array p pointed to. Simple as that

`B[2][3]` is see as two 1D array. With the first array as `B[0]` and the second as `B[1]` 
+ ! Therefor `int p* = B;` will not return `B[2][3]` but just `B[0]` since the pointer always pointed to the 1st memory address of the array.
+ ? Each int take 4 bytes. So 1 B's array take 12 bytes. Thus if B[0] MA is 400 -> B[1]  MA will be 412 
+ !  `int (p*)[3] = B;`  will return `B[2][3]`

![[Pasted image 20240113074136.png]]
Having `B[0]` acted as the entire 1D array, we can access it variable like normal like this:
`B[0][n] as n are the element position in the array: 1,2,3 `
so `*(*p + 0)` will be 2, `*(*p + 1)` will be 3 and `*(*(p+1) + 0)` will be 4 



+ ! Row ist represent as a integer pointer but column are represent as an integer
	 In the context of a dynamically allocated 2D array in C, the rows are represented as pointers to integers (`int *`), and the columns are represented as integers (`int`).
	
	 When you allocate memory for the 2D array, you first allocate memory for the rows with `malloc(rows * sizeof(int *))`. This creates an array of `rows` number of pointers to integers. Each of these pointers will then point to an array of integers, which will be the columns of the 2D array.
	
	 Then, for each row, you allocate memory for the columns with `malloc(cols * sizeof(int))`. This creates an array of `cols` number of integers.
	
	 So, in the end, `arr` is a pointer to a pointer to an integer (`int **`). The first level of indirection (the first `*`) is used for the rows of the array, and the second level of indirection (the second `*`) is used for the columns. You can access the elements of the 2D array with `arr[i][j]`, where `i` is the row index and `j` is the column index.
	
	 However, there's a problem with your code. You're declaring `arr` as a variable-length array (VLA) pointer with `int (*arr)[cols];`, but then you're trying to use it as a dynamically allocated 2D array. These are two different ways to create a 2D array, and they're not compatible with each other. You should remove the line `int (*arr)[cols];` and the following lines related to `B`, as they're not needed for a dynamically allocated 2D array.


#### 3D Array
we have the construction of 2D array
![[Pasted image 20240115085714.png]]
So it pretty easy to imagine out 3D array 
![[Pasted image 20240115085906.png]]
For easy understanding: 2D array are still normal: `C[0][0]`
+ But the 1st element of the array for 3D array will be: `C[0][0][0]`
+ Applied this principle fpr every elements in the arary, we'll have the 2nd element of the 1st array ist: `C[0][0][1]` .
+ ! For the 3D array, the first block `C[0]` (represent the 3D and each array), the 2nd block `c[0][0]` the first 2 element inside the 1st array, the 3 block represent the element inside that 2D array.
+ ! Yes the 3D array wrap the 2D array (2D array sit inside the 3D array)
+ ! `int C[3][2][2]` mean declare an 3D array, with 3 array containing another 2 sub-array with each sub-array container 2 elements. (Basically like a container in HTML)![[Pasted image 20240115091649.png]]
=> The first block `[]` represent 3D array for n block. the other 2 block `[][]` still present as 2D array like normal.

As for 2D arary we have `(*p)[n]`**(pointer to array of n integer)** if we want to represent with pointer , in 3D array we can write it like this: still the pointer replace the 1st block.
![[Pasted image 20240115090618.png]]
Then applied the same principle, for the additional block we just use 2D array + k (k as the total array)
and add * from the outside to get it value.
![[Pasted image 20240115090821.png]]

![[Pasted image 20240115091115.png]]
![[Pasted image 20240115091105.png]]
for `*(c[0][1] + 1)` we have 4, for `*(c[1][0] + 1)` we have 6

**3D array as a Function**
+ ! remember: what don't be written or declare will be consider as 0. Ex ; `A[2] = A[2][0][0]`
![[Pasted image 20240115092244.png]]
+ ! Conclusion: n-D array is just n array wrap inside n array. 

### Pointer Errors
Dangling pointer (con trỏ bị treo - xảy ra khi cố dùng con trỏ đã xóa  rồi hoặc ko tồn tại.
> happend when an undeclare pointer pointed to a value 
Ex: declare * ptr then delete * ptr, and then pointed * ptr to a value -> Dangling pointer


