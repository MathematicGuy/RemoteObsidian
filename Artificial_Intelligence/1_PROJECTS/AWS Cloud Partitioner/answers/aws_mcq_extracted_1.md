### AWS Cloud Practitioner Practice Questions

Q1. What is AWS EC2?
- [ ] A. AWS EC2 is a serverless compute service
- [x] B. AWS EC2 is a virtual server in the AWS Cloud
- [ ] C. AWS EC2 is a data center
- [ ] D. AWS EC2 is a resource monitoring service

Q2. What are Edge Locations?
- [ ] A. Physical hard drives
- [ ] B. AWS Regions
- [ ] C. Data centers that store petabytes of data
- [x] D. Data centers that deliver data fast to the users

Q3. A large company is interested in avoiding long-term contracts and moving from fixed costs to variable costs. What is the value proposition of AWS for this company?
- [ ] A. Economies of scale
- [x] B. Pay-as-you-go pricing
- [ ] C. Volume pricing discounts
- [ ] D. Automated cost optimization

Q4. A user is planning to launch three EC2 instances behind a single Elastic Load Balancer. The deployment should be highly available.
- [x] A. Launch the instances across multiple Availability Zones in a single AWS Region
- [ ] B. Launch the instances as EC2 Spot Instances in the same AWS Region and the same Availability Zone
- [ ] C. Launch the instances in multiple AWS Regions, and use Elastic IP addresses.
- [ ] D. Launch the instances as EC2 Reserved Instances in the same AWS Region, but in different Availability Zones

Q5. Which of the following is an advantage that users experience when they move on-premises workloads to the AWS Cloud?
- [x] A. Elimination of expenses for running and maintaining data centers
- [ ] B. Price discounts that are identical to discounts from hardware providers
- [ ] C. Distribution of all operational controls to AWS
- [ ] D. Elimination of operational expenses

Q6. A company no longer needs to purchase and maintain physical servers after migrating its workloads to AWS. Which cloud benefit does this demonstrate?
- [x] A. Stop spending money running and maintaining data centers
- [ ] B. Increase speed and agility
- [ ] C. Global reach
- [ ] D. Elasticity

Q7. A company expands its application to customers in Europe and Asia by deploying resources in multiple AWS Regions. Which cloud benefit does this demonstrate?
- [ ] A. Elasticity
- [x] B. Global reach
- [ ] C. Massive economies of scale
- [ ] D. Pay-as-you-go pricing

Q8. Which AWS Cloud benefit allows organizations to convert upfront infrastructure costs into variable expenses?
- [x] A. Trade CAPEX for OPEX
- [ ] B. High availability
- [ ] C. Elasticity
- [ ] D. Global reach

Q9. A development team can launch new infrastructure resources within minutes using the AWS Management Console or APIs. Which cloud advantage does this represent?
- [ ] A. Massive economies of scale
- [x] B. Increased speed and agility
- [ ] C. Data durability
- [ ] D. Global infrastructure

Q10. Which cloud computing service model allows users to control the operating system and applications while the cloud provider manages the physical infrastructure?
- [ ] A. Software as a Service (SaaS)
- [ ] B. Platform as a Service (PaaS)
- [x] C. Infrastructure as a Service (IaaS)
- [ ] D. Network as a Service (NaaS)

Q11. What is the main difference between Edge Locations and AWS Regions?
- [ ] A. Edge Locations are used for compute resources; Regions are for storage only
- [x] B. Edge Locations cache content and serve it with low latency; Regions contain full AWS services
- [ ] C. Edge Locations are physically larger than Regions
- [ ] D. There is no difference; they are the same thing

Q12. CloudFront is primarily used to deliver content with low latency. Which AWS component does it leverage?
- [ ] A. Availability Zones
- [ ] B. AWS Regions
- [x] C. Edge Locations
- [ ] D. VPCs

Q13. A company is designing a disaster recovery strategy and wants the ability to instantly fail over to a secondary Region with near-zero data loss. Which approach is recommended?
- [ ] A. Backup data manually to another Region every 24 hours
- [x] B. Implement Active-Active deployment across two Regions with real-time data replication
- [ ] C. Keep a cold standby in another Region and restore from backups when needed
- [ ] D. Use S3 cross-region replication only

Q14. Which disaster recovery approach requires the least RTO (Recovery Time Objective) and RPO (Recovery Point Objective)?
- [ ] A. Backup and restore strategy
- [ ] B. Pilot light approach
- [ ] C. Warm standby approach
- [x] D. Active-Active approach (multi-region)

Q15. A global e-commerce company wants to serve content to users with the lowest possible latency worldwide. Which combination of AWS services should they use?
- [x] A. Multiple Regions + Multi-AZ within each Region + CloudFront
- [ ] B. Single Region + CloudFront
- [ ] C. Multiple Regions only
- [ ] D. Edge Locations only

Q16. Which AWS service enables organizations to intelligently route DNS queries to the optimal AWS Region based on the geographic location of users, health status of endpoints, and configurable routing policies?
- [x] A. Amazon Route 53
- [ ] B. AWS Global Accelerator with anycast IP addresses
- [ ] C. Amazon CloudFront distribution with origin failover configured
- [ ] D. AWS Transit Gateway with inter-region peering connections

Q17. How does deploying resources across AWS Regions help organizations reduce their total cost of ownership when serving a globally distributed user base?
- [x] A. By reducing data transfer costs and latency charges through proximity to end users in each geographic market
- [ ] B. By leveraging automated inter-Region replication to eliminate the need for backup storage and archival solutions at individual locations
- [ ] C. By reducing data transfer expenses through proximity to end users and enabling volume discounts on bandwidth consumption across Regions
- [ ] D. By consolidating all workloads into a single Region with the lowest EC2 pricing tier to maximize compute savings

