AWS resource for verify information
e.g. Which AWS resource is a searchable database of troubleshooting articles and answers to frequently asked technical questions? re:Post, Prescriptive Guidance, Blog or Knowledge Center. 

which AWS service can be used to *reservation utilization budget (tạo ngân sách sử dụng)* and *coverage budget for both RÍ and Saving Plan (phạm vi đặt chỗ cho RI và SP).* 

**Saving Plan** offer Significant Discounts -> in exchange for a commitment to a consistent amount of compute usage, measured in $/hour, for a 1- or 3-year term 
+ $ Discount automate apply to Amazon EC2, AWS Fargate, and AWS Lambda, and can be flexible across instance families, sizes, and even AWS Regions.
	*Discount NOT applied  for S3*, because S3 have Tiering List and Life Cycle which Data Storage Tier based on data Access Frequency to SAVE COST.

*Compare Saving Plan to Convertible Reserved Instances (RIs)*
	Convertible Reserved Instances (RIs) offer a discount for a term commitment and *allow you to change instance attributes like family, size, or OS*
	while Saving Plan apply for A LOT MORE like Amazon EC2, AWS Fargate, and AWS Lambda, and can be flexible across instance families, sizes, and even AWS Regions.
+ @ To conclude, **SAVING PLAN > Convertible RIs**. SAVING PLAN apply to most of AWS compute service  while *Convertible RIs only apply to EC2.* 


*CloudWatch Dashboard vs AWS Billing & Cost Management Dashboard* note
	Cost Management Db is for billing monitoring central ![[Pasted image 20260513193030.png]]
	CloudWatch Dashboard is for monitor AWS infrastructure (resource and application) it collects and tracks metrics, logs and events but not billing or cost management. ![[Pasted image 20260513193225.png]]

**AWS Docs for Verify and Research**
+ **re:Post** -> community-driven question-and-answer (Q&A) service -> could have valuable resource for troubleshooting but not official articles from AWS. 
+ AWS **Prescriptive Guidance** -> provides proven *strategies, architectural patterns, and best practices* for designing and deploying solutions on AWS. 
	**focus on build applications correctly** rather than troubleshooting existing problems.
+ AWS **Blog** - blog but not structured as a searchable database for resolving common technical issues. 
+ AWS **Knowledge Center** - *specifically designed as a searchable repository of official articles and videos created by AWS support engineers*. It provides answers to frequently asked questions and step-by-step guidance for troubleshooting common technical issues.

AWS Pricing Model for data transfer IN and OUT of region.
![[Pasted image 20260513193920.png]]


## FULL Test 1 
![[Pasted image 20260513204331.png]]

Different between Migration Hub vs Catalog

Which of the following is a security capability that AWS provides to all customers at no additional cost?
A) AWS Shield Standard
B) Amazon GuardDuty (30-day free trial excluded)
C) AWS Shield Advanced
D) AWS Firewall Manager

#### Domain 1: Cloud Concepts
A development team uses a script that automatically shuts down non-production Amazon EC2 instances outside of business hours. This is an example of cost savings through:
A) Rightsizing ???? -> process of *matching instance types* and sizes to your Workload (e.g. *large instance to medium one) not STOPPING them.* 
	Incorrect. Rightsizing is the process of matching instance types and sizes to your workload performance and capacity requirements at the lowest possible cost. It involves modifying the compute resources (e.g., changing from a large instance to a medium one), not stopping them.
B) *Automation* - okay Logic, *resize also require Automation so THAT WHY Automatic is the Correct Answer.* 
	Correct. Automation involves using scripts, tools, or services to perform tasks automatically without human intervention. In this scenario, a script is used to shut down EC2 instances, which is a classic example of automating a cost-optimization practice to avoid paying for idle resources.
C) Economies of scale
	Incorrect. Economies of scale is a benefit that cloud providers like AWS achieve by operating at a massive scale, which allows them to offer lower pay-as-you-go prices. While this is a core economic benefit of the cloud, it is not what is being demonstrated by the team's specific action of shutting down instances.
