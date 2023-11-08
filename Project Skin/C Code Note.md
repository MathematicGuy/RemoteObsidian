
input
```c
int main(){
	int number;
	printf("Enter a number: ");
	scanf("%d", &number); //take %digit as an input
	printf("You enter number: %d\n", number);
	
	return 0;
}
```
> Take Double input 
```c
int main(){
    char celebrityF[20]; 
    char celebrityL[20];
    scanf("%s%s", celebrityF, celebrityL); // double input
    
    printf("I love %s %s\n", celebrityF, celebrityL);
	
    return 0;
}
```


Array
```c
int number[] = {1,2,3,4,5,6,7,8};
number[2] = 200;
printf("You enter number: %d\n", number[2]);

return 0;
```

Function
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
+ Function input
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

If Statement
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


2D Arrays - Just like Matrix 
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

Memory Address
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

