**Format Specifier**
- `%d` or `%i`: Integer
- `%f`: Floating point number
- `%lf`: Double
- `%c`: Character
- `%s`: String (an array of characters. Example: char[100])
- `%p`: Pointer
- `%u`: Unsigned integer
- `%x` or `%X`: Unsigned hexadecimal integer
- `%o`: Unsigned octal integer
- `%%`: A literal '%' character

### [[common value errors]]

### [[C Data Type]]

### [[C String Manipulation]]

## [[C Exam]]

### [[C File Handling]]

**scanf**
```c
int main(){
	int number;
	printf("Enter a number: ");
	scanf("%d", &number); //take %digit as an input
	printf("You enter number: %d\n", number);
	
	return 0;
}
```
> Double input example 
```c
int main(){
    char celebrityF[20]; 
    char celebrityL[20];
    scanf("%s%s", celebrityF, celebrityL); // double input
    
    printf("I love %s %s\n", celebrityF, celebrityL);
	
    return 0;
}
```


**Input Stream** or buffer ( !important ) 
![[Pasted image 20240102082022.png]]
> The `scanf` function reads input until it encounters a whitespace character (like a space, tab, or newline). When you enter a number and press Enter, `scanf` reads the number but leaves the newline character in the input buffer.
notice: all number are numeric value and the rest are all  characters
	meaning any unidentify value such as a space, empty line except numbers is a character.
```c
int d;
int b;
char c;
// this work just fine
scanf("%d", &d);
scanf("%d", &b); // take a number like normal
```
![[Pasted image 20240102084141.png]]

```c
// but this is not
scanf("%d", &d);
scanf("%c", &c); // this will take the left over line (an empty line) as char
```
> This output 34 straight away even thought I justr input 1.
In your code, when you use `scanf` to **read an integer,** **it leaves a newline character in the input buffer.** Then, when you use `scanf` again to read a character, it **immediately reads that leftover newline **character instead of waiting for you to enter a new character.
![[Pasted image 20240102083954.png]]
Solution
```c
// but this is not
scanf("%d", &d);
getchar(); // get the empty line
scanf("%c", &c); // this will take ln (an empty line) as char
```

#### [[common errors when using scanf]]

**Atoi**
> Convert number in string format to int number 
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char str[] = "1234";
    int num = atoi(str);
    printf("The string \"%s\" is converted to the integer %d.\n", str, num);
    return 0;
}
```


**Itoa**
> `itoa()` is a function in C that converts an integer value to a string of character using (DECIMAL or HEX form)
```c
#include <stdio.h>
#include <stdlib.h>

#define DECIMAL 10 // use base-10 (0 to 9)
#define HEX 88 // use base-16 that use 16 digits (0-9 and A-F)


int main() {
    int num = 10;
    char buffer[10];
    itoa(num, buffer, DECIMAL);
    printf("The decimal number %d is converted to the string %s.\n", num, buffer);

    itoa(num, buffer, HEX);
    printf("The decimal number %d is converted to the hexadecimal string %s.\n", num, buffer);
    return 0;
}
```

decimalToBinary()
```c
void decimalToBinary(int n){
    int store[1000]; // store binary chars. static so it won't be destroyed after the functon call
    int i = 0;
        
    // Step1: Convert num to binary
    while (n > 0)
    {
        i++; // result i = 5. But store[0] leave empty
        int binaryN = n % 2;
        n /= 2;

        store[i] = binaryN;
        // caution - if put i++ at the end i will be 1 more than the actual number of digits. result in i = 6;        
    }

    printf("Binary:\n");
    // print store array in reverse to get the binary format
    //? why value at pos 6 is trash value ?
    for (int j = i; j > 0 ; j--){
        printf("%d - %d\n", j, store[j]);
    }
}
```

**sprintf**
> `sprintf` is a function in the C programming language that formats and stores a series of characters and values in a string
> int sprintf(char * str, const char * format, any_string);
> + **value** is save into **buffer** pointer 
```c
#include <stdio.h>

int main() {
    char buffer[100];
    int value = 42;
    sprintf(buffer, "The value is %d.", value);
    printf("%s\n", buffer);
    return 0;
}
```


## **Array**

```c
int number[] = {1,2,3,4,5,6,7,8};
number[2] = 200;
printf("You enter number: %d\n", number[2]);

return 0;
```

**Loop through Array manually**
```c
for (int i = 0; i <  sizeof(prices)/sizeof(prices[0]); i++){
    printf("\n$%.2lf", prices[i]);
}
```
**Loop through Array using function**
```c
#include <stdio.h>

//? "int size" is explicitly passed to the function,
//? representing the size of the array 
int arrayLength(double array[], int size){
    //? return size of the pointer not size of the array
    //! int length = size/sizeof(array[0]);
    
    int length = size/sizeof(array[0]);
    return length; 
}

