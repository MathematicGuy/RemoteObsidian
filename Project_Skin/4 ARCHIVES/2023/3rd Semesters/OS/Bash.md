#### Common Question - Terminal vs Shell vs Bash
> **Terminal** is what **run Bash & Shell**


#### Text meaning
**u** - user 
**x** - connect (mean it can be acess)
	**u+x** -> connect u to x
	**u-x** -> detach u from x
**chmod u+x** mean user connect user to (or giving user access to...)
**chmod u+x test.sh** -> give user access to test.sh file
số tương ứng trong bash:
0 -
1 
#### run file from other dict
![[Pasted image 20230831100813.png]]


```
#### Command

```bash
.	# dot mean "at current document, file, etc.." I need this.
# Example: count.sh -> I need shell for this file  
echo  # print()
date  # return date
cal   # return calendar
clear # clear the terminal

cd   # change dir
pwd  # current dir
cd.. # back to the previous dir
ls -l # print detail list of the files
cd ~/filename # back to file



# return to home dir
ls ~ 
cd ~

mkdir   # make dir. Ex: mkdir test is create test folder.
rm      # remove file 

# remove dir
rm -r * 
rmdir

> # Practice: Create a file in a Directory and remove it after editing.


mv  # move. Ex: mv home/text/file.jpg
cp  # copy file

# create file
touch textname.txt 
touch hello.py 
# edit file 
nano textname.txt # create a code file
nano hello.py     # create python file

cat hello.py # return file contents
cat file1.txt file2.txt # show 2 files content
cat > hoa.txt # To enter stup in file. Ctr + D to Save progress.

grep    # find string. Phân biệt chữ hoa vs thường.
grep -i # find string regardless of case

># Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?
>> grep s.ing/usr/file.txt

# use $ to check if it end with a pattern
grep cat$
```

#Pipe
$ls | lpr
# pipe struture
command filename.txt | command for file
 
```python
### Coding with Nanox`
> Attention FirstLine start with: 
> (#! + filepath)
#!/home/user/dir/file.txt 

==Bash run code==
```bash
# use this if permission deny
$chmod usertype + permission filename.py
chmod +x test.sh # asking runs permission
chmod u+x test.sh

./codefile .py   # run file

# String need to have $ upfront
STRING = "Hi You"
cd Uecho $STRING

.. # mean return 1 dir
cd .. # return 1 dir.
cd ../.. # return back 2 dir. 

# rename
mv test.txt test.java
```

> Bash command is difference from alter OS

```
Alt + U -> undo
Alt + E -> redo

^ -> Control[]()

```


### Shell Programming

$ -> nối biến, dữ liệu
  >"  " ->  is code placeholder
> $  -> for get/connect variable
```sh
echo "Nhap so nguyen thu nhat: " # print
read so1 // read and save value to so1
echo "Nhap so nguyen thu hai: " # print
let "tong = so1 + so2" # set tong = "so1 + so2".  
let "tich = so1 * so2" 
echo "Tong cua $so1 va $so2 la: $tong" # callout variables with $
echo "Tich cua $so1 va $so2 la: $tich"
```


Cách **Khai, Gọi ($) và Đọc**   Biến
```sh
let "count = 0"
echo "count equal to: $count"
read count
```


![[Pasted image 20230727102122.png]]


**Array**
```sh
MyList = (one two three four)
echo($MyList) # one
echo ${MyList[@]} # print all of its

array=(0 1 2 3 4 5 6 7 8 9 0 a b c d e f g h)
echo ${array[@]:7}
# 7 8 9 0 a b c d e f g h

```



**ForLoop**
```sh
for item in ${MyList[@]}; do echo -n $item  wc -c; done
# $item the current item
# wc: word count
# -w: command for current file name (who logged in)

for n in AAA CCC DDD
do
	echo $n
done
```


```sh
for Variable in $(); do
	command
done
```

Problem: Ko bik cách khai biến.

Brace expansions may be nested. The results of each expanded string are not sorted; left to right order is preserved. For example,
```sh
bash$ echo a{d,c,b}e
# ade ace abe
```


## translate & run C in Bash 
```bash
// translte java to c
gcc -o test.java test.c 
gcc test.c -o tuan
```
