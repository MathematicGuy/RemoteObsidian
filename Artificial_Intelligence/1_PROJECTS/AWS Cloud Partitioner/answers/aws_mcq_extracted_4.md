### AWS Cloud Practitioner Practice Questions (Set 4)

Q1. Which AWS service is specifically designed to allow you to centrally govern and manage multiple AWS accounts?
- [x] A. AWS Organizations
- [ ] B. AWS Cost Explorer
- [ ] C. IAM Identity Center
- [ ] D. Amazon EventBridge

Q2. Which AWS service allows a user to set custom alerts that will notify them via email or SNS when their AWS usage or spending exceeds a predefined threshold?
- [ ] A. AWS Cost Explorer
- [ ] B. AWS Trusted Advisor
- [x] C. AWS Budgets
- [ ] D. AWS Cost Anomaly Detection

Q3. Which service natively supports automatic rotation of database credentials?
- [x] A. AWS Secrets Manager
- [ ] B. AWS Certificate Manager
- [ ] C. SSM Parameter Store
- [ ] D. AWS KMS

Q4. Which of the following is a common threat that AWS WAF protects against?
- [ ] A. Unencrypted EBS volumes
- [x] B. SQL Injection
- [ ] C. SYN Floods
- [ ] D. Unauthorized OS logins

Q5. Which of the following services uses machine learning to continuously monitor for malicious activity and unauthorized behavior?
- [ ] A. AWS Macie
- [ ] B. AWS KMS
- [x] C. Amazon GuardDuty
- [ ] D. AWS CloudTrail

Q6. Which service automatically scans Amazon S3 buckets to discover and protect sensitive data like Personally Identifiable Information (PII)?
- [ ] A. Amazon Inspector
- [ ] B. Amazon GuardDuty
- [x] C. Amazon Macie
- [ ] D. AWS Secrets Manager

Q7. Which service enables automated vulnerability scanning of Amazon EC2 instances and container images in Amazon ECR?
- [ ] A. Amazon GuardDuty
- [x] B. Amazon Inspector
- [ ] C. AWS Config
- [ ] D. AWS WAF

Q8. According to the principle of "Least Privilege", how should permissions be granted in AWS?
- [ ] A. Grant users full administrator access to avoid permission errors.
- [x] B. Grant users only the specific permissions necessary to perform their required tasks.
- [ ] C. Apply the same permissions to all users in the account using a single IAM Group.
- [ ] D. Allow all users access to the root account for emergencies.

Q9. What is described as a 'non-negotiable' requirement to accurately track and attribute costs to different business units or projects?
- [ ] A. Running all workloads in a single VPC
- [ ] B. Using Amazon S3 Intelligent-Tiering
- [ ] C. Enabling AWS CloudTrail
- [x] D. Implementing Cost Allocation Tags

Q10. A company wants to implement detailed tracking of its cloud costs by department and project. Which AWS feature or service should the company use?
- [ ] A. AWS Marketplace
- [ ] B. AWS Budgets
- [x] C. Cost allocation tags
- [ ] D. Consolidated billing

Q11. In the context of AWS Cost Breakdown, how is data transfer generally billed?
- [ ] A. Both inbound and outbound data transfers are completely free.
- [ ] B. Both inbound and outbound data transfers are always charged at the same rate.
- [x] C. Inbound data transfer (data into AWS) is generally free, while outbound data transfer (data out to the internet) is charged.
- [ ] D. Outbound data transfer is free, while inbound data transfer is charged.

Q12. Your company plans to run a steady-state database on Amazon EC2 continuously for the next 3 years. To optimize costs and get the highest possible discount compared to On-Demand pricing, which purchasing option should you apply?
- [ ] A. Spot Instances
- [x] B. Reserved Instances (or Savings Plans)
- [ ] C. Dedicated Hosts
- [ ] D. On-Demand Instances

Q13. A startup is planning to migrate their on-premises infrastructure to AWS. Before migrating, management wants to estimate the total expected monthly AWS bill for their designed architecture (including EC2, S3, and RDS). Which tool is best suited for this scenario?
- [x] A. AWS Pricing Calculator
- [ ] B. AWS Cost Explorer
- [ ] C. AWS Billing and Cost Management Console
- [ ] D. AWS Inspector

Q14. A data processing application runs on EC2 and processes batch jobs. These jobs are flexible, meaning they can start and stop at any time, and can be interrupted without affecting the final result. Which EC2 pricing model provides the most cost-effective solution for this specific scenario?
- [x] A. Spot Instances
- [ ] B. Reserved Instances
- [ ] C. On-Demand Instances
- [ ] D. Savings Plans

Q15. An enterprise wants to simplify its billing process by combining the AWS usage of its 10 different departments into a single monthly invoice. They also want to take advantage of volume pricing discounts across all departments. Which AWS feature should they use to achieve this?
- [ ] A. AWS Cost Categories
- [x] B. Consolidated Billing (AWS Organizations)
- [ ] C. AWS Resource Access Manager (RAM)
- [ ] D. AWS Budgets

Q16. A company uses AWS Organizations to manage multiple accounts. They have a central "production" account and a member account for training. A user in the training account attempts to create an S3 bucket inside the "production" account but receives an "Access Denied" error. What is the primary cause of this issue?
- [ ] A. S3 bucket names must be globally unique across all AWS accounts.
- [x] B. The user lacks the appropriate cross-account IAM permissions/permission sets to create resources in the production account.
- [ ] C. The production account has reached its maximum billing limit.
- [ ] D. Consolidated billing is not enabled.

