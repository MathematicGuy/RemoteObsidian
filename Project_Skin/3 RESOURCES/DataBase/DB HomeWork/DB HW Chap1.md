### Bài Tập Chương 1
note:
+ DBMS (Data Base Management)

**1.1 Chương này đã mô tả một số ưu điểm chính của hệ cơ sở dữ liệu. Hãy nêu hai nhược điểm của hệ cơ sở dữ liệu?**
**Advantages**
+ **Data Abstraction**
	Only show what are useful for the users or to hide he complexity of data from the basic users.
+ **Controlling Data Redundancy**
	DBMS system help controls the data redundancy and integrates all data into a single database file. As result saving storage and increase retrieval & update speed.
+ **Data Manipulation Easily**
	With tools like SQL, Php, etc.. data base can be easily manipulated (insertion, modification, deletion) easily. 
+ **Data  can be shared  world wide**
	Data can be shared easily by multiple applications in centralized DBMS.
**2 Draw Back**
+ **Cost of staff trainning**
	DBMS are often complex systems, so training is required for the users to use the DBMS. 
+ **Performance issues**
	As the number of users and data grows, DBMS may become slow to query and update.

**1.2 Liệt kê năm điểm khác biệt giữa hệ thống khai báo kiểu của một ngôn ngữ như Java hoặc C++ với ngôn ngữ định nghĩa dữ liệu được sử dụng trong cơ sở dữ liệu.**

1. **Object Creation**:   
    - In **DDL**, executing an action (such as creating a table) results in the creation of an object (e.g., a table) in the database.
      
    - In contrast, a **type declaration** in Java or C++ is simply an abstraction used within the program, not directly tied to creating database objects.
2. **Consistency Constraints**:
    - DDL allows specifying consistency constraints (such as primary keys, foreign keys, and unique constraints) for maintaining data integrity.
    
    - Programming language type systems (like Java and C++) generally do not allow such fine-grained constraints.
3. **Access Rights**:
    - DDL supports defining access rights for different users (e.g., granting read or write permissions).
      
    - Java and C++ do not inherently provide such access control mechanisms.
4. **Manipulating Data**:
    - A type declarative language like Java or C++ is used to manipulate data within the program itself (e.g., inserting, updating, or deleting rows).
      
    - DDL, on the other hand, defines column attributes of tables but does not directly manipulate data.
5. **Focus**:
    - DDL focuses on specifying types and relationships of attributes within relations (tables).
      
    - Programming languages allow creating objects and collections of objects beyond just table attributes.

**1.3 Hãy nêu 6 bước chính mà bạn sẽ thực hiện khi thiết lập cơ sở dữ liệu cho một doanh nghiệp cụ thể.**

1. **Formulate an Idea for a Solution**:
	   
    - Understand the enterprise’s requirements and objectives.
    - Identify the purpose of the database (e.g., managing customer data, inventory, transactions, etc.).
2. **Gather Information and Clarify Needs**:
    
    - Engage with stakeholders (users, managers, IT staff) to collect detailed requirements.
    - Define the scope of the database system.
3. **Develop a List of All Useful Fields**:
    
    - Create a comprehensive list of data elements (fields) that need to be stored.
    - Consider both primary data (e.g., customer names, product details) and metadata (information about the data).
4. **Organize the Fields into Logical Tables**:
    
    - Group related fields into tables based on their semantic meaning.
    - Normalize the tables to minimize redundancy and improve data integrity.
5. **Determine and Define Table Relationships**:
    
    - Establish relationships between tables (e.g., one-to-many, many-to-many).
    - Use keys (primary keys, foreign keys) to link records across tables.
6. **Test, Refine, and Improve**:
    
    - Develop prototypes or mockups to validate the design.
    - Test the system rigorously for correctness, performance, and security.
    - Iterate based on feedback and real-world usage.


**1.4 Hãy mô tả ít nhất 3 loại thông tin khác nhau mà một trường đại học sẽ lưu giữ, ngoài những loại thông tin được mô tả (trong mục 1.7 ở slide bài giảng) dưới đây**

+ **3 types of info an university would retain beside those given**:  total_budget, location, instructor_name, classroom_id, building_name, etc...

**1.5 Truy vấn từ khóa được sử dụng trong tìm kiếm trên Web khác với truy vấn cơ sở dữ liệu. Liệt kê những khác biệt chính về cách các truy vấn được chỉ định và về kết quả của một truy vấn.**

1. **Definition**:
    
    - **Web Search Queries**:
        - Web search queries are what users type into search engines (like Google) to find information online.
        - They are often plain text and rarely use boolean search directives.
    - **Database Queries**:
        - Database queries are specific actions to request information from a database.
        - They follow structured query languages (e.g., SQL) with strict syntax rules.
2. **Audience**:
    
    - **Web Search Queries**:
        - Typed by users seeking information.
        - Users are not aware of terms like “keywords” or “queries.”
    - **Database Queries**:
        - Executed by developers, analysts, or administrators.
        - Used to retrieve data from databases.
