#### Reading Files
```python
file.readline() # read 1 line currently
file.read() # read all

# Openning & Close 
with open("spider.txt") as file:

# Print line by line 
with open('spider', 'r') as file:
	for line in file:
		print(line)
		# without empty line
		print(line.strip())

```


#### Writing File
```python
# Return Number of characters that it wrote if write successful.

with open('spider', 'w') as file:
	file.write("something")

>> 
```
> **Notice:**
> + "w" (wrting) an already exist file will Overwrite the old contents. 
![[Pasted image 20230711145316.png]]
