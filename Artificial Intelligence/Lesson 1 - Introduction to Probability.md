 `note from Page 175, Mathematics for Machine Learning book`
**The sample space Ω**
	The sample space is the set of all possible outcomes of the experiment, sample space usually denoted by Ω. For example, two successive coin tosses have
	a sample space of {hh, tt, ht, th}, where “h” denotes “heads” and “t”
	denotes “tails”.

**The event space A**
	The event space is the space of potential results of the experiment. A event space
	subset A of the sample space Ω is in the event space A if at the end
	of the experiment we can observe whether a particular outcome ω ∈ Ω
	is in A. The event space A is obtained by considering the collection of
	subsets of Ω, and for discrete probability distributions (Section 6.2.1) A is often the power set of Ω.

**The probability P**
	With each event A ∈ $\Omega$, we associate a number P (A) that measures the
	probability or degree of belief that the event will occur. P (A) is called
	the probability of A.

**Odd** = Total Even happened / Total Even not happened
**Odd Ratio** = Odd of Event happened / Odd of Event not happended  
![[Pasted image 20241018141326.png]]

# What is probability
Say we have 10 kids, 3 kids play soccer, 7 kids don't play soccer. Easily we find out, taking 3 kids out of the total 10 would return the prob for kid's playing soccer.
![[Pasted image 20241003195750.png]]

### Venn Diagram
![[Pasted image 20241003195825.png]]
Represent Sample Space using Diagram and Diagram relationship. An example for diagram relationship is subtract the total kids with kids who play soccer, we left with kids who don't.

### Coin Example
+ ? **Experiment:** activity produce an outcome that is uncertain.
> Flip 2 coin 1 time. Because there only 4 outcome so 1/4 is the prob for each scenario.
![[Pasted image 20241003200756.png]]

If flipping 3 coin, we would have 8, which making each scenario prob is: 1/8.
![[Pasted image 20241003200902.png]]

### Dice Example 
6 Faces -> 1/6 each face
If rolling 2 6 faces dice. The probability for a 6, 6 would be each face dice_1 * each face dice_2. That leave us with 36 faces scenario in total, so the prob will be 1/36. 

### Complement of Probability 
> Probability of the event that not occur.  xác suất bổ sung.
![[Pasted image 20241003210315.png]]


### Sum of Probabilities (Disjoint Event) 
**A Union B**
![[Pasted image 20241003211841.png]]

---
note: 
+ categorical: a discrete random variable or sth continuous.
$T$: target space 
	consider element of T as state

### Bayes Theorem
![[Pasted image 20241004092204.png]]

### **Disjoin Event**
![[Pasted image 20241020135645.png]]
**Mutually Exclusive Event**
> Event that are not related to eachother. Probability of 2 events Happened is its sum.
> $P(A \bigcup B) = P(A) + P(B)$


### **Join Event**
**Non-mutually Exclusive Event**
Example of **prosibilties kid play soccer and basketball**:
>   Total kid is 10, kid play soccer and basketball are 6 and 5 respectively. The goal is to find how many kid that are playing sport, first notice that if we group soccer and basketball together the sum would be over ten, that because there is always are some kids who played both sports, in other word some kids got counted 2 times (Intersect of 2 Event: soccer and basketball)
>   ![[Pasted image 20241020134633.png]]
>   To solve this issue, we simply subtract kids who played both sport given there're 3 of them.
>   ![[Pasted image 20241020135157.png]]
>   **Visualize Answer**
>   ![[Pasted image 20241020135335.png]]![[Pasted image 20241004094448.png]]
+ ? Replace numbers of kids as possibility of kids we got the fomula to calc probabilty kids played sport: ![[Pasted image 20241020135557.png]]


**Disjoint Event vs Joint Events**
![[Pasted image 20241020142455.png]]

**Problem:**  
You roll two dice. Find the probability that either:
- The sum of the dice is 7, or
- The difference between the dice is 1 (e.g., pairs like 1 & 2, 2 & 3, etc.).

