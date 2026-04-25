![[Pasted image 20260224143748.png]]
[[AWS Final Project Review]]
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
*Application* - your Website/App Code
*Data* - dataset, model weight, information stored or processed by the application.
*Runtime* - execution environment for the code to run e.g. Bash, C/Java/Python Interpreter
*Middleware* - middleware function as software which support your code like Authentication function in ASP.NET (`Auth, UserAuthentication`), REST API service and Runtime environment too.
*OS (Operating System)* - software that manages hardware and software resources
*Virtualization* -  tech that allows a single physical server to be partitioned into multi-server "instances" e.g Virtual Disk, Virtual OS -> Enables AWS give you EC2 instances without giving you the whole physical machine.
*Servers* - other people computer (with CPUs, GPU & RAM) that perform computation,.
*Storage* - physical disk (SSDs or HDDs) where you store everything software related.
*Networking* - *physical and virtual cables* (ie. software to encode & decode sound), routers and switches that allow your application to communicate with the internet or other service.

*Software Deployment - classified by responsibility*
![[Pasted image 20260310161440.png]]
*IaaS - Infrastructure as a Service (You manage it)* e.g. AWS EC2
	Providing raw computing infrastructure allow Connection and computation World Wide (server, storage, networking across the world) without the need of sacrifying control.
-> For company that priortize control, customization like Google Cloud and Red Hat.
e.g. Digital Ocean (simple AWS), AWS S3 for Object Storage (ie. data), Azure Virtual Desktop (allow company to host entire Windows desktops in the cloud for remote employee)
+ ? Rent a Un-Setup Computer, you're freely to choose Deployment App like Docker, OS like Ubuntu or MacOS

*PaaS - Platform as a Service (You build on it - Tool for developers)*
	You just need to manage your app and data bc PaaS offers a complete develop and deployment env in the cloud.
e.g. AWS Elastic Beanstalk (for deploying and scaling web app), Vercel (frontend deployment), Supabase (Backend-as-a-service) provide instant PostgreSQL DB, Authentication service, *Heroku, Northflank.*
+ ? Basically Deployment Env where you push your code on.

*SaaS - Software as a Service (You use it)*
	Other people software that take care of everything, you just have to pay and use it.
e.g. AWS itself, Google Calendar, Youtube, Slack, Zoom


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
*CapEX (physical hardware setup, buying hardware stuff)* include purchasing physical assets (server, data centers, neworking and hardware).
-> AWS pay-as-you-go remove this Upfront burden. also eliminate over-provision.
*OpEX (operational cost)* - cost of running the hardware you bough in CapEX. This include cost like maintainant cost, physical security, etc...
-> AWS remove this burden, instead of operating you just used their infrastructures.

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

`Region(Avalibility Zone(Edge))` - *1 to Many*
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

