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
*OPEX (On Premise):* is more eco in the long-term and offer ultimate controlled. Use when u have a strong DevOps team, fast prod experient cycle or don't need expand DC over time or Globaly.

*CAPEX (Cloud):* is more eco shorterm and userbase-flow fluctuate a lot (not stable). But more costly in long term. Allow Global connection.
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


A startup is building a new custom web application. They have a small software engineering team to write the application code and manage user data, but they do not want to spend time managing or patching the underlying operating systems, runtime environments, or server hardware. Which cloud computing model should they choose?

**A.** Infrastructure as a Service (IaaS), because it provides the team with full control over the operating system and runtime environment.
**B.** Software as a Service (SaaS), because the cloud provider will manage everything including the application and data, eliminating the need for their engineering team.
**C.** Platform as a Service (PaaS), because the provider manages the underlying infrastructure, operating system, and runtime, allowing the startup to focus solely on their application and data.
**D.** On-Premises, because it allows their software engineering team to have complete control over the physical data center.

**Explaination:** In a PaaS model, you rent the environment to run apps; the cloud provider manages the infrastructure, Operating System (OS), middleware, and runtime, leaving the customer responsible only for the Applications and Data


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