**Solution:**
1. **Total possible outcomes:**  
   Rolling two dice has 36 possible outcomes (6 faces on each die, so $6 \times 6 = 36$).

2. **Probability of the difference being 1:**  
   The pairs where the dice differ by 1 are:  
   $$(1,2), (2,3), (3,4), (4,5), (5,6) \quad \text{and the reverse:} \quad (2,1), (3,2), (4,3), (5,4), (6,5)$$  
   That's 10 outcomes in total, so the probability is:  
   $$\frac{10}{36}$$

3. **Probability of the sum being 7:**  
   The pairs where the dice sum to 7 are:  
   $$(1,6), (2,5), (3,4) \quad \text{and the reverse:} \quad (6,1), (5,2), (4,3)$$  
   That's 6 outcomes in total, so the probability is:  
   $$\frac{6}{36}$$

4. **Overlap (both sum = 7 and difference = 1):**  
   Notice that $(3,4)$ and $(4,3)$ appear in both the "sum = 7" and "difference = 1" cases. These are counted twice, so we subtract their probability:  
   $$P(\text{sum=7 and diff=1}) = \frac{2}{36}$$

5. **Final probability (sum = 7 or difference = 1):**  
   Using the inclusion-exclusion principle:  
   $$P(\text{sum=7 or diff=1}) = P(\text{sum=7}) + P(\text{diff=1}) - P(\text{sum=7 and diff=1})$$  
   $$= \frac{6}{36} + \frac{10}{36} - \frac{2}{36} = \frac{14}{36} = \frac{7}{18}$$
![[Pasted image 20241004094605.png]]
```ad-summary
**Simplified Explanation:**
- There are 36 possible outcomes when rolling two dice.
- 10 outcomes have a difference of 1 between the dice, and 6 outcomes have a sum of 7.
- Two outcomes (3,4 and 4,3) fit both conditions, so we subtract them once to avoid double-counting.
- The final probability of getting either a sum of 7 or a difference of 1 is $\frac{7}{18}$.
```

## [[Product of Multiple Independent Events]]
### Independent 
> **Independence event** happens **when the occurrence of one event does not affect the probability of the occurrence of another even.** (opposite of chess)

**Example**
In a school with 100 kids, where 40 like soccer and 60 don't, if we randomly split the kids in two rooms with 30 kids in one room and 70 in other, what is your best estimate on the number of kids in room 1 that like soccer?
-> 40% of the kids being in the 1st room of 30 kids are: 12 kids. (Calc independently with room 2)
-> So 40% of room 2 with 60 kids are: 24 

