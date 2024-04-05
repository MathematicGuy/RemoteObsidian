SQL
pro: query


NoSQL
pro: when data changes constantly
cons: duplicate, abnormal data

**Project summary:** Quản lý công việc của các nhân viên tham gia trong các dự án ở các ban. 

- **employees** (empl)
    M (empl) - 1 (dep) 
- **departments** (dep)
    1 (dep) - M (proj)
- **projects** (proj)
	1 (proj) - M (tas)
- **tasks** (tas)

VD: 
SQL có 1 bảng riêng cho từng thể loại film
-> 1 người ko thể tự nhiên có 1 thể loại film

NoSQL có thể thêm tùy ý vô số lần. 1 người có thể gán thêm hàng trăm thể loại film thì ko bị ràng buộc.
+ Tra cứu tệ. Tra theo ràng buộc 