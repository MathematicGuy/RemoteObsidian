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