Q18. What benefit does AWS's distributed global infrastructure provide for organizations that need to maintain low-latency access for users in different continents?
- [ ] A. Deployment of resources in a single strategic location that maximizes network backbone utilization to reduce round-trip time for global users
- [x] B. Deployment of resources closer to end users in multiple geographic locations to reduce network transmission time
- [ ] C. Automatic replication of all data across every available Region to ensure users can access information from the nearest geographic location
- [ ] D. Centralized routing through a single primary Region that optimizes bandwidth allocation and reduces network congestion for international users

Q19. What is the primary benefit of deploying applications across multiple Availability Zones?
- [ ] A. Increased application latency for better performance
- [x] B. High availability and fault tolerance
- [ ] C. Reduced AWS pricing for the same workload
- [ ] D. Automatic database replication without additional configuration

Q20. Which of the following services is designed with native fault tolerance, storing objects redundantly across multiple Availability Zones?
- [ ] A. Amazon Redshift
- [ ] B. AWS Snowball
- [ ] C. Amazon RDS (when Multi-AZ enabled)
- [x] D. Amazon S3

Q21. Which statement best defines cloud computing?
- [ ] A. Running applications only on personal computers without connecting to the internet.
- [ ] B. Installing physical servers locally and maintaining hardware inside an organization building.
- [ ] C. Storing data permanently on removable storage devices such as USB drives.
- [x] D. Delivering computing resources through the internet with on-demand access and pay-as-you-go pricing.

Q22. Which AWS service provides resizable compute capacity in the cloud and gives you full administrative control over the operating system?
- [ ] A. AWS Lambda
- [x] B. Amazon EC2
- [ ] C. AWS Fargate
- [ ] D. Amazon S3

Q23. What is the primary characteristic of an Availability Zone (AZ) regarding fault isolation?
- [ ] A. It is a geographic area isolated by international boundaries for data sovereignty.
- [ ] B. It consists of multiple Regions connected by low-latency networks.
- [x] C. It has independent power, cooling, and networking to ensure full fault isolation.
- [ ] D. It provides edge caching to reduce latency for global users.

Q24. A global e-commerce website receives visitors from many countries. The company wants to direct users to the correct application endpoint using their domain name and also speed up delivery of images, videos, and static content for users around the world. Which combination of services is used to achieve these goals?
- [x] A. Use Amazon Route 53 for domain name resolution and Amazon CloudFront for global content delivery.
- [ ] B. Use Amazon CloudFront for domain name resolution and Amazon Route 53 for content caching.
- [ ] C. Use Amazon Route 53 for caching static files and Amazon CloudFront for managing domain records.
- [ ] D. Use Amazon CloudFront for routing DNS traffic and Amazon Route 53 for video streaming services.

Q25. A company runs a reduced-capacity but fully functional copy of its application stack in a secondary Region. During a disaster, it plans to scale out that environment to handle production traffic. Which strategy is this?
- [ ] A. Backup and Restore
- [ ] B. Pilot Light
- [x] C. Warm Standby
- [ ] D. Active/Active

Q26. Which cloud computing model provides virtualized computing resources such as virtual machines, storage, and networking over the internet?
- [ ] A. Software as a Service (SaaS)
- [ ] B. Platform as a Service (PaaS)
- [x] C. Infrastructure as a Service (IaaS)
- [ ] D. Function as a Service (FaaS)

Q27. A small e-commerce company hosts its website on one physical server located in its office. One day, the server suddenly stops working because of a hardware problem. As a result, the entire website becomes unavailable and customers cannot access the online store. The IT team realizes that the system design caused the entire service to stop when a single component failed. Which concept best describes the problem in this situation?
- [x] A. Single Point of Failure where one component failure stops the entire system
- [ ] B. Resource Pooling where multiple users share the same infrastructure resources
- [ ] C. Rapid Elasticity where computing resources scale automatically with demand
- [ ] D. Broad Network Access where services are available through internet networks

Q28. A company wants to deploy its application in multiple geographic regions so users around the world can access it with lower latency. Which AWS Cloud benefit supports this requirement?
- [ ] A. High availability
- [x] B. Global reach
- [ ] C. Elasticity
- [ ] D. Pay-as-you-go pricing

Q29. A startup has continuously changing workloads, needs rapid deployment, does not want to invest in a data center upfront, and wants to pay only for the resources it actually uses. According to the slide content, which of the following best explains why cloud is more suitable than on-premises?
- [ ] A. Cloud provides full control over physical infrastructure and completely eliminates internet dependency
- [x] B. Cloud changes upfront fixed capital costs into variable costs based on usage and supports flexible resource scaling
- [ ] C. Cloud requires the company to manage all networking, storage, and virtualization by itself
- [ ] D. Cloud is only suitable for large enterprises with stable workloads over many years

Q30. A small startup wants to build a web application for online food delivery. The team wants to focus mainly on developing application features rather than managing servers, operating systems, and platform maintenance. Which service model is the most appropriate solution for this situation?
- [ ] A. On-Premises infrastructure where the company manages servers, software, and networks
- [ ] B. Infrastructure as a Service (IaaS) providing virtual servers while users manage operating systems
- [x] C. Platform as a Service (PaaS) providing runtime environments while users deploy applications
- [ ] D. Software as a Service (SaaS) providing complete applications managed entirely by providers

Q31. A global media company stores high-resolution video files in an Amazon S3 bucket located in the us-east-1 (N. Virginia) Region. While users in the United States experience fast download speeds, users in Singapore and Tokyo report significant delays and "slow content delivery" when accessing the same files. Which architectural change would provide the best user experience and performance for the global audience while minimizing the load on the origin S3 bucket?
- [ ] A. Create a secondary S3 bucket in the ap-southeast-1 (Singapore) Region and manually copy all video files to it.
- [x] B. Deploy Amazon CloudFront and configure the N. Virginia S3 bucket as the origin.
- [ ] C. Upgrade the S3 bucket to a Multi-AZ configuration to increase data replication speed.
- [ ] D. Instruct global users to use a VPN to connect directly to the N. Virginia network path.

