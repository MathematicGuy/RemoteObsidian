**Hình thái của 1 từ**
![[maxresdefault.jpg]]

**Discourse:** luận văn (diễn tải sd nhiều từ/câu ẩn dụ, vd ngữ nghĩa trong toán học)

Phonetics and Phonelogy (âm học và  ngữ âm học)

**Morphology**: langauge with prefix, appear in Western languages.
Ex: re + vital + ize + ation (word allow prefix-postfix concatinate)
Ques: language have gender like german  ?

Semantics and Pragmatics: (Ngữ Nghĩa & Ngữ dụng )
Lexicon: list for each morpheme (From Phonology to Pragmatics)

**NLP - Unsupervised or Supervied ?**

---
TA: Anh Quân - 
# Chap 2: Coding Exercise

# Chap 3: Information Extraction
**Goals:** assign a probability to a sentence or ordered sequence of words. 
![[Pasted image 20250114101916.png]]
Related Task:
+ Probability of an upcoming word

Base on **Bayes's Theorem**, a **Language Model** is a **model that computes either of these** 
![[Pasted image 20250114102255.png]]
![[Pasted image 20250114102245.png]]
>Basically, the last $P(W_{n})$ represent the whole sentence i.e. $P(W)$ since the current word based on the previous words. 

![[Pasted image 20250114102629.png]]
$$P(its, water, is, so, transparent) = P(its) \times P(water | its) \times P(is|\text{its water}) \times P(so | \text{its water is}) \times  P(transparent | \text{its water is so})$$

**Continuous Space:** each vectors represent a words. 
(diff from on-hot and discrete vectors)

**How to estimate probabilites:** **use frequents** to count number of times each Events occurs. For intances, divide frequent of head to tail when flipping a coin.
![[Pasted image 20250114103531.png]]

+ ? What Bayes statistics rule I need to learn?

### Markov Assumption
-> approximate each component in the product.


*Calc many tokens at once instead of token by token like* (below) 
**Unigram:** xs của câu bằng xs của từ nhân vs nhau. (tính 1 từ cùng 1 lúc)
**Biagram:** probability of a word depend on its previous word. (tính 2 từ cùng 1 lúc)
![[Pasted image 20250114111833.png]]
**N-gram models:** like Unigram and Biagram but longer. (tính N từ cùng 1 lúc) 
+ N-grams: ***Token*** sequences of length ***N***
+ In contrast, this an insufficient model of language because language has *long-distance dependencies*.
**Example:**![[Pasted image 20250114105520.png]]

## Estimating N-gram Probabilities
#### Maximum Likelihood Estimate
$w_{i}$: word
>Divide numbers of times of the current word to the word after its. (Chia xác suất của từ tr'c với từ sau nó)
![[Pasted image 20250114105933.png]]
   Example:
![[Pasted image 20250114110226.png]]

#### Raw bigram counts
![[Pasted image 20250114110438.png]]
**Convert bigram to probabilities**
![[Pasted image 20250114110708.png]]

Word used in the Same Context -> Same Meaning (high chance) 
**Practical Issues**
+ do **Eveything in Log Space** -> avoid underflow (number close to zero), adding fast than multiplying. (Basically, **convert Multiply to Addition** using **log conversion**)

**LM Toolkits**: SRILM, KenLM.
note: Corpus (plural form: Corpora)

**Language Modeling**: Evaluation and Perplexity

### Evaluation (đánh giá) and Perplexity (bối rối) in LLM
>**LOW Perplexity is GOOD and HIGH Perplexity is BAD**

-> Assign higher prob to 'real' or 'frequently observed' sentences.
To evaluate, we **train** ours model **on trainning set** then **test on testing set and validation set**. Then **apply evaluation metric.**

#### Perplexity
Get highest P(sentence) on unseen test set.  Use hat invert $-\frac{1}{N}$ to calc Perplexity, so **the higher the Posibility the lower the Perplexity**. (Đơn giản là dùng nghịch đảo để tính Perplexity)
![[Pasted image 20250114115340.png]]
>The same apply
![[Pasted image 20250114115425.png]]

### Generalization and zeros
What if P(W) = 0 then we can't calc Perplexity -> need a Smoothing method. 
	Bigrams with zero probability mean that we will assign 0 probability to the test set!
	-> hence we cannot compute perplexity (can’t divide by 0)

## Smoothing: Add-one (Laplace) smoothing
>Lessen what we have more, increase what we have less. Hence smoothing -> Avoid 0
-> **Laplace smoothing**. (note: learn Laplace)
![[Pasted image 20250114120352.png]]
  (Näive Bayes) -> Use Add-1 estimate

Let find some more effective methods

## Interpolation, Backoff and Web-Scale LMs

**Sometimes it helps to use less context**. (If can't use Trigrams then use Bigram, if not Biagram then Unigram)
**Interpolation:** mix unigram, bigram, trigram (Nội suy)
#### Linear Interpolation
$\lambda$: super parameters
![[Pasted image 20250114121227.png]]
+ $ Each lamda is independent. And the sum of all $\lambda$ is 1 (**like weight but for probability**) 
+ ? why w have 1 hat and 1 sub-script

#### How to set $\lambda$ ?
**Development dataset** or **Held-Out dataset** -> **Use to adjust super parameters.** -> Then re-test on the test dataset to check the results. 

#### Unknown words: Open versus closed vocabulary tasks
**Out Of Vocabulary** = OOV words


#### Huge web-scale n-grams
entropy big -> big influence over the dataset -> if entropy low then prune them (cut them down like cutting branch from a tree)

#### Smoothing for Web-scale N-grams
**Stupid backoff**: No discounting, just use relative frequencies.
![[Pasted image 20250114121954.png]]
(Good for Transformer, the larger the dataset the better the model is)

### N-gram Smoothing Summary
Add-1 smoothing:
	OK for text categorization, not for language modeling
The most commonly used method:
	• Extended Interpolated Kneser-Ney
For very large N-grams like the Web:
	• Stupid backoff

### Kneser-Ney Smoothing
>This fomula help us to automatically if not work with unigram then change to biagram.

