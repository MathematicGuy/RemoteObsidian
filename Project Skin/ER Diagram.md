![[Pasted image 20240421152924.png]]

![[Pasted image 20240421152937.png]]

One-to-One: Security
![[Pasted image 20240421153143.png]]

I want to create a ER Diagram for these Features. 
+  Choose compatible Teams for the Project through team's main skill (Ex: Shoping website project will require Web Development Team, Management Team, Marketing Team, etc.. )
+  Choose the right employee for Team (ex: Web Development team will choose employee that have skills like web programming, JS programming, Design, Back-end programming, etc..)
+  The Team Table should connect to a Role table which use to grant tag to team's member the role later. (1 member can have only 1 role)
+ Employee can have may skills (which is granted by the manager)
+ manager also a employee (manager_id is a FK refer employee_id)
Let me give you a Example of the Work Flow from the web persective:
1) Skills tags will be given to the employee by admin. Now the employees will have 1 to many skills. 
2) Employee that can do Web Programming works will be in Web Programming Team. The same for AI, Business Team, etc..
3) The Team will then grant team's member role. Ex: member can do FE and BE be a FullStake role, member with great communication and general skill be a Team lead.
4) Now, the compatible Team for be chosen for the Project. Ex: Shopping Project will only choose Web Deve, Markting team

These are my main Feature for the system: Tag Management, Role Management, Choose compatiple team for the Project, Choose compatible employee for the team.
Also explain the relationship and table in detail

![[Pasted image 20240421171444.png]]

