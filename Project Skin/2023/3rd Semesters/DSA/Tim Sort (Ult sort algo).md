1) **Divide Array** into group
![[Pasted image 20230801102615.png]]

3) **Sort each run individually** with the help of **Insertion Sort**
4) **Merge these runs two-by-two** with **merge method** (of the Merge Sort)


**Performance**:
> the merge method performs very well when the size of the sub-arrays is a power of two, and that is why usually the run size is picked between 32 and 64.


