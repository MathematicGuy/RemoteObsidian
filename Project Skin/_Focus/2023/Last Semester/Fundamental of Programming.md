### [[C Code Note]]

### [[C Fundamental]]

Why Learn C? It the mother of languages
	It the fundamental, writer for major of programming language, tools and kernel like: SQL, Linux, Python intepeter, UNIX, etc...  
> Also inspiring the syntaxs for JS, Java, C++, C, c#, php, perl 

Runtime Dependent -> Need specific compiler for each OS system

[How to Set up Visual Studio Code for C and C++ Programming](https://www.youtube.com/watch?v=9VE7p-he4fA)

[Pointers in C / C++](https://www.youtube.com/@freecodecamp)

Note:
	return 1 -> failure 
	return 0 -> success
+ Doesn't support OOPs features
	Math functions (math.h library)
	fmod() -> returns the remainder of dividing two numbers


Data types
+ Array Type
+ Structure Type
	CHAR
	INT
	+ Unsigned
		+ unsigned char - 1 byte - 0 > 255
		+ unsigned - 1 byte - 0 > 65535
		+ unsigned long - 4 byte - 0 > 4294967295
	+ Signed
		![[Pasted image 20231101131811.png]]
	+ Real Nuber
		+ FLOAT (%f)
		+ DOUBLE (%lf) -> Higher Precision.
	SHORT/LONG
+ Pointer Type 
+ Bool, logical expression 
+ Char type
	most common char: ([ASCII Chart – CommFront](https://www.commfront.com/pages/ascii-chart))

### C Variable

**Output variable**
	To output variables in C, you must get familiar with something called "format specifiers".
> For example, to output the value of an `int` variable, you must use the format specifier `%d` or `%i` surrounded by double quotes, inside the `printf()` function:
```c
int myNum = 15;  
printf("%d", myNum);  // Outputs 15
```
> To print other types, use `%c` for `char` and `%f` for `float`:

![[Pasted image 20231101141639.png]]
and -> 1 when a and b are the same. 
	0 + 0 = 1,
	1 + 1 = 1,
	1 + 0 = 0 and 0 + 1 = 0
```c
int main() {
    int result;
    int num1 = 12; // binary: 1100
    int num2 = 6;  // binary: 0110
    result = num1 & num2;
    // binary: 0100 (decimal: 4)
    printf("Value after Data Type Conversion: %d\n", result);
    return 0;
}
```

**Bit manipulation operators**
> ShiftRight
```c
int main() {
    int num = 10; // binary: 1010
    int shiftAmount = 1;
	
    int result = num << shiftAmount; // result: 1010 << 0 (Add 0 to the right of binary num)
     // result: 10100
    printf("Value %d after 1-bit shift is: %d\n", num, result); 
    return 0;
}
```

gán bit vào bên phải
```c
void main(){
    int m;
    char st[32];
    printf("Enter a Integer: ");
    scanf("%d", &m);

    // Lấy biểu diễn nhị phân của m
    itoa(m, st, 2);
    printf("\n Binary of (%d)=%s", m, st);

    // Gán bit thứ 5 từ bên phải của m bằng 1. Nếu 0 thì đổi thành 1, ko thì giữ nguyên.
    m |= 16; // mask = 16
    // lấy biểu diễn nhị phân của m sau khi gán bit số 5 bằng 1
    itoa(m, st, 2);
    printf("\n  Binary = %s", st);
    getch();

}
```

Expections (Ngoại lệ) - cause a program to crash, limited or lead to unexpected results.
	1 số ngoại lệ ko thể có thông báo. 
```c
try() {}
catch(){}
```

