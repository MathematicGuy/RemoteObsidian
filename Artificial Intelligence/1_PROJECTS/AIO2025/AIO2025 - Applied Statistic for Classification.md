## Review
### Conditional Independence
Events **A and B are conditionally are independent given C if** and only if:
	$P(AB|C) = P(A|C).P(B|C)$

Note: *independent event -> P(A|B) = P(A)*

## Naive Bayes Classifier (Foundation of Science)
Class: Fail, Pass -> 2 outcome
Features: Confident, Studied, Sick
We can predict the outcome, knowing that the total prob is determind by prob of each features given Pass/Fail class respectively.  

![[Pasted image 20250716142359.png | 290]]

**Posterior probability** is the probability of sth happening given that you've observed some specific data or evidence.  It's calc using Bayes Theorem to reflects how your initial belief (prior probability) is modified by the new information. 

**General Bayes' Theorem Formula:** used to calculate posterior probability)
$$p(R|Co, St, Si) = \frac{p(Co, St, Si|R)p(R)}{p(Co, St, Si)}$$
**which simplified to, given there're 3 features**
$$p(Co = \text{yes}, St = \text{yes}, Si = \text{yes})$$
$$=p(R = \text{pass / fail}|Co = \text{yes}, St = \text{yes}, Si = \text{yes})$$

**Posterior Probability for Pass:** (the same for fail))
$$p(R = \text{pass / fail} | Co = \text{yes}, St = \text{yes}, Si = \text{yes})$$
$$= \frac{p(Co = \text{yes}, St = \text{yes}, Si = \text{yes}|R = \text{pass}) * p(R = \text{pass})}{p(Co = \text{yes}, St = \text{yes}, Si = \text{yes})}$$
**Overview**
![[Pasted image 20250716140524.png# left | 600]]

$p(Co = \text{yes}, St = \text{yes}, Si = \text{yes}|R = \text{pass}) * p(R = \text{pass})$
$= p(Co = \text{yes} | R=\text{pass}) * P(St=\text{yes} | R=\text{pass}) * p(Si = \text{yes} | R=\text{pass})$
*Note:* $p(Co = \text{yes} | R=\text{pass})$ mean `len(Co=Yes) where Result=Pass`
+ ? Fastest way to understand one's code, ask question like "Please give me the desired output for each function".


**Xác định xem vì sao cần train.** 
1) Get the **probability of all features** -> calc conditional_probs.
2) **Retrieve feature's probabilty by index** (e.g. Sunny, Cool, High, String).
3) Using **Naive Bayes to calc posterior probability for YES/NO respectively** from trained data.
4) Using posterior probability from trained_data for prediction given X (features) data.
	
	**Example for Trained Data Posterior Probability**, apply Naives Bayes Theorem we have: 
$$p(R|Co, St, Si) = \frac{p(Co, St, Si|R)p(R)}{p(Co, St, Si)}$$

 
