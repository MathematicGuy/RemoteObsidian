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
 
