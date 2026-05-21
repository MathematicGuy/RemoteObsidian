
Tổng 10 Tuần.
Tuần 7-8: Kiểm tra giữa kì

---
[[BDA - HW1]]
[[BDA - Lab 2]]
[[BDA - Lab 5 MongoDB]]

---

Meta Data: [metadata](https://dataedo.com/kb/data-glossary/what-is-metadata) is data that describe data or **Data Properties** (E.g. Image Properties, Header, Table of contents, summary text of a book, book title, author)
![[Pasted image 20250107092616.png]]

**Big Data Characteristic**: **5 V**
+ **Velocity:** Speed at which data are generated and analyzed.
+ **Variety:** different types and forms of data (structured & un-structured)
+ **Value:** Potential of big-data for social development 
+ **Veracity:** Level of **quality, Integrity and Uncertainty of data**. 
+ **Volumn:** Vast amount of data generated through large-scale and digitalization of information. (like Velocity but **generated at vast scale instead of fast**) 

**Challenges:** store and process 
Too big -> distribute data to process in parallel. 
Trong suốt đối vs người dùg (indicate that the users don't know and don't care)

Hadoop Distributed FIle System(HDFS)
	Storage File (Block) in a Distributed file system (DFS) that run on large clusters. ![[hdfs-architecture.png]]

Each Blocks copies to 3 different DataNodes for Backup purpose.
Each file get divided into Blocks (often 3), each block typically 128MB or 256MB.
**Example:** 
+ A 500MB file would be divided into roughly 4 blocks (if block size is 128MB).
+ A 1GB file would be divided into roughly 8 blocks (if block size is 128MB).

3 Blocks saved to n different DataNodes -> Allow to save & process data more efficient. (3 copies for each block)![[Pasted image 20250109092748.png]]

---

**Basic Statistics**
- Mean
- Median
- Variance
- Counts
- Top-N
- Distinct

**Integration**
+ Bayesian Inference
+ Expectations
+ Markov Chain
+ Monte Carlo (Dat Circle Problem)

**Linear Algebra Computation**
+ Linear Algebra.
+ Linear Regresion
+ PCA

**7 main Computational Tasks in Analytic:**
1) Basis Statistics
2) Generalized N-Body Problems
3) Linear Algebraic Computation
4) Graph-Theoretic Computations
5) Optimizations
6) Integration 
7) Alignment Problems

**Process of Data Analysis**
![[Pasted image 20250114084521.png]]

**Data Graph** 
-> Meaning of each types of graph in Data Analytics

#### Big data analytics techniques
+ Quantitative Analysis - phân tích định lượng 
+ Qualitative Analysis - phân tích định tính -> phân tính tính chất của dữ liệu định lượng. 
+ Data Mining
+ Statistical Analysis
+ Machine Learning
+ Semantic Analysis
+ Visual Analysis

**A/B Testing -** Compare Example A with Example B to see which is better. 
**Correlation -** Tìm ra các mối quan hệ bằng cách *xem xét sự tương quan giữa đối tượng này vs các đối tượng khác*. 
**Regression -** is _a set of statistical methods used to estimate relationships_ between a dependent variable (i.e.`y`) and one or more independent variables (i.e. `X={x1, x2, ..., xn}`).
**Correlation vs Regression:** 

**Clustering vs Classification**
Clustering: 
+ Unsupervised Learning -> have no label, Machine have to learn the relationship between variables itself and self classified it into a cluster. (number of Classes is not limited)

Classification:
+ Supervised Learning -> have n given label. (Label is predefine thus number of Classes is limited) 

---
# Hadoop Architecture

## [MapReduce](https://www.todaysoftmag.com/article/1358/hadoop-mapreduce-deep-diving-and-tuning)
**Abstract:** Organize and Reduce 
**Process:**
![[a11.png]]
1) Load Big Data
2) Map multiple data as <key, value> pairs from Big Data..
3) <key, value> pairs then get Shuffle and Sort 
4) The Reduce function takes in input as <key, value> pairs and produces - <key,value> pairs as output.