Q32. An e-commerce company increases the number of servers in its architecture to handle a steady increase in customer traffic over the years. Which concept does this represent?
- [ ] A. Elasticity
- [ ] B. Agility
- [ ] C. Fault tolerance
- [x] D. Scalability

Q33. A development team can now provision hundreds of virtual servers in minutes, compared to the weeks it took to procure and deploy physical hardware. Which AWS Cloud advantage does this describe?
- [ ] A. Benefit from massive economies of scale
- [x] B. Increase speed and agility
- [ ] C. Stop guessing capacity
- [ ] D. Go global in minutes

Q34. A company is using Amazon EC2 to run their web applications. According to the Shared Responsibility Model, which of the following tasks is the customer's responsibility?
- [ ] A. Maintaining the physical network infrastructure of the data center.
- [ ] B. Replacing failed physical hard drives in the servers.
- [ ] C. Managing the virtualization software (hypervisor).
- [x] D. Updating patches for the Guest Operating System (Guest OS) installed on the EC2 instances.

Q35. When a large financial organization requires full control over its infrastructure for strict security reasons but still wants to use virtualization technology, which deployment model should they choose?
- [ ] A. SaaS (Software as a Service)
- [ ] B. Hybrid Cloud
- [ ] C. Public Cloud
- [x] D. Private Cloud

Q36. Which deployment model is characterized by the deployment of resources on-premises, using virtualization and resource management tools?
- [ ] A. Public Cloud
- [x] B. Private Cloud
- [ ] C. Hybrid Cloud
- [ ] D. Infrastructure as a Service (IaaS)

Q37. A user is moving a workload from a local data center to an architecture that is distributed between the local data center and the AWS Cloud. Which type of migration is this?
- [ ] A. On-premises to cloud native
- [ ] B. Hybrid to cloud native
- [x] C. On-premises to hybrid
- [ ] D. Cloud native to hybrid

Q38. A startup deploys its application to multiple AWS Regions so users from different continents can access the service with low latency. Which AWS Cloud advantage does this demonstrate?
- [x] A. Global reach
- [ ] B. Elasticity
- [ ] C. Reliability
- [ ] D. Resource pooling

Q39. A company is looking for the most cost-effective disaster recovery strategy. They are willing to accept a recovery time of several hours and a potential loss of data from their last daily backup. Which strategy should they choose?
- [ ] A. Active-Active
- [ ] B. Warm Standby
- [ ] C. Pilot Light
- [x] D. Backup & Restore

Q40. An organization needs to implement a Disaster Recovery strategy where they maintain a scaled-down but fully functional version of their application environment in a different AWS Region. Which DR strategy are they using?
- [ ] A. Backup and Restore
- [ ] B. Pilot Light
- [x] C. Warm Standby
- [ ] D. Multi-Site Active-Active

Q41. In the Software as a Service (SaaS) model, what is the user responsible for?
- [ ] A. Managing infrastructure and operating systems
- [ ] B. Managing runtime environment and applications
- [x] C. Only using the software provided
- [ ] D. Managing hardware and networking

Q42. Which deployment model combines cloud resources with existing on-premises infrastructure?
- [ ] A. Public Cloud
- [ ] B. Private Cloud
- [x] C. Hybrid Cloud
- [ ] D. SaaS

Q43. A company wants to achieve Disaster Recovery (DR) with "Zero Downtime". Based on the DR Strategy Ladder, which deployment pattern is this?
- [ ] A. Backup and Restore
- [ ] B. Pilot Light
- [ ] C. Warm Standby
- [x] D. Multi-Site (Active-Active)

Q44. What is the main difference between Multi-AZ and Multi-Region deployments?
- [ ] A. Multi-AZ is for caching global content, while Multi-Region is for compute workloads
- [x] B. Multi-AZ prevents data center failure impact (High Availability), while Multi-Region provides disaster recovery against regional failures
- [ ] C. Multi-AZ uses asynchronous replication, while Multi-Region uses synchronous replication
- [ ] D. Multi-AZ requires user traffic routing via DNS, while Multi-Region relies on simple Load Balancers

Q45. An e-commerce business experiences a massive spike in traffic during a holiday sale. The AWS Cloud automatically adds more servers to handle the traffic, and then removes them when the sale ends. Which cloud characteristic is this?
- [ ] A. Agility
- [ ] B. Global Reach
- [x] C. Elasticity
- [ ] D. Reliability

Q46. Which of the following is NOT one of the six main advantages of cloud computing described by AWS?
- [ ] A. Go global in minutes
- [x] B. Trade variable expense for fixed expense
- [ ] C. Stop spending money running and maintaining data centers
- [ ] D. Benefit from massive economies of scale

Q47. Which of the following does NOT belong to the AWS Cloud Computing models?
- [ ] A. Platform as a Service (PaaS)
- [ ] B. Infrastructure as a Service (IaaS)
- [ ] C. Software as a Service (SaaS)
- [x] D. Networking as a Service (NaaS)

Q48. A company wants to reduce the physical compute footprint that developers use to run code. Which service would meet that need by enabling serverless architectures?
- [ ] A. Amazon Elastic Compute Cloud (Amazon EC2)
- [x] B. AWS Lambda
- [ ] C. Amazon DynamoDB
- [ ] D. AWS CodeCommit

Q49. Which feature of the AWS Cloud will support an international company's requirement for low latency to all of its customers?
- [ ] A. Fault tolerance
- [x] B. Global reach
- [ ] C. Pay-as-you-go pricing
- [ ] D. High availability

Q50. Which of the following is an AWS Cloud architecture design principle?
- [ ] A. Implement single points of failure
- [x] B. Implement loose coupling
- [ ] C. Implement monolithic design
- [ ] D. Implement vertical scaling

Q51. A company already has an on-premises data center but wants to integrate some workloads with AWS services while keeping sensitive data locally. Which deployment model should the company use?
- [ ] A. Public Cloud
- [ ] B. Private Cloud
- [x] C. Hybrid Cloud
- [ ] D. Community Cloud

