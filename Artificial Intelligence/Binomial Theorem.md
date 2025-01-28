+ ! Note: When **order doesn't matter** divide by $k!(n - k)!$ to **remove duplicate in each choosen pair** hence $k!$, when **order does matter** divide $(n - k)!$ to remove the unchosen slot permutation hence $(n - k)!$ .
+ ? **Permutation** represent **number of times a elements in a list can be re-arrange** $\approx$  **Combination of element can be repeated.**


**Binomial Theorem in Pascal's Triangle**
Calc value at line $n=5$, position $r=3$ $\to 5C_{2} = 10$ 
![[Pasted image 20250113143729.png]]
![[Pasted image 20250113143709.png]]

## Permutations and Combinations
![[Pasted image 20250113155032.png]]
>In Permutation the order matter (each pair is unique) so P=12, while in Combination the order doesn't matter (e.g. AB and BA are count as 1) so C=6.


+ **Define Set:** a set is a collection of different things. `e.g. set of letters A = {a,b,c}`
+ **Define Factorial:** product of postive number from n to 1 where  `n!` anotate the factorial of n. **In permutation context**, `n!` mean **number of ways a thing can be arrange**.  e.g. `a` is a thing in set `A={a,b,c}`.
+ **Define Permutation:** represent **number of ways a particular set can be arrange**. `e.g. abc, acb, bac, bca, cba, cab` or simple product of the factorials. 
**Permutation Fomula:**
Say we have 3 slots for `abc`, if we first select 1 slot `_` for `a`, we can arrange `a` in `3` different position, so we say  `a` have permutation of `3`: 
`_ _ _`
Because `a` take up 1 slot , if we select 1 slot for `b`,  `b` can be arrange in `2` different position, so we say `b` have permutation of `2` :
`a _ _`
With `a` and `b` take up 2 slot, there only `1` slot left for `c`, so we say `c` have permutation of `1`:
`a b _`
(This work the same no matter what letters was choose first)
Therefor the total permutation of `abc` is $3 \times 2 \times 1 = 6$ no matter which letters was chosen first. For instance, we would have arrange `bca`, `abc`, etc... no matter `a`, `b` or `c` was chosen first.
-> permutation of `abc` is the factorial of 3 or `3!`. In other word, $abc$ get **repeated 6 times if order doesn't matter.**


Let fo a bit further, what if we have 5 letters `{abcde}` but only have 3 slots `_ _ _`, as you have guess its `5 x 4 x 3`

---
## Binomial Distribution Intuition 
$$P(X = k) = \begin{pmatrix} 
n \\ k 
\end{pmatrix}.p^{k}.(1-p)^{(n-k)}
$$
**Where:**
+ $\begin{pmatrix}n \\ k\end{pmatrix}=$ number of ways to choose k out of n
+ $p^k=$ probability of $k$ success
+ $(1-p)^{n-k}=$ probability of $n-k$ failures

#### "n choose k" combination
+ $ **"n choose k"** represents the number of ways to choose *k* successes out of *n* trials (i.e. total items), **without considering order.** (e.g. *A, B* the same as *B, A*) (i.e. *order doesn't matter*)
$$\begin{pmatrix}
n \\ k
\end{pmatrix} = \frac{n!}{k!(n-k)!}$$
+ ? Example: From 5 students { A, B, C, D, E } choose 3 students to join the student concil, how many ways to arrange 3 out of 5 students.   

**Steps to Calculate:**
1. Pick out the first person:
	you have 5 choices
2. Now pick the second person:
	After picked 1, there're **4 remaining choices** left.
3. Finally pick the third person:
	After picked 2, you have **3 remaining choices** left.
	
So there $5 \times 4 \times 3 = 60$ ways to pick 3 people if order matters. 
**But since order doesn't matter, we're overcounting**. For every pair of 3 (e.g. A, B, C) we've counted it 6 times (i.e. ABC, ACB, BAC, BCA, CBA, CAB) in other word we overcounted ABC by its permutation -> divide number of ways by ABC permutation.

**Remove the Overcounting**
To fix this, divide by the number of ways (i.e. permuation) to arrange 3 people:
$$\begin{pmatrix}5 \\ 3\end{pmatrix} = \frac{5 \times 4 \times 3!}{3! \times 2!} = \frac{5 \times 4}{2} = 10$$

### But when order does matter we use Permutation
Then **{A, B, C}** is different than **{B, C, A}, {B, A, C}, etc.**
So $\begin{pmatrix}n \\ k\end{pmatrix}$ annotate as $P(n, k)$ represent permutation regular fomula and thus $P(5, 3) = 5 \times 4 \times 3$.  

To make $P(n , k)$ look like "n choose k" combination fomula when "order doesn't matter", we simply multiply "5 x 4 x 3" with "2 x 1" and divided it by "2 x 1":
$$\frac{5 \times 4 \times 3 \times 2 \times 1}{2 \times 1}$$
and well, isn't that just:
$$\frac{5!}{2!} = \frac{5 \times 4 \times 3 \times 2!}{(5 - 3)!} = \frac{5 \times 4 \times 3 \times 2!}{2!}  = 5 \times 4 \times 3 = 60$$
Let's rewrite the $\frac{5!}{2!}$ in fomula format:
$$P(n, k) = \frac{n!}{(n - k)!}$$

To conclude Binomial Distribution fomula have 2 forms:
+ ? 1 when **order matter** (*e.g.* Forming Team of people) $$P(X = k) = \begin{pmatrix}
n \\ k
\end{pmatrix}.p^k(1 - p)^{(n - k)}$$
+ ? 1 when **order doens't matter** (*e.g.* Flipping coin) $$P(X = k) = P(n, k).p^{k}.(1 - p)^{(n - k)}$$ 
**where**
+  $p$ is the success probability
+ $(1 - p)$ is the failure probability
+ $k$ is the number of success trial 
+ $n - k$ is the number of failure trials
**and the first part represent number of trials occured:** 
$$P(n ,k) = \frac{n!}{(n - k)!}$$
$$\begin{pmatrix}n \\ k\end{pmatrix} = \frac{n!}{k!(n - k)!}$$
**and the second part represent probability of success and failure** 
$$p^k(1 - p)^{(n - k)}$$

