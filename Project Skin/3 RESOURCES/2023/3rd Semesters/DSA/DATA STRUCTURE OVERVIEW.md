> Cách/ Phương Pháp Sắp Xếp, Xử Lý dữ liệu trên máy tính

### [[DATA STRUCTURE in 15 Min]]

### Data Structure **Type**

### Linear Data Structure 
>  Data arranged in sequence one after another.

##### Static 
	**1. Array**
> Arranged in continuous memory. All element are the same type.  
![[Pasted image 20230627181220.png]]

##### Dynamic
	**2. Stack** 
> Element are store in LIFO principle. (Last in First out)
![[Pasted image 20230627181435.png]]

	**3. Queue** 
> Element are store in LIFO principle. (First in First out)
![[Pasted image 20230627181523.png]]

	**4. Linked List** 
> Data element are connected through a series of nodes. 
![[Pasted image 20230627181757.png]]  

### Non-Linear Data Structure  
> Unlike Linear, element in Non-linear are not any sequence. Therefor **one Element will be connected to one or more element**.   

#### 1. Graph Structure
![[Pasted image 20230627182451.png]]
> Each node conencted to a vertex. (mỗi điểm kết nối với 1 đỉnh. Đỉnh này có thể là Điểm của 1 đỉnh khác)
![[Pasted image 20230627183938.png]]

#### 2. Tree Data Structure
![[Pasted image 20230627183253.png]]
> Similar to Graph. But each Vertex only have 2 nodes. (Parent connected to 2 children) But there are rule among data structure. 
>  > Like the righmost child is Max, leftmost child is Min.
![[Pasted image 20230627183951.png]]


| Linear Data Structure                                        | Non Linear Data Structure                       |
| ------------------------------------------------------------ | ----------------------------------------------- |
| Số lượng phần tử cố định (bắt buộc các phần phải có giá trị) | Ko tuyến tính nên Có thể có các phần tử rỗng () |
| Array, Stack, Queue                                          | Graph, Tree, Map                                     |
| Biểu diễn tuần sự -> 1 Lớp [array]                                                              | Không tuần tự -> liên kết đc với nhiều lớp. [{}] -> Dict inside List or List inside Dict                                                 |

Ưu và Nhược Điểm 
+ Không tối ưu bộ nhớ                                        | Từng kiểu dữ liệu tối yêu dựa trên kiểu vấn đề 
+ Đô phức tạp thời gian (Big(O))                        | Đỗ phức tạp thời gian Giữ Nguyên
	tăng theo số dữ liệu                                 
##### Why Data Structure?
>> Help me to understand how can to approach a Problems + Optimized + Effeciency + to Save Time & Memory.
