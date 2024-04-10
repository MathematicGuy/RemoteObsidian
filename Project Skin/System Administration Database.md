Đỗ Hồng Quân 
	dhquan@cmc-u.edu.vn
Research activities: 
+ Specialie: ML
+ Application domains: OCV, Recommender System 
Non Relational SQL
+ [[MongoDB]]

[[SDA HW1]]
[[SDA HW2]]
[[Practice Procedure and Trigger]]
[[SAD Project]]
[[SDA NoSQL HW1]]

note: bài có thể vào: thiết kế DB, tối_ưu/chuẩn_hóa DB, giải thích các câu 
truy vấn. 

#### [[SDA Review]] (System Database Administator)

#### [[NoSQL]]


breaching data: in-structure data

--- 
Đặt chỉ mục (như trong Từ Điển) -> search A, found Acronym, Account, Apple, etc.. search B -> Bible, Barbie, Bubble, etc..

Server (
+ run 24/24,
+ static IP address (address create 1, use forever)
)

Local (
+ run only turn on,
+ dynamic IP address (change whenever my Laptop turn on/off)
)


DDL (data definition lanaguage)
DML (data manipulation language)
DCL (data controll language)
	Decentralize Permission, add clients to server

+ Decentralize editing and deletion rights
	3 admin, but hold different rights
		Ex:
		+ Sales DB manager, Social DB manager - only able to edit, delete, add to some allow permission table.
		+ admin - have every right.


DB Architecture
	Centralized DBMS 
	Client/Server
	Three-Tier Client/Server
		Save Data on 2 DB. 
		1 hold all data
		1 hold just the needed data
		+ ? Why? For security. The main DB only give out the necessary data![[Pasted image 20240226144851.png]]

API (Application Program Interface)

Redis (DBSM dạng key-value) - (recommended)
	run on RAM -> faster speed 

Document Oriented -> MongoDB
GraphDB 

### Trigger
How to delete an Admin user. 
(Ex: Manager who have relation with many other employees)
+ ! Errors: Cannot delete because it have many Dependened 
+ ? Purpose: Remove or Swap a high rank member from the Database.
ROLL BACK -> return to before executed state.
+ ? Why not Remove Contraint, because it may create errors that make the Employee become the Manager.

INSTEAD OF DELETE -> run this instead of DELETE.

+ 'ON UPDATE CASCADE' -> (often use)
	Automatically Update all the related data.
		Ex: Update Manager_department_id to 5 instead of 1 -> All Employees_ department_id automatically update t 5.
+ 'ON DELETE CASCADE' -> (Limited Usages)


password: gy3yvYUUyQzK151x
```cs
dotnet add package MongoDB.Driver
```

```cs
using MongoDB.Driver;
using MongoDB.Bson;

const string connectionUri = "mongodb+srv://dinhnhatthanh248:gy3yvYUUyQzK151x@new.qlstmml.mongodb.net/?retryWrites=true&w=majority&appName=New";

var settings = MongoClientSettings.FromConnectionString(connectionUri);

// Set the ServerApi field of the settings object to set the version of the Stable API on the client
settings.ServerApi = new ServerApi(ServerApiVersion.V1);

// Create a new client and connect to the server
var client = new MongoClient(settings);

// Send a ping to confirm a successful connection
try {
  var result = client.GetDatabase("admin").RunCommand<BsonDocument>(new BsonDocument("ping", 1));
  Console.WriteLine("Pinged your deployment. You successfully connected to MongoDB!");
} catch (Exception ex) {
  Console.WriteLine(ex);
}
```