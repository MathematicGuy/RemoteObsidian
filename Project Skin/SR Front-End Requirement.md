> **29/2: Cả 2 Đưa ra các Thiết Kế rồi thảo luận**
Languages: HTML, CSS, Tailwind CSS, JS, JQuery 
> 

**Core Design Concept**
Color: 70/20/10 - **one neutral color, one rich color, and one accent color**


**Reviewer Interface & Functionality**
+ Java Script
	+ React: popular and efficiency

**Tailwind CSS** is a fantastic choice for styling ASP.NET Core websites.

+ **Maintainability:** Its low-level approach means you work with more predictable and maintainable stylesheets.
+ **Responsive Design:** Tailwind has built-in responsiveness, making it easy to create mobile-friendly websites.
+ **Atomic CSS Approach:** While some find this different, it can promote better code organization and scalability.


### Requirement (1st Step)

**Home UI requirement**
+ Sign-In/Sign-Up 
	If not Sign-up can press Sign-up link below Sign-In
+ Forgot password

+ Reference
	![[Pasted image 20240227105049.png]]
Setting 


**Student UI requirement**
+ Dashboard (view Enrolled Assignment)
+ Public Assignment
+ ....

+ Reference
	![[Pasted image 20240227105121.png]]

**Teacher UI Requirement**
+ Dashboard (view Submited Assignment)
+ View Assignment 
	+ Show Assignment Start & Due Date 
	+ Show total students had submitted assignment
		+ Click to see who had submitted


+ **Create Assignment**
+ **Draft Assignment**
+ **Publish Assignment**
+ **Opended Assignment**
+ **Closed Assignment**

+ Finalized Assignment
+ Export Score (in csv, txt, xlsx) 
+ Score Assignment parallel with ChatGPT result
	+ Can view ChatGPT code score & review side by side (can be fold)

+ Setting (Manage profile, functionalities(change theme, Compact view, Normal, etc..)
+ Reference
	![[Pasted image 20240227105139.png]]

**Admin UI Requirement**
+ Seperate Table for each type of user
+ View
	+ User basic info
	+ Can view user detail info

+ Disable/Enable User Account
+ Verify User Account
+ Bot management (Modify Bot, Fine-Tune Bot)

+ Reference
	![[Pasted image 20240227103305.png]]
