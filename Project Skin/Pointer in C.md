### [[Pointer types]]

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