Q52. A startup launches a new online course platform. During enrollment periods, the number of users increases dramatically, but outside the enrollment season traffic is very low. The company wants infrastructure that can automatically scale up during high demand and scale down when demand decreases. Which cloud characteristic BEST addresses this requirement?
- [ ] A. Broad Network Access
- [x] B. Rapid Elasticity
- [ ] C. Resource Pooling
- [ ] D. Measured Service

Q53. A company wants to avoid large upfront costs for servers and data centers and prefers paying only for the resources they use. Which cloud advantage supports this business goal?
- [ ] A. Global reach
- [x] B. Trade fixed expense for variable expense
- [ ] C. Resource pooling
- [ ] D. Broad network access

Q54. Currently, your company (a FinTech company working with stock market data) has its servers (EC2) and databases (RDS) hosted in Tokyo. To ensure that your application does not go down if the entire Tokyo region experiences a natural disaster (such as an earthquake), while also reducing network latency for customers in London (Europe), which architecture should you choose?
- [ ] A. Single AZ
- [ ] B. Multi-AZ
- [x] C. Multi-Region
- [ ] D. Edge-only

Q55. Which of the following is NOT a characteristic of an AWS Region?
- [ ] A. It consists of multiple Availability Zones (AZs) located within the same geographic area.
- [ ] B. The resources and infrastructure within a Region are fully isolated from other Regions.
- [x] C. It shares the same physical networking infrastructure with nearby Regions for risk redundancy.
- [ ] D. The Availability Zones within a Region are connected through low-latency networks.

Q56. When building an Electronic Emergency Medical Records system on the AWS platform, the system stores extremely sensitive personal patient information. At the same time, because it is used in an emergency clinic, doctors require that patient medical records be retrieved almost instantly in order to make life-saving decisions. The project is also allocated a limited monthly budget for ongoing operations. Based on the key factors used when selecting an AWS Region, which of the following options represents the most appropriate priority order (from most important to least important) for the system architecture?
- [ ] A. Cost Optimization -> Service Availability -> Latency Optimization -> Compliance
- [ ] B. Latency Optimization -> Compliance -> Cost Optimization -> Service Availability
- [x] C. Compliance -> Latency Optimization -> Service Availability -> Cost Optimization
- [ ] D. Service Availability -> Compliance -> Latency Optimization -> Cost Optimization

Q57. A company deploys its application across multiple Availability Zones (AZs) behind an Application Load Balancer (ALB). What does this primarily provide?
- [ ] A. Lower storage cost
- [ ] B. Global caching
- [x] C. High availability
- [ ] D. Cross-region disaster recovery

Q58. Which statement best describes an Availability Zone?
- [ ] A. A single data center globally shared
- [x] B. Multiple isolated data centers in one Region
- [ ] C. A globally distributed caching system
- [ ] D. A logical network boundary

Q59. Which architecture pattern provides the highest level of resilience?
- [ ] A. Single AZ
- [ ] B. Multi-AZ
- [x] C. Multi-Region
- [ ] D. Edge-only

Q60. An application is designed to run on EC2 instances across 2 different Availability Zones (Multi-AZ). However, both instances read/write data to a single EBS volume. Does this design truly provide High Availability (HA) for the system?
- [ ] A. Yes, because the compute power is distributed across two independent AZs
- [ ] B. No because the distance between AZs will increase data read/write latency
- [ ] C. Yes, because AWS automatically replicates EBS volumes to all other AZs in a Region
- [x] D. No, because an EBS volume is a zonal resource, creating a 'Single Point of Failure'

Q61. Which cloud concept describes the ability to automatically acquire resources as needed and release them when they are no longer required to match demand?
- [ ] A. Reliability
- [ ] B. High Availability
- [x] C. Elasticity
- [ ] D. Durability

Q62. Which of the following components is the customer responsible for managing in the Platform as a Service (PaaS) model?
- [ ] A. Operating Systems (OS)
- [x] B. Applications and Data
- [ ] C. Networking and Storage
- [ ] D. Virtualization

Q63. A company wants full control over its infrastructure and hosts its servers inside its own building. Which deployment model is being used?
- [ ] A. Public Cloud
- [ ] B. Hybrid Cloud
- [ ] C. Edge Computing
- [x] D. Private Cloud (On-premises)

Q64. What is an AWS Region?
- [ ] A. A single data center located in a major city.
- [x] B. A physical geographic area that contains multiple Availability Zones.
- [ ] C. A collection of Edge Locations used for content caching.
- [ ] D. A virtual network boundary for your AWS resources.

Q65. What is the primary purpose of an AWS Edge Location?
- [ ] A. To host primary compute workloads like EC2 instances.
- [ ] B. To provide long-term archival storage for data.
- [x] C. To deliver content closer to end-users to reduce latency.
- [ ] D. To provide synchronous data replication between Regions.

Q66. Which Disaster Recovery (DR) strategy involves keeping a minimal, scaled-down version of a functional environment always running in a secondary Region?
- [ ] A. Backup and Restore
- [ ] B. Pilot Light
- [x] C. Warm Standby
- [ ] D. Multi-Site (Active-Active)

Q67. A European fintech company must comply with strict GDPR data residency requirements that mandate customer data must be stored within a specific country's legal jurisdiction. What is the most critical factor for them when setting up their AWS environment?
- [ ] A. Selecting the Region with the lowest pricing for S3 storage.
- [ ] B. Ensuring they have the maximum number of AZs available in their chosen continent.
- [x] C. Selecting the specific AWS Region located within the required geographic/legal boundary.
- [ ] D. Using IAM policies to restrict global access to their data.

Q68. Why is synchronous data replication typically limited to a Multi-AZ architecture rather than a Multi-Region architecture?
- [ ] A. Because Edge Locations do not support synchronous protocols.
- [ ] B. Because AWS does not allow data transfer between different Regions.
- [x] C. Because the physical distance between Regions introduces latency that makes synchronous sync difficult.
- [ ] D. Because Regional services like Amazon RDS cannot operate in multiple AZs.

