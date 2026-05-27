### AWS Cloud Practitioner Practice Questions - Part 2

Q1. A user needs to automatically discover, classify, and protect sensitive data stored in Amazon S3. Which AWS service can meet these requirements?
- [ ] A. Amazon Inspector
- [ ] B. Amazon Macie
- [ ] C. Amazon GuardDuty
- [ ] D. AWS Secrets Manager

Q2. What kind of database is Amazon DynamoDB?
- [ ] A. Document database
- [ ] B. Relational database
- [ ] C. NoSQL database
- [ ] D. Graph database

Q3. Which Amazon S3 storage class has the lowest cost?
- [ ] A. S3 Intelligent-Tiering
- [ ] B. S3 Standard
- [ ] C. S3 Glacier Deep Archive
- [ ] D. S3 One Zone-IA

Q4. What is AWS EFS?
- [ ] A. AWS Elastic File System
- [ ] B. AWS Efficient File System
- [ ] C. AWS Enterprise File System
- [ ] D. AWS External File Storage

Q5. Economies of scale continually reduce AWS Cloud pricing.
- [ ] A. False
- [ ] B. True
- [ ] C. Only for enterprise customers
- [ ] D. Only for storage services

Q6. Which tool lets you visualize and manage your AWS costs?
- [ ] A. AWS Cost Explorer
- [ ] B. AWS Budgets
- [ ] C. AWS Price Calculator
- [ ] D. AWS Billing Dashboard

Q7. Which service lets you run code without managing servers?
- [ ] A. AWS ECS
- [ ] B. AWS Lambda
- [ ] C. Amazon EC2 Auto Scaling
- [ ] D. AWS Fargate

Q8. Which AWS service provides a history of application data changes with immutability?
- [ ] A. AWS Quantum Ledger Database
- [ ] B. AWS Neptune
- [ ] C. Amazon DocumentDB
- [ ] D. AWS ElastiCache

Q9. What is Amazon DynamoDB Accelerator (DAX) capable of?
- [ ] A. Improves visualization of graphs
- [ ] B. Improves write performance
- [ ] C. Improves read performance of NoSQL data
- [ ] D. Improves relational queries

Q10. A development team has multiple Linux-based EC2 instances across different Availability Zones that need concurrent read/write access to a shared, POSIX-compliant file system. The system must be highly available, automatically scale, and require no management of underlying servers. Which storage service is the most appropriate?
- [ ] A. Amazon Elastic Block Store (Amazon EBS)
- [ ] B. Amazon Elastic File System (Amazon EFS)
- [ ] C. Amazon FSx for Windows File Server
- [ ] D. Amazon S3

Q11. Which of the following Amazon S3 storage classes has NO constraint on a minimum storage duration charge for objects?
- [ ] A. Amazon S3 Standard- Infrequent Access (S3 Standard- IA)
- [ ] B. Amazon S3 One Zone- Infrequent Access (S3 One Zone-IA)
- [ ] C. Amazon S3 Glacier Flexible Retrieval
- [ ] D. Amazon S3 Standard

Q12. A real-time stock trading platform needs a load balancer that can handle millions of TCP requests per second with ultra-low latency. Which ELB should they choose?
- [ ] A. Application Load Balancer
- [ ] B. Network Load Balancer
- [ ] C. Gateway Load Balancer
- [ ] D. Classic Load Balancer

Q13. Which EBS volume type supports Multi-Attach, allowing it to be attached to multiple EC2 instances simultaneously?
- [ ] A. Cold HDD (sc1)
- [ ] B. General Purpose SSD (gp2/ gp3)
- [ ] C. Throughput Optimized HDD (st1)
- [ ] D. Provisioned IOPS SSD (io1/io2)

Q14. Which feature eliminates the initial read latency when accessing a newly restored EBS volume from a snapshot?
- [ ] A. EBS Multi-Attach
- [ ] B. EBS Snapshot Archive
- [ ] C. Provisioned IOPS
- [ ] D. Fast Snapshot Restore (FSR)

Q15. What is Amazon EBS primarily used for?
- [ ] A. Hosting static websites.
- [ ] B. Creating a highly scalable data lake.
- [ ] C. Providing Block Storage volumes for Amazon EC2 instances.
- [ ] D. Archiving compliance logs for 10 years.

Q16. A company needs to physically migrate 50 Petabytes of data from their local data center to AWS because transferring it over their internet connection would take several years. Which service is designed for this?
- [ ] A. AWS Storage Gateway
- [ ] B. AWS Snowball Edge
- [ ] C. AWS Snowmobile
- [ ] D. AWS Direct Connect

Q17. A startup wants to store secondary backup copies of data that can be easily recreated if lost at the absolute lowest cost possible, without needing high resilience. Which storage class is best?
- [ ] A. Amazon S3 Standard
- [ ] B. Amazon S3 One Zone-IA
- [ ] C. Amazon S3 Standard-IA
- [ ] D. Amazon S3 Intelligent-Tiering

