
### Generic = Allows for code reusability for different data types

![[Pasted image 20231004122506.png]]
In OOP, To swap 2 value of the same Data Type each time we'll need to make a new function. (int, float, string, etc...) 

With Generic we can set Data Type like (int, float, string, etc..) as a symbol T (note that T is just a name)
And **flexibly swaping T for other Data Type** without having re-write the whole function just to change its data type
```cs
public static void swap<T>(ref T a, ref T b){
	T temp = a;
	a = b;
	b = temp;
}

int a = 5, b = 7;
double c = 2.2, d = 5.5;
swap<int>(ref a, ref b)
swap<double>(ref a, ref b)
```


### Collections

Example:

List
![[Pasted image 20231004141949.png]]

Queue
![[Pasted image 20231004142035.png]]

Stack
![[Pasted image 20231004142108.png]]