*AWS Lambda (Faas - Function as a Service)* - serverless *auto-scale compute service* which *contain runtime ev like Python*, Java, etc... This is *THE SAME as Python Lambda Function*, you could upload your scripts by:
+ Zip your script and libraries then upload them via AWS Console
+ Or Dockerize your code and push it into Amazon Elastic Container Registry (ECR) where you could store, deploy and manage your code -> more neat.
To run, simply call your Scripts API function ([Python Lambda Practice](https://docs.aws.amazon.com/lambda/latest/dg/file-processing-app.html)).
+ ! *Lambda Limits:* 15' runtime, 10GB RAM.
+ @ Help to *test your code instantly* without the need of EC2 instance.
+ $ Could *Integrate other AWS serverless service.*
Other benefits:
1. *Run code without provision* (run instantly on a AWS HA Instance). *Simply write or upload* code as a `.zip` file or container image.
2. *Automatically respond to code execution requests at any scale*, from hundreds to thousands per second..
3. Pay only for the compute you use (*Pay-as-you-go*)



AWS Lambda upon triggering:
+ Defined API Call in your Code
+ S3 events - uploading a file to a bucket
+ Schedules - like Auto Run your AI validation & training Function every 2 weeks.
+ Database changes - like when a row is added to DynamoDB
+ Internal AWS Events - EC2 shutting down
+ ? Lambda charge by the number of requests and the duration for your code to execute. e.g. 2 parallel function take up 2 min -> 4 min totals of cost.

+ Example: AWS Lambda *run your API defined Function within a Docker Container Image or Zip Code Package when a Input Event is Trigger.* - Kind of like Docker to be honest but their Cloud Server is your Desktop.

**DynamoDB** - High-performance *NoSQL* that support massive scale (*Multi-AZ*). Auto-Scale, Low Operational Cost. ![[Pasted image 20260323173024.png]]
*Read/Write Capacity Mode*
+ Provisioned Capacity Mode (Default) - Pay for predefine resource (RCU - Read Capacity Units, WCU - Write Capacity Units).
+ One-Demand Capacity Mode - Auto-scaling, Pay for what you used but more Expensive.
![[Pasted image 20260323173148.png]]

DynamoDB DAX - improve *READ* and *reduce load on tables.*
![[Pasted image 20260323173422.png]]
Data Steam Processing (act as the Main Processor Database) - DynamoDB only have 24hr data retention so *to save data you have to move data to Kinesis Data Streams.*
![[Pasted image 20260323173436.png]]

*DynamoDB Streams*
Kinesis act as the main storage manage continuous stream of data.
![[Pasted image 20260323173627.png]]

*Global Tables* - replicated DynamoDB tables across multiple AWS Region.
![[Pasted image 20260323174110.png]]

*API Gateway* - use to *call Lambda Function* to call REST API
![[Pasted image 20260323174215.png]]





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

+ ! The **a Server $\neq$ a Instances** -> A Server could be partition into multiple Instance, so renting a dedicated instance is like renting a 1 parts out of all Instance within a Server.

- *Dedicated Instances (No commitment):* Physically isolated at the host hardware level from other AWS account, often used for compliance.  AWS choose *a random dedicated instance* for you -> not share with anyone else.
	*License Limit: No visibility* into physical sockets or cores. -> **cannot** bring licenses that require core-based or socket-based tracking.

- [Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) (1–3 year commitment): *Rent the entire Physical Servers (contain multiple instances)* dedicated to your use, offering visibility of cores/sockets for BYOL (Bring Your Own License) scenarios and strict compliance.
	-> You could use a **Host ID** to *force my EC2 instance to run on one specific piece of hardware I have already rented*, rather than letting AWS pick a random empty one for me. Because of *strict compliance* that *require licenses per-socket, per-core and per-VM.*
+ ? A *dedicated host runs multiple dedicated instance* bc you rent the whole Machine. Often cost more and you pay for them even when they are not used.

*Dedicated Instance vs Dedicated Host*
+ **Dedicated Instance** runs as a *virtual machine on hardware* reserved *for a single customer account.*
+ While a **Dedicated Host** provides an *entire physical server for exclusive use*, offering full control over instance placement d the underlying hardware detail.
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

![[Pasted image 20260323175825.png]]


**AWS ECR vs ECS**
You store, manage and deploy your Docker Container Image on ECR -> then you pull 1 of that Docker Image from ECR to ECS to run on EC2 (server) or Fargate (serverless).
-> Basically *ECR to store and manage* your Docker's Image and *ECS to Orchestrate and run* your Docker *Image pull from ECS.*
+ ? Note that *Deploy $\neq$ Run*
+ ECR is a storage repository for container images.
+ ECS is the compute engine that run containers.


*AWS ECR (Elastic Container Registry)* - Container setup and management.
![[Pasted image 20260323181059.png]]

*AWS ECS (Elastic Container Service)* full managed container orchestration service that simplifed deploying, managing and *scaling Docker-based application.*
Have 2 types:
+ AWS Fargate (serverless) - don't have to worry about the server as in serverless definition -> don't need to worry about Scaling, Patching, Securing and managing servers.
+ AWS EC2 instances (server) - have ability to control your EC2 server.
```ad-caution
*AWS Fargate* - often *cost more x6-10 times* than an well-optimize EC2 instance. However, its more convenience and fast. But *good for unpredictable traffic spike*.
-> use Fargate for inrrupt-tolerant task.
-> use EC2 for predictable 24/7 workloads.
```

*ESC Cluster*
![[Pasted image 20260323180230.png]]
+ $ If Auto-Scaling enable, ECS could deploy Container within each EC2 instance.
	+ ? Cần cài ECS Agent để autoscale docker bên trong EC2 instance.



#### Placement Groups
*Cluster Placement Groups* - group of EC2 that close together in a single AZ -> Help reduce Latency between Instance.  ![[Pasted image 20260321004956.png]]
*Spread Placement Groups* - Spread instances across multiple Availability Zone -> Help with High Availability (HA) ![[Pasted image 20260321004932.png | 666]]
*Partition Placement Groups* (combination of Cluster and Spread) - Cluster of instance run on mutiple Hardware Rack and Across AZ for Partition -> Help reduce Latency on some Instance while maintain HA. ![[Pasted image 20260321005022.png]]
+ ! Number of partition per AZ limited to 7.
+ ? Use in Distributed System like HDFS, Hadoop, Cassandra and Kafka.

**AMI** - Template for EC2 instance with pre-configuration env, OS and EBS snapshots.

#### Elastic Block Store (EBS)
*Elastic Block Store (EBS)* - *network-attached disk* that can be attached to a running EC2. AWS automatically attaches an EBS volume called the Root EBS Volume to EC2 instance at launch.
![[Pasted image 20260321005839.png]]
+ $ Data remains even if the EC2 instance stops or terminate bc they're network attached.
+ ! Limited to 1 AZ.
+ ? Usually attached to ONE instance at a time (Except for io1/io2 multi-Attach)

Optional: turn on Delete on termination to delete EBS along with EC2 instance.
![[Pasted image 20260321005915.png]]

*Snapshots -* *point-of-time* backup of an Amazon *EBS volume (Snapshot for data within the Disk itself - independent from the EC2)*
-> Can be Copied across regions or shared across AWS accounts  ![[Pasted image 20260322141845.png]]
*Could be attached to a newly created AMI*
![[Pasted image 20260323154030.png]]
Note that Snapshot is still storage so u basically could SAVE MONEY by moving snapshot to archive although it took 24-72hrs.
![[Pasted image 20260323154151.png]]


#### EBS Volumes come in 6 types
![[Pasted image 20260323154443.png]]
+ *IOPS (Input/Output Operations Per Second):* I/O performance of an EBS *-> Latency of the Input/Output*
	+ ? Number of read and write per second where each IOPS have N size.

+ *Throughput:* total volume of data transferred to and from the volume per second, typically expressed in MiB/s or MB/s  -> *Maximum amount of Data tranfer each Input/Output*.
	+ ? Throughput = IOPS × I/O Size

*SSD*-based Voumn for *Common Workload.* (small databases, and development environments.)
![[Pasted image 20260323155135.png]]

*Provisioned IOPS (PIOPS) SSD* is the Highest performance EBS storage designed for mission-critial and heavy workload.  ![[Pasted image 20260323155241.png | 555]]
-> SSD provide high IOPS and Throughput at the cost of money. Use for real time workloads.


*Hard Disk Drive (HDD)* design for storage. Have large, sequential throughput workloads with rather than high IOPS performance. There're 2 types: Cold HDD for slow tranfer speed and Throughput Optimized HDD for sequential workloads with decen throughput (~500MiB/s) both have large Storage. ![[Pasted image 20260323155815.png]]
*-> Trade Data tranfer speed for Storage. Much cheaper for storage.* Mostly for storage and save for later types of data. Like data to retrain later.


*EC2 Instance Store* - *TEMPORARY* block storage located on cache of the physical host machine attached to the EC2 instance.
![[Pasted image 20260323153529.png]]


*Sao lưu lũy kế (Cummulative Backup):* chỉ save những thay đổi mới (like github commit). Where each Snapshot version have a independence data (changes).
	e.g. Day 1 snapshot store 2GB of changes, Day 2 snapshot delete 1 GB & update 2 GB so 3GB change, Day 3 don't have any update -> 0GB of change. Very Memory Efficient.
+ ? But what if you delete the previous snapshot ? will it affect the latter snapshot sequenctly.
+ $ Like github, it just push the necessary changes from Day 1 Snapshot to Day 2 Snapshot, so the latter snapshot stay intact.

*EBS Encryption* - mã hóa ổ cứng. *The Catch* is you coudn't Encrypted a already running EBS Volumn. So simply, you could:
1) Create a Replica of the current EBS volumn then Apply Encryption
2) Detach the Old Volumn then Attach the New Volumn. (EC2 could be dettach/attach EBS volumn while running)
3) Start the Instance Again.

Note that *Serverless mean you don't need to setup anything. Just Plug-n-Play.* Anything related to workloads AWS takecare of them for you at the cost of MONEY (Auto-Scaling, Multi-AZ, etc...)
![[Pasted image 20260323160421.png]]
While *EBS (like S3) is single AZ & Manual-Scaling*, *EFS is multi-AZ & HA & Auto-Scaling*. Allowing *great used as the Central Data/Content Management System* -> Simplified Shared Content across Region. *Where EFS act as the main DB* where EBS across Region retrieval just the right data from it.
![[Pasted image 20260323161146.png]]


*EBS vs EFS vs Instance store vs S3* as a whole.
EBS act as the Long-Term storage within 1 AZ having their volumn's snap-shot stored in A3.
-> S3 coud be use for Backup. And EBS act as the Harddrive of the server.
EC2 Instance act as the Cache so High Performance.
+ act as the Cache Buffer (temp) between the Main EBS Storage and EFS.
+ only available when EC2 is running.
-> Like Copy and Paste, but on Globle Server Scale
![[Pasted image 20260323161313.png]]
Ref: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html
So
+ EFS act is a multi-AZ shared network folder that hundreds of servers across region can access.
+ EBS act is a single-AZ attachable databases for server. Like a Harddrive
+ S3 is a Object storage (files + metadata), can be access gloably.

*Scalability & HA*
Vertical Scalability -> Upgrade a Instance (more CPU, GPU, RAM, etc..)
Horizontal Scalability -> Copy & Paste More Instance/Template.
	often for Distributed System Architecture. Workload distributed across Instances (virtual server) or Servers (1 Server could have multiple virtual instance/server).
-> Improve Fault Tolerant (FT), Performance and Scability.
![[Pasted image 20260323161957.png | 888]]

*Types of HA*
+ Passive HA:  run only the 1st EC2 (running mode) while sync data to the 2nd EC2 (standby mode) -> Disaster Recovery
+ Active HA: Use EBL to distirbuted workloads across EC2s.

*Use ASG and ELB for Scalability*
![[Pasted image 20260323162706.png]]

*Security Group use-case*
*Isolate your backend servers* (EC2) so they **only** accept traffic from your Load Balancer (ELB), rather than the entire internet. ![[Pasted image 20260323163606.png]] -> EC2 instance will **only** accept traffic if it comes from a resource associated with that specific Load Balancer SG -> Help direct cyber-attack on the an EC2 Instance.

