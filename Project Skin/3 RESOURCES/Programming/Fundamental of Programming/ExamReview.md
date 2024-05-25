
![[De_kiemtra1tiet.jpg]]

1)
```sql
select MAGV, HOTEN, DIENTHOAI, MAKHOA
from Giangvien
join
	Khoa on Giangvien.MAKHOA = Khoa.MAKHOA 
where 
	TENKHOA = "Tin học"
```
2)
```sql
select Lichgiangday.NGAYDAY
from Lichgiangday 
join
	Giangvien on Lichgiangday.MAGV = Giangvien.MAGV
where Giangvien.HOTEN = "Ngô Thu Hà"
```
3)
```sql
select Monhoc.TENMH, Monhoc.MAMH, Giangvien.HOTEN 
from Giangvien 
JOIN 
	Lichgiangday on  Giangvien.MAGV = Lichgiangday.MAGV 
JOIN 
	Monhoc on Lichgiangday.MAMH = Monhoc.MAMH 
JOIN 
	Lop on Lichgiangday.MALOP = Monhoc.MALOP
GROUP BY 
	Monhoc.TENMH, Monhoc.MAMH, Giangvien.HOTEN 
HAVING 
	Monhoc.SISO = MAX(Monhoc.SISO)
```
4)
```sql
select * from Khoa 
JOIN
	Lichgiangday ON Khoa.MAMH = Lichgiangday.MAMH
JOIN
	Lichgiangday ON Lichgiangday.MAMH = Monhoc.MAMH
where 
	Monhoc.TENMH = "Cơ sở dữ liệu"
```
5)
```sql
select MAKHOA, TENKHOA, SUM(SISO) from Lop 
JOIN 
	Khoa ON Lop.MAKHOA = Khoa.MAKHOA 
Group by
	Khoa.MAKHOA
ORDER BY SUM(SISO) DESC
```