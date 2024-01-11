fgets() use to read file
```c
char buffer[256];
FILE* file = fopen("file.txt", "r");
if (file != NULL) {
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    fclose(file);
}
```
> Printf until the end of file


fprintf() use to print to file
```c
FILE* file = fopen("file.txt", "w");
if (file != NULL) {
    fprintf(file, "Hello, %s!\n", "world");
    fclose(file);
}
```


```c
#include <stdio.h>

int main() {
  int arr[5] = {1, 2, 3, 4, 5};
 
  // Mở file để ghi
  FILE *fp = fopen("test.bin", "wb");
 
  // Ghi mảng vào file
  fwrite(arr, sizeof(int), 5, fp);
 
  // Đóng file
  fclose(fp);

  // Mở lại để đọc
  fp = fopen("test.bin", "rb"); // read in binary mode
 
  // Đọc dữ liệu từ file
  int readArr[5];
  fread(readArr, sizeof(int), 5, fp);

  // In ra mảng đọc được
  for(int i = 0; i < 5; i++) {
    printf("%d ", readArr[i]);
  }

  fclose(fp);
 
  return 0;
}
```