Q17. Your FinOps team wants to implement a proactive cost monitoring strategy. They need to receive an email alert automatically whenever their forecasted monthly AWS spending exceeds $1,000. Which service should they configure?
- [ ] A. AWS Cost Explorer
- [ ] B. AWS Trusted Advisor
- [x] C. AWS Budgets
- [ ] D. AWS Organizations

Q18. Your DevSecOps team is setting up a CI/CD pipeline. They want to ensure that container images do not contain known software vulnerabilities before being deployed to Amazon Elastic Container Registry (ECR). Which of the following solutions best meets this requirement automatically?
- [x] A. Enable Amazon Inspector to automatically scan container images (Amazon ECR).
- [ ] B. Configure AWS WAF on the Application Load Balancer.
- [ ] C. Set up Network Firewall for the Docker environment.
- [ ] D. Run Amazon Macie to analyze source code inside the container.

Q19. To meet data retention and compliance requirements in DevSecOps, a company needs to record the entire history of API calls made within their AWS account. Which service should you apply?
- [ ] A. Amazon Inspector
- [ ] B. Amazon Macie
- [ ] C. AWS Systems Manager
- [x] D. AWS CloudTrail

Q20. According to the Shared Responsibility Model, which of the following tasks is the responsibility of the CUSTOMER when using Amazon EC2?
- [ ] A. Physical security of AWS data centers.
- [x] B. OS patching and installing antivirus software on the instance.
- [ ] C. Maintaining AWS network hardware and routers.
- [ ] D. Safely disposing of broken server hard drives.

Q21. Which service should you use to protect your web applications from common exploits such as SQL Injection or Cross-Site Scripting (XSS)?
- [x] A. AWS WAF (Web Application Firewall)
- [ ] B. AWS Shield
- [ ] C. Network ACL
- [ ] D. Amazon Inspector

Q22. Regarding networking costs in AWS, which of the following actions typically does NOT incur data transfer charges?
- [ ] A. Data transfer between two different Regions.
- [ ] B. Data transfer from AWS to the Internet (Outbound Data Transfer).
- [x] C. Data transfer from the Internet to AWS (Inbound Data Transfer).
- [ ] D. Data transfer between two different Availability Zones (AZs) within the same Region.

Q23. Which pricing model is most suitable for a developer who needs to run a short-term, unpredictable testing workload for only a few hours?
- [ ] A. Savings Plans
- [ ] B. Reserved Instances
- [ ] C. Spot Instances
- [x] D. On-Demand Instances

Q24. According to the "Pay-as-you-go" principle, which of the following is considered a primary driver of S3 storage costs?
- [ ] A. IAM User count
- [x] B. Data Transfer OUT
- [ ] C. Instance Runtime
- [ ] D. Number of AWS accounts

Q25. Which AWS tool allows you to visualize and forecast your monthly spend while grouping costs by service or linked accounts?
- [ ] A. AWS Budgets
- [ ] B. AWS Organizations
- [x] C. AWS Cost Explorer
- [ ] D. AWS CloudWatch

Q26. Which AWS pricing principle suggests that customers should "pay less by using more," as seen in tiered S3 storage pricing?
- [ ] A. Economies of Scale
- [ ] B. Pay-as-you-go
- [ ] C. On-Demand Pricing
- [x] D. Volume Discounts

Q27. What is a significant risk for companies that do NOT implement cost allocation tags on their AI models?
- [ ] A. They cannot choose an AWS Region.
- [x] B. They cannot attribute spend or identify wasted resources.
- [ ] C. They will be unable to use Amazon S3.
- [ ] D. Their AWS Support Plan will be automatically downgraded.

Q28. A company wants to allow an application running on an EC2 instance to access S3 securely without embedding access keys in the code. What is the BEST solution?
- [ ] A. Create an IAM user and store credentials in the application
- [x] B. Use an IAM role attached to the EC2 instance
- [ ] C. Store credentials in environment variables
- [ ] D. Store credentials in environment variables

Q29. A company needs to manage permissions for multiple developers who require the same level of access to AWS resources. What is the MOST efficient approach?
- [ ] A. Assign policies individually to each IAM user
- [ ] B. Create IAM roles for each developer
- [x] C. Create an IAM group and attach policies to the group
- [ ] D. Share one IAM user among developers

Q30. A company wants to enforce that all data stored in S3 is encrypted using customer-managed keys with full control over key rotation. Which service should they use?
- [ ] A. AWS Certificate Manager
- [x] B. AWS Key Management Service (KMS)
- [ ] C. Amazon Inspector
- [ ] D. AWS Shield

Q31. A company wants to analyze EC2 instances for vulnerabilities and unintended network exposure. Which AWS service should they use?
- [x] A. Amazon Inspector
- [ ] B. AWS Shield
- [ ] C. AWS WAF
- [ ] D. AWS IAM

Q32. A company uses multiple AWS accounts and wants to centrally manage security policies and billing. What should they use?
- [x] A. AWS Organizations
- [ ] B. AWS Config
- [ ] C. IAM roles
- [ ] D. IAM groups

Q33. A company wants to encrypt sensitive data stored in an RDS database and ensure that encryption keys are rotated automatically. Which solution should they choose?
- [ ] A. Use IAM policies
- [x] B. Use AWS KMS with automatic key rotation
- [ ] C. Use AWS Shield
- [ ] D. Use AWS Organizations

