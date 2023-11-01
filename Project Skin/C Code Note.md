
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

### Function
Assigned
```c

```
Itoa
```c

```