Q18. A global corporation has a predictable baseline of compute usage across multiple AWS Regions. They use a mix of EC2 instances, AWS Lambda, and AWS Fargate. Which purchasing model provides the highest level of flexibility to cover all these services?
- [ ] A. Standard Reserved Instances
- [ ] B. EC2 Instance Savings Plans
- [ ] C. Compute Savings Plans
- [ ] D. Regional Reserved Instances

Q19. A solutions architect is designing a system for a tightly coupled scientific simulation that requires extremely low-latency communication between nodes using a Cluster Placement Group. What is a true limitation of this strategy?
- [ ] A. It cannot span across multiple Availability Zones
- [ ] B. It is limited to a maximum of 7 instances per Region
- [ ] C. It requires the use of Dedicated Hosts for all instances.
- [ ] D. It only supports T-series instance types

Q20. Which Amazon EFS storage class offers the lowest "first byte read latency"?
- [ ] A. EFS Standard
- [ ] B. EFS Infrequent Access (IA)
- [ ] C. EFS Archive
- [ ] D. They all have the same latency.

Q21. A developer is using an AWS Lambda function to process large video files uploaded to S3. The function consistently takes 18 minutes to complete the processing. To ensure the function finishes successfully, which action should be taken?
- [ ] A. Increase the Memory (RAM) allocation to the maximum (10GB) to provide more CPU power.
- [ ] B. Change the Timeout setting in the Lambda configuration to 20 minutes
- [ ] C. Migrate the workload to Amazon EC2 or AWS Fargate.
- [ ] D. Enable Provisioned Concurrency to keep the function "warm" for longer processing.

Q22. You are using an Amazon EBS Volume (General Purpose SSD) attached to an EC2 instance in Availability Zone (AZ) us-east-1a. There is a major power outage that takes down the entire us-east-1a zone. How can you access your data in another zone (us-east-1b)?
- [ ] A. EBS is a Regional service, so you can simply attach the volume to a new instance in us-east-1b.
- [ ] B. You cannot; EBS volumes are tied to a specific AZ. You must restore the data from a snapshot.
- [ ] C. AWS automatically replicates EBS volumes across all AZs in a Region for high availability.
- [ ] D. Use S3 Transfer Acceleration to move the EBS data to the new zone.

Q23. What is an Amazon Machine Image (AMI) primarily used for?
- [ ] A. To automatically scale EC2 resources
- [ ] B. To provide a preconfigured template to launch EC2 instances
- [ ] C. To distribute network traffic across instances
- [ ] D. To provide network-attached storage for EC2

Q24. Which feature allows you to run a startup script automatically when an EC2 instance first boots?
- [ ] A. Auto Scaling Groups
- [ ] B. AWS Step Functions
- [ ] C. EC2 User Data
- [ ] D. Elastic Network Interfaces

Q25. Which EC2 purchasing option allows you to use spare AWS capacity at up to a ~90% discount, but can be interrupted with a 2-minute notice?
- [ ] A. Spot Instances
- [ ] B. Eco Plans
- [ ] C. Savings Instances
- [ ] D. Savings Plans

Q26. What is the maximum number of instances per Availability Zone allowed in a Spread Placement Group?
- [ ] A. 3
- [ ] B. 5
- [ ] C. 7
- [ ] D. Based on developer's settings

Q27. What is the default termination behavior for the root EBS volume when an EC2 instance is terminated?
- [ ] A. It is kept and must be manually deleted.
- [ ] B. It is automatically backed up to a snapshot, then deleted.
- [ ] C. It is automatically deleted.
- [ ] D. It is moved to the Recycle Bin.

Q28. Which EBS volume type provides the lowest-cost storage option and is designed specifically for infrequently accessed data?
- [ ] A. Provisioned IOPS SSD (io1/io2)
- [ ] B. Throughput Optimized HDD (st1)
- [ ] C. General Purpose SSD (gp2/gp3)
- [ ] D. Cold HDD (sc1)

Q29. In order to use the EC2 Hibernate feature, which requirement must be met for the root volume?
- [ ] A. The root volume must be stored on an Instance Store.
- [ ] B. The root volume must be an encrypted Amazon EBS volume.
- [ ] C. The root volume must be detached before hibernating.
- [ ] D. The root volume must be backed by an EFS file system.

Q30. Which OSI layer does the Application Load Balancer (ALB) operate at in AWS Structure?
- [ ] A. Layer 3
- [ ] B. Layer 4
- [ ] C. Layer 7
- [ ] D. Layer 2

Q31. Which EC2 pricing option provides the lowest cost but can be interrupted?
- [ ] A. On-Demand Instances
- [ ] B. Dedicated Hosts
- [ ] C. Reserved Instances
- [ ] D. Spot Instances

Q32. What does horizontal scaling (scale out) mean?
- [ ] A. Adding more instances to handle load
- [ ] B. Increasing CPU and RAM of one instance
- [ ] C. Reducing storage size
- [ ] D. Moving to a different region