Q34. A company is running a web application on Amazon EC2 instances that needs to upload files to an Amazon S3 bucket. The security team requires that no long-term AWS credentials be stored on the instances. Which solution provides secure access while following AWS best practices?
- [ ] A. Create an IAM user with S3 permissions and store the access keys in a configuration file on the EC2 instance.
- [x] B. Create an IAM role with the required S3 permissions and attach it to the EC2 instance.
- [ ] C. Store AWS access keys in AWS Systems Manager Parameter Store and retrieve them at runtime.
- [ ] D. Create an S3 bucket policy that allows public write access from the EC2 instance's public IP address.

Q35. A company deploys an Application Load Balancer across two public subnets in different Availability Zones. The load balancer distributes traffic to EC2 instances running in private subnets. What is the PRIMARY advantage of this architecture?
- [ ] A. It reduces the cost of running EC2 instances by eliminating the need for Auto Scaling.
- [x] B. It ensures high availability and fault tolerance by distributing traffic across multiple Availability Zones.
- [ ] C. It allows EC2 instances in private subnets to have direct internet access.
- [ ] D. It removes the need to configure security groups for the EC2 instances.

Q36. A company wants to create an isolated network in AWS that behaves like its own private data center. Which AWS service should be used?
- [ ] A. Amazon Route 53
- [x] B. Amazon VPC
- [ ] C. Amazon CloudFront
- [ ] D. Amazon S3

Q37. A company deploys an Application Load Balancer across two public subnets in different Availability Zones and routes traffic to web servers in private subnets. What is the main benefit of this design?
- [ ] A. It eliminates the need for Security Groups
- [ ] B. It provides direct internet access to private instances
- [x] C. It improves availability and distributes traffic across targets
- [ ] D. It replaces Route 53 completely

Q38. You have set up consolidated billing for several AWS accounts. One of the accounts has purchased a number of reserved instances for 3 years. Which of the following is true regarding this scenario?
- [ ] A. The Reserved Instance discounts can only be shared with the master account
- [x] B. All accounts can receive the hourly cost benefit of the Reserved Instances
- [ ] C. The purchased instances will have better performance than On-demand instances
- [ ] D. There are no cost benefits from using consolidated billing; it is for informational purposes only

Q39. A customer is using multiple AWS accounts with separate billing. How can the customer take advantage of volume discounts with minimal impact to the AWS resources?
- [ ] A. Create one global AWS account and move all AWS resources to that account
- [ ] B. Sign up for three years of Reserved Instance pricing up front
- [x] C. Use the consolidated billing feature from AWS Organizations
- [ ] D. Sign up for the AWS Enterprise support plan to get volume discounts

Q40. Which of the following is an advantage of AWS consolidated billing?
- [x] A. The ability to receive one bill for multiple accounts
- [ ] B. Service limits increasing by default in all accounts
- [ ] C. A fixed discount on the monthly bill
- [ ] D. The automatic extension of the master account's AWS support plan to all accounts

Q41. Which of the following security measures protect access to an AWS account?
- [x] A. Activate multi-factor authentication (MFA) for privileged users
- [ ] B. Enable AWS CloudTrail
- [ ] C. Create one IAM user and share with many developers and users
- [ ] D. Enable Amazon CloudFront

Q42. How can a customer increase security to AWS account logons?
- [ ] A. Configure AWS Certificate Manager
- [x] B. Enable Multi-Factor Authentication (MFA)
- [ ] C. Use Amazon Cognito to manage access
- [ ] D. Enable AWS Organizations

Q43. Which statement is not true about Server-side Encryption at Rest?
- [ ] A. Data is encrypted after being received by the server
- [x] B. Data is decrypted after being sent
- [ ] C. It is stored in an encrypted form thanks to a key (usually a data key)
- [ ] D. The encryption / decryption keys must be managed somewhere, and the server must have access to it

Q44. A developer wants to store credentials securely and rotate them automatically. Which service should be used for this, as opposed to encrypting large volumes of data?
- [ ] A. AWS KMS
- [ ] B. AWS IAM
- [ ] C. AWS Artifact
- [x] D. AWS Secrets Manager

Q45. What is the primary purpose of AWS KMS in the context of security?
- [ ] A. Managing network security groups
- [ ] B. Storing user passwords for IAM users
- [x] C. Creating and managing encryption keys
- [ ] D. Auditing infrastructure spend

Q46. Which is not a type of KMS Key?
- [x] A. Middle-man Managed Keys
- [ ] B. AWS Managed Keys
- [ ] C. AWS Owned Keys
- [ ] D. Customer Managed Keys

Q47. Which AWS service enables you to quickly purchase and deploy SSL/TLS certificates?
- [ ] A. Amazon GuardDuty
- [ ] B. Amazon Detective
- [ ] C. AWS WAF
- [x] D. AWS ACM

Q48. Which AWS tool is used to estimate the cost of using a specific set of AWS services before any resources are actually provisioned?
- [x] A. AWS Pricing Calculator
- [ ] B. AWS Trusted Advisor
- [ ] C. AWS Cost Explorer
- [ ] D. AWS Budgets

Q49. Under the AWS Shared Responsibility Model, which of the following is a responsibility of the customer regarding billing?
- [ ] A. Determining the base price for EC2 instances
- [ ] B. Calculating the tax rates for all global regions
- [x] C. Configuring AWS Budgets and alerts
- [ ] D. Maintaining the billing infrastructure hardware

Q50. Which feature of AWS Organizations allows a company to receive a single bill for all of its AWS accounts?
- [ ] A. Unified Cost management
- [ ] B. Resource Groups
- [x] C. Consolidated Billing
- [ ] D. Control Tower

