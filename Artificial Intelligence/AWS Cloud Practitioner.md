![[Pasted image 20260224143748.png]]
---
## Leson 1: Cloud Concepts
**How to build a server ?**
1. close to my location for (easier maintainance, low connection lantency)

*On Premise (at current location) vs On Cloud (other people machine)*
Avoid Single Point of Failure - occur when a large system designed so baddly it have a CHOKE point. if that 1 Point go down, everything go down.
+ ? How to avoid -> have a load balancer - Distribute the Load.

*What if an unexpected problem happened ?*  - like outage problem ?
![[Pasted image 20260310160140.png|499]]
-> Have *multiple Backup* -> but I don't have money for backup -> use AWS :))

**Problem:** what if we want to expand our bussiness to Thailand ?
	SME (Small-Medium Enterprise)
	Low Latency and ThaiLan Data Comliance.
+ CAPEX (Capital Expenditure) - have a lot of money resource to open another datacenter at Thailand.
+ *Elasticity (flexible compute expansion) -* save cost by only expan vertical or horizontal when there're demand.
+ Business Concentration - need 1 person to lead the Data Expansion mission while you the CEO doing Businesses.
	Allow Agility (Data Center deployment) scalable and flexible Resource Usage.

**PaaS (Platform as a service)**
![[Pasted image 20260310161337.png]]

*Software Deployment - classified by responsibility*
![[Pasted image 20260310161440.png]]
*IaaS - Infrastructure as a Service (Cloud basis)*
e.g. amazonEC2
PaaS - Platform as a Service
SaaS - Software as a Service

**Why do we use Cloud ?**
Main Limitation:
+ Need a guy with Cloud and Deployment knowledge
+ Need another guy for monitoring and maintenance
+ Too much Cost to deploy DC on premise as a Startup
	and doesn't not always have a lot of customer - userbase migh spike a day then flatten for a week.
But good if you are a big company with privacy concern and need long term benefit.
![[Pasted image 20260310162747.png]]
*Cloud is just better short-term*, period.
![[Pasted image 20260310162756.png]]

Overall, in COST.
```ad-summary
*OPEX (Operating Expenditure):* is more eco in the **long-term invesment** and offer ultimate controlled. In DevOps, use when u have a strong DevOps team, fast prod experient cycle or don't need expand Data Center over time or Globaly.

*CAPEX (Capital Expenditure):* is more eco shorterm and userbase-flow fluctuate a lot (not stable). Keep the business running but more costly in long term
```
![[Pasted image 20260310163945.png]]

**Hybird (AWS Outpost)**
However, *why use 1 when you could use Both*. In LLMOps, we could run Small Model and Processing service on local machine while run LLM on Cloud to save electric and inference cost (bc cloud have better GPU that are fast and cheaper to run).
![[Pasted image 20260310164308.png]]

*Provision and Deprovision in DevOps/Cloud*
*Provision* - expand network, hardware. Updating use acess (ADD)
*Deprovision* - removing network, hardware. User access (REMOVE)
*Availability* - available workload that is *% its available* when you need it at any point of time.

*Reliability* - system *resiliency and minimizing downtime*. e.g. achive HA by deploying on Multi-AZ.

*HA* mean designing system so they *remain active* even *when 1 or more server fail*.

*Agility* talk about IT *Development and Deployment speed*. Ability to provision and deprovision compute and storage resources quickly (in a few minutes) with minimal effort.

*Elasticity* talk about *Optimize Resource usage with Auto-Scaling*, how *efficiency your system expand and shrink to handle fluctuated traffic* without over-provision.
-> Question ask the user compare Agility and Elasticity.

---
## Lesson 2: AWS Global Architecture
+ @ *Goal:* Chọn Region phù hợp cho workload

*Multi-AZ:* act like a load balancer to directs loads to multiple instances.
*AWS-Region:* location with multiple data-centers (note: each region is isolated from other region) e.g. ap-southeast-1, eu-central-1
	SaaS company runs workloads in multiple regions so latency between users to server is reduce.

+ When selecting *Region, think about latency, compliance/data residency* (control that house that data centers and its guideline)
	Note: *Price is not the main deciding factor*

*Elastic data Center (ECs)*  or *Amazone EC2 (Amazone Elastic Compute Cloud):* virtual servers in the AWS cloud.  Basically **a Data Center**

