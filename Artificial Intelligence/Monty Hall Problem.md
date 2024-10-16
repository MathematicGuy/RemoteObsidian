1 door is a car meaning the prob of each door is.
A: 1st door: 0.3333333333
However hypothetically the 1st door is a goat (i.e.  wrong guess), there is 
$1-0.3333333333=0.6666666667$ chances ours following guess is right.

Thus, each remainning door have prob of having a car is
	$\frac{0.6666666667}{2}=0.3333333334$ 


#### Analytical solution

This section is more advanced, you may skip it if you want to! 

Now, the game is:
- There are $n$ doors, and you must choose one door.
- Host opens $k$ doors and revealing goats.
- You may or may not change your previously chosen door.

The question is: is it always better to switch doors? Will it depend on $k$? 

To answer this question analyticaly, first define the following events:

$$E_i = \text{ the car is behind door i. In this case, } i = 1, \ldots, n.$$

Again, the $E_i$'s are independent from each other, because there is only $1$ car available.

Note that, since the Host never opens the same door the player chose and also never opens the winning door, there is an upper bound for $k$, which is $n-2$, so $$ 0 \leq k \leq n-2.$$
(this mean $k$  is the door the Host opened. Which is not containing the car and same door as the player opened (i.e. n-2))


Two facts can be assumed:

- The player chooses door $1$
- The host opens doors $2, \ldots, k+1$

This is because we can always rename the doors to get this result. For instance, if the player chooses door number $10$, we can rename it as door $1$ and door $1$ will become door $10$. This is just to avoid getting too complex on indices notations. In math terminology, it is usually said that we can do this *without loss of generality*, since it will not affect the final result. 

Now that there are $n$ doors, the probability that the car is behind door $1$ is $\frac{1}{n}$, i.e.,
$$P(E_1) = \frac{1}{n}.$$

By the complement rule, the probability that the car is **not** behind door $1$ is:
note: $E$ mean Event

$$P(E_1^c) = 1 - P(E_1) = 1 - \frac{1}{n} = \frac{n-1}{n}.$$

Note that $$E_1^c = E_2 \cup E_3 \cup \ldots \cup E_n.$$

There is a notation to simplify the right hand side equation above, we can write it as:

$$\bigcup_{i = 2}^{n} E_i.$$

This works in the same fashion as a summation symbol, but the opeartion being performed is set union.

So, we know that 

$$P\left(\bigcup_{i = 2}^{n} E_i\right) = \frac{n-1}{n}.$$

Now we can answer the question: What is the probability of winning, given that we switch doors?

Let's take a look on the following image:
![[Pasted image 20241016163354.png]]


If the player switches to a random available door, then they must choose one of the $k+2, k+3, \ldots, n-1, n$. Therefore, the probability of picking the car is:

The probability of **not picking the car** in door $1$ $\left(P(E_1^c) = \frac{n-1}{n}\right)$ times the probability of picking the car **now**, which is $\frac{1}{n-k-1}$ **(e.g. 2/3=0.6666667 in the previous example)** because this is the number of remaining doors. 


So, the final probability is given by (product of openning 1st door and after openning the 1st door (i.e. $-1$) and the host doors (i.e. $k$))
$$P(win | switch) = \frac{n-1}{n} \cdot \frac{1}{n-k-1}.$$
It can be rewriten in the following manner:

$$P(win | switch) = \frac{n-1}{n} \cdot \frac{1}{n-k-1} = \frac{1}{n} \cdot \frac{n-1}{n-k-1} \geq \frac{1}{n} = P(E_1) = P(win | not\ switch).$$

And the equality only holds when $k = 0$. This means that the host does not open any door.

Therefore, **it is always better to switch doors**. This may sound counterintuitive at first, but think that switching doors you are using the **new piece of information** that the host gave you, whereas if you choose not to switch, you will be ignoring this new information.

