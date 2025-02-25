**Activate HBASE**
```sh
hbase shell
```

# Lab 2 Overview

## Step 1: Set Up Your HDP Sandbox

Before you begin, ensure:

- The **HDP Sandbox** is installed and running.
- You have **SSH access** to the HDP Sandbox.
- **HBase and Hive services** are running.

To check:
```bash
# SSH into the Sandbox
ssh root@<sandbox-ip>

# Start HBase if not running
start-hbase.sh

# Start Hive if needed
hive
```

---

## Step 2: Practice HBase

You'll execute HBase shell commands to create and manipulate a table.

### **1️⃣ Connect to HBase**

```bash
hbase shell
```

### **2️⃣ Create a Table**

```bash
create 'students', 'info'
```

### **3️⃣ Insert Data**

```bash
put 'students', '1001', 'info:name', 'Nam'
put 'students', '1001', 'info:age', '21'

put 'students', '1002', 'info:name', 'Thanh'
put 'students', '1002', 'info:age', '23'

put 'students', '1003', 'info:name', 'Hai5D5D5D'
put 'students', '1003', 'info:age', '22'
```
![[Pasted image 20250213091213.png]]
![[Pasted image 20250213091219.png]]

### **4️⃣ Retrieve Data**
```bash
get 'students', '1001'   # Get all details for student 1001
get 'students', '1002', 'info:name'  # Get only the name of student 1002
scan 'students'  # Retrieve all records
```
![[Pasted image 20250213083801.png]]

### **5️⃣ Modify Data**

```bash
put 'students', '1003', 'info:age', '22'  # Update Charlie’s age
```

### **6️⃣ Delete Data**
```bash
delete 'students', '1002', 'info:age'  # Remove Bob’s age
deleteall 'students', '1003'  # Delete Charlie’s row
```
![[Pasted image 20250213084219.png]]

### **7️⃣ Drop the Table**
```bash
disable 'students2'
drop 'students2'
```
Before
![[Pasted image 20250213091507.png]]
After
![[Pasted image 20250213091550.png]]

### **8️⃣ Add a New Column Family**
```bash
alter 'students', 'contact'
put 'students', '1001', 'contact:email', 'alice@example.com'
```
![[Pasted image 20250213084800.png]]

---

## Step 3: HBase and Pig Integration

You'll run a **Pig script** to load data into HBase.

### **1️⃣ Download Required Files**
```bash
wget https://raw.githubusercontent.com/ashaypatil11/hadoop/main/movies.user
wget https://raw.githubusercontent.com/ashaypatil11/hadoop/main/hbase_example.pig
```
Check if File Uploaded in Root File) 
+ ? `~` mean root file
```sh
ls ~
cd ~ # to to root file
```
	
### **2️⃣ Upload Files to HDFS**

```bash
hadoop fs -mkdir /user/maria_dev/pig
hadoop fs -copyFromLocal movies.user /user/maria_dev/pig/movies.user
```

### **3️⃣ Verify Pig Script**

```bash
less hbase_example.pig
```

### **4️⃣ Start HBase Services**

```bash
start-hbase.sh
```
if already start use
```sh
hbase shell
```

### **5️⃣ Execute Pig Script**

```bash
pig hbase_example.pig
```
![[Pasted image 20250217213937.png]]

check the **detailed error logs**:
`cat /var/log/pig/*.log | tail -50`
Access hadoop: `http://192.168.1.60:8088/cluster` 

### **6️⃣ Verify Data in HBase**
![[Pasted image 20250218065500.png]]
```bash
hbase shell
list
scan 'your_hbase_table_name'
```

---

## Step 4: Practice Hive

You'll work with **web store data** to perform SQL-like queries.

### **1️⃣ Download Sample Data**

