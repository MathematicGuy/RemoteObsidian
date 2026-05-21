[Table Schema Design](https://drawsql.app/teams/3-bowls-of-rice/diagrams/student-score-management-db) 

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
-- Create Students table
CREATE TABLE Students (
    studentID NCHAR(1) PRIMARY KEY NOT NULL,
    name NVARCHAR(255) NULL,
    class NVARCHAR(5) NULL,
    contactInfo NVARCHAR(255) NULL
);

-- Create Scores table
CREATE TABLE Scores (
    scoreID NCHAR(1) PRIMARY KEY NOT NULL,
    studentID NCHAR(1) NOT NULL,
    subject NVARCHAR(50) NULL,
    scoreValue INT NULL,
    FOREIGN KEY (studentID) REFERENCES Students (studentID)
);
```


INSERT
```sql
-- Insert values into Students table
INSERT INTO Students (studentID, name, class, contactInfo)
VALUES 
    ('1', 'John Doe', 'DS101', 'john.doe@example.com'),
    ('2', 'Jane Smith', 'DS102', 'jane.smith@example.com'),
    ('3', 'Bob Johnson', 'DS103', 'bob.johnson@example.com'),
    ('4', 'Alice Williams', 'DS104', 'alice.williams@example.com'),
    ('5', 'Charlie Brown', 'DS105', 'charlie.brown@example.com');

-- Insert values into Scores table
INSERT INTO Scores (scoreID, studentID, subject, scoreValue)
VALUES 
    ('A', '1', 'Math', 85),
    ('B', '2', 'English', 92),
    ('C', '3', 'Science', 78),
    ('D', '4', 'History', 88),
    ('E', '5', 'Programming', 95);
```