Q51. Which of the following determines the cost of using Amazon S3 storage?
- [ ] A. Which of the following determines the cost of using Amazon S3 storage?
- [x] B. Storage class used and the total amount of data stored
- [ ] C. The type of data (e.g. images, text...) being stored
- [ ] D. The operating system used to upload the files

Q52. Which AWS billing tool provides a visual representation of your cost and usage trends over time and allows you to forecast future costs?
- [ ] A. AWS Marketplace
- [ ] B. AWS Purchase Order Management
- [x] C. AWS Cost Explorer
- [ ] D. AWS License Manager

Q53. A user wants to save money on their compute costs and is willing to commit to a consistent amount of usage (measured in $/hour) for a 1-year term. Which option should they choose?
- [ ] A. Pay-as-you-go pricing
- [ ] B. Volume Discounts
- [ ] C. On-demand Capacity Reservations
- [x] D. Savings plans

Q54. Which AWS service is used to manage user identities and their access levels to AWS resources and services?
- [ ] A. AWS Secrets Manager
- [ ] B. AWS Directory Service
- [x] C. AWS Identity and Access Management (IAM)
- [ ] D. AWS Resource Access Manager (RAM)

Q55. A company needs to manage encryption keys and control their use across a wide range of AWS services. Which service should they use?
- [ ] A. AWS Cloud HSM
- [ ] B. AWS Systems Manager (SSM)
- [x] C. AWS Key Management Service (KMS)
- [ ] D. AWS Certificate Manager (ACM)

Q56. Which AWS service helps protect web applications from common web exploits like SQL injection or cross-site scripting (XSS)?
- [ ] A. AWS Shield
- [ ] B. Amazon GuardDuty
- [x] C. AWS WAF (Web Application Firewall)
- [ ] D. AWS Network Firewall

Q57. A user needs to provision, manage, and deploy public and private SSL/TLS certificates for use with AWS services. Which service should they use?
- [x] A. AWS Certificate Manager (ACM)
- [ ] B. AWS IAM
- [ ] C. AWS Artifact
- [ ] D. AWS Secrets Manager

Q58. What is the core difference between IAM Roles and IAM Users in Identity and Access Management services?
- [ ] A. IAM Users can contain multiple IAM Groups, but IAM Roles cannot.
- [ ] B. IAM Roles are region-bound resources, while IAM Users are global resources.
- [x] C. IAM Users have long-term login credentials, while IAM Roles use temporary security credentials.
- [ ] D. IAM Users are for humans only, while IAM Roles are for AWS services only.

Q59. Why are Managed Services (like Amazon S3 or DynamoDB) considered to have "Less Customer Responsibility" compared to Infrastructure Services (like Amazon EC2)?
- [ ] A. The customer does not need to use IAM for managed services
- [ ] B. Customers are not responsible for client-side encryption in managed services
- [x] C. AWS handles the management of the underlying OS, network configuration, and platform software for managed services
- [ ] D. Managed services do not require any configuration from the customer

Q60. Under the shared responsibility model, which of the following is a customer responsibility for Amazon EC2?
- [ ] A. Physical data centers
- [ ] B. Global infrastructure such as Regions and Availability Zones
- [x] C. The operating system and applications running on the instance
- [ ] D. The virtualization layer (hypervisor)

Q61. A company has three problems at the same time: (1) It wants to find PII inside S3 buckets. (2) It wants to detect CVEs and package vulnerabilities in ECR images. (3) It wants alerts for suspicious API activity and possible DNS-based exfiltration. Which mapping is the most correct?
- [x] A. Macie / Inspector / GuardDuty
- [ ] B. GuardDuty / Macie / Inspector
- [ ] C. Inspector / GuardDuty / Macie
- [ ] D. Macie / GuardDuty / Inspector

Q62. An organization needs to automatically scan millions of files in Amazon S3 buckets to detect sensitive information such as credit card numbers and personal identifiers (PIIs). Which of the following services performs this task best?
- [x] A. Amazon Macie
- [ ] B. AWS Inspector
- [ ] C. Amazon Security Tasks
- [ ] D. AWS WAF

Q63. Which list correctly shows the main components in the AWS cost breakdown?
- [x] A. Compute, Managed Services, Storage, Network Traffic & Data Transfer, Misc
- [ ] B. Compute, IAM, DNS, Storage, Support
- [ ] C. EC2, Lambda, S3, VPC, CloudTrail
- [ ] D. CPU, RAM, Disk, API, Backup

Q64. According to the slide, which formula is used to calculate compute cost?
- [x] A. Compute Cost = Runtime × Bandwidth × Users
- [ ] B. Compute Cost = Storage × Requests × Region
- [ ] C. Compute Cost = Instance Type × Instance Amount × Runtime
- [ ] D. Compute Cost = Instance Type × Availability Zone × Storage

Q65. Which of the following is NOT one of the four storage cost drivers shown in the slide?
- [ ] A. Storage class tiers
- [ ] B. PUT/GET request volume
- [ ] C. Lifecycle transitions
- [x] D. CPU clock speed

Q66. Which of the following is listed as an advantage of the Pay-as-you-go model?
- [ ] A. Revenue is unpredictable and volatile
- [ ] B. Pricing is always simple
- [x] C. Lower upfront costs attract users
- [ ] D. It is difficult to retain customers

Q67. Which option correctly lists the four AWS pricing models shown in the document?
- [x] A. On-Demand, Spot Instances, Reserved Instances, Savings Plans
- [ ] B. Free Tier, Premium Tier, Enterprise Tier, Custom Tier
- [ ] C. Compute Plan, Storage Plan, Network Plan, Security Plan
- [ ] D. Basic, Standard, Advanced, Professional

