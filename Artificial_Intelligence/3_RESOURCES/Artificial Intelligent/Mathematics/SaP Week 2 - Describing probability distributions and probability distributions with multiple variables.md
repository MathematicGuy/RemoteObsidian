# Lesson 1 - Describing Distributions
**Skewness and Kurtosis:** độ lệnh và độ nhọn
**Equilibrium point:** điểm cân bằng
+ ? Learn how mean, median and mode describe the center of the distribution, and how variance describes the spread of the distributions. 

## Expected Value: Discrete Case (Mean & Median)
**Mean: average value of the whole sets (number)**. Rewrite the equation into probability out of 10 for age 0, 1, 2, 3 we got the fomular for Expected Value.
![[Pasted image 20241029142803.png]]
+ ? *In Statistic Mean called Expected Value*. Both describe the weighted average of all possible outcomes of a random variable, which **show the average outcome of the experiment.**


**Expected Value: Motivation Example 1** -  Maximum amount of money to bet for $5 on head.
![[Pasted image 20241029143003.png]]

**Expected Value: Motivation Example 2** - Maximum amount of money to bet where you flip 3 coins and win $1 for each heads. 
-> Flip 3 coins, half of them are head -> 1.5 dollars is the maximum price.
![[Pasted image 20241029143137.png]]

To conclude, $\mathbb{E}[X]$ (i.e. Expected Value) for discrete variable x will have the Probability Mass Function (PMF) that show the probability of each outcome X. The Expected value is the sum of x $(0,1,2,3)$ times the probability of x $\left( \frac{1}{8}, \frac{3}{8}, \frac{3}{8}, \frac{1}{8} \right)$ for all possible values of x $(0, 1, 2, 3)$.   
![[Pasted image 20241029144112.png]]
+ $ To visualize for discrete value, the **Expected Value is** the **Equilibrium point** of the Probability Mass Function. In simple term, **average value point** so **if some of the outcome have more weight than other, the average value point will change**.
![[Pasted image 20241029145455.png]]

For **Discrete Variables**, it the **Equilibrium point** of the **Probability Mass Function.**
For **Continuous Variables**, it the **Equilibrium point** of the **Probability Dense Function.**
![[Pasted image 20241029150354.png]]
+ ? For some of you want to revision, the idea behind integrals is that you are summing all the area of rectangle that get thinner and thinner so that in the limit you are adding an **infinite number of very very narrow rectangle.**  

### Example
>You collect data each time you waiting for the bus for many years and its each point of time are filled out (thus it Uniform Distributed) with the average of 30.  
![[Pasted image 20241029150702.png]]
>For Uniform Distribution, $\mathbb{E}[X]$ always locate in the middle point since data are distributed equally. 
![[Pasted image 20241029150846.png]]


![[Pasted image 20250721201921.png|400]]
**Common Misconception**: Expected value is not the center point. It the point where data are balance the most. Spread out data might look small but it bring a heavy punch. This called Outlier, a topic which we will discuss next. 
	The middle point is more refer to the median. Not the Mean

### Other Measure of central tendency
**Median Motivation:** the average can be very deceiving when there are outliers.
![[Pasted image 20241029152458.png]]

**Outliers**: affect the whole datasets and make it inaccurate. The data got skewed by that one point on the right, to fix that let consider a diff metric. 
![[Pasted image 20241029152844.png]]
**Put them all in in order by salary**, so now it's **just the position that matters** and the salary in the **middle is the median**. 
![[Pasted image 20250722155223.png]]
So the moral here is when the average is deceiving, go for the median and you may get a better idea of your data. And **Median definition** is the **middle value in a sorted dataset**.
![[Pasted image 20241029153251.png]]
calculate by the fomula, where $N$ is the len of the data. And $S(N)$ is value at index $N$.
+ odd (e.g. 3,5,7): $median = \frac{N+1}{2}$ 
+ even (e.g. 2,4,6): $median = \left(S\left( \frac{N}{2} \right) + S(\frac{N+1}{2} \right))/2$ (Take 2 numbers because they both in the middle)


