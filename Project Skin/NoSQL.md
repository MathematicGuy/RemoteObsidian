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