## YARN
+ ? Yarn stand for Yet Another Resource Negotiator
-> Allocates Allocates RAM, memory and other resources to different applications. 
![[Pasted image 20250206074113.png]]

## Hadoop Distributed Filesystem (HDFS)
### What is Distributed Filesystem (DFS) ?
> Divide a big File System into Smallar Managable File Systems which all connected to eachother. 
![[Pasted image 20250206074333.png]]
>Files from smaller Fs increase processing speed with each Fs focus on a separated task. 
	note: Fs mean File system

### Hadoop Cluster
Each cluster work with Master Salves where Master Fs manages Slaves Fs
![[Pasted image 20250206074805.png]]

### Hadoop Cluster Architecture Overview
**YARN:** act as the MASTER
**HDFS:** act as the SLAVE
![[Pasted image 20250206075031.png]]

**FS-Image:** Current data status
**Edit log:** Status changes history
With SECONDARY NAMENODE act like a supporter for the 1st NAMENODE
![[Pasted image 20250206075357.png]]

Each file in **HDSF is stored as a data block.** **Default size is 128MB** with the **last block can be the same or lesser.** 
![[Pasted image 20250206081050.png]]
Each note block have 3 Replica so Block's data (e.g. B & D) is not lost even if the Node 5 crashes. 
![[Pasted image 20250206081251.png]]

**Advantages of HDFS**
+ **Scalable:** as it uses distributed storage
	Cluster -> optimize storage space
+ **Cost effective:** require less power to process Big Data as HDFS process tasks in individua cluster which increase efficiency.
+ **Fault tolerant:** HDFS have multiple data copies (ie. Replication) to crashes if any Node fail.
+ **Data Security:** Procevides data security (e.g. encryption, authen, auti, etc.)

## Hadoop HDFS commands
![[Pasted image 20250206082544.png]]
>[Apachy Hadoop Setup](https://topdev.com.vn/d/271-apache-hadoop-la-gi-cach-xay-dung-apache-hadoop-va-code-java-voi-no)

## MAP REDUCE PATTERN

### Numerical Summarization 
+ ? Numerical summarization patterns are used to compute various statistics such as counts, maximum, minimum, mean, etc.

#### Example: Count
1) **Map**: map number of time URL get visited. ![[Pasted image 20250206091735.png]]
2) **Sort & Shuffle**: Sort each URL and shuffle them into group 
	![[Pasted image 20250206091923.png]]
3) **Reduce:** Merge and Count URL in each URL group ![[Pasted image 20250206092228.png]]

#### Example: Max/min
![[Pasted image 20250206092325.png]]

---
# Deep Dive into Hadoop

[HDF Turtorial](https://www.cloudera.com/services-and-support/tutorials.html)
Get Account & Password in *QUICK LINKS*. AMBARI's pass and acc is *raj_ops*    
![[Pasted image 20250211113918.png]]

---

**Final Semester Format Report** 
- **Mở đầu:** giới thiệu bài toán và giới thiệu phương pháp của mình. 
- **Tổng quan**: lược sử về bài toán, những cách giải pháp đã có rồi, giải pháp đó giải quyết vấn đề đến đâu, lỗ hổng của giải pháp đó. Cuối cùng nêu ra hướng tiếp cận và giải pháp của mình.  
- **Phương pháp thực hiện**: ý tưởng và các bước
- **Thực nghiệm và đánh giá kết quả**
- **Kết luận:** kết luận kết quả của mình, đã làm đc gì, vấn đề gì đã được giải quyết.  
- **Tài liệu tham khảo** (chính thống, chọn lọc tài liệu chất lượng chứ ko cần chọn nhiều)
- **Phụ lục:** giải thích định nghĩa, **để nói rõ thêm 1 số dữ liệu**, có thể chứa hình ảnh.  

Slide: 15 trang
Báo cáo: 15-20 trang

---



