**Self-information (Surprise of an outcome)** - *inverse* propotional to probability, hence divided by 1. 
$$I(x)=\log\left( \frac{1}{P(x)} \right)$$
-> *rare event are more suprising* and carried more information (ie. higher $I(x)$). 

**Entropy (Average Suprise)** - basically log-likelihood for *Encode outcome as average bits of Information*
$$H(P)=\sum_{i}P(x_{i})\log\left( \frac{1}{P(x_{i})} \right)$$
-> Expected/Average number of Bits need to encode outcomes using a Optimal code [[Shannon Entropy]].  The more unexpected a event is the more Bits required to encode. 
![[Pasted image 20260412164034.png | 777]]
	
**Cross-Entropy (Average surprise under wrong belief $Q(x_{i})$)**
What if **the code is optimized for another distribution** ? In this case, we would need 1.75 bits of information. 
$$H(P,Q)=\sum_{i}P(x_{i})\log \frac{1}{Q(x_{i})}$$
![[Pasted image 20260412164111.png | 777]]

**KL Divergence (extra cost for wrong belief)** = Extra bits we waste when **measures the Extra cost of using the wrong distribution cue to encode the data** when the data **follow a True Distribution $P(x)$**.  
![[Pasted image 20260412162906.png | 777]]

**Asymmetry in KL divergence** 
Reverse KL punish Q when P = 0 (y-axis) or P is None. Leading to mode-Seeking behaviour in Reverse KL where **Q choose 1 distribution and discard the rest.**  
![[Pasted image 20260412170926.png]]

+ ? Note: One-shot encode the label as the distribution P(x), where only 1 class is True. 
	With 2 distributions, we apply KL Diversion for Q (predict class distribution) and P (True class distribution). 
 Because the True Distribution of the Label is always 1, the 1st term is a constaint. Making the function the same as Cross-Entropy Loss when apply Derivative. Which is what you see in most AI training code.    
![[Pasted image 20260412170634.png]]
$$H(P,Q)=-\sum_{i}P(x_{i})\log Q(x_{i})$$

**Computation Challange for KL Divergence**
In NLP next token prediction task, we need to sum all possible outcome -> Very Expensive. 
![[Pasted image 20260412171347.png]]
For continous distribution, this become even worst (bc -inf to inf)

**Estimate Expectation** using Monte Carlo Estimation.
Let start writing the divergence with the Expectation of log between P and Q. Then apply Monte Carlo Estimation, due to Data Distribution, the more data we have the better the Function Converged.
![[Pasted image 20260412172316.png]]
This Estimation is unbiases -> the more data, the approximation converged to the True KL value.  
![[Pasted image 20260412171850.png]]
+ $ Data is Variance, not Bias
+ ! Some value is negative bc when Q < P log is negatie, probability cannot be negative.

We use a trick by Squaring the log and multiply by 1/2 (the 2 hat and 1/2 cancel eachother as we apply derivation).
+ ! However, this trick prevent KL to converge to the True value (ie. purple line) bc of Bias. 
![[Pasted image 20260412172827.png]]

So, the 1st func is KL's value Variance and 2nd KL's value is bias. Let combine both of them,  ![[Pasted image 20260412173014.png]]Simplified
![[Pasted image 20260412173036.png]]

![[Pasted image 20260412173215.png]]
Achieve Convergencce without Negative side effect.
![[Pasted image 20260412173315.png]]

---

## A Visual and Intuitive Guide to KL-Divergence
**VAE in a Nut Shell** - compress data into latent representation $z$, use $z$ to reconstruct original data. 
![[Pasted image 20260424165235.png | 344]]


**Joint-Distribution**

**KL-Divergence** - measure the different between 2 joint distributions $P(x,y)$ and $Q(x,y)$ by calc the expected log-likelihood ratio -> often used to determine the distance between complex model. 

**Applicaiton in high-dims:** the divergence can be broken down using chain-rule of KL divergence, allowing hierarchical analysis of where the distributions differ.

**KL-Divergence function explain:**
![[Pasted image 20260421204633.png]]
$$L(x)= \mathbb{E}_{q(z|x)}[\log p(x|z)]-KL(q(z|x) \space| \space p(z))$$
+ The 1st term $\mathbb{E}_{q(z|x)}[\log p(x|z)]-KL(q(z|x)$ measure the data consistency -> How well the model can construct the Image $X$ from it Encoded Version $Z$. ![[Pasted image 20260421204831.png]]
+ The 2nd term KL-Divergence act like a Latent space Regularization.

+ ! How to backpropagate through the sampling process ? ![[Pasted image 20260421205129.png]]
Well, *you can, but only* with the *Reparameterization Trick.* Instead of sampling the Random/Gaussian Distribution, we create a random variable $\epsilon$ to handle the randomness outside of the network.  ![[Pasted image 20260421205310.png]]
First, you sample a random point from a standard normal distribution. Then scale it up by the Variane of our approximated posterior distribution and shift by its mean 
![[Pasted image 20260421205349.png | 344]]
-> Just like you just sample a value from the Posterior Distribution, except that by using te reparameterization trick.

The VAE also output the parameters $\mu$ and $\sigma$ of the APD (approximate posterior distribution) 
-> allow we to calc the KL divergence between this posterior distribution and the prior distribution (ie. just 2 normal distribution).  