Q69. Under the Shared Responsibility Model, which task is a customer's responsibility when using Infrastructure as a Service (IaaS) but becomes AWS's responsibility when using a managed Platform as a Service (PaaS)?
- [ ] A. Physical security of the data center
- [x] B. Patching the guest operating system
- [ ] C. Maintaining the virtualization layer
- [ ] D. Disposal of physical storage disks

Q70. A company wants to ensure its application remains operational even if an entire data center facility within a Region fails. Which architecture should they implement?
- [ ] A. Single-AZ deployment with higher-capacity servers.
- [x] B. Multi-AZ deployment within the same Region.
- [ ] C. Deploying the application in a single Edge Location.
- [ ] D. Moving the entire workload to an on-premises Private Cloud.

Q71. Which of the following businesses is better suited for using On-premise infrastructure rather than Cloud computing?
- [ ] A. A video streaming business with rapid, seasonal growth in viewership.
- [ ] B. A startup that lacks the capital to invest in its own data center.
- [x] C. A commercial bank with a large, stable customer base that must strictly comply with data security regulations.
- [ ] D. An e-commerce company that frequently runs high-traffic flash sales.

Q72. A company operates in a geographic area with high political instability. Which AWS deployment strategy should they choose to ensure maximum business continuity and resilience?
- [ ] A. Deploy the application across all Availability Zones within one Region
- [ ] B. Deploy the application on a single On-premise server with a backup on AWS S3.
- [x] C. Deploy the application across multiple AWS Regions
- [ ] D. Use a single Edge Location to host the entire application infrastructure.

Q73. When should a business prioritize choosing Platform as a Service (PaaS)?
- [ ] A. When the business needs to rent raw virtual servers to install operating systems and configure networks from scratch.
- [ ] B. When the business wants to provide complete software to end-users without any source code customization.
- [x] C. When the business wants to focus entirely on developing, running, and managing applications without worrying about maintaining the underlying infrastructure (OS, storage, networking).
- [ ] D. When the business requires total control over physical hardware and data center cooling systems.

Q74. You ONLY want to manage Applications and Data. Which type of Cloud Computing model should you use?
- [ ] A. On-Premises
- [ ] B. Infrastructure as a Service (IaaS)
- [ ] C. Software as a Service (SaaS)
- [x] D. Platform as a Service (PaaS)

Q75. Which Global Infrastructure identity is composed of one or more discrete data centers with redundant power, networking, and connectivity, and are used to deploy infrastructure?
- [ ] A. Edge Locations
- [x] B. Availability Zones
- [ ] C. Regions
- [ ] D. Local Zones

Q76. Which of the following is NOT one of the Five Characteristics of Cloud Computing?
- [ ] A. Rapid elasticity and scalability
- [ ] B. Multi-tenancy and resource pooling
- [x] C. Dedicated Support Agent to help you deploy applications
- [ ] D. On-demand self service

Q77. In Disaster Recovery (DR) strategies, which of the following characteristics distinguishes the "Pilot Light" model from the "Warm Standby" model?
- [x] A. Core resources (such as databases) are always running, but other components are only created after a disaster occurs.
- [ ] B. Data is only periodically saved as backups, and no resources are running.
- [ ] C. The entire system is fully replicated and runs in parallel in an Active-Active state.
- [ ] D. A reduced version of the entire system is always running and ready to handle low traffic.

Q78. In the physical infrastructure of AWS, how is each Availability Zone (AZ) designed to ensure fault isolation?
- [x] A. It has independent power supplies, cooling systems, and networking infrastructure.
- [ ] B. They share one large data center, but it is divided into different rooms.
- [ ] C. Each AZ is located in a different country to ensure legal safety.
- [ ] D. They are connected to other AZs through the public internet to ensure independence.

Q79. An organization is moving from Infrastructure as a Service (IaaS) to Platform as a Service (PaaS) to host their web application. Which of the following tasks will the organization NO LONGER be responsible for after this migration?
- [ ] A. Managing user access and identity (IAM).
- [ ] B. Configuring the application code and business logic.
- [x] C. Patching and maintaining the underlying Operating System (OS).
- [ ] D. Ensuring the security of the data stored within the application.

Q80. Under the Shared Responsibility Model, when an organization migrates to a Software as a Service (SaaS) solution, which of the following remains a primary responsibility of the customer?
- [ ] A. Physical security of the data center.
- [ ] B. Updating and patching the operating system.
- [x] C. Managing data access permissions and user identities.
- [ ] D. Maintaining the underlying network infrastructure.

Q81. Which AWS Cloud characteristic allows customers to scale resources up or down automatically based on demand?
- [ ] A. Resource pooling
- [x] B. Rapid elasticity
- [ ] C. Broad network access
- [ ] D. Measured service

Q82. Which AWS service is considered a global service?
- [ ] A. Amazon EC2
- [ ] B. Amazon RDS
- [x] C. AWS IAM
- [ ] D. Amazon S3

Q83. What is the primary purpose of AWS Edge Locations?
- [ ] A. Run virtual machines
- [ ] B. Store relational databases
- [x] C. Cache content closer to users to reduce latency
- [ ] D. Host application servers

Q84. Which cloud service model allows customers to manage operating systems and applications, while AWS manages the underlying infrastructure?
- [ ] A. SaaS
- [ ] B. PaaS
- [x] C. IaaS
- [ ] D. On-premises

Q85. Which AWS infrastructure component provides geographic isolation?
- [ ] A. Availability Zone
- [x] B. Region
- [ ] C. Edge location
- [ ] D. Data center

Q86. What best describes the concept of scalability?
- [ ] A. The ability for a system to withstand a certain amount of failure and still remain functional
- [x] B. The ability for a system to grow in size, capacity, and/or scope
- [ ] C. The ability for a system to grow and shrink based on demand
- [ ] D. The ability for a system to be accessible when you attempt to access it

