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
Provision - expand network, hardware. Updating use acess (ADD)
Deprovision - removing network, hardware. User access (REMOVE)