*Available Zone (AZ)* - 1 or more *independent data center within a region.* (with its owns cooling, power, networking system)
	*usecase:*
	+ app run 2 ECs (data center) in 2 different AZ so if 1 EC fail the other take over.
	+ a startup use loadbalancer to distribute dataloads traffic automatically AZ-1 and AZ-2.

What about *Multi-AZ,* well likewise Multi-AZ improve avaibility of your systems.
![[Pasted image 20260312202204.png]]

*Route-53 (port 53 use for DNS)* - Amazone Global Traffic mangement -> tell browser *where to go.*
	e.g.
	+ 1 website have multiple servers like google, route-53 help me to connect to the nearest server.
	+ So when a server is failover (unavailable) Route-53 route traffic to other server.

*Content Delivery Network (CDN)* - network of interconnected servers that speeds up webpage.
*Edge Locations (**cache data between Server and End-User**)* -  sites AWS use CDN to *speed up latency* (connection speed) using *Cache.*
	*Intuition:* Delivery Company instead of storing all package at the main Warehouse, they distribute item across local warehouse within the region.

*Usecase:*
+ Global websites accelerates drelivery of images, CSS and JS files through Edge caching.
	+ DNS queries for global app are process through *AWS Edge infrastructure like Amazone Route 53.*
![[Pasted image 20260312202344.png]]
![[Pasted image 20260312202430.png]]
Have good security.
![[Pasted image 20260312202641.png]]

---

`Region(Avalibility Zone(Edge))`
	*1 to Many*
Trong kiến trúc AWS, Region quyết khu vục có tài nguyên compute AZ mean Data Center.

Note: CloudFront is the network that provide Cache.
![[Pasted image 20260312204014.png]]
-> Sử dụng Edge Locations để Cache nội dung.
![[Pasted image 20260313004430.png]]
-> If Region include multiple server, then Edge is like a Mini-Server used to speed up data transfering speed using Cache.

*HA (High Avaliability) Patterns:* basically a designing (system) pattern so that your **system remain in Operation if 1 or more components fail.** (basically low downtime bc your server don't go down)
	HA achieve often achieved by
	+  using ECs from multi-AZ, Load Balancing (direct traffict from 1 EC to another EC) and enable Auto-Scaling (if more traffic increase)
	+ uses redundant server and replicated databasees across AZs to reduce downtime.
*Usecase:* Netflix use Auto-Scaling and Load-balancing to handle large traffic in the Weekend.
+ $ In Exam, *HA* is strongly associated with *Multi-AZ deployment*.
+ ? Why does AWS typically maintain at least 3 Availability Zones in a modern Region instead of just 2 ? -> Follow the N + 1 Rule. If 1 EC go down, then the other 2 EC can handle the extra 50% workflow to maintain full system functionality. :)) I mean if 1 EC already take 50-70% of workload, you cannt expect it to take another 100% of the workload, that too much.


*Multi-AZ  vs Multi-Region (Asia Pacific)*
*Definition Note:*
+ 1 Region contain multiple AZ (available zone), available zone contain multiple ECs (server).
+ *Region Example:* Asia Pacific (hence ap)
+ *AZ example:* ap-south-1, basically zone with Mltiple Amazone Server (Cluster of Server)
+ ? Multi-AZ mean deploy deploying multiple server across multiple Available Zone (AZ) within a Region to improve availability in case of Disaster and when global traffic increase bc if a server is full u would need another server.
*Usecase:*
+ *Availability Back-Up:* web app deploy runs on multiple AZs in Asia Pacific (ap-south-1, ap-southeast-6) so the services remains available even if 1 AZ goes down.
+ *Banks use Multi-AZ in 1 region for uptime and Multi-Region for disaster recovery planning*.
+ Wuthering Waves setup 1 AZ in Asia and 1 AZ in Europe, 1 AZ in American and 1 AZ in Brazil so player enjoy low latency across the world.
![[Pasted image 20260313004316.png]]

 + @ **Connections & Association**
	*Multi-AZ (multiple server within 1 Region)* $\to$ HA (high availability)
		service: EC2, RDS, Lambda, VPC
	*Multi Region (AZ across region)* $\to$ Disaster Recovery (*DR*) & Global Connection/Users - also help Isolated Error.
		service: IAM, Route 53, CloudFront

