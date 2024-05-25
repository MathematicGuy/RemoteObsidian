#### **Compiler Errors**
Programming Languages have rules

Syntax errors - something wrong with the structure
+ Missing semicolon (int x = 5)
+ printf("l am here);
> Error like missing semi colin ; or dismiss a coding rule

Semantic Errors - something wrong with the meaning 
+ a + b; // when it doesn't make sense to add a and b
> Sth wrong about the logic. 

#### **Compiler Warnings** (still Run but errors vulnerble)
+ Do NOT Ignore them
+ There an Issue with your code that could lead to a potential problem.
Ex: 
```c
int total;
printf("Total is %d\n", total);
```
> total hasn't been initialize

**Linker Errors** (can be tricky to fix)
+ Linkers have trouble linking all the object files into an executable code.
+ Likly there is a library or object file that is missing.
	Misisng library from a third party.
![[Pasted image 20231115135231.png]]
x is missing its library. 


**Runtime Errors**
+ Errors that occur when the program is executing
+ Some typical runtime errors
	+ Divide by zero
	+ File not found
	+ Out of memory	
ntoe: seen more when we work with file

**Logic Errors**
+ Errors or bugs in your code that cause your program to run incorrectly
+ Logic errors are mistakes made by the programmer
Suppose you want to be a pilot
But (You Blind) -> logic errors


