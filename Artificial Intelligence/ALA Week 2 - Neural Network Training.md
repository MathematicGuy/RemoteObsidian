**Basic of Neural Network**
![[Pasted image 20241104090334.png]]

### Alternative Functions
**ReLU (Rectified Linear Unit)**
If $z < 0 \to g(z)$ is 0, if $z >=0 \to g(z)$ is $z$

**Examples of Activation Functions**
+ ? Each nodes have a activation function that take inputs and output 1 or many values. 
+ ? Keep in mind that Linear Activation function $y = ax+b$ is like no activation function.
![[Pasted image 20241104091047.png]]

+ $ ReLU is the most common and used activation function for regression problem.
	![[Pasted image 20241104091722.png]]
Implement using tensor flow
![[Pasted image 20241104091757.png]]

# Multiclass Classification
Classify more than 2 categories.
![[Pasted image 20241104093424.png]]

### Softmax (regression algorithm)
+ ? **Softmax regression is a generalization of logistic regression**, which is a **binary classification algorithm to the multiclass classification contexts.**

**For Logistic regression**, if the possibility of y=1 is 0.71 then prob of y=0 is 0.29 since their sum are 1 (prob of 2 events). 
![[Pasted image 20241104093846.png]]
For Softmax regression, we see each output as a possibility by dividing each input $e^n$ by the sum of all $e^{n}(n \in \mathbb{N})$ existed. And the sum of all activations is 1 since they represent the prob of each outcome.  
![[Pasted image 20241104094628.png]]
We can re-write the fomula for each activation $j$ as:
![[Pasted image 20241104095133.png]]
+ $ If you was to use **softmax regression for 2 possible output value**, you would get the **same result as logistic regression.** (we can say that softmax come from linear regression)

The cross-entropy loss function, have $\log (a_{1})$ and $\log(1-a_{1})$ represent success event $a_{1}$and un-success event $a_{2} =1-a_{1}$. So if I was calculating event $a_{1}$ ($y=1)$ then y must be 0, replace $y=0$ to the loss function and 
![[Pasted image 20241104095901.png]]
**the loss function can be simplified as** for $a_{n}$
$$loss = -y\log(a_{1})$$ ![[Pasted image 20241104100723.png]]
+ $ For $y=j$, the smaller $a_{j}$ is the larger the loss. Therefor we would want to maximize $a_{j}$
+ ? Notice that in this **loss function y in each training example** can **take on only one value**. e.g. **if y was equal to 2, you end up computing $-\log(a_{2})$,** but **not any of the other $-\log(a_{1})$** or the other terms here.

For each $z$ we need to calc each $a$ acoordingly.
![[Pasted image 20241104103003.png]]

**MNIST with Softmax**
![[Pasted image 20241104103701.png]]
(There a version better than the code above, show below)

### Improved implementation of softmax
**Numerical Roundoff Errors (on computer)**
![[Pasted image 20241104103944.png]]
We need a **more numerically accurate implementation of Logistic Loss:**
![[Pasted image 20241104105224.png]]
+ ? If use we use a as the intermediate value, it could lead to some small numerical error. 
+ $ But if we were to **use $\frac{1}{1+e^{-z}}$ explicitly** then tensorflow can rearrange the expression (loss function) and **come up with a more numerically accurate way to compute loss function.** We could achieve this by adding `(from_logits=True)`

**More numerically accurate implementation of Softmax**
+ ? **Intuition:"** $e^z$ scale along with z, so if z small then $e^z$ is small. **By rearranging terms**, TensorFlow can **avoid some of these very small or very large numbers and therefore come up with more actress computation** for the loss function. ![[Pasted image 20241104110010.png]]

+ @ **Summary:** **instead of using $a_{n}$** and passing with through loss function, **add them  explicitly to the loss function**. We implement this technique by adding `from_logits=True` 

![[Pasted image 20241104112432.png]]
### Additional NN Concept
**Adam (Adaptive Moment estimation)** 
>If the learning rate are **too small when each step heading to the same direction then  "Adam Algorithm" will make it take bigger step** and **get to the minimum faster**. And if the **step are too big and bouncing in many direction (i.e. oscillating) then "Adam" can also make each step smaller.** 
+ ? Each parameter have a different learning rate ![[Pasted image 20241104114443.png]]
![[Pasted image 20241104114539.png]]

**Softmax Costfunction Summary**
![[Pasted image 20241104115727.png]]
- Here:
    - $z_j^{(i)}$​ is the unnormalized logit for the $j$-th class of the $i$-th example.
    - $\sum_{k=1}^N e^{z_k^{(i)}}$​ is the denominator of the softmax function, ensuring the outputs sum to one (probability distribution).
    
- The **outer summation iterates over all examples,** and the **inner summation iterates over all classes for each example**. The indicator function ensures that only the log probability for the target class is included in the loss for each example.


**TensorFlow Implement**
![[Pasted image 20241104114606.png]]
note: try and test diff learning to see which one is the best.

back propagation
![[Pasted image 20241104121103.png]]