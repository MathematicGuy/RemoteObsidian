### AWS Cloud Practitioner Practice Questions (Set 3)

Q1. Which type of replication does an Amazon RDS Read Replica use?
- [ ] A. Synchronous replication
- [ ] B. Multi-region synchronous replication
- [ ] C. Snapshot-based replication
- [x] D. Asynchronous replication

Q2. Between the two engines supported by Amazon ElastiCache, which one supports Multi-AZ with Auto-Failover and data persistence?
- [x] A. Redis
- [ ] B. Neither
- [ ] C. Both Memcached and Redis
- [ ] D. Memcached

Q3. You need a message queue that guarantees messages are processed in the exact order they were sent and prevents duplicates. Which queue type should you use?
- [ ] A. Priority Queue
- [ ] B. Standard Queue
- [ ] C. Dead-Letter Queue
- [x] D. FIFO Queue

Q4. Which feature allows an Aurora database to be restored to a specific point in time without using backups or creating a new cluster?
- [ ] A. Point-in-Time Restore (PITR)
- [x] B. Backtrack
- [ ] C. Snapshot Restore
- [ ] D. Database Cloning

Q5. You want to decouple two microservices so that the "Order Service" can continue to function even if the "Shipping Service" is temporarily unavailable. Which service should you use?
- [ ] A. Amazon SNS
- [ ] B. Amazon RDS Proxy
- [x] C. Amazon SQS
- [ ] D. Amazon Route 53

Q6. What is the primary benefit of deploying an Amazon RDS database with a Read Replica configuration?
- [ ] A. Provide synchronous replication for Disaster Recovery.
- [x] B. Offload read-heavy traffic from the primary database instance.
- [ ] C. Automatically scale storage capacity when space runs out.
- [ ] D. Improve the write performance (INSERT, UPDATE) of the database.

Q7. A company needs to ensure their database can automatically failover to another Availability Zone with zero manual intervention in case of an outage. Which RDS feature should they enable?
- [ ] A. Read Replicas
- [x] B. Multi-AZ Deployment
- [ ] C. Auto Scaling Group
- [ ] D. Database Snapshotting

Q8. A company wants to send a single alert that triggers an email notification to the admin and simultaneously starts a Lambda function to log the event. Which architecture is best?
- [x] A. SNS Topic with Email and Lambda as subscribers
- [ ] B. SQS Queue with Email and Lambda as consumers
- [ ] C. Amazon CloudWatch Logs
- [ ] D. SES (Simple Email Service)

Q9. Which CIDR suffix allows for the largest number of total IP addresses?
- [ ] A. /32
- [ ] B. /24
- [ ] C. /16
- [x] D. /8

Q10. An engineering team wants to ensure that in case of an Availability Zone (AZ) outage, their RDS database should continue working on the same endpoint without any manual administrative intervention. Which of the following solutions addresses this use-case?
- [x] A. Configure the database in Multi-AZ deployment
- [ ] B. Configure the database in RDS Read Replica mode
- [ ] C. Provision the database via AWS CloudFormation
- [ ] D. Enable RDS Storage Auto Scaling

Q11. A company needs to improve read performance of its production database without affecting write operations. Which solution is MOST appropriate?
- [ ] A. Enable Multi-AZ
- [x] B. Create Read Replicas
- [ ] C. Enable automated backups
- [ ] D. Use snapshots

Q12. Which RDS feature uses synchronous replication and automatically fails over without manual intervention?
- [x] A. Multi-AZ
- [ ] B. Read Replica
- [ ] C. Backup & Restore
- [ ] D. Auto Scaling

Q13. An application needs extremely fast data access with very low latency for frequently accessed data. Which service should be used?
- [ ] A. Amazon RDS
- [ ] B. Amazon Aurora
- [x] C. Amazon ElastiCache
- [ ] D. Amazon SQS

Q14. A system requires guaranteed message ordering and no duplicate processing. Which combination should be used?
- [x] A. SNS FIFO + SQS FIFO
- [ ] B. SNS + SQS Standard
- [ ] C. SQS Standard only
- [ ] D. Amazon MQ

Q15. A company wants the lowest-cost disaster recovery strategy and can tolerate long recovery time. Which approach should they choose?
- [ ] A. Multi-site
- [ ] B. Warm Standby
- [ ] C. Pilot Light
- [x] D. Backup & Restore

Q16. Which statement correctly describes Aurora compared to standard RDS?
- [ ] A. Aurora does not support replication
- [ ] B. Aurora is slower than RDS
- [x] C. Aurora automatically scales storage up to large capacity
- [ ] D. Aurora only supports one Availability Zone

Q17. A company wants to deploy its infrastructure in AWS while keeping full control over IP addressing, internal communication rules, and internet access configuration. Which AWS service provides this capability?
- [ ] A. Security Group
- [ ] B. Subnet
- [x] C. VPC
- [ ] D. Route Table

Q18. A company creates a subnet that has a route to an Internet Gateway and is directly accessible from the internet. What type of subnet is this?
- [ ] A. Private Subnet
- [x] B. Public Subnet
- [ ] C. Isolated Subnet
- [ ] D. Internal Subnet

Q19. A private subnet needs to access the internet for downloading updates but must not be directly accessible from the internet. Which component is required?
- [ ] A. Internet Gateway
- [ ] B. Route Table
- [x] C. NAT Gateway
- [ ] D. Security Group

Q20. Which statement correctly describes a subnet in AWS?
- [ ] A. It spans multiple regions
- [ ] B. It is a physical server
- [x] C. It is a logical subdivision of a VPC within a specific AZ
- [ ] D. It replaces VPC

