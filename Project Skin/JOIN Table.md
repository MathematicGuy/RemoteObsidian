primary key: 
+ game - id
+ eteam - id
+ goal - matchid (match id)


![[Pasted image 20231130144753.png]]
![[Pasted image 20231130144804.png]]


```sql
CASE WHEN condition1 THEN value1 
	 WHEN condition2 THEN value2  
	 ELSE def_value 
END
FROM bbc
```
> Use this to print sth at condition x, y, z, etc...
![[Pasted image 20231130160422.png]]

  order by mdate, team1, team2
```sql
SELECT mdate,
  team1,
  SUM(CASE 
      WHEN teamid=team1 THEN 1 ELSE 0 END) as score1,
  team2,
  SUM(CASE      
      WHEN teamid=team2 THEN 1 ELSE 0 END) as score2
  FROM game JOIN goal ON matchid = id
  group by mdate, team1
  order by mdate, team1
```



  FROM game JOIN goal ON matchid = id
  group by mdate, team1, team2