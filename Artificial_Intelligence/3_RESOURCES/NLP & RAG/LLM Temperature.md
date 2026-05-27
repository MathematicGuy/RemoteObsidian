Basically **Softmax** but logit $z_{i}$ divided by $T$:  $$\frac{z_{i}}{T}$$ where $T$ is the **Temperature**. Softmax fomula with temperature:
$$P_{i} = \frac{e^{z_{j} / T}}{\sum^{K}_{j=1}e^{z_{j} / T}}$$
With logits computed from the last layer are `[1, 3]`
+ When $T=1$: equivilent to no temperature, or softmax probabilities are `[0.12, 0.88]` 
+ When $T = 0.5 < 1$:  the probabilities are `[0.02, 0.98]`, so output become more bias toward higher value.
+ When $T = 2 > 1$: the probabilties are `[0.27, 0.73]`, the model seem more balancely distributed. 
+ $ The **higher temperature is, the Less likely model is going to pick the dominance** option (value with highest logit), making model's output more creative but potentially less coherent. The **lower the temperature, the more Likely the model to pick the most dominance value** -> Model become more consistent but more boring.![[Pasted image 20250326153327.png]]
+ ? Base on your need, temperature of 0.7 is recommended for creative use cases, as it creativity and determinism. But oft you should experiment to find which value suit most.

A language model work with vocab size of 100,000. Which mean the probabilities of many token can be too small to be represent. Small number might be rounded down to 0, log scale help reduce this problem.  
![[Pasted image 20250326155959.png]]


**Re-Explain:** https://huyenchip.com/2024/01/16/sampling.html#temperature