Q87. What is the goal of High Availability architecture?
- [x] A. Minimize downtime
- [ ] B. Reduce cost
- [ ] C. Increase storage capacity
- [ ] D. Simplify deployment

Q88. A company wants to deploy an application for users in Vietnam and Southeast Asia. Which AWS Region would most likely provide the lowest latency?
- [ ] A. us-east-1 (N. Virginia)
- [ ] B. ap-south-1 (Mumbai)
- [ ] C. eu-west-1 (Ireland)
- [x] D. ap-southeast-1 (Singapore)

Q89. A company wants to improve application availability within a single region. Which architecture should they implement?
- [x] A. Deploy instances in multiple AZs
- [ ] B. Deploy instances in a single AZ
- [ ] C. Deploy in a single EC2 instance
- [ ] D. Deploy using only edge locations

Q90. An application stores frequently accessed static images globally. Which AWS service can cache these images near users?
- [ ] A. RDS
- [x] B. CloudFront
- [ ] C. EC2
- [ ] D. EBS

Q91. A company is migrating its application from an on-premises infrastructure to the cloud to improve high availability and reduce infrastructure management overhead. The company decides to run its application on Amazon EC2. According to the Shared Responsibility Model of Amazon Web Services, which of the following responsibilities belongs to the customer?
- [ ] A. Maintaining the physical servers in AWS data centers
- [x] B. Managing and patching the operating system running on the EC2 instance
- [ ] C. Ensuring the availability of the underlying AWS networking infrastructure
- [ ] D. Maintaining the cooling systems and power supply in AWS data centers

Q92. Which of the 'Six Advantages of Cloud Computing' specifically addresses the ability of a company to avoid over-provisioning or under-provisioning based on workload estimates?
- [ ] A. Trade fixed expense for variable expense
- [ ] B. Benefit from massive economies of scale
- [x] C. Stop guessing capacity
- [ ] D. Go global in minutes

Q93. Over Night is a startup that provides event management and online ticket distribution services. The company wants to avoid large upfront investments in hardware, quickly launch its platform, and automatically scale resources to handle sudden increases in demand. Which solution would BEST meet these requirements?
- [ ] A. Build an on-premises data center and purchase enough servers to handle the highest expected traffic
- [ ] B. Use a co-location data center and manage all physical servers and networking infrastructure internally.
- [x] C. Deploy the application in the AWS Cloud using scalable services that automatically adjust capacity based on demand.
- [ ] D. Purchase several physical servers and host the application in the company's office.

Q94. A healthcare company is working with sensitive patient records which is currently stored in an on-premise way. The company intends to extend globally and expecting high demand due to the computational resource of upcoming AI usage for medical image analysis. Which architecture should the company choose?
- [ ] A. Build more on-premise data center over the globe for expansion and security.
- [ ] B. Move everything to cloud for easy expand and scale as well as lower latency due to powerful pre-installed infrastructure.
- [ ] C. Keep everything on-premise for full control and security.
- [x] D. Build a hybrid model where keeping patient record on-premise while computational resource utilizing cloud infrastructure.

Q95. A global e-learning platform stores videos in S3 in the Tokyo Region. Students from Europe complain about slow loading times. Which solution BEST improves performance for these users while keeping data in the same Region?
- [ ] A. Deploy in a single AZ with Auto Scaling only
- [x] B. Deploy across multiple AZs behind an Application Load Balancer
- [ ] C. Deploy in two different Regions without load balancing
- [ ] D. Use CloudFront Edge Locations to host the system directly

Q96. A global e-learning platform stores videos in S3 in the Tokyo Region. Students from Europe complain about slow loading times. Which solution BEST improves performance for these users while keeping data in the same Region?
- [ ] A. Move S3 buckets to a European Region only
- [ ] B. Enable Multi-AZ for the S3 bucket
- [x] C. Use CloudFront with Edge Locations to cache video content closer to users
- [ ] D. Create a second S3 bucket in Europe and manually sync data daily

Q97. You are acting as a Solution Architect for an online retail corporation. During a briefing, the Customer Service department reported that the website frequently experiences high latency during traffic peaks, leading to a high cart abandonment rate. Additionally, the Chief Financial Officer (CFO) requires the new solution to be cost-optimized and operationally simple. The business has defined the following technical requirements: 1. Performance: Internal network latency must be extremely low (< 10ms) for real-time transaction processing. 2. Availability: If a data center experiences a hardware failure, the system must automatically fail over immediately without impacting the customer experience. 3. Scope: Currently, the customer base is primarily concentrated within a single country. Which architecture would you propose as the MOST optimal solution?
- [ ] A. Deploy a Multi-Region (Global Resilience) architecture to ensure the system remains operational even during a regional disaster.
- [x] B. Deploy a Single-Region, Multi-AZ architecture using an Active/Active configuration and Synchronous Replication.
- [ ] C. Use a Hybrid Cloud model by placing payment servers at the corporate headquarters to reduce cloud operational costs.
- [ ] D. Deploy the application across multiple Edge Locations to ensure fast access for customers from any geographic location.

Q98. A company deploys its Amazon EC2 instances across 2 AZs within a Region. A load balancer automatically routes traffic to healthy instances. The database is replicated across the same two AZs. Which statement is the most correct one?
- [ ] A. The architecture is Fault Tolerance because it can still operate when one AZ fails.
- [ ] B. The architecture is not Highly Available, because it runs only in a single Region.
- [ ] C. The architecture provides Global Resilience, because multiple Availability Zones are used.
- [x] D. The architecture provides High Availability, but not Fault Tolerance, because the system may experience brief downtime during failover.

Q99. A company needs to ensure its application can survive a catastrophic event that takes down an entire AWS Region. Which design strategy provides the highest level of resilience and the lowest Recovery Time Objective?
- [ ] A. Deploying the application across multiple Availability Zones with an Application Load Balancer.
- [x] B. Implementing a Multi-Region Active-Active strategy with Route 53 for global traffic routing.
- [ ] C. Setting up a Pilot Light environment in a different Availability Zone within the same Region.
- [ ] D. Using CloudFront to cache content at Edge Locations to prevent regional service interruption