Q33. Which statement best describes AWS Lambda?
- [ ] A. Requires manual server provisioning
- [ ] B. Runs continuously like EC2
- [ ] C. Executes code in response to events
- [ ] D. Only supports Java

Q34. Which of the following workload types is least suited for Reserved Instances?
- [ ] A. Long-term workloads
- [ ] B. Batch jobs
- [ ] C. Permanent workloads
- [ ] D. Non-changing workloads

Q35. A European bank with a stable customer base needs a database server running 24/7. They need a specific EC2 configuration, want to save costs while ensuring high availability. Which EC2 pricing model is most appropriate?
- [ ] A. On-Demand Instances
- [ ] B. Reserved Instances
- [ ] C. Savings Plans
- [ ] D. Spot Instances

Q36. Which of the following is not a valid EC2 instance type?
- [ ] A. Data Lake Optimized
- [ ] B. General Purpose
- [ ] C. Compute Optimized
- [ ] D. Memory Optimized

Q37. What is statement is WRONG about EBS and EFS file systems?
- [ ] A. EFS works across multiple AZs.
- [ ] B. EBS can be mounted by only one EC2 instance.
- [ ] C. Both are only compatible with Linux-based AMIs.
- [ ] D. EFS can be mounted by multiple EC2 instances simultaneously.

Q38. A company plans to host its database on one or more EC2 instances to store persistent transaction data. Which storage option is not suitable for this use case?
- [ ] A. Elastic File System
- [ ] B. Instance Store
- [ ] C. Elastic Block Store
- [ ] D. None

Q39. Which AWS service provides virtual servers in the cloud?
- [ ] A. Amazon S3
- [ ] B. Amazon EC2
- [ ] C. AWS Lambda
- [ ] D. Amazon RDS

Q40. A company with no remote offices wants to host an internal website that is used only during business hours. Which EC2 purchasing option is most suitable?
- [ ] A. On-Demand
- [ ] B. Reserved Instances
- [ ] C. Spot Instances
- [ ] D. Savings Plans

Q41. A retail company expects unpredictable traffic spikes during a flash sale. They need to automatically add servers to handle demand and remove them afterward to save costs
- [ ] A. Spot Instances and Placement Groups
- [ ] B. Auto Scaling Group (ASG) and Elastic Load Balancing (ELB)
- [ ] C. Reserved Instances and CloudWatch
- [ ] D. Dedicated Hosts

Q42. A biotech startup needs high parallel processing power for complex genomic analysis that standard CPUs process too slowly. They require specialized hardware accelerator
- [ ] A. Compute Optimized
- [ ] B. Memory Optimized
- [ ] C. Accelerated Computing
- [ ] D. Storage Optimized

Q43. A financial company must retain data for 10 years for compliance at the lowest possible cost. Data is rarely accessed, and a retrieval time of 12-48 hours is acceptable. Which Amazon S3 storage class is the best fit for this use case?
- [ ] A. Amazon S3 Standard-IA
- [ ] B. Amazon S3 Glacier Deep Archive
- [ ] C. Amazon S3 Glacier Flexible Retrieval
- [ ] D. Amazon S3 Intelligent-Tiering

Q44. In Amazon EC2, what acts as a virtual firewall at the instance level to control inbound and outbound traffic?
- [ ] A. Security Group
- [ ] B. Network Access Control List (NACL)
- [ ] C. AWS WAF
- [ ] D. Route Table

Q45. A company needs to store data for a Big Data system that requires high throughput but does not require a high number of Input/Output Operations Per Second (IOPS). Which of the following Amazon EBS volume types is the most cost-effective choice?
- [ ] A. Cold HDD (sc1)
- [ ] B. Throughput Optimized HDD (st1)
- [ ] C. Provisioned IOPS SSD (io2)
- [ ] D. General Purpose SSD (gp3)

Q46. You have a large amount of old image data that is infrequently accessed (about once every few months). However, when needed, the data must be immediately available in milliseconds. Which Amazon S3 storage class is the most cost-optimized choice?
- [ ] A. S3 Standard-IA
- [ ] B. S3 Glacier Flexible Retrieval
- [ ] C. S3 One Zone-IA
- [ ] D. S3 Standard

Q47. A batch processing application is highly fault-tolerant and can be paused and restarted later without affecting the results. Which Amazon EC2 instance purchasing option provides the most cost savings (up to 90%)?
- [ ] A. Spot Instances
- [ ] B. On-Demand Instances
- [ ] C. Dedicated Hosts
- [ ] D. Reserved Instances

Q48. When using EBS Multi-Attach (io1/io2 family only), how many EC2 instance(s) can it support?
- [ ] A. 4
- [ ] B. 8
- [ ] C. 16
- [ ] D. All of the above

Q49. A compliance team requires that a copy of all S3 objects in a critical bucket be maintained in another AWS Region to protect against regional disasters. The copy must occur automatically when new objects are created. Which feature should you configure?
- [ ] A. S3 Lifecycle transition to Glacier Deep Archive in the same Region
- [ ] B. Amazon EFS asynchronous replication between Regions
- [ ] C. S3 Cross-Region Replication (CRR) on the bucket
- [ ] D. EBS snapshot copy from the primary Region to the secondary Region

