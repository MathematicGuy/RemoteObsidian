### Shared Responsibility (Physical and Software)
**AWS Responsibility (Infrastructure)** - Security "OF" the Cloud 
+ @ Infrastructure include its Physical, Hardware, Software and Networking
	Physical Security like their Data Centers, security of their chosen Operation System (Red Head, Ubuntu, etc..) Virtualization Layers and Networking connecting regions and AZ. 

**User Responsibility (Their Software & Setup)** - Security "IN" the Cloud
	Everything that the user uploaded to AWS is the User responsibility to taken care of. I mean the code wouldn't run itself if it on AWS's Cloud.

+ @ Their Software & Setup include Data, Application, Identity Management and Configuration.
+ ? The "Data" come from outside of AWS and may not in the user control so its could be hack most easily, The software if not handle carefully, could also be breaches and create vulnerabality. Identity Mangement and Configuration can be breach through Social Engineering where Employees is the suspects, 

**The "Shared" Nature shift between Service Type (IaaS, PaaS, SaaS)**
*IaaS (EC2) -* the user have more Control of their systems (OS, apps, data) but also required more responsibility. 
*PaaS (Serverless Lambda) -* the just mange the Data & Application, AWS manage the OS. 
*SaaS (Chime)* - AWS manages almost everything exceept for user Data.

#### Responsibility Use Cases:
**User Responsibility:** If your *code is perfectly secure* but your Initialization script (EC2 setup script) is *misconfiguration,* your server's network (include Database, Application Code, Data, etc..) open to the world or you accidently assign *overly broad IAM permissions*, your application *is compromised (unauthorized individuals (hackers/cybercriminals) have accessed).*  

**EC2 App Deployment (IaaS):** 
+ *AWS:* Protect their HardDrive, Maintaint their server rack, protect internet connection not like Cloud Flare.
+ *User:* Make sure the Data & Software is save without misconfiguration, setup S*ecurity Group and VPC to make sure your app doesn't expose to the public.* Granting only the *minimum permissions using IAM Principle of Least Provilege* necessary for users, roles, or services to perform specific tasks. 


**Platform as a Service (PaaS) - Amazon RDS**
You don't have enough money to extend your Database for the Upcoming high Traffic day. TO reduce the operation overhead and cost you move the RAG's system database out of EC2 and into AWS RDS (relational database system) -> *Don't worry about Scaling, Setup DBMS* (Data Base Management System like Microsoft SQL Server, MySQL, MongoDB, Oracle Database, etc..) *for your Database.*
+ *AWS:* Handle over patching the Database Operating system (e. OS update & security patches) and the software & hardware mantainance, you just have to upload your Data and DB Schema.
+ *User:* just have to configuring the db rules, ensure DB have network connection and security in your *VPC (only YOUR EC2 can talk to your RDS database via Security Group and only Explicit personel have accessed to your RDS database)* and enabling client-side data encryption. 

**Serverless/ Managed Service - AWS Lambda & AWS S3**
POV: you have money, fast deployment on a Decouple System. Your RAG docs now stored in S3 and Python scripts runs entirely on AWS Lambda function, Your Database run on AWS RDS or Aurora. 
+ *AWS:* manages almost everything (*hardware, OS, runtime env and infrastructure patching*) except for your Data and Access Permission.  
+ *User:* only responsible for the Core *"your data and who access it (IAM)"*, making sure only specific ppl have access to S3 bucket and your services in VPC to each of them (Lambda, EC2) are connected to eachother have the rights to read data from S3. Also *Customer data is Encrypted.*    


### Identity and Access Management (IAM) 
![[Pasted image 20260402164326.png]]

*IAM User* usually account with trusted user who *manage access within AWS account* itself like dev & admin, such as *granting permissions to dev, admin, or other users.* 
+ @ Trusted User. Have Pernament access unless Evoke. Don't have to authenticated twice to sign in.  

*IAM Role* is a account that been *assigned temporary specific permission by IAM user.*
+ @ Session access account (auto logout after a time period). Assigned temporary permission.
+ ! IAM Group only contian User not IAM role. 

*IAM policies* are JSON documents that define permissions for IAM Users, Groups, and Roles.

**AWS Organization:** *centrally manage* and govern *multiple AWS account.* Simplifying multiple account creation, *policy enforcement, resource sharing* and *consolidataed Billing.* OU mean Organization Unit (a Group of User with the same Range of Permission) - [The AWS Security Reference Architecture - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) (AWS Organization include all of this):
![[Pasted image 20260402163850.png]]
![[Pasted image 20260402163915.png]]



