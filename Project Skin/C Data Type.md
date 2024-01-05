
1. Integer types
```c
int a = 10; // integer
short b = 5; // short integer
long c = 1000L; // long integer
long long d = 5000LL; // long long integer
unsigned int e = 20; // unsigned integer
```

2. Floating-point types
```c
float f = 5.75f; // single-precision floating point
double g = 20.123456; // double-precision floating point
long double h = 30.123456789012345L; // extended-precision floating point
```

3. Character types
```c
char i = 'A'; // character
unsigned char j = 'B'; // unsigned character
signed char k = 'C'; // signed character
```

4. Void type
```c
void function(void); // function with no return value and no parameters
```

5. Pointer types
```c
int l = 10;
int *m = &l; // pointer to an integer (). *m mean pointer pointed to | &l mean the memory address of l => m pointer pointed to l memory address
```
+ `*`: When used in a declaration, the asterisk (`*`) is the **dereference operator** (toán tử quy chiếu). It specifies that `m` is **not just a regular integer variable, but a pointer to an integer.** When used in an expression, `*` is used to dereference a pointer, i.e., to access the value that the pointer points to.
+ - `&`: This is the **address-of** operator. It returns the memory address of its operand. In this case, `&l` gives the memory address where the integer `l` is stored.
+ if  value at &m (* m) changes then value at &l (* l) also changes and revert. 
**misunderstood/misconception**
+ if * p = &slice but &p != & slices because p have it own memory address, * p just stored the value in &slice. 

5. Array types
**Important Note:** The last character of the array ist /0 (null)
```c
int n[5] = {1, 2, 3, 4, 5}; // array of integers. 
```
> The maximum characters this array can take is 5. If you input more than that, it will cause overflow and output nonsense stuffs.

7. Structure types
```c
struct person {
    char name[50];
    int age;
}; // structure type
```

8. Union types
```c
union data {
    int o;
    float p;
    char q;
}; // union type
```

9. Enumeration types
```c
enum week {Mon, Tue, Wed, Thu, Fri, Sat, Sun}; // enumeration type
```

10. Function types
```c
int function(void); // function type
```