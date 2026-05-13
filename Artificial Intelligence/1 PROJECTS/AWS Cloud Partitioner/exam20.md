# Practice Exam 20

Click on the **Answer** button for the correct answer and its explanation.
---

1. Which AWS service helps identify malicious or unauthorized activities in AWS accounts and workloads?
    - A. Amazon Rekognition
    - B. AWS Trusted Advisor
    - C. Amazon GuardDuty
    - D. Amazon CloudWatch


2. A company wants to try a third-party ecommerce solution before deciding to use it long term. <br/> Which AWS service or tool will support this effort?
    - A. AWS Marketplace
    - B. AWS Partner Network (APN)
    - C. AWS Managed Services
    - D. AWS Service Catalog


3. Which AWS service is a managed NoSQL database?
    - A. Amazon Redshift
    - B. Amazon DynamoDB
    - C. Amazon Aurora
    - D. Amazon RDS for MariaDB


4. Which AWS service should be used to create a billing alarm?
    - A. AWS Trusted Advisor
    - B. AWS CloudTrail
    - C. Amazon CloudWatch
    - D. Amazon QuickSight


5. A company is hosting a web application in a Docker container on Amazon EC2. <br/> AWS is responsible for which of the following tasks?
    - A. Scaling the web application and services developed with Docker
    - B. Provisioning or scheduling containers to run on clusters and maintain their availability
    - C. Performing hardware maintenance in the AWS facilities that run the AWS Cloud
    - D. Managing the guest operating system, including updates and security patches


6. Users are reporting latency when connecting to a website with a global customer base. <br/> Which AWS service will improve the customer experience by reducing latency?
    - A. Amazon CloudFront
    - B. AWS Direct Connect
    - C. Amazon EC2 Auto Scaling
    - D. AWS Transit Gateway


7. Which actions represent best practices for using AWS IAM? (Choose two.)
    - A. Configure a strong password policy
    - B. Share the security credentials among users of AWS accounts who are in the same Region
    - C. Use access keys to log in to the AWS Management Console
    - D. Rotate access keys on a regular basis
    - E. Avoid using IAM roles to delegate permissions


8. Which AWS feature or service can be used to capture information about incoming and outgoing traffic in an AWS VPC infrastructure?
    - A. AWS Config
    - B. VPC Flow Logs
    - C. AWS Trusted Advisor
    - D. AWS CloudTrail


9. A company wants to use an AWS service to monitor the health of application endpoints, with the ability to route traffic to healthy regional endpoints to improve application availability. <br/> Which service will support these requirements?
    - A. Amazon Inspector
    - B. Amazon CloudWatch
    - C. AWS Global Accelerator
    - D. Amazon CloudFront


10. According to the AWS Well-Architected Framework, what change management steps should be taken to achieve reliability in the AWS Cloud? (Choose two.)
    - A. Use AWS Config to generate an inventory of AWS resources
    - B. Use service limits to prevent users from creating or making changes to AWS resources
    - C. Use AWS CloudTrail to record AWS API calls into an auditable log file
    - D. Use AWS Certificate Manager to whitelist approved AWS resources and services
    - E. Use Amazon GuardDuty to validate configuration changes made to AWS resources


11. Which service can be used to monitor and receive alerts for AWS account root user AWS Management Console sign-in events?
    - A. Amazon CloudWatch
    - B. AWS Config
    - C. AWS Trusted Advisor
    - D. AWS IAM


12. Which design principle should be considered when architecting in the AWS Cloud?
    - A. Think of servers as non-disposable resources
    - B. Use synchronous integration of services
    - C. Design loosely coupled components
    - D. Implement the least permissive rules for security groups


13. Which AWS services can be used to move data from on-premises data centers to AWS? (Choose two.)
    - A. AWS Snowball
    - B. AWS Lambda
    - C. AWS ElastiCache
    - D. AWS Database Migration Service (AWS DMS)
    - E. Amazon API Gateway


14. A batch workload takes 5 hours to finish on an Amazon EC2 instance. The amount of data to be processed doubles monthly and the processing time is proportional. <br/> What is the best cloud architecture to address this consistently growing demand?
    - A. Run the application on a bigger EC2 instance size.
    - B. Switch to an EC2 instance family that better matches batch requirements.
    - C. Distribute the application across multiple EC2 instances and run the workload in parallel.
    - D. Run the application on a bare metal EC2 instance.


15. Each department within a company has its own independent AWS account and its own payment method. New company leadership wants to centralize departmental governance and consolidate payments. <br/> How can this be achieved using AWS services or features?
    - A. Forward monthly invoices for each account. Then create IAM roles to allow cross-account access.
    - B. Create a new AWS account. Then configure AWS Organizations and invite all existing accounts to join.
    - C. Configure AWS Organizations in each of the existing accounts. Then link all accounts together.
    - D. Use Cost Explorer to combine costs from all accounts. Then replicate IAM policies across accounts.


