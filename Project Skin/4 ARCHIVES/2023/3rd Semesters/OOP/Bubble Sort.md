
  
> Imagine bubble rise on top then stack its to one side  
 Pick first value. Until the end:  
	 a. If the next value is larger or equal, pick that value.  b. If the next value is smaller swap values.  

```python
def BubbleSort(lts):
    # create a border seize for each next number
    # len(lts) - 1 to make room for adjacent numbers
    for border in range(len(lts) - 1, 0, -1):  
        for current_pos in range(border):
            adjacent_pos = current_pos + 1
            if lts[current_pos] >= lts[adjacent_pos]:
                lts[current_pos], lts[adjacent_pos] =                                        lts[adjacent_pos], lts[current_pos]
    return lts

bs = BubbleSort(lts=list_to_sort)
print(bs)
```