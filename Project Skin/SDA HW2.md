![[DB_Schema.jpg]]
![[1.jpg]]
![[2.jpg]]

1)
```sql
select last_name, departments.department_id, departments.department_name
from  employees
    INNER JOIN departments ON employees.department_id = departments.department_id;
```
2)
```sql
select Distinct(job_title), street_address from jobs
JOIN employees ON jobs.job_id = employees.job_id
JOIN departments ON employees.department_id = departments.department_id
JOIN locations ON departments.location_id =  locations.location_id  
where departments.department_id = 4

select * from locations
```
3)
```sql

```
4)
```sql

```
5)
```sql

```
6)
```sql

```
7)
```sql

```
8)
```sql

```
9)
```sql

```
10)
```sql

```