
```cs
def permutation(word):  
if len(word) == 1:  
return [word]  
  
perms = permutation(word[1:])  
char = word[0]  
result = []  
  
for perm in perms:  
for i in range(len(perm) + 1):  
result.append(perm[:i] + char + perm[i:])  
return result  
  
  
def permute_without_recursion(sequence):  
perms = [[]] # Start with an empty permutation  
for current in sequence:  
new_perms = []  
for permutation in perms:  
for i in range(len(permutation) + 1):  
new_permutation = permutation[:i] + [current] + permutation[i:]  
new_perms.append(new_permutation)  
perms = new_perms  
  
return perms  
  
perms = permute_without_recursion(['a', 'b', 'c'])  
  
perms = permutation('12345678910')  
print(perms)  
print(len(perms))
```


