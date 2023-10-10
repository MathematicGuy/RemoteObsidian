
## Regular Expressions (regex or regexp)
> **Allow us to search a text for strings matching a specific pattern**

+ **grep**
	https://youtube.com/shorts/5_t_I_4OuwQ?feature=share
+ **sed**
+ **awk**

##### Why use regular expressions ?
> getting info out of a stack of strings
```python
log = "jujy 20 2004 -03; 393 ijdlkjf39933m0 [21244]: ERROR preforming package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log) # KeyConcept: search for regex in log
print(result[1])
```


##### grep command
```sh
grep    # find string. Phân biệt chữ hoa vs thường.
grep -i # find string regardless of case

># Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?
>> grep s.ing/usr/file.txt

# use $ to check if it end with a pattern
grep cat$
```


#### Regex (biểu thức chính quy)
```python
# use re module
re.grep() # find key word. detect lower case + upper case 
re.match() # find the match
re.search() # find all matches for a predefinded regular expression
re.findall()

# circumflex
[^]
# dollar sign
[$] 
# singe character pattern 
r.g 
grep r.g # find the pattern that have r->g

>> # The circumflex and the dollar sign specifically match the start and end of a line or string, but not necessarily the words themselves.
```


## Basic Regular Expression
```python
import re
```


```python
def check_aei (text):
	# check what between a and e and i
	result = re.search(r"a.e.i", text) 
	# ignore cases
	result2 = re.search(r"a.e.i", text, re.IGNORECASE) 

	return result != None # if there no char or 1 char return False 

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

```


### Wildcards and Character Classes

> Space does present a character.
```python
# Search the char a to z for first char then find the next chars.
# span(begin index, end index) of searchs character.

# True
print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'> 

# False, bc a and way have a space betwen
print(re.search(r"[a-z]way", "What a way to go")) 
# None
```


**Exercise: Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.**
```python
def check_punctuation(text):
	# check every char between []
    result = re.search("[,.:;?!]",text) 
    return result != None

# True
print(check_punctuation("This is a sentence that ends with a period.")) 
# False
print(check_punctuation("This is a sentence fragment without a period")) 
# True
print(check_punctuation("Aren't regular expressions awesome?")) 
# True
print(check_punctuation("Wow! We're really picking up some steam now!")) 
# False
print(check_punctuation("End of the line")) 
``` 


**Substring**
```python
# str1 | str 2 -> str1 or str 2
print(re.search(r"cat | dog", "I like cats")) # check if cat or dog.

# if there're cat and dog. Only search the first one
print(re.search(r"cat | dog", "I like dogs and cats")) 

# can search both cat & dog
print(re.findall(r"cat | dog", "I like dogs and cats")) 

```


### Repetition Qualifiers

**Repeated matches** (dots followed by a star ->  .* )
```python
# search Py then as many n as possible. return index of py -> last n
print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>
```


**Connected matches**
```python
# True if there is "ol" (o and l)
print(re.search(r"o+l+", "lsssalotol"))
```


**Exercise: The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work.**
```python
import re
def repeating_letter_a(text):
  result = re.search(r"[a|A].*[a|A]", text)
  return result != None

# True
print(repeating_letter_a("banana")) 
# False
print(repeating_letter_a("pineapple")) 
# True
print(repeating_letter_a("Animal Kingdom")) 
# True
print(repeating_letter_a("A is for apple")) 
```
> Conclusion:
>  |          mean **OR** 
> .*         mean **And** and **Repeat**
> ?          means 0 or 1 occurence of the char before or after it.
```python
# True
print(re.search(r"h?rny?", "I love to be horny")) # 1 char before ? 
# False
print(re.search(r"ho?ny?", "I love to be horny")) # 2 char before ?
# True
print(re.search(r"hor?y?", "I love to be hor?y")) # 1 char after ?
```


? what about match dollars sign and question mark?
### Escaping Characters

> Dùng để kiểm tra các space tạo ra bởi tab, xuống dòng và các từ thông dụng.
```python
/n : # break line
/t : # Tab
/w : # represent any alphanumeric character (all alphabet chars)
/d # digits
/s : # white space chars
/b : # word boundary

# EX:
import re

print(re.search(r".com", "welcome"))

result = re.search(r"\w*", "This is an example") # return single word
# <re.Match object; span=(0, 4), match='This'>

result = re.search(r"\w", "This is an example") # return single char
# <re.Match object; span=(0, 1), match='T'>
print(result)
```
> Ký tự có gạch chéo (/) nghĩa là nó có thể là 1 biểu thức chính quy hay 1 từ đặc biệt (gạch )
![[Pasted image 20230727054840.png]]

#### In regex, what does "[\w* ]" mean?
> **Quick answer:** `^[\w*]$` will match a string consisting of a single character, where that character is alphanumeric (letters, numbers) an underscore ( _ ) or an asterisk ( * ).

**Details:**
 > - The "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus underscore (_)
> - The " ^ "anchors" to the beginning of a string, and the " $ " anchors" To the end of a string, which means that, in this case, the match must start at the beginning of a string and end at the end of the string.
> - The `[]` means a character class, which means "match any character contained in the character class".

> It is also worth mentioning that normal quoting and escaping rules for strings make it very difficult to enter regular expressions (all the backslashes would need to be escaped with additional backslashes), so in Python there is a special notation which has its own special quoting rules that allow for all of the backslashes to be interpreted properly, and that is what the " r " at the beginning is for.

> **Note:** Normally an asterisk ( * ) means "0 or more of the previous thing" but in the example above, it does _not_ have that meaning, since the asterisk is _inside_ of the character class, so it loses its "special-ness".


**Exercise: Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.**
```python
import re
def check_character_groups(text):
  result = re.search(r"\w\s+\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
```

## Advanced Regular Expressions





## Module Review 