16. The ability to horizontally scale Amazon EC2 instances based on demand is an example of which concept in the AWS Cloud value proposition?
    - A. Economy of scale
    - B. Elasticity
    - C. High availability
    - D. Agility


17. An ecommerce company anticipates a huge increase in web traffic for two very popular upcoming shopping holidays. <br/> Which AWS service or feature can be configured to dynamically adjust resources to meet this change in demand?
    - A. AWS CloudTrail
    - B. Amazon EC2 Auto Scaling
    - C. Amazon Forecast
    - D. AWS Config


18. Which AWS service enables users to securely connect to AWS resources over the public internet?
    - A. Amazon VPC peering
    - B. AWS Direct Connect
    - C. AWS VPN
    - D. Amazon Pinpoint


19. Which tool is used to forecast AWS spending?
    - A. AWS Trusted Advisor
    - B. AWS Organizations
    - C. Cost Explorer
    - D. Amazon Inspector


20. A company is running an ecommerce application hosted in Europe. To decrease latency for users who access the website from other parts of the world, the company would like to cache frequently accessed static content closer to the users. <br/> Which AWS service will support these requirements?
    - A. Amazon ElastiCache
    - B. Amazon CloudFront
    - C. Amazon Elastic File System (Amazon EFS)
    - D. Amazon Elastic Block Store (Amazon EBS)


21. Which of the following is a component of the AWS Global Infrastructure?
    - A. Amazon Alexa
    - B. AWS Regions
    - C. Amazon Lightsail
    - D. AWS Organizations


22. Which AWS service will help users determine if an application running on an Amazon EC2 instance has sufficient CPU capacity?
    - A. Amazon CloudWatch
    - B. AWS Config
    - C. AWS CloudTrail
    - D. Amazon Inspector


23. Why is it beneficial to use Elastic Load Balancers with applications?
    - A. They allow for the conversion from Application Load Balancers to Classic Load Balancers.
    - B. They are capable of handling constant changes in network traffic patterns.
    - C. They automatically adjust capacity.
    - D. They are provided at no charge to users.


24. Which tasks are the customer's responsibility in the AWS shared responsibility model? (Choose two.)
    - A. Infrastructure facilities access management
    - B. Cloud infrastructure hardware lifecycle management
    - C. Configuration management of user's applications
    - D. Networking infrastructure protection
    - E. Security groups configuration


25. IT systems should be designed to reduce interdependencies, so that a change or failure in one component does not cascade to other components. <br/> This is an example of which principle of cloud architecture design?
    - A. Scalability
    - B. Loose coupling
    - C. Automation
    - D. Automatic scaling


26. Which AWS service or feature can enhance network security by blocking requests from a particular network for a web application on AWS? (Choose two.)
    - A. AWS WAF
    - B. AWS Trusted Advisor
    - C. AWS Direct Connect
    - D. AWS Organizations
    - E. Network ACLs


27. An application runs on multiple Amazon EC2 instances that access a shared file system simultaneously. <br/> Which AWS storage service should be used?
    - A. Amazon EBS
    - B. Amazon EFS
    - C. Amazon S3
    - D. AWS Artifact


28. A web application is hosted on AWS using an Elastic Load Balancer, multiple Amazon EC2 instances, and Amazon RDS. <br/> Which security measures fall under the responsibility of AWS? (Choose two.)
    - A. Running a virus scan on EC2 instances
    - B. Protecting against IP spoofing and packet sniffing
    - C. Installing the latest security patches on the RDS instance
    - D. Encrypting communication between the EC2 instances and the Elastic Load Balancer
    - E. Configuring a security group and a network access control list (NACL) for EC2


29. What is the benefit of elasticity in the AWS Cloud?
    - A. Ensure web traffic is automatically spread across multiple AWS Regions.
    - B. Minimize storage costs by automatically archiving log data.
    - C. Enable AWS to automatically select the most cost-effective services.
    - D. Automatically adjust the required compute capacity to maintain consistent performance.


30. The continual reduction of AWS Cloud pricing is due to:
    - A. pay-as-you go pricing
    - B. the AWS global infrastructure
    - C. economies of scale
    - D. reserved storage pricing


31. A company needs an Amazon S3 bucket that cannot have any public objects due to compliance requirements. <br/> How can this be accomplished?
    - A. Enable S3 Block Public Access from the AWS Management Console.
    - B. Hold a team meeting to discuss the importance if only uploading private S3 objects.
    - C. Require all S3 objects to be manually approved before uploading.
    - D. Create a service to monitor all S3 uploads and remove any public uploads.


32. A Cloud Practitioner identifies a billing issue after examining the AWS Cost and Usage report in the AWS Management Console. <br/> Which action can be taken to resolve this?
    - A. Open a detailed case related to billing and submit it to AWS Support for help.
    - B. Upload data describing the issue to a new object in a private Amazon S3 bucket.
    - C. Create a pricing application and deploy it to a right-sized Amazon EC2 instance for more information.
    - D. Proceed with creating a new dashboard in Amazon QuickSight.


