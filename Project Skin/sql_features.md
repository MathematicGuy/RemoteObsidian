# SQL Features Document
## SQL Basic Features (CRUD - Create, Read, Update, Delete)
### Tag, Role
**Manage Tag, Role**
- Insert Skill and Role Tag and Task:
+ add Skills Tag:
```sql
INSERT INTO Skills (skill_name, skill_description) 
VALUES ('Tên kỹ năng', 'Mô tả kỹ năng');
```
+ add Role Tag:
```sql
INSERT INTO Role (role_name, role_description)
VALUES ('Tên_role_mới', 'Mô_tả_role_mới');
```
+ add Task:
```sql
 INSERT INTO Task (task_name, task_description, task_priority, status, due_date)
 VALUES ('Develop new feature', 'Implement new feature X according to specifications', 'High', 'Pending', '2024-05-15');
```

- View Skills and Role Tag and Task:
+ View Skills Tag:
```sql
SELECT skill_id, skill_name, skill_description FROM Skills;
```
+ View Role Tag:
```sql
SELECT role_id, role_name, role_description FROM Role;
```
+ Add Task:
```sql
SELECT task_id, task_name, task_description, task_priority, status, due_date FROM Task;
```
 

- Edit Skills and Role Tag and Task:
+ Edit Skills Tag:
```sql
UPDATE Skills
SET skill_name = 'Tên kỹ năng mới', skill_description = 'Mô tả kỹ năng mới'
WHERE skill_id = 1;
```
+ Edit Role Tag:
```sql
UPDATE Role
SET role_name = 'Tên_role_mới', role_description = 'Mô_tả_role_mới'
WHERE role_id = id_cần_sửa;
```
+ Add Task: 
```sql
 UPDATE Task
 SET 
	  task_name = 'Phát triển tính năng mới',
	  task_description = 'Triển khai tính năng X theo yêu cầu',
	  task_priority = 'High',
	  status = 'In Progress',
	  due_date = '2024-05-20'
 WHERE 
	  task_id = [task id cần sửa];
```

- Delete Skills and Role Tag
+ Delete Skills Tag: Trigger to Delete Skills and it dependency: skill_id from Team , employee_skills, team_skill_tag 
```sql
    CREATE OR ALTER TRIGGER cascade_delete_skill 
    ON Skills
    INSTEAD OF DELETE
    AS
    BEGIN
        DECLARE @deleted_skill_id INT;

        SELECT @deleted_skill_id = skill_id FROM deleted;

        -- Delete from team_skill_tag
        DELETE FROM team_skill_tag
        WHERE skill_id = @deleted_skill_id;

        -- Delete from employee_skills
        DELETE FROM employee_skills
        WHERE skill_id = @deleted_skill_id;

        -- Delete from employee_skills
        DELETE FROM project_prefer_skills
        WHERE skill_id = @deleted_skill_id;

        -- Delete from Team (assuming cascading delete is not set up)
        UPDATE Team SET team_skill_id = NULL WHERE team_skill_id = @deleted_skill_id;
        DELETE FROM Skills WHERE skill_id = @deleted_skill_id;


    END;
    GO
```
    
+ Delete Role Tag: Delete a Role and its dependency like role_id from team_member
```sql
    CREATE OR ALTER TRIGGER delete_role_actions
    ON Role
    INSTEAD OF DELETE 
    AS
    BEGIN
        DECLARE @deleted_role_id INT;

        SELECT @deleted_role_id = role_id FROM deleted;

        -- 1. Remove associated role assignments (team_member or similar)
        DELETE FROM team_member 
        WHERE role_id = @deleted_role_id;  

        DELETE FROM Role 
        WHERE role_id = @deleted_role_id;  
    END;
    GO
```

### Employees
**Manage Employee**
- Insert Employee
```sql
    INSERT INTO employees (first_name, last_name, email, phone_number, address, birth_date, hire_date)
    VALUES ('Họ', 'Tên', 'Email', 'Số điện thoại', 'Địa chỉ', 'Ngày sinh', 'Ngày tuyển dụng');
```

- View Employee
```sql
SELECT * FROM Employee 
```

