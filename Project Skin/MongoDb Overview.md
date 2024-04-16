![[Pasted image 20240415134802.png]]
Ko cần pải Join

**Mô hình**
**Standalone**
![[Pasted image 20240415134955.png]]
csdl bth

**Replication**
![[Pasted image 20240415135019.png]]
Tất cả chứa trong 1 server. 

**Sharding**
![[Pasted image 20240415135248.png]]
> cụm máy chủ.
> Mỗi cụm chứa riêng 1 phần dữ liệu. 


![[Pasted image 20240415135704.png]]
On-premise: lưu local.

### MongoDb Architecture
Logic
+ Collection - table


Kiến trúc khi hoạt động![[Pasted image 20240415140116.png]]
 user -> db memory -> file

**Storage Engine**
![[Pasted image 20240415140407.png]]
```json
mongosh // activate mongoDb
db.serverStatus().storageEngine
```
> check storage engine


file Journal -> restore when Db get shutdown/broken
file Snapshots -> like quick save. Then save to Journal
![[Pasted image 20240415140854.png]]
file bin -> cài đặt quan trọng
file log -> các log trong qtrinh hoạt động

Cấu trúc insert ko cần phải giống nhau. (bên SQL pải giông ở cả hàng vs cột)
Id - auto 


### Lọc dữ liệu
![[Pasted image 20240415153439.png]]

![[Pasted image 20240415153447.png]]

-- Explain Execution Stats
```json
db.users.find({firstName:"Charlie", age:52}).explain("executionStats");
```
**BEFORE INDEXING**
total exc time 43 mili sec
totalDocsExamL 52k
returnDocument: 135
52k / 135 = 385.1851851852 (each 385 file found one document) 
Algorithm: 


**AFTER INDEXING**
```json
db.users.find({age:30}).explain("executionStats");
```
> nReturn: 10454 (found document)
> totalKeysExamined: 10454 
![[Pasted image 20240416183947.png]]
