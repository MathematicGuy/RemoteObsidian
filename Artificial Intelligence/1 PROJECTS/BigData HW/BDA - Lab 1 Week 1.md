**HDFS Shell Command**
![[Pasted image 20250218074826.png]]
![[Pasted image 20250213151222.png]]

note: rename file
```sh
mv old_name.csv new_name.csv
```

#### 2) Ambari Dashboard
![[Pasted image 20250212230210.png]]

#### 3) Root folder in HDFS
![[Pasted image 20250213210241.png]]

#### 4) Add & Delete file from HDFS
**Download .csv file via given link**
	`wget [https://raw.githubusercontent.com/minsuk-heo/BigData/master/ch06/populationbycountry19802010millions.csv](https://raw.githubusercontent.com/minsuk-heo/BigData/master/ch06/populationbycountry19802010millions.csv)`

**Move file to HDFS root folder**
![[Pasted image 20250213213510.png]]
**View HDFS Root folder**
`ls ~`
![[Pasted image 20250213213549.png]]
Delete file from HDFS Root Folder
`hdfs dfs -rm /populationbycountry19802010millions.csv`
![[Pasted image 20250213213354.png]]

#### 5) Send the same data file from the local machine (where you boot up) to HDFS root Folder
Move to Local VM root folder
	`cd ~`
Move download file in Local root to HDFS Amari Files View Root folder:
	`hdfs dfs -put /home/raj_ops/populationbycountry19802010millions.csv /`
Display root folder:
	`hdfs dfs -ls /`
![[Pasted image 20250213215028.png]]

#### 6) Access Shell via port `2222`  in the terminal and move downloaded file to HDFS root folder
Access HDFS ip via port 2222:
	`ssh root@192.168.1.60 -p 2222`
Check if downloaded file existed in HDFS root folder
	`hdfs dfs -ls /`
Create `data` folder
	`hdfs dfs -mkdir /data`
Move downloaded file in VM local root folder to HDFS root folder 
	`hdfs dfs -put home/raj_ops/populationbycountry19802010millions.csv/data`
Verify command result
	`hdfs dfs -ls /data`
![[Pasted image 20250213215928.png]]

#### 7) Reset the password of Ambari-Admin and access to Ambari as an admin. Display the roles of the users in the cluster. 
**Reset password**
	`ambari-admin-password-reset`
![[Pasted image 20250213220821.png]]
Re-Login Ambari with 
	`user: admin`
	`password: thanh1234`
**Display Role of the users in the Cluster**
![[Pasted image 20250213221653.png]]

#### 8) Create a new user with your name and give it cluster manager (admin) role. 
>Add `Dadandan` role as `user` and dadandan as `password`
![[Pasted image 20250213221913.png]]