Q21. A startup wants a managed relational database for a steady, predictable workload using standard MySQL with minimal administration. High availability in a single Region is required, but they do not need global replication. Which service best fits their needs?
- [x] A. Amazon RDS for MySQL
- [ ] B. Amazon DynamoDB
- [ ] C. Amazon Aurora Global Database
- [ ] D. Amazon Neptune

Q22. You notice that requests to your application fronted by an Application Load Balancer (ALB) sometimes fail when one Availability Zone experiences issues, even though other Zones are healthy. Which configuration change can improve resilience to AZ failures?
- [ ] A. Disable health checks on the ALB so that it continues sending traffic to all targets evenly.
- [ ] B. Register targets with the ALB only in a single Availability Zone to simplify routing.
- [x] C. Enable cross-zone load balancing on the ALB and ensure there are healthy targets in multiple Availability Zones.
- [ ] D. Use Network ACLs to block traffic from the affected Availability Zone.

Q23. An e-commerce company is experiencing order loss during peak traffic because the Order service directly calls the Payment service, and they want to decouple the system while ensuring no data loss, which solution is most appropriate?
- [x] A. Amazon SQS
- [ ] B. Amazon SNS
- [ ] C. Amazon EC2
- [ ] D. Amazon RDS

Q24. An AdTech company needs to process clickstream data from millions of users in real-time with very high throughput, which service is the best fit?
- [ ] A. Amazon SQS
- [ ] B. Amazon SNS
- [x] C. Amazon Kinesis
- [ ] D. Amazon S3

Q25. A company is deploying a web application that uses Amazon RDS as its database. To ensure optimal security and the ability to perform software patching, which architecture is the MOST suitable?
- [ ] A. Deploy the RDS instance in a public subnet so that the AWS technical team can access and patch the database directly via the internet.
- [x] B. Deploy the RDS instance in a private subnet, use a NAT gateway to allow outbound connections for software updates, and configure a security group to allow traffic only from the web server.
- [ ] C. Use an internet gateway to provide a direct connection between end-users and the RDS instance to reduce query latency.
- [ ] D. Deploy both the RDS instance and the web server in the same public subnet and use a Network ACL to block all inbound traffic from external sources.

Q26. In an Amazon VPC, which of the following conditions characterizes a subnet as a 'Public Subnet'?
- [ ] A. It contains EC2 instances with the most powerful configurations.
- [ ] B. It is configured to deny all inbound traffic from external sources.
- [ ] C. It is located within a default Availability Zone.
- [x] D. It has a route in its route table that points to an Internet Gateway.

Q27. Which VPC component allows resources in a private subnet to connect outbound to the internet (for example, to download software updates,...) but prevents the internet from initiating a connection to those resources?
- [ ] A. Security Group
- [ ] B. Internet Gateway
- [x] C. NAT Gateway
- [ ] D. Virtual Private Gateway

Q28. Which AWS service is a managed relational database service that supports engines like MySQL, PostgreSQL, and Oracle?
- [ ] A. Amazon DynamoDB
- [x] B. Amazon RDS
- [ ] C. Amazon Redshift
- [ ] D. Amazon ElastiCache

Q29. What is the main purpose of an Internet Gateway (IGW) in a VPC?
- [ ] A. To connect two different VPCs together.
- [x] B. To allow communication between your VPC and the internet.
- [ ] C. To encrypt data stored in S3 buckets.
- [ ] D. To balance traffic across multiple EC2 instances.

Q30. A company is building an e-commerce application using a relational database. They require: - Automatic read scaling - Fast failover (under 30 seconds) - Minimal operational overhead. Which solution is the most appropriate?
- [ ] A. Amazon RDS Multi-AZ with Read Replica
- [x] B. Amazon Aurora with Aurora Replicas
- [ ] C. Amazon DynamoDB with DAX
- [ ] D. Amazon RDS Single-AZ with automated backup

Q31. A company wants to implement a disaster recovery (DR) strategy with the following requirements: - Lowest possible cost - Recovery can take a few hours. Which strategy is the most appropriate?
- [x] A. Backup & Restore
- [ ] B. Pilot Light
- [ ] C. Warm Standby
- [ ] D. Multi-site Active-Active

Q32. An application is using Amazon RDS but is experiencing a bottleneck with a read-heavy workload. Which is the most optimal solution?
- [ ] A. Increase instance size
- [x] B. Add Read Replica
- [ ] C. Switch to Multi-AZ
- [ ] D. Enable backup

Q33. A video processing pipeline requires: - Very high throughput - Processing in small batches - No need for strict global ordering. Which service should be chosen?
- [ ] A. Amazon SQS FIFO
- [x] B. Amazon SQS Standard
- [ ] C. Amazon Kinesis Data Streams
- [ ] D. Amazon SNS

Q34. A public-facing web server must be accessible from the internet. Which condition makes a subnet a public subnet?
- [ ] A. It contains an EC2 instance with a public IP only
- [x] B. It has a route to an Internet Gateway
- [ ] C. It has a Security Group that allows HTTP
- [ ] D. It is placed in Availability Zone A

Q35. A private application server in a private subnet needs outbound internet access to download updates, but it must not be directly reachable from the internet. Which solution is most appropriate?
- [ ] A. Internet Gateway
- [x] B. NAT Gateway
- [ ] C. Security Group
- [ ] D. Route 53

Q36. A global website needs lower latency and faster delivery of static assets such as images, videos, and HTML by caching content closer to users. Which service is the best choice?
- [ ] A. Amazon Route 53
- [x] B. Amazon CloudFront
- [ ] C. Amazon RDS
- [ ] D. Amazon EC2 Auto Scaling

Q37. A company wants to create an isolated network in AWS that behaves like its own private data center. Which AWS service should be used?
- [ ] A. Amazon Route 53
- [x] B. Amazon VPC
- [ ] C. Amazon CloudFront
- [ ] D. Amazon S3