int main(){
    double prices[] = {5.0, 10.0, 15.0, 25.0, 20.0};
    
    printf("Size of %d bytes", sizeof(prices));
    printf("\nSize of 1 bytes %d", sizeof(prices[0]));
    
    
    int length = arrayLength(prices, sizeof(prices));
    
    printf("\nList of prices:");
    for (int i = 0; i < length; i++){
        printf("\n$%.2lf", prices[i]);
    }
    return 0;
}
```




**Function**
```c
int main(){
    printf("Top\n");
    cal();
    printf("Bottom\n");
    
	return 0;
}

void cal(){
	int number[] = {1,2,3,4,5,6,7,8};
	number[2] = 200;
	printf("You enter number: %d\n", number[2]);
}
```


**Function Input**
```c
int num;

printf("Enter a num: ");
scanf("%d", &num);
cal(num);
```

> 2 ways to Active a function. The first is to declare it before-hand 
```c
double cube(double num){
    double result = num * num * num;
    return result;
} 

int main(){
	printf("Float: %f ",cube(2));
	return 0;
}
```
> Second is to make a protoype of it. And Complete it later
```c
double cube(double num);

int main(){   
	printf("Float: %f ",cube(2)); // output: 8
	return 0; 
}

double cube(double num){
    double result = num * num * num;
    return result;
} 
```


**If Statement**
```c
#include <stdio.h>
int max(int a, int b, int c){
    int result;
    if (a > b && a >c){
        result = a;
    }   
    else if (b > a && b > c){
        result = b;
    }
    else{
        result = c;
    }
    
    return result;
}

int main(){
    printf("Max num: %d", max(8, 10, 2));
    return 0;
}
```

switch statement
```c
#include <stdio.h>

int main() {
    char grade = 'F';

    switch (grade) {
        case 'A': 
            printf("pass");
            break;
        case 'B':
            printf("You did alright"); 
            break;
        default:
            printf("How yall doing"); 
            break;
    }   
    return 0;
}
```

Basic class struture
```c
#include <stdio.h>
#include <stdlib.h>

struct Student {
    char name[20];
    char major[20];
    int age;
    double gpa;
};

int main() {
    
    struct Student student1;
    student1.age = 22;
    student1.gpa = 3.2;
    strcpy(student1.name, "Harry Po'er");
    strcpy(student1.major, "Neuron Science");
    printf("%s\n", student1.major);   


    struct Student student2;
    student2.age = 18;
    student2.gpa = 4.2;
    strcpy(student2.name, "Meth");
    strcpy(student2.major, "Art & History");
    printf("%s", student2.major);   
    return 0;
}
```

While Loop
```c
int main(){
    int index = 0;
    while (index <= 5){
        printf("Hello %d\n", index);
        index++;
    }
}
```
continue - Skipping while loop 
> skip the rest of the loop when i is 5
```c
#include <stdio.h>

int main() {
    int i = 0;

    while (i < 10) {
        i++;
        if (i == 5) {
            continue; // skip the rest of the loop when i is 5
        }
        printf("%d\n", i);
    }

    return 0;
}
```

Guessing Game using While Loop
```c
#include <stdio.h>
#include <stdlib.h>


//! guessing game
int main(){
    int secretNum = 5;
    int guess;

    while (guess != secretNum){
        printf("Guess a number: ");
        scanf("%d", &guess);
        printf("Your Guess is wrong, guess again\n");
    }
    printf("Your Guess is right\n");
             
    return 0;
}
```

2D Arrays 
> an array,
> + where each element is **an entire array, useful for matrix, grid or table of data**  
```c
#include <stdio.h>
#include <stdlib.h>

//! 2D Array
int main(){
    int nums[3][4] = {
        {1,2,3,10},
        {4,5,6,60},
        {7,8,9,90},
    };
    
    int i,j;
    for (i = 0; i<3; i++){
        for (j = 0; j<4; j++){
            printf("%d ",nums[i][j]);
        }
        printf ("\n");
    }

    return 0;
}
```

```c
#include <stdio.h>

