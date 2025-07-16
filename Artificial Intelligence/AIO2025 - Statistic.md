o## Chapter 1: Basic Statistic Definition
What is probability ? probability is likelihood (khả năng xảy ra) of sth to happened, but what is likelihood. 

In statistic, we define probability as a measurement of how likely something to happend heuristically (trực giác), and likelihood describe how likely something to happened base on what actually happend when tested.   
![[Pasted image 20250710164357.png | 500]]

```ad-question
**What the different between Probability and Likelihood ?**

**Probability:** Assume how likely sth to happend (i.e. **prob WITHOUT TESTED**)
+ $ Suppose you have an **unbiased** coin. If you flip the coin, the probability of getting head and a tail is equal, which is 0.5. 
+ ? **When calculating the probability of coin getting heads, you assume that P(head) = 0.5**

|

**Likelihood:** Calc the probability sth actually happened (i.e. **prob AFTER TESTED**)
+ $ However, when calculating the likelihood, you are **trying to find if the model parameter (p = 0.5) is correctly specified or not.**
+ ? The **fact that a coin only lands on heads 14 times out of 50 makes you highly suspicious that the true probability of a coin landing on heads on a given toss is p = 0.5.**
```

**Sample Space - $\Omega$:** is a set of all the possible outcomes of the experiment. Denoted as $\Omega$.
	For example, two successive coin tosses have a sample space of `{hh, tt, ht, th}`, where `h` denotes “heads” and `t` denotes “tails”.
	
**Even $E$:**  is a subset of the sample space $\Omega$, we see **a Event** **as a single possible outcome** within the sample space. For example, `hh` and `tt` is 2 Event within the Sample Space, this can be annotate as $E \in \Omega$     
	
**Even Space $A$** with $E$ as an Event, we call the collection of E (many Events) as a Even Space $A$. Because $E \in \Omega \to A \in \Omega$,. 

**Probaility $P$** with each event $A \in \Omega$, we associate (gán) a number P(A) that measure a degree of belief that the event will occur. P(A) called the probability of A. 

## Chapter 2: Counting Technique (Tổ Hợp và Chỉnh Hợp)



## Chapter 3: Các Quy Tắc Xác Suất Cơ Bản
**Independet Event:** outcome of 1 event doesn't affect outcome of another event.
**Dependent Event:** outcome of 1 event affect outcome of another event. 
Note: Both addition and product can ahve independence or dependent event. 

**When to Use Sum: Addition Rule** 
When you want to **find the probability of either one event OR another event occuring**. (x/s của 1 trong 2 events)

**When to Use Multiply: Prouduct Rule** 
**2 or more events happenning at the same time.** 

## Chapter 4: Xác Suất Có Điều Kiện và Biến Cố Phụ Thuộc:
### Conditional Probability
![[Pasted image 20250714163106.png# left | 250]]
Given B happend first, then A happend mean ONLY choose parts of A that happend given B. We then divided the "intersection between A and B" to B because it how we calculate probability, in other word, out of all events in B, what is the probability A and B happend.  

### Conditional Probability Example
2 Sequential event -> multiply
![[Pasted image 20250714161456.png]]
The reason P(A2 | A1) after P(A1) is because P(A1) had happened. Problem of A standing first annotate its happened first. This rule repeat for $A_n$. 
![[Pasted image 20250714161728.png]]
Say that we only open the door on the 3rd attempt, this mean attempt 1st and 2nd fail and the 2nd attempt is depend on the 1st attempt. 
-> $P(\bar{A_{1}})$ then $P(\bar{A_{2}} | \bar{A_{1}})$ (attempt 2 not success given attempt 1 not success) then $P(A_{3} | \bar{A_{1}} \bar{A_{2}})$ all multiply to each other to describe sequence of events. 
<-> $P(\bar{A_{1}} \bar{A_{2}} A_{3})$ = $P(\bar{A_{1}}).P(\bar{A_{2}} | \bar{A_{1}}).P(A_{3} | \bar{A_{1}} \bar{A_{2}})$
From here we just plug in the numbers.
![[Pasted image 20250714162930.png|600]]


### Bayes Theorem 
**Independent events**
Do event A affect event B ? This mean if we only want to find Prob of B given B so then $P(A|B) = P(B)$  
+ ? For example, A single fair dice is rolled. Let A={4} and B={2, 4, 6} mean B can either be 2 or 4 or 6. Are A and B independent ?
To check if A and B is independent ? We just need to multiply them so see if their probability really intersect. 

Because 4 is in {2,4,6}, we know **In Theory for event A and B both happened the dice must be 4** because 4 exist in both A and B, **in other word P(A).P(B) = P(4)** = 1/6 (prob equal the intersection part).  
**But In Practice (real life), let see if P(A).P(B) really = P(4)** 
With P(A) = 1/6, P(B) = 1/2 (because that the chance of B to happened), P(A).P(B) = 1/12. 
Since 1/12 $\neq$ 1/6, Events A and B is not independent. 


**Total Probability Theorem**
Happened in parallel (event happened independetly) -> Addition
Happened in sequence (event A afect event B) -> Multiply
![[Pasted image 20250714165815.png]]
Step 1: choose bag (3 independent cases)
Step 2: choose read marble from that bag. (depend on which bag get chosen i.e. prob of the bag which is 1/3 since there're 3 bags)
 $\to .75 \times \frac{1}{3} + .60 \times \frac{1}{3} + .45 \times \frac{1}{3} = \frac{1}{3} \times (.75 + .60 + .45) = \frac{P_{1} + P_{2} + P_{3}}{3}$ 
 + ! Warning: this is a simple way to calculate average of the probability, in realife prob of choosing red might be hight because of bias, each P would have their own weight as bag's probability. e.g. $P(red) = \alpha P_{1} + \alpha P_{2} + \alpha P_{3}$ (This call Weighted Average, use when each cases have a diff probability)
![[Pasted image 20250714170609.png]]
A1 is bag 1
P(H1) is the prob of H having red marble, given that A1 get chosen where A1 is the prob of bag 1 getting chosen and H is the prob space where of red marble.  

## Chương 5: Công Thức Xác Suất Toàn Phần.


## Chương 6: Xác Suất Hình Học

p R|Co, St, Si = p Co, St, Si R p(R)
p(Co, St, Si)

$P(R|Co, St, Si) = \frac{P(Co, St, Si | R).P(R)}{P(Co,St,Si)}$

