Score: HW (15 - 25%) + Midterm (20%) QA/Multiple-Choice + Final Project (60%)
3 bài - mỗi bài bao gồm code (lấy từ bài tập đã học bắt đầu từ tuần 1) + báo cáo (thuật toán cài đặt, optinal: thuật toán mở rộng) 

---

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

---
### Practice: Language Modeling
**Content:**
	**Language modeling**
		Calculate n-gram
		Conditional probability
		Smoothing techniques
	**Basic decoding**
		Greedy search
		Beam search
		Random sampling
	**Perplexity**

---
## Text Classification 

**Quiz: What the different between Machine Learning and Deep Learning ?**
Deep Learning -> Choose Features (i.e. Feature Engineering) by itself.
Machine Learning -> Human have to Engineer Features Manually.


HW: Use skitlearn for Naive Bayes problem

---
# Word Embedding
function word (từ chức năng): a, the, thì, mà, con, cái, thằng, fetc..
contents word (từ quan trọng, có ý nghĩa): 


**2 kinds of embeddings:**
1) tf-idf (Term Frequency - Inverse Document Frequency)
	but frequency doesn't show the real word importantness, overly frequent words like *the, it* or *they* are not very informative about the context. It's a paradox, how can we balance these 2 conflicts and constraints.
	-> 
2) Word2vec
---
### Code Explaination 
[[Trigram_model]]
[[Language_Modeling_with_Trigrams_explain]]
[[Sentiment Analysis using LSTM]]
[[NLTK_&_Spacy_practice]]

+ **drive .ipynb:** https://drive.google.com/file/d/1o0Rf-AvhuqNcQynUi4UVpaQi-o_wyjLH/view 
+ [Sentiment Analysis on IMDB Movie Reviews: A Beginner’s Guide](https://medium.com/@AMustafa4983/sentiment-analysis-on-imdb-movie-reviews-a-beginners-guide-d5136ec74e56)
+ [Sentimen Analysis Video Turtorial](https://www.youtube.com/watch?v=C5wRAlLuuY0)

---
# Seq2seq modal and application for machine translation

Lịch sử Machine Translation
Rule base -> Example base machine translation (EBMT) -> Statistical Base (Syntax base SMT, Hiearchical base SMT) -> Neural Machine (Attention base, Transformaer)

What is NMT (Neural Machine Translation)
NMT use single neural network (to avoid probabation errors - stack of errors)

Encoder - Decoder Framwork
note: log(0 -> 1) âm 

Greedy Decoding (can't undo decision) -> better option: Beam Search (a search algo) to explore several *hypotheses* and select the best one. 

### Advantage of NMT
Compare to SMT, NMT has many advantages:
+ Better performance: more fluent, better use of context and phrase similarites.
 
 

---

[[Sequence to sequence (seq2seq)]]
### Schedule
1. Transformer (4/3)
2. Practice [Code Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html) x 2 (6/30 + 11/3)
3. Review of Project (13/3)
4. LLMs (ChatGPT) (10/3)
5. Practice
6. Prompting + Practice
7. Review Project 

---
 [Beam Search](https://machinelearningmastery.com/beam-search-decoder-natural-language-processing/)
# Large Language Model

### From Chat-GPT to GPT-2 to GPT-3

