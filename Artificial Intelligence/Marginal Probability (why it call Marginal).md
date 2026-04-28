**"marginal" is named after the literal margins of a piece of paper.**

Before computers, statisticians tracked the probabilities of two connected events (like the Weather and the Temperature) using physical grids drawn on paper. This grid of all possible combinations is called a **Joint Probability Distribution**.
![[Pasted image 20260424171953.png]]
If a statistician wanted to ignore the Temperature and just find the overall probability of it being Sunny, they had to add up the entire "Sunny" row (Sunny & Hot + Sunny & Cold). Because the grid was completely filled with numbers, they wrote these final row totals and column totals in the blank white space at the edges of the paper—**the margins**.

Therefore, a "Marginal Probability" is simply the total probability of one single event happening, regardless of any other variables, traditionally found by looking at the margins of the table!
![[Pasted image 20260425155225.png]]
+ @ Basically the Sum of all Possible Scenario of a Event that could happened.

**Discrete conditional probability distributions.**
"Joint Prob" / "Marginal Prob" of that Event.  
![[Pasted image 20260425155749.png]]
Contional Distributions are a way to update our knowledge after we observe part of a system -> that observation *lower the uncertainty in a system (prob for a Event increase)* than before we make that observation. 

In other word, the dimensionality of the problem or number of processes about which were uncertain decreases -> *2D distribution becomes a 1D distribution* or (N)D distribution become (N-1)D distribution. 

## Continous Marginal Distribution
### Continous conditional probability distributions
The fomula is the same as Discrete Conditional Probability Distribtion: "Probability of Bear Volumn given Body Fat = 10" / "The Marginal Probability of the Body Fat = 10". 

The marginal here:
+ $P(B|F=10)$ imagine walking along the line F=10 and keep track of the amount of "energy" (value from B axis) along that part. Because we sample value along the margin of F and B axis, we call it. Continous marginal distribution.
+ is the Sum of all value sample along B if F=10.
![[Pasted image 20260425161626.png | 666]]

### Continous Probability Distributions
When the probability of Event is continous (ie. within a range not discrete) like "temperature, times" we use CPDs ($s$ because there're multiple distribution, the rectangle).
![[Pasted image 20260425153311.png | 666]]
How to estimate CPD ? -> Area of the Rectangle.
Note: 
+ **w.r.t** (with respect to $T$ or $dT$) mean you are **integrating along the $T$ axis.** We calculate the area of the Rectable $H\times W$ so with $P(T)$ as the Height, we want to take account of all value across the $x$ axis to, that where w.r.t $T$ term come in. Kinda like derivative, which said let move X along Y.
+ $\int f(x)dx$ mean summing up these $\infty$ small probability over a range to find the total probability such as $P(a < X <b)=\int^{b}_{a}f(x)dx$ (probability within a range of value)

![[Pasted image 20260425152159.png | 666]]
Marginal Distribution for continous prob can be Obtain by
+ 1st method: *Integrating the Joint Density* with respect to the Nuisance variable (i.e variable were not interested in). 
+ 2nd method: *Appoximate by Sampling* then draw the histogram with respect to only the variable we're interested in. 

### Intro to Central Limit Theorem
Note: if you *sample (i.e inference) a large number of values from a Random Population, those values should resemble a Normally Distribution* (Gaussian Distribution). Even if the original population distribution is not normal. 
	Inference mean repeated samples from that population and calculating the **sample mean** for each one. By doing this, we can understand the underlying characteristics of the population, such as the **true population mean (mu)**.
![[Pasted image 20260425162543.png | 666]]

### Intuition behind Bayesian inference - [source](https://www.youtube.com/watch?v=yvWlpwnT1nw&list=PLwJRxp3blEvZ8AKMXOy0fc0cqT61GsKCG&index=23)
If we transmit a message using our code language which is optimized the language $Q$ for a message for language $P$ then each letter is $\frac{1}{4}$ bit longer than its optimal length - [source](https://www.youtube.com/watch?v=LJwtEaP2xKA&list=PLwJRxp3blEvZ8AKMXOy0fc0cqT61GsKCG&index=34)
![[Pasted image 20260425170252.png]]

### The ideal measure of a model's predictive fit 
![[Pasted image 20260425172120.png]]
ELPF - Expected Log Predictive Density

	