Q100. Which component of the AWS global infrastructure is made up of one or more discrete data centers that have redundant power, networking, and connectivity?
- [ ] A. AWS Region
- [x] B. Availability Zone
- [ ] C. Edge location
- [ ] D. AWS Outposts

Q101. In a Platform as a Service (PaaS) model, which of the following layers is the customer responsible for managing?
- [ ] A. Operating System and Virtualization
- [x] B. Applications and Data
- [ ] C. Runtime and Middleware
- [ ] D. Servers and Storage

Q102. A company wants to run native AWS services, APIs, and tools locally in their own physical data center. Which service enables this hybrid cloud architecture?
- [ ] A. Amazon Bedrock
- [ ] B. AWS Elastic Beanstalk
- [x] C. AWS Outposts
- [ ] D. Amazon RDS

Q103. Which deployment model requires fixed upfront costs and assigns the responsibility of system updates entirely to the enterprise's internal technical team?
- [ ] A. Public Cloud
- [ ] B. Hybrid Cloud
- [ ] C. Serverless
- [x] D. On-Premises

Q104. What is the term for a single component, node, or process in a system that, if it experiences an outage, causes the entire system to stop functioning or crash?
- [x] A. Single Point of Failure (SPOF)
- [ ] B. Loose Coupling
- [ ] C. Isolated Data Center
- [ ] D. Monolithic Architecture

Q105. Which deployment strategy do highly agile tech companies like Netflix, Spotify, and Airbnb primarily utilize to achieve massive economies of scale and global reach?
- [ ] A. Pure On-Premises
- [ ] B. Hybrid Cloud
- [x] C. Public Cloud
- [ ] D. Isolated Data Centers

Q106. When using an Infrastructure as a Service (IaaS) provider, which specific layers are managed strictly by the cloud provider rather than the customer?
- [ ] A. Applications, Data, and Runtime
- [ ] B. Operating System, Middleware, and Runtime
- [x] C. Servers, Storage, Networking, and Virtualization
- [ ] D. Applications, OS, and Virtualization

Q107. A fintech startup is legally required to ensure that all customer financial data physically remains within the borders of a specific country to comply with government regulations. Which AWS infrastructure concept is primarily used to address this data residency requirement?
- [ ] A. Edge Locations
- [x] B. AWS Regions
- [ ] C. High Availability
- [ ] D. Amazon Route 53

Q108. How are Availability Zones physically and logically connected to one another within a single AWS Region?
- [ ] A. Through the public internet using encrypted VPN tunnels
- [ ] B. Through distributed global Edge Locations
- [x] C. With high-bandwidth, low-latency network links
- [ ] D. Using isolated, asynchronous satellite connections

Q109. A company maintains a scaled-down but fully functional version of their production environment running at all times in an alternate location for disaster preparedness. Which Disaster Recovery (DR) approach does this describe?
- [ ] A. Backup and Restore
- [ ] B. Pilot Light
- [x] C. Warm Standby
- [ ] D. Multi-Site (Active-Active)

Q110. Which cloud service model provides the highest level of control over the operating system and installed applications?
- [ ] A. SaaS (Software as a Service)
- [ ] B. PaaS (Platform as a Service)
- [x] C. IaaS (Infrastructure as a Service)
- [ ] D. FaaS (Function as a Service)

Q111. Which statement best describes the difference between CAPEX and OPEX in cloud computing?
- [ ] A. CAPEX refers to paying only for resources used, while OPEX requires upfront investment.
- [x] B. CAPEX requires large upfront investment in infrastructure, while OPEX allows paying for resources as they are consumed.
- [ ] C. CAPEX and OPEX are identical cost models used in cloud computing.
- [ ] D. OPEX requires purchasing physical servers before deployment.

Q112. What is the main purpose of an Availability Zone (AZ) in the AWS global infrastructure?
- [ ] A. To provide a global endpoint for all AWS services
- [x] B. To isolate infrastructure failures within a region and improve high availability
- [ ] C. To connect AWS to on-premises data centers
- [ ] D. To provide edge caching for content delivery

Q113. Which of the following identifiers is an example of an AWS Region?
- [ ] A. Edge-Location-Tokyo
- [ ] B. aws-global-1
- [ ] C. us-east-1a
- [x] D. us-east-1

Q114. How are Availability Zones (AZs) within the same Region connected?
- [ ] A. High-bandwidth satellite network
- [x] B. Private internal network with low latency (< 2 ms)
- [ ] C. Only when backup is required
- [ ] D. Through the public Internet

Q115. Which service is used to efficiently route users to AWS resources globally?
- [x] A. Amazon Route 53
- [ ] B. Amazon VPC
- [ ] C. Amazon EC2
- [ ] D. AWS Lambda

Q116. A Japanese company hosts their applications on Amazon EC2 instances in the Tokyo Region. The company has opened new branches in the United States, and the users are complaining of high latency. What can the company do to reduce latency for the users in the US while minimizing costs?
- [ ] A. Applying the Amazon Connect latency-based routing policy.
- [ ] B. Registering a new US domain name to serve the users in the US.
- [ ] C. Building a new data center in the US and implementing a hybrid model.
- [x] D. Deploying new Amazon EC2 instances in a Region located in the US.

Q117. The ability to horizontally scale Amazon EC2 instances based on demand is an example of which concept?
- [ ] A. Economy of scale
- [ ] B. High Availability
- [ ] C. Disaster recovery
- [x] D. Elasticity

Q118. One of the most important AWS best-practices to follow is the cloud architecture principle of elasticity. How does this principle improve your architecture's design?
- [ ] A. By automatically scaling your on-premises resources based on demand.
- [ ] B. By automatically scaling your AWS resources using an Elastic Load Balancer.
- [ ] C. By reducing interdependencies between application components wherever possible.
- [x] D. By automatically provisioning the required AWS resources based on changes in demand