D) BYOL
	Incorrect. BYOL (Bring Your Own License) is a model that allows customers to use their existing software licenses on a cloud provider's infrastructure. This is a cost-saving strategy related to software licensing, not the operational management of compute instances.

A research institute needs to move an entire 100 PB data archive to the AWS Cloud. Which AWS service is designed for data transfers of this magnitude?
A) AWS Direct Connect
B) AWS Snowball
C) AWS DataSync
*D) AWS Snowmobile* (*has expired*) - but *if this option exist in the quiz for 100PB data, just choose it.*

Moving to the cloud helps companies stop spending money on running and maintaining data centers. What aspect of cloud economics does this describe?
A) Increasing speed and agility.
B) Benefiting from economies of scale.
*C) Trading capital expense for variable exr*
D) Going global in minutes.
*-> Benefiting from economies of scale vs "CAPEX vs variable expense or OpEx"* what the different ? 
+  economies of scale -> massive scale mean Lower cost for user. not related to runnig and maintain datacenter. 
+ trading CAPEX to OPEX -> bc the company is directly trading capital expense when using AWS. not just lower cost -> eliminates the costs associated with purchasing, running, and maintaining a physical data center.

#### Domain 2: Security and Compliance
A development team needs to ensure that both the data they store in an Amazon S3 bucket and the data sent from users to their Application Load Balancer are secure. Which TWO security mechanisms should they implement to meet these requirements? choose Two:
+ @ Implement **Encryption in Transit and at Rest** to the Data for maximum security. 
*A) Implement encryption in transit on the Application Load Balancer listener*
	Correct. Implementing *encryption in transit* on an *Application Load Balancer (ALB) listener protects data **as it travels from users over the internet to the load balancer.*** This is typically achieved by configuring an HTTPS listener with an SSL/TLS certificate, fulfilling the requirement to secure data in transit.
B) Use Amazon GuardDuty
	Incorrect. Amazon GuardDuty is an intelligent threat detection service that continuously monitors for malicious activity and unauthorized behavior. It **helps protect** AWS accounts and workloads *but does not directly encrypt data.*
C) Enable AWS CloudTrail data events
	Incorrect. *AWS CloudTrail* is a service for governance, compliance, and auditing. Enabling data events logs API activity for S3 objects, which is useful *for monitoring access but does not encrypt* the data itself, either at rest or in transit.
D) Attach a *security group to the S3 bucket*
	Incorrect. *Security groups act as a virtual firewall for resources like Amazon EC2 instances*, controlling inbound and outbound traffic. They **cannot be attached directly to Amazon S3 buckets**. Access to S3 is managed through IAM policies, bucket policies, and Access Control Lists (ACLs).
*E) Implement server-side encryption for the S3 bucket* -> *(meaning encyption at rest for an S3 bucket)* data is encrypted as it is written to disks in AWS data centers and decrypted when accessed, fulfilling the requirement to secure stored data.
+ $ **Encryption at Rest** mean encrypted **before it is written to the physical storage medium** (HDD or SSD) -> It ensures 100% that if someone steals the physical hard drive, or gains unauthorized access to the storage volume, they cannot read the files without the encryption keys
	How Server-Side Encryption at Rest Works
	1. **Data Transmission:** Data moves to the server over a secure channel (encrypted in transit).
	2. **Server Receives & Encrypts:** The *server receives the plain text, then immediately encrypts it* using managed keys *before writing it to the disk*.
	3. **"Resting":** The data sits on the SSD/HDD in a scrambled (ciphertext) format.
	4. **Decryption:** When an authorized user requests the data, the server decrypts it on the fly and sends it over a secure connection

A company wants to manage access for a large group of users by connecting their existing identity source, such as Okta or Azure AD, to AWS. Which AWS service is BEST suited for this purpose?
(Migrate Identification)
A) AWS Secrets Manager -> *only store, mange and rotate (change the Secreat password string and API key text* while its ARN, Metadata remain) Not Importing or Migrate Keys
	AWS Secrets Manager is a service designed to securely store, manage, and rotate secrets like database credentials and API keys. It does not handle user identity management or connect to external identity providers.
B) AWS config
	AWS Config is a service used for *assessing, auditing, and evaluating the configurations of AWS resources*. It helps with compliance and operational troubleshooting **but is not used for managing user access or identity federation.**
