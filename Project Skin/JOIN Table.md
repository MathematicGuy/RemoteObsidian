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

|mdate|team1|score1|team2|score2|
|---|---|---|---|---|
|1 July 2012|ESP|4|ITA|0|
|10 June 2012|ESP|1|ITA|1|
|10 June 2012|IRL|1|CRO|3|
|11 June 2012|FRA|1|ENG|1|
|11 June 2012|UKR|2|SWE|1|
|12 June 2012|GRE|1|CZE|2|
|12 June 2012|POL|1|RUS|1|
|13 June 2012|DEN|2|POR|3|
|13 June 2012|NED|1|GER|2|
|14 June 2012|ESP|4|IRL|0|
|14 June 2012|ITA|1|CRO|1|
|15 June 2012|SWE|2|ENG|3|
|15 June 2012|UKR|0|FRA|2|
|16 June 2012|CZE|1|POL|0|
|16 June 2012|GRE|1|RUS|0|
|17 June 2012|DEN|1|GER|2|
|17 June 2012|POR|2|NED|1|
|18 June 2012|CRO|0|ESP|1|
|18 June 2012|ITA|2|IRL|0|
|19 June 2012|ENG|1|UKR|0|
|19 June 2012|SWE|2|FRA|0|
|21 June 2012|CZE|0|POR|1|
|22 June 2012|GER|4|GRE|2|
|23 June 2012|ESP|2|FRA|0|
|24 June 2012|ENG|0|ITA|0|
|27 June 2012|POR|0|ESP|0|
|28 June 2012|GER|1|ITA|2|
|8 June 2012|POL|1|GRE|1|
|8 June 2012|RUS|4|CZE|1|
|9 June 2012|GER|1|POR|0|
|9 June 2012|NED|0|DEN|1|
