Note: _Preliminary: The process of finding out what there is to find out_. 
**Context**
*In Classical ML*, all training data arive at the same time.
*In Incremental Learining (IL),* training data come in sequence or in number of steps, and the distribution of data shift/ overtime as new data arrived (like real world stream of continous data).
<-> IL is not i.i.d (independent and Identically Distribution - Độc lập và phân phối đồng nhất). *violation of the IID assumption is what leads* to "Catastrophic Forgetting (CF)".
-> Solve CF allow model to continously learn new data no matter their distribution is. 

![[Pasted image 20260112142639.png]]
**Class-Incremental Learning**
(a) in [[class-incremental learning]], an algorithm must incrementally learn a set of clearly distinguishable tasks.
	training data come in sequence instances with *each Task doens't contain overlapping class $Y_{b} \cap Y_{b}' = \varnothing$.* After each task, the trained model is evaluated over all seen classes in task $b$ $(Y_{b} = Y_{1} \cup \dots Y_{b})$  CILM aim to fit a model $f(x): X \to Y_{b}$ over all class b. 
	Note: If $Y_{b} \cap Y_{b}' \neq \varnothing$ then it Blurry CIL where old classes emerge in new tasks, this allow model to revision old knowledge ie. classes, which weaken the learning difficulty. 
	


(b) in task-incremental learning, an algorithm must incrementally learn to distinguish between a growing number of objects or classes. 
	

(c) in domain-incremental learning, an algorithm must learn the same kind of problem but in different contexts.
-> oncentrates on the scenario with concept drift or distribution change [10], where new tasks contain instances from different domains but with the same label space. (ie. class same Guy class, but 1 in Anime domain and 1 in Cartoon domain)

Distinguish each Class/Task/Domain Incremental Learning
![[Pasted image 20260112143758.png | 388]]


| Scenario                    | Intuitive description                                  | Mapping to learn      |
| --------------------------- | ------------------------------------------------------ | --------------------- |
| Task-incremental learning   | Sequentially learn to solve a number of distinct tasks | $f: X \times C \to y$ |
| Domain-incremental learning | Learn to solve the same problem in different contexts  | $f: X \to y$          |
| Class-incremental learning  | Discriminate between incrementally observed classes    | $f: X \to C \times y$ |
Note: $X$ is the input sapce, $y$ is the within-context output space and $C$ is the context space. 