C) Amazon GuardDuty
	Amazon GuardDuty is an intelligent *threat detection service that continuously monitors AWS accounts* for malicious activity and unauthorized behavior. It is a security monitoring service, not an access management service.
*D) AWS IAM Identity Center*
	AWS IAM Identity Center (formerly known as AWS Single Sign-On) is the ideal service for this requirement. It centrally manages Single Sign-On (SSO) access to multiple AWS accounts and cloud applications. It is *specifically designed to connect with external identity providers (IdPs) like Okta and Azure AD, enabling users to log in with their existing corporate credentials.*

What does the security concept of 'encryption at rest' refer to?
A) Encrypting data as it moves across a network.
	Incorrect. This describes *'encryption in transit', which protects data as it travels across a network* (e.g., the internet). Encryption at rest applies to data that is not actively moving and is stored on a physical medium.
B) Hashing user passwords before they are stored -> Hasing is 1-way cryptographic while Encryption is 2-way process (encrypt/decrupt)
	Incorrect. While hashing passwords is a crucial security practice for protecting credentials, it is distinct from the general concept of encryption at rest. Hashing is a one-way cryptographic function, whereas encryption is a two-way process (encrypt/decrypt). Encryption at rest is a broader concept that applies to all types of stored data, not just passwords.
*C) Protecting data that is stored physically on a disk or storage media.*
	Correct. Encryption at rest is a security control that involves *encrypting data when it is stored or 'at rest' on physical storage media*, such as *hard drives, SSDs, or tapes.* This ensures that if the physical media is compromised, the data remains unreadable without the corresponding decryption keys. AWS services like S3 and EBS provide options for encryption at rest.
D) *Encrypting an API call* to an AWS service.
	Incorrect. Encrypting an API call to an AWS service *is a form of 'encryption in transit'.* This is typically handled by using secure protocols like HTTPS (which uses TLS/SSL) to protect the data while it travels from a client to the AWS service endpoint.


Which of the following are valid identity types in AWS IAM that can be assigned permissions ?
A) IAM Policies
	Incorrect. An IAM Policy is a JSON document that explicitly defines permissions. Policies are not identities themselves; they are attached to identities (like users, groups, and roles) to grant or deny access to AWS resources.
*B) IAM Users*
	Correct. An IAM User is a fundamental identity that represents a person or application interacting with AWS. A user has associated long-term credentials (like a password and access keys) and can be assigned permissions directly or by being a member of an IAM Group.
C) Amazon EC2 instances (EC2 is the Service/Compute Resource that RECEIVE/GRANTED permissions when Assigned/Attached with IAM Role, it the IAM Role that contain the permission)
*D) IAM Roles* (is an Identity acting as a Intermediate to Receive permission and Granted permission to other Identity if assigned to, like IAM user, an application or an AWS service)  -> provide temp credential, not long-term. 
E) IAM Groups - that direct persmission policies to the User within it. 
	Incorrect. An IAM Group is a valid **IAM Identity type** that can have permission policies assigned to it directly. It is used to simplify permission management for multiple users. Note that while it is an _Identity_, it is not a _Principal_ (it cannot log in, hold credentials, or make active API requests itself; the users inside it inherit its assigned rules).
+ ? Only entities that can **prove who they are** using AWS security credentials can be a principal (in Principle Identity). Valid principals include:
	An **IAM User** (logs in with password or access keys) [2]
	An **IAM Role** (assumes temporary STS tokens to act) [2]
	An **AWS Account** (the root user) [2]
	An **AWS Service** (like EC2 or Lambda acting on your behalf) [2]
	-> when AWS ask "Who is the Principal making this request ?" -> it always be IAM User or IAM Roles.
#### Domain 3: Cloud Technology and Services
An e-commerce platform wants to provide real-time, *individualized product recommendations to its users based on their browsing history*. Which AWS service specializes in creating recommendation engines?
A) Amazon Comprehend (use NLP to understand human language)
	Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to *find insights and relationships in unstructured text,* such as customer reviews or social media posts. It is not designed for creating product recommendation engines