*Root* is the highest level of (policies) Container, use to apply basic policies for all Account (usually use to *Define Basic Rules and Policies* for all account). *Like Discord Admin.* 
	Each managed *account* can be *invited from outside or created within the org.* 
+ *Organization Units (OU):* group of Account that have the same policies.
+ *IAM Policies* (like in real life) help restricting or setting boundaries for each account. Most *important policies is "Service Control Policy (SCP)."*
	*SCP Don't Grant Permission but DEFINE the MAXIMUM Permission that IAM users and roles can have*, Apply to all IAM user 
	+ ? The Root user setup highest permission & power 1 user can have. So if "high level user" abuse role to assign high permission to Member account, they can't.
	+ Other Use Cases:
		Restrict access to specific AWS services
		Prevent risky actions (e.g., deleting logging resources)
		Enforce organization-wide security and compliance standards
![[Pasted image 20260402141322.png]]
+ @ Make sure each Units of your Company (accountant, engineering, marketing) only have access to the right Services with the Root User Managed and Monitor all account in each Region Globally, this include (setup IAM policies and Billing).
	Note that Root User still have to pay 1 last time for the Removed Account, but after that Bill are seperately. 


**Set up Permission with AWS Organization workflow:**
![[Pasted image 20260402143036.png | 777]]


### Key Management Service (KMS), SSM 
For Security and compliance
AWS KMS - can be integrated with **Amazon S3, EBS, RDS, Lambda, and SSM** to handle data encryption and decryption. 
	Because *data is encrypted by key*, key enryption also mean data encryption. ![[Pasted image 20260402170917.png]]

**Server-side Encryption at Rest**
AWS KMS offer encryption AT REST for S3- "At rest" in refers to ==securing data that is actively stored on persistent storage devices (like disks, SSDs, or S3 buckets) rather than data currently moving over a network==
![[Pasted image 20260402173350.png]]

**Client-side Encryption**
![[Pasted image 20260402173412.png]]

KMS can have **Multi-Region Keys** -> You just have to create the Primary keys the replica across region. 
![[Pasted image 20260402173936.png | 666]]


### AWS Certificate Manager (ACM) 
Integrations with (load TLS certificates on)
+ Elastic Load Balancers (CLB, ALB, NLB)
+ CloudFront Distributions
+ APIs on API Gateway
+ ! Cannot use ACM with EC2 (can’t be extracted)
![[Pasted image 20260402164526.png | 677]]


To Certified, you need to requesting Public Certificates: 
![[Pasted image 20260402171455.png | 666]]

ACM sends daily expiration events starting 45 days prior to expiration. 
![[Pasted image 20260402171645.png | 444]]



### AWS WAF (Web Application Firewall), Shield, Firewall Manager 
**AWS WAF (Layer 7 FOCUS (Application), inspect HTTP/HTTPS)** - protect from web exploits and malicious traffic *from cookies, headers, payloads*. *CREATE security RULES to filter and manage web requests* based on conditions such as IP addresses, HTTP headers, query strings, and more.
![[Pasted image 20260402175034.png]]
	Can be integrated with AWS services like Amazon CloudFront, Application Load Balancer (ALB), API Gateway, and AWS AppSync. 
