## 1. Basic of Software Architecture
by building an ecommerce site

**First:** Get The Context
	What should the system do?
		search data?
		add to cart?
	How should function behave? a.k.a ..-lities
		+ Non-function requirement 
		+ Developed for several years (Maintainability)
		+ Able to serve millions of users (Scalability)
		+ Available 24/7
		  (Reliabiliy)
	Restriction (in your region)
		Standards, Cost, etc...

**Second:** Priorities
Time to market vs Features?
Do we really need portability?
-> portability vs maintainability/scalability


Start with One at a Time
(Don't overthink it or you'll Over Enginneer it)

![[Pasted image 20231215091152.png]]


## 2. Scaling Distributed System 

More user -> More scale (Database)
-> **Horizontal Scaling**

![[Pasted image 20231215091904.png]]
#### Consistency Level
Strict Consistancy
	Any write immediatly available to all readers
Eventual Consistency
	There's a delay between a write and when all the readers can see that write
-> Will system need to read or write more?


#### How to achieve Horizontal Scaling

![[Pasted image 20231215092215.png]]
Sharding: spit data for each region
![[Pasted image 20231215092303.png]]
Sharding by Hash

![[Pasted image 20231215092317.png]]
Replication: replication of data in multiple servers.

**Summary**
![[Pasted image 20231215092403.png]]



Distributed Caches -> increase data flow 
Cached can be added later


## Client/Server Model
1 Client, 1 Server, 1 Database 
![[Pasted image 20231215095116.png]]

### Mirco Service v/s Monolithic Service
Micro service: divide each service account for 1 problem
	If 1 thing breakdown -> only that service break down
	Each service run independently.
Monolithic: hold all service
	if 1 thing break down -> all thing break down
![[Pasted image 20231214013524.png]]

Serverless Architecture
	+ Function as a service (FAAS) is a software design pattern where our function is hosted by a 3rd party like MS Azure, Firebase cloud, AWS, etc..
![[Pasted image 20231214013601.png]]