*Disaster Recovery (DR)* strategy and process used to restore systems, data and operation after a major failure like cyber attack, outage or regional failure.
	if Multi-Region help with DR, then Multi-Region HA is a architecture that  ensure HA in a Global Disaster this call Global Resilience.

*Common DR Approaches:*
+ Backup and Restore - backup in another region after failure
+ Pilot Light -


+ ! Regional Server is a Huge Open Network that you have minimal control over.
+ $ _A VPC seperates the giant network_ of the AWS data centers _into smaller isolated virtual network_ and let you build out rules about what networked resources you want to be able to talk to what other networked resources.
	VPC like a private LAN at home.

**RTO & RPO:** 2 most important metrics when evaluating *Business Impact analysis* in case of a disaster happened - [reference](https://scalefactory.com/blog/2022/05/11/disaster-recovery-strategies-on-aws/)
+ **Recovery Time Objective (RTO) -** maximum acceptable delay between the interruption of server and restoration of service *ie. How much downtime you can afford ?*
+ **Recovery Point Objective (RPO) -** maximum amount of time since the last recovery point. *ie. How much data to you willing to lose to save money ?*
![[Pasted image 20260313005519.png]]

*Disaster Recovery Strategy Ladder* the higher the better but more expensive. (so choose by Budget)
![[Pasted image 20260313005706.png]]
+ *Backup & Restore* - backup data in another Region and restore data after the incident.
+ *Pilot Light* - keep env always Running at LOW. ie. *server run at minimal condition.*
+ *Warm Standby* - keep a *scaled-down but functional env running.*
+ *Multi-Site (Active-Active)* - achieve zero-downtime by running prod workloads across Multi-Region at the same time.
+ @ **Exam Tips:** remember Multi-AZ HA help HA and Multi-Region HA help Regional DR.
+ ? Contries compliance and regional latency are often more important than cost in scenario question bc cheap region could not be ultilize it a useless server.


*Multi-AZ (in 1 Region) ko thay thế đc Multi-Region Disaster Recovery* if the Disaster is over a Region.
+ ! Cons: *high cost for duplicated resources aross reigion* (inter region data transfer)
-> very expensive if required no downtime continuously. But resilience between region failures.

Multi-Region for Disaster Recover
	protect from regional disaster.
	or having multi-region customer
	but required you to have a Budget.

Multi-AZ for normal usage (protect data center failure) - low lantency - don't need syncronous replication.
	Limited cost and team size

*Identity and Access Management (IAM) -* this is multi-region.  IAM help achieves data compliance bc its help to protect personal data and keep it private using secure authentication levels to access personal data (Data access by level).
![[Pasted image 20260313011550.png]]

![[Pasted image 20260312212316.png]]
**Key Take-Aways:**
	Region and Multi is the CORE
	Must have multi-AZ for every workload (IMPORTANT invest)
	Multi-Region required for mission critical.
	Choose the right disaster recovery base on current budget.

+ @ Goals: Draw the entire AWS infrastructure and explain the design.
+ ? Visualize traffict direction and AWS infrastructure as we explain.

*AWS Shared Responsibility Model* -  AWS manages security **"of"** the cloud *(physical infrastructure, hardware, software, networking)*, while customers manage security **"in"** the cloud *(data, applications, OS patching, configurations)*

*Synchronous* = Multi-AZ (same region, high speed, zero data loss)
	send and receive at the same time.
*Asynchronous* = Multi-Region (different region, lower speed, disaster recovery)
	both size send data with latency gaps in between, allowing the receiver to process each byte as it arrives.

[Good Disaster Recovery Video](https://youtu.be/s_K-ntsb-cM?si=tpGSni0wVO01fGbl)

----
## Lesson 3: AWS Infrastructure + Compute Cloud and Serverless 
+ @ Goal: Understand AWS serverless service (ESC Fargate, Lambda, Auto-Scaling) and What EC2 Instance type to choose. 

### 3.1 Review: AWS INFRASTRUCTURE
*Decoupling -* design principle of separating system component so they ca operate independently and reduce inter dependency (ie. component A must run for Component B to run)
*Consistency -* In term of latency and data, e.g. data storage in Asia is in sync with storage in Europe.
-> For data to synchronize better, we *use a primary database* (new data update to this db) between these 2 region so Database within each Region just need to read without the need of update. 
Reduce Latency -> Cloud Front Edge Location Cache.

AWS Tổ Chức Infrastructure của nó như thế nào ? -> Peer2Peer
![[Pasted image 20260320161437.png | 555]]
Distributed System like Logistic Network, Rail Network.

### 3.2 AWS Compute Cloud and Serverless
EC2 Instance - server (CPU + GPU + stuff)
EBS - Elastic Bucket Storage - for data storage 
ELB - Elastic Load Balancing -> distirbute workload across EBS and EC2 server.
ASG - Auto Scaling Group - auto scaling EC2 and EBS. 

AMI (Amazone Machine Image) - pre-setup EC2 instance for specific used. 
![[Pasted image 20260320203049.png]]
Note that EC2 is like your Desktop, you install thing and setup the required software as well as env. Rent a server ~ Rent a Work Station Computer.

There are 3 *types of AMIs*: 
![[Pasted image 20260320203416.png]]

*Boostrap EC2* - Basically write bash command within `User data` to *install pre-configuration to the computer/server during initial startup.* 
+ ? Example: run `.sh` scripts that download Pytorch, CUDA and python, uv and run pip install `requirements.txt` 
![[Pasted image 20260320204158.png]]

EC2 instance Naming Convention: `d` is for dev, `p` is for production. 

#### Practical Questions
*Which help to Control Traffic of AWS EC2*  

*AWS Free Services*
+ EC2 Server instance (12 Months Free Trial), AWS Lambda (1M request / month) 
+ AWS S3 Bucket Storage (5GB) - 12 Months Free Trial
+ AWS DynamoDB (25GB), AWS RDS (first 75- hr of db.t2/t3 micro is free)
+ CloudFront (Cache) - 1st 1TB tranfer is free
+ BeanStalk & Cloud Watch is Free - [aws free web](https://aws.amazon.com/free/?ams%23interactive-card-vertical%23pattern-data-339318104.search=CloudWatch) 

*AWS Lambda (Faas - Function as a Service)* - serverless compute service (not runtime env) which contain runtime ev like Python, Java, etc... To use Lambda, you must:
+ Zip your script and libraries then upload them via AWS Console
+ Or *Dockerize your code and push it into Amazon Elastic Container Registry (ECR)* where you could *store, deploy and manage your code* -> more neat. 

AWS Lambda can be trigger by:
+ Defined API Call in your Code
+ S3 events - uploading a file to a bucket
+ Schedules - like Auto Run your AI validation & training Function every 2 weeks. 
+ Database changes - like when a row is added to DynamoDB
+ Internal AWS Events - EC2 shutting down
+ ? Lambda charge by the number of requests and the duration for your code to execute. e.g. 2 parallel function take up 2 min -> 4 min totals of cost.   
	
+ Example: AWS Lambda *run your API defined Function within a Docker Container Image or Zip Code Package when a Input Event is Trigger.* - Kind of like Docker to be honest but their Cloud Server is your Desktop.  

*EC2 Instance Family* ![[Pasted image 20260320171947.png]]
**Use Case Note:**
+ General -> mid tier (good for general use in mid web/app)
+ Memory Optimized for in-memory cache optimize scenario (ie. in RAM)
	`R-family` provides a *high RAM-to-CPU ratio* (ideal for in-memory cache and high-RAM database)
+ *Opposite of R-Family* which is have the best optimize RAM-to-CPU ratio, `Z-family` have *both high memory and CPU Compute.* 
+ `I-family` designed for high/low-latency workload, *random I/O to local storage*. IOPS - Input/Output Operations Per Second used for range Read-Write access to large datasets. 
	Use for *Large Data Read & Write in Data Warehouse*, Large Database.  
+ `C` for CPU optimised instances to handles large batch data processing, ML workload.
+ `p` family for parallel processing -> `p6e`  used to handle large workload like Image Processing.  remember `p` is for picture. 
+ Suffix (at the end) `g` indicates instances powered by AWS *Graviton* processor *which is ARM-based.*  
+ F1 for custom hardware (e.g. FPGA)
+ Suffix `d` indicates the instansces includes local *NVMe-based SSD storage.* 
	think `d` as disk
+ `t-family` for sudden spike workload but otherwize sit idle most of the time. 
	t as in tiny (indle workload) and turbo (fast increase for large workload)
+ `x-family` for *extreme in-memory (RAM)* application workload 
+ `h1` with `h` stand for HDD have balanced compute and memory and is optimzed for MapReduce and HDFS workload.  
+ `n` suffix stand for high-bandwidth networking. 

[EC2 instance Suffix rule:](https://sudoconsultants.com/ec2-instance-types-a-simple-guide/)
![[Pasted image 20260320210324.png]]
Common AWS Instance Suffix Meanings:
- *g (Graviton):* Powered by AWS-designed ARM-based processors.
- *i (Intel):* Uses Intel Xeon processors (e.g., `m7i`).
- *a (AMD):* Uses AMD EPYC processors (e.g., `m6a`).
- *n (Network Optimized):* Enhanced networking speed (e.g., `c6n`).
- *d (Disk/NVMe):* Includes local NVMe SSD storage.
- *e (Extended Memory/Storage):* Extra capacity per vCPU.
- *z (High Frequency):* High compute frequency.
- *b (Blackwell):* Indicates NVIDIA Blackwell GPU acceleration.


*EC2 instance purchasing options:*	
+ Spot Instance: this Instance use only spare EC instance, but they can be interrupt. 
	-> Use for processing workload that are 'interuption-tolerant'
	
+ [On-Demand Instances](https://aws.amazon.com/compare/the-difference-between-on-demand-instances-and-reserved-instances/) (No commitment): Pay by the second, ideal for short-term, unpredictable workloads or testing.
	
- [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/) (1–3 year commitment): Significant discounts (up to 72%) compared to on-demand, suited for stable, predictable usage -> *Need Upfront Money.* e.g. Rent for 1 year, pay for 1 year. ![[Pasted image 20260320172111.png]] -> for Stable, long-term workload bc upfront payment in a *Fixed Region.* 
	
+ *Savings Plans (flexible):* *Don't need Upfront Money*. *Dollar / hour Discount type*. e.g. `10$/hour` -> Use if you need to changes instance size or types frequenly like Fargate/Lambda.    
	
- *Dedicated Instances (No commitment):* Physically isolated at the host hardware level from other AWS account, often used for compliance.  *AWS choose a random dedicated instance for you* -> not share with anyone else.
	
- [Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) (1–3 year commitment): *Rent the entire Physical servers* dedicated to your use, offering visibility of cores/sockets for BYOL (Bring Your Own License) scenarios and strict compliance.  
	-> You could use a **Host ID** to *force my EC2 instance to run on one specific piece of hardware I have already rented*, rather than letting AWS pick a random empty one for me. Because of *strict compliance* that *require licenses per-socket, per-core and per-VM.*



![[Pasted image 20260320221715.png]]
Ref: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-change-tenancy.html
Rent Pricing at *On-Demand rate*

*Serverless* mean you don't have to manage the server, just push your Code Package and run. e.g. Number of Server instance, OS, Runtime, etc..
	Basically, you just upload your code and Lambda handle the runtime, scaling and high availability ie. the server.  

*AWS Auto-Scaling* - scale instance more or less base on demand. Have the ability to:
+ Auto remove unhealthy instance
+ Predict when and how to Scale base on forecast data
+ Adjust resource base on target metric (question at here)
![[Pasted image 20260320172556.png]]
Note that AWS Auto-Scale doesn't responsible for Cyber Attack bc its not Physical Server related & Pay-as-you-go model.

*EC2 - Private & Public IP (IPv4)*
![[Pasted image 20260320211144.png]]

*Elastic IPs* - If 1 EC2 instance fail, its IP address will be move to another EC2 instance replica to make sure the instance is always available. -> 2 diff instanec but the same IP -> that how website keep running even if 1 EC2 fail.

*EC2 Hibernate*
![[Pasted image 20260320212433.png]]
*Load system state and application state from RAM to EBS volumn* (given that you setup EBS S3 bucket first) -> Faster STARTUP. 
+ ? Because EC2 calc COST by second -> every second save through faster startup mean every dollar saved. 

(`Explain in Detail later`)
*Security Groups:* act as a virtual firewall for your EC2 instances group to control incoming and outgoing traffic.
+ ? For example, you have to have specific IP Address to enter the Dash Board page (where only admin could enter).  The same for server, *some server are private so you need security group to only some specific people can come enter.* 
![[Pasted image 20260320213040.png | 777]]
+ Inbound Rule - security for input Type (e.g SSH).
+ Outbound Rule - security for output Type. 


**AWS ECR vs ECS**
You store, manage and deploy your Docker Container Image on ECR -> then you pull 1 of that Docker Image from ECR to ECS to run on EC2 (server) or Fargate (serverless).  
-> Basically *ECR to store and manage* your Docker's Image and *ECS to Orchestrate and run* your Docker *Image pull from ECS.*  
+ ? Note that *Deploy $\neq$ Run*
+ ECR is a storage repository for container images. 
+ ECS is the compute engine that run containers.


*AWS ECR (Elastic Container Registry)* - manual Container setup and management. 

*AWS ECS (Elastic Container Service)* full managed container orchestration service that simplifed deploying, managing and scaling Docker-based application. 
Have 2 types:
+ AWS Fargate (serverless) - don't have to worry about the server as in serverless definition -> don't need to worry about Scaling, Patching, Securing and managing servers. 
+ AWS EC2 instances (server) - have ability to control your EC2 server. 
```ad-caution
*AWS Fargate* - often *cost more x6-10 times* than an well-optimize EC2 instance. However, its more convenience and fast. But *good for unpredictable traffic spike*. 
-> use Fargate for inrrupt-tolerant task.
-> use EC2 for predictable 24/7 workloads. 
```

#### Placement Groups
*Cluster Placement Groups* - group of EC2 that close together in a single AZ -> Help reduce Latency between Instance.  ![[Pasted image 20260321004956.png]]
*Spread Placement Groups* - Spread instances across multiple Availability Zone -> Help with High Availability (HA) ![[Pasted image 20260321004932.png | 666]]
*Partition Placement Groups* (combination of Cluster and Spread) - Cluster of instance run on mutiple Hardware Rack and Across AZ for Partition -> Help reduce Latency on some Instance while maintain HA. ![[Pasted image 20260321005022.png]]
+ ! Number of partition per AZ limited to 7.
+ ? Use in Distributed System like HDFS, Hadoop, Cassandra and Kafka. 

#### EC2 Storage
*Elastic Block Store (EBS)* - *network-attached disk* that can be attached to a running EC2. AWS automatically attaches an EBS volume called the Root EBS Volume to EC2 instance at launch. 
![[Pasted image 20260321005839.png]]
+ $ Data remains even if the EC2 instance stops or terminate bc they're network attached. 
+ ! Limited to 1 AZ.
+ ? Usually attached to ONE instance at a time (Except for io1/io2 multi-Attach)

Optional: turn on Delete on termination to delete EBS along with EC2 instance. 
![[Pasted image 20260321005915.png]]

*Snapshots -* *point-of-time* backup of an Amazon EBS volume. 
-> Can be Copied across regions or shared across AWS accounts ![[Pasted image 20260321010217.png |444]]

---

AWS service to host static website -> S3

**Key S3 Glacier Storage Class Types:**
S3 Glacier Instant Retrieval 
+ Use Case: Medical images, news media assets, or infrequently accessed data needing immediate access.
+ Retrieval Time: Milliseconds
+ Min Duration - 90 days


S3 Glacier Flexible Retrieval (formerly S3 Glacier):
+ Use Case: Backup data, offsite storage, or data that does not need immediate access.
+ Retrieval Time: min to 12hrs (Expedited: 1–5 min, Standard: 3–5 hours, Bulk: 5–12 hours).
+ Min Duration - 90 day

S3 Glacier Deep Archive:
+ Use Case: Long-term compliance (regulatory, legal) or data accessed less than once a year.
+ retrieval time: 12 to 48 hours
+ Min Duration - 180 days


AWS EFS for Linux-base workload
	stored file in folder, accessed by file path and *shared by several application server*

**"AWS Intelligent-Tiering only (no further transition)"** means the storage class is set to **INTELLIGENT_TIERING**, but the optional, manual archiving tiers *(Archive Access or Deep Archive Access) have not been enabled*


*S3 storage lifecycle*
S3 Intelligent Tiering is genuenly the best for it automatic lifecycle management.
-> Its move data from Frequent -> Infrequent -> Archive -> Deep Archive based on access frequency.

Learn about OSI layer. 

