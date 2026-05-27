+ DictReader ->(Called Element by Name) 
+ Reader        -> (Called Element by Int)
### csv.reader
> Put each Element to a **List**
```python
import csv  
''' CSV: Sort Variable by ROW '''  
with open('NguyenBui.txt') as f:  
	f.readline()  
	csv_F = csv.reader(f) 
for row in csv_F:  
	print()  
	print(row)  
	print('Name: {} - Status: {}'.format(row[0], row[2]))

# ['Mail Tree ', ' 5.34', ' production ', ' 324']
# Name: Mail Tree  - Status:  production 
# 
# ['CalDoor ', ' 1.25.1', ' beta ', ' 22']
# Name: CalDoor  - Status:  beta 
# 
# ['Chatty Chicken', ' 0.34', ' alpha', ' 4']
# Name: Chatty Chicken - Status:  alpha
```
> **Extract Element form Row:** name, phone, role = row
![[Pasted image 20230626181736.png]]
```python
csv.DictReader(file)
software.csv
```
user@ubuntu:-$ cat software.csv
name , version , status , users
Mail Tree , 5.34, production , 324
CalDoor , 1.25.1, beta , 22
Chatty Chicken, 0.34, alpha, 4
user@ubuntu:-$

>**DictReader()** turn each **Row to** a **Dictionary**. 
> **Access Data** by Using the **Column Name** instead of position in the row.
```python
with open('software.csv') as software:
	reader = csv.DictReader(software)
	for row in reader:
		print("{} has {} user".format(row["name"], row["users"]))

# Mail Tree has 324 users
# CalDoor has 22 users
# Chatty Chicken has 4 users
```
>> csv DictReader allow to called variable by name, not by Int like csv.reader() 
```python
import csv  
''' CSV: Sort Variable by ROW '''  
with open('software.txt') as file:  
	csv_file = csv.reader(file)   
	for row in csv_file:  ro
		print('Name: {}'.format(row))
	
# Name: ['name', 'version', 'status', 'users']
# Name: ['Mail Tree ', ' 5.34', ' production ', ' 324']
# Name: ['CalDoor ', ' 1.25.1', ' beta ', ' 22']
# Name: ['Chatty Chicken', ' 0.34', ' alpha', ' 4']
```


### csv.DictWriter(file)
![[Pasted image 20230626150444.png]]
```python 
import csv  
  
users = 
[ 
	 {'name': 'Sol Masil', 'username': 'solm', 'department': 'IT'},  
	 {'name': 'Jacko', 'username': 'Mukka', 'department': 'Labor'},
]  
keys = ['name', 'username', 'department']  
with open('by_department.csv', 'w') as by_department:  
writer = csv.DictWriter(by_department, fieldnames=keys)  
# write & set header in keys to csv file
writer.writeheader()   
# write each item in each dict
writer.writerows(users) 
```
#### **by_department.csv** file (Text / Table Editor)
![[Pasted image 20230626152621.png]]
> ![[Pasted image 20230626152539.png]]





**1. We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents of file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a
dictionary using DictReader.**
> DictReader(file)
```python
import os
import cs

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

  
# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""
  
  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, 'r') as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
      
  return return_string
  
#Call the function

print(contents_of_file("flowers.csv"))
```

**2. Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. How do you skip over the header record with the field names?**
> ele1, ele2, ele3 = row
```python
import os
import csv

  
# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

  

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  

  # Call the function to create the file 
  create_file(filename)

  

  # Open the file
  with open(filename, 'r') as filesss:
    
    # Read the rows of the file
    filesss.readline()
    rows = csv.reader(filesss)

    # Process each row
    for row in rows:
      name, color, types = row
      # Format the return string for data rows only
      return_string += "a {}\n{} is {}\n".format(color, name, types)
  return return_string
  

#Call the function
print(contents_of_file("flowers.csv"))