int main(){
    // int numbers[2][3] = {
    //     {1,2},
    //     {3,4},
    //     {5,6},
    // };
    
    int numbers[2][3];
    int a = sizeof(numbers[0][0]);
    // printf(a);
    
    //? rows: size of the whole array / size of 1 row
    int rows = sizeof(numbers) / sizeof(numbers[0]);
    //? cols: size of 1 row / size of 1 element
    int cols = sizeof(numbers[0]) / sizeof(numbers[0][0]);
    
    printf("rows: %d\n", rows);
    printf("cols: %d\n", cols);
    
    int num = 0;
    for (int i=0; i<rows; i++){
        for (int j=0; j<cols; j++){
            num++;
            numbers[i][j] = num;
            printf("%d\n", numbers[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```
> rows: 2
cols: 3
1
2
3
-
4
5
6


Array of String
```c
#include <stdio.h>
#include <string.h>

int main(){
    char cars[][10] = {"FLower", "Hue", "Plane"};
    // must use "strcpy" to add item to string array 
    strcpy(cars[0], "Tesla");
    
    for (int i = 0; i < sizeof(cars)/sizeof(cars[0]); i++){
        printf("%s\n", cars[i]);
    }
    return 0;
}
```

Swap Array
```c
int main(){
    char x[] = "Lime";
    char y[] = "Dome";
    char temp[15];

    //! swap 2 values
    //? copy of x to temp
    strcpy(temp, x);
    //? copy of y to x
    strcpy(x, y);
    strcpy(y, temp);

    printf("x = %s\n", x);
    printf("y = %s\n", y);

    return 0;
}
```

Array Size
```c
char str_ary[10][50]; // now this array can only store 10 elements max
int i;
for (i=0; i<12;i++){
  printf("Nhap Chuoi %d:", i);
  gets(str_ary[i]);
}
printf('String ary: ', str_ary[])
```

**Memory Address**
```c

//! Memory Address
int main(){
    int age = 30;
    double gpa = 3.5;
    char grade = 'A';
	
    printf("age: %p\ngpa: %p\ngrade: %p", &age, & gpa, &grade);
	
    return 0;
}
```

###### Pointer 
>Think of its like a House Address. Your friend want to come to your house, however give them a picture of your house couldn'wouldn't help a lot, so you give them your house address. 
```c
//! Pointer
int main(){
    int age = 99;
    int * pAge = &age;
	
    double gpa = 3.14;
    int * pGpa = &gpa;
	
    char address = 'Newton Street';
    char * pAddress = &address;
	
    printf("GPA's memory address: %p\n", &pGpa);
    printf("Age's memory address: %p\n", &pAge);
    printf("Address's memory address: %p\n", &pAddress);
	
	
    return 0;
}
```
Age's memory address: 0061FF14
Address's memory address: 00000074

**Dereferencing Pointer**
	Take data from that memory address
	* pAge will print out the value 99
	* &pAge will print out the memory address like normal 
```c
printf("Age's memory address: %d\n", *&pAge);
printf("Address's memory address: %p\n", *pAddress);
```
Age's memory address: 6422292
Address's memory address: 00000074


**Writing Files**
> fpointer will be pointing at the memory address of the employee.txt file
r -read, w - write, a - append
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE * fpointer = fopen("employee.text", "r");
    fprintf(fpointer, "Employee, Jackseptieye\nPam, Receiptionist");
    fclose(fpointer);
    return 0;
}
```


Bit-shift
```c
 int main() {
     int num = 10; // binary: 1010
     int shiftAmount = 1;
     
     int result = num << shiftAmount; // result: 1010 << 0 (Add 0 to the right of binary num)
      // result: 10100
     printf("Value %d after 1-bit shift is: %d\n", num, result); 
     return 0;
}

void main(){
     int m;
     char st[32];
     printf("Enter a Integer: ");
     scanf("%d", &m);
     
     // Lấy biểu diễn nhị phân của m
     itoa(m, st, 2);
     printf("\n Binary of  (%d)=%s", m, st);
     
     // Gán bit thứ 5 từ bên phải của m bằng 1. Nếu 0 thì đổi thành 1, ko thì giữ nguyên.
     m |= 16; // mask = 16. Thêm vào vị trí bit có giá trị 16. e.g. m |= 16/32/64/
     // lấy biểu diễn nhị phân của m sau khi gán bit số 5 bằng 1
     itoa(m, st, 2);
     printf("\n  Binary = %s", st);
     getch();
}
```

**FILE**
gets();  
	read all line
scanf();
	read all line until space (stop scanning when there a space)

![[Pasted image 20240102070722.png]]
+ the big holder haldThePizza must be the same type as the convert data type: double in this example
to only type casting 1 value - cho vào trog ngoặc: (double) (slices) / people

### Calculate Binary with Recursion
```c
#include <stdio.h>

void printBinary(int num) {
    if (num > 1) {
        printBinary(num / 2);
    }
    printf("%d", num % 2);
}

int main() {
    printBinary(44);
}
```

### ASCII
behind every letter is a number behind it 
![[Pasted image 20240102072758.png]]
128 in bits -> 'A' in char form and 65 in numeric form


operator: + - * /
operand: 12345678..
precedence: * / (priority)
associaticity
![[Pasted image 20240102074246.png]]


array memory allocation
```C
int arrayLength;
printf("Nhap so luong phan tu: ");
scanf("%d", &arrayLength);

// allocate memory for each element in the array (base on the array length)
short *head = (short*)malloc(n * sizeof(short));
if (head == NULL){
  printf("Error: cannot allocate memory for array\n");
}
nhap_danhsach(head, arrayLength);


//! Ex4
for (int i = 0; i < arrayLength; i++){
  printf("pointer head value %d at %d\n", *(head + i), head+i);
}
```