Q38. A company deploys an Application Load Balancer across two public subnets in different Availability Zones and routes traffic to web servers in private subnets. What is the main benefit of this design?
- [ ] A. It eliminates the need for Security Groups
- [ ] B. It provides direct internet access to private instances
- [x] C. It improves availability and distributes traffic across targets
- [ ] D. It replaces Route 53 completely

Q39. A web application experiences heavy read traffic, causing the primary Amazon RDS for MySQL database to become a performance bottleneck. The architecture also requires automated failover in case of an Availability Zone outage. Which combination of features should a Solutions Architect implement?
- [ ] A. Create a Read Replica in the same AZ and enable Multi-AZ on the Read Replica.
- [ ] B. Enable Multi-AZ on the primary instance and offload read queries to the standby instance.
- [ ] C. Migrate the database to Amazon DynamoDB for infinite read scaling.
- [x] D. Enable Multi-AZ on the primary instance and create one or more Read Replicas to handle the read traffic.

Q40. A financial company requires a database solution with a Recovery Point Objective (RPO) of less than 1 second and a Recovery Time Objective (RTO) of less than 1 minute in the event of a full AWS Region outage. Which service is best suited for this requirement?
- [ ] A. Amazon Redshift cross-region snapshots
- [x] B. Amazon Aurora Global Database
- [ ] C. Amazon RDS with Cross-Region Read Replicas
- [ ] D. Amazon DynamoDB Global Tables

Q41. A gaming company is launching a new multiplayer game that expects highly unpredictable traffic spikes during launch week, followed by a steady but unknown baseline of users. Which Amazon DynamoDB capacity mode is the MOST cost-effective and operationally efficient for this launch?
- [ ] A. Provisioned capacity with maximum read/write capacity units allocated upfront.
- [ ] B. DynamoDB Accelerator (DAX) with minimum provisioned capacity.
- [x] C. On-Demand capacity mode.
- [ ] D. Provisioned capacity with Auto Scaling configured to target 50% utilization.

Q42. A data analytics team needs to run complex, long-running SQL queries combining historical sales data stored in an Amazon S3 data lake with recent transactional data. They want to avoid loading all the S3 data into the database compute nodes. Which AWS service and feature should they use?
- [ ] A. Amazon DynamoDB with Amazon EMR
- [ ] B. Amazon RDS with S3 Select
- [x] C. Amazon Redshift Spectrum
- [ ] D. Amazon Aurora with Federated Query

Q43. A company is migrating its legacy on-premises Oracle database to Amazon Aurora PostgreSQL. The schema structures and stored procedures differ significantly between the two database engines. Which approach should the migration team take?
- [ ] A. Take an Oracle RMAN backup and restore it directly to Amazon Aurora.
- [x] B. Use the AWS Schema Conversion Tool (AWS SCT) to convert the schema and stored objects, then use AWS DMS to migrate the data.
- [ ] C. Use AWS Database Migration Service (AWS DMS) to automatically convert the schema and migrate the data.
- [ ] D. Export data to CSV files and use the Aurora \copy command to import data and schemas.

Q44. An application reads messages from an Amazon SQS Standard queue and processes video files. Processing a video usually takes 3 minutes. However, developers notice that the same video is occasionally being processed multiple times by different worker instances. What is the most likely cause of this issue?
- [x] A. The Visibility Timeout of the SQS queue is set lower than the time required to process the message.
- [ ] B. The SQS queue is configured as a Standard queue instead of a FIFO queue.
- [ ] C. The worker instances are failing to send a ReceiveMessage API call.
- [ ] D. The message retention period is shorter than the processing time.

Q45. A startup wants to build a serverless REST API that automatically scales based on traffic and requires minimal operational overhead. Which AWS services should be used?
- [ ] A. Amazon EC2 + Auto Scaling
- [x] B. Amazon API Gateway + AWS Lambda
- [ ] C. Amazon RDS
- [ ] D. AWS Elastic Beanstalk

Q46. A company wants to store frequently accessed data in memory to reduce database load and improve application performance. Which AWS service is the best fit?
- [ ] A. Amazon DynamoDB
- [x] B. Amazon ElastiCache
- [ ] C. Amazon S3
- [ ] D. Amazon Redshift

Q47. A company wants to analyze log data stored in Amazon S3 using standard SQL queries without managing infrastructure. Which AWS service should they use?
- [x] A. Amazon Athena
- [ ] B. Amazon RDS
- [ ] C. Amazon EC2
- [ ] D. AWS Glue

Q48. A company has two applications running in separate Amazon VPCs in the same region. They need private communication between the VPCs with low latency, no internet exposure, simple setup. Which solution is the best fit?
- [x] A. Use VPC Peering
- [ ] B. Use AWS Transit Gateway
- [ ] C. Use Internet Gateway
- [ ] D. Use AWS Site-to-Site VPN

Q49. What is the defining characteristic of a Public Subnet compared to a Private Subnet?
- [ ] A. It requires a NAT Gateway to allow outbound internet access.
- [ ] B. It does not have a route to the internet at all.
- [x] C. It has a direct route to the internet via an Internet Gateway.
- [ ] D. It is primarily designed to host backend databases and internal APIs.

Q50. According to the presentation, what is the relationship between an AWS Subnet and an Availability Zone (AZ)?
- [ ] A. A single subnet can span across multiple Availability Zones.
- [ ] B. An Availability Zone is a small slice of a subnet's IP range.
- [x] C. A subnet is a slice of your VPC's IP range that lives in a specific Availability Zone.
- [ ] D. A subnet automatically creates new Availability Zones for disaster recovery.

