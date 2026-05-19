Main Goals:
+ [x] Control AWS User account - Least Priverledge Permission
+ [x] Avoid addition budget
- [ ] Practice - AWS Compute Cloud and Serverless (ongoing)
+ [ ] Deploy Docker Application to AWS (lastly)
- [ ] [DEPLOY Fully Private + Local AI RAG Agents](https://www.youtube.com/watch?v=bankdPmQnHU)
- [ ] [Deploy RAG to Production](https://www.youtube.com/watch?v=ldFONBo2CR0)

## Control your AWS's Bank Account
![[Pasted image 20260518162347.png]]

### Segment 1: Apply Least Priviledge Permission.
Set up MrLeast IAM User and Minimum Role for MrLeast.
![[Pasted image 20260518163104.png]] 

### Segment 2: GuardDuty + Security Hub (automatic threat detection using ML)
Log chỉ ghi lại chứ ko phát hiện đc nguy hiểm -> Cần SecurityHub & GuardDuty
+ *SecurityHub (Control Center)* - Centralize Dardboard for AWS Security Service 
  (e.g. Marcie, Inspector, GuardDuty, etc..) ![[Pasted image 20260518174824.png]]
+ *GuardDuty (The Watchdog)* - Continuously monitors your AWS environment for malicious activity, unauthorized access, and anomalies using machine learning and threat intelligence.  ![[Pasted image 20260518165919.png]]Bật GuardDuty và Security Hub - Giả vờ làm Attacker và tạo IAM Access cho user để nhận thông báo -> Xem log thông báo.  

### Segment 3: AWS Config + Trusted Advisor (compliance monitoring in real-rime)
(How to Check for Misconfiguration)
Tạo Misconfiguration để kiểm chứng hệ thống.
![[Pasted image 20260518171626.png]]
Check if any bucket have Read Permission 
![[Pasted image 20260518173608.png]]
Skip Trust Advisor bc they cost money for AWS Enterprise. 

### Segment 4: Cost Explorer + Budgets
![[Pasted image 20260518174349.png]]

Finally, Clean up.
![[Pasted image 20260518174514.png]]


## Deploying AWS Aurora Multi-AZ and Read Reploca Simulate Failover
RDS - support most of popular databases type ![[Pasted image 20260518200745.png | 255]] 
Compare RDS vs regular Database host on EC2
-> handle OS maintainance, Multi-AZ deployment for HA, Storages and auto backup.
-> Help Dev focus on writing optimization algo for DB instead of managing the DB itself.
![[Pasted image 20260518200810.png]]

**RDS vs Aurora**
	Security about the same.

*RDS (Traditional DB type)*
+ Run on EC2 instance
+ Compatible with 7 DBMS (database management server)
+ failover take more time (ie. recovery after failing)
+ Save data to S3. Manage delete or save replica manually.
+ Scalability - Must be done Manually or setup a fixed config volumn first.
+ Simple CloudWatch metrics
+ Base on usage (IOPS/Storage)

*Aurora (Serverless)*
+ ony compatible with MySQL and PostgreSQL
+ Fast Auto failover and selfhealing 
+ Cost: base on instance type, engine region and registrated storage. bc you set EC2, S3 manually 

**If MySQL is a DBMS then what is AWS Aurora do ?** 
-> think MySQL as the "engine", Aurora is the car itself, the wrapper that amplified MySQL potential like RAG and LLM.

### Demo - [RDS Aurora setup](https://www.youtube.com/watch?v=SMgem5DJR0Y&t=23s) - [EC2 Security Group setup](https://www.youtube.com/watch?v=P-BVDUL9Dx0)
![[Pasted image 20260518202841.png]]
1. Create Bastion host (Intermediate host to access internal system or VPC)
2. Create AWS Aurora
3. Connect Endpoint to Aurora Database (MySQL)
4. Connect to Bastion Host
5. Perform hand-on SQL queries through SSH
6. Simulate Failover (change backup region) to test Multi-AZ
7. Check activity after Failover
8. Clean UP (everything u just setup)

#### Setting up EC2 instances - [setup guide](https://github.com/stuart-lab/aws-setup) 
1. Log into AWS console
2. EC2 > launch instance
3. Choose a name
4. Select Ubuntu 22.04 operating system
5. Choose instance type that is the minimum required for the project
6. Select key pair, or create one
7. Allow SSH traffic from your computer IP address only
8. Select the amount of EBS storage required
9. Launch instance
10. Go to instance details > security > security groups > inbound > add rule
11. Add the following custom TCP rules: port 8787 (rstudio), port 8888 (jupyterlab)
12. Copy the IP address
13. Log in via ssh: `ssh -i <key> ubuntu@<ip>`
14. Run an OS update:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt dist-upgrade
sudo reboot
```
- Log back in once rebooted and clone your repository: `git clone repo`
- Run startup script to install dependencies: `sh aws-setup/startup.sh`
- Logout
#### Installing AWS CLI
Configure AWS User before connect to your EC2 instance through CLI Connect.
```sh
aws configure
```
To create AWS access keys, log into the AWS console and go to:
Security credentials -> Access keys -> Create new access key
Note the key ID and secret access key.

#### Additional EC2 setup Note 
**Goal: Deploy Multi AZS deployment and Load Balance**
![[Pasted image 20260519151222.png]]
Set up 2 EC2 in the same Region difference AZ - **setup 1 Security Group** make sure to *allow inbound IPv4 address from your local laptop/desktop.* 
![[Pasted image 20260519151258.png]]
Setup another Security Group for ALB 
![[Pasted image 20260519151159.png]]
![[Pasted image 20260519151333.png | 344]]



Setup EC2 and Security Group Inbound Rule (let Remote IP IN) and Outbound Rule (let Security Group IP out)
When setting up Inbound Rule: 
+ Run the following command to get your local IP address (if you unsure about your IP address):   `curl https://checkip.amazonaws.com` [[1](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html)]
+ Then authorize the ingress using your IP address with the `/32` suffix:   `aws ec2 authorize-security-group-ingress --group-id YOUR_SG_ID --protocol tcp --port 22 --cidr YOUR_IP_ADDRESS/32`
-> After Verify your Inbound IP with security group, you're free to access any servers that Security Group Protect.
![[Pasted image 20260518215039.png]]
run Linux in Window git Bash: `wsl -d AlmaLinux-9` 
Activate root linux first user `sudo -i` 
copy the `.pem` key file to `/root` from your linux folder directory in the terminal `sudo cp /home/heval111/vpc-demo.pem /root/`  
cd to folder `cd '/mnt/d/Personlich/AIO/AIO2025 - Main/AWS Cloud Partitioner'`
conncet to ec2: `ssh -i "vpc-demo.pem" ec2-user@ec2-32-236-85-61.ap-southeast-2.compute.amazonaws.com`
```bash
curl https://checkip.amazonaws.com
wsl -d AlmaLinux-9
sudo -i
cd '/mnt/d/Personlich/AIO/AIO2025 - Main/AWS Cloud Partitioner'
```
+ $ Make sure to **edit Outbound Rule so that ur EC2 could connect to the Internet** anywhere from IPv4 
![[Pasted image 20260519142804.png]]
```
ssh -i "vpc-demo.pem" ec2-user@ec2-3-107-69-50.ap-southeast-2.compute.amazonaws.com

sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
echo "Hellow from AZ3" | sudo tee /var/www/html/index.html
# Create html page and echo
echo "Hellow from AZ1" | sudo tee /var/www/html/index.html
echo "Hellow from AZ2" | sudo tee /var/www/html/index.html
# test on browser "http://32.236.85.61" 
```

#### Setup LoadBalancer & AutoScaling 
![[Pasted image 20260519160443.png]]

Create EC2 template for AC -> add UserData 
```sh
#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd.service
httpd enable httpd.service
echo Hellow from New AZ: ${hostname -f}> /var/www/html/index.html
```
![[Pasted image 20260519163954.png | 444]]
stress test
```sh
sudo yum install stress -y
sudo stress -c 4
```

- [ ] Map out what I need to do - write down the constraints
- [ ] Map aws aurora configuration into a CloudFormation file.  

```
#!/bin/bash
sudo yum update -y
sudo yum install -y httpd.x86_64
sudo systemctl start httpd.service
sudo systemctl enable httpd.service
echo "Hello from New AZ: $(hostname -f)" > /var/www/html/index.html
```

### Setup Security Group for Aurora
![[Pasted image 20260519183305.png]]
userdata
```sh
#!/bin/bash
wget https://dev.mysql.com/get/mysql80-community-release-el9-5.noarch.rpm
sudo dnf install mysql80-community-release-el9-5.noarch.rpm -y
sudo dnf repolist enabled | grep "mysql.*-community.*"
sudo dnf install mysql -y
```