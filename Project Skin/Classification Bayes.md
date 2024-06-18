# Naive Bayes
![[Pasted image 20240618094216.png]]

![[Pasted image 20240618094350.png]]
> Probability of Y given X is the same as [(Prob of X given Y) * (Prop of Y)] / (Prop of X)


![[Pasted image 20240618094809.png]]**Prior P(Y):** Prob of an event before considering *Evidence*
**Posterior P(Y|X):** Prob of an event considering some *Evidence*  (the set of features)
**Evidence  P(X):** Set of features 
**Likelihood P(X|Y):** The Probability of the opposite senario. (Prob of Failures) 

### Let Calc all the variable throught this Example
![[Pasted image 20240618095231.png]]
+ ? First, let compute each case of Y
Given the table with X = {0 ,1, 2} Y = {0, 1} (unique value of X and Y)
We can see Calc the prob of a case like P(Y =0) = Probability of Y = 0 by dividing that case to all case can be happend in the table.
+ **P(Y=0) = 6/10** (bc there're 6 times Y = 0 out of 10 case it have)
+ **P(Y=1) = 4/10** (the same for Y=1)

+ ? Next, we compute the case of X given Y. This mean for every case Y = 1, we see if if (X1, X2) = (0, 2)
 ![[Pasted image 20240618100411.png]]
![[Pasted image 20240618095803.png]]
+ The same for **P(X = (0,2) | Y = 0)**, we have 0

Putting it all together, we'll have:
![[Pasted image 20240618100937.png]]
However, **there a problem in this method. It hard to find that particular combination of X1 and X2** in our dataset. For instance, we **only find 1 case where X = (0, 2) and Y = 1** and we **don't find a single occurance where X = (0,2) and Y = 0**
> if the table have hundreds of value, It very likely we will never encounter some particular combination of features. If we don't find a singal occurance of multiple search combinations then the prob value will always 0 -> can't compare with only 0

+ $ Let's assume X1, X2 are independant (warning, only when features are independent. Hence the name Naive Bäyes )
When the **features are independence, we can calc P(X = (0,2) | Y = 0) by multply the product of P(X,Y) where X have multiple value and each value of X are independen*
![[Pasted image 20240618101634.png]]
+ ! How to dealing with Continuous features (do this later)

# Naive Bayes  Classification
![[Pasted image 20240618104544.png]]

![[Pasted image 20240618103727.png]]

