**Keywords:** Monte Carlo, Uniform distribution.

**Binomial Theorem in Pascal's Triangle**
Calc value at line $n=5$, position $r=3$ $\to 5C_{2} = 10$ 
![[Pasted image 20250113143729.png]]
![[Pasted image 20250113143709.png]]

# Permutations and Combinations
![[Pasted image 20250113155032.png]]
>In Permutation the order matter (each pair is unique) so P=12, while in Combination the order doesn't matter (e.g. AB and BA are count as 1) so C=6.


+ **Define Set:** a set is a collection of different things. `e.g. set of letters A = {a,b,c}`
+ **Define Factorial:** product of postive number from n to 1 where notate as `n!`. **In permutation context**, `n!` mean **number of ways a thing can be arrange**.  e.g. `a` is a thing in set `A={a,b,c}`.
+ **Define Permutation:** represent **number of ways a particular set can be arrange**. `e.g. abc, bac, bca, etc...` or simple product of the factorials. 

**Permutation Fomula:**
Say we have 3 slots for `abc`, if we first select 1 slot `_` for `a`, we can arrange `a` in `3` different position, so we say  `a` have permutation of `3`: 
`_ _ _`
Because `a` take up 1 slot , if we select 1 slot for `b`,  `b` can be arrange in `2` different position, so we say `b` have permutation of `2` :
`a _ _`
With `a` and `b` take up 2 slot, there only `1` slot left for `c`, so we say `c` have permutation of `1`:
`a b _`
(This work the same no matter what letters was choose first)
Therefor there are $3 \times 2 \times 1 = 6$ ways to re-arrange `abc` no matter which letters was chosen first because when re-arrange `bca` permute if `b` was chosen first would match `bca` of `c` or `a` if `c` or `a` was chosen first. Simple Right !

Let fo a bit further, if we have 9 letters `{abcdefghi}` the permutation would be $9 \times 8 \times 7$
