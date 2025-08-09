### From Event to Random Variables
![[Pasted image 20250717213431.png]]
+ **Discrete** - Finite number of values (within a range) -> ony take a countable number of values. 
+ **Continous** - Infinite number of values (within a range) -> takes values on an interval, thus there're infinite value within that range. 

**Discrete random variables**: finite number of values (could also be infinite too) 
+ ? Have infinite range of values but only take a countable number of values (e.g. 1,2,3 12313213, 42432423) as long as it countable. 
+ $ represent a List

Continous random variables (Infinite number of values.) 
+ ? Take an entire interval (i.e. infinite range of values), so cannot be put in a list. 
	e.g. all real numbers between 0 and 1: 0, 0.1, 0.2...0.00000001...0.8, 0.9, 1. (there are indeed infinite numbers can be listed out)
+ $ represent a Interval

**Random Variable vs Deterministic Variable**
![[Pasted image 20241028100143.png]]

### Probability Distributions (Discrete)
Flip a coin 32 times and **list out all the outcome in a Histogram**, we have the posibility of all senario, this called **Probability Mass Function (PMF)**. This is define as the probability that the random variable takes at a particular value $p_{X}(x) \geq 0$. 
+ $ Help us to see how the probability distribute among all the variables. In other word, prob of all possible outcome of the experiment.
![[Pasted image 20241028102839.png]]

![[Pasted image 20241028104001.png]]

### Binomial Distribution (Discrete Probability Distribution)
+ ? Binomial Distribution is a **prob distribution that describe the number of success in $n$ independent Bernoulli trials**, each with the same probability of success $p$.
	Note: Bernoulli trials is a single experiment or **event that has exactly 2 possible outcomes**: success (1) or failure (0). 

**An Example:** given 5 coins, there $5!$ total possible outcome.  
![[Pasted image 20241028104232.png]]
$5!:$ number of ways you can order five coins .
	but these 5 coin have repeated numbers, so we need to account for that. 
