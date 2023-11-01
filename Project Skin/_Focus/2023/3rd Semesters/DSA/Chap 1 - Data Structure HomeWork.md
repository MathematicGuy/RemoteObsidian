![[Pasted image 20230705212823.png]]
Mỗi TH (list) sẽ được in 1 lần 
Mỗi hàng sẽ có giai thừa TH chưa được Hoán Vị. 4 * 3 * 2 * 1 = 24 
=>  Vậy độ phức tập thời gian là: O(n *  n!)

### Có 2 quy tắc

+ Hoán vị  phần tử hiện tại với các phần tử còn lại.
+ Chỉ hoán vị với những phần tử chưa đc hoán vị.

=> Lấy Hoán Vị ở hàng cuối cùng.

## Permutation
(a,b,c)
1) Box to store all the Permutation 
2) Contain each permutation in a list
3) Swap each element in the list.
4)  Hoán vị các phần tử vs phần tử đầu tiên trong list. List đã hoán vị trở thành 1 list mới 
5)  Lặp lại bước (4) với mỗi List mới.
6) Lặp lại 2n lần (n là số phần tử trong list. 2n tổng thời gian chạy hết vòng lặp)
Total Permutation cases (6):
	(a,b,c)   
	(b,a,c)   |  (c,b,a)  
	(b,c,a)   |  (c,a,b)  

Time Complexity: ( Time to print 1 permutation * Number of Permutation)
>> **O( n * n ! )**

##### Algorithm
> Phân tích các bước thành các bước bé hơn.

![[Pasted image 20230706134046.png]]


##### Code

> No RECURSION.
```cs
def permute_without_recursion(sequence):
    # permutation inside []
    permutations = [[]]  # Start with an empty permutation
    for current in sequence:
        new_permutations = []
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                new_permutation = permutation[:i] + [current] + permutation[i:]
                new_permutations.append(new_permutation)
        permutations = new_permutations

    return permutations

# Example usage
input_sequence = [1, 2, 3]
permutations = permute_without_recursion(input_sequence) # input
print(permutations)

```


## ![[Permutation Time Compexity test]]
