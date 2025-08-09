## Chapter 1: Basic Statistic Definition
What is probability ? probability is likelihood (khả năng xảy ra) of sth to happened, but what is likelihood. 

In statistic, we define probability as a measurement of how likely something to happend heuristically (trực giác), and likelihood describe how likely something to happened base on what actually happend when tested.   
![[Pasted image 20250710164357.png | 500]]

```ad-question
**What the different between Probability and Likelihood ?**

**Probability:** Assume how likely sth to happend (i.e. **prob WITHOUT TESTED**)
+ $ Suppose you have an **unbiased** coin. If you flip the coin, the probability of getting head and a tail is equal, which is 0.5. 
+ ? **When calculating the probability of coin getting heads, you assume that P(head) = 0.5**

|

**Likelihood:** Calc the probability sth actually happened (i.e. **prob AFTER TESTED**)
+ $ However, when calculating the likelihood, you are **trying to find if the model parameter (p = 0.5) is correctly specified or not.**
+ ? The **fact that a coin only lands on heads 14 times out of 50 makes you highly suspicious that the true probability of a coin landing on heads on a given toss is p = 0.5.**
```

**Sample Space - $\Omega$:** is a set of all the possible outcomes of the experiment. Denoted as $\Omega$.
	For example, two successive coin tosses have a sample space of `{hh, tt, ht, th}`, where `h` denotes “heads” and `t` denotes “tails”.
	
**Even $E$:**  is a subset of the sample space $\Omega$, we see **a Event** **as a single possible outcome** within the sample space. For example, `hh` and `tt` is 2 Event within the Sample Space, this can be annotate as $E \in \Omega$     
	
**Even Space $A$** with $E$ as an Event, we call the collection of E (many Events) as a Even Space $A$. Because $E \in \Omega \to A \in \Omega$,. 

**Probaility $P$** with each event $A \in \Omega$, we associate (gán) a number P(A) that measure a degree of belief that the event will occur. P(A) called the probability of A. 

## Chapter 2: Counting Technique (Tổ Hợp và Chỉnh Hợp)


## Chapter 3: Các Quy Tắc Xác Suất Cơ Bản
**Independet Event:** outcome of 1 event doesn't affect outcome of another event.
**Dependent Event:** outcome of 1 event affect outcome of another event. 
Note: Both addition and product can ahve independence or dependent event. 

**When to Use Sum: Addition Rule** 
When you want to **find the probability of either one event OR another event occuring**. (x/s của 1 trong 2 events)

**When to Use Multiply: Prouduct Rule** 
**2 or more events happenning at the same time.** 

