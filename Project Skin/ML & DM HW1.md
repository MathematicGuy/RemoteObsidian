![[Pasted image 20240617224944.png]]
![[Pasted image 20240617224920.png]]

To solve this problem using Naive Bayes classification, we'll follow these steps:

1. **Calculate the prior probabilities** for each class (play = yes, play = no).
2. **Calculate the likelihood** of each feature given each class.
3. **Use Bayes' Theorem** to combine these probabilities and find the posterior probability for each class.
4. **Choose the class** with the highest posterior probability.

Let's break it down step-by-step:

### 1. Calculate Prior Probabilities

The prior probability is the proportion of each class in the dataset.

- **P(play = yes)** = (Number of "yes" instances) / (Total number of instances)
- **P(play = no)** = (Number of "no" instances) / (Total number of instances)

From the table:

- Number of "yes" instances = 9
- Number of "no" instances = 5
- Total instances = 14

So, P(play=yes)=914≈0.64P(play = yes) = \frac{9}{14} \approx 0.64P(play=yes)=149​≈0.64 P(play=no)=514≈0.36P(play = no) = \frac{5}{14} \approx 0.36P(play=no)=145​≈0.36

### 2. Calculate Likelihoods

For each feature, we'll calculate the likelihood for each class.

#### For outlook = overcast:

- P(outlook = overcast | play = yes)
- P(outlook = overcast | play = no)

From the table:

- Overcast and yes = 4
- Total yes = 9
- Overcast and no = 0
- Total no = 5

So, P(outlook=overcast∣play=yes)=49≈0.44P(outlook = overcast | play = yes) = \frac{4}{9} \approx 0.44P(outlook=overcast∣play=yes)=94​≈0.44 P(outlook=overcast∣play=no)=05=0P(outlook = overcast | play = no) = \frac{0}{5} = 0P(outlook=overcast∣play=no)=50​=0

#### For temperature = 60 (using Gaussian distribution for continuous data):

- P(temperature = 60 | play = yes)
- P(temperature = 60 | play = no)

We need the mean (μ) and standard deviation (σ) for temperature when play = yes and no.

For play = yes: μyes=(83+70+68+65+64+72+69+75+75)9≈71.22\mu_{\text{yes}} = \frac{(83 + 70 + 68 + 65 + 64 + 72 + 69 + 75 + 75)}{9} \approx 71.22μyes​=9(83+70+68+65+64+72+69+75+75)​≈71.22 σyes=∑(x−μ)2N≈6.59\sigma_{\text{yes}} = \sqrt{\frac{\sum (x - \mu)^2}{N}} \approx 6.59σyes​=N∑(x−μ)2​


















----
**Data Archive**

| *outlook* | *temperature* | *humidity* | *windy* | *play* |
| --------- | ------------- | ---------- | ------- | ------ |
| sunny     | 85            | 85         | FALSE   | no     |
| sunny     | 80            | 90         | TRUE    | no     |
| overcast  | 83            | 86         | FALSE   | yes    |
| rainy     | 70            | 96         | FALSE   | yes    |
| rainy     | 68            | 80         | FALSE   | yes    |
| rainy     | 65            | 70         | TRUE    | no     |
| overcast  | 64            | 65         | TRUE    | yes    |
| sunny     | 72            | 95         | FALSE   | no     |
| sunny     | 69            | 70         | FALSE   | yes    |
| rainy     | 75            | 80         | FALSE   | yes    |
| sunny     | 75            | 70         | TRUE    | yes    |
| overcast  | 72            | 90         | TRUE    | yes    |
| overcast  | 81            | 75         | FALSE   | yes    |
| rainy     | 71            | 91         | TRUE    | no     |


| *Feature*   | *Class* | *Mean (μ)* | *Std Dev (σ)* |
| ----------- | ------- | ---------- | ------------- |
| Temperature | Yes     | 72.78      | 8.65          |
| Temperature | No      | 7          | 6.56          |
| Humidity    | Yes     | 81.67      | 9.94          |
| Humidity    | No      | 8          | 8.54          |