Q50. You manage an S3 bucket storing log files that grow quickly. Older logs (over 90 days) are rarely accessed, but must remain immediately retrievable when needed. How should you configure storage classes using lifecycle policies?
- [ ] A. Store all logs in S3 Glacier Deep Archive to minimize cost
- [ ] B. Immediately transition logs to S3 One Zone-IA upon upload
- [ ] C. Delete logs after 90 days using lifecycle expiration
- [ ] D. Transition objects to S3 Standard-IA after 90 days and keep them there

Q51. A company runs a web application on Amazon EC2. Traffic spikes during peak hours and drops at night. The company wants a solution that automatically adjusts the number of instances based on actual load while minimizing operational effort. Which solution is the most appropriate?
- [ ] A. Use Scheduled Scaling
- [ ] B. Use Target Tracking Scaling
- [ ] C. Manually increase instance size
- [ ] D. Use Reserved Instances

Q52. An application requires high availability and fault tolerance. If one instance fails, traffic must automatically be routed to another instance, and the system must self-recover. Which solution is the most appropriate?
- [ ] A. Use EC2 only
- [ ] B. EC2 + Auto Scaling
- [ ] C. EC2 + Load Balancer
- [ ] D. EC2 + Load Balancer + Auto Scaling

Q53. A company wants to run short-term workloads at the lowest possible cost and is willing to accept that instances may be terminated at any time. Which solution is the most appropriate?
- [ ] A. On-Demand
- [ ] B. Reserved
- [ ] C. Spot Instances
- [ ] D. Dedicated Hosts

Q54. A company runs a steady workload on EC2 over a long period of time. They want to minimize costs as much as possible without changing the architecture. Which solution is the most appropriate?
- [ ] A. On-Demand Instances
- [ ] B. Spot Instances
- [ ] C. Reserved Instances
- [ ] D. Auto Scaling

Q55. A company wants to quickly deploy multiple instances with the same configuration and pre-installed software, while minimizing setup time. Which solution is the best?
- [ ] A. Configure each instance via SSH
- [ ] B. Use snapshots each time
- [ ] C. Create an AMI and use it in a Launch Template
- [ ] D. Manually copy files

Q56. A company runs a web application on multiple EC2 instances behind an Application Load Balancer (ALB). The instances need to share a common directory containing user-uploaded files with low latency. Which solution is the most appropriate?
- [ ] A. Store the files in Amazon S3 and mount it directly to the EC2 instances
- [ ] B. Use an EBS volume and attach it to all instances
- [ ] C. Use Amazon EFS and mount it to all instances
- [ ] D. Store the files in the instance store

Q57. A company needs to store millions of log files. The files will be accessed frequently during the first 30 days, after which they will rarely be accessed but must be retained for a long period. Which solution is the most cost-effective?
- [ ] A. Amazon S3 Standard with a lifecycle policy transitioning to Glacier
- [ ] B. Amazon S3 Standard
- [ ] C. Amazon S3 Intelligent-Tiering
- [ ] D. Amazon EFS Infrequent Access

Q58. A system needs to store static files (images, CSS, JavaScript) for a public website, with high scalability and CDN integration. Which solution is the best?
- [ ] A. EBS
- [ ] B. EFS
- [ ] C. S3 + CloudFront
- [ ] D. Instance Store

Q59. An engineer notices that Amazon EFS has higher latency than Amazon EBS when running database workloads. What is the main reason?
- [ ] A. Amazon EFS does not use SSDs
- [ ] B. Amazon EFS is a network file system
- [ ] C. Amazon EFS is object storage
- [ ] D. Amazon EFS does not support caching

Q60. A company is designing a shared storage solution for a containerized application running on multiple Amazon EC2 instances across different Availability Zones. The application requires a POSIX-compliant file system with automatic scaling and high availability. Which solution is the most appropriate?
- [ ] A. Use Amazon EBS volumes and attach them to all EC2 instances across Availability Zones
- [ ] B. Use Amazon EFS and mount it on all EC2 instances
- [ ] C. Store data in Amazon S3 and access it using the S3 API
- [ ] D. Use instance store volumes for shared storage

Q61. Which service is a serverless, pay-as-you-go compute service that scales automatically based on incoming requests?
- [ ] A. Amazon EC2
- [ ] B. AWS Lambda
- [ ] C. Amazon Lightsail
- [ ] D. AWS Outposts

Q62. Which S3 feature allows you to automatically transition objects to a cheaper storage class after a certain period?
- [ ] A. S3 Versioning
- [ ] B. S3 Replication
- [ ] C. S3 Lifecycle Policy
- [ ] D. S3 Transfer Acceleration

Q63. Which AWS service provides a managed registry for storing, managing, and deploying Docker container images?
- [ ] A. Amazon ECS
- [ ] B. Amazon EKS
- [ ] C. Amazon ECR
- [ ] D. AWS App Runner