Types of Load Balancer (Left is Newer, Older to the Right):
![[Pasted image 20260323163822.png]]

**Application Load Balancer** - located in *Layer 7*
![[Pasted image 20260323163926.png]]

ELB could *route Traffic in 3 different Path:*
![[Pasted image 20260323164046.png | 444]]

*Target Groups:* allow Loadbalancer to *route traffic to multiple Group* instead of 1 single EC2 Instance -> *Target IP, instance, and AWS lambda function* target types.
![[Pasted image 20260323164235.png]]
**Example:**
1. HTTP Based Traffic
![[Pasted image 20260323164325.png | 777]]

2. Query Strings/Parameters Routing
![[Pasted image 20260323164418.png | 777]]


**Network Load Balancer** - locate at *Layer 4* becore ALB -> *Point directly at TCP/UIP Instance*
![[Pasted image 20260323164619.png]]
NLB Target Group - Think this as *Group Balancer for Application Load Balancer*
![[Pasted image 20260323164814.png]]
This mean, Like ALB Target Group but *could also Target of ALP* (Target types: *IP, instance, and ALB*)
![[Pasted image 20260323164911.png]]


*Cross-Zone Load Balancing* - Regional Load Balancer.
-> This features is *Turn On automatically* when ALB is used.
![[Pasted image 20260323165738.png]]

*Auto Scaling Group* -> *Create* new Instance *if the Condition is met.*
![[Pasted image 20260323170030.png]]
*Max Size -* max size to prevent cost explosion. Highest mode.
*Desired Capacity -* AWS will target for the Desired Capacity. If traffic Hit, increase to this desirer capacity or Launch new istance to maintain this capacity if some instance fail.
*Min Size -* Size to keep when there are Low Traffic and No Traffic.Think of this as Maintainance mode.

*Launch Template* - Auto-Created a pre-configuration EC2 Instance (Optional: add scaling policy for Auto-Scaling)
![[Pasted image 20260323171004.png]]

**AWS Cloud Watch** - *Monitor EC2 instance* performance (if reach a threshold) to notify when to Auto-Scaling -> Monitor CPU and hardware. *Monitor Metrics*
Note: firmware is low-level software.

**AWS CloudTrail** - captures actions taken through the Management Console, SDKs, and CLI, providing visibility into "who did what, where, and when" across AWS. *Monitor log in SDK and Code*
+ *Security Monitoring:* Detects unauthorized access or unusual activity patterns by recording every individual API call.

AWS *Artifact* -> *download AWS Compliance Report/Docs* and Certification.
AWS Certificate Manager (ACM) - creating, storing, and *renewing public and private SSL/TLS*
![[Pasted image 20260406214026.png]]


*Scaling Policies* - Auto-Scaling *Strategies*
![[Pasted image 20260323171400.png]]
Dynamic Scaling - Only Scale within a range of value (e.. > 70% -> scale-up or < 30% -> scale-down) -> Fixed.
Scheduled Scaling - scale within a time-period (like 8AM - 12AM) -> Fixed
Predictive Scaling - use ML algorithm to predict when to forcast scaling demand -> Automatic
Scaling Cooldowns - *sometime resource could not distributed data fast enough* to the new EC2, so we need cooldown to prevent inefficient scaling. e.g. *FE loaded while BE isn't.*

**Overview**
![[Pasted image 20260323171907.png]]

### Serverless
*AWS Serverless stack* ![[Pasted image 20260323172057.png]]


---

