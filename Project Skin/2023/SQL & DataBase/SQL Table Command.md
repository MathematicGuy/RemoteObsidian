```sql
-- Tạo CSDL SimThe
CREATE DATABASE SimThe;

-- Chuyển sang CSDL SimThe
USE SimThe;

-- Tạo bảng Sim
CREATE TABLE Sim (
  SimID VARCHAR(9) NOT NULL,
  NgayKichHoat CHAR(50),
  NgayHetHan CHAR(50),
  KhuyenMai CHAR(1) DEFAULT NULL
);

-- Tạo khóa chính cho bảng Sim
ALTER TABLE Sim
ADD CONSTRAINT PK_Sim PRIMARY KEY (SimID);
```


INSERT
```sql
INSERT INTO Sim (SimID, NgayKichHoat, NgayHetHan, KhuyenMai)
VALUES
  ('096512344', '2023-07-20', '2024-07-20', 'x'),
  ('098790123', '2023-08-01', '2024-08-01', NULL),
  ('091234567', '2023-09-01', '2024-09-01', 'x'),
  ('093456789', '2023-10-01', '2024-10-01', NULL);
GO
```