Q64. Which storage option is best for low-latency database workloads?
- [ ] A. S3
- [ ] B. Glacier
- [ ] C. EBS SSD
- [ ] D. EFS Infrequent Access

Q65. For long-term backup with infrequent access, which service should you use?
- [ ] A. S3 Standard
- [ ] B. EFS
- [ ] C. Glacier
- [ ] D. EBS

Q66. How many EC2 instances can an EBS volume be attached to at the same time?
- [ ] A. Multiple instances
- [ ] B. One instance (except Multi-Attach)
- [ ] C. None
- [ ] D. Unlimited

Q67. What is a key limitation of Amazon EBS compared to Amazon EFS regarding instance attachment?
- [ ] A. EBS is object-based
- [ ] B. EFS only attaches to one instance
- [ ] C. EBS usually attaches to one instance at a time
- [ ] D. EFS is much slower

Q68. What happens to the data in an Instance Store if the associated EC2 instance is terminated?
- [ ] A. Data is saved to S3
- [ ] B. Data is persistent
- [ ] C. Data is lost
- [ ] D. Data is moved to EBS

Q69. Where are Amazon EBS snapshots stored to ensure high durability and availability?
- [ ] A. Inside the EC2 instance
- [ ] B. On an Instance Store
- [ ] C. In Amazon S3
- [ ] D. On a Tape Gateway

Q70. A company plans to deploy containers on AWS. The company wants full control of the compute resources that host the containers. Which AWS service will meet these requirements?
- [ ] A. Amazon Elastic Kubernetes Service (Amazon EKS)
- [ ] B. AWS Fargate
- [ ] C. Amazon EC2
- [ ] D. Amazon Elastic Container Service (Amazon ECS)

Q71. Which Amazon EC2 pricing model is the MOST cost efficient for an uninterruptible workload that runs once a year for 24 hours?
- [ ] A. On-Demand Instances
- [ ] B. Reserved Instances
- [ ] C. Spot Instances
- [ ] D. Dedicated Instances

Q72. A company needs to run a batch processing job. This task can be abruptly interrupted and resumed later without causing errors or affecting the final result. Which Amazon EC2 pricing model will provide the lowest cost for the company in this scenario?
- [ ] A. On-Demand Instances
- [ ] B. Spot Instances
- [ ] C. Reserved Instances
- [ ] D. Dedicated Hosts

Q73. An e-commerce website frequently experiences unpredictable spikes in traffic. Which of the following architectures combines two AWS services to automatically increase the number of servers during high load and evenly distribute incoming traffic across them?
- [ ] A. AWS Lambda and Amazon Route 53
- [ ] B. Amazon CloudFront and Amazon S3
- [ ] C. Amazon EC2 Auto Scaling and Elastic Load Balancing (ELB)
- [ ] D. AWS Elastic Beanstalk and Amazon RDS

Q74. A developer wants to automatically run a code script to compress an image immediately every time a user uploads a new image to Amazon S3. They only want to pay for the exact compute time the code consumes and do not want to provision, configure, or manage any servers. Which compute service is best suited for this requirement?
- [ ] A. Amazon EC2
- [ ] B. Amazon ECS
- [ ] C. AWS Elastic Beanstalk
- [ ] D. AWS Lambda

Q75. Your company is planning to migrate its microservices architecture, currently packaged as Docker containers, to AWS. The technical team wants to use a fully managed container orchestration service that natively supports the open-source Kubernetes engine. Which service should they choose?
- [ ] A. Amazon Elastic Container Service (Amazon ECS)
- [ ] B. Amazon Elastic Kubernetes Service (Amazon EKS)
- [ ] C. AWS Fargate
- [ ] D. AWS Elastic Beanstalk

Q76. A company is looking for a storage solution that can store a vast amount of unstructured data, such as images and videos. Each item must be stored with a unique identifier and descriptive metadata. Which storage type should they use?
- [ ] A. Block Storage
- [ ] B. File Storage
- [ ] C. Object Storage
- [ ] D. Single Disk Storage

Q77. Compared to a Single Disk Storage, which of the following is a key characteristic of a Distributed Storage System (Max Scale)?
- [ ] A. Lowest Durability and High Speed
- [ ] B. Very High Durability and Very High Throughput
- [ ] C. Low Cost and Limited Throughput
- [ ] D. Low Latency and High Speed

Q78. A developer is building a real-time AI recommendation system. They need a storage layer that ensures the data used for training is the same as the data used for serving (consistency) and requires low latency for instant predictions. Which storage layer should they use?
- [ ] A. Raw Data Storage
- [ ] B. Feature Storage
- [ ] C. Metadata Storage
- [ ] D. Model Storage

Q79. A big data analytics platform requires Very High Throughput to process massive datasets and Very High Durability to ensure no data is ever lost. They can tolerate higher latency (slower response time). Which storage is most suitable?
- [ ] A. Single Disk Storage
- [ ] B. Distributed Storage System (Max Scale)
- [ ] C. Block Storage
- [ ] D. Local Storage

