Here are some common pitfalls to avoid when using `scanf` for reading input in C:

1. **Not Checking Return Value**: `scanf` returns the number of successfully read items. If it doesn't match the number of expected items, there might be an error or unexpected input. Always check the return value of `scanf`.
    
2. **Leaving Newline in Buffer**: When you use `scanf` to read a number or a word, it leaves the newline character in the input buffer. The next `scanf` will immediately read this newline character, which is often not what you want. Use `getchar()` to consume the newline character.
    
3. **Buffer Overflow**: If you use `scanf` with `%s` to read a string into a character array, make sure the array is large enough to hold the input string and the null character at the end. If the user enters a string that's too long, it can cause a buffer overflow, leading to unpredictable behavior.
    
4. **Reading Strings with Spaces**: `scanf` with `%s` **reads a string until it encounters whitespace**. If you want to read a string that contains spaces, use `fgets` instead.
```c
#include <stdio.h>

int main(){
 char d[100]; // declare d as an array of characters
 char a[100]; // declare c as an array of characters

 printf("Enter a sth: ");
 scanf("%s", &d);

 getchar(); // read the newline character (enter key

 printf("Enter a sth: ");
 fgets(a, sizeof(a), stdin); // read a string into c
 

 printf("d - %s\n", d);
 printf("a - %s\n", a); // print the string
 
 return 0;
}
```
![[Pasted image 20240102090916.png]]
> `scanf("%s", a)`  read the string untill it reach a space leaving all the other chars in the streamline. Therefor fgets() immediatly take what left in the streamline.
**Solution to input many chars with space first**
+ only use fgets()
+ use fgets() before scanf()
Conlusion:
+ Can use `scanf("%s", a);` to read each chars seperate by a space.
+ use `fgets(str, sizeof(str), stdin);` to read the whole paragraph
+ `fgets(str, sizeof(str), stdin);` read the whole line until there a line break (`\n`) while `scanf("%s", a);` read until there a space.
```c
#include <stdio.h>

int main(){
    char d[100]; // declare d as an array of characters
    char a[100]; // declare a as an array of characters

    printf("Enter a sth: ");
    fgets(d, sizeof(d), stdin); // read a string into d

    printf("Enter a sth: ");
    fgets(a, sizeof(a), stdin); // read a string into a

    printf("d - %s", d);
    printf("a - %s", a); // print the strings

    return 0;
}
```
>In this code, `fgets` reads up to 99 characters from the standard input (`stdin`) and stores them in `d` and `a`. It stops reading if it encounters a newline character (`\n`) or end-of-file. The remaining character in the array is reserved for the null character (`\0`), which marks the end of the string. This allows you to read strings that contain spaces.

5. **Not Using Address-of Operator**: When reading a value with `scanf`, you need to provide the address of the variable where you want to store the value. **Forgetting the address-of operator** (`&`) is a common mistake.


## Character arrays and pointers errors
In C, strings can be stored in two ways: as character arrays or as string literals. The difference between these two lies in where they are stored and whether they can be modified.

+ ! **Strings as Character Arrays**: When you declare a string as a character array, it gets stored in an area of memory known as the stack. This memory is writable, so you can modify the string. Here's an example:
```c
char str[] = "Hello"; // this store in stack so it can be modify
```
> In this case, `str` is an array of characters. The string "Hello" is copied into the array at initialization. You can modify this string because it's stored in the stack.

+ ! **Strings as String Literals (Compile Time Constants)**: When you declare a string as a string literal, it gets stored in a read-only part of memory (often called the data segment). This memory is not writable, so you cannot modify the string. Here's an example:
```c
char *str = "Hello";
```
> In this case, `str` is a pointer to the first character of the string. The string "Hello" is a string literal stored in read-only memory, and `str` points to it. If you try to modify this string, you'll get a segmentation fault because you're trying to write to read-only memory.
