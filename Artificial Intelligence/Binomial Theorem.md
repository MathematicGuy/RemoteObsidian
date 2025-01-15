**Binomial Theorem in Pascal's Triangle**
Calc value at line $n=5$, position $r=3$ $\to 5C_{2} = 10$ 
![[Pasted image 20250113143729.png]]
![[Pasted image 20250113143709.png]]

# Permutations and Combinations
![[Pasted image 20250113155032.png]]
>In Permutation the order matter (each pair is unique) so P=12, while in Combination the order doesn't matter (e.g. AB and BA are count as 1) so C=6.


+ **Define Set:** a set is a collection of different things. `e.g. set of letters A = {a,b,c}`
+ **Define Factorial:** product of postive number from n to 1 where  `n!` anotate the factorial of n. **In permutation context**, `n!` mean **number of ways a thing can be arrange**.  e.g. `a` is a thing in set `A={a,b,c}`.
+ **Define Permutation:** represent **number of ways a particular set can be arrange**. `e.g. abc, bac, bca, etc...` or simple product of the factorials. 

**Permutation Fomula:**
Say we have 3 slots for `abc`, if we first select 1 slot `_` for `a`, we can arrange `a` in `3` different position, so we say  `a` have permutation of `3`: 
`_ _ _`
Because `a` take up 1 slot , if we select 1 slot for `b`,  `b` can be arrange in `2` different position, so we say `b` have permutation of `2` :
`a _ _`
With `a` and `b` take up 2 slot, there only `1` slot left for `c`, so we say `c` have permutation of `1`:
`a b _`
(This work the same no matter what letters was choose first)
Therefor the total permutation of `abc` is $3 \times 2 \times 1 = 6$ no matter which letters was chosen first. For instance, we would have arrange `bca`, `abc`, etc... no matter `a`, `b` or `c` was chosen first.
-> permutation of `abc` is the factorial of 3 or `3!`. 

Let fo a bit further, what if we have 9 letters `{abcdefghi}` but only have 3 slots `_ _ _`.

---

![[Pasted image 20250114205443.png]]
N = {a,b,c,...,n}
n mean total letters.
k is the number of slots which stored letters in N.

If we have 5 letters and 3 slots. That mean n = 5 and k = 3. 
So there will be 2 left over letters if we try to arrange the first 3 numbers. Say `a,b,c` then `d,e` are left out, thus the permutation will be: $k! \times (n-k)! = 3! \times 2!$ this example basically mean, for each  permutation of `abc`, when we switched 2 slots in `abc` (e.g. `a__`, `b__`, `c__`) , we have 2 permutations for each case., which is number of permutations of `d` and `e`.

**We know** 
The total numbers of ordering is `n!`
![[Pasted image 20250114213814.png]]
Number of ways to arrange `n letters` in `k slots` is:  `k!(n-k)!` 
$$n! = k! \times (n-k)! \times \frac{n!}{k!(n-k)!}$$
where 
![[Pasted image 20250114211948.png]]
thus
![[Pasted image 20250114211944.png]]
**Example of** `a`
![[Pasted image 20250114213824.png]]