**Product Rule**: only when A and B are independent
![[Pasted image 20241004104857.png]]
e.g. each coin toss are independet from eachother. (and 2nd coin toss isn't 1/4)
![[Pasted image 20241004104957.png]]



#### Birthday Problem:
> Probability That Everyone Has a Different Birthday
![[Pasted image 20241004110709.png]]

### Conditional Probability - Part 1
>Prob of landing Head twice given the 1st is Head. 
![[Pasted image 20241004111122.png]]
>Conditional Probability - Dice Example 3
![[Pasted image 20241004111412.png]]
+ ? So solve this first we look into the prob of getting 6 is: $\frac{1}{6}$ then we see that there only 1 case where the sum if 6 is 10 (i.e. 6+4=10) thus prob for sum=10 given first roll is 6 is: 1/6.  
>From this example, we can conclude the fomula:
> ![[Pasted image 20241004111534.png]]
> that tell the probability of A intersect B is the probability of A multiply by the probability of B given A happened first.

### Conditional Probability - Part 2
![[Pasted image 20241004112520.png]]
Another way to see this using tree graph
![[Pasted image 20241004112612.png]]

**Independent vs Dependent Events**
+ **Independet event:** event that are not related to eachother
+ **Dependet event:** event occurs given another event occur before it. or 1 event being influent by another event. 

![[Pasted image 20241016170209.png]]


### Exercise: Birthday Problem
> Apply the idea of either happend (n) or not happend (1 - n)

Suppose you want to find the probability of n friend with the same birthday. We know that:
+ the birthday probability of 1 friend  is: $\frac{1}{365}$   
	thus of n friends is $\left( \frac{1}{365} \right)^n$ i.e. n number of fr with the same birthday, this also represent all friend with the same bd. 

**However we need to calc prob of at least 1 std have the same bd not all**
+ Prob of **none student** having the same bd: $1-\frac{1}{365}$ 
	+ So the prob for **none of the n student** have the same birthday is $\left( 1-  \frac{1}{365} \right)^n$ using **complement rule**.
+ Thus the prob of at least 1 friend with the same bd is: $1 - \left( 1- \frac{1}{365} \right)^n$
	**note:** n represent the sample size of a space. e.g. $1 - \left( 1- \frac{1}{365} \right)^n$ so n represent the sample size of $\left( 1- \frac{1}{365} \right)$

##### choose 1 random std , prob having the same birthday with that std:
> This is the same as the problem above.  but the diff is 1 student been chosen, there for n become  n - 1 (all std except for that chosen std). We got: $1 - \left( 1- \frac{1}{365} \right)^{n-1}$
![[Pasted image 20241004101506.png]]
+ note: $ln(a^b)=b⋅ln(a)$, $1-x \approx e^{-x}$

---
**Terms:** 
**relative:** sth relative mean it is dependent on other thing. e.g. relative values are dependent on other numbers. 
**prevalence:** sth that is commo (phổ biến)
**posterior probability**: probability that come after a probability, sth like consequence.

## Bayes Theorem - Intuition 
$$P(E) = P(H)P(E|H) + P(\neg H)P(E|\neg H)$$
In Baye's Theorem, the term $P(E)$ represents the total **probability of event $E$**. This probability can be calculated by considering all the ways in which event $E$ can happen, depending on different conditions (or hypotheses).

**Example:** green farmer, blue, librarian.
![[3Blue1Brown - Bayes theorem, the geometry of changing beliefs [HZGCoVF3YvM - 996x560 - 7m27s].png]]


![[Pasted image 20241004135004.png]]
> (actual sick and diagnoised sick)  / (total people who was diagnoised sick) = $99 / 10098 = 0.0098$
![[Pasted image 20241004135234.png]]

## Bayes Theorem - Mathematical Fomula
![[Pasted image 20241004135726.png]]

For **P(diagnosed sick)** we take the sum of people who diagnoised sick that "sick/not sick" since sick and not sick cannot happend at the same time and not depend on eachother: 
note: $\cap$ mean happened at the same time.
![[Pasted image 20241004140728.png]]
combine with P(sick and diagnoised sick) we got:
![[Pasted image 20241004140804.png]]
![[Pasted image 20241004160134.png]]

---
## [[Monty Hall Problem]]

## Bayes Theorem - Spam Example
0.7 - 70%
0.125 - 12.5%
![[Pasted image 20241004160628.png]]
Actually very simple, we just need to care about the spams. Take the spam email of a Event Space (14) divided with the total spam of the Sample Space (24).
![[Pasted image 20241004161055.png]]
![[Pasted image 20241004161728.png]]
write the answer down to paper.

## Bayes Theorem - Prior and Posterior
+ ? **Prior:** original probability that you can calculate, not knowing anything else.
+ ? **Event**: The event gives you information about the probability.
+ $ With that information, you can calculate something called the posterior
	Examples: ![[Pasted image 20241004162138.png]]
	![[Pasted image 20241004162255.png]]

## Bayes Theorem - The Naive Bayes Model
![[Pasted image 20241004163804.png]]

![[Pasted image 20241004164722.png]]

![[Pasted image 20241016164445.png]]
Is there a faster way?
![[Pasted image 20241025164756.png]]

![[Pasted image 20241025164910.png]]

