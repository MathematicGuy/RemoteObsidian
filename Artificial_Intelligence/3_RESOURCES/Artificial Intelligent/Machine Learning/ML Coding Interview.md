## Coding Note
**For Loop:** 
`for i in range(start: 0, stop: 3, step: 2)`: for loop stop if `step` > `stop` so if 
+ `stop` = 3 then there 2 loop: 0, 2, stop the whole loop
+ but if `stop` = 2 then there only 1 loop "0, stop the whole loop" because `step == 2` at the second step. 

**Condition at the Start vs End of the Loop** 
*start:* hard break - stop incorrect result from ever happened.
*end:* soft break - stop partial correct/incorrect result to happend. 
	e.g. You want a list length of 3 but there 1 *left over* value in the list so you want to scoop up the last value. 

*Case Study:* In my Token Chunking problem i check if the Chunk_size > total_token_length (ie. the whole sequence length).  
```python
condition at the start: [['a', 'b', 'c']] 
condition at the end: [['a', 'b', 'c'], ['d']] # Slide operation get whatever leftover value at the end for 1 last time
```


### [[Computer Vision Revision]]