Download and extract: [Click here](https://drive.google.com/file/d/1Otyp8MI5soC6qS1OeodHYuNkMbXFj6Tl/view?usp=sharing)

Extract:
- `Omniture.0.tsv.gz`
- `users.tsv.gz`
- `products.tsv.gz`

### **2️⃣ Upload Data to HDFS**

```bash
hadoop fs -mkdir /tmp/admin
hadoop fs -copyFromLocal Omniture.0.tsv /tmp/admin/
hadoop fs -copyFromLocal users.tsv /tmp/admin/
hadoop fs -copyFromLocal products.tsv /tmp/admin/
```

### **3️⃣ Create Hive Database**

```sql
CREATE DATABASE IF NOT EXISTS click;
```

### **4️⃣ Create Tables**

```sql
USE click;

CREATE TABLE users (
  swid STRING, 
  birth_dt STRING, 
  gender_cd CHAR(1)
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE 
TBLPROPERTIES ("skip.header.line.count"="1");

CREATE TABLE products (
  url STRING, 
  category STRING
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE 
TBLPROPERTIES ("skip.header.line.count"="1");

create table omniturelogs (col_1 STRING,col_2 STRING,col_3 STRING,col_4 STRING,
						   col_5 STRING,col_6 STRING,col_7 STRING,col_8 STRING,col_9 STRING,col_10 STRING,col_11 STRING,col_12 STRING,col_13 STRING,col_14 STRING,col_15 STRING,col_16 STRING,col_17 STRING,col_18 STRING,col_19 STRING,
						   col_20 STRING,col_21 STRING,col_22 STRING,col_23 STRING,col_24 STRING,
						   col_25 STRING,col_26 STRING,col_27 STRING,col_28 STRING,col_29 STRING,
						   col_30 STRING,col_31 STRING,col_32 STRING,col_33 STRING,col_34 STRING,
						   col_35 STRING,col_36 STRING,col_37 STRING,col_38 STRING,col_39 STRING,
						   col_40 STRING,col_41 STRING,col_42 STRING,col_43 STRING,col_44 STRING,
						   col_45 STRING,col_46 STRING,col_47 STRING,col_48 STRING,col_49 STRING,
						   col_50 STRING,col_51 STRING,col_52 STRING,col_53 STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED by '\t'
stored as textfile
tblproperties ("skip.header.line.count"="1");
```

### **5️⃣ Load Data into Hive**

```sql
LOAD DATA INPATH '/tmp/admin/products.tsv' OVERWRITE INTO TABLE products;
LOAD DATA INPATH '/tmp/admin/users.tsv' OVERWRITE INTO TABLE users;
LOAD DATA INPATH '/tmp/admin/Omniture.0.tsv' OVERWRITE INTO TABLE omniturelogs;
```

### **6️⃣ Run Queries**

```sql
SELECT * FROM users LIMIT 5;
SELECT * FROM products LIMIT 5;
SELECT COUNT(*) FROM omniturelogs;
```


```sql
SELECT * from omniturelogs;
SELECT * from omniturelogs;
SELECT * from omniturelogs;
```
### In order to optimize your website and convert more visits into sales and revenue.

**Analyze the clickstream data by location**
+ $ Find high-revenue locations.
+ ? This query count the **clickstream by user location**.
```sql
SELECT col_50, COUNT(*) AS total_vitis
FROM omniturelogs
GROUP BY col_50;
```


**Filter the data by product category**
+ $ Understand interest by category
+ ? This query retrieves **clickstream interactions** for a specific **product category**.
```sql
SELECT location, 
       COUNT(*) AS total_visits, 
       SUM(revenue) AS total_revenue
FROM clickstream_data
GROUP BY location
ORDER BY total_revenue DESC;
```
![[Pasted image 20250225092519.png]]

**Graph the website user data by age and gender**
+ $ Visualize user behavior
+ ? This query aggregates **user visits and revenue** based on **age and gender**.
```sql
SELECT birth_dt, 
       CASE 
           WHEN CAST(SUBSTRING(birth_dt, -2) AS INT) > 25 
           THEN 1900 + CAST(SUBSTRING(birth_dt, -2) AS INT)  -- Convert '84' to 1984
           ELSE 2000 + CAST(SUBSTRING(birth_dt, -2) AS INT)  -- Convert '05' to 2005
       END AS birth_year,
       2025 - (CASE 
                   WHEN CAST(SUBSTRING(birth_dt, -2) AS INT) > 25 
                   THEN 1900 + CAST(SUBSTRING(birth_dt, -2) AS INT)
                   ELSE 2000 + CAST(SUBSTRING(birth_dt, -2) AS INT)
               END) AS age,
		gender_cd
FROM users;
```
![[Pasted image 20250225094035.png]]
![[Pasted image 20250225094025.png]]

**Pick a target customer segment**
+ $ Choose high-revenue customer segments
+ ? Find the c based on revenue contribution.
```sql
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 24 THEN '18-24'
        WHEN age BETWEEN 25 AND 34 THEN '25-34'
        WHEN age BETWEEN 35 AND 44 THEN '35-44'
        WHEN age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    COUNT(*) AS total_users
FROM (
    SELECT 
        gender_cd, 
        2025 - (
            CASE 
                WHEN CAST(SUBSTR(birth_dt, -2) AS INT) > 25 
                THEN 1900 + CAST(SUBSTR(birth_dt, -2) AS INT)
                ELSE 2000 + CAST(SUBSTR(birth_dt, -2) AS INT)
            END
        ) AS age
    FROM users
) 
GROUP BY age_group, gender_cd
ORDER BY total_users DESC
LIMIT 1;

```

**Identify a few web pages with the highest bounce rates**
+ $ Optimize low-performing pages
+ ? Bounce rate = (single-page visits) ÷ (total visits).
```sql
SELECT page_url, 
       COUNT(CASE WHEN exit_page = entry_page THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM clickstream_data
GROUP BY page_url
ORDER BY bounce_rate DESC
LIMIT 10;
```



---

## Step 5: Self-learning - Hortonworks ODBC Driver

Install the **Hortonworks ODBC Driver** to connect Hive with Power BI, Excel, or Tableau.

🔗 **Guide**: [Watch Here](https://www.youtube.com/watch?v=PeTBqfUnwsw)

### Connect Hive with Python

```python
from pyhive import hive
import pandas as pd

# Establish connection
conn = hive.Connection(host='localhost', port=10000, username='hive')
cursor = conn.cursor()

# Execute a query
cursor.execute("SHOW TABLES")

# Fetch and print results
for table in cursor.fetchall():
    print(table)

# Close connection
cursor.close()
conn.close()
```

---

## **✅ Summary**

| Task                                                        | Status |
| ----------------------------------------------------------- | ------ |
| ✅ Set up HDP Sandbox                                        | ✅      |
| ✅ Practice HBase (Create, Insert, Query, Delete)            | ✅      |
| ✅ HBase-Pig Integration (Pig script for HBase)              | ✅      |
| ✅ Practice Hive (Create tables, Load data, Query)           | ✅      |
| ✅ Self-learning: Hortonworks ODBC & Python-Hive Integration | ✅      |
