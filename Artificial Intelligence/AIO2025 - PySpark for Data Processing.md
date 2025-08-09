## Phần 1. Big Data là gì ?
1) Thử Thách -> Động Lực của BigData đối vs tăng trưởng mạnh của Internet  
-> Dữ liệu được gọi BigDSpark  

Big Data Framework we learning today
![[Pasted image 20250807202436.png|444]]

## Phần 2. Giải thích cơ chế hoạt động của Hadoop và Apache Spark + Ví dụ áp dụng trong thực tế

Preprocessing data
	**Streaming (real-time data)** coming from mobile app like facebook, X (Twitter) -> Kafka.
	**Static Data (already downloaded data)** - index and process with Elastic Search
**Env to RDD

**HDFS:** giải thích cách Hadoop hoạt động 
![[Pasted image 20250807235352.png|444]]
**Map Reduce**
![[Pasted image 20250807235418.png|444]]


**Spark RDD (Resilient Distributed Dataset)**
Note: Explain RDD with python function terminology.
+ $ Transform data into each Partition, e.g. each data within a list get transform into a partition independently. Not like multi-threading where all thread share the same memory.
+ $ RDD is an Action. 
+ ? If a RDD i.e. Action fail, then it take data from RDD2 to recalculate.
![[Pasted image 20250807212103.png|533]]
Mỗi dữ liệu, biến trong mảng được chia vào 1 partition.


Ensured Partition to not broken. 
![[Pasted image 20250807204407.png|544]]

Each `RDD_n` perform a different task. So if a RDD_2 fail, we only have to re-perform RDD_2, not RDD_1.
![[Pasted image 20250807204215.png]]

+ $ Hadoop vs PySpark và tác vụ chuyên dụng của chúng
![[Pasted image 20250807204603.png|544]]
**Hadoop shuffle** -> if 1 step fail -> re-do all over again. (process linearly) - **1 system optimizing 1 tasks.**
**Spark divided to multiple RDD_d for each task**, this allow stable processing. If 1 step fail, only that step need toPySpark
Apache Spark provide tools for Data Sciecne, Engineering and Machine Learning.
	MLflow for version and meta data ![[Pasted image 20250807204847.png| 344]]
	![[Pasted image 20250807204953.png|433]]
	![[Pasted image 20250807205002.png| 344]]

Infrastructure create for initializing system e.g. Spark, Kubernetes for resource magement.

+ ? RDD is above Apache Spark Core API
![[Pasted image 20250807205020.png|344]]
Newest Spark version have another layer name Spark Connect above Tools.

SparkSQL integrate SQL queries to perform retrieval data like Parquet, Json, Csv.

MLib integrate algorithm for ML training, features extraction, tools for building pipelines. ![[Pasted image 20250807205240.png]]

**Spark Streaming** -> efficient real time data processing
	**Streaming** mean **data get generate rapidly** in real-time.
![[Pasted image 20250807205342.png|444]]

**Spark GraphX** -> for parallel execution, for graph analytical engine
![[Pasted image 20250807205436.png|444]]

Spark Connect - protocol for connect application with remote Spark server. (giao thức kết nối như TCP-IP)
	Why connect ? for submit data to Spark server. 
	1. establisth connect
	2.  translate query to logical plan, not processing but filter query as logical plan.
	3.  seriealize query
	4. perform query
![[Pasted image 20250807205749.png|444]]
Spark Conenct **version:** **3.5.1**

## Phần 3. Pyspark: python version of spark - Áp dụng Spark trong Python
Common error when connecting Spark: **v4.0.0** -> set-up with **v3.5.x**
![[Pasted image 20250807205831.png|544]]

Kiến trúc tương tự như Spark. Cũng có RDD và tools.
![[Pasted image 20250807205927.png|344]]

### Giải thích RDD hoạt động rõ hơn với PySpark
![[Pasted image 20250807210700.png|544]]
Without Action Transformation stay in 1 stage, thus didn't evolve/transform.


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


### So sánh Flow hoạt động của Sklearn và PySpark để dễ hơn
**Different Name, Same Function for ML**
In sklearn, we have  
![[Pasted image 20250807220355.png]]

In PySpark, we have
![[Pasted image 20250807220406.png]]

