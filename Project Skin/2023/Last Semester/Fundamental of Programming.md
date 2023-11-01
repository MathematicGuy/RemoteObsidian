### [[C Code Note]]

### C

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
 