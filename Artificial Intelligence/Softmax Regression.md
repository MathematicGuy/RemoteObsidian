**Openning:** Introduce problem we're trying to solve (Name/Type - "Classified multiple digit"/"Supervised Learning) -> Intro the main Method (To find the right ML Algorithm / Optimzation Func)

explain simple term:
	 i item / sample
	 k class

matrix - code thing more efficiently (re-write the line function f(x) into 
matrix form ->  simplified it -> explain)

**Main Part - Loss func #1: classification error** (explain introducted fomula every part of the way)
Need a optimization function -> annotated with a hypothesis func $h_{\theta}(X)$ (note: this func can be anything as long as it satisfied the mathematic requirements)

explain error loss: from input to output. 
+ ? 0 if $argmax_{i} \space h_{i}(x)$ - loss equal to 0 at maximum value of $h_i$ is equal to $y$. where $argmax_{i}$ mean at maximum index $i$
![[Pasted image 20251129140814.png]]
+ ! Not differentiable (ie. khả vi mean the func is smooth enough to calculate derivative bc the rate of change only changed if it not constant, unsmooth surface like a line only allow 1 rate of change, like a rock sliding down a slide in space) -> Can't change -> Bad for optimization. 

**Loss function #2: softmax / cross-entropy loss**
Translate math function into human language for flexible understanding. 
![[Pasted image 20251129142921.png]]
But make sure to explain term on the run. (e.g. what normalize, norm & exponential mean) 
+ **Function Goals:** to convert every options/classes into probability for determine which options are more likely to happened given that the plausability of 1 option decrease the plausability of other option. 
+ Use exponential because there no such thing as negative chance of winining or in term of probability.
+ $ To normalize is to re-scale the value into a range of value like from 0 to 1 so calculation are easier and calculatable bc all value of $z$ are converted into a probability distribution. (see [[Why Do Neural Network love Softmax]] to understand more) 
	+ ? ie. $exp(h_i(x))$ like rescaling the photo within a specific frame by dividing the function by its norm which is the Whole of frame (total size of the frame). Likewise, to normalize a function at index i-th is to divide its by the sum of the function for all index i-th (total size of the function)  $\frac{1}{\sum^{k}_{j=1}\exp(h_{j}(x))}$, note that j-th is a dummy index that represent for all index i-th while i-th represent a specific class.  
	
+ Softmax only account for the True (ie. class 1 in 0 or 1) -> $y$ always = 1$$loss = l_{ce}(h(x), y) = -[(1-y)\log(1-y) + y\log(y)]$$so the Loglikelihood from Logistic Regression become $-\log p(y)$ for every $y$.

Because softmax convert *all options/class into a probability distirbution* where the increase in *prob of 1 class decrease the prob of every other class* equally. Method to calc *Loss for softmax* is pretty easy (the lower the loss the better), we just need to *substract True option's $-h_{y}(x)$ probability by the False options's probability $\log \sum^k_{j=1}\exp(h_{j}(x))$*.  
![[Pasted image 20251129160835.png]]




---


### Logistic Regression Cost Function to Softmax Cost Function Note
![[Pasted image 20251129165222.png]]
+ $ $1 \{y^{(i)}=k\}$ represent the TRUE class by returning 1 while returning 0 for False. This way, only the TRUE class kept during matrix multiplication when calculating Loss. 
+ ? $1 \{y^{(i)}=k\}$ term mean if the True Class $y^{(i)}$ is equal to the current class $k$ then return 1.  
We use ${y^{(i)} = k}$ to identify class so we can accounted both class 0 and 1 flexibly with k represent both class 0 and 1, and $y^{(i)}$ represent the True class. Yes, we're using for loop to eliminate False class with 0 on this one. 
![[Pasted image 20251129170048.png]]
+ $ This way, $\{y^{(i)}=k\}$ term help to *eliminate all the undesirable class by multiply them with 0 while keeping only the True class by multiply them with 1.* 

Apply this same principle to Softmax, which not limited to binary class (0 and 1) but multiple class $K$, we could create a function that eliminate every others class while keeping only the True class for Loss.
![[Pasted image 20251129170451.png]]

Note: 
![[Pasted image 20251129171117.png]]


**Softmax Derivative**
![[Pasted image 20251129170921.png]]