### 3.3 Storage System in AI & in Data Platform
*Important Note:* make usecase for each concepts that how business work. Like with this new function, what can I do with it -> Help gorup concepts with usecase and context.
[quiz](https://forms.gle/xuyqzAUaZqDjnVHS8)

**Key S3 Glacier Storage Class Types:**
![[Pasted image 20260323183009.png]]

![[Pasted image 20260323183043.png]]
*Requests:* Costs per 1,000 PUT, COPY, POST, or GET requests (varies by tier).
*Data Transfer:* Data transferred _into_ S3 is free; data transferred _out_ to the internet or other regions incurs costs.

*S3 Glacier Instant Retrieval*
+ Use Case: Medical images, news media assets, or infrequently accessed data needing immediate access.
+ Retrieval Time: Milliseconds
+ Min Duration - 90 days

*S3 Glacier Flexible Retrieval (formerly S3 Glacier):*
+ Use Case: Backup data, offsite storage, or data that does not need immediate access.
+ Retrieval Time: min to 12hrs (Expedited: 1–5 min, Standard: 3–5 hours, Bulk: 5–12 hours).
+ Min Duration - 90 day

*S3 Glacier Deep Archive:*
+ Use Case: Long-term compliance (regulatory, legal) or data accessed less than once a year.
+ retrieval time: 12 to 48 hours
+ Min Duration - 180 days

AWS EFS for Linux-base workload
	stored file in folder, accessed by file path and *shared by several application server*

**"AWS Intelligent-Tiering only (no further transition)"** means the storage class is set to **INTELLIGENT_TIERING**, but the optional, manual archiving tiers *(Archive Access or Deep Archive Access) have not been enabled*

*S3 storage lifecycle*
S3 Intelligent Tiering is genuenly the best for it automatic lifecycle management.
-> Its move data from Frequent -> Infrequent -> Archive -> Deep Archive based on access frequency.

*AWS Storage Gateway **(Specifically for Hybrid Cloud Storage)*** - Bridge/connecting *On-premise Infrastructure to AWS Cloud Service* for for backup, disaster recovery, and tiered storage -> *sync data between on-prem and cloud*
	Usecase: move on-premised data storage on an NFS file system to AWS Cloud Storage.
Compare to EBS and EFS -> they are on Cloud service.
	Note: EBS (Elastic Block Service) and EFS (- File Service -) and S3 is both block, file and tape (??)

Note to deploy static website on S3 you have to allow **Bucket policy**.
+ $ **GOAL:** Identify what I want to focus on the most. THESE Concepts took too much time.

---
## Lesson 5 - AWS Database and Integration
Amazon Neptune vs Amazon Simple Storage Service (Amazon S3) vs Amazon Relational Database Service (Amazon RDS vs Amazon DynamoDB

SQL: Aurora, RDS, RedShift
NoSQL: DynamoDB, Neptune (Graph), ElastiCache, .
Db Migration service:
+ AWS DMS: explain, example, usecase
+ Transit Gateway: ...

AWS Neptune - graph database service for highly connected datasets, such as recommendation engines, fraud detection, and knowledge graphs.
AWS SQS - allow user to decouple and expand microservice. Distributed system and serverless application.  Use Queue.
AWS Kinesis Data Streams design to process large amount of realtime data.
AWS *Redshift* - serverless cloud storage, *analyze large data* in TERA to PETABYTE for BI.
AWS Snowball - service that move data from on-premise to Cloud in Terabyte and Petabyte scale (hence snowball (rolling))

AWS Glue is for ETL (extract, transform, load)
AWS Storage Gateway is a hybrid-cloud storage service *for connecting on-premise with AWS Cloud.*
Read Replica help with Read Scability bc it reduce load on a single database.
*Redit in ElastiCache* support advance Data structure, persistant storage via AOF and HA through multi-AZ and read replicas.
	Note that DAX is build for DynamoDB not other DB engine.


*[Parquet Format](https://data-mozart.com/parquet-file-format-everything-you-need-to-know/):* It is self-describing, containing metadata, and supports schema evolution
![[Pasted image 20260324013131.png | 777]]

### AWS ElastiCache - Manage Caching Engines
![[Pasted image 20260407173344.png]]

![[Pasted image 20260407174154.png]]
Application first queries ElastiCache
	If data is not found (cache miss):
		Fetch from RDS
		Store result in ElastiCache
		Subsequent requests are served from cache (cache hit)

*ElastiCache for Redis vs ElastiCache for Memcached*
![[Pasted image 20260407174719.png | 888]]
+ *Redis* -> for *Complex Application with Advanced feature* (set, lists, Pub/Sub)
+ *Memcached* -> simple, *multi-threaded, high-performance caching system.*
	[so sánh Redis vs Memcaches](https://viblo.asia/p/memcached-vs-redis-ORNZqb93l0n)

### AWS RDS
+ ? RDS (Relational Db Service) is a *managed database service* for differnt Database Engines. Manage Database Provisioning and Scaling, Backups and Recovery, Failure detection along with Monitoring and Insight Analysis. Support many database application like PostgreSQL, AWS Aurora, MariaDB, MySQL, etc...
	Note that S3 is a Storage service like Harddisk and SSD, not the Database itself.

**Read Replica** sp up to 15 Read Rpk (Replika)
*Use Case -> Read Rpk promote to DB in failover, reduce workload on primay DB.*
During Failover, the *Read Replica can be promoted to a standablone database within current AZ* Useful for HA & Disaster Recovery.  ![[Pasted image 20260323224307.png]]

When there're too much workload in a Database. You could create a Read replica db to only run BI/reporting for appplication server or Run the addition read-heavy workload on the replica -> *RDS Read replica is Scalable* (read only)
![[Pasted image 20260323224425.png]]

*RDS Multi AZ (Disaster Recovery)* sync replica - Data is immediately replicated to the standby instance. Help with HA bc this auto failover to standby in case of: AZ, Network and Instance or Storage failure.
![[Pasted image 20260323224648.png | 555]]

Red mean Take Cost. ie. Send Data Across Region DB and DB between EC2.
-> Database Replica is free within Region. Take cost across region.
![[Pasted image 20260323202541.png]]

Amazon RDS can upgrade *From Single-AZ to Multi-AZ with No Downtime*
![[Pasted image 20260323202911.png]]
*RDS Backups type:*
	Auto-Backup: every N minutes, Daily, Point In Time Recovery (PITR)
	Or Manually create Snap-Shot.
	Note: Retention period mean retention to recover at instanetly at Point-In-Time.


### Amazon Aurora (Relational Database) & RDS
+ $ Serverless Relational Database built for Disaster Recovery (cost ~20% more than RDS)
![[Pasted image 20260323204036.png]]
Compatible with MySQL and PostgreSQL.
Cost: *~20% More than RDS*
Each Aurora (Arr) instance have 6 copies across 3 AZ. Storage is distributed across hundreds of volumns.
-> Built in HA. Fast / Near-instant Failover.
![[Pasted image 20260323204134.png]]
*Only the Master storage responsible for Write*. Every other DB for read, replication, self-healing and auto-expanding.
-> *Fault-tolerant storage* system that replicates data across 3 Availability Zones.


Auto-Scale
Shared Storage Volumn
Is Serverless
![[Pasted image 20260323204242.png]]
-> Cost effective for Low/Intermittent workloads.
Aurora Global architecture - 1 Primary Region (read/write) and 5 secondary region (read-only). Each 2ndary supports up to 16 read replica.
	is low latency.
AuroraDB built for Disaster Recovery (having Replica across regions) with Simple setup. *RTO (Recovery Time Object) < 1 minutes.*

*Aurora Backups* always enable. retention period 1 to 35 days (Within this retention windows support PITR (Point In Time Recovery)). Compare to RDS:
![[Pasted image 20260323205129.png]]
Aurora Snapshot always create new DB Snapshot.

*Copy-on-Write* prototal allow to *clone Database instantly.* This work bc there no additional Data is being copied but rather *clone points to the same pages as the source.*
-> This strategy only save new data as the Cloned data, the original data still being accessed through A database.
	Aurora shares the same underlying storage volume between the source and the new clone, *only copying individual data blocks (pages) when they are updated.*
	+ Cost only inccur for new data after the copy Point-Of-Time.
![[Pasted image 20260323205958.png]]


*AWS Solutions for Decoupling (1 break, other keep working)* - all 3 methods can be combine base on your needs.
![[Pasted image 20260323232942.png | 777]]


### AWS SQS - Allow you to *Preserve Message* within a Queue *until it is processed and explicitly deleted (timeout)* -> Resilience
Help decouple application layer (distribute), so if 1 components fail then the messages is still safely save within the Queue.
	[SQS Blog and Practice](https://blog.vietnamlab.vn/he-thong-cua-ban-se-toang-nhu-the-nao-neu-khong-co-queue/)
![[Pasted image 20260323231922.png]]
A **queue** is a data structure that holds messages waiting to be processed
![[Pasted image 20260323231947.png]]
1. Producer (Component 1) send mess A to a queue. , and the message is distributed across the Amazon SQS servers redundantly (stored persisted until the Receiver delete it)
2. When a Receiver (Component 2) is ready to process messages, it consumes messages from the queue, and message A is returned. While message A is being processed, it remains in the queue and isn't returned to subsequent receive requests for the duration of the [visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html).
3. The Receiver (Component 2) *deletes message A from the queue to prevent the message from being received and processed again* when the visibility timeout expires.
![[Pasted image 20260323232600.png]]
This is the Standard Queue where *Receiver/Consumer Messages* can run on EC2 instances, Servers or Lambda (as long as its a REQUEST) - Yes, SQS run on API
![[Pasted image 20260323235115.png]]
*Message Lifecycle*
- retention time from 4 to 14 days. *Remains in the queue until a consumer deletes it.* Hold message up to 256kb.
+ if a *mess fail* to process then SQS can move them to *Dead Letter Queue (DLQ)* for later inspection rather than letting it block the entire system.

*SQS flow example:*
1. *Poll SQS for messages:* Poll receive up to 10 mess per request
2. *Process the messages:* Example: store data in RDS, trigger workflows, etc.
	If there are multiple Consumer, after a consumer pull the message, the message will temporary become invisible (about 30s, can be edit) to prevents multiple consumers from processing the same task simultaneously.
3. *Delete the messages:* Use DeleteMessage API after successful processing to prevent *processing duplication.*
![[Pasted image 20260323235436.png]]

*Veticle-Scaling for SQS: Multiple EC2 Instances Consumers*
	Data within Queue could be processed in Parallel for multiple EC2 instances.
![[Pasted image 20260323233736.png]]
SQS Keys Benefit are:
+ Elasticity with Auto-Scaling (add more worker instances based on the number of message in the queue)
+ Fault Tolerant
	- if a *mess fail* to process then SQS can move them to *Dead Letter Queue (DLQ)* for later inspection rather than letting it block the entire system.
	- if the servers go down, the message sit safely in queue.
+ You Pay for what you Used.

*Dynamic SQS Queue with Auto Scaling Group* - You set a observer (Cloud Watch - CW) to detect a threshold (CW Alarm - CWA), if number of Queues exceed that threshold then scale-up else in-reverse scale-down.
![[Pasted image 20260324000345.png]]
1. *Amazon CloudWatch* tracks the `ApproximateNumberOfMessagesVisible` metric from the **SQS Queue**. This represents the "backlog" or queue length.
2. *Alarm Trigger* trigger if pass a threshold (e.g. >= 100 message in queue) Then active 'ALARM' state.
3. *Auto Scaling Group (ASG) Action* if the alarm get send to the ASG, the ASG will executes a scaling policy to 'add' or 'remove' EC2 Instances -> So that how Auto-Scaling work behind the hood.
4. *Processing*, the current and new EC2 instances immediately begin to *Poll for messages* from the SQS queue.

**Key Metric: Backlog Per Instance**
![[Pasted image 20260324001041.png]]
-> *Provides a more accurate picture of "load".* For example, 1,000 messages might be fine for 50 instances, but a major problem for only 2.
**Detail Visualization:**
![[Pasted image 20260323235804.png]]

Example for **Amazon SQS** acts as a "buffer" to decouple a **Front-end web app** from a **Back-end processing application**. So how Decoupling Architecture (kiến trúc tách rời) work here:
+ *Asynchronous Comminitation:* FE receive and immediately send user request without knowing if the backend is busy or not.
+ *Independent Scaling:* FE and BE scale independetly because their input request stack up differently (FE process immediately while BE take more time to process -> mostly only BE need to be scale bc of the message in SQS queue).
+ *Spike Traffic Handling* because the FE dump all the request immediately into the SQS. Even if the BE coudn't follow up, the message still stay safe in queue and will be processes after a T period of time
	-> that why some user have to wait for the page to load
	-> save the website from crashing even when there're too much traffic.
	-> Could be use to create fast website illusion (e.g the FE send the user an instant "Order Receive" without worrying the BE from missing the order msg request)
![[Pasted image 20260324001405.png | 777]]

*SQS Security* - use IAM (use NotebookLM to differentiate each service Security, also ask why is this matter)
![[Pasted image 20260324003552.png]]

*Message Visibility Timeout Cycle* - if a message not deleted within the timeout. If becomes visible again in the queue so another Comsumer can process it again.
![[Pasted image 20260324003708.png]]

*Long Pooling* - *wait message to arrived, if too long timeout.*
The Consumer wait for a period of time for "Message to arrive or Timeout end" instead of returning an Empty Respond right always -> That how timeout work.
	*Empty Respond example:* user press 'Check Connection on EC2 server, wait for 20s, if there are no return respond (ie. end of timeout) then return empty
![[Pasted image 20260324003740.png]]
-> *Dynamic SQS Queue* + Long Pooling -> Improve Resilience for multiple EC2/services.

### AWS SNS (Pub/Sub model) - Send a message to “many” receivers
Used to send one message to multiple receivers (fan-out pattern), like a Paper Publisher.
	Note: 1 Model have multiple pattern (like design core philopsophy), *Fan-out pattern is an implementation of Pub/Sub model.*
![[Pasted image 20260324004246.png]]
*Pub/Sub Message* - Basically calling Multiple Function at once. Or the Authors sending News to all Subcribers at once.
![[Pasted image 20260324004458.png]]

![[Pasted image 20260324004727.png]]

*Security* - integrate with IAM for secure access.
![[Pasted image 20260324004756.png]]

*Use Case:*
+ For alert teams of new tasks.
+ **Event-Driven Architecture:** Triggering subsequent actions (e.g., triggering a Lambda function when a new file is uploaded to S3).
+ **Media Processing:** A single "Image Uploaded" event triggers parallel tasks for generating thumbnails, performing image recognition, and storing metadata.
+ In Continual Learning AI inference, "data send" task trigger the model to learn right alway, and get send back to the dataset for replay, and also trigger analytic function to update the Dashboard.

### SNS + SQS Fan Out Architecture -> Resilience & Scalable
+ $ Allow you to *Scale AWS SQS* model
+ ? Imagine you have Multiple Service (BI, ML, Monitoring, etc..) and want to *scale each service differently* while being resilience.
*SNS + SQS Fan Out Architecture* send 1 message fom SNS to multiple SQS queues (subcribers)
-> Fully Decoupling architecture where each SQS queue receive a copy of the main message.
-> Very Scalable bc this is One-to-Many.
![[Pasted image 20260324005013.png]]
1) **Publisher:** A producer service (like an Order API) sends one message to an **SNS Topic**.

2)  **SNS (The Broadcaster):** SNS acts as the central hub. It immediately "fans out" or copies that message to every SQS queue subscribed to it.

3) **SQS (The Buffers):** Each downstream service has its own dedicated SQS queue. These queues store the message until the service is ready to process it.

4) **Consumers:** Independent workers (like AWS Lambda or EC2 instances) pull messages from their respective queues and perform specific tasks

![[Pasted image 20260324005338.png]]
**Benefits:** Parallel processing, Decoupling architecture so the system is more resilient if some service go down bc each task have its own SQS queue..

### SNS FIFO - Ensure strict Event's Order & Executed Exactly One -> Consistency
**SNS FIFO** - a messaging service designed for applications where the **order of events is critical** and **duplicates cannot be tolerated**.
+ **Exactly-Once Processing:** It prevents a message from being delivered or processed more than once and In the *Exact Order.*
+ ! Limite Throughput due to sequential in order.
![[Pasted image 20260324005811.png]]
*Use Case:*
+ *Bank Transaction* where everything have to be in order. No more No less.
+ *Inventory Update* making sure item update correctly.
+ *Log* - make sure log are save only 1 at a specific point of time.

### SNS FIFO + SQS FIFO Fan Out -> Strict Order, Distributed, Decoupling, Resilient
*SNS FIFO & SQS FIFO Fan Out* like above but now with FIFO ordering. Where 1 *Message get send and distributed exactly 1* from SNS FIFO Topic -> This making sure *Big Request don't get repeated and waste resource.*
-> Very Intuitive, because you want the Main Order to be Distributed to other service exactly One (strict order), while multiple services receive the order and execute idenpendetly to accomplish different task like BI, Training ML/DL model, Archiving, etc..
![[Pasted image 20260324010643.png]]

### Kinesis Data Streams - Real-time Streaming & Analytics
![[Pasted image 20260324011222.png]]
+ Data Retention last 1 to 365 days.
+ Support Data Replay (reprocessing)
+ Data cannot be delete manually (Expired after retention period )
+ *Immutability:* Once data is inserted into Kinesis Data Streams, it cannot be deleted, ensuring data integrity.
+ *Partition Keys:* *Same partition key's msg are directed to the same shard*, providing key-based ordering for data.
+ *Shard* is a throughput unit and *uniquely identified* (through partition key) sequence of data within a data stream. Where each shards (throughput unit) provideds a fixed amount of read and write capacity.
	*AWS allow you to scale shard flexibly*: To increase throughput, you can increase the number of shards (split a shard); to decrease capacity and cost, you can reduce the number of shards (merge shards).

*Core Architecture* Kinesis Data Streams is built on a distributed architecture that ensures high availability and durability by replicating data across three Availability Zones (AZs)

*Each Shards hold up to 1 MB/s (or 1,000 records/s)* for writes and 2 MB/s for reads. Shard can be scale manually (Provisioned) or automatically (On-Demand).
![[Pasted image 20260324011912.png]]

**Enhanced Fan-Out** - distribute workload to multiple EC2 instances.
+ Each consumer receives two megabytes per second of data per shard.
+ Low latency (70 milisecond) & Scalability.
+ Support KCL 2.0 and AWS Lambda making it versatile solution for various use cases.
![[Pasted image 20260324011606.png]]
**Use Case:** High-throughput, *real-time data* that needs to be *"replayed" or analyzed by multiple apps simultaneously.*
![[Pasted image 20260324020731.png]]

### Amazon Data Firehose - Zero-Administration Data Loading (ETL).
Scenario: receive data from AWS Kinesis and automatically loads it into **Amazon S3** or **Redshift**. It "pours" the stream into a storage bucket for *Data Replay and Analytics* with *almost no configuration.*
	Note: Could Preprocess data using Lambda to transform raw data before delivering it to the destination.
![[Pasted image 20260324021853.png]]

| **Feature**     | **SQS**            | **SNS**        | **Kinesis**           | **Firehose**      |
| --------------- | ------------------ | -------------- | --------------------- | ----------------- |
| **Model**       | Pull (Polling)     | Push (Pub/Sub) | Pull/Push (Streaming) | Push (Delivery)   |
| **Recipients**  | 1 Consumer         | Many (Fan-out) | Many (Shards)         | 1 Destination     |
| **Persistence** | Up to 14 days      | No (Immediate) | 24h to 365 days       | No (Transit only) |
| **Main Use**    | Decoupling Workers | Sending Alerts | Real-time Analytics   | Loading Data (S3) |
| **Scaling**     | Automatic          | Automatic      | Manual (Shards)*      | Automatic         |

*Use Case:*
![[Pasted image 20260324021546.png]]

*Kinesis vs FireHose*
![[Pasted image 20260324021916.png]]


![[Pasted image 20260324021943.png]]

*Write Down Note Compare SQS vs SNS vs Kinesis vs Firehose:*


### Disaster Recovery (note detail later with Slides)
*Scenario:*
	On-premise → On-premise -> Traditional DR (high cost, complex)
	On-premise → AWS Cloud -> Hybrid recovery approach AWS
	Region A → AWS Region B -> Cloud-native disaster recover

*Recovery Metrics* - Tradeoff between *Amount Recover Data and Downtime.* Low Metrics (Better) mean more Complexity and Cost.
- **[Recovery time objective (RTO)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html):** The *maximum acceptable delay* between the interruption of service and restoration of service -> This determines an acceptable length of time for service downtime.
	Fast Back-Online mean less data Recovery.
- **[Recovery point objective (RPO)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html):** The *maximum acceptable amount of time* since the last data recovery point (ie. checkpoint) -> This determines what is considered an acceptable loss of data.
![[Pasted image 20260324174421.png]]


**DR strategies - Tradeoff between Cost and "Data & Recovery Speed" (RTO/RPO)**
Of course you need Multi-AZ and Multi-Region but how much ? what is the right Threshold for your company.
![[Pasted image 20260324174636.png]]

#### [Amazone Backup](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/) - [DR Blogs](https://blog.cloudmentor.pro/blog/aws/disaster-recovery-strategies-on-aws)
**Backup and Restore** - Mult-AZ and Multi-Region backup -> High RPO but *least Efficient RTO.*
![[Pasted image 20260324175945.png]]


**Pilot light -** Only keep Active and *save the most Important Services (Primary Database, EC2, etc..)* (imagine what you save if your house on fire). Least Budget for for Full Recovery (but might having the most downtime)
![[Pasted image 20260324175353.png]]


**Warm Standby** - like Pilot Light, but instead of shutdown all services it keep *Minimum Effort for each service.*
![[Pasted image 20260324175530.png]]


**Multi-site Active/Active** - Runs full production workloads across two or more regions like nothing happened.
![[Pasted image 20260324175911.png]]

---
## Lesson 5 - AWS Networking & Delivery
+ @ **Goals:** Set up the best network for your Enterprise
[Quiz](https://docs.google.com/forms/d/e/1FAIpQLSc8K0MHiVh5T5yz3v6-M5c-Ed6U60Qo-MPBTJbiCuORLSkLGA/viewform)
![[Pasted image 20260326203651.png | 888]]
VPC (Virtual Private Cloud) is a logically isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define.
+ *IP Address Range:* Define the boundary of our data center.
+ *The Internal Connection:* In our private space, we set the rule for server work. We don’t want they talking together.
+ *Gateway/Access:* Our server is 100% isolated from the public internet, we need open the door for customer access.

+ Question: We’re moving company’s servers to the cloud. And we want it as our *own private data center*. What are exactly we want ?

### Private Network in AWS
What the point of **Addressing with CIDR – Bit counting** -> Foundational for designing a secure, scalable, and organized cloud network.
![[Pasted image 20260326204324.png | 555]]
Primary point of using CIDR and subnet masks in AWS:
1. *Network Segmentation and Organization:* divide a large VPC network into smaller, manageable chunks called **subnets**
2. *Efficient IP Address Management:* Because IPv4 addresses are limited, CIDR allows for variable-length subnet masking (VLSM), meaning you only allocate the number of IP addresses necessary, reducing waste.
3. *Security and Traffic Control:* CIDR blocks are fundamental to securing your network.
4. *Routing and Connectivity:* Subnet masks determine where a packet should go
![[Pasted image 20260326205031.png]]
Base Address: 176.16.XX
	16 free bits.
	XX -> freebits -> can change flexibly.

8 số 1 là Broadcast address.

### Controlling Traffic Flow
![[Pasted image 20260326210340.png]]

Route Table - default route table

Đi vào: Inbound -> Internet Gate way -> VPC -> Public Subnet
Đi ra: Public Subnet -> Internet Gateway


**Nat Instance** - Instance nên nó là 1 service.
Vì Private subnet ko đi vào từ bên ngoài dc nên nó cần kết nối với NAT instance (NAT có public IP, giúp kết nối đc ra bên ngoài). Làm *trung gian giữa Public và Private subnet.*
![[Pasted image 20260326211204.png]]


![[Pasted image 20260326211631.png]]
Security Group at Instance level.
![[Pasted image 20260326211529.png | 488]]

*Inbound Rules* -> traffic from application level.
*Outbound Rules* ->

### Network Security
**Stateful vs Stateless Firewall**
![[Pasted image 20260326212203.png]]
Stateful - allow the return traffic automatically

*Network ACL* (security at subnet level - *stateless Firewall*) - *control what goes in and out of the Subnet/VPC* or used for S3 Object access control.
![[Pasted image 20260326212359.png]]


### Naming & Access: DNS
A record - route traffic to IPv4
C name - route traffic from a domain to another domain (between 2 domain)
Alias - turn on (maintain connection to IPv4)

<<<<<<< HEAD
---
## [[AWS Security and Compliance]]

![[Pasted image 20260402163224.png]]

![[Pasted image 20260402162951.png]]


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


### Key Management Service (AWS KMS), SSM
For Security and compliance
AWS KMS - can be integrated with **Amazon S3, EBS, RDS, Lambda, and SSM** to handle data encryption and decryption.
	Because *data is encrypted by key*, key enryption also mean data encryption. ![[Pasted image 20260402170917.png]]

*AWS KMS and Secret Manager are complementary* security service
+ ? Secrets Manager stores, manages, and rotates sensitive data (API keys, passwords), using KMS to encrypt this data at rest.

**AWS Secret Manager Rotate AWS KMS keys** - 3 types - Manage key have 1yr expire date, Imported key don't.
AWS *Managed Keys*
- Automatic rotation *every 1 year*
Customer *Managed Keys*
+ Optional → must enable manually
+ Then rotates *every 1 year*
![[Pasted image 20260402191338.png]]

*Imported* Keys
+ *No automatic rotation*
+ Must rotate manually (typically using aliases)
![[Pasted image 20260402191324.png]]



**Server-side Encryption at Rest**
AWS KMS offer encryption AT REST for S3- "At rest" in refers to ==securing data that is actively stored on persistent storage devices (like disks, SSDs, or S3 buckets) rather than data currently moving over a network==
![[Pasted image 20260402173350.png]]

**Client-side Encryption**
![[Pasted image 20260402173412.png]]

KMS can have **Multi-Region Keys** -> You just have to create the Primary keys the replica across region.
![[Pasted image 20260402173936.png | 666]]

**AMI Sharing Process Encrypted via KMS**
![[Pasted image 20260402184728.png]]

```
Account A wants to share an Amazon Machine Image (AMI) backed by an encrypted EBS volume with Account B. Which combination of actions is strictly REQUIRED for Account B to successfully launch an EC2 instance from this shared AMI?

Only share the underlying KMS key with Account B, because the AMI is inherently linked to it.
Copy the AMI to an S3 bucket and grant Account B cross-account access to the bucket.
**Share the AMI launch permissions with Account B AND share the underlying KMS key with Account B.**
Make the AMI public and temporarily disable KMS encryption during the launch process.

Explain: you must modify the image attribute to add a Launch Permission to the target AWS account (ie. Account B)



In an AWS Organization, a Service Control Policy (SCP) is applied to an Organizational Unit (OU). The SCP explicitly allows access to Amazon S3. However, an IAM user within a member account of that OU receives an 'Access Denied' error when trying to upload a file to S3. What is the most likely reason?

SCPs only monitor billing limits and do not actually affect resource access.
The IAM user does not have an IAM policy attached that explicitly grants them S3 permissions.
The master account must perform an S3 action first to activate the SCP for the member accounts.
The SCP must be applied directly to the IAM user instead of the Organizational Unit.

Explain: SCP define the HIGHEST permission for the IAM user not Granting IAM permission to the user.



Both AWS Secrets Manager and AWS Systems Manager (SSM) Parameter Store can be used to securely store database credentials. What is a key capability unique to AWS Secrets Manager that justifies its higher cost ?

It uses a hierarchical path structure to organize configuration data.
It natively supports automatic rotation of secrets on a schedule using a Lambda function.
It provides free public TLS/SSL certificates for your applications.
It is the only service that integrates with AWS KMS for encryption at rest.

Explain: SSM only store credentials in folder hiarchy (free) while AWS Secrets Manager supports automatic secret rotation via Lambda function (0.4$/month)



```

### AWS Certificate Manager (ACM)
Integrations with (load TLS certificates on)
+ Elastic Load Balancers (CLB, ALB, NLB)
+ CloudFront Distributions
+ APIs on API Gateway
+ ! Cannot use ACM with EC2 (can’t be extracted)
![[Pasted image 20260402164526.png | 677]]
cerificate ~ token ~  encryption keys
+ ? Allow generate encryption keys that can be used to encrypt data

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

+ ? Note: AWS CloudWatch used for *monitoring resources like AWS infrastructure hardware usage (CPU, GPU, Disk, etc..)* and *automated actions based on predefined rules.*  Monitor Cost and Billing as well.


**Access Control Lists (ACLs)** - *manage access to resources (buckets and object/file)* at different levels, such as Amazon *S3 buckets* or *Virtual Private Cloud (VPC) subnets*. Offer fine-grained control - [what is AWS ACL - Search](https://www.bing.com/search?pglt=417&q=what+is+AWS+ACL&cvid=901bf0cd948343409ca93b6b219a83f9&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgcICBDrBxhA0gEIMzc3MGowajGoAgiwAgE&FORM=ANNTA1&PC=U531)
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

*VPC Flow Logs* - captures information about *IP traffic going to and from network interfaces in a VPC* (Virtual Private Cloud)
-> for monitoring, Logs output to CloudWatch, S3 or Data Firehose. ![[Pasted image 20260409130554.png | 777]]
+ ? Logs from *Flow Logs* reached *CloudWatch* which can be used to trigger "alarm -> action" for EC2 auto scaling



**AWS Inspector (identifying risks/vulnability scanner):** *scans EC2/ECR instances*, containers, and Lambda functions for software flaws -> *Scanning resource for vulnability and misconfiguration* like Outdated software, misconfiguration, missing patches or exposed network ports (also support DevOps pipeline).
+ ? Monitor real-time Vulnability in *Software* and unintended network setup *(network exposure)*.
![[Pasted image 20260402175846.png]]


**AWS Inspector vs GuardDuty** in short while:
+ Inspector is resource-focused by *scan for vulnerability from inside.*
+ GuardDuty is activity-focused by *detecting threat from outside.*

	**AWS Macie is serverless** use *ML and Pattern Matching to auto Discover, Classify and Protect Sensitive data* (like PII e.g. name, email, IDs financial data and credentials) stored in *AWS S3 buckets.* S3 Protection focus. *Regional Level* ![[Pasted image 20260402180128.png]]

### AWS Well-Architected Framework (6 pillars)
==Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability==,


### AWS Trusted Advisor vs Inspector vs Cloud Watch vs CloudTrail
AWS Trusted Advisor - give advises base on action records.
+ ? identifies ways to improve your AWS infrastructure across 5 unique pillars: *Security, Performance, Cost Optimization, Fault Tolerance, and AWS Service Quotas.*

**AWS CloudTrail vs CloudWatch**
+ Cloud Watch - *monitoring resources like AWS infrastructure hardware usage (CPU, GPU, Disk, etc..)* and *automated actions based on predefined rules*. - [source](https://cloudchipr.com/blog/aws-cloudwatch)
	![[Pasted image 20260409122933.png]]
	Example: Monitor bandwidth utilization, performance, and the traffic parameters of your app. ![[Pasted image 20260407181212.png]]

+ CloudTrail - are *records of API activity and management events* hence the word *Trail/Evidence*, providing detailed information about who, what, and when actions were performed.  ![[Pasted image 20260407184327.png]]
	+ ? *Monitor account activity* include user actions in the AWS Management Console, AWS SDKs, command-line tools, and other AWS services
	Example: identify the hacker/attacker with the help of historical CloudTrail data Logs.

+ [Practice CloudTrail & CloudWatch Integration](https://www.opsramp.com/guides/aws-monitoring-tool/cloudtrail-vs-cloudwatch/) ![[Pasted image 20260407181315.png]]

## AWS Pricing & Billing (of Network + Storage + Compute)
**Common Cost Breakdown:**
1. Compute
2. Manage Services
3. Storage
4. Network Traffic & Data Transfer
5. Mics (other cost)

**Compute Cost:** Instance Type $\times$ Instance Amount $\times$ Runtime
+ ? Cost Scale Up Linearly so be extra careful if renting multiple Hardware. ![[Pasted image 20260407151053.png]]

**Storage Cost:** Data Amount $\times$ Frequency of Access $\times$ Performance
	Frequency of Access: 	![[Pasted image 20260407151132.png]]
**4 Cost Drivers:**
+ *Storage Volumn -* the more data you stored the higher the cost - [more on S3 Overall Storage Cost](https://zesty.co/blog/the-ultimate-guide-to-s3-costs/)
	-> Use S3 Storage Tiers/Types to reduces Storage cost like S3 Glacier Deep Archive for rarely used data, S3 Standard for frequent used data, Intelligent-Tiering (auto move data between tier), Standard-IA (infrequent) and One Zone-IA for low-cost infrequent.

+ *Request Volumn (PUT/GET) -*  Every API calls taken to manage or access data in S3 incurs a small "micro-charge".
	+ ? `PUT`, `COPY`, `POST`, or `LIST` requests (uploading/managing) are more expensive than `GET` requests (retrieving data)

+ *Transfer OUT (Outbound Data) -* charge for moving data in AWS env to the Internet. While Inbound data is free in AWS and data transfer within 1 Region (e.g. from S3 to EC2 in the same AZ) is generally Free, moving data across-region cost a lot.

+ *Transitions (Lifecycle) -*  Data Storage Tier based on data Access Frequency to SAVE COST. ![[Pasted image 20260407151804.png]] Lower-cost tier like Glacier offer super low storage cost for infrequent access data.

Example of AWS Cloud Billing across layers.
![[Pasted image 20260407150302.png]]
+ ! **Invisible cost** are what made Bills so high: *storage nobody cleaned up, data transfer nobody modeled, DynamoDB tables nobody turned off.*

AWS Budget (Proactive Control) -  Đặt ngưỡng ngân sách và t*ự động dừng dịch vụ (e.g. EC2)*, cảnh báo *khi vượt ngưỡng*.
+ ? *Action-Enable budget* (a budget that automatically takes predefined actions to control costs or usage when a threshold is exceeded)

**How Action-Enable Budget it work**
1. Select a type of Service (e.g. EC2, RDS) as your action type.
2. Execution - set the action to run automatically or manually (in CLI) as soon as the threshold is reached.
	Note that the First 2 Action-Enable Budget (ie. service auto-stop) are free, after that you have to pay $0.10 per day.
3. [Practice Budget Alert](https://kubex.ai/finops/aws-budgets-vs-cost-explorer/#:~:text=Both%20tools%20are%20free%20for%20basic%20use,reports%2C%20while%20Cost%20Explorer%20charges%20for%20API)

**Exceed Budget Auto-Stop Use Case**
*Cost Explorer (Analysis)* - phân tích chi phí theo dịch vụ, tài khoản, thẻ/tag và khoảng thgian (ngày/tháng/custom range) + Visualization các chi phis dịch vụ trong Lịch sử (xu hướng chi phí vào services nào, filter/group by, time range) -> **analyzing historical usage**

*AWS Pricing Calculator* - Setup EC2/Storage/Network then calculate the **expected cost (hypothesis/predicted cost).**
Migration Evaluator - retrieve on-premises workload from hardwares (CPU, RAM, IO, utilization) -> right-size workload when migrate to AWS.
	Compare on-prem vs AWS cost - evaluate migration cost.

*AWS Global accelerator* - Improve performance by up to 60% by *routing user traffic through the AWS global network backbone* rather than the public internet - [source](https://cloudonaut.io/review-aws-global-accelerator-latency-multi-region-disaster-recovery/) ![[Pasted image 20260409124441.png | 777]]
**AWS Migration Hub**
*AWS Total Cost of Ownership (TCO)* Calculator ==allows organizations to estimate cost savings by comparing on-premises infrastructure to AWS services==.
Note: value proposition mean your advantage againt your competitor.

First AWS Principle is Pay-as-you-go -> This model gather customers but Revenue is Unpredictable and volatile.
+ ? To Retain long-term customer, AWS offer higher discount the longer you used their services.    ![[Pasted image 20260407153435.png | 666]]


### AWS Pricing Model
**VPC Peering** (network connection between 2 VPC,  simple setup with *VPC < 5 connection setup*) -> Allow *No-COST Data Transfer between Region* by routing traffic to eachother using private IP address.
	Meshed network topology (vpcp)
![[Pasted image 20260407160336.png | 888]]

 **AWS Transit Gateway:**  Distribute data flow between VPC (Complex setup with *Multiple VPC > 5*)
 + ? It eliminates the need for complex VPC peering, *routing traffic between thousands* of VPCs, VPNs, and Direct Connect connections using *centralized* route tables. *Not Free*
	 Star topology
![[Pasted image 20260407160754.png]]

**AWS Direct Connect gateway** (globally available) - *connect on-premises networks to multiple Amazon VPCs across different AWS regions* using private virtual interfaces (VIFs). Data Transfer across Region take up a lot of cost.
![[Pasted image 20260407162859.png | 888]]
*Tips for planning architecture:*
+ Use VPC endpoints to avoid internet transfer
+ Gateway endpoints: free S3/DynamoDB same
+ Region Interface endpoints cost hourly and data transfer
+ Minimize cross-AZ and cross-Region traffic
+ Use tools: Free Tier, Calculator, dashboards

### Billing System & Cost Monitoring
Cost Allocation Tags -> Tag which service used for Billing. So admin can see where "this" cost come from.
![[Pasted image 20260407163248.png]]
+ $ Allow tracking cost across Teams (e.g. dev team, test team), Label, identifying and categorizing cost in different areas -> Help Tracking costs and managing resources. ![[Pasted image 20260407163632.png | 455]]


**How AWS Budget work ?**
![[Pasted image 20260407164756.png]]
*AWS Athena -* act like a Filter for Dashboard in AWS QuickSight.
*Data Collection Account -*
+ ? Read cost specified organized by Tag in AWS Budget  then save it to AWS S3 Bucket for Centralize Monitor and Inspection.
+ $ Used the Read Role Permission from AWS Organization.

**AWS Budget Usage Example**
![[Pasted image 20260407164228.png]]

AWS Anomaly Detection -> run script on Lambda, help to detect anomaly like DDOS.
![[Pasted image 20260407164313.png]]
Rate Limiting AWS step func -> limit IP that access too much to prevent DDOS.

### [Lab Session](https://zoom.us/rec/play/6hYqLGNN7Pin90ccDHdzwYKW7X6bSDZoDolPHBEwsQBGd7nY1dcv7DCJIEKHl19cvLdG7w-nif5NOKZ-.7D_lWernqB-I9miS?eagerLoadZvaPages=&accessLevel=meeting&hasValidToken=false&canPlayFromShare=true&from=share_recording_detail&continueMode=true&oldStyle=true&componentName=rec-play&originRequestUrl=https://zoom.us/rec/share/VI7U1wf1S5om16eIFLdlrbyOGWLJOyYppeEd4INKns9h8OMP50ClWnKsauB9enZk.0QhjY029W_0aTcmo)
Pillars of the AWS Well-Architected  -> Security & Performance.
*AWS Trusted Advisor* -> AWS service to identifies security groups that allow unrestricted access to a user's AWS resources.
+ ? Inspects your AWS environment and provides actionable recommendations to follow best practices.
+ $ Advisor Help checks and optimize the these categories:
	*Cost Optimization (Identitfy under-ultilize resource)* - unsed assesst (like rent but not use S3)
	*Security (Evaluate)* - security gaps
	*Performance (Monitor resource usage)* - scan for performance Bottleneck
	*Fault Tolerant (Detects gaps in configuration to ensure resillient)*
	*Service Quota (Monitors)* - Monitors your usage of AWS services against regional limits. e.g. Flags usage over 80% EC2 usage
-> like a Scan and Recommended system.

Fault Tolerant - ability for the system to keep running in case of 1 or more components fail e.g. EC2.

When design Cloud Architecture -> Elasticity (adaptibility) is the principle architecture
-> Allow pay-as-you-go and HA.

Extend Local to Cloud -> Storage Gateway and Direct Connect.
AWS system Manager -> Allow auto security version patching
Mechanism allow dev to *access AWS service from Application Code* -> SDK (Library that connect through API)
S3 - store Object

*AWS Partner Network* - community of over 100,000 technology and *consulting firms* that leverage AWS to build, market, and sell customer solutions. *AWS Services Distributioner*.
AWS Professional Services - Service from AWS.

AWS Connect - offer *custom-built AI customer service for Company* at a lower cost on Cloud.
AWS Enterprise Support - have a exclucise Concierge team (lễ tân)

---
## What Next
![[Pasted image 20260420132113.png]]