B) Amazon Forecast (timeseries forsure)
	Incorrect. Amazon Forecast is a fully managed service that uses machine learning *for time-series forecasting*. It is used to predict future business outcomes like product demand or inventory needs, not for providing real-time, individualized user recommendations.
*C) Amazon Personalize* (Recommended Engine)
	Correct. Amazon Personalize is a fully managed machine learning service *specifically designed to build and deploy recommendation engines*. It enables developers to provide real-time, individualized recommendations and personalized user experiences for applications like e-commerce platforms.
D) Amazon Kendra (aws RAG)
	Incorrect. Amazon Kendra is an intelligent enterprise search service powered by machine learning. It *allows users to search for information across various internal data sources,* but it does not specialize in generating personalized user recommendations.


Which AWS service is used to launch fully managed, high-performance file systems like Lustre or Windows File Server in the cloud?
A) Amazon EBS
	Incorrect. Amazon EBS provides persistent block-level storage volumes for use with Amazon EC2 instances. It functions like a raw, unformatted hard drive and is not a fully managed file system service like Lustre or Windows File Server.
B) Amazon S3
	Incorrect. Amazon S3 is an object storage service, not a file system service. It is designed for storing and retrieving large amounts of data, but it does not provide the file system protocols and features of services like Lustre or Windows File Server.
*C) Amazon FSx* -> for Lustre and Window server. 
	Correct. Amazon FSx is a fully managed service designed to launch and run popular high-performance file systems. It offers specific services like Amazon FSx for Lustre and Amazon FSx for Windows File Server, directly addressing the requirements mentioned in the question.
D) Amazon *EFS* (*only for AWS*)
	Incorrect. Amazon EFS provides a scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. However, it does not specifically offer managed file systems based on Lustre or Windows File Server.
+ @ Insight: if I know about EFS and never heart that it support Lustre or Window Server then -> It MUST be FSx bc no way it will be EBS or S3.

An Amazon EBS volume can be attached to:
A) Any resource within a VPC.
	Incorrect. Amazon EBS volumes are block storage devices specifically designed to serve as virtual disks for Amazon EC2 instances. They cannot be attached to other types of AWS resources within a VPC, such as NAT Gateways, subnets, or security groups.
B) A single EC2 instance in the same Availability Zone.
	Correct. This describes the fundamental design of Amazon EBS. An EBS volume is created within a specific Availability Zone and can only be attached to a single EC2 instance that resides in that same Availability Zone. This co-location ensures the low-latency, high-performance connectivity required for block storage.
*C) Multiple EC2 instances in the same Availability Zone* (this is Correct bc AT THIS LEVEL, ppl only attach EBS to 1 EC2 although there a Multiple-Connect option)
	Incorrect. The standard and most common behavior for an Amazon EBS volume is to be attached to only one EC2 instance at a time. While a feature called EBS Multi-Attach exists for certain volume and instance types, the general rule, and what's expected for this exam level, is a one-to-one relationship.
D) Multiple EC2 instances in different Availability Zones.
	Incorrect. An Amazon EBS volume is specific to a single Availability Zone and cannot be attached to an EC2 instance in a different Availability Zone. Furthermore, a standard EBS volume can only be attached to a single instance at a time.


#### Domain 4: Billing, Pricing, and Support
A company is designing a new, highly available application on AWS. During the design phase, they would like to get architectural guidance from AWS at no extra cost. Who should they contact?
is AWS Sol Architect FREE ???
A) AWS Enterprise Support
	AWS Enterprise Support is the highest tier of paid support plans. While it includes access to experts for architectural guidance, it is a premium service and therefore does not meet the 'at no extra cost' requirement.
B) The AWS Trust and Safety team
	The AWS Trust and Safety team is responsible for handling security, abuse, compliance, and fraud issues on the AWS platform. They do not provide architectural guidance for application design.
**C) An AWS Solutions Architect** (Even if it Hard to Believe THIS IS **FREE**, but it the only Reasonable answer, bc who would chose a Trust and Safety Team sound like they work for Security and they does)
	This is the correct answer. AWS Solutions Architects are technical experts who provide architectural guidance and best practices to customers. *This service is often available at no direct cost as part of a customer's relationship with their AWS account team,* especially during the design and pre-sales phases.