Q51. Which of the following statements is true regarding Security Groups in AWS?
- [ ] A. They operate at the subnet level to control inbound and outbound traffic.
- [ ] B. They are stateless and require explicit rules for return traffic.
- [x] C. They operate at the instance level and are stateful.
- [ ] D. They evaluate network traffic rules strictly in numbered order.

Q52. By default, how do Security Groups handle outbound network traffic?
- [ ] A. They block all outbound traffic completely.
- [ ] B. They allow outbound traffic only to resources located within the same VPC.
- [ ] C. They only allow outbound traffic on standard ports like 80 and 443.
- [x] D. They allow all outbound traffic.

Q53. Which network security feature allows you to create explicit "Deny" rules?
- [ ] A. Security Groups
- [x] B. Network ACLs
- [ ] C. Route Tables
- [ ] D. Internet Gateways

Q54. Which component is required for resources in a Private Subnet to initiate outbound internet traffic?
- [ ] A. Internet Gateway
- [ ] B. Route 53
- [x] C. NAT Gateway
- [ ] D. Bastion Host

Q55. Which AWS service is best suited for running a managed relational database such as MySQL or PostgreSQL without managing the underlying infrastructure?
- [ ] A. Amazon DynamoDB
- [x] B. Amazon RDS
- [ ] C. Amazon SQS
- [ ] D. Amazon SNS

Q56. What is a key difference between Amazon Aurora and standard Amazon RDS database engines?
- [ ] A. Aurora is a messaging service for event-driven systems
- [x] B. Aurora is AWS's proprietary high-performance relational database compatible with MySQL and PostgreSQL
- [ ] C. Aurora is a NoSQL database designed for millisecond latency at any scale
- [ ] D. Aurora is used only for data warehousing

Q57. Which AWS database service is fully managed, NoSQL, and designed for single-digit millisecond performance at scale?
- [ ] A. Amazon Redshift
- [ ] B. Amazon Aurora
- [x] C. Amazon DynamoDB
- [ ] D. Amazon RDS for SQL Server

Q58. In the CIDR notation 174.16.0.0/24, how many IP addresses are available in total?
- [ ] A. 65536
- [x] B. 256
- [ ] C. 16
- [ ] D. 16.7 million

Q59. A company wants to host a backend database that should NOT be accessible from the internet. Which subnet type is most suitable?
- [ ] A. Internet Gateway Subnet
- [ ] B. Edge Location
- [x] C. Private Subnet
- [ ] D. Public Subnet

Q60. Which component is required to allow resources in a public subnet to communicate with the internet?
- [ ] A. Customer Gateway
- [x] B. Internet Gateway
- [ ] C. Virtual Private Gateway
- [ ] D. NAT Gateway

Q61. What is the primary difference between a Security Group and a Network ACL (NACL)?
- [x] A. Security Groups support "Allow" rules only; NACLs support both "Allow" and "Deny" rules
- [ ] B. Security Groups are stateless; NACLs are stateful
- [ ] C. Security Groups work at the subnet level; NACLs work at the instance level
- [ ] D. There is no functional difference; they are redundant services

Q62. When configuring a Security Group for your Web Server in the Lab, what should you 'Allow' to ensure the Application Load Balancer (ALB) can reach it?
- [ ] A. All outbound traffic to the VPC CIDR
- [ ] B. SSH traffic from the Internet
- [x] C. HTTP traffic from the Security Group ID of the ALB
- [ ] D. HTTP traffic from source 0.0.0.0/0

Q63. A web application is hosted on EC2 instances in a Private Subnet. You have successfully created a NAT Gateway in a Public Subnet. However, the instances still cannot access the internet to download updates. What is the most likely missing step?
- [ ] A. The EC2 instances do not have a Public IP address assigned.
- [x] B. The Route Table associated with the Private Subnet does not have a route pointing 0.0.0.0/0 to the NAT Gateway.
- [ ] C. The Security Group of the NAT Gateway is blocking inbound traffic from the Private Subnet
- [ ] D. The NAT Gateway needs to be attached to an Internet Gateway directly.

Q64. You have two VPCs (VPC A and VPC B) in the same region. You want instances in VPC A to communicate with instances in VPC B using private IP addresses. Which AWS feature should you implement?
- [ ] A. NAT Gateway
- [x] B. VPC Peering
- [ ] C. Internet Gateway
- [ ] D. AWS CloudFront

Q65. You want to perform a "Blue/Green" deployment where you shift 10% of your traffic to a new version of your application to test stability. Which Route 53 policy is most suitable?
- [ ] A. Simple Routing Policy.
- [x] B. Weighted Routing Policy
- [ ] C. Failover Routing Policy.
- [ ] D. Latency Routing Policy.

Q66. A security admin wants to prevent a specific range of malicious IP addresses from even reaching the subnets in a VPC. Which tool provides this 'Deny' capability at the network boundary?
- [x] A. Network ACLs
- [ ] B. Security Groups
- [ ] C. Application Load Balancer
- [ ] D. NAT Gateway

Q67. A solutions architect is troubleshooting a connectivity issue. An EC2 instance in a public subnet can reach the internet, but an instance in the private subnet cannot, even though a NAT Gateway is present. What is the most likely cause?
- [ ] A. The instance is missing an Elastic IP address
- [x] B. The NAT Gateway is located in the private subnet
- [ ] C. The Route Table for the private subnet points 0.0.0.0/0 to the NAT Gateway
- [ ] D. The private instance does not have a public IP address

Q68. Which of the following can be described as a global content delivery network (CDN) service?
- [ ] A. AWS VPN
- [ ] B. AWS Direct Connect
- [ ] C. AWS Regions
- [x] D. Amazon CloudFront

