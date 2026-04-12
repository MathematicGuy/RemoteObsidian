**AWS Review Rule - Do not SPAM MCQ**. Review exact AWS domains/chapter that I faild to correct. Review what I haven't understand correctly.
![[Pasted image 20260314233913.png]]
-> A is correct before AWS global infrastructure help reduce data transfer cost and data latency.(through Proximity/Cache).

![[Pasted image 20260314234045.png]]
-> B is Correct - because CloudFront Edge Location is deployed globally.  

![[Pasted image 20260314234102.png]]
-> C  because Pay-as-you-GO is the Opposite of Up-Front 

![[Pasted image 20260314235857.png]]
-> A Correct - IAM is global. 

![[Pasted image 20260315000238.png]]
-> D is correct bc S3 automatically replicates your objects across a minimum of **three physically separated Availability Zones (AZs)** within an Region. Bc S3 is multi-SZ redundancy, it provide 99.999999999% (11 nines) of durability. 

----
*Strict Regulatory Compliance* and DB must run on *isolated hardware* -> Dedicated Host. Low Latency -> io2. Save Money up to 3-year -> Reserve Instance.  
![[Pasted image 20260322143106.png]]

## Canary Deployment
Basically, move user from Stable Version to the New Verion little by little in a incremental way. e.g. 90% stable / 10% new -> 80% stable / 20% new -> and so on. 
![[Pasted image 20260322223216.png | 300]]

---

### AWS Security and Networking

**CIDR notation (e.g. 10.0.0.0/16)** - address
+ 10.0.0.0 - is like the street address of your Apartment complex. Technically, its the **Base Address,** the possible IP address in your range. 
+ `/16` is the  capacity in Classless Inter-Domain Routing notation (CIDR), its define the size of your network. Like how many "apartments" (IP Address can fit inside your compex). If an IPv4 have 32bits, the number of bits behind the slash `/` tell you how many address are "free" for your devices. `2^16 = 65,535 (bits)` for 64,535 unique IP addresses for your EC2 instances, Load Balancers and Gateways (basically IP for your AWS service) 


**Subnet** - private & public
![[Pasted image 20260327155658.png]]
Note:
+ Bastion host is a EC2 placed i a public subnet as a secure gateway for accessing private instances (Single point of ingress from the internet). 
	Wait this kind of like NAT gateway. Well, *NAT is outbound from your instance. Bastion is inbound to your instance.*

*Inbound connection* mean Public to Private. *Everything going out but nothing coming in.*
*Outbound connection* mean Private to Public. *Can only be Access Into, cannot connect from the Inside to Outside*

### NAT Gateway (Outbound) vs Bastion Host (Inbound) - (Presentation - Example Quiz Use Case - Interacting with Viewer)
![[Pasted image 20260327173003.png | 777]]
**Theme:** Private Subnet Instances with *Bastion Host and NAT Gateway to enable internet access from inside*.

When we're talking about NAT and Bastion, we're talking about access between Public and Private subnet. 
![[Pasted image 20260327164738.png | 666]]
*Bastion (Pháo Đài - Jump Boxes authentication - Inbound only)* - connect your application to your Private subnet. But control inbound entry point for administrators to SSH/RHP into private instances. *Jump Box* mean securely "jump" *via SSH or RDP into private,*
-> For Management/Administration through 1 Entry Point to Multiple Subnet. (self-healing host *min 1 max 1 desire 1 in Auto-Scaling Group* to make sure at least Bastion Host are always up if it go down)