33. What does the AWS Simple Monthly Calculator do?
    - A. Compares on-premises costs to colocation environments
    - B. Estimates monthly billing based on projected usage
    - C. Estimates power consumption at existing data centers
    - D. Estimates CPU utilization


34. Who is responsible for patching the guest operating system for Amazon RDS?
    - A. The AWS Product team
    - B. The customer Database Administrator
    - C. Managed partners
    - D. AWS Support


35. Which AWS services may be scaled using AWS Auto Scaling? (Choose two.)
    - A. Amazon EC2
    - B. Amazon DynamoDB
    - C. Amazon S3
    - D. Amazon Route 53
    - E. Amazon Redshift


36. Which of the following are benefits of AWS Global Accelerator? (Choose two.)
    - A. Reduced cost to run services on AWS
    - B. Improved availability of applications deployed on AWS
    - C. Higher durability of data stored on AWS
    - D. Decreased latency to reach applications deployed on AWS
    - E. Higher security of data stored on AWS


37. A user who wants to get help with billing and reactivate a suspended account should submit an account and billing request to:
    - A. the AWS Support forum
    - B. AWS Abuse
    - C. an AWS Solutions Architect
    - D. AWS Support


38. Which AWS Cloud best practice uses the elasticity and agility of cloud computing?
    - A. Provision capacity based on past usage and theoretical peaks
    - B. Dynamically and predictively scale to meet usage demands
    - C. Build the application and infrastructure in a data center that grants physical access
    - D. Break apart the application into loosely coupled components


39. Which method helps to optimize costs of users moving to the AWS Cloud?
    - A. Paying only for what is used
    - B. Purchasing hardware before it is needed
    - C. Manually provisioning cloud resources
    - D. Purchasing for the maximum possible load


40. Under the AWS shared responsibility model, which of the following is a customer responsibility?
    - A. Installing security patches for the Xen and KVM hypervisors
    - B. Installing operating system patches for Amazon DynamoDB
    - C. Installing operating system security patches for Amazon EC2 database instances
    - D. Installing operating system security patches for Amazon RDS database instances


41. The AWS Cost Management tools give users the ability to do which of the following? (Choose two.)
    - A. Terminate all AWS resources automatically if budget thresholds are exceeded.
    - B. Break down AWS costs by day, service, and linked AWS account.
    - C. Create budgets and receive notifications if current of forecasted usage exceeds the budgets.
    - D. Switch automatically to Reserved Instances or Spot Instances, whichever is most cost-effective.
    - E. Move data stored in Amazon S3 to a more cost-effective storage class.


42. Under the AWS shared responsibility model, the security and patching of the guest operating system is the responsibility of:
    - A. AWS Support
    - B. the customer
    - C. AWS Systems Manager
    - D. AWS Config


43. Which AWS service makes it easy to create and manage AWS users and groups, and provide them with secure access to AWS resources at no charge?
    - A. AWS Direct Connect
    - B. Amazon Connect
    - C. AWS Identity and Access Management (IAM)
    - D. AWS Firewall Manager


44. Which AWS service provides on-demand of AWS security and compliance documentation?
    - A. AWS Directory Service
    - B. AWS Artifact
    - C. AWS Trusted Advisor
    - D. Amazon Inspector


45. Which AWS service can be used to turn text into life-like speech?
    - A. Amazon Polly
    - B. Amazon Transcribe
    - C. Amazon Rekognition
    - D. Amazon Lex


46. What is one of the core principles to follow when designing a highly available application in the AWS Cloud?
    - A. Design using a serverless architecture
    - B. Assume that all components within an application can fail
    - C. Design AWS Auto Scaling into every application
    - D. Design all components using open-source code


47. A user needs to generate a report that outlines the status of key security checks in an AWS account. The report must include:
    <br/> (The status of Amazon S3 bucket permissions, Whether multi-factor authentication is enabled for the AWS account root user, If any security groups are configured to allow unrestricted access.) <br/> Where can all this information be found in one location?
    - A. Amazon QuickSight dashboard
    - B. AWS CloudTrail trails
    - C. AWS Trusted Advisor report
    - D. IAM credential report


48. Which Amazon EC2 pricing model should be used to comply with per-core software license requirements?
    - A. Dedicated Hosts
    - B. On-Demand Instances
    - C. Spot Instances
    - D. Reserved Instances


49. Which of the AWS global infrastructure is used to cache copies of content for faster delivery to users across the globe?
    - A. AWS Regions
    - B. Availability Zones
    - C. Edge locations
    - D. Data centers


50. Using AWS Config to record, audit, and evaluate changes to AWS resources to enable traceability is an example of which AWS Well-Architected Framework pillar?
    - A. Security
    - B. Operational excellence
    - C. Performance efficiency
    - D. Cost optimization