Q68. Which task falls under the customer's responsibility when utilizing managed services like Amazon S3 or Amazon DynamoDB?
- [ ] A. Maintaining the physical hardware and data centers
- [ ] B. Managing the host operating system and hypervisor
- [x] C. Configuring client-side data encryption
- [ ] D. Securing the global infrastructure and edge locations

Q69. How does AWS handle key rotation for Customer Managed Keys (CMKs) where the key material was manually imported by the user?
- [ ] A. Keys are rotated automatically every 365 days
- [ ] B. Keys are rotated automatically every 90 days
- [ ] C. AWS Support must rotate the key upon receiving a support ticket
- [x] D. There is no automatic rotation; it must be done manually

Q70. A development team wants to store database credentials securely and needs a service that natively supports automatic rotation of these secrets. Which AWS service is best suited for this requirement?
- [ ] A. AWS Systems Manager Parameter Store
- [x] B. AWS Secrets Manager
- [ ] C. AWS Key Management Service (AWS KMS)
- [ ] D. AWS Certificate Manager (ACM)

Q71. A system administrator has provisioned a public TLS certificate via AWS Certificate Manager (ACM). Which of the following resources can this certificate be directly deployed on to provide in-flight encryption?
- [ ] A. Amazon EC2 instances
- [x] B. Application Load Balancers (ALB)
- [ ] C. Amazon S3 buckets
- [ ] D. Amazon RDS instances

Q72. An architecture requires AWS WAF for Layer 7 protection and a fixed, static IP address for external whitelisting. Since an Application Load Balancer (ALB) does not offer a static IP by default, what is the recommended architecture?
- [ ] A. Apply AWS WAF directly to a Network Load Balancer (NLB)
- [ ] B. Attach an Elastic IP directly to the AWS WAF Web ACL
- [x] C. Place AWS Global Accelerator in front of the ALB
- [ ] D. Use Amazon Route 53 to generate a static IP for WAF

Q73. A startup is running a machine learning training job that can be interrupted and resumed later without affecting the final model. The team needs to minimize compute costs as much as possible. Which pricing model should they choose?
- [ ] A. On-Demand Instances
- [ ] B. Reserved Instances
- [x] C. Spot Instances
- [ ] D. Savings Plans

Q74. A company has deployed two Amazon EC2 instances within an Amazon Virtual Private Cloud (VPC). To ensure no data transfer charges occur when these instances communicate with each other, how must the instances be deployed?
- [ ] A. In different AWS Regions using VPC Peering.
- [x] B. In the same Availability Zone.
- [ ] C. In different Availability Zones within the same AWS Region.
- [ ] D. Behind an AWS Transit Gateway in the same AWS Region.

Q75. Which of the following is NOT one of the primary cost drivers for Amazon S3 storage?
- [ ] A. Storage Class Tiers
- [ ] B. PUT/GET Request Volume
- [x] C. Number of IAM Users accessing the bucket
- [ ] D. Lifecycle Transitions

Q76. An enterprise is deploying an AI document processing tool that analyzes historical financial records overnight. There is no requirement for instant results. Which approach will be the most cost-effective for running this compute workload?
- [ ] A. Deploying a real-time Amazon SageMaker endpoint.
- [ ] B. Using Amazon EC2 On-Demand instances to run real-time inference 24/7.
- [x] C. Utilizing batch inference jobs.
- [ ] D. Provisioning Amazon DynamoDB with maximum read capacity.

Q77. A company wants to track and organize its AWS costs by individual departments, such as "Marketing" and "Development". What is the most effective way to achieve this?
- [ ] A. Create separate AWS Regions for each department.
- [x] B. Apply User-Defined Cost Allocation Tags to resources.
- [ ] C. Use AWS Cost Anomaly Detection to filter traffic.
- [ ] D. Enable Amazon CloudWatch Metrics Dashboard.

Q78. Which AWS service or feature provides an additional layer of security by requiring a user to provide a unique code from a device in addition to their password?
- [ ] A. AWS Shield
- [x] B. Multi-Factor Authentication (MFA)
- [ ] C. AWS Artifact
- [ ] D. AWS Key Management Service (AWS KMS)

Q79. A company stores sensitive customer data including credit card numbers and personal information in Amazon S3 buckets. The security team wants to automatically identify and classify this sensitive data. Which AWS service should they use?
- [x] A. Amazon Macie
- [ ] B. AWS Security Hub
- [ ] C. Amazon Inspector
- [ ] D. Amazon GuardDuty

Q80. A company uses AWS Organizations. They want to prevent all accounts in a specific department from launching EC2 instances. Which feature should they use?
- [ ] A. IAM Permission Boundary
- [ ] B. AWS Config Rules
- [x] C. Service Control Policies (SCP)
- [ ] D. AWS Security Hub

Q81. Which IAM component is used to grant temporary security credentials to AWS services like EC2 or Lambda?
- [ ] A. IAM User
- [ ] B. IAM Group
- [x] C. IAM Role
- [ ] D. IAM Policy

Q82. Which AWS service is used to easily provision, manage, and deploy SSL/TLS certificates for encryption in transit?
- [ ] A. AWS KMS
- [ ] B. AWS Secrets Manager
- [x] C. AWS Certificate Manager (ACM)
- [ ] D. SSM Parameter Store

Q83. Which type of KMS Key allows you to download and share the Public Key with others?
- [ ] A. Symmetric KMS Keys
- [ ] B. AWS Owned Keys
- [x] C. Asymmetric KMS Keys
- [ ] D. AWS Managed Keys