*Why Bastion ?*
**Not every server can sit on the public internet - especially sensitive resources like production databases, app servers, or dashboards.** But engineers still need access. That’s where *bastion hosts* come in.
+ Instead of protecting 50 servers from the internet, you only need to harden and protect ONE server (the Bastion).
+ Network Isolation - maintain critical workload in private subnets (unchanging workload) and meeting compliance requirements (HIPAA, PCI-DSS).
+ Central Point for Logging access - easy to monitor. 
![[Pasted image 20260327161504.png]]
Bastion SSH Jump or Proxy Jump - allow you to Jump through multiple Authentication step
![[Pasted image 20260327162326.png | 777]]
If your Company have multiple Security layer (Bastion 1 for Company access, Bastion 2 for AI Engineer service, Bastion 3 for accountant service). Without Proxy Jump, you have to go through 3 SSH login step. Instead Proxy Jump SHH go through them in 1 command. 
![[Pasted image 20260327161722.png | 666]]
In Netflix, Bastion work with "AWS Access Control service" to direct user with specific Identity to Specific Application through SSH. Access Log will be save within AWS Logging service below. 1 Bastion
![[Pasted image 20260327161945.png]]
Note: Netflix use an Hardened Bastion Host Layer integrated with their Identity Management platform 
0.  Login with MFA - to start the Bastion Host section -> Ensure stolen SSH keys alone aren't enough go gain access. 
1. Engineer may have SSH access to the application servers but not the Payment Database -> Enforce by AWS Security Group and IAM policies -> Engineer Only see what they suppose to see.
2. Every SSH command run through the bastion is logged -> easy to monitor activity and respond quickly if any thing suspisus happend (AWS Athena to analyze data in S3).
3. Access to the Bastion is Time Bound. Session Auto-Expire -> reducing the risk if an engineer's machine is compromised (hỏng hóc).
-> However Bastion access can be revoke if want to allow freely access in case of need. And be locked again. 
+ ! If you only have one bastion host in a single AZ, and that AZ experiences an outage, you will lose access to all your private instances -> Need Multiple Bastion Host for HA and Fault Tolerance (Multi-AZ). Bastion Host is an EC2 Instance. 

*Visibility:* Public address and could be Scan, but can limited Public Access in Security Group.  
![[Pasted image 20260327165529.png]]
*Components Explain:*
*VPC (10.0.0.0/16)* 
+ 10.0.0.0/16 -> your possible IP address. 
+ VPC - Virtual Private Cloud
+ Internet Gateway (IGW) - allow VPC to connect to the outside Internet. *(Each VPC have a Unique Internet gateway, 1-1)*

*Public Subnet (10.0.1.0/24)* - buffer zone (often call DMZ) contain:
+ *Bastion Host (EC2)* - a proxy for administrators to access private servers.
+ *NAT gateway (Outbound)* - managed service that  allow instances/application (EC2) to talk to outside internet without allowing them to talk back.

*Private Subnet (invisible / no address)* - Where all of your Services lives (Database, Python Application, Web service, etc..)
Could only *access through a single monitored SSH entry point from Bastion Host (Inbound).* 
![[Pasted image 20260327173455.png | 666]]
Note: 
+ Auto-Scaling Group for Bastio Host - Self-Healing host usually use 1-1-1 setup, *min 1 max 1 desire 1 in Auto-Scaling Group* to make sure at least Bastion Host are always up if it go down.
+ Wit
*The Worklflow is as follow:* 
1. the user access (SSH client) connects to the Public IP of the active Bastion Host. 
2. IAM (identity check) - Bastion verify the admin's credential (SSH keys)
3. Internal Jump - The traffic is then "tunneled" or "forwarded" from the Bastion (using its private IP) to the **Backend Server's** private IP (10.0.2.x).
4. This way No One know the Private Subnet IP Address. Help it stay completely hidden from the Internet (you could find 1 public IP address without having access to the Private subnet, bc their IP address doens't exist)

*NAT Gateway (Outbound traffic)* - used when your app is 1-Way-Access ie. *App have access to the Internet but the Internet doesn't have access to your application.* For example, your app was deployed on Private Subnet instances and those subnet don't have a route to Internet Gateway (no internet access) 
	-> Use in Automated Service or Backend Instance. Send order from inside, receive none.  
Visibility: Invisible. Cannot be scan. 

Within a VPC, Company want initnitate connection between Private and Public Netowork -> NAT gateway bc its allow resource transit from Private subnet to the outside Internet but Prevent outside traffic/request. 
+ $ Allow Private subnet to communicate with outside Internet but prevent Request from entering private subnet. 
	Note: traffic is the amount of data within each Request. e.g. data for image, text message, etc..

----

Implement encryption in transit - which security service (understand what "in transit" mean and its relation to SSL/TLS certificates)
AWS Support Plan