**Extra example:** consider the dataset: 1, 2, 3, 4, 100.
**Mean:** (1 + 2 + 3 + 4 + 100) / 5 = 22. The mean is significantly affected by the outlier 100. 
**Median:** The median is not significantly affected by the outlier 100 and represents a more typical value in the dataset. 


**Mode: value with the highest probability ** 
+ ? There's another way to describe the center of a distribution apart from the mean and the median and it's called **the mode**. 
	![[Pasted image 20241029153432.png]]

**Mode: Multimodal (not model) Distribution**
![[Pasted image 20241029153503.png]]

#### Mean, Median and Model in Binomial Distribution where outcomes are evenly distribute
Example with Discrete value where **weight of each outcome are evenly distributed.** 
![[Pasted image 20241029153554.png]]

Example with Discrete value where **weight of each outcome are random.** 
![[Pasted image 20241029153638.png]]
+ Median is where half of the data is to the right and half of the data to the left.
+ Mode will be the highest prob.

**Examples: Continuous**
![[Pasted image 20241029153657.png]]

### Expected value of a Function
Fomular for expected value of a function is similiar to expected value:
![[Pasted image 20241029154045.png]]
+ ? remember, sum of all $p(x)$ equal 1.

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

+ ? Variance và Ứng dụng của nó (tạm thời chỉ giải thích trước, tôi sẽ cho bạn 1 vài ví dụ về ứng dụng của nó trong Machine Learning sau)

### Standard Deviation

![[Pasted image 20250722194607.png]]
Điểm yếu của Variance, trong TH X dùng thước đo là mét để tính. Thì $E[X]$ cũng sx dùng mét và $Var[X]$ sẽ dùng mét bình phương $m^2$. Nên ta cần có 1 thước đo chuẩn hơn để đo đúng mét cho Phương sai mà không bị ảnh hưởng bởi dấu hay bình phương. 
Để đạt được điều này, $\sqrt{Var[X]}$ sẽ là thước đo để do đúng Mét. 
Ta gọi $$std(X) = \sqrt{Var(X)}$$ là độ lệch chuẩn.  

![[Pasted image 20250722195135.png]]

### Everything is nicer when Standard Distribution is 1 
```ad-success
When Standard Distribution is 1, its:
+ Improve ML model convergenec speed (bc smaller number)
+ Improve data comparability bc all data big or small are move into the same scale. This also simplified statistical analysis process for human too
```

![[Pasted image 20250730150659.png|400]]

Note: because Variance is linear, you can take constant out of the Variance. 
Apply the same process for Standard Deviation where $\mu$ is a constant. **That's why dividing by the std means our new variable has a std of 1.**
![[Pasted image 20250730150841.png|555]]

![[Pasted image 20250730151054.png|555]]

### Skewness and Kurtosis (Độ lệch và Độ nhọn): Moments of a Distribution
**Moments of a Distribution:** is the sum th expectations of the variable from 1 to the k. Those will be very useful in a bit.   
+ ? $X^2$ isn't Variance bc its centerlize, but its does related to variance. 
![[Pasted image 20250730151525.png|555]]
+ $ In general, if the varible can take up to $x_1$ to $x_2$, with probability from $p_{1}$ to $p_n$. Then the 1st moment is $p_{i}, x_{i}$, the 2nd $p_{i}, x_{i}^2$, the 3rd is $p_{i}, x_{i}^3$ and so on the k is $p_{i}, x_{i}^k$.  
![[Pasted image 20250730151609.png|555]]

