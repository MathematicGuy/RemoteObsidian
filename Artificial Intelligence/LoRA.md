+ @ LLM have a lot of params, researcher found LLM can learn a new task efficient by just update a small set of weight. LoRA create a new set of weight and update them efficiently while the *original weight performed forward pass only.*
	reference: 
	+ [LORA: LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS](https://arxiv.org/pdf/2106.09685)
	+ [What is LoRA Explained ?](https://www.youtube.com/watch?v=KEv-F5UkhxU)

In dense neural network, each model weight have its own respective gradient. If we want to finetune a LLM (1B for example) for a specific task, we would need to train the whole 1B params -> too costly and time consuming. 

![[Pasted image 20260213172438.png | 344]]

While LLM have a large intrinsic dimension (a lot of parameters), the actual mathematical space or "degree of freedom" required to learn a new task is much smallar (the intrinsic dimension)

Research shows that the pre-trained LLM can learn efficiently despite random projection to a smaller subspace (ie. another set of initialize weight)


Instead of modified all the model weights - we freeze the original Weight and add another set of weight for update having same size as the original.
+ ? Note: Finetuned Weights initialize with random distribution (e.g. random Gaussian noise $A \sim \mathcal{N}(0, \sigma^2)$ or He initialization). 

For a pre-trained weight matrix $W_{0} \in \mathbb{R}^{d\times k}$
LoRA update by representing the latter $W_{0}$ with low-rank decomposition (ie. phân rã ma trận, like simplified): $$W_{0} + \Delta W = W_{0} + BA$$where $B \in \mathbb{R}^{d \times r}$ and $A \in \mathbb{R}^{r \times k}$  with rank $r \ll min(d, k)$ ($\ll$ mean much less than, so small tha tit can be ignore)

While training $W_{0}$ is frozen and does not receive gradient update, only $\Delta W = BA$ are trainable. Note that both $W_{0}$ and $\Delta W$ received the same input. For $h=W_{0}x$ the forward pass is:
$$h = W_{0}x + \Delta Wx = W_{0}x + BAx$$

![[Pasted image 20260213172531.png | 333]]


![[Pasted image 20260213173016.png | 444]]

r as rank. Simply *r is the the number of B and A* vectors you took for multiplication. If $r = 2$ then that 2 cols $\times$ 2 rows.     
![[Pasted image 20260213174052.png]]
How to choose Matrix rank: https://chatgpt.com/c/698f0e20-9550-8323-9027-1b0fb395f8bf
	Choose rank base on Task Novelty, the harder the task the higher the rank. 

+ $ The right rank is the **smallest one that stops underfitting**.
$$W_{eff} = W + \frac{\alpha}{r}AB$$

## Compare LoRA with Existing Solution
**PEFT**
