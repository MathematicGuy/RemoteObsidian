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


Make a Table Like this
![[Pasted image 20231130195329.png]]
Notice in the query given every goal is listed. If it was a team1 goal then a 1 appears in score1, otherwise there is a 0. You could SUM this column to get a count of the goals scored by team1. **Sort your result by mdate, matchid, team1 and team2.**
```sql
SELECT
  mdate,
  team1,
    SUM(CASE WHEN teamid = team1 THEN 1 ELSE 0 END) AS score1,
  team2,
    SUM(CASE WHEN teamid = team2 THEN 1 ELSE 0 END) AS score2
FROM game
LEFT JOIN goal 
ON matchid = id
GROUP BY mdate, team1
ORDER BY mdate, matchid
```
-- **JOIN reject NULL** value by default  (0 also consider as NULL)
++ using **LEFT JOIN or RIGHT JOIN keep NULL** & 0 in the table.   
++ ORDER BY matchid because there might be 2 match in the same day. Using matchid we can identify which start first and which start later. 


```sql
select name, title from actor JOIN movie 
where yr=1962 and
```

```sql
select title, name from movie JOIN actor ON
select name from actor
where actor.id IN (select actorid from movie JOIN casting ON movieid = id where yr=1962 and ord = 1)
```

```sql
select name, title from movie JOIN actor 
where movie.id IN (select id from movie where yr=1962)
and actor.id IN (select actorid from casting where ord=1)
```