Q84. Which AWS Cloud service can send alerts to customers if custom spending thresholds are exceeded?
- [ ] A. AWS Cost Explorer
- [ ] B. AWS Cost Allocation Tags
- [ ] C. AWS Organizations
- [x] D. AWS Budgets

Q85. A company is planning to migrate its on-premises workloads to AWS. They want to estimate their potential monthly costs for a specific set of services (such as Amazon EC2, Amazon RDS, and Amazon S3) based on their expected usage before actually launching any resources. Which AWS tool should they use?
- [ ] A. AWS Cost Explorer
- [x] B. AWS Pricing Calculator
- [ ] C. AWS Budgets
- [ ] D. AWS Trusted Advisor

Q86. Under the AWS Shared Responsibility Model, which of the following is a responsibility of the customer regarding billing and cost management?
- [ ] A. Maintaining the physical billing infrastructure.
- [x] B. Managing cost allocation tags to track expenses by department.
- [ ] C. Ensuring the global availability of the AWS Billing console
- [ ] D. Determining the underlying hardware costs for EC2 instances.

Q87. A large enterprise has multiple AWS accounts for different business units. The finance department wants to receive a single, combined invoice for all accounts to simplify the payment process and benefit from volume-based discounts. Which feature of AWS Organizations should they implement?
- [ ] A. Service Control Policies (SCPs)
- [ ] B. Resource Groups
- [ ] C. AWS Cost and Usage Report
- [x] D. Consolidated Billing

Q88. Which security service uses Machine Learning to automatically discover and protect sensitive data (such as PII) stored in Amazon S3?
- [ ] A. Amazon GuardDuty
- [ ] B. Amazon Inspector
- [x] C. Amazon Macie
- [ ] D. AWS WAF

Q89. Which commitment-based pricing model provides the highest level of flexibility by covering compute usage across EC2, AWS Lambda, and AWS Fargate regardless of instance family or region?
- [ ] A. Standard Reserved Instances
- [ ] B. EC2 Instance Savings Plans
- [x] C. Compute Savings Plans
- [ ] D. Convertible Reserved Instances

Q90. According to AWS AI case studies, what is typically the primary cause for the observed average monthly budget gap of $3,400 - $13,800?
- [ ] A. Rapid scaling of On-Demand instance counts
- [x] B. Invisible costs like uncleaned storage and unmodeled data transfer
- [ ] C. High premium charges for Enterprise Support plans
- [ ] D. Inaccurate pricing forecasts from AWS Cost Explorer

Q91. For non-customer-facing AI workloads like historical fraud scoring, which strategy is recommended to reduce compute costs by 60-70%?
- [ ] A. Utilizing Spot Instances for all inference tasks
- [ ] B. Enabling HNSW-PQ compression for vector storage
- [x] C. Using Batch Transform jobs instead of real-time endpoints
- [ ] D. Implementing automated instance scheduling for off-hours

Q92. In a production RAG deployment, which specific technique can reduce annual vector storage costs from $75,000 down to approximately $10,000?
- [ ] A. HNSW-FP16 compression
- [x] B. HNSW-PQ compression
- [ ] C. Implementing lifecycle transitions to S3 Glacier
- [ ] D. Consolidating multiple OpenSearch clusters

Q93. When accessing AWS services like S3 or DynamoDB within the same region, which architectural pattern incurs both a per-hour service charge and a per-GB data processing charge?
- [ ] A. Pattern 1: Internet Gateway
- [x] B. Pattern 2: NAT Gateway
- [ ] C. Pattern 3: VPC Peering
- [ ] D. Pattern 4: Gateway Load Balancer

Q94. A security team wants to audit which IAM users in the account have not used their access keys in the past 90 days. Which IAM tool should they use?
- [ ] A. IAM Access Advisor
- [ ] B. AWS CloudTrail
- [x] C. IAM Credentials Report
- [ ] D. AWS Config

Q95. A company stores sensitive documents in Amazon S3 and needs to encrypt them using keys that they can fully control, rotate manually, and audit via IAM policies. Which AWS KMS key type should they use?
- [ ] A. AWS Owned Keys
- [ ] B. AWS Managed Keys
- [ ] C. Symmetric Imported Keys
- [x] D. Customer Managed Keys (CMK)

Q96. A company's web application hosted behind an Application Load Balancer is experiencing a large-scale SQL injection attack. Which AWS service should be deployed to block these malicious HTTP requests?
- [ ] A. AWS Shield Standard
- [ ] B. AWS Network Firewall
- [x] C. AWS WAF with a Web ACL attached to the ALB
- [ ] D. Amazon GuardDuty

Q97. A security engineer needs to automatically discover and report any Personally Identifiable Information (PII) that has been accidentally uploaded to the company's Amazon S3 buckets. Which AWS service is purpose-built for this task?
- [ ] A. Amazon GuardDuty
- [ ] B. AWS Trusted Advisor
- [ ] C. Amazon Inspector
- [x] D. Amazon Macie

Q98. Which of the following can the AWS Pricing Calculator do?
- [ ] A. Provide users with access to their monthly bills.
- [x] B. Project monthly AWS costs.
- [ ] C. Provide in-depth information about AWS pricing strategies.
- [ ] D. Calculate historical AWS costs

Q99. A company wants to implement detailed tracking of its cloud costs by department and project. Which AWS feature or service should the company use?
- [ ] A. AWS Marketplace
- [ ] B. AWS Budgets
- [x] C. Cost allocation tags
- [ ] D. Consolidated billing

