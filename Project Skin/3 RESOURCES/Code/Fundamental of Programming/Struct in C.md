```c
struct Student {
	int score;
	char name[100];
}
struct Student aStudent = {3.9, "Kevin"}; 
```

Declare a struct in better way
```c
typedef struct {
  char studentID[4];
  char studentName[129];
  float avgMark;
} Student;

Student myStudent = {"123", "Minh", 9.5};
```