+ Example: 
	+ *Define Rules to block, allow, or count requests based on specific conditions* like IP addresses, HTTP headers, or geographic locations (These rules could be Manged by GROUP). 
		+ ? Example: unauthorized login using compromised/hacked credentials, Filter web Traffic (No traffic from China allow for example, DDOS Mitigation.  
	+ Real-Time Monitoring
	+ DDOS *protection against Layer 7 DDOS* attack.
	+ Auto-Scaling to handle increased traffic.
+ ! Rule Setup can be complex if unfamilier with Web Security. Layer 7 FOCUS, does not address lower network layer attacks. ![[7 Layers of AWS Security.png]]
+ ? Practice [DDoS Protection on AWS with AWS Shield and AWS WAF]([Advanced DDoS Mitigation (Layer 7) - AWS Shield :: AWS Security Maturity Model](https://maturitymodel.security.aws.dev/en/3.-efficient/shield-advanced/))

**Fixed IP with Load Balancer** for WAF. 
+ ? Application Load Balancer support WAF (Layer 7) but does not provide fixed static IP address because Network Load Balancer is at Layer 4.
+ $ The trick is use *Global Accelerator with Fixed IPv4* for static IP address with All incomming traffic being route to the ALB -> work like a Network Load Balancer. 


**AWS Shield Standard** - free, auto service *protecting DDOS attack.* Protect Layer 3/4 DDOS attack.
-> Ensure website/app stay HA during network attack. 

**AWS Shield Advanced (3000$/month per org)** - cost Money. Protect 7 Layers. Custom Detection based on traffic pattern, *24/7 Support from AWS DDoS Response Team (DRT)*, include *DDOS Insurance* for *Cost Protection*, offer *near real-time attack diagnostics* via CloudWatch, AWS WAF integrated (no additional cost), *SRT proactively contact you during DDOS event*. 
-> Use for Business Critical Mission.

**AWS Certificate Manager (ACM)** is used to provision and manage TLS/SSL certificates.
	Directly with services like **Elastic Load Balancers (ALB, NLB, CLB), Amazon CloudFront, and API Gateway** to secure HTTP requests

**AWS Security Token Service (AWS STS)** is a web service that provides temporary, limited-privilege credentials for AWS resources. 
+ @ The *same as Access Token.* Act as a Temporal Security Key (15' - 12h). Support federated access (ie. outside user have access without creating IAM user)  
+ Best Practice - [AWS STS - Search](https://www.bing.com/search?pglt=417&q=AWS+STS&cvid=4b88fa7751e04f86830bd38ac7869465&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOdIBCDExMjVqMGoxqAIIsAIB&FORM=ANNTA1&PC=U531):*
	1. Configure your workloads to *use Regional AWS STS endpoints for better performance and reduced latency.*
	2. *For automation, use IAM roles* to automatically obtain temporary credentials without manual intervention.
	3. *Enable AWS CloudTrail to log and monitor AWS STS* API calls for auditing and troubleshooting.


**Access Control Lists (ACLs)** - *manage access to resources (buckets and object/file)* at different levels, such as Amazon S3 buckets or Virtual Private Cloud (VPC) subnets. Offer fine-grained control - [what is AWS ACL - Search](https://www.bing.com/search?pglt=417&q=what+is+AWS+ACL&cvid=901bf0cd948343409ca93b6b219a83f9&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgcICBDrBxhA0gEIMzc3MGowajGoAgiwAgE&FORM=ANNTA1&PC=U531) 
+ $ Often *use to protect private File.* 
+ ? You don't have to use ACLs unless Object-level (Object are File) permission are required, just use bucket policies for access control. 
	Note that a S3 object represent a file (5TB max size) - [what is a Object in S3 - Search](https://www.bing.com/search?pglt=417&q=what+is+a+Object+in+S3&cvid=5e1bf02ecd3a4e65adc7d2b305ad26ba&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgcICBDrBxhA0gEIMjg5MGowajGoAgiwAgE&FORM=ANNTA1&PC=U531)


### AWS GuardDuty, Inspector, Macie
-> Analyzing security vulnerability on EC2 instance

**AWS GuardDuty** - continuously *analyzes security-related **AWS logs (VPC flow logs, DNS query logs, Cloudtrail logs).*** 
+ @ Runtime Threat detection. Using **machine learning, anomaly detection, and threat intelligence**,
Usecase - [aws guard duty vs inspector - Search](https://www.bing.com/search?qs=LT&pq=AWS+Guard+duty+vs+&sk=CSYN1&sc=10-18&pglt=417&q=aws+guard+duty+vs+inspector&cvid=cfc6bfc399bd4db4acab27279aa027b8&gs_lcrp=EgRlZGdlKgcIABAAGPkHMgcIABAAGPkHMgYIARBFGDkyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBwgIEOsHGEDSAQg1NjkwajBqMagCCLACAQ&FORM=ANNTA1&PC=U531): 
	Detects compromised EC2 instances, IAM credential misuse, and unauthorized access.
	Identifies anomalous API activity, such as high-volume IAM actions.
	Alerts on network reconnaissance, such as scanning for open ports..
+ ? Monitor real-time *AWS accounts, logs, and network traffic* (like VPC Flow Logs, CloudTrail events, DNS logs, and EKS audit logs).

**AWS Inspector (identifying risks/vulnability scanner):** *scans EC2/ECR instances*, containers, and Lambda functions for software flaws -> *Scanning resource for vulnability and misconfiguration* like Outdated software, misconfiguration, missing patches or exposed network ports (also support DevOps pipeline). 
+ ? Monitor real-time Vulnability in *Software* and unintended network setup *(network exposure)*. 
![[Pasted image 20260402175846.png]]


**AWS Inspector vs GuardDuty** in short while:
+ Inspector is resource-focused by *scan for vulnerability from inside.*
+ GuardDuty is activity-focused by *detecting threat from outside.*

	**AWS Macie is serverless** use *ML and Pattern Matching to auto Discover, Classify and Protect Sensitive data* (like PII e.g. name, email, IDs financial data and credentials) stored in *AWS S3 buckets.* S3 Protection focus. *Regional Level* ![[Pasted image 20260402180128.png]]




