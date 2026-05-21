**Resources:**
+ [turtorialdojo - cheatsheat](https://tutorialsdojo.com/aws-cheat-sheets/)
+ [github - simulate real exam aws](https://github.com/untddanny/AWS-Certificed-Cloud-Practitioner-Mock/blob/main/Practice%20mock/exam1.md)  
+ [Examtopic - CL Practitioner Exam with Human Verification](https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner-clf-c02/view/2/)
+ [exam guide](https://tutorialsdojo.com/aws-cloud-practitioner-clf-c02-exam-guide/)

*kananinirav practice exam* 
	[Cloud Practitioner mindmap outline](https://kananinirav.com/mind-map-aws-ccp.html)
	[Practice Exam](https://kananinirav.com/practice-exam/practice-exam-1.html) ![[Pasted image 20260512135718.png | 555]]
*Jsbonso*
	[Exam Requirements](https://github.com/jsbonso/aws-certified-cloud-practitioner-clf-c02)

---
**Exam Descriptions** - [preference](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide_C02.pdf)
	50 questions / 90 minutes - 15 test question that hold 0 score.
	$\geq$ 700/1000 to pass ![[Pasted image 20260512134607.png]]

Cloud Concept - 24%
Security & Compliance - 30% 
Cloud Technology - 34% 
Billing, Pricing & Support - 12% 

*The exam validates a candidate’s ability to complete the following tasks:*
+ Explain the value of the AWS Cloud.
+ Understand and explain the AWS shared responsibility model.
+ Understand security best practices.
+ Understand AWS Cloud costs, economics, and billing practices.
+ Describe and position the core AWS services, including compute, network, database, and storage services.
+ Identify AWS services for common use cases.

## What to FOCUS on - Frequently asked Question
### AWS Pricing (pricing, TCO and cost optimization)
+ $ Always prioritize utility over pricing. Cheapest question isn't always right, the right question is the most Appropriate for the scenario's needs. 

**TCO (Total Cost of Ownership)**


**AWS Pricing Tools**


**Disaster Recovery Revision**

### Shared Responsibility Model
AWS Security by learning Best Practices for Security, Identity, & Compliance [webpage](https://aws.amazon.com/architecture/security-identity-compliance/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all).
AWS Security Tools.
IAM concepts user, group, policies and roles. 
AWS monitoring and logging features like Cloudwatch, CloudWatch Logs, VPC Logs, and [CloudTrail](https://tutorialsdojo.com/aws-cloudtrail/).
	Network level security and subnet level security.
AWS Well-Architected Framework - 
**AWS Support Plans** along with AWS Trusted Advisor. 


### AWS Well-Architected Framework


### Commond Scenario Example
#### Domain 1: Cloud Concepts 
**Why migating on-prem to AWS ? iow, what are the key financial benefits.**
-> Replaces upfront capital expense (CAPEX) with low variable operational expense (OPEX) 
-> Reduce the total cost of Ownership (TCO)

AWS Cloud **architecture design principle** (follow cloud best practice design)
1. Design for failure
2. Decouple components
3. Implement Elasticity
4. Think Parallel 

AWS Tools (e.g. Load Balancer) USE CASE. 

AWS VPC Design question like you need to enable EC2 instances in the public subnet to connect to the public internet -> Internet Gateway.

Service to resolve connection between on-premises VPN and AWS VPC. 

#### Domain 2: Security and Compliance
Compliance Related Document - AWS Artifact

It (ie. aws service) provides the event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command-line tools, and other AWS services -> AWS CloudTrail.

company need to download the compliance-related document in AWS -> AWS artifact (store docs and compliance)

improve security of IAM user ->  Enable MFA (multi-factor auth) and Configure a strong password policy.

Grant permission for S3 resource -> Bucket/user policy. 

It Scales up to milions of users and supports sign-in with social identity provider like Facebook, Google and AWS and ..  providers via *SAML 2.0* -> AWS Cognito -> *Manage user Authentication and Identity service that is Scalable.*

a company need to Evaluate IAM policies -> SImulator (IAM policy simulator)

Service that discorver, classifies and protects sensitive data like PII -> AWS Macies

Threat detection service that continously monitors for malicious activity to protect ur aws acc -> AWS GuardDuty

Prevent unauthorized deletion of S3 obj -> MFA

Someone need to control traffic going in and out of its VPC subnet -> NACL (Network Access Control List)

Responsibility (AWS vs User) to patch the host OS system of an EC2 -> AWS bc it physical.

#### Domain 3:  Cloud Technology and Services

Move/Transfer a lot of data at petabytes or exabyte-scale dataset -> AWS Snowmobile.

type of EC2 instance that allows you to bring your License -> Dedicated Host. 

Thing that Dev used to interact with their AWS service -> AWS CMD and SDKs. 

HA scalable cloud DNS web service in AWS -> AWS Route 53.

Store the results of I/O intensive SQL database queries -> AWS ElastiCache. 

Combinaiton of AWS service (more than 1) that allows u to servce the static files with Lowes possible latency -> S3 and AWS CloudFront.

Auto-scale the capacity of an AWS Cloud Resource (e.g. EC2, Database, etc..) based on incoming traffic to improve HA and reduce failure -> Auto-Scaling bc Load-Balancer only Distrbuted the Load to avaible Resource not Increase the resource capacity. 

Need Migrate database from on-prem SQL to AWS RDS -> AWS Database Migration Service (AWS DMS)

Auto transfer old data to more cost-effective storage class -> S3 lifecycle policy. 

Company need to establish connect for on-prem to AWS VPC -> AWS Direct Connect.
+ ? Usecase for Establish connection from prem to cloud.

AWS *ML service* that allow you to *add visual analysis features* to your app -> AWS Rekognition

Service that trace user requests in ur app -> AWS X-ray

Recommendation for saving money, improve system performance or closing security gaps -> AWS Trusted Advisor 

Speed content delivery across AZ around the globe (regional scope) - AWS CloudFront

Create and deploy infrastructure-as-code templates -> AWS CloudFormation

*Encrypt log data* that is stored and *managed by AWS Cloudtrail* -> AWS KMS

Database service can be used to store JSON docs -> AWS DynamoDB.

#### Domain 4: Billing, Pricing and Support 
Customer Estimated cost of moving its application to AWS -> AWS Total Cost of Ownershup Calculator.
Set target and get alert when utilization drops below the threshold you define -> AWS Budges. 
90% discount EC2 -> Splot Instance.
Cost-efficient storage option for retaining database backups that allows ocasional data retrieval in mins -> AWS Glacier. 
Forecast price based on past consumtion -> Cost Explorer.
Most Cost effective when you purchase a Reserved Instance for a 1-year term -> All Upfront. 
Cheapest plan that allow unlimited num of technical support cases -> Dev Support Plan.
Want to combine usage volumn discount across multiple AWS accounts -> Consolidated Billing.
Sell custom AMIs in AWS -> AWS marketplace.

**Support Channels**
Channels that shares a collection of offerings to *help you ACHIEVE specific business outcomes related to enterprise cloud adoption* through paid engagements in several practice areas -> AWS Professional Services. ![[Pasted image 20260512155337.png | 666]]
+ ? *AWS Professional Service* offering delivers a set of activity, best practice and docs, they help org design and accelerate path to successful cloud adoption. AWS Procfessional Services create the AWS Cloud Adoption Framework (AWS CAF) this help user realize measurable business benefits from clou adoption faster and with less risk.  

*AWS Enterprise Support ->* provides 24x7 technical support from high-quality engineers to managed the health of ur env, the consultative architectural guidance delivered in the context of your applications and use-cases And a designated Technical Account Manager (TAM) to coordinate access to proactive/preventative programs and AWS subject matter experts.

*Concierge (Lễ Tân) Support*  is for Enterprise Billing and account best practice so you can focus on running your business.

*AWS Technical Account Manager* - help plan and build solution using best practice, coordinate access to subject matter (main topic) experts and product teams -> Proactively keep your AWS env operationally healthy. 

```txt
A company is planning to launch a new system on AWS, but it does not have an employee with AWS expertise. Which of the following AWS channels can instead help the company design, architect, build, migrate, and manage its workloads and applications on AWS?

1. AWS Partner Network (APN)Technology Partners
2. AWS Marketplace
3. AWS Partner Network (APN) Consulting Partners
4. Technical Account Management
```

*AWS Parnter Network (APN)* there are 2 types of APN parners
1. APN Consulting partners
2. APN Technology partners
![[Pasted image 20260512161706.png]]
+ *Consulting Partners* - are service firms that *help customers* of all sizes *design, architect migrate or build new application on AWS.*  
+ *Technology Partners* - this *Provide Software solutions that are either hosted on or integrated* with AWS platform.
+ *Technical Account Management* - just a part of AWS Enterprise Support

## Weak Points
### [[AWS CLP Practice 1]]
[[Exam Topic CLP Practice]]

