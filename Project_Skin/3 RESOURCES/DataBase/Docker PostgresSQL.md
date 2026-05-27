---
category: "3 RESOURCES/DataBase/Docker PostgresSQL.md"
summary: "This deployment note explains how to manage PostgreSQL database servers using Docker containers and the Windows Services utility. It details commands for checking container status and addresses connection timeout resolutions."
keywords: []
confidence: "high"
analyzed_at: "2026-05-27T17:32:07.262431+00:00"
---
src: https://youtu.be/RdPYA-wDhTA?si=pggXY2rz8PRTiU3C
Docke .yml file is just like DbContext file. It help connect the API and the Database
![[Pasted image 20240801162411.png]]

docker login
docker ps   


## Postgres Server Timeout
1) Window + S -> Click Service
2) Find postgresql and click it
	![[Pasted image 20240802002143.png]]
3) Start Postgres server if it not running yet. That it, now active your database again. 
	![[Pasted image 20240802002218.png]]



Remember to Create Table. Docker can't do it for you