Q100. Both AWS Secrets Manager and AWS Systems Manager (SSM) Parameter Store can be used to securely store database credentials. What is a key capability unique to AWS Secrets Manager that justifies its higher cost?
- [ ] A. It uses a hierarchical path structure to organize configuration data.
- [x] B. It natively supports automatic rotation of secrets on a schedule using a Lambda function.
- [ ] C. It provides free public TLS/SSL certificates for your applications.
- [ ] D. It is the only service that integrates with AWS KMS for encryption at rest.

Q101. Under the AWS Shared Responsibility Model, which of the following is a responsibility specifically managed by the CUSTOMER when running an application on Amazon EC2 ?
- [ ] A. Disposal of decommissioned hard drives.
- [x] B. Patching the guest operating system and the application software.
- [ ] C. Maintenance of the underlying virtualization software (Hypervisor).
- [ ] D. Physical security of the data centers.

Q102. To satisfy a regulatory audit, a company needs to provide a history of all API calls made within their AWS account, including who made the call and from which IP address. Which service provides this record?
- [ ] A. Amazon CloudWatch Logs.
- [ ] B. AWS Config.
- [x] C. AWS CloudTrail.
- [ ] D. Amazon Inspector.

Q103. Your application needs to securely store a third-party API key that rarely changes. You want the most cost-effective solution that supports encryption at rest via KMS and allows hierarchical organization of the configuration data. Which service should you choose ?
- [x] A. AWS Systems Manager (SSM) Parameter Store
- [ ] B. AWS Certificate Manager (ACM)
- [ ] C. AWS Key Management Service (KMS)
- [ ] D. AWS Secrets Manager

Q104. A data analytics team is running a batch processing job that can be interrupted and resumed at any time. Which EC2 instance type offers the deepest discount (up to 90%) for this workload?
- [ ] A. Convertible Reserved Instances.
- [ ] B. On-Demand Instances.
- [ ] C. Standard Reserved Instances.
- [x] D. Spot Instances.

Q105. According to the AWS Compute Cost calculation formula, which three variables determine the total cost?
- [ ] A. On-demand Rate, Reserved Capacity, and Throughput
- [ ] B. Storage Tier, Data Transfer, and Region
- [ ] C. vCPU Count, Memory Size, and API Requests
- [x] D. Instance Type, Instance Amount, and Runtime

Q106. What is identified as a primary drawback for a provider using the 'Pay-as-you-go' pricing model?
- [ ] A. It is too simple for customers to understand
- [ ] B. Customers are locked into long-term contracts
- [ ] C. It attracts fewer users due to high entry costs
- [x] D. Revenue is unpredictable and volatile

Q107. For an unpredictable workload where you do not know how long the system will run, which pricing model is most appropriate?
- [ ] A. Compute Savings Plans
- [x] B. On-demand Pricing
- [ ] C. Convertible Reserved Instances
- [ ] D. Standard Reserved Instances

Q108. When accessing AWS services within the same Region, what is the cost impact of using a NAT Gateway compared to an Internet Gateway?
- [ ] A. NAT Gateway has no data transfer charge, while Internet Gateway charges per GB.
- [ ] B. Both have a flat monthly fee regardless of usage.
- [x] C. NAT Gateway incurs both a per-hour service charge and a per-GB data processing charge.
- [ ] D. Internet Gateway incurs a per-hour service charge.

Q109. For advanced FinOps in AI deployments, why is it highly recommended to use Batch Inference instead of Real-Time Endpoints whenever latency allows?
- [ ] A. Batch Inference runs 24/7 to ensure zero latency.
- [x] B. Real-Time SageMaker endpoints run 24/7 whether they serve requests or not, leading to idle waste.
- [ ] C. Batch Inference utilizes more expensive GPU types.
- [ ] D. Real-Time Endpoints do not support modern AI models.

Q110. What do you gain from setting up consolidated billing for five different AWS accounts under another master account?
- [ ] A. AWS services' costs will be reduced to half the original price.
- [ ] B. The consolidated billing feature is just for organizational purpose.
- [x] C. Each AWS account gets volume discounts.
- [ ] D. Each AWS account gets five times the free-tier services capacity.

Q111. What are the two main types of KMS keys, and how do they differ in usage?
- [ ] A. Symmetric keys use one key for encryption only, while asymmetric keys use one key for decryption only.
- [x] B. Symmetric keys use a single key for encryption and decryption, while asymmetric keys use a public/private key pair.
- [ ] C. Symmetric keys use public/private pairs, while asymmetric keys use a single shared key.
- [ ] D. Both symmetric and asymmetric keys require two keys for encryption and decryption.

Q112. Which services does Amazon Inspector integrate with to send findings?
- [ ] A. Amazon S3 & Amazon DynamoDB
- [x] B. AWS Security Hub & Amazon EventBridge
- [ ] C. Amazon RDS & AWS Lambda
- [ ] D. Amazon CloudFront & AWS Shield

Q113. Which is the correct workflow for identifying sensitive data using Amazon Macie?
- [x] A. Amazon S3 -> Amazon Macie (analyze sensitive data) -> Amazon EventBridge (notify & integrate)
- [ ] B. Amazon EC2 -> AWS Shield -> Amazon SNS
- [ ] C. Amazon RDS -> AWS WAF -> Amazon CloudWatch
- [ ] D. AWS Lambda -> Amazon GuardDuty -> AWS Security Hub

