SELECT
note: COALESCE(field, '') use to define all field NULL value and replace it with value inside ''  
```sql
select 
    Students.studentID, COALESCE(scoreValue, '0') 
as 
    studentScore, name, class 
from
    Students 
LEFT OUTER JOIN
    Scores 
ON Students.studentID = Scores.studentID;
```

CREATE
```sql
CREATE TABLE Students (
  studentID INT PRIMARY KEY,
  name VARCHAR(255),
  class VARCHAR(10),
  contactInfo VARCHAR(255)
);
```

```sql
CREATE TABLE Scores (
  scoreID INT PRIMARY KEY,
  studentID INT,
  subject VARCHAR(255),
  scoreValue INT,
  FOREIGN KEY (studentID) REFERENCES Students(studentID)
);
```


INSERT
```sql
INSERT INTO Students (studentID, name, class, contactInfo) VALUES
  (1, 'John Doe', 'A101', 'john@example.com'),
  (2, 'Jane Smith', 'B203', 'jane@example.com'),
  (3, 'Michael Brown', 'C304', 'michael@example.com'),
  (4, 'Emily Johnson', 'D405', 'emily@example.com'),
  (5, 'Daniel Williams', 'E506', 'daniel@example.com');
```

```sql
INSERT INTO Scores (scoreID, studentID, subject, scoreValue) VALUES
  (1, 1, 'Math', 85),
  (2, 1, 'English', 92),
  (3, 2, 'Math', 78),
  (4, 3, 'Physics', 88),
  (5, 3, 'Chemistry', 95);
```