- Edit Employee
```sql
    UPDATE Employee
    SET first_name = 'Họ mới', last_name = 'Tên mới', email = 'Email mới', phone_number = 'Số điện thoại mới', address = 'Địa chỉ mới', birth_date = 'Ngày sinh mới', hire_date = 'Ngày tuyển dụng mới'
    WHERE employee_id = [ID của nhân viên];
```
- Delete Employee
```sql
    CREATE OR ALTER TRIGGER cascade_delete_employee
    ON Employee
    INSTEAD OF DELETE
    AS
    BEGIN
        DECLARE @deleted_employee_id INT;

        SELECT @deleted_employee_id = employee_id FROM deleted;

        -- 1. Delete assignments from team_member 
        DELETE FROM team_member 
        WHERE member_id = @deleted_employee_id; 

        -- 2. Delete assigned tasks from team_task
        DELETE FROM team_task
        WHERE assigned_employee_id = @deleted_employee_id; 

        -- 3. Update team_lead_id to NULL in Team table
        UPDATE Team 
        SET team_lead_id = NULL
        WHERE team_lead_id = @deleted_employee_id;

        -- 4. Update project_manager_id to NULL in Project table
        UPDATE Project 
        SET project_manager_id = NULL 
        WHERE project_manager_id = @deleted_employee_id;

        -- 5. Delete records from employee_skills 
        DELETE FROM employee_skills 
        WHERE employee_id = @deleted_employee_id;

        -- 6. Finally, delete the employee
        DELETE FROM Employee
        WHERE employee_id = @deleted_employee_id;
    END;
```

### Team
**Manage Team**

- Insert Team
```sql
    INSERT INTO Team (team_name, team_skill_id, team_lead_id, team_status)
    VALUES ('Tên nhóm mới', id_kỹ_năng, id_nhân_viên_trưởng_nhóm, 'Trạng thái nhóm');
```

- View Team
```sql
    SELECT 
        t.team_id, 
        t.team_name, 
        s.skill_name AS team_skill, 
        CONCAT(e.first_name, ' ', e.last_name) AS team_lead,
        COUNT(tm.member_id) AS number_of_members
    FROM 
        Team t 
    LEFT JOIN 
        Skills s ON t.team_skill_id = s.skill_id 
    LEFT JOIN 
        Employee e ON t.team_lead_id = e.employee_id 
    LEFT JOIN 
        team_member tm ON t.team_id = tm.team_id 
    GROUP BY 
        t.team_id, t.team_name, s.skill_name, e.first_name, e.last_name;
```

- Edit Team
```sql
    UPDATE Team
    SET 
        team_name = 'Tên nhóm mới',
        team_skill_id = 'ID kỹ năng mới',
        team_lead_id = 'ID trưởng nhóm mới'
    WHERE 
        team_id = [ID_nhóm];
```

- Delete Team
- ? Change Team status to Deactive instead of Delete (since Team hold many contraint and valuable infomation)
```sql
    update Team
    set team_status = 'Deactive' -- status: Active/Deactive
    where team_id = 1

    select * from Team
```

### Task
- Create
+ Add Task to Team (project_manager create overview task and assign to team)
```sql
CREATE OR ALTER PROCEDURE create_task_for_team
    @task_id INT,
    @team_id INT,
    @task_name VARCHAR(MAX), -- Adjust the size as needed 
    @task_description VARCHAR(MAX), 
    @task_priority VARCHAR(10), -- Or appropriate datatype
    @task_status VARCHAR(10),  -- Or appropriate datatype
    @task_due_date DATE -- Or DATETIME 
AS
BEGIN
    INSERT INTO Task (task_name, task_description, task_priority, status, due_date)
    VALUES (@task_name, @task_description, @task_priority, @task_status, @task_due_date);

    SET @task_id = SCOPE_IDENTITY();

    INSERT INTO team_task (team_id, task_id)
    VALUES (@team_id, @task_id);
END;
-- usage example
EXEC create_task_for_team 
    @team_id = 2, 
    @task_name = 'Design User Interface',
    @task_description = 'Create wireframes and high-fidelity mockups',
    @task_priority = 'High',
    @task_status = 'Pending',
    @task_due_date = '2023-12-25';  
```


