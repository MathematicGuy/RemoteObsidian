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