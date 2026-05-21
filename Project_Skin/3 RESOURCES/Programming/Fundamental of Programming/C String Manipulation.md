#### Copy string array to another string array
```c

int main() {
    char n[128];
    char m[128];
    
    strcpy(n, inputNum()); // copy array of char from inputNum() to n
    copy n to m
    size_t destination_size = sizeof (m);
    strncpy(m, n, destination_size);
    m[destination_size - 1] = '\0'; // Null terminate m[destination_size - 1] to avoid buffer overflow
    printf("m: %s\n", m);
}
```
 

Copy string to an array
```c
#include <string.h>

char str1[100] = "Hello, ";
char str2[] = "World!";
strcat(str1, str2);
printf("%s\n", str1); // This will print "Hello, World!"
```


• strrev(): Returns the reverse of the given string
• strlwr(): Returns the lowercase string from the given string
• strupr(): Returns an uppercase string from the given string
• strstr(): Finds the substring from the first match to the last match