Q69. What is the AWS service that provides a virtual network dedicated to your AWS account?
- [ ] A. AWS VPN
- [ ] B. AWS Subnets
- [ ] C. AWS Dedicated Hosts
- [x] D. Amazon VPC

Q70. You are working on two projects that require completely different network configurations. Which AWS service or feature will allow you to isolate resources and network configurations?
- [ ] A. Internet Gateways
- [x] B. Virtual Private Cloud (VPC)
- [ ] C. Security Groups
- [ ] D. Amazon CloudFront

Q71. Which term below has the role of simplifying routing by auto-adding VPN routes?
- [x] A. Propagation
- [ ] B. Edge Association
- [ ] C. Local Route
- [ ] D. Destination

Q72. Which of the below options is true of Amazon VPC?
- [ ] A. Amazon VPC allows customers to control user interactions with all other AWS resources
- [x] B. AWS Customers have complete control over their Amazon VPC virtual networking environment
- [ ] C. AWS is responsible for all the management and configuration details of Amazon VPC
- [ ] D. Amazon VPC helps customers to review their AWS architecture and adopt best practices

Q73. Which feature below does not belong to Private Subnet?
- [x] A. No requirement of NAT Gateway Usage for internet access
- [ ] B. Not directly accessible from the internet
- [ ] C. Route table does not include a route to the Internet Gateway
- [ ] D. Used for Databases, Internal Application Servers, or Batch Processing

Q74. A developer is planning to build a two-tier web application that has a MySQL database layer. Which of the following AWS database services would provide automated backups for the application?
- [ ] A. A MySQL database installed on an EC2 instance
- [ ] B. Amazon DynamoDB
- [x] C. Amazon Aurora
- [ ] D. Amazon Neptune

Q75. Which service is best for storing common database query results, which helps to alleviate database access load?
- [ ] A. Amazon Machine Learning
- [ ] B. Amazon SQS
- [x] C. Amazon ElastiCache
- [ ] D. Amazon EC2 Instance Store

Q76. Amazon Relational Database Service (Amazon RDS) offers which of the following benefits over traditional database management?
- [ ] A. AWS manages the data stored in Amazon RDS tables
- [x] B. AWS manages the maintenance of the operating system
- [ ] C. AWS automatically scales up instance types on demand
- [ ] D. AWS manages the database type

Q77. What is one of the advantages of the Amazon Relational Database Service (Amazon RDS)?
- [x] A. It simplifies relational database administration tasks
- [ ] B. It provides 99.99% reliability and durability
- [ ] C. It automatically scales databases for loads
- [ ] D. It enabled users to dynamically adjust CPU and RAM resources

Q78. A company wants to run a relational database in AWS without managing most of the underlying operational work. Which service best fits this need?
- [ ] A. Amazon EC2
- [x] B. Amazon RDS
- [ ] C. AWS Lambda
- [ ] D. Amazon VPC

Q79. A team wants a relational database service in AWS that is designed for high availability and runs in a VPC with multiple subnets across Availability Zones. Which service is the best fit?
- [x] A. Amazon Aurora
- [ ] B. Amazon SQS
- [ ] C. Amazon Route 53
- [ ] D. Amazon CloudFront

Q80. Which statement about subnets is correct?
- [ ] A. A subnet can span multiple AWS Regions
- [ ] B. A subnet can span multiple Availability Zones
- [x] C. A subnet must reside in one Availability Zone
- [ ] D. A subnet is used only for databases

Q81. Which option describes a customer responsibility when designing a VPC for databases?
- [x] A. Choosing IP address ranges and subnets
- [ ] B. Maintaining AWS data centers
- [ ] C. Replacing failed physical servers
- [ ] D. Managing the AWS global backbone network

Q82. How does Amazon Aurora Database Cloning differ from a traditional snapshot-and-restore approach?
- [ ] A. Cloning requires a full copy of all data at creation time, making it slower but more reliable
- [x] B. Cloning uses a copy-on-write protocol, sharing the same storage volume initially, making it much faster and cost-efficient
- [ ] C. Cloning creates an independent storage volume immediately, which doubles the storage cost
- [ ] D. Cloning is only available for cross-region duplication and cannot be used within the same region

Q83. A company runs a production MySQL database on Amazon RDS that handles heavy read/write traffic. They now need to run complex analytics and reporting queries without impacting production performance. Additionally, they want to ensure the database remains available even if an entire Availability Zone fails. Which combination of RDS features should they implement?
- [ ] A. Enable Multi-AZ deployment for read scaling, and use RDS Proxy for analytics queries
- [x] B. Create a Read Replica for the analytics workload, and enable Multi-AZ deployment for high availability
- [ ] C. Enable Aurora Serverless for analytics, and use ElastiCache for high availability
- [ ] D. Create multiple Read Replicas in the same AZ for both analytics and disaster recovery

Q84. Which disaster recovery strategy has the lowest RTO (Recovery Time Objective) and RPO (Recovery Point Objective) by keeping a fully functional copy of the environment running in another region?
- [ ] A. Pilot Flight
- [ ] B. Warm Standby
- [x] C. Multi-site (Active-Active)
- [ ] D. Backup and Restore

Q85. How many copies of your data does Aurora automatically replicate across Availability Zones?
- [x] A. 6 copies across 3 AZs
- [ ] B. 1 copy per AZ in every region
- [ ] C. 3 copies in a single AZ
- [ ] D. 2 copies across 2 AZs

Q86. When migrating an on-premises database to AWS, which service helps you migrate data quickly and securely while the source database remains operational?
- [ ] A. AWS Snowball
- [x] B. AWS Database Migration Service (AWS DMS)
- [ ] C. AWS DataSync
- [ ] D. AWS Elastic File System (EFS)

