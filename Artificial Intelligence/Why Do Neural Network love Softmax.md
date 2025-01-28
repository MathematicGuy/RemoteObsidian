### Input Values
As you already know, the sum of all distribute probs for each class in softmax is 1. Thus when 1 value (out of 4) increase (in sigmoid path) other (4) decrease (in sigmoid path). Since the total are all the height (each value) added together and each value get normalize by the total height, they (values) actually don't change at all. 
![[Pasted image 20250121135457.png]]


Temperature: build base on softmax -> help to change the randomness of the outputs.  
![[Pasted image 20250121134829.png]]
If the more equally distribute the probs are the more random its become, whereas the more spread out the probs are the more deterministic it will be, thus less random.
![[Pasted image 20250121135042.png]]

### Output Probability
If we want to see all the output probabilities look like over the entire inputs space. Let try to get a better idea of how the inputs space to the softmax function gets transformed into probabilities. 

### Temperature
Like energy with more temperature, the more accessible it will be. In softmax with more temperature the more possibility can happened. 
![[Pasted image 20250121143420.png]]

**Softmax - chosing the maximum softly**
Image we have a sentence "A cat is chasing a...." and some words appear with their own probability. By using **temperature** we can **re-distribute the probability** to be **more deterministics or more random** which allow the language model to be more creative since more word can be chosen out of the pocket.
	Note: If a word have probs close to 1 while other words close to 0. It mean the func is hard maximum.
![[Pasted image 20250121143430.png]]
![[Pasted image 20250121143525.png]]
>Kind of like human huh ? When ones get angry, think about that. 

---
![[Pasted image 20250121144603.png]]

 Firsty, Softmax map score to positive value![[Pasted image 20250121144815.png]]


