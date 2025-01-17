
Tổng 10 Tuần.
Tuần 7-8: Kiểm tra giữa kì

---
[[BDA - HW1]]


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