Q80. A data processing firm runs batch jobs that are stateless and can be interrupted at any time. They are looking for the absolute lowest cost for compute. Which option is best?
- [ ] A. Saving Plans
- [ ] B. On-Demand Instances
- [ ] C. Spot Instances
- [ ] D. Capacity Reservation

Q81. Which EC2 pricing model allows you to bid for unused AWS capacity?
- [ ] A. On-Demand
- [ ] B. Dedicated Hosts
- [ ] C. Reserved Instances
- [ ] D. Spot Instances

Q82. A company needs to run a specialized compliance-heavy workload that requires software licenses bound to a specific physical server's sockets and cores. Which EC2 tenancy model is the only one that supports this requirement?
- [ ] A. Dedicated Instances
- [ ] B. Dedicated Hosts
- [ ] C. On-Demand Capacity Reservations
- [ ] D. Reserved Instances

Q83. An organization is looking to migrate to AWS and wants to commit to a 3-year term. They need a discount that applies to EC2 instances regardless of the instance family, AWS Region, or even if they switch to AWS Fargate or Lambda. Which Savings Plan fits this best?
- [ ] A. EC2 Instance Savings Plans
- [ ] B. SageMaker Savings Plans
- [ ] C. Compute Savings Plans
- [ ] D. Standard Reserved Instances

Q84. A developer is using Spot Instances for a non-critical test environment. If AWS needs the capacity back, how much notice does the developer receive before the instance is terminated?
- [ ] A. 5 minutes
- [ ] B. No notice is provided
- [ ] C. 30 seconds
- [ ] D. 2 minutes

Q85. A company wants to receive the maximum possible discount on their EC2 usage. They have a predictable workload for the next 3 years and are willing to pay for the entire term upfront. Which payment option provides the highest savings?
- [ ] A. Monthly Billing
- [ ] B. All Upfront
- [ ] C. No Upfront
- [ ] D. Partial Upfront

Q86. If an On-Demand Capacity Reservation is not being used (no instances are running in it), how is the customer billed?
- [ ] A. They are billed a small "holding fee" (10% of On-Demand)
- [ ] B. They are billed at the full On-Demand rate for the reserved capacity
- [ ] C. They receive a credit for future use
- [ ] D. They are not billed at all

Q87. Which AWS tool can provide recommendations on which Reserved Instances or Savings Plans to buy based on your historical usage?
- [ ] A. AWS Budgets
- [ ] B. AWS Cost Explorer
- [ ] C. AWS Trusted Advisor
- [ ] D. Amazon Inspector

Q88. Which EC2 purchasing option is the most cost-effective for fault-tolerant, flexible workloads (such as batch processing) and can offer discounts up to 90% off On-Demand prices?
- [ ] A. On-Demand Instances
- [ ] B. Spot Instances
- [ ] C. Reserved Instances
- [ ] D. Dedicated Hosts

Q89. To optimize applications that require extremely low network latency and high network bandwidth between instances within the same Availability Zone (AZ), which type of Placement Group should you use?
- [ ] A. Cluster Placement Group
- [ ] B. Spread Placement Group
- [ ] C. Partition Placement Group
- [ ] D. Auto Scaling Group

Q90. Which service provides object-level storage in AWS?
- [ ] A. Amazon EBS
- [ ] B. Amazon Instance Store
- [ ] C. Amazon EFS
- [ ] D. Amazon S3

Q91. Which type of Load Balancer of Amazon ELB service can be reached via Route Table Entry?
- [ ] A. Application Load Balancer
- [ ] B. Network Load Balancer
- [ ] C. Gateway Load Balancer
- [ ] D. Classic Load Balancer

Q92. Which statement best describes Elastic Load Balancing?
- [ ] A. It translates a domain name into an IP address using DNS
- [ ] B. It distributes incoming application traffic across one or more Amazon EC2 instances
- [ ] C. It collects metrics on connected Amazon EC2 instances
- [ ] D. It automatically adjusts the number of Amazon EC2 instances to support incoming traffic

Q93. Which AWS service provides a simple and scalable shared file storage solution for use with Linux-based AWS and on-premises servers?
- [ ] A. Amazon S3
- [ ] B. Amazon Glacier
- [ ] C. Amazon EBS
- [ ] D. Amazon EFS

Q94. A company is hosting a web application in a Docker container on Amazon EC2. AWS is responsible for which of the following tasks?
- [ ] A. Scaling the web application and services developed with Docker
- [ ] B. Provisioning or scheduling containers to run on clusters and maintain their availability
- [ ] C. Performing hardware maintenance in the AWS facilities that run the AWS Cloud
- [ ] D. Managing the guest operating system, including updates and security patches

Q95. Where can you store files in AWS?
- [ ] A. Amazon EFS
- [ ] B. Amazon SNS
- [ ] C. Amazon ECS
- [ ] D. Amazon EMR

Q96. Using Amazon EC2 falls under which of the following cloud computing models?
- [ ] A. IaaS & SaaS
- [ ] B. IaaS
- [ ] C. SaaS
- [ ] D. PaaS