Q87. Which RDS feature provides high availability and automatic failover by maintaining a synchronous secondary copy of the database in a different Availability Zone?
- [ ] A. Database Snapshots
- [x] B. Multi-AZ Deployment
- [ ] C. Read Replicas
- [ ] D. RDS Proxy

Q88. A student is learning about managed database services on AWS. Which service is specifically designed to manage relational databases and automate tasks like backups and patching?
- [ ] A. Amazon SQS for messaging between distributed applications.
- [x] B. Amazon RDS for managing relational database instances.
- [ ] C. Amazon SNS for broadcasting messages to subscribers.
- [ ] D. Amazon S3 for storing unstructured object data.

Q89. Which of the following database engines is not currently supported by Amazon RDS?
- [ ] A. PostgreSQL
- [ ] B. MariaDB
- [x] C. MongoDB
- [ ] D. IBM DB2

Q90. When using Amazon SQS, what happens to a message after a consumer retrieves it from the queue, but before it is explicitly deleted?
- [ ] A. The message is immediately removed from the queue to prevent duplicate processing.
- [ ] B. The message remains visible to all other consumers immediately.
- [x] C. The message enters a visibility timeout period where it is hidden from other consumers.
- [ ] D. The message is moved to a Dead Letter Queue (DLQ) automatically.

Q91. Which AWS service is used to send one message to multiple subscribers using a publish/subscribe model?
- [ ] A. Amazon SQS
- [x] B. Amazon SNS
- [ ] C. Amazon RDS
- [ ] D. Amazon ElastiCache

Q92. An e-commerce application experiences heavy read traffic during sales events. The primary database becomes a bottleneck, but write operations must remain consistent. What is the best solution?
- [ ] A. Enable Multi-AZ deployment to distribute read traffic.
- [ ] B. Replace RDS with SQS to queue database operations.
- [ ] C. Use SNS to broadcast database queries to all services.
- [x] D. Create Read Replicas and redirect read queries there.

Q93. What is the fundamental difference in replication mechanism between RDS Read Replicas and RDS Multi-AZ?
- [ ] A. Read Replicas uses synchronous replication (SYNC), while Multi-AZ uses asynchronous replication (ASYNC).
- [ ] B. Both features use synchronous replication (SYNC) to ensure no data loss.
- [x] C. Read Replicas uses asynchronous replication (ASYNC), while Multi-AZ uses synchronous replication (SYNC).
- [ ] D. Read Replicas only supports replication within the same Availability Zone, while Multi-AZ supports regional replication.

Q94. A developer needs to ensure that a single event, such as 'New Order', is delivered to multiple independent downstream applications, and that each application receives its own copy of the event for separate processing. Which AWS architecture is most appropriate?
- [ ] A. Use a single SQS queue that all processing applications poll from.
- [x] B. Use an SNS topic to publish the event, with multiple SQS queues subscribed to that topic.
- [ ] C. Use RDS Proxy to broadcast the event to multiple database tables.
- [ ] D. Use ElastiCache Redis to store the event and have applications check for updates.

Q95. Which statement is correct about Amazon SQS Standard Queue?
- [ ] A. It guarantees strict message ordering
- [ ] B. It can send only one message at a time
- [x] C. A message may be delivered more than once
- [ ] D. It can only be used with EC2, not with Lambda

Q96. A company needs to build an order processing system where, whenever a new order is placed, information needs to be sent simultaneously to three independent systems: Warehouse, Accounting, and Shipping. Which AWS service is best suited for implementing this model?
- [ ] A. Amazon ElastiCache
- [x] B. Amazon SNS
- [ ] C. AWS Database Migration Service (DMS)
- [ ] D. Amazon SQS

Q97. A learner is studying DNS and wants to understand its main job in web access. What is the main purpose of DNS?
- [ ] A. It translates private keys into IAM policies
- [x] B. It translates domain names into IP addresses
- [ ] C. It translates packets into cached objects
- [ ] D. It translates routes into subnet addresses

Q98. Which AWS service is a fully managed relational database service that supports engines such as MySQL, PostgreSQL, Oracle, and SQL Server?
- [ ] A. Amazon DynamoDB
- [x] B. Amazon RDS
- [ ] C. Amazon ElastiCache
- [ ] D. Amazon Redshift

Q99. What type of replication do RDS Read Replicas use?
- [ ] A. Synchronous (SYNC)
- [x] B. Asynchronous (ASYNC)
- [ ] C. Semi-synchronous
- [ ] D. Real-time streaming

Q100. What is the primary purpose of RDS Multi-AZ deployment?
- [ ] A. Improve read performance by distributing queries
- [x] B. Provide disaster recovery and high availability
- [ ] C. Reduce storage costs
- [ ] D. Enable cross-region data access

Q101. How many copies of data does Amazon Aurora store, and across how many Availability Zones?
- [ ] A. 3 copies across 2 AZs
- [ ] B. 4 copies across 2 AZs
- [x] C. 6 copies across 3 AZs
- [ ] D. 9 copies across 3 AZs

Q102. Which workload type is Aurora Serverless best suited for?
- [ ] A. Stable, predictable workloads
- [x] B. Infrequent or unpredictable workloads
- [ ] C. Workloads requiring sustained high performance
- [ ] D. Write-heavy OLTP workloads only

Q103. Which caching engines does Amazon ElastiCache support?
- [ ] A. MySQL and PostgreSQL
- [x] B. Redis and Memcached
- [ ] C. MongoDB and Cassandra
- [ ] D. DynamoDB and DocumentDB

Q104. Which ElastiCache engine supports Multi-AZ with Auto-Failover and data persistence?
- [ ] A. Memcached only
- [x] B. Redis only
- [ ] C. Both Redis and Memcached
- [ ] D. Neither

