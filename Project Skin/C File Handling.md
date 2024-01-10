```c
while((c=fgetc(fp))!=EOF)
	printf("%c",c);
```
> Printf until the end of file



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