Q114. You need to encrypt application data at rest in Amazon S3 using AWS Key Management Service (KMS) with fine-grained control over who can use the key. Which key type is the best fit?
- [x] A. Customer managed KMS key that you create and control
- [ ] B. Default S3 server-side encryption with S3-managed keys (SSE-S3)
- [ ] C. KMS key for AWS CloudHSM only, with no IAM policies
- [ ] D. AWS managed key aws/s3 used transparently by S3

Q115. An organization with many AWS accounts wants to centrally define and enforce AWS WAF rules and Shield Advanced protections across all accounts in the organization. Which service is designed to simplify this centralized management?
- [ ] A. Amazon Macie
- [ ] B. AWS Config
- [ ] C. Amazon GuardDuty
- [x] D. AWS Firewall Manager

Q116. Which statement best describes the main difference between AWS Certificate Manager (ACM) and AWS Key Management Service (KMS)?
- [x] A. ACM manages SSL/TLS certificates for securing network connections, while KMS manages encryption keys for protecting data at rest and in transit
- [ ] B. ACM is used only for database encryption, while KMS is used solely for logging and monitoring
- [ ] C. KMS automatically deploys SSL/TLS certificates to Elastic Load Balancers, while ACM only stores private keys in hardware modules
- [ ] D. Both ACM and KMS are used only for generating client-side encryption keys that never leave the customer's environment

Q117. In the Shared Responsibility Model of Amazon Web Services, which of the following responsibilities belongs to AWS?
- [ ] A. Configuring firewall rules for EC2 instances
- [ ] B. Encrypting data at the application level
- [x] C. Maintaining the physical hardware in data centers
- [ ] D. Managing IAM users and permissions

Q118. You want to enhance security for the root account and IAM users in AWS. Which of the following is a best practice?
- [ ] A. Use strong passwords only, without additional factors
- [ ] B. Use AWS Identity and Access Management roles instead of users for all access
- [x] C. Enable Multi-Factor Authentication for the root account and critical IAM users
- [ ] D. Share access keys among developers for easier management

Q119. You want to track AWS costs per project and receive alerts when budgets are exceeded. Which combination of services should you use?
- [ ] A. Amazon CloudWatch + Trusted Advisor
- [x] B. AWS Cost Explorer + AWS Budgets
- [ ] C. AWS Shield + AWS WAF
- [ ] D. AWS Organizations + IAM

Q120. Which AWS service is used to temporarily provide federated security credentials to access AWS resources?
- [ ] A. AWS Certificate Manager
- [ ] B. AWS Secrets Manager
- [x] C. AWS Simple Token Service (AWS STS)
- [ ] D. Amazon GuardDuty

Q121. A company has an AWS Business Support plan. The company needs to gain access to the AWS DDoS Response Team (DRT) to help mitigate DDoS events. Which AWS service or resource must the company use to meet these requirements?
- [ ] A. AWS Shield Standard
- [ ] B. AWS Enterprise Support
- [ ] C. AWS WAF
- [x] D. AWS Shield Advanced

Q122. An AWS user wants to proactively detect when an instance or account might be compromised or if there are threats from attacks. Which AWS service should the user choose?
- [ ] A. Amazon Inspector
- [ ] B. AWS WAF
- [x] C. Amazon GuardDuty
- [ ] D. AWS Shield

Q123. A company plans to launch an ecommerce website that contains many images for a product catalog. The company wants to keep the cost of running the website within a specific budget. Which AWS service or tool should the company use to monitor the ongoing costs of the website?
- [ ] A. AWS CloudFormation
- [x] B. AWS Cost Explorer
- [ ] C. AWS SDKs
- [ ] D. EC2 Image Builder

Q124. A company wants to visualize and manage AWS Cloud costs and usage for a specific period of time. Which AWS service or feature will meet these requirements?
- [x] A. Cost Explorer
- [ ] B. AWS Budgets
- [ ] C. Consolidated billing
- [ ] D. AWS Organizations

Q125. A company has multiple AWS accounts. The company needs to receive a consolidated bill from AWS and must centrally manage security and compliance. Which AWS service or feature should the company use to meet these requirements?
- [ ] A. AWS Security Hub
- [ ] B. AWS Config
- [x] C. AWS Organizations
- [ ] D. AWS Cost and Usage Report

Q126. A company has moved all its infrastructure to the AWS Cloud. To plan ahead for each quarter, the finance team wants to track the cost and usage data of all resources from previous months. The finance team wants to automatically generate reports that contains the data. Which AWS service or feature should the finance team use to meet these requirements?
- [ ] A. Amazon Detective
- [ ] B. AWS Pricing Calculator
- [x] C. AWS Budgets
- [ ] D. AWS Savings Plans

Q127. Which AWS service or tool provides a visualization of historical AWS spending patterns and projections of future AWS costs?
- [ ] A. Amazon Cloud Watch
- [ ] B. AWS Budgets
- [ ] C. AWS Cost and Usage Report
- [x] D. Cost Explorer

Q128. A company wants to track the monthly cost and usage of all Amazon EC2 instances in a specific AWS environment. Which AWS service or tool will meet these requirements?
- [ ] A. AWS Trusted Advisor
- [ ] B. AWS Compute Optimizer
- [ ] C. AWS Cost Anomaly Detection
- [x] D. AWS Budgets

Q129. A company is using multiple AWS accounts for different business teams. The finance team wants to receive one bill for all of the company's accounts. Which AWS service or tool should the finance team use to meet this requirement?
- [ ] A. AWS Budgets
- [ ] B. Cost Explorer
- [ ] C. AWS Trusted Advisor
- [x] D. AWS Organizations