Q105. What delivery behavior does an Amazon SQS Standard Queue provide?
- [ ] A. Exactly-once delivery with strict ordering
- [x] B. At-least-once delivery with best-effort ordering
- [ ] C. At-most-once delivery with FIFO ordering
- [ ] D. Exactly-once delivery with no ordering guarantee

Q106. What communication model does Amazon SNS use?
- [ ] A. Point-to-point queue model
- [ ] B. Streaming model
- [x] C. Publish/Subscribe (Pub/Sub) model
- [ ] D. Request/Response model

Q107. Which disaster recovery strategy provides the fastest RTO but at the highest cost?
- [ ] A. Backup and Restore
- [ ] B. Pilot Light
- [ ] C. Warm Standby
- [x] D. Multi Site / Hot Site

Q108. Which AWS service or tool can be used to set up a firewall to control traffic going into and coming out of an Amazon VPC subnet?
- [ ] A. Security group
- [ ] B. AWS WAF
- [ ] C. AWS Firewall Manager
- [x] D. Network ACL

Q109. A company needs stateless network filtering for its VPC. Which AWS service, tool, or feature will meet this requirement?
- [ ] A. AWS PrivateLink
- [ ] B. Security group
- [x] C. Network access control list (ACL)
- [ ] D. AWS WAF

Q110. To reduce costs, a company is planning to migrate a NoSQL database to AWS. Which AWS service is fully managed and can automatically scale throughput capacity to meet database workload demands?
- [ ] A. Amazon Redshift
- [ ] B. Amazon Aurora
- [x] C. Amazon DynamoDB
- [ ] D. Amazon RDS

Q111. Which networking component acts as a firewall for associated subnets, controlling both inbound and outbound traffic at the subnet level?
- [ ] A. NAT Gateway
- [ ] B. Internet Gateway
- [ ] C. Security Group
- [x] D. Network Access Control List (NACL)

Q112. You are designing a Hub-and-Spoke architecture with 50 VPCs that need to communicate with a central hub. You want to allow these VPCs to communicate with each other without creating hundreds of individual Peering connections. Which AWS service is the most optimal solution?
- [ ] A. AWS VPC Endpoint Services (PrivateLink)
- [x] B. AWS Transit Gateway
- [ ] C. Full-mesh VPC Peering
- [ ] D. AWS Software VPN

Q113. A company has an Amazon EC2 instance in a private subnet. The company wants to initiate a connection to the internet to pull operating system updates while preventing traffic from the internet from accessing the EC2 instance. Which AWS service or feature should the engineer use to simplify and scale this connectivity as the VPCs increase in number?
- [ ] A. VPC endpoint
- [x] B. NAT gateway
- [ ] C. Amazon PrivateLink
- [ ] D. VPC peering

Q114. A company wants to securely access an Amazon S3 bucket from an Amazon EC2 instance without accessing the internet. What should the company use to accomplish this goal?
- [ ] A. VPN connection
- [ ] B. Internet gateway
- [x] C. VPC endpoint
- [ ] D. NAT gateway

Q115. A network engineer needs to build a hybrid cloud architecture connecting on-premises networks to the AWS Cloud using AWS Direct Connect. The company has a few VPCs in a single AWS Region and expects to increase the number of VPCs to hundreds over time. Which AWS service or feature should the engineer use to simplify and scale this connectivity as the VPCs increase in number?
- [ ] A. VPC endpoints
- [x] B. AWS Transit Gateway
- [ ] C. Amazon Route 53
- [ ] D. Amazon Route 53 D. AWS Secrets Manager

Q116. Which of the following AWS database services is best described as an in-memory data store used to improve application response time?
- [ ] A. Amazon DynamoDB
- [ ] B. Amazon RDS
- [x] C. Amazon ElastiCache
- [ ] D. Amazon Redshift

Q117. What type of replication does Amazon RDS Multi-AZ use between the primary and standby instance?
- [ ] A. Asynchronous replication to minimize latency
- [x] B. Synchronous replication to ensure data consistency
- [ ] C. Eventual consistency replication
- [ ] D. Snapshot-based replication every 5 minutes

Q118. A web application is experiencing high latency due to read-heavy traffic on its primary Amazon RDS database. The development team wants to implement an in-memory caching layer to reduce the load on the database and improve response times. Which AWS service is the best choice for this use case?
- [ ] A. Amazon S3
- [ ] B. Amazon SQS
- [x] C. Amazon ElastiCache
- [ ] D. Amazon Aurora Serverless

Q119. An architecture includes a front-end web application and a back-end processing application. Traffic spikes frequently cause the tightly coupled back-end to become overwhelmed and fail. Which AWS service can be used to decouple these applications and asynchronously store messages until the back-end is ready to process them?
- [ ] A. Amazon SNS
- [x] B. Amazon SQS
- [ ] C. Amazon ElastiCache
- [ ] D. Amazon API Gateway

Q120. Which of the following is a characteristic of AWS Security Groups?
- [ ] A. They operate at the subnet level.
- [ ] B. They support both "Allow" and "Deny" rules.
- [ ] C. They are stateless and require explicit rules for both inbound and outbound return traffic.
- [x] D. They are stateful, meaning they automatically allow return traffic.

Q121. A company needs to migrate its on-premises Oracle database to an Amazon Aurora PostgreSQL-compatible cluster. They require the source database to remain fully operational during the migration and need to convert the database schema before moving the data. Which combination of AWS tools should they use?
- [ ] A. AWS Snowball and Amazon S3
- [ ] B. AWS Backup and Amazon RDS Snapshot
- [x] C. AWS Schema Conversion Tool (SCT) and AWS Database Migration Service (DMS)
- [ ] D. Amazon RDS Proxy and AWS Lambda