D) AWS Professional Services
	AWS Professional Services is a paid consulting engagement where a global team of experts helps customers with specific outcomes. This is not a free service and is used for complex, paid projects rather than general architectural guidance.



A company has a predictable, steady-state workload running on a **fleet of c5.large EC2 instances**. They want to reduce costs and are willing to commit to a 3-year term. They have no plans to change the instance family. Which purchasing option would provide the highest discount?
A) Compute Savings Plans
	Incorrect. Compute Savings Plans offer significant discounts over On-Demand pricing and provide flexibility by applying discounts across different instance families, instance types, and regions. However, for a workload that is completely predictable and uses a specific instance family without change, Standard Reserved Instances typically offer a higher discount.
*B) Standard Reserved Instances*
	Correct. Standard Reserved Instances provide the highest discount for predictable, long-term workloads. By committing to a specific instance family (c5), instance size, and region for a 3-year term, the company can achieve the maximum possible savings for this steady-state use case.
C) Spot Instances
D) On-Demand Instances
-> because it **just Instance and steady for 3-years** so Standard Reserved Instances provide the most Discount. 


A company that builds commercial software wants to make its product available to **AWS customers (not public business customer)**, who can then deploy it directly from the AWS Management Console. Which AWS service should the company use ?
A) AWS Partner Network
	program provides technology and consulting businesses
B) AWS CodeCommit
	Incorrect. AWS CodeCommit is a fully-managed source control service that hosts secure Git-based repositories. It is used for code storage and version control during development, not for distributing finished software products to customers.
*C) AWS Marketplace*
	Correct. AWS Marketplace is a digital catalog and online store where independent software vendors (ISVs) can list and sell their software and services. It is *specifically designed for AWS customers to find, buy, and deploy third-party software directly on AWS, often with a few clicks from the AWS Management Console.*
D) AWS Service Catalog
	used by organizations to create and manage catalogs of IT services -> designed for governance within a company, not for distributing commercial software to external customers.

Which AWS resource provides detailed documentation on AWS services, including API references, developer guides, and tutorials? -> Document not Blog. This is hard to Classified.

## Full Test 2
**Improvement:**
+ **AWS S3 Storage Tiering.** 
+ AWS Security service Comparison with Usecase - AWS CloudTrail, CloudWatch, Trusted Advisor and SecurityHub. Note SecHub provide comprehensive view for ur AWS Team across multiple account, service (GuardDuty, Inspectir and Macie).
+ **AWS Cloud Adoption Framework (CAF) - 6 perspective**
+ Cloud Characteristic. 
+ Data Soveignties -> AWS Region in multiple contries in the world. 
+ AWS IAM Identity Center also know as AWS Single Sign-On or SSO) -> allow central management of access to mutl aws acc and application. 
+ AWS Security
+ AWS Code service - AWS Code Build -> compiles source code, runs tests, and produces software packages that are ready to deploy.
+ How to use TCO calculator -> for example, you have to input on-prem facilities cost like power (electricity) and colling to accurately calc the total cost of ownershup comapre to aws. 
+ AWS AI service:
	transcribe - aws speech recognition (ASR) convert speech into text -> transcribe audio and video files. 
	translate - duh 
	polly - TTS or text to speech service that convert text into human like speech. 
	comprehend - use nlp service that use ml to find insight understand relationship within text basically understand or comprehense human itention in text -> for recommendation engine. 
+ AWS Amplified -> amplified BE engineer power by provide a set of tools and services for build, ship and host a fullstack application and mobile application. Like a framework and CLI to easily provision and integrate BE feature lika auth, data storage and serverless APIs. 
+ Service that help Analyze, Debug and provide a Visual map of its component in a Microservice -> AWS X-Ray.   


Note: Resource Pooling mean multiple user shared and used the same Resource like AWS Compute and Storage Resource. 
Share control between customer and AWS -> Patch Management bc this cinclude patching underlying infras, hypervisor and physical hardware. While the customer patch their own gues OS and application. To conclue, they patch different component but still shared control. 

