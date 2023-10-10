```python
import os
```

### Working with Files
```python
# Basic command
os.rename('name1', 'name2')
os.path.exist('file name')
os.create()
os.remove()
```

### More File Information
```python
os.path.getsize() # file size
os.path.getmtime() # return Unix timestamp

os.path.abspath('spider.txt') # return absolute path
```

```python
import datetime

timestamp = os.path.getmtime('spider.txt')
datetime.datetime.fromtimestamp(timestamp)
>> # datetime.datetime(2020, 1, 6, 7, 2, 3)
```

### Directories
```python
os.mkdir() # make directory
os.rmdir() # remove directory
os.getcwd() # get directory path
os.chdir("new") # change directory

os.listdir() # return directory item in list
os.path.join() # match 2 directory together
```
Split in difference OS
	OS & Linux -> / 
	Windows -> \

### Files & Directories (reading summary)


### [[Pratice Quiz]]