Q122. A media company wants to collect and store large-scale, real-time streaming data from IoT devices for advanced analytics. They need the ability to "replay" or reprocess the data for up to 365 days if necessary. Which service should they choose?
- [ ] A. Amazon Data Firehose
- [ ] B. Amazon SQS FIFO Queue
- [x] C. Amazon Kinesis Data Streams
- [ ] D. Amazon MQ

Q123. Which of the following is NOT a supported database engine in Amazon RDS?
- [ ] A. PostgreSQL
- [ ] B. MySQL
- [x] C. MongoDB
- [ ] D. Oracle

Q124. An EC2 instance is launched in a private subnet and needs to download updates from the internet, but must not be directly reachable from the internet. Which solution should be used?
- [ ] A. Attach an Internet Gateway to the subnet
- [x] B. Use a NAT Gateway in a public subnet and update the route table
- [ ] C. Assign a public IP address to the instance
- [ ] D. Use a VPC Peering connection

Q125. Which statement correctly describes the difference between Security Groups and Network ACLs?
- [ ] A. Security Groups are stateless, while NACLs are stateful
- [ ] B. Security Groups and NACLs are both stateless
- [x] C. Security Groups are stateful, while NACLs are stateless
- [ ] D. Both Security Groups and NACLs are stateful

Q126. A packet is allowed by a Security Group but denied by a Network ACL. What happens?
- [ ] A. Allowed (Security Group wins)
- [ ] B. Allowed (first match wins)
- [x] C. Denied
- [ ] D. Depends on subnet type

Q127. A cloud engineer has deployed several backend database instances in a private subnet within a VPC. These instances need to securely download software patches from the internet, but they must not be directly accessible from the public internet. Which AWS component is required to allow this outbound traffic?
- [ ] A. Internet Gateway
- [x] B. NAT Gateway
- [ ] C. Network ACL
- [ ] D. Route 53

Q128. What is the primary difference between a Public Subnet and a Private Subnet in an AWS VPC?
- [x] A. A Public Subnet has a route table connected directly to an Internet Gateway, while a Private Subnet does not.
- [ ] B. A Private Subnet can be accessed directly from the Internet, while a Public Subnet cannot.
- [ ] C. Public Subnets only support IPv4, while Private Subnets only support IPv6.
- [ ] D. A Public Subnet is always located in the first Availability Zone (AZ), while Private Subnets are in the others.

Q129. In Amazon RDS, which feature is primarily designed for High Availability and Disaster Recovery rather than read scaling?
- [ ] A. Read Replicas
- [x] B. Multi-AZ Deployment
- [ ] C. RDS Proxy
- [ ] D. Vertical Scaling

Q130. Which of the following engines are supported by Amazon ElastiCache?
- [ ] A. MySQL and PostgreSQL
- [ ] B. Oracle and MariaDB
- [x] C. Redis and Memcached
- [ ] D. DynamoDB and MongoDB

Q131. Which component in the AWS network security model acts as a firewall for Subnets (Subnet-level) and supports both "Allow" and "Deny" rules?
- [ ] A. Security Groups
- [ ] B. Internet Gateway
- [ ] C. Route Table
- [x] D. Network ACLs (NACL)

Q132. Which of the following is a key benefit of using Amazon SQS (Simple Queue Service) in system integration?
- [ ] A. It enables real-time, synchronous communication between services.
- [x] B. It allows for the "decoupling" of application components to improve scalability.
- [ ] C. It automatically sends email notifications to customers when a new message arrives.
- [ ] D. It stores data permanently until the user manually deletes it.

Q133. A company runs a read-heavy analytics workload that is overloading its Amazon RDS production database. Which solution should a cloud architect recommend to offload the read traffic while keeping the production database unaffected?
- [ ] A. Enable Multi-AZ deployment on the RDS instance
- [x] B. Create an RDS Read Replica and direct analytics queries to it
- [ ] C. Increase the RDS instance size to handle more connections
- [ ] D. Enable RDS Storage Auto Scaling to expand capacity

Q134. Which Amazon S3 storage class replicates data within a single Availability Zone and is NOT resilient to the physical loss of an entire AZ?
- [ ] A. Glacier Deep Archive
- [x] B. One Zone-IA
- [ ] C. Intelligent-Tiering
- [ ] D. Standard-IA

Q135. A company wants to host its public-facing web servers while keeping its database servers completely isolated from the internet. Which AWS VPC architecture best satisfies this requirement?
- [ ] A. Place all servers in a single public subnet and use Security Groups to block database traffic
- [x] B. Place web servers in a public subnet and database servers in a private subnet within the same VPC
- [ ] C. Create two separate VPCs: one for web servers and one for databases
- [ ] D. Place all servers in a private subnet and attach an Internet Gateway directly to each EC2 instance

Q136. A developer in a private subnet needs to download OS security patches from the internet, but the company policy forbids assigning public IP addresses to backend servers. Which AWS service enables this outbound-only internet access?
- [ ] A. Internet Gateway (IGW)
- [ ] B. VPC Peering
- [ ] C. AWS Direct Connect
- [x] D. NAT Gateway

Q137. A global e-commerce company wants to reduce latency for users worldwide when they access static content such as images and videos stored in Amazon S3. Which AWS service is the MOST appropriate solution?
- [x] A. Amazon CloudFront
- [ ] B. AWS Global Accelerator
- [ ] C. AWS Route 53 with latency-based routing
- [ ] D. Elastic Load Balancing (ELB)

Q138. A company is looking at real-time processing of streaming big data for their ad-tech platform. Which of the following AWS services is the right choice for this requirement?
- [x] A. Amazon Kinesis Data Streams
- [ ] B. Amazon Simple Queue Service (Amazon SQS)
