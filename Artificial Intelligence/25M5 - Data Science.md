## How Modern Data Teams Work (Engineer, Analysis, Scientist, Architect, ML)

Managers see problems in business (e.g which areas underperform, perform thus need to invest more, why profits down ?)
-> Need and relied 

**Data Analysis -** pulling the data manually from the source, analyst a data and present it to the manager -> its manuall -> not scalable, need a automated pipeline.    
**Data architect -** design a scalable data system. 
**Data engineer -** the one who building it. Build a data pipeline, ensure the data to move quickly from Raw to the database.  -> Allow data analyst to analyse data faster. focus on what matter.
However, data analysist only present the insight once, like running a SQL query everytime someone ask for it. We need a web or dashboard so everyone can see it, without running SQL query manually. 
**BI Developer (Business Insight developer) -** build a env like server for visualize using Dashboard so everyone in the company can see the data in live. 
![[Pasted image 20251020083344.png# left]]

Data Scienctist - create/training/experiement Model (ML/DL) for predicting the future. 
ML Engineer - prepare server & env to run and deploy a model from the Data Scientists automatically 24/7. Also include report UI/UX for the manager & everyone to see insight.   
![[Pasted image 20251020083755.png | 555]]

![[Pasted image 20251020083937.png | 555]]

### ETL vs ELT (E - Extract, T - Transform, L - Loading)
What are they ? 
![[Pasted image 20251020094904.png]]
ETL - when there're sensitive data, thus personal data need to be mask before transfer into the database. Taken time due to the volume and variety of incomming data. 
ELT - for fast loading speed and job that can clean the data by themself. But data complience (e.g. sensitive data) may be effected. 
a