3. **Complexity**:
    
    - **Web Search Queries**:
        - Usually short and simple phrases.
        - Vary greatly due to unique user phrasing.
    - **Database Queries**:
        - More complex and structured.
        - Involve specifying conditions, joins, and aggregations.
4. **Result Type**:
    
    - **Web Search Queries**:
        - Return a list of web pages that match the keywords.
    - **Database Queries**:
        - Return a set of records (rows) that match the query criteria.
5. **Purpose**:
    
    - **Web Search Queries**:
        - Aimed at finding information, products, or services online.
    - **Database Queries**:
        - Used for data retrieval, reporting, analytics, or updates within a database.

**1.6 Liệt kê 4 ứng dụng bạn đã sử dụng có nhiều khả năng sử dụng hệ thống cơ sở dữ liệu để lưu trữ dữ liệu liên tục**

+ 4 apps that likely use DBMS to rapidly save datas 
	+ Zapier (update & automate tasks)
	+ Facebook (update infomation of all types )
	+ eToro (Updating Stocks price)
	+ Shoppe (Managing infos for customers and sellers)

**1.7 Liệt kê năm trách nhiệm của hệ thống quản lý cơ sở dữ liệu. Đối với mỗi trách nhiệm, hãy giải thích những vấn đề sẽ phát sinh nếu trách nhiệm đó không được thực hiện**
(+) : responsibilitie
(-) :  arise problems if responsibility is not fulfilled

+ Data Storage
	(+) Responsible for storing datas in persistent and organized manner.
	(-) Data may be lost, corrupted or inaccessible
+ Data Retrieval
	(+) Retrieving data in response to user queries.
	(-), The data may be inaccurate, incomplete, or slow to retrieve.
+ Data Integrity
	(+) Maintaining data integrity and consistency. It uses consistency constraints, transactions, and recovery mechanisms to ensure that the data is valid, reliable, and recoverable
	(-) The data may be inconsistent, erroneous, or irrecoverable.
+ Data Security
	(+) Protecting data from unauthorized access and modification. It uses authentication, authorization, and encryption mechanisms to control user access and secure data transmission.
	(-) Data may be vulnerable to breaches, leaks, or attacks.
+ Data Performance
	(+) Optimizing data performance and efficiency. It uses optimization engines, indexing, and caching techniques to improve query speed and resource utilization.
	(-) The data may be slow, inefficient, or costly to process.

**1.8 Giải thích những vấn đề nảy sinh khi thiết kế bảng trong hình dưới đây**
![[Pasted image 20231102210533.png]]

+ **Data redundancy:
	+ The table contains redundant data, such as the department name and building number for each employee. This can lead to data inconsistency and errors, and it can also make the table more difficult to maintain.
+ **Column names are not descriptive:**
	+ dept_name are not descriptive enough, it should be name "department" or "division"
+ **Table is not normalized:**
	+ Id order not follow any rule. Causing negative effect in searching process and data integrity. 
	+ The table is in first normal form (1NF) there for could be improve much more to minimize redundancy and improve data integrity.

**The table could be improved by:** 
- Adding a primary key to identify each employee uniquely.
- Creating separate tables for related data, such as departments and buildings.
Example:
```
Employee table:

id | name | salary | department_id | building_id

Department table:

id | name | building_id

Building table:

id | name
```
> This table design would eliminate the data redundancy and improve the data integrity of the original table.

**1.9 Hãy nêu 5 chức năng chính của người quản trị cơ sở dữ liệu ?**

1. **Design and Implementation**:
    
    - You create and maintain database standards and policies.
    - Support database design, creation, and testing activities.
    - Implement and maintain development and production database environments.
2. **Availability and Performance Management**:
    
    - Monitor database availability and performance.
    - Handle incident and problem management.
    - Administer database objects to achieve optimal utilization.
3. **Security and Integrity**:
    
    - Identify, report, and manage database security issues.
    - Implement audit trails for security purposes.
    - Ensure data integrity through proper access controls.
4. **Housekeeping and Optimization**:
    
    - Perform database housekeeping tasks such as tuning, indexing, etc.
    - Define and implement event triggers to alert on potential performance or integrity issues.
    - Design backup, archiving, and storage strategies.
5. **Monitoring and Maintenance**:
    
    - Monitor usage, transaction volumes, response times, concurrency levels, etc.
    - Continuously assess performance metrics.
    - Respond to changing requirements by adapting the database environment.

**1.10 Mô tả ít nhất 3 bảng có thể được sử dụng để lưu trữ thông tin trong hệ thống mạng xã hội như Facebook**

3 Tables that can be use to storeed datas in facebook social media system
+ **A friend's table** which contains the list of users who are connected to particular user.
+ **A user table** that contain their detailts like name, age, gender, location and other profile infomation. 
+ **A content table** containing user provided content, such as text, image and associated with the user who uploaded it.
