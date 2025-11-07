### Sample spaces
-> Space for events to happend. If a coin flip, all events (hh, tt,ht, th) that happend are within a sample space. 
Axiom of prob
![[Pasted image 20251107012926.png]]
Prob problem follow this pattern: **identify sample space -> identify events -> apply the law**

**Set Operation**
**Complement rule** change of sth that happend is just chance of 1 - the change of it not happend. 
![[Pasted image 20251107013336.png| 244]]


![[Pasted image 20251107013607.png| 444]]
![[Pasted image 20251107013523.png| 444]]

"not" - use complement, describe sth happend multiple times (power of)
"and" - use intersect
"or" - use addition but watch for overlapped to switch to and. 

But what if the number get astronomical (super many possible/event)
Example - trying to crack a 4-digit lock. 

### Law of total probability
![[Pasted image 20251107014448.png]]

**F2 = Total of Times / (Number of Order Allowed)**
![[Pasted image 20251107014420.png]]
![[Pasted image 20251107015442.png]]

**F3 = Total of Times / ((Different way to arrange repeated order) x (Number of Order Allowed))**
![[Pasted image 20251107014433.png]]
![[Pasted image 20251107015432.png]]


### Conditional probability 
![[Pasted image 20251107015728.png]]
Notice that the one picked first affect the prob of other marble. e.g. if pick blue first then there are only 9 marble total, that mean higher possibility for picking up other marble that have are more.  
-> just think that the universe shrink every time you pick a marble. 
![[Pasted image 20251107015919.png]]
Note that the Numerator (giao) represent all outcome where both A and B happend. 
Denominator P(B) = all outcome of B happend
the division give us the proportion where only B happend without A. Think of a venn diagram. A and B intersect / B -> B without the intersect part. Fomula just a mathematical way to shrink the universe (probability). 
![[Pasted image 20251107020423.png]] 
**Probability Update as you Gain Information**
![[Pasted image 20251107020647.png]]


**Joint Probability -** 2 or multiple events happend together.  
**Margin prob (xs cận biện) -** just Joint probability added up. It called marginal bc its **at the margin of the table ie. total value**. 
![[Pasted image 20251107021034.png]]

How can u tell if 2 events are Connected or Independent ? 
![[Pasted image 20251107021252.png]]

![[Pasted image 20251107021310.png]]
Check Independence -> Check if marginal prob is == joint prob.  
![[Pasted image 20251107021552.png]]
True Independence: A doesn't cost B and revert. 
![[Pasted image 20251107021637.png]]
Causation $\neq$ Correlation.  

### Expected value
![[Pasted image 20251107022034.png]]

![[Pasted image 20251107022628.png]]
Dependencies are completely irrelevant.
![[Pasted image 20251107022615.png]]
+ $ Only work for addition. For multi u need independent.  

### Continuous Prob
![[Pasted image 20251107022846.png]]
-> Mathematical Modeling.
![[Pasted image 20251107023146.png|444]]
![[Pasted image 20251107023203.png|444]]

### Bayes' rule
![[Pasted image 20251107023233.png]]
![[Pasted image 20251107023441.png]]

![[Pasted image 20251107023508.png]]
![[Pasted image 20251107023533.png | 433]]
![[Pasted image 20251107023552.png | 433]]

![[Pasted image 20251107023614.png | 444]]
![[Pasted image 20251107023623.png | 444]]
Bayes Rule is exactly like Rational Thinking. It tell us how much we should update our beliefs when we get new information. 

### Recursion
![[Pasted image 20251107023930.png]]
-> simplified we get E = 2. So the avg is just 2. 

![[Pasted image 20251107024547.png]]
Here where recursion come in, we already know prob of E_H is 1 + (1/2)xE. Just add to the equation E = (1 + (1/2).T + E/2) + 1/2(1 + E/2) = 1+E/2 + 1/2 + E/4 
-> 4E = 4 + 2E + 2 + E  <-> E = 6
(1/2).T mean T more flip for head. Since we assume the first is tail then T=0 i.e. no head. 
![[Pasted image 20251107025233.png]]
Applycation
![[Pasted image 20251107025247.png]]

