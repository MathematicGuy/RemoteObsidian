Link quiz: [https://forms.gle/CjtyUMSXB4UL2J3g6](https://forms.gle/CjtyUMSXB4UL2J3g6)
![[Pasted image 20260421202237.png | 666]]
The Variational Autoencoder latent space is continuous. It provides random sampling and interpolation. Instead of outputting a vector of size n, the encoder outputs two vectors:

[Traditional VAE + ResidualConnection Code](https://colab.research.google.com/drive/1PBSaiQ2sf2dBtCiUrFsA52tAS1ggwvUK#scrollTo=owJFXtc-8XfG)
*Understand underlying ideas of VAE*
	basic udstand of *traditional Autoencoder.*
	Basic Prob concept -> Kullback Leibler divergence.
[Clear Explaination of VAE KL-Divergence Loss - Medium](https://medium.com/@jpark7/finally-a-clear-derivation-of-the-vae-kl-loss-4cb38d2e47b3)

	
*VAE and Dropout (DON'T)*: VAEs already have built-in regularization via the KL-divergence term in the loss function, which helps prevent overfitting. [visualization](https://bleyddyn.github.io/2020-01-14-vae-dropout)

*Apply Masking in VAE ?*

---

in this formula we have $\tilde{x}^{(i)}$ and not our original $x$. This means that *our input is a partially destroyed input image (a noisy image).*
$$\tilde{x}^{(i)} \approx X(\tilde{x}^{(i)}|x^{(i)})$$
Like Dropout which drop neuron in a NN, adding noise to the image act like a regulariaztion term that prevents VAE from overfitting when reconstructing image.
$$L(\theta, \phi) = \frac{1}{N} \sum_{i=1}^{N} \left[ x^{(i)} - f_{\theta} \left( g_{\phi} \left( \tilde{x}^{(i)} \right) \right) \right]^2$$


Different from trad Autoencoder, VAE don't have a bottleneck vector.
**In contrast, we have a so-called probabilistic encoder where the function $q_{\phi}$ is now given as a conditional probability.**
![[Pasted image 20260422220035.png]]

**Prerequisites of probability theory for Variational Autoencoders:**
1. We are going to start with the basic concept which is **The probability of a random variable $P(X)$**. 
- Then, we will have a **Conditional probability** of $X$ given a random variable $Y (P(X|Y))$
- Next, we have an operation – **Mathematical expectation $E$**. 
- Finally, we will explain **KL Divergence** which is more advanced concept.

**The Bayes’ theorem:**
![[Pasted image 20260422220517.png]]
+ $X$ is the Evidence, $Y$ is the Hypothesis.
+ Likelihood or Joint Distribution $P(X|Y).P(Y)$ said what is the chance X given Y, and because Y happened we multiply by $P(Y)$ 
	-> simplified $P(X,Y)$
	$P(X)$ as marginal ([[Marginal Probability (why it call Marginal)]]) - *probability of the Evidence*, under any circumstance. ie. reflect the degree to which the data support the overall model.
	
+ Prior Probability $P(Y)$ probability *before the evidence* is considered.
+ Posterior Probability $P(Y|X)$ - *updated probability after the evidence* is considered.


![[Pasted image 20260422222413.png]]
The **likelihood ratio $\frac{P(B|A)}{P(B)}$** act as the **"Surprise/ Belief and Evidence Multiplier"**, it compares 2 things:
1. $P(B|A)$ how likely is this evidence $B$ if our theory $A$ is true
2. $P(B)$ how common is this evidence $B$ just happening randomly on its own ?

Okay, for simplicity, If $P(A)$ is the prob that for "Wet Grass" and $P(B)$ is the probability for "Raining", then $P(B|A)$ is the probability for "The Grass is Wet given its Raining". And $Z$ is the probability space (yes, I just name it) ![[Pasted image 20260422224027.png | 444]]
*Intuitionly explain why $\frac{P(B|A)}{P(B)}$ is the Belief/Evidence Multiplier* 
First, divide in probability is like comparing event or a scaling factor, like What is the chance of $P(B|A)$ to happened compare to $P(B)$. For example:
+ *example 1 -* If the chance of Rain given Wet Grass $P(B|A)$ is 0.2 and the chance of rain $P(B)$ is 0.8 $\leftrightarrow \frac{0.2}{0.8}=\frac{1}{4}$, it would mean "Rain" is *LESS* likely to happend 4 times than normally *given the Evidence that the Grass is Wet.*
+ *example 2 -* If the chance of Rain given Wet Grass $P(B|A)$ is 0.8 and the chance of rain $P(B)$ is 0.2 $\leftrightarrow \frac{0.8}{0.2}=4$, it would mean "Rain" is *MORE* likely to happend 4 times than normally *given the Evidence that Grass is Wet.* 
$\to$ This Perfectly make sense for a Belief Multiplier, say the Grass is inside your house.
+ *In the example 1 (Wet Grass because it Rain is LOW)* if your Grass is NOT WET every RAINY day, your belief and the probability of "Rain given Grass is Wet" wouldn't increase much, because most day showed that "Rain isn't always equivalent to Grass is Wet".    
+ *In the example 2 (Wet Grass because it Rain is HIGH)* if your Grass is NOT WET every NORMAL day but WET mostly on RAINY day. It would absolutely increase your belief that "THE GRASS is most likely WET because it RAIN" (belief A1) in other word "IT RAIN because the Grass is WET" (belief A2).
$\to$ This make even more sense because of Bayes' Theorem say the 2 term (ie. A1 and A2) is equivalent (ie. calculating *$\frac{P(B|A)}{P(B)}$ give the exact multiplier number as calculating $\frac{P(A|B)}{P(A)}$*)
	(the First - multiplier for Wet Grass if "Wet Grass given Rain" is Rare)
	is the same as 
	(the Second - multiplier for Rain if "Rain given Wet Grass" is Rare)
+ @ In short in $\frac{P(B|A)}{P(B)}$, if the chance of *RAIN (event $B$) occur because of Wet Grass (event $A$) is HIGHs, and the sky is NOT ALWAYS RAIN (ie. event B is RARE).* When it *suddendly RAIN, it would a huge Evidence and Belief and increase the robability that the GRASS is WET (event A) is HIGH, hence Multiplier for $P(A)$ $\frac{P(B|A)*P(A)}{P(B)}$* 
**$\to$ Rare events = High Surprise = Massive Information**

**Mutual Exclusive Event** mean *2 events CAN'T OCCUR TOGETHER.* 
$P(A \text{ and } B)=0$![[Pasted image 20260424161929.png | 355]]Examples include flipping a coin (heads/tails), because there's *no possible way to flip a coin and head it land as both heads and tails.* 
	$P(A \text{ or } B)=P(A)+P(B)$

**Independent Event (not mutual exclusive)** - occurence of one event doesn't affect the occurence of another event. e.g. Prob of you Cooking and the sky Raining. ![[Pasted image 20260424162317.png | 355]]
![[Pasted image 20260424170919.png | 444]]
+ @ VAE in a nutshell is just Joint Distribution where we find $p_{\theta}(z)$ (like $\theta$ in MLP) to reconstruct original image $x$ using Decoder $p_{\theta}(x|z)$. 
+ ?  Joint Distirbution as like the Chain Rule of probability 
$$P_{\theta}(z,x)=p_{\theta}(z).p_{\theta}(x|z)$$
We don't know how $z$ is distributed so we just use Gaussian Distribution $\mathcal{N}(0,1)$  

Given this factorization we can see that the VAE is encouraged to map the full data distribution $D$ to produce realistic synthetic examples in data space. 

But for that we have to maximize our original Target $p_{\theta}(x)$ and now this can only be found by **integrating The Joint probability distribution over all possible values of Z in other words by marginalizing over Z.** 
![[Pasted image 20260424172544.png | 444]]

*What is Marginal you ask,* first let understand Discrete Marginal Probability [[Marginal Probability (why it call Marginal)]] then there Continuous Marginal Probability because z from P of X ie. $p_{\theta}(z)$ is sample from Gaussian Distribution so there are an $\infty$ variable for sampled from. 

Because it $\infty$ you couldn't use $\sum$ symbol so in calculus we use integral $\int$ for "adding up an infinite number of sample or infinitely tiny possibilities. *So you STILL writing the total in the margins but your grid just has an $\infty$ number of columns.* 
![[Pasted image 20260425145031.png]]

Numerical integration techniques we'd require a number of samples that increases exponentially with the number of latent variables so we can't do this in cases.

VAE realized we don't need to compute P of X itself, we just need some way of increasing it as much as we can for the examples in our data set and it does this within a Baysian framework

Adapt Bayes rule to our Hypothesis - 
![[Pasted image 20260424170658.png | 444]]
Find theta for which the right hand size (Generation) to be maximize.
![[Pasted image 20260424170750.png | 444]]
	*Tractable* mean *Solvable in a reasonable amount of time.*
	*Intracble* mean *Unsolvable in a reasonable amount of time* because there are a $\infty$ amount of value.

Marginal likelihood is intractable the posterior is also intractable since the marginal likelihood is required in the calculation of the posterior nevertheless this simple relationship means that if we know one then we know the other given that the joint probability here is actually tractable
-> Shift our attention *from trying to directly calculate P of x to trying to approximate the posterior instead.*

*Variational Inference* is the process of *approximating some Target distribution* $p$ with an approximation $Q$. 
+ @ This mean the Distribution sample from $Q$ is approximate $p$. And to Approximate the Target $p_{\theta}$ we need a Objective function ie. KL-Divergence to compare if 2 distribution is similarto eachother.
![[Pasted image 20260424173729.png | 344]]
Objective function for Variational Inference is KL divergence (always $\geq{0}$).

+ $ The original KL is integral so we need to Simplified the KL to discrete using Expected Value.  
![[Pasted image 20260425164242.png]]
Note:
+ Expected Value *$E[X]=\sum_{i}x_{i}p_{i}$ is the Sum of $[$ each outcome $\times$ its probability $]$* -> that why it could be used to simplified integral.

move terms around, we see loglikelihood is the sum of KL-Divergence so $E_{q \space \phi}$ alone must be smaller or equal to $\log p_{\theta}(x)$
![[Pasted image 20260425164418.png]]
You could *alternatively derive* the ELBO using mathematical result called Jensen's inequality
![[Pasted image 20260425172957.png]]

Lower KL Divergence increase the tighness/closenes of this bound
![[Pasted image 20260425173053.png]]
we can think of the **K Divergence from P to Q as essentially the gap between the Elbow $q$ and the Actual Log Likelihood (target $p$)** so in other words a **lower K Divergence increases the tightness of this bound** now we can see from this picture that maximizing the elbow by *optimizing $\phi$ and $\theta$ will simultaneously do two things* one it will *maximize the log P of X* and two it will *minimize the the K Divergence from the true posterior P to the approximation Q.* 
	in other words both the generative model and the inference model are simultaneously *optimized all this without having to explicitly calculate P of X ($P_{\theta}(x)$) itself*

SO how do we optimized the ELBO of a large dataset itself -> OPTMIZATION FUNCTIOn -> Kernel Reperameterization Trick. 

Natural Approch: Stochastic GD.
![[Pasted image 20260425173545.png | 455]]
From the right term above let:
**Find the Gradient w.r.t $\theta$** -> Expand the fomula into integral -> bring the Gradient to the Integral -> the Integral is just the Expected Value itself -> Expected Value is easy to process bc we could use a simple procedure like  Naive Monte Carlo estimation sampling 
![[Pasted image 20260425173849.png | 666]]
Note: With respect to $\theta$ so remove the log q of $\phi$ 

In constract **Find the Gradient w.r.t $\phi$ is more tricky** -> Expand the Expectation like before -> Bring Gradient into the integral (replace the fomula with ELBO for short, shorter but still the same) -> Apply the product rule of differentiation to split into 2 integral -> We see that the 1st term is the Exptectation over Q (esay to estimated) but the 2nd term is not an Expectation so it cannot be estimated easily. 
![[Pasted image 20260425174453.png | 666]]
The solution is to replace Q with an equivalent distribution that is nto parameterize by $\phi$ using the reparameterization trick: 
1) Express $z$ by some function $g$. 
2) $\epsilon$ - sample from $p(\epsilon)$, remain constant during training ->$\phi$ influence $g$ deterministically. Externalized the randomness by transferring it from $z$ to $\epsilon$ 
![[Pasted image 20260425175237.png | 666]]

![[Pasted image 20260425175251.png | 666]]

![[Pasted image 20260425175334.png | 444]]

![[Pasted image 20260425175401.png | 666]]

![[Pasted image 20260425175416.png | 777]]

![[Pasted image 20260425175602.png | 666]]

Which Distribution to use. If multi-dim use Gaussian. If Binary like MNIST dataset use Bernoulli
![[Pasted image 20260425175702.png | 666]]

Prevent overfitting set $y_{\sigma}=1$ -> deter model on $z$
![[Pasted image 20260425175829.png]]

![[Pasted image 20260425175902.png | 666]]

![[Pasted image 20260425175924.png | 666]]

![[Pasted image 20260425180000.png | 666]]

prior of $z$ - unit of the Gaussian
Any value within the Distribution always a resonable output. ![[Pasted image 20260425180134.png | 666]]
VAEs force the latent space to follow a **Gaussian (Bell Curve)** distribution, which creates two key properties:
+ **Continuity:** If you move slightly in the latent space, the generated image changes smoothly (e.g., a face slowly begins to smile)
+ **Completeness:** Almost any point you pick in the central latent space will produce a sensible, realistic output

![[Pasted image 20260425180401.png | 666]]