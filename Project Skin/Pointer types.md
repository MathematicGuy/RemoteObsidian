# Pointers and dynamic memory - stack vs heap

note:
+ the play button - represent where the program will start
+ the pause button - represet function that haven't run yet. 

+ Whenever a function is called it'll be added to the stack. (yes, in any way a function is called it'll be added to the stack )
+ After a function returned, it'll be remove from the stack
+ repeat 2 steps for every function inside main()
![[Pasted image 20240105100039.png]]

**UNDERSTANDING** 
+ a stack with too many function can causes stackoverflow
![[Pasted image 20240105100813.png]]
+ If I try to allocate a short next to eachother. They will be 2 bytes apart since short take up 2 bytes of memory. That mean, 4 bytes apart if I use int, 1 Bytes apart if I use char, etc...


**HEAP - Dynamic Memory Allocation**
(nothing to do with the heap data structure)
1. **malloc**: This function allocates a block of memory of the specified size and returns a pointer to the beginning of the block. The memory is not initialized, meaning it will have random values. Here's how you can use it:
```c
int *p = malloc(4 * sizeof(int)); // Allocates memory for 4 integers
```
+ If `malloc` can't allocate the requested memory, it returns `NULL`.   
+ ? When to use malloc() ? -> when I want to dynamically declare varibles size or array size  
+ In this example, I don't know how long the array will be when the user input it. So I use malloc to allocate it element's memory dynamically with n element store side by side having int as their data type.
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);
	
    // Allocate memory for 'n' elements
    arr = (int*)malloc(n * sizeof(int));
    if(arr == NULL) {
        printf("Memory allocation failed\n");
        return -1;
    }

    // Initialize the array elements
    for(i = 0; i < n; i++) {
        arr[i] = i+1;
    }

    // Print the array elements
    for(i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    // Don't forget to free the allocated memory
    free(arr);

    return 0;
}
```
> 


2. **calloc**: This function works like `malloc`, but it also initializes the allocated memory to zero. It takes two arguments: the number of elements and the size of each element. Here's how you can use it:
```c
int *p = calloc(4, sizeof(int)); // Allocates memory for 4 integers and initializes it to zero
``` 
   + Like `malloc`, `calloc` returns `NULL` if it can't allocate the requested memory.
 
3. **realloc**: This function changes the size of the memory block pointed to by a given pointer. It can either shrink or expand the memory block, and it keeps the original data. If it expands the block, the new memory is not initialized. Here's how you can use it:
```c
p = realloc(p, 8 * sizeof(int)); // Changes the size of the memory block pointed to by p to hold 8 integers   
```
+ If `realloc` can't allocate the requested memory, it returns `NULL`, and the original block is left untouched.

4. **free**: This function deallocates the memory block pointed to by a given pointer, which must have been returned by a previous call to `malloc`, `calloc`, or `realloc`. After `free` is called, that part of memory becomes available for further allocation. Here's how you can use it
```c
free(p); // Deallocates the memory previously allocated by malloc, calloc, or realloc
```


**Example**
![[Pasted image 20240105102030.png]]
+ the 1st p is allocate point p at memory address 200 (200 as example starting address) and the 2nd at memory address 400;
+ After that we pointed the value at that 2 addresses with 10 and 20.

![[Pasted image 20240112100435.png]]
The intepreter don't see `int a[]` as an array, but as an pointer `int *A`.
+ Which mean sizeof() calc size of the pointer not the entire array
+ ? The `sizeof` operator can give the size of an array in bytes, but when used on a pointer, it gives the size of the pointer, not the size of what it points to. That's why you cannot use `sizeof(A)/sizeof(A[0])` inside the function to get the size of the array. **It would give the size of the pointer `A` divided by the size of an `int`**, which is not the size of the array.

Since `*A` output 1 variable so there no way we can't calc the size of the whole array.
-> So we need to pass  array size to SumOfElements() from main 
![[Pasted image 20240112100558.png]]