$2!:$ number of swaps.
	divided 5 factorial by 2 factorial to remove all cases where you have simply swapped the 2 heads. ![[Pasted image 20241028145807.png]] (since swap head1 with head2 doesn't change anything)
$(5 - 2!):$
	Because we just take account for 2 head, we have to remove the case where you have swapped the 2 heads, so as the 3 tail. (order doesn't matter, we just want to calc prob where it 2 heads and 3 tails)
![[Pasted image 20241028145953.png]]

1 common property is that n choose k is the same as n choose n-k, that why the PMF of a fair coin has a symmetric shape.
![[Pasted image 20241028150407.png]]

![[Pasted image 20241028150900.png]]
$$\binom{n}{k} = \frac{n!}{k!(n-k)!} \space\text{ "Counting All Favourable Sequence"}$$  $$p^k(1 - p)^{n-k} \space\text{ "Probability of a Specific Sequence"}$$
**Bernoulli Distribution**
$$\binom{n}{k} p^k(1 - p)^{n-k}$$

By multiplying those, we can calculate all the possible orders with probability of each binomial events. 
![[Pasted image 20241028151612.png]]
**p = 0.5 $\implies$ symmetrical**
![[Pasted image 20241028151647.png]]

![[Pasted image 20250721080053.png]]

**Factorial in Binomial Coefficient Explain**
$k!$ simply show us how to order k different object. 
![[Pasted image 20250721081009.png| 400]]

![[Pasted image 20250721080802.png|600]]
+ ? Note: unorder mean *only take account for different outcome, not different order* 12345 and 54321 is the same and $k!$ take account for that.
	Each time we pick a number we have 1 less option to chose. So **if we want them to be unorder** we have to **divide them to $k!$ which is the number of time those events happened, that being said $(n-k)!$ also need to be divided since it represent number of time those events didn't happened.** That how we calculate all possible outcome for a event with and without order. 

This function work well with logic, for example we was to choose 0 head out of fair coin flip. The only 1 way to don't have any head is to not choose any.
![[Pasted image 20250721082239.png| 400]]


### Probability Distribution (Continuous)
#### From Discrete to Continuous
+ ? As you remember, the sum of all outcome are 1, but you can quickly reliazed if there are infinity outcome, then the probability of each outcome would come closer to 0. (e.g. if there 1000 outcome, each of them would have prob of 1/1000, so the more outcome, the smaller the prob) 
+ $  But we did nothing wrong, it just this distribution is fundamentally different, as it's not discrete, but it is continuous. So this approach will not really work.  
![[Pasted image 20250721134630.png|400]]
As we know, the answer is ZERO.

+ $ So instead of asking what is the probability of the call taking a fixed amount of time like 1,2,3, let's think of it in terms of windows like between 1 and 2, 2 and 3, etc.. (i.e. between value range).
Start example -> divide each time windows (khoảng thời gian) smaller & smaller.
![[Pasted image 20250721140214.png| 400]]
+ ? Think **the call lasts some time between a certain window.** say *0 and 1; 0 and 0.25; 0.25 and 0.5* and continous to divide smaller and smaller etc...![[Pasted image 20241028160642.png]]
Split the interval infinite, we get this curve. Imagine many very very skinny bar represent the probability of each super small interval)
![[Pasted image 20241028161020.png]]
*Basically calculate the sum of the blue area*
**Discrete:** Sum of heights equals 1
**Continuous:** Area under the curve equals 1

### Probability Density Function (PDF - Continous)
When talk about continous distributions, we cannot talk about probability like in throw a coin ten times and 3 of them and heads in a certain number. For example, if I make a phone call, the probability that the phone call lasts exactly two minutes to the dot at is zero.
But I can still talk about intervals. I can talk about the probability that a phone call lasts between two certain interval like $[2, 3]$ minute is $\frac{1}{5}$ 
![[Pasted image 20241028161255.png]]
**Now let split the interval even smaller, with the same reason possibility between 2 and 2.5 is $\frac{1}{10}$.** If you notice the **height of these bar not changing at all, just their width are halved**, this is **bc we're not looking at the heights** of towers instead, **we need to think about areas.**
![[Pasted image 20241028161750.png]]

Let's return to the previous example where the calls are not equally the same lenght (bar represent call frequency). Split the area much more smaller
![[Pasted image 20241028162132.png]]
(Vận dụng tích phân (integral) để tính xác suất trong khoảng 2 - 3 phút)

When the areas become so smaller, the probability at exactly 1 point is Approximatly 0. (Hence prob at 2 minute are 0 at the start). 
> In summary, we divided the intervals into smaller and smaller, also the areas get smaller and smaller until they get to zero.
![[Pasted image 20241028162226.png]]


This called **Probability Density Function (PDF) - $f_x(x)$**, it tells you the **rate you accumulate probability around each point**. Only **defined for continuous variables** and all $f_{x(}x)> 0$ and `Area under the Curve = 1` bc its probability, duh.
![[Pasted image 20250721141407.png]]
You can use the PDF to calc prob by getting the are under the PDF between a specific range, point A and B for example.
$$P(a < X < b) = \text{area under } f_{X}(x)$$

In summary, **Discrete Random Variables take only countable number** of values like a coin toss, dice roll while **Continuos random variable are used to model experiement where the outcome can take any value in an interval** like the probability the call last between 1 to 2 minutes, the person jump height is between 40 to 60 cm.   
+ **To measure the prob of events in discrete random variable**, you have **Probability Mass Function**, which is defined as the **probability that X takes on a particular value.**
+ **For Continuous Random Variable**, you have the **Probability Density Function**, for this type of variable the **probability that the variable takes on a particular value is always 0. So you need to calc the area within a interval**.
![[Pasted image 20250721141821.png]]

### Cumulative Distribution Function
+ ? For **PDF**, you **have to calc areas underneath a curve** in order to find the prob. This is **NOT CONVENIENT**, we don't want to be always calc areas. The *cumulative distribution function (CMF) is one that shows the actual probability that the call is between zero and a certain number of minutes.* (i.e. from start to a particular point)

+ $ **Cumulative property** tells you the **probability that an event happened before some reference point**. Hence why we adding all the probabilities from previous events up to a particular point (i.e. final point). *Like other prob function*, its *total prob of all possible outcomes is 1.*

For example, on the left the prob of the call is between 1 and 2, on the right we're looking at the prob being between 0 and 1, 0 and 2 then 0 and 3, 0 and 4. 
![[Pasted image 20241028163224.png]]

The *different between PDF and CDF* is 
+ **PDF** tells the prob **between an interval under the curve** 
+ **CDF** tells the sum of the interval, which is the **sum of the area under the curve**. 
+ ? CDF have the limit between 0 and 1, while PDF can be go infinitely to the left and right. 
![[Pasted image 20250721145933.png]]


**Cumulative Distribution Function (CDF): Formal Definition**
In short, the CDF tells you how much prob a random variable accumulates up to a certain value. So the cdf is actually the probability a random variable x is smaller than or equal to some value x.
(where the function planks - hàm đạt đến điểm dừng)
Define as $F_{X}(x)$, unlike PDF written in $f$. 
![[Pasted image 20241028165015.png]]


> never decrease since it's accumulating probabilities and probabilities can never be negative. 
![[Pasted image 20241028165226.png]]

[Interactive tools for Distribution model](https://www.coursera.org/learn/machine-learning-probability-and-statistics/supplement/5mYZm/interactive-tool-relationship-between-pmf-pdf-and-cdf-of-some-distributions) 

### Uniform Distribution
Uniform Distribution look homogeneous within a time interval. 
+ ? **Used when all outcome within a specific range are equally likely.** For example, random numbers are drawn from a Uniform Distribution to simulate random behaviour. Uniform Distribution **help model scenarios where each outcome within a specified range is equally likely** and it provides a solid foundation for applications in *random sampling, quality control and simulations*.

Imagine that **a call center can answer in anytime from 0-15 minutes with equal probability**. If they don't answer within 15 minutes, the call is disconnected. The **last 200 times you call them, you made a note of how much time you had to wait. Notice** that **the points seem to be more or less equally distributed over the y-axis.**
(Some deviation is expected since this is base on measurement)
![[Pasted image 20250721151725.png| 600]]

**Uniform Distribution: Motivation**
![[Pasted image 20241028165829.png]]
Call T, the time in minutes that you have to wait and any value between 0 and 15 should have roughly the same frequency of occurrence. Which means that the PDF must be constant on the interval 0-15, so no value is favored over the others.
+ $ The area under the curve must be 1 so that times 15 is the length of the interval. Therefor the height is 1/15 or 0.06.   

**Uniform Distribution: Model**
+ ? All points outside the interval a and b are zeros. 
![[Pasted image 20241028170137.png]]

**CDF of Uniform Distribution**
![[Pasted image 20241028170413.png]]
> As expected, CDF represent only the accumualate probability between the starting point 0 and ending point 1. if x < 0, it 0 because nothing happened, if $x \geq 1$ then it just 1 since that the maximum accumulative point.


For the **general uniform distribution between a and b**, you can see that the **CDF is the ratio between the length of the segment ax and the length between the extreme values a and b**. For values of x between a and b, for x less than a, you have 0 cumulative probability. Again, for x bigger than b, you've already gathered all the probability, so therefore, the CDF is 1 after that point.
![[Pasted image 20241028171224.png]]

### Example of CDF:
If we take the interval $[1, 10]$ and calculate the CDF at $x = 5$:
$$F(5) = \frac{5 - 1}{10 - 1} = \frac{4}{9}$$

### Normal Distribution
> Normal Distribution or **Gaussian Distribution** name after famous mathematician Carl Gauss. The most common Distribution which appear in statistics, in science, in machine learning, everywhere. 

When n is very large, Gaussian Distribution represent a bell curve. As **Normal Distribution is a nature order** (quy luật trong tự nhiên) founded by Gaus, we could **try to use a function to fit this curve.**  
![[Pasted image 20241028172314.png]]

**1) Use a function that resemble the Bell Shaped Data (before reshaping it)**
The function (in orange) $$e^{-\frac{x^2}{2}}$$seem to **work really well**, so we will use it as our **base function to fit/model the bell curve.**
![[Pasted image 20250721155059.png|500]]
Our **base function start from the center of the x-axis** with $x=0.0$ represented as $\mu=0$. 
So to *move our function closer to the center of the data in the right* where $\mu=2$ we substract $x$ by $\mu$ $$(x-\mu)^{2}= (2-0)^{2} = 4$$
The width of the bell curve is quite skinny, we can **widen it a bit using Standard Deviation** notate as $\sigma$. **This tell us how thick the curve is.** 
![[Pasted image 20241028172601.png]]
The way we **thicken the curve is by dividing the exponent** by $\sigma$. Now the only problem we have is the Height.
![[Pasted image 20241028172724.png]]

The **area under the blue curve is 1 because it's probability distribution** and given the Areas of the Data is $3\sqrt{ 2\pi}$.  

![[Pasted image 20241028172752.png]]
We can get the right curve by divide the Big Curve (Bell curve) to the Small Curve (Data) (Diện tích 2 hình chia cho nhau).

![[Pasted image 20250721160009.png]]

![[Pasted image 20241028173045.png]]

Replace values with parameters $\sigma$ and $\mu$ we get Gaussian Distribution:
![[Pasted image 20241028173133.png]]

![[Pasted image 20241029091723.png]]
$\mu$ center of the bell (Mean, center of the bell)
$\sigma$ spread of the bell (standard distribution)
$\sigma^2$ variance.
$\frac{1}{\sqrt{ 2\pi }\sigma}$ scaling constant

Normal Distribution *can be rewrite as*
$$X \approx N(\mu, \sigma^2)$$
As Standard Normal Distribution center around 0. We can simplified the function into:
![[Pasted image 20250721160619.png|500]]

### Standardization
Convert any **normal distribution to the standard one**
![[Pasted image 20250721160902.png|250]]
$\mu$ to re-adjust Function center. 
$\sigma$ to re-scale the function height.

![[Pasted image 20241029094231.png|500]]
> Help to compare 2 variable with completely different range of values.

![[Pasted image 20250721160944.png|500]]


**Computing Distribution Applications**: weight, height, IQ. Also many ML models assume variables follow a normal distribution.  In general, characteristics that are sum of many independent processes. 

---

### Chi-Square Distribution
Call the noise $Z$.  
![[Pasted image 20241029094756.png]]

**Chi Square Distribution with 1 Degree of Freedom** 
![[Pasted image 20241029094844.png]]
+ $ Each value of W (each dots on the right) can be achieved with 2 diff values of Z (Interval of Z on the left), which are negative square root of W and W. 
+ $ Even more, the probability that capital W's and W, is the area under the PDF curve on the Gaussian between these $-\sqrt{w}$ and $\sqrt{w}$.
+ ? **W** (right) curve **increase slower and slower bc the areas under Z intervals are getting smaller and smaller.**
Since CDF (Accumulative Distribution Func) is integral of the PDF (Probability Distribution Func), then you can easily find the PDF by taking the derivative of the CDF. 

![[Pasted image 20241029101130.png]]
Since the CDF is the integral of the PDF, then you can easily find the PDF by taking the derivative of the CDF (Chi-Square Distribution Func). 
+ ? We see the rate of change of at which **the probability w** is accumulated is big for small values of w and get smaller and smaller as W increase , the reason is the **steep curve grow very quickly for small values of w and grows slower and slower for larger value of w.** (check question mark above)

**What about Accumulated power over 2 transmissions and n transmission?**
![[Pasted image 20241029102642.png]]
*df: degree of freedom*
+ $ The sum of Chi-Square represent Chi-Square with k degree of freedom. As **k increase,the PDF is more spread and becomes more and more symmetrical.**
  ![[Pasted image 20241029102910.png]]


### Sampling from a Distribution (lấy mẫu từ phân phối)
+ ! Can't go collect more data, it's too expensive -> **Create synthetic data that looks a lot like the original one.** 
+ ? One way to do this is to construct a distribution out of this data and then sample it out. By sampling, it mean **picking points that have the probabilities given by the original distribution.** 

**How to sample datas from distribution?**
![[Pasted image 20241029110346.png]]

**CDF the Sample**
Let **plot the (3 colors) interval vertically and set them up as CDF. Choose 4 points sampled uniformly**, along these 4 points you simply pickout out **what the value is in the horizontal axis of the CDF**   
![[Pasted image 20241029110443.png]]

**Sampling from a Normal Distribution**
![[Pasted image 20241029110842.png]]

---
A = P(sick) diese / whole population = 1%
B = P(test positive | sick) =  95%
not A = P(test positive | sick) =  95%

$$p(A|B)=\frac{P(B|A)P(A)}{P(B)}=\frac{P(B|A)P(A)}{P(B)}$$
1 - B = 5%

![[Pasted image 20241029120207.png]]![[Pasted image 20241029120243.png]]
![[Pasted image 20241029120253.png]]