Q97. Which is not a type of Storage in AWS services?
- [ ] A. Block Storage
- [ ] B. File Storage
- [ ] C. Disk Storage
- [ ] D. Object Storage

Q98. Which of the following procedures will help reduce your Amazon S3 costs?
- [ ] A. Use the Import/Export feature to move old files automatically to Amazon Glacier
- [ ] B. Use the right combination of storage classes based on different use cases
- [ ] C. Pick the right Availability Zone for your S3 bucket
- [ ] D. Move all the data stored in S3 standard to EBS

Q99. An application runs on multiple Amazon EC2 instances that access a shared file system simultaneously. Which AWS storage service should be used?
- [ ] A. Amazon EBS
- [ ] B. Amazon EFS
- [ ] C. Amazon S3
- [ ] D. AWS Artifact

Q100. Which storage type is most suitable for running relational databases (SQL) and Virtual Machine (VM) disks?
- [ ] A. Object Storage — because of its rich metadata capabilities
- [ ] B. File Storage — because of its hierarchical directory structure
- [ ] C. Block Storage — because of its extremely fast performance and support for high-transaction workloads
- [ ] D. Archival Storage — because of its low cost

Q101. A customer showed interest in a company product and wanted to quickly review its application. To do it, the boss wants to launch an instance as fast as it can and optimizing the cost shows we can easily stop it after the customer's review. Which purchasing options below are preferred?
- [ ] A. Spot instance
- [ ] B. Reserved Instance
- [ ] C. On-demand Instance
- [ ] D. Saving Plans

Q102. Which of the following that an ALB can't route traffic to?
- [ ] A. S3 Buckets
- [ ] B. EC2 Instances
- [ ] C. Lambda Functions
- [ ] D. IP Addresses

Q103. Which service provides temporary block storage that is physically attached to the host computer?
- [ ] A. Instance store
- [ ] B. EBS
- [ ] C. S3 standard
- [ ] D. Amazon EFS

Q104. What attaching an EBS volume to an EC2 instance, where must the volume be located?
- [ ] A. In any AWS region
- [ ] B. Should be at your physical service where you company placed
- [ ] C. In the same AZ as the EC2 instance
- [ ] D. In the same VPC as the EC2 instance

Q105. What is the keys difference between EBS and EFS in terms of Availability Zones?
- [ ] A. EFS is only available in a single AZ
- [ ] B. Neither service supports multiple AZs
- [ ] C. EBS is locked to a single AZ, while EFS data is stored redundantly across multiple AZs.
- [ ] D. EBS can work across multiple AZs by default

Q106. How does EFS scale its storage capacity?
- [ ] A. Manually increase the size in the AWS console
- [ ] B. It scales automatically as you add or remove files
- [ ] C. It scales based on the number of EC2 instances attached
- [ ] D. You must use Auto Scaling Groups to scale EFS

Q107. Which ELB is best suited for handling millions of requests per second while maintaining ultra-low latency?
- [ ] A. Application Load Balancer
- [ ] B. Network Load Balancer
- [ ] C. Classic Load Balancer
- [ ] D. Amazon Load Balancer

Q108. Which service allows multiple EC2 instances to access the same file system simultaneously across different AZs?
- [ ] A. EBS
- [ ] B. EFS
- [ ] C. ELB
- [ ] D. ENI

Q109. Elastic block storage (EBS), Elastic network interfaces (ENI), Elastic load balancer (ELB), Elastic file system (EFS). Which network service here, its setup default can only work with a single EC2 instance?
- [ ] A. EBS
- [ ] B. ENI
- [ ] C. ELB
- [ ] D. EFS

Q110. A startup is building an event-driven image-processing pipeline. Every time a user uploads a file, the application must resize the image, add a watermark, and store metadata. Traffic is highly unpredictable, ranging from almost zero to sudden spikes of thousands of requests per minute. The team does not want to provision or manage servers, and they are comfortable packaging any required libraries with the application. Which statement best identifies the customer's remaining responsibility if AWS Lambda is selected?
- [ ] A. Managing the physical servers that execute the function
- [ ] B. Updating the operating system and Lambda runtime
- [ ] C. Writing and maintaining the function code and its dependencies
- [ ] D. Configuring the underlying AWS networking infrastructure for the Lambda service

Q111. What are the core differences in operating models between AWS Lambda and Amazon EC2?
- [ ] A. Lambda executes event-driven code and automatically manages the infrastructure, while EC2 requires users to manage and maintain virtual machines.
- [ ] B. Lambda is designed to run tasks continuously for extended periods, while EC2 can only run for short durations.
- [ ] C. Lambda only supports Python, while EC2 supports a variety of different operating systems.
- [ ] D. EC2 scales automatically without configuration, while Lambda requires setting up an Auto Scaling Group.