- Delete: Delete a Task and its dependency like task_id from team_task 
```sql
    CREATE OR ALTER TRIGGER cascade_delete_task 
    ON Task
    INSTEAD OF DELETE
    AS
    BEGIN
        DECLARE @deleted_task_id INT;
        SELECT @deleted_task_id = task_id FROM deleted;

        -- Delete dependencies from team_task
        DELETE FROM team_task
        WHERE task_id = @deleted_task_id; 
    END;
```

### Project
**Manage Project**
- Insert Project
```sql
    INSERT INTO Project (name, goal, number_of_employees, prefer_team, project_priority, project_status, start_date, end_date, project_manager_id) 
    VALUES ('Tên dự án', 'Mục tiêu dự án', [Số lượng nhân viên], 'Đội ưu tiên', 'Mức độ ưu tiên', 'Trạng thái dự án', 'Ngày bắt đầu', 'Ngày kết thúc', [ID của quản lý dự án]);
```

- View Project
```sql      
    SELECT 
        p.*
        CONCAT(e.first_name, ' ', e.last_name) AS project_manager,
        COUNT(DISTINCT tp.team_id) AS number_of_teams
    FROM 
        Project p
    LEFT JOIN 
        Employee e ON p.project_manager_id = e.employee_id
    LEFT JOIN 
        team_project tp ON p.project_id = tp.project_id
    GROUP BY 
        p.project_id, p.name, p.goal, p.number_of_employees, p.project_priority, p.project_status, p.start_date, p.end_date, e.first_name, e.last_name;
```

- Edit Project
```sql
    UPDATE Project
    SET name = 'Tên dự án mới', goal = 'Mục tiêu dự án mới', number_of_employees = [Số lượng nhân viên mới], prefer_team = 'Đội ưu tiên mới', project_priority = 'Mức độ ưu tiên mới', project_status = 'Trạng thái dự án mới', start_date = 'Ngày bắt đầu mới', end_date = 'Ngày kết thúc mới', project_manager_id = [ID của quản lý dự án mới]
    WHERE project_id = [ID của dự án cần cập nhật];
```

- Deactivate Project: Change Project status to Deactive instead of Delete (since Project hold many contraint and valuable infomation)
```sql
    UPDATE Project
    SET project_status = 'Completed' -- ('Pending', 'In Progress', 'Completed')
    WHERE project_id = 1;
    select * from Project;
```
- ? Set Project to project_priority
```sql
    UPDATE Project
    SET project_priority = 'Low' -- ('Low', 'Medium', 'High')
    WHERE project_id = 1;
    select * from Project;
```
- ? Update start_data and Update end_date
```sql
    UPDATE Project
    WHERE project_id = 1;
    select * from Project;
```


### SQL Specical Features (Procedure, Trigger)
#### Procedures
- ? Team Features: View Employee through Skill Tag
```sql
    /*
        Procedure: ListEmployeesBySkillID

        Description:
        This stored procedure retrieves a list of employees who have a specific skill ID.

        Parameters:
        - @SkillID: The ID of the skill to filter the employees by.

        Returns:
        The result set includes the first name, last name, email, phone number, and hire date of the employees who have the specified skill ID.
    */

    CREATE OR ALTER PROCEDURE ListEmployeesBySkillID
        @SkillID INT
    AS
    BEGIN
        SELECT e.first_name, e.last_name, e.email, e.phone_number, e.hire_date
        FROM Employee e
        INNER JOIN employee_skills es ON e.employee_id = es.employee_id
        INNER JOIN Skills s ON es.skill_id = s.skill_id
        WHERE s.skill_id = @SkillID;
    END;
    Go
    
    -- select * from employee_skills
    EXEC ListEmployeesBySkillID 20;
```


- ? Project Procedure: Skill needed for a Project
```sql
    SELECT s.skill_name, s.skill_description
    FROM Skills s
    JOIN project_prefer_skills pps ON s.skill_id = pps.skill_id
    WHERE pps.project_id = 1; -- Assuming Project A is project_id 1
```

