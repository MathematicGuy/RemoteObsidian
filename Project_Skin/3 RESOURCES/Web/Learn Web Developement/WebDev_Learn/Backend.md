**back-end: save and manages data**

*bc Computers can't receive messages (by default)* -> use a Server

Popular backend programming language
	JS (Node JS), Python ,Ruby, Java

*However written a backend cost a lot of effort and time so we use 2 of this tools:*
1. **Backend Framework**
	>Create a Server easier with much less code.
	+ **Language**: Express (ExpressJS), django (Python Django), Rails (Ruby on Rails), spring (Java Spring)
2. **Package Manager**
> Each language has it own Package Manager:
> + npm for javascript 	
	+ pip for python
	+ bundler for ruby
	+ Maven for Java

*The web is running, now we need a place ot store ours data*
![[Pasted image 20231022104915.png]]
	Use a data base
![[Pasted image 20231022104930.png]]
Request-Response cycle
	*Frontend send msg to Server*: Request
![[Pasted image 20231022105349.png]]
*Server save the msg to DataBase*  
	 *Then send a msg back to the front-end*: Response 

 
 **API (Application Programming Interface)** 
**Path** 
	![[Pasted image 20231022110724.png]]
**In the Back-end**
	![[Pasted image 20231022110817.png]]
	 (line of codes) Function that interacs with server in other word Create Commands

**REST API = API + REST**   -> naming comvention
+ REST (Representational State Transfer)
	![[Pasted image 20231022110950.png]]
	 **Type (request)**
	+ POST = create something
		Ex: POST /orders = create an order
	+ GET = get something
	+ DELETE = delete something
> 	**URL PATH**
> 		the last part represent a NAME, for specifications:  /orders


**Cloud Computing Pillars**
![[Pasted image 20231022095615.png]]
+ IaaS: Infrastructure as a service
		service like: Virtual Machine, Server, etc..
		VM like a small computer inside a computer
	+ cloud company like: AWS, GG Cloud Platform, MS Azure 
+ PasS: Platform as a service 
		Integrate code, Set up VM, install Loadbalancer for you  
	+ company: AWS Elastic Beanstalk, App Engine from GG, App Service from MS Azure 
+ Saas: Software as a service (A company that Optimize a specific part of a Web/App to sell their service)
		Doing Microsercice like Email Service from automatic sending to uploading. 
	+ company: twilio (Email), Elasticsearch (search database)  
***Most of Back-end problems has a company provide the solution. For it optimize, economic you more likely don't need to make one on your own.*** 

