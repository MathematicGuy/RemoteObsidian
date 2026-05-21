- Length is Constant 
+ Muốn đi tới phần tử nào đó thì phải đi từ đầu (Bộ nhớ từ điển)

**contiguous**
> Array is contiguos so data can be almost access instanctly. 
> (Các phần tử đc lưu ở các vị trí liền kề nhau - theo cùng 1 hàng ko tính cột )
> VD: Hash Table
![[Pasted image 20230801075552.png]]

**non contiguous** 
> Store a value which reference where the next value is. Have Overhead time -> thus take additional times.
> (Các phần tử sắp xếp ko liền kề, khác )
>![[Pasted image 20230801075648.png]]


| homogeneous                  | heterogenous                   |     |
| ---------------------------- | ------------------------------ | --- |
| > Contain same type of value | any kind of value can be mixed |     |
| (Cùng kiểu giá trị)          | (Mọi kiểu giá trị)                               |     |


Compilar - the brain of the language
>How python using array to Get & Store it values
>-> Take & Store Value in an Seperate Array.
![[Pasted image 20230801080705.png]]

Để duy trì độ dài của dãy khi:
Insert -> *phần tử mới vào ô nhó khiến các phần tử dịch sang phải bắt đầu từ phần tử insert*  (Để cân bằng độ dài dãy khi 1 ô nhớ mới đc thêm vào ở cuối dãy. Phần tử cuối cùng dịch sang phải để chiếm đóng ô nhớ, các phần tử sau nó cũg dịch sang để lấp đầy ô nhớ bên phải của nó, Cuối cùng ô nhớ dành cho phần tử insert sẽ trống. Bắt đầu insert phần tử vào ô nhớ đó) O(n)

Delete -> các phần tử lùi sag (để chiếm lấy ô nhớ có phần tử bị xóa). *Cách thức như trên nhưng dịch trái*
O(n)