- ? Project Procedure: Team in a Project
```sql
    SELECT t.team_id, t.team_name
    FROM Team t
    JOIN team_project tp ON t.team_id = tp.team_id
    WHERE tp.project_id = 111;  -- Assuming you want teams for Project 3
```

- ? Team Procedure: Employees on a Team with Specific Skill
```sql
    -- This query selects the first name, last name, and email of employees who have the skill with skill_id 1 and are part of the 'Web Development Team'.
        SELECT e.first_name, e.last_name, e.email
        FROM Employee e
        JOIN employee_skills es ON e.employee_id = es.employee_id
        JOIN team_skill_tag tst ON es.skill_id = tst.skill_id
        JOIN Team t ON tst.team_id = t.team_id
        WHERE t.team_name = 'Web Development Team' AND tst.skill_id = 1; -- Assuming skill_id 7 is 'Mobile Development'
```

- ? Team Procedure: Display Teams by Skill ID 
```sql
    -- This stored procedure is used to display teams based on a specific skill ID.
    -- It takes a parameter called @skill_id_param, which represents the skill ID to filter the teams by.
CREATE OR ALTER PROCEDURE display_teams_by_skill_id
    @skill_id_param INT
AS
BEGIN
    -- The SELECT statement retrieves the team ID, team name, skill name, and skill description
    -- from the Team, team_skill_tag, and Skills tables.
SELECT DISTINCT t.team_id, t.team_name, s.skill_name, s.skill_description
    FROM Team t
    JOIN team_skill_tag tst ON t.team_id = tst.team_id
    JOIN Skills s ON tst.skill_id = s.skill_id
    WHERE s.skill_id = @skill_id_param;
    -- The WHERE clause filters the result set based on the provided skill ID parameter.
    -- Only teams with the specified skill ID will be returned.
END;
Go
EXEC display_teams_by_skill_id 1
```

- ? Display Employees by Team Skill Tag
```sql
    /*
        Procedure: display_employees_by_team_skill
        Description: This procedure displays the employees who have skills matching a specified team's ID.
        Parameters:
            - @team_id: The ID of the desired team.
        Returns: None
        */

        CREATE OR ALTER PROCEDURE display_employees_by_team_skill 
            @team_id INT -- Parameter to specify the desired team's ID
        AS
        BEGIN
            SELECT e.first_name, e.last_name, e.email, s.skill_name -- Select relevant employee and skill data
            FROM Employee e
            JOIN employee_skills es ON e.employee_id = es.employee_id -- Join with employee skills
            JOIN team_skill_tag tst ON es.skill_id = tst.skill_id -- Join with team skill associations
            JOIN Skills s ON es.skill_id = s.skill_id -- Join with the skills table  
            JOIN Team t ON tst.team_id = t.team_id -- Join with the teams table
            WHERE t.team_id = @team_id; -- Filter for employees matching the team's skills 
        END;
        GO

        EXEC display_employees_by_team_skill @team_id = 3; -- Execute the procedure with team_id = 1
```

- ? Display Employees by Skill Tag and Which Team they in
```sql
    -- This stored procedure displays employees who have a specific skill.

    -- Creating or altering the stored procedure 'display_employees_by_skill'
    CREATE OR ALTER PROCEDURE display_employees_by_skill 
        @skill_id INT -- The ID of the skill to filter employees by
    AS
    BEGIN
        -- Selecting the necessary employee details and team name
        SELECT 
            e.first_name, e.last_name, e.email, e.phone_number, e.hire_date, t.team_name
        FROM Employee e
        JOIN employee_skills es ON e.employee_id = es.employee_id
        JOIN team_member tm ON e.employee_id = tm.member_id 
        JOIN Team t ON tm.team_id = t.team_id 
        WHERE es.skill_id = @skill_id; -- Filtering employees by the specified skill ID
    END;
    GO

    -- Executing the stored procedure with a specific skill ID
    EXEC display_employees_by_skill @skill_id = 17; -- Assuming skill_id 7 represents 'Mobile Development'
```


#### Triggers
- ? We Cannot perform an aggregate function on an expression containing an aggregate or a subquery. 
- ? Trigger: Update Project 'number_of_employees' - On Progress
```sql

```






