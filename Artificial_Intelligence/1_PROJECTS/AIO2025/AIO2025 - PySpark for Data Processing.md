## Phần 1. Big Data là gì ?
Thử Thách -> Động Lực của BigData đối vs tăng trưởng mạnh của Internet  -> Dữ liệu được gọi là  Big Data khi   

Big Data Framework we learning today
![[Pasted image 20250807202436.png|444]]

## Phần 2. Giải thích cơ chế hoạt động của Hadoop và Apache Spark + Ví dụ áp dụng trong thực tế

Preprocessing data
	**Streaming (real-time data)** coming from mobile app like facebook, X (Twitter) -> Kafka.
	**StatiConnect version: 3.5.1

## Phần 3. Pyspark: python version of spark - Áp dụng Spark trong Python

Common error when connecting Spark: **v4.0.0** -> set-up with **v3.5.x**
![[Pasted image 20250807205831.png|544]]
Kiến trúc tương tự như Spark. Cũng có RDD và tools.
![[Pasted image 20250807205927.png|344]]

### Giải thích RDD hoạt động rõ hơn với PySpark
![[Pasted image 20250807210700.png|544]]
Without Action Transformation stay in 1 stage, thus didn't evolve/transform.
w

RDD comming partition like Disk. Parallelize data -> Partialize data for parallel processing.
![[Pasted image 20250807211053.png]]

5 data in num_data -> 5 partition. 
**Each RDD represent a action**
![[Pasted image 20250807211142.png|544]]

![[Pasted image 20250807211348.png|544]]

+ ? Vậy cơ bản, Spark RDD là xử lý từng data song song. mỗi RDD đại diện cho là 1 hàm thế nên nếu 1 bước RDD fail mình ms ko cần chạy lại toàn bộ.


### Spark DataFrame - So sánh Spark vs Pandas trước rồi đi vào giải thích từng Code BlockBlock
Spark track each Action/RDD as Stage. 
![[Pasted image 20250807213351.png | 544]]

Defining function in PySpark
![[Pasted image 20250807213436.png| 544]]

```ad-abstract
Để thực hiện 1 yêu cầu (chương trình) trên 1 khối lượng dữ liệu khổng lồ nó khó hơn bình thường. Về mặt phân lớp thì chia thành 2 lớp:  
  
-) Lớp 1 là logic của chính chương trình đấy  
  
-) Lớp 2 là việc thực thi logic ấy trên 1 bộ dữ liệu khổng lồ mà vẫn đảm bảo hiệu năng. Ví dụ 1 hàm search trên 1 kho dữ liệu khổng lồ là không đơn giản. Các giải pháp song song trên BigData phải phân tích nhiệm vụ, chia thành các tác vụ, chia việc cho các cụm máy, quản lý tài nguyên, gom góp kết quả, tổng hợp kết quả, tối ưu hạ tầng, phần cứng cho 1 lệnh tưởng chừng rất đơn giản.  
  
Những giải pháp như Spark theo mình nghĩ là đảm bảo làm sao mình chủ yếu quan tâm đến công việc lớp 1 và không phải quan tâm đến quá nhiều công việc ở lớp 2. Đi vào chi tiết thì hoa mắt nhưng hiểu sơ sơ thì vậy.
```

### Spark SQL: Tương tự phần trên nhưng cho SQL
Giải thích mỗi Câu lệnh Pyspark sử dụng SQL.
PySpark UI for monitoring.
Repartition -> gộp lại. 

`select()` - actually a transformation function, surprise.
`udf()` - áp dụng 1 custom function lên từng dòng trong DataFrame.  
`Cache vs Persist` - the same, only diff is the level of control they offer over the storage strategy.
	Cache is Persist with default storage level with Memory Only. Persist provide more control over storage level. In short, Cache is a storage level while Persist is a function to choose storage level.  

**Lazy Evaluation** - doesn execute immediately, but build a Execution plan (DAG or Directed Acrylic Graph) of the operation. 
	hold the evaluation process of an expression untils its value is needed, this avoid repeated evaluations.
	
Checkpoint - checkpoint for error. almost like git or cache. (When DAG is too long or error prone)

### Đi Qua các Phương Pháp Tối Ưu PySpark



## Phần 4. So sánh Flow hoạt động của Sklearn và PySpark để dễ hơn
**Different Name, Same Function for ML**
In sklearn, we have  
![[Pasted image 20250807220355.png]]

In PySpark, we have
![[Pasted image 20250807220406.png]]