## Chapter 4: Xác Suất Có Điều Kiện và Biến Cố Phụ Thuộc:
### Conditional Probability
![[Pasted image 20250714163106.png# left | 250]]
Given B happend first, then A happend mean ONLY choose parts of A that happend given B. We then divided the "intersection between A and B" to B because it how we calculate probability, in other word, out of all events in B, what is the probability A and B happend.  

### Conditional Probability Example
2 Sequential event -> multiply
![[Pasted image 20250714161456.png]]
The reason P(A2 | A1) after P(A1) is because P(A1) had happened. Problem of A standing first annotate its happened first. This rule repeat for $A_n$. 
![[Pasted image 20250714161728.png]]
Say that we only open the door on the 3rd attempt, this mean attempt 1st and 2nd fail and the 2nd attempt is depend on the 1st attempt. 
-> $P(\bar{A_{1}})$ then $P(\bar{A_{2}} | \bar{A_{1}})$ (attempt 2 not success given attempt 1 not success) then $P(A_{3} | \bar{A_{1}} \bar{A_{2}})$ all multiply to each other to describe sequence of events. 
<-> $P(\bar{A_{1}} \bar{A_{2}} A_{3})$ = $P(\bar{A_{1}}).P(\bar{A_{2}} | \bar{A_{1}}).P(A_{3} | \bar{A_{1}} \bar{A_{2}})$
From here we just plug in the numbers.
 
![[Pasted image 20250714162930.png|600]]


### Bayes Theorem 
**Independent events**
Do event A affect event B ? This mean if we only want to find Prob of B given B so then $P(A|B) = P(B)$  
+ ? For example, A single fair dice is rolled. Let A={4} and B={2, 4, 6} mean B can either be 2 or 4 or 6. Are A and B independent ?
To check if A and B is independent ? We just need to multiply them so see if their probability really intersect. 

Because 4 is in {2,4,6}, we know **In Theory for event A and B both happened the dice must be 4** because 4 exist in both A and B, **in other word P(A).P(B) = P(4)** = 1/6 (prob equal the intersection part).  
**But In Practice (real life), let see if P(A).P(B) really = P(4)** 
With P(A) = 1/6, P(B) = 1/2 (because that the chance of B to happened), P(A).P(B) = 1/12. 
Since 1/12 $\neq$ 1/6, Events A and B is not independent. 


**Total Probability Theorem**
Happened in parallel (event happened independetly) -> Addition
Happened in sequence (event A afect event B) -> Multiply
![[Pasted image 20250714165815.png]]
Step 1: choose bag (3 independent cases)
Step 2: choose red marble from that bag. (depend on which bag get chosen i.e. prob of the bag which is 1/3 since there're 3 bags)
 $\to .75 \times \frac{1}{3} + .60 \times \frac{1}{3} + .45 \times \frac{1}{3} = \frac{1}{3} \times (.75 + .60 + .45) = \frac{P_{1} + P_{2} + P_{3}}{3}$ 
 + ! Warning: this is a simple way to calculate average of the probability, in realife prob of choosing red might be high because of bias, each P would have their own weight as bag's probability. e.g. $P(red) = \alpha P_{1} + \alpha P_{2} + \alpha P_{3}$ (This call Weighted Average, use when each cases have a diff probability)

![[Pasted image 20250714170609.png]]
A1 is bag 1
P(H1) is the prob of H having red marble, given that A1 get chosen where A1 is the prob of bag 1 getting chosen and H is the prob space where of red marble.  
**Note: $$P(H_{1}, H_{2}, H_{3} | C) = P(H_{1}|C).P(H_{2}|C).P(H_{3}|C)$$ 

## Baye's Rule
### Bernoulli Naive Bayes for Single Feature
Probability of a feasible even / Probability for all event to happend. 
$$P(C|X=x) = \frac{P(C).P(X|C)}{P(X)}$$
where 
+ $C$ is the Class and X is the Feature
+ $P(X)$ probability of a Features to happend 
+ $P(X|C)$ probability of the Feature to happend given the Class
+ $P(C)$ probability of all Conditional Event that is that class. e.g. $= P(C)P(X_{1}|C) + P(C)P(X_{2}|C)$

![[Pasted image 20250729090000.png]]
$P(R=r|S=s)=\frac{P(S).P(S|R)}{P(R)}$
$P(S) = P(R_{1}).P(R_{1}|S) + P(R_{2}).P(R_{2}|S)$
$P(R_{1}).P(R_{1}|S) = \frac{3}{6}.\frac{1}{3}=\frac{1}{6}$
$P(R_{2}).P(R_{2}|S) = \frac{3}{6}.\frac{2}{3}=\frac{1}{3}$
$P(S) = \frac{1}{2}$

$$P(R_{1}=Fail|S=Studied)=\frac{P(R_{1}).P(R_{1}|S)}{P(S)} = \frac{1}{3}$$

$$P(R_{2}=Pass|S=Studied)=\frac{P(R_{2}).P(R_{2}|S)}{P(S)}=\frac{2}{3}$$
note: $a \propto b$ mean as a increase, b increaase 
```ad-seealso
In Summary, P(C=c|X=x) is the probability that c happend divive to "every event of $C$ given X" where c is a class inside Class.  
```

### Bernoulli Naive Bayes for Multiple Feature
![[Pasted image 20250729100700.png|550]]

### Gaussian Naive Bayes Classifier
[gaussian naive bayes from scratch in python](https://youtu.be/AqW3aPSPIhc?si=LOZLH3Uz4ojjp7uG)
+ ? Use Gaussian Naive Bayes instead of Basic Conditional Probability
![[Pasted image 20250729102212.png|555]]


Một lập trình viên có thể debug thành công một đoạn mã lỗi trong 2 bước như sau:
+ Nếu họ tìm đúng module đầu tiên, xác suất sửa lỗi là 80%.
+ Nếu họ chọn sai module đầu tiên, họ có thể thử lại một lần (tổng cộng 2 lần). Xác suất tìm đúng trong lần thứ hai là 60%. 
	
	Biết rằng xác suất chọn đúng module ngay từ đầu là 40%.
	Hỏi xác suất để lập trình viên sửa được lỗi sau 2 lần thử là bao nhiêu?

**Naive Bayes:** $$P(x_{1},x_{2},\dots,xn|lass)=P(x_{1}|class).P(x_{2}|class)\dots P(x_{n}|class)$$-> xác suất xảy ra của mẫu (tập hợp các đặc trưng x1,x2,...,xn) với điều kiện biết trước class.
+ ? e.g. **Với một mẫu** mới có Length = 5.5 và Width = 3.0, hãy tính xác suất P(Class 1 | Length=5.5, Width=3.0) sử dụng Gaussian Naive Bayes.

**Bayes Theorem:** $$P(class|x)=\frac{P(x)P(x|class)}{P(class)}$$--> xác suất để một sample thuộc về class nào đó sau khi đã quan sát đặc trưng x
+ ? e.g. Cho trước 3 features là Confidence, Studied, Sick thuộc về 2 class Pass và Fail. Hãy dự đoán Class của quan sát mới P(yes, yes, yes). Note: tính Posterior của P(pass) và P(fail) rồi nhân xác suất từng Class vs P(yes, yes, yes) để xem class nào có khả năng xảy ra cao hơn.  
![[Pasted image 20250729145950.png]]

----
Đề thi sẽ có khoảng **53 câu** chia đều cho các **kiến thức ở** những **buổi thứ 3, thứ 4, thứ 6** **và chủ nhật ở module 2.** Các câu hỏi **phần lớn yêu cầu các tính tay cho các bài toán xác suất** và **cuối bài sẽ có khoảng 6-7 câu** yêu cầu **code**.