Q119. A company is considering migrating its on-premises data centre to Amazon Web Services to reduce costs and improve scalability. Which of the following is a primary benefit of adopting the AWS Cloud, as outlined in the AWS Well-Architected Framework?
- [ ] A. Increased hardware maintenance responsibilities
- [ ] B. Fixed pricing for all compute resources
- [x] C. High availability and elasticity
- [ ] D. Mandatory coding for all deployments

Q120. A company has a Linux server located in its office. Employees log in to the server using SSH to run code and process data. The server is manually administered by the IT department. What is the most accurate description of this system?
- [ ] A. Private cloud
- [ ] B. Public cloud
- [x] C. Traditional on-premise server
- [ ] D. Hybrid cloud

Q121. Which tasks are AWS responsibilities according to the AWS Shared Responsibility Model?
- [x] A. Patching networking devices
- [ ] B. Defining user password policies
- [ ] C. Configuring security groups
- [ ] D. Patching an EC2 instance operating system

Q122. Who is responsible for decommissioning underlying storage devices that reach the end of their useful life used to host data on AWS?
- [ ] A. Customer
- [x] B. AWS
- [ ] C. Account creator
- [ ] D. Auditing team

Q123. Which of the following is a customer responsibility, according to the AWS Shared Responsibility Model?
- [x] A. Identity access management
- [ ] B. Hard drive disposal
- [ ] C. Data center hardware security
- [ ] D. Availability zone security

Q124. A company runs a e-commerce web application on AWS. During a large sales event, the traffic increases by 10 times and the system automatically launches additional servers to handle the load. After the event ends, the extra servers are automatically terminated. Which AWS characteristic is best represented in this scenario?
- [ ] A. Resource pooling
- [x] B. Rapid elasticity
- [ ] C. Measured service
- [ ] D. Broad network access

Q125. A company is moving a legacy application to AWS. In the past, they had to purchase $50,000 worth of hardware every 3 years to ensure they had enough "headroom" for growth, yet 40% of that hardware remain undo most of the time. Which specific AWS Cloud Advantage directly addresses this inefficiency?
- [ ] A. Go global in minutes
- [ ] B. Benefit from massive economies of scale
- [x] C. Stop guessing capacity
- [ ] D. Increase speed and agility

Q126. A company is comparing the costs of running their own data center versus moving to AWS. They realize that because AWS serves hundreds of thousands of customers, AWS can purchase hardware at much lower costs than the company ever could. This leads to lower prices for the company. Which cloud advantage is this?
- [ ] A. Trade capital expense for variable expense
- [ ] B. Stop guessing capacity
- [ ] C. Increase speed and agility
- [x] D. Benefit from massive economies of scale

Q127. A development team wants to deploy a web application. They do not want to manage the operating system or the runtime, but they want to keep full control over the application's environment configuration and code versions. Which service model fits best?
- [ ] A. SaaS
- [x] B. PaaS
- [ ] C. On-premise
- [ ] D. IaaS

Q128. Which AWS Cloud feature enables users to have the ability to pay based on current needs, rather than projected needs?
- [ ] A. AWS Budgets
- [x] B. Pay-as-you-go pricing
- [ ] C. Volume discounts
- [ ] D. Saving Plans

Q129. Which AWS service acts as the global DNS service that directs users to different AWS resources?
- [ ] A. Amazon Cloudfront
- [x] B. Amazon Route 53
- [ ] C. Elastic Load Balacing
- [ ] D. AWS Global Accelerator

Q130. Under the AWS Shared Responsibility Model, if a customer's Amazon EC2 instance is hacked because the guest operating system was not updated with the latest security patches, who is responsible?
- [ ] A. AWS, because they own the physical hardware.
- [x] B. The Customer, because they are responsible for patching the guest OS.
- [ ] C. Both AWS and the Customer share the responsibility for OS patching.
- [ ] D. The Operating System vendor (e.g., Microsoft or Linux provider).

Q131. A company wants to move to AWS to reduce their Total Cost of Ownership (TCO). Which of the following is an example of moving from Capital Expenditure (CAPEX) to Operational Expenditure (OPEX)?
- [ ] A. Signing a 10-year lease for a new data center facility.
- [ ] B. Buying high-end physical servers and networking gear upfront.
- [x] C. Paying only for the compute power used each month.
- [ ] D. Hiring a large team of hardware maintenance engineers.

Q132. "An ecommerce company has migrated its IT infrastructure from an on-premises data center to the AWS Cloud. Which cost is the company's direct responsibility?
- [x] A. Cost of application software licenses
- [ ] B. Cost of power for the AWS servers
- [ ] C. Cost of the hardware infrastructure on AWS
- [ ] D. Cost of physical security for the AWS data center

Q133. Which option is a physical location of the AWS global infrastructure?
- [ ] A. AWS DataSync
- [ ] B. Amazon Connect
- [x] C. AWS Region
- [ ] D. AWS Organizations

Q134. An AI startup is training deep learning models with continuously changing data and needs to experiment with different types of hardware (A100, H100 GPUs) in a short period of time. Based on the characteristics of cloud computing, why should they choose the cloud instead of building their own internal GPU farm?
- [ ] A. Because cloud computing provides full control over both the physical and virtualization layers for engineering teams.
- [ ] B. To optimize CAPEX costs by making long-term investments in hardware.
- [ ] C. To ensure that data is always stored on-premise in order to comply with the strictest security regulations.
- [x] D. To leverage Agility and Stop Guessing Capacity so they can instantly change hardware configurations according to their experimentation needs.

Q135. A large financial corporation has strict regulations requiring that sensitive data must not leave national borders, but it still wants to use advanced AI services from AWS to analyze data on-site. Which architecture solution is the most optimal?
- [ ] A. Build a private cloud that is completely isolated from the Internet.
- [ ] B. Migrate the entire system to the public cloud and encrypt the data.
- [x] C. Use AWS Outposts to run AWS services directly within their internal data center.
- [ ] D. Use a SaaS model for all financial applications.
