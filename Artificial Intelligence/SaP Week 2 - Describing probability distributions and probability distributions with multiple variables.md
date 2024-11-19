# Lesson 1 - Describing Distributions
**Skewness and Kurtosis:** độ lệnh và độ nhọn
**Equilibrium point:** điểm cân bằng
## Expected Value: Discrete Case
**Mean**: **average value of the whole sets (number)**. Rewrite the equation into probability out of 10 for age 0, 1, 2, 3 we got the fomular for Expected Value.
![[Pasted image 20241029142803.png]]

**Expected Value: Motivation Example 1** -  Maximum amount of money to bet for $5 on head.
![[Pasted image 20241029143003.png]]
**Expected Value: Motivation Example 2** - Maximum amount of money to bet where you flip 3 coins and win $1 for each heads. 
-> Flip 3 coins, half of them are head -> 1.5 dollars is the maximum price.
![[Pasted image 20241029143137.png]]

To conclude, $\mathbb{E}[X]$ (i.e. Expected Value) for discrete variable x will have the Probability Mass Function (PMF) that show the probability of each outcome X. The Expected value is the sum of x $(0,1,2,3)$ times the probability of x $\left( \frac{1}{8}, \frac{3}{8}, \frac{3}{8}, \frac{1}{8} \right)$ for all possible values of x $(0, 1, 2, 3)$.   
![[Pasted image 20241029144112.png]]
+ $ To visualize for discrete value, the **Expected Value is** the **Equilibrium point** of the Probability Mass Function. In simple term, average value point. (need to note more detail)
![[Pasted image 20241029145455.png]]
For **continuous variables**, it the **Equilibrium point** of the **Probability Dense Function**
![[Pasted image 20241029150354.png]]

### Example
>You collect data each time you waiting for the bus for many years and its each point of time are filled out (thus it Uniform Distributed) with the average of 30.  
![[Pasted image 20241029150702.png]]
>For Uniform Distribution, $\mathbb{E}[X]$ always locate in the middle point since data are distributed equally. 
![[Pasted image 20241029150846.png]]

**Common Misconception**: Expected value is not the centrel point. It the point where data are balance the most. Spread out data might look small but it bring a heavy punch.

### Other Measure of central tendency
**Median**: Motivation
The average can be very deceiving.
![[Pasted image 20241029152458.png]]

**Outliers**: affect the whole datasets and make it a bit inaccurate. The data got skewed by that one point on the right, to fix that.
![[Pasted image 20241029152844.png]]
Let consider a diff metric. **Put them all in in order by salary**, so now it's **just the position that matters** and the salary in the **middle is the median**. 
![[Pasted image 20241029152916.png]]
Then you continue to take the median of that median (middle point)
![[Pasted image 20241029153251.png]]

**Mode**
+ ? There's one more way to describe the center of a distribution apart from the mean and the median and it's called **the mode**. 
	value with the highest probability.
	![[Pasted image 20241029153432.png]]

**Mode: Multimodel Distribution**
![[Pasted image 20241029153503.png]]

**Examples: Discrete**
![[Pasted image 20241029153554.png]]
![[Pasted image 20241029153638.png]]

**Examples: Continuous**
![[Pasted image 20241029153657.png]]

### Expected value of a Function
Fomular for expected value of a function is similiar to expected value:
![[Pasted image 20241029154045.png]]

Given a dice roll game, you get to roll 1 time. The reward are the double ($\times2$) of the value you rolled. In addition, the enter fee is 5 dollar
![[Pasted image 20241029154624.png]]
So for each win you only win ($\text{rolled value} - 5$)
![[Pasted image 20241029155000.png]]
How much do you win on average?
![[Pasted image 20241029154414.png]]
>Simplified the equation, we see that:
  Expected value is a linear operator. The expected value of constant is the constant itself.

### Sum of expectations
![[Pasted image 20241029155532.png]]
![[Pasted image 20241029155710.png]]
![[Pasted image 20241029155723.png]]

**Game:** There are 8 billion people in the world. There is a bag with their 8 billion names, and each person is given a random name from it.
What is the expected number of correct assignments?
>If there only 3 people's name in the bag, there are 3 corrects out of all permuation the name handed to the right people and its average is 1.
![[Pasted image 20241029160112.png]]
> What about 8 billion peoples? a simpler way to do this is to calc the sum of each people exected value. The result remain 1
![[Pasted image 20241029160509.png]]
> Apply to 8 billion, we got the fomula: $$\mathbb{E}[Matches] = n * \frac{1}{n} = 1$$
> ![[Pasted image 20241029160919.png]]

### Variance
+ ? Expected value, although it tells us a lot about the distribution, it doesn't tell us the whole story. For example, **2 distributions** may have the same **expected value but 1 is very narrow and 1 is wide**. This is **captured by sth called the variance.** 

**Variance Motivation: Measuring Spread**
+ ? One way to think of the idea of spread is how far away the points are from the expected outcome. If the spread is small, you would expect most points to be close to the expected value.![[Pasted image 20241029165355.png]]
> The expected value will always appear at the point at which the positive and negative deviations cancel each other out.  


**Variance Fomula**
![[Pasted image 20241029165436.png]]
**Examples**
![[Pasted image 20241029165717.png]]
![[Pasted image 20241029165753.png]]

**Variance Fomula**
![[Pasted image 20241029170001.png]]
![[Pasted image 20241029170146.png]]
![[Pasted image 20241029170205.png]]

![[Pasted image 20241029170305.png]]

![[Pasted image 20241029170530.png]]
+ ? X is graph above and Y is the graph below. with X = .5 we got Y as 1. 
+ Note: $Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^{2}]=\mathbb{E}[X^{2]}- \mathbb{E}[X]^2$
The deviation for the same outcome where $X=4$ becomes $Y - \mathbb{E}[Y]=(2⋅4−5)−2=1$