#### Skewness Lottery vs Insurance Example
![[Pasted image 20250730154822.png]]
+ ? But with $X_1^2$ and $X_{2}^2$ are the same, how can we tell them apart ?
+ $ Note that $E[X_{1}^{2}] = p_{1}x_{1}^{2} + \dots + p_{n}x_{n}^k$ and $E[X_{1}^{2}] \neq E[X_{1}]^2$, With Mean = 0, we can simplfied Variance to $E[X^2]=99$. And cubed $X$ to $E[X_1]^3$
![[Pasted image 20250730152340.png|555]]
This way, we not only allow value to be negative, we also **magnified X by Cubed**: $X^3$ to express **Skewness** better in Std. So in summary, the cubeds help us to detect if some value is skewed to the right when $E[X^3]$ is positive, and skewed to the left when negative.

But we still need to standardize. So **after standized and cetered we have 3 cases:**
![[Pasted image 20250730152518.png|555]]
```ad-summary
+ Positive Skewed: if X is larger than the mean and skewed to the right. Std cubed > 0 
+ Not Skewed: if X is close to the mean. Std cubed = 0
+ Negative Skewed: if X is very negative than the mean and skewed to the left. Std cubed < 0.
```

#### Kurtosis: Example

---
# Lesson 2 - Describing Distributions

### Join Distribution Discrete (Distribution of 2 events happened)
+ ? Understand how 2 Probability Distribution create a Join Distribution to calculate the probability for each pairs of events happened at the same time. with 2 examples, 1 for dependent variables and 1 for independent variables.  

#### Join Distribution Discrete for Dependent Variables
2 distribution merge into 1 distribution. But before that, lets start small by asking what is the prob  of a child that is 9 years old and 49 inches tall (not picking, just asking), apply conditional prob then we have 3/10  since there is 3 child that is 49 inches tall if not picking randomly.
![[Pasted image 20250730170157.png|500]]
The probability can be express as
$$P_{xy} = P(x=9, y=49)=\frac{3}{10}$$
If we **graph Age in Years (X) and Inches in Height (Y) into 1 tables**, we have Join Distribution for Height and Age that show the **probability of child Age for these height**.  
![[Pasted image 20250730170712.png|555]]

#### Join Distribution Discrete for Independent Variables
**Example:** map all outcomes for each pair of dices and calc their probability. Because both dices are IID (Independent and Identically Distributed Data) so the prob of all pair of outcome are $\frac{1}{36}$. 
![[Pasted image 20250730171254.png]]

**Example 2:** Probability of the "sum of each outcome"
Join Distribution for Independent Variable like Dice. 
	Where x-axis show the number of dice, y-axis show the sum of dice between a variable x and other dice values (i.e. 1,2,3,4,5,6,7). That why we have a graph with each "sum of dice  outcome" have prob as $1/36$. 
![[Pasted image 20250730165710.png|280]]

### Joint Distribution (Continuous)
![[Pasted image 20250730172743.png|555]]


**Comparison: Discrete Joint Distribution vs Continuous Joint Distribution** -> improve understanding and coherant of why we use 2 of them.
+ Discrete Joint Distribution asssign probability to individual outcomes while Continuous Joint Distribution assign probability to range or interval of possible outcome. 

## Marginal and Conditional Distribution 
### Marginal Distribution
+ ? Marginal Distribution is really just the sum of 1 variables of X or Y within Joint Distribution while completely ignore the other. 
For example in a Joint Distribution of Age and Height,
+ The marginal distribution of Age = 7 will be the probability joint distribution sum of each Height for Age = 7.  
+ The same for marginal distribution of Height = 50. Its just the sum of probability of each Age with height = 50.
![[Pasted image 20250730174800.png]]

Plot the Marginal Distribution of both Age and Height as Heat grid, we could see whether there are more count of children for a specific datapoint. 
![[Pasted image 20250730175636.png|200]]

![[Pasted image 20250730175326.png|555]]
 

**Example 2: Marginal Distribution of Independent Variable (Dice)**
Back to the Dice Joint Distribution example, calculate its marginal distribution:
![[Pasted image 20250730175829.png|555]]

![[Pasted image 20250730180001.png|455]]

https://www.coursera.org/learn/machine-learning-probability-and-statistics/lecture/csZ6s/conditional-distribution