Q112. How does Horizontal Scalability (Scaling Out) differ fundamentally from Vertical Scalability (Scaling Up)?
- [ ] A. Horizontal scaling involves adding more RAM to an existing instance, while vertical scaling adds more instances.
- [ ] B. Vertical scaling is restricted by hardware limits of a single machine, while horizontal scaling is theoretically limitless by adding more nodes.
- [ ] C. Horizontal scaling is preferred for non-distributed systems like traditional databases.
- [ ] D. Vertical scaling requires a Load Balancer, whereas horizontal scaling does not.

Q113. What is the benefit of using a Cluster Placement Group?
- [ ] A. It spreads instances across different physical hardware to minimize correlated failures
- [ ] B. It partitions instances across different racks to support distributed data systems.
- [ ] C. It packs instances close together in a single Availability Zone to achieve low-latency, high-throughput networking.
- [ ] D. It automatically distributes traffic across multiple Availability Zones.

Q114. A student is reviewing core AWS services related to EC2, scaling, networking, and availability. They want to verify which statements are correct. How many of the following statements are correct? (1) Elastic Load Balancer distributes incoming traffic across multiple EC2 instances; (2) Auto Scaling Group automatically increases or decreases the number of EC2 instances based on demand; (3) An AMI is used to route traffic between multiple servers; (4) Private IP addresses allow EC2 instances to communicate within a VPC; (5) Deploying resources in multiple Availability Zones improves high availability.
- [ ] A. 2
- [ ] B. 3
- [ ] C. 4
- [ ] D. 5

Q115. In the structure of an object in object storage, which component contains descriptive information such as Content-Type and other custom attributes?
- [ ] A. Unique ID
- [ ] B. Metadata
- [ ] C. Data
- [ ] D. Storage Pool

Q116. In the architecture of an Object Storage system (like Amazon S3), what is the primary characteristic of its addressing system compared to traditional file systems?
- [ ] A. It uses a nested directory tree with file paths.
- [ ] B. It uses a flat address space where each object has a unique identifier.
- [ ] C. It organizes data into fixed-size 4KB blocks with physical addresses.
- [ ] D. It relies on a Master Boot Record (MBR) to locate data across clusters.

Q117. A startup is building an AI data lake to store raw datasets, processed outputs, model artifacts, and logs. The team wants virtually unlimited scalability, high durability, low-cost storage, and API-based access for cloud-native applications. Which AWS storage service is the best fit?
- [ ] A. Amazon EBS
- [ ] B. Amazon EFS
- [ ] C. Amazon S3
- [ ] D. EC2 Instance Store

Q118. A machine learning team runs training jobs on multiple Amazon EC2 instances across different Availability Zones, and all instances must read and update the same shared dataset using a standard file system interface without managing storage capacity manually. Which AWS storage service is the most appropriate?
- [ ] A. Amazon S3
- [ ] B. Amazon EFS
- [ ] C. Amazon EBS
- [ ] D. Amazon S3 Glacier Deep Archive

Q119. A company applies a lifecycle rule to transition objects to Amazon S3 Glacier after 90 days and to delete them after 365 days. What is the expected outcome?
- [ ] A. Objects remain in S3 Standard and only metadata is moved to Glacier after 90 days.
- [ ] B. Objects are archived in Glacier and cannot be deleted after the lifecycle policy is applied.
- [ ] C. Objects are moved to Glacier after 90 days and automatically deleted after 365 days
- [ ] D. Objects are duplicated into Glacier and the original objects remain until deleted manually

Q120. Which EC2 placement group strategy divides instances into logical segments, ensuring that each segment runs on separate underlying hardware racks to support large distributed systems like Hadoop or Cassandra?
- [ ] A. Cluster Placement Group
- [ ] B. Spread Placement Group
- [ ] C. Partition Placement Group
- [ ] D. Dedicated Hosts

Q121. Which feature allows you to fully initialize an Amazon EBS volume created from a snapshot to eliminate initial read latency?
- [ ] A. Snapshot Archive
- [ ] B. Recycle Bin for Snapshots
- [ ] C. Fast Snapshot Restore (FSR)
- [ ] D. Cross-Region Snapshot Copy

Q122. When deploying containers using Amazon Elastic Container Service (Amazon ECS), which launch type allows you to run tasks on AWS-managed infrastructure without provisioning or managing the underlying EC2 instances?
- [ ] A. EC2 Launch Type
- [ ] B. Fargate Launch Type
- [ ] C. External Launch Type
- [ ] D. Kubernetes Launch Type

Q123. What must be enabled as a prerequisite before you can set up Amazon DynamoDB Global Tables for cross-region data replication?
- [ ] A. DynamoDB Accelerator (DAX)
- [ ] B. Amazon Kinesis Data Streams
- [ ] C. On-Demand Capacity Mode
- [ ] D. DynamoDB Streams

Q124. If an Application Load Balancer is configured to route incoming traffic based on the domain name, such as routing one.example.com to Service A and other.example.com to Service B, which routing method is being utilized?
- [ ] A. Host-based routing
- [ ] B. Request-based routing
- [ ] C. Path-based routing